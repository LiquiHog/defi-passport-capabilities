"""Check navigation and browseable structure without imposing prose templates."""
from pathlib import Path
from urllib.parse import unquote
import json
import re

ROOT = Path(__file__).resolve().parents[1]
errors = []
files = [p for p in ROOT.rglob('*')
         if p.is_file() and not any(part.startswith('.') or part == '__pycache__'
                                   for part in p.relative_to(ROOT).parts)]
pages = [p for p in files if p.suffix == '.md']
for page in pages:
    text = page.read_text(encoding='utf-8')
    if not text.startswith('# '):
        errors.append(f'{page.relative_to(ROOT)}: missing page title')
    prose = re.sub(r'```.*?```', '', text, flags=re.S)
    for target in re.findall(r'\[[^\]]*\]\(([^\s)]+)\)', prose):
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
            continue
        local = unquote(target.split('#', 1)[0])
        if local and not (page.parent / local).exists():
            errors.append(f'{page.relative_to(ROOT)}: missing link {target}')

for folder in ROOT.rglob('*'):
    if not folder.is_dir() or any(part.startswith('.') or part == '__pycache__'
                                  for part in folder.relative_to(ROOT).parts):
        continue
    children = list(folder.iterdir())
    if not children:
        errors.append(f'{folder.relative_to(ROOT)}: empty directory')
    elif len(children) == 1 and children[0].name == 'README.md':
        errors.append(f'{folder.relative_to(ROOT)}: single-page folder; use a descriptive file')

for path in files:
    if path.suffix == '.json':
        try:
            json.loads(path.read_text(encoding='utf-8'))
        except (ValueError, UnicodeError) as exc:
            errors.append(f'{path.relative_to(ROOT)}: {exc}')
if errors:
    raise SystemExit('\n'.join(errors))
entries = [p for p in pages if 'catalog' in p.relative_to(ROOT).parts and p.name != 'README.md']
print(f'PASS: {len(pages)} Markdown pages, {len(entries)} catalog entries; local links, folder structure and JSON syntax.')
