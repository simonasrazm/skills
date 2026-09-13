const root = new URL('../../', import.meta.url);
const files = [...new Bun.Glob('skills/*/SKILL.md').scanSync({ cwd: root.pathname, absolute: true })];
if (!files.length) throw new Error('No public skills found.');

const names = new Set<string>();
for (const file of files) {
  const text = await Bun.file(file).text();
  const frontmatter = text.match(/^---\n([\s\S]*?)\n---\n/);
  if (!frontmatter) throw new Error(`${file}: missing YAML frontmatter`);
  const name = frontmatter[1].match(/^name:\s*(.+)$/m)?.[1].trim();
  const description = frontmatter[1].match(/^description:\s*(.+)$/m)?.[1].trim();
  if (!name || !/^[a-z0-9-]+$/.test(name)) throw new Error(`${file}: invalid name`);
  if (names.has(name)) throw new Error(`${file}: duplicate name ${name}`);
  names.add(name);
  if (!description || description.length < 60) throw new Error(`${file}: description is too weak for discovery`);
  const internal = /^user-invocable:\s*false$/m.test(frontmatter[1]);
  if (!internal && !/\buse (when|for)\b/i.test(description)) throw new Error(`${file}: description must say when to use the skill`);
}

console.log(`Validated ${files.length} skill definitions.`);
