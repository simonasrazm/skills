import { readFile, stat } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';
const root=resolve(import.meta.dir,'..');
const catalog=await Bun.file(root+'/skills.catalog.json').json();
const plugin=await Bun.file(root+'/.claude-plugin/plugin.json').json();
if(catalog.version!==plugin.version||!/^\d+\.\d+\.\d+(?:-rc\.\d+)?$/.test(catalog.version))throw Error('Invalid or mismatched release version');
const names=new Set<string>();
for(const entry of catalog.skills){
 if(names.has(entry.name)||entry.path!==`skills/${entry.name}`||!['arena','stable','deprecated'].includes(entry.maturity))throw Error('Invalid catalog entry');
 names.add(entry.name);
 const text=await readFile(resolve(root,entry.path,'SKILL.md'),'utf8');
 if(!text.includes(`\nname: ${entry.name}\n`))throw Error('Catalog/name mismatch');
 if(plugin.skills.includes('./'+entry.path)!==(entry.maturity==='stable'))throw Error('Stable plugin selection mismatch: '+entry.name);
}
for(const file of new Bun.Glob('skills/*/SKILL.md').scanSync({cwd:root}))if(!names.has(file.split('/')[1]))throw Error('Uncataloged skill '+file);
if(plugin.skills.some(p=>!catalog.skills.some(e=>'./'+e.path===p)))throw Error('Uncataloged plugin skill');
const family=catalog.skills.filter(s=>s.family==='sflo-waydriver');
if(family.length!==7)throw Error('Incomplete family');
let links=0;
for(const entry of family)for(const file of new Bun.Glob('**/*.md').scanSync({cwd:root+'/'+entry.path,absolute:true})){
 const text=await readFile(file,'utf8');
 if(/\/Users\/|\.scratch\/dark-factory-skill/.test(text))throw Error('Private path '+file);
 for(const m of text.replace(/```[\s\S]*?```/g,'').matchAll(/\]\(([^)]+)\)/g)){
  if(/^(https?:|#)/.test(m[1]))continue;
  await stat(resolve(dirname(file),m[1]));links++;
 }
}
const arenaExists=await stat(root+'/arena').then(()=>true,error=>{if(error.code==='ENOENT')return false;throw error;});
if(arenaExists)throw Error('Arena is metadata; remove the obsolete directory');
console.log(`Release ${catalog.version}: ${names.size} catalog entries, 7 family members, ${links} links valid.`);
