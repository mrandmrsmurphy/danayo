#!/usr/bin/env python3
"""Audit syllable pages against the checklist and current character database."""

import yaml
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path('/Users/robertmarshallmurphy/Documents/danayo')
SYLLABLES_DIR = ROOT / 'syllables'
CHARACTERS_DIR = ROOT / 'characters'

required_fields = ['date-last-perfect', 'size', '羅馬字', '諺文', '注音', 'english', 'tags']

def parse_frontmatter(path):
    text = path.read_text(encoding='utf-8')
    if not text.startswith('---'):
        return {}, text
    parts = text.split('---', 2)
    if len(parts) < 3:
        return {}, text
    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as e:
        return {'_yaml_error': str(e)}, text
    return fm, text

# Index characters by 注音 and 諺文
chars_by_bopomofo = defaultdict(list)
chars_by_hangul = defaultdict(list)
char_paths = {}
for p in CHARACTERS_DIR.glob('*.md'):
    fm, _ = parse_frontmatter(p)
    name = p.stem
    b = fm.get('注音')
    h = fm.get('諺文')
    if b:
        chars_by_bopomofo[b].append(name)
    if h:
        chars_by_hangul[h].append(name)
    char_paths[name] = p

rows = []
for p in sorted(SYLLABLES_DIR.glob('*.md')):
    if p.name == 'Syllables.md':
        continue
    fm, text = parse_frontmatter(p)
    name = p.stem

    issues = []

    # Required fields
    for field in required_fields:
        if field not in fm or fm[field] is None or fm[field] == '':
            issues.append(f'missing {field}')

    # date-last-perfect
    dlp = fm.get('date-last-perfect')
    if dlp is None or dlp == '':
        issues.append('not perfected')

    # dataviewjs placeholder
    if 'dataviewjs' in text:
        issues.append('still has dataviewjs placeholder')

    # Cross-check with characters
    bopomofo = fm.get('注音')
    hangul = fm.get('諺文')
    expected_chars = set()
    if bopomofo:
        expected_chars.update(chars_by_bopomofo.get(bopomofo, []))
    if hangul:
        expected_chars.update(chars_by_hangul.get(hangul, []))

    # Normalize: strip (char) suffix for comparison
    expected_base = {n.replace(' (char)', '') for n in expected_chars}

    # Extract character links from Characters section
    char_section_match = re.search(r'## Characters.*?(?=## Data check|$)', text, re.S)
    listed_chars = set()
    if char_section_match:
        section = char_section_match.group(0)
        # Match [[X (char)]] or [[X]]
        for link in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', section):
            link = link.strip()
            listed_chars.add(link.replace(' (char)', ''))

    # Check size
    size = fm.get('size')
    if size is not None and isinstance(size, int):
        if len(listed_chars) != size:
            issues.append(f'size mismatch: frontmatter says {size}, found {len(listed_chars)} entries')

    # Compare expected vs listed
    if expected_base:
        missing = expected_base - listed_chars
        extra = listed_chars - expected_base
        if missing:
            issues.append(f'missing characters: {sorted(missing)}')
        if extra:
            issues.append(f'extra/unexpected characters: {sorted(extra)}')

    rows.append({
        'file': name,
        'dlp': dlp,
        'size': size,
        'listed': len(listed_chars),
        'expected': len(expected_base),
        'issues': issues,
    })

# Reports
print(f'Total syllable files audited: {len(rows)}')
print()

not_perfect = [r for r in rows if r['issues']]
perfect = [r for r in rows if not r['issues']]
print(f'Perfect ({len(perfect)}):')
for r in perfect[:10]:
    print(f'  {r["file"]}  dlp={r["dlp"]}  size={r["size"]}')
if len(perfect) > 10:
    print(f'  ... and {len(perfect)-10} more')
print()

print(f'Imperfect ({len(not_perfect)}):')
for r in sorted(not_perfect, key=lambda x: (x['dlp'] or '', x['file'])):
    print(f'\n  {r["file"]}')
    print(f'    dlp={r["dlp"]}  size={r["size"]}  listed={r["listed"]}  expected_chars={r["expected"]}')
    for issue in r['issues']:
        print(f'    - {issue}')

# Summary by issue type
print('\n--- Summary by issue type ---')
counts = defaultdict(int)
for r in rows:
    for issue in r['issues']:
        key = issue.split(':')[0]
        counts[key] += 1
for key, cnt in sorted(counts.items(), key=lambda x: -x[1]):
    print(f'{cnt:4d}  {key}')
