from pathlib import Path
import re, json, sys, importlib.util, hashlib, zipfile, tempfile
import yaml

V=Path('D:/PerfectLife/LifeVault')
S=Path('C:/Users/ethan/.codex/skills')
names=['getting-started','lifevault-remember','lifevault-resume','lifevault-research','lifevault-teach','lifevault-audit']
errors=[]
notes=list(V.rglob('*.md'))

for p in notes:
    t=p.read_text(encoding='utf-8')
    if p.name!='AGENTS.md':
        m=re.match(r'^---\n(.*?)\n---\n',t,re.S)
        if not m: errors.append(f'Missing metadata: {p}')
        else:
            try:
                y=yaml.safe_load(m[1])
                for key in ['type','status','created','updated','schema']:
                    if key not in y: errors.append(f'Missing {key}: {p}')
            except Exception as e: errors.append(f'YAML {p}: {e}')
    for target in re.findall(r'\[\[([^\]]+)\]\]',t):
        base=target.split('|')[0].split('#')[0]
        if not base: continue
        q=V/(base if base.endswith('.md') else base+'.md')
        if not q.exists(): errors.append(f'Broken wiki link in {p.name}: {target}')
    if 'D:\\LifeVault' in t: errors.append(f'Old path: {p}')

for p in (V/'.obsidian').glob('*.json'):
    try: json.loads(p.read_text(encoding='utf-8'))
    except Exception as e: errors.append(str(e))

spec=importlib.util.spec_from_file_location('validator','C:/Users/ethan/.codex/skills/.system/skill-creator/scripts/quick_validate.py')
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
for name in names:
    ok,msg=mod.validate_skill(S/name)
    if not ok: errors.append(name+': '+msg)
    t=(S/name/'SKILL.md').read_text(encoding='utf-8')
    for target in re.findall(r'\]\((references/[^)]+)\)',t):
        if not (S/name/target).exists(): errors.append(f'Missing skill reference {name}/{target}')
    meta=yaml.safe_load((S/name/'agents/openai.yaml').read_text())
    short=meta['interface']['short_description']
    if not 25<=len(short)<=64: errors.append(f'Description length: {name}')
    if '$'+name not in meta['interface']['default_prompt']: errors.append(f'Prompt: {name}')

bank=(S/'getting-started/references/interview.md').read_text(encoding='utf-8')
ids=re.findall(r'^- \*\*([A-L]\d{2})',bank,re.M)
assert len(ids)==120 and len(set(ids))==120
assert bank.count(' · core**')==36
startup=sum(len((V/p).read_text(encoding='utf-8').split()) for p in ['00 System/Start.md','00 System/Context.md','03 Projects/Projects.md'])
if startup>1500: errors.append(f'Startup too large: {startup}')
print(json.dumps({'notes':len(notes),'skills':len(names),'questions':len(ids),'core_questions':36,'startup_words':startup,'errors':errors},indent=2))
if errors: sys.exit(1)
