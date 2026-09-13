import { readFile, stat } from 'node:fs/promises';
import { dirname, isAbsolute, relative, resolve } from 'node:path';

const semver = /^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$/;
const validName = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;

export async function validateRelease(root: string) {
  const catalog = await Bun.file(resolve(root, 'skills.catalog.json')).json();
  const plugin = await Bun.file(resolve(root, '.claude-plugin/plugin.json')).json();
  if (catalog.schemaVersion !== 2 || catalog.releaseUnit !== 'collection' ||
      !semver.test(catalog.version) || catalog.version !== plugin.version)
    throw Error('Invalid or mismatched collection version');
  if (!Array.isArray(catalog.skills) || !catalog.skills.length || !catalog.releaseUnits ||
      !Array.isArray(plugin.skills) || new Set(plugin.skills).size !== plugin.skills.length)
    throw Error('Invalid catalog or plugin selection');

  const membership = new Map<string, string>();
  for (const [name, unit] of Object.entries(catalog.releaseUnits) as [string, any][]) {
    if (!validName.test(name) || !semver.test(unit.version) || !Array.isArray(unit.members) || !unit.members.length)
      throw Error('Invalid release unit: ' + name);
    for (const member of unit.members) {
      if (membership.has(member)) throw Error('Duplicate release membership: ' + member);
      membership.set(member, name);
    }
  }
  const names = new Set<string>();
  let links = 0;
  for (const entry of catalog.skills) {
    if (!validName.test(entry.name) || names.has(entry.name) || entry.path !== `skills/${entry.name}` ||
        !['arena', 'stable', 'deprecated'].includes(entry.maturity)) throw Error('Invalid catalog entry');
    names.add(entry.name);
    const unit = catalog.releaseUnits[entry.releaseUnit];
    if (!unit || membership.get(entry.name) !== entry.releaseUnit || entry.version !== unit.version)
      throw Error('Release membership/version mismatch: ' + entry.name);
    const definition = await readFile(resolve(root, entry.path, 'SKILL.md'), 'utf8');
    if (!definition.match(/^---\n([\s\S]*?)\n---/)?.[1].split('\n').includes(`name: ${entry.name}`))
      throw Error('Catalog/name mismatch: ' + entry.name);
    if (plugin.skills.includes('./' + entry.path) !== (entry.maturity === 'stable'))
      throw Error('Stable plugin selection mismatch: ' + entry.name);
    for (const file of new Bun.Glob('**/*.md').scanSync({ cwd: resolve(root, entry.path), absolute: true })) {
      const markdown = (await readFile(file, 'utf8')).replace(/```[\s\S]*?```|~~~[\s\S]*?~~~/g, '');
      for (const match of markdown.matchAll(/\]\(([^)]+)\)/g)) {
        const target = match[1].replace(/^<([^>]+)>.*$/, '$1').replace(/\s+"[^"]*"$/, '');
        if (/^(?:[a-z][a-z0-9+.-]*:|#)/i.test(target)) continue;
        const path = decodeURIComponent(target.split(/[?#]/)[0]);
        const destination = resolve(dirname(file), path);
        const withinRoot = relative(root, destination);
        if (isAbsolute(path) || withinRoot === '..' || withinRoot.startsWith('../'))
          throw Error('Local link escapes repository: ' + file + ' -> ' + target);
        await stat(destination);
        links++;
      }
    }
  }
  for (const member of membership.keys()) if (!names.has(member)) throw Error('Uncataloged release member: ' + member);
  for (const file of new Bun.Glob('skills/*/SKILL.md').scanSync({ cwd: root }))
    if (!names.has(file.split('/')[1])) throw Error('Uncataloged skill: ' + file);
  if (plugin.skills.some((path: string) => !catalog.skills.some((entry: any) => './' + entry.path === path)))
    throw Error('Uncataloged plugin skill');
  return { version: catalog.version, skills: names.size, releaseUnits: Object.keys(catalog.releaseUnits).length, links };
}

if (import.meta.main) console.log(await validateRelease(resolve(import.meta.dir, '../..')));
