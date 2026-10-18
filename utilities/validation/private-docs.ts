import { execFileSync } from 'node:child_process';
const git = (...args: string[]) => execFileSync('git', args, { encoding: 'utf8' });
const paths = git('ls-files', '-z').split('\0').filter(Boolean);
const history = git('rev-list', '--objects', 'HEAD').split('\n').map(line => line.slice(line.indexOf(' ') + 1));
const forbidden = [...new Set([...paths, ...history].filter(path => path.split('/').includes('docs')))];
if (forbidden.length) {
  console.error('Private documentation must not occur in the public tree or its history:\n' + forbidden.join('\n'));
  process.exit(1);
}
console.log('Public tree and reachable history contain no private docs paths.');
