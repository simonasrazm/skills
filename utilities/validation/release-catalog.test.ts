import { afterEach, expect, test } from 'bun:test';
import { mkdtemp, mkdir, rm, writeFile } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { validateRelease } from './release-catalog';
const roots: string[] = [];
afterEach(async () => { await Promise.all(roots.splice(0).map(root => rm(root, { recursive: true }))); });
async function fixture(change: (catalog: any, plugin: any) => void = () => {}) {
  const root = await mkdtemp(join(tmpdir(), 'release-catalog-')); roots.push(root);
  const catalog = { schemaVersion: 2, version: '1.2.0', releaseUnit: 'collection',
    skills: [{ name: 'example', path: 'skills/example', maturity: 'stable', releaseUnit: 'example', version: '1.0.0' }],
    releaseUnits: { example: { version: '1.0.0', members: ['example'] } } };
  const plugin = { version: '1.2.0', skills: ['./skills/example'] }; change(catalog, plugin);
  await mkdir(join(root, '.claude-plugin'), { recursive: true });
  await mkdir(join(root, 'skills/example'), { recursive: true });
  await writeFile(join(root, 'skills.catalog.json'), JSON.stringify(catalog));
  await writeFile(join(root, '.claude-plugin/plugin.json'), JSON.stringify(plugin));
  await writeFile(join(root, 'skills/example/SKILL.md'), '---\nname: example\n---\n');
  return root;
}
test('accepts a release unrelated to any particular skill family', async () => {
  expect(await validateRelease(await fixture())).toMatchObject({ skills: 1, releaseUnits: 1 });
});
test('rejects component version drift', async () => {
  await expect(validateRelease(await fixture(c => c.skills[0].version = '2.0.0'))).rejects.toThrow('version mismatch');
});
test('rejects duplicate membership', async () => {
  await expect(validateRelease(await fixture(c => c.releaseUnits.other = { version: '1.0.0', members: ['example'] }))).rejects.toThrow('Duplicate');
});
test('rejects members missing from catalog', async () => {
  await expect(validateRelease(await fixture(c => c.releaseUnits.example.members.push('missing')))).rejects.toThrow('Uncataloged release member');
});
test('rejects collection/plugin version mismatch', async () => {
  await expect(validateRelease(await fixture((c, p) => p.version = '1.1.0'))).rejects.toThrow('collection version');
});
test('checks links for every skill and ignores fenced examples', async () => {
  const root = await fixture();
  const file = join(root, 'skills/example/guide.md');
  await writeFile(file, '```md\n[example](missing.md)\n```\n[skill](SKILL.md#section)');
  expect((await validateRelease(root)).links).toBe(1);
  await writeFile(file, '[broken](missing.md)');
  await expect(validateRelease(root)).rejects.toThrow('ENOENT');
});
test('rejects a skill omitted from catalog', async () => {
  const root = await fixture(); await mkdir(join(root, 'skills/extra'));
  await writeFile(join(root, 'skills/extra/SKILL.md'), '---\nname: extra\n---\n');
  await expect(validateRelease(root)).rejects.toThrow('Uncataloged skill');
});
test('rejects arena skills accidentally included in stable plugin selection', async () => {
  await expect(validateRelease(await fixture(c => c.skills[0].maturity = 'arena'))).rejects.toThrow('Stable plugin');
});
