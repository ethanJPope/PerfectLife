"""Create a local recovery package. No upload, deletion, or scheduled task."""
from pathlib import Path
from datetime import datetime
import argparse
import hashlib
import json
import zipfile

VAULT = Path('D:/PerfectLife/LifeVault')
SKILLS = Path('C:/Users/ethan/.codex/skills')
NAMES = ['getting-started', 'lifevault-remember', 'lifevault-resume',
         'lifevault-research', 'lifevault-teach', 'lifevault-audit']
GLOBAL = Path('C:/Users/ethan/.codex/AGENTS.md')

def create_backup(destination):
    destination = Path(destination).resolve()
    root = VAULT.resolve()
    if destination == root or destination.is_relative_to(root):
        raise ValueError('Backup destination must be outside the vault.')
    if not (root / '00 System/Memory rules.md').is_file():
        raise ValueError('LifeVault root or memory rules missing.')
    pairs = []
    # Symlinks could accidentally include files outside the intended source roots.
    for base, prefix in [(root, 'LifeVault')] + [(SKILLS / n, 'skills/' + n) for n in NAMES]:
        if not base.is_dir() or base.is_symlink():
            raise ValueError(f'Missing or linked source root: {base}')
        for p in sorted(base.rglob('*')):
            if p.is_symlink():
                raise ValueError(f'Refusing linked source: {p}')
            if p.is_file() and '.trash' not in p.parts and '__pycache__' not in p.parts:
                pairs.append((p, prefix + '/' + p.relative_to(base).as_posix()))
    pairs.append((GLOBAL, 'codex/AGENTS.md'))
    project_agents = root.parent / 'AGENTS.md'
    if project_agents.is_file():
        pairs.append((project_agents, 'project/AGENTS.md'))
    destination.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().astimezone().strftime('%Y-%m-%d_%H%M%S_%f')
    archive = destination / f'LifeVault-{stamp}.zip'
    manifest = {'created': datetime.now().astimezone().isoformat(), 'files': {}}
    with zipfile.ZipFile(archive, 'x', compression=zipfile.ZIP_DEFLATED) as z:
        for path, name in pairs:
            content = path.read_bytes()
            z.writestr(name, content)
            manifest['files'][name] = hashlib.sha256(content).hexdigest()
        z.writestr('MANIFEST.json', json.dumps(manifest, indent=2))
    with zipfile.ZipFile(archive) as z:
        error = z.testzip()
        if error:
            raise RuntimeError(f'Integrity check failed: {error}')
    print(json.dumps({'archive': str(archive), 'files': len(pairs), 'integrity': 'passed'}))
    return archive

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--destination', required=True)
    create_backup(parser.parse_args().destination)
