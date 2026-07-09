#!/usr/bin/env python3
"""Audit syllable pages, counting both wiki-links and Markdown character links."""

import yaml
import re
import urllib.parse
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
chars_by_bopomofo = defaultdict(set)
chars_by_hangul = defaultdict(set)
for p in CHARACTERS_DIR.glob('*.md'):
    fm, _ = parse_frontmatter(p)
    name = p.stem
    b = fm.get('注音')
    h = fm.get('諺文')
    if b:
        chars_by_bopomofo[b].add(name)
    if h:
        chars_by_hangul[h].add(name)

def extract_first_char_link(line):
    """Return the character name from the first link on a numbered/bullet line, or None."""
    # Wiki-link [[X]] or [[X (char)]]
    m = re.search(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', line)
    if m:
        return m.group(1).strip().replace(' (char)', '')
    # Markdown link [X](characters/...) or [X](words/...) — only count character links
    m = re.search(r'\[([^\]]+)\]\(([^)]+)\)', line)
    if m:
        href = m.group(2)
        decoded = urllib.parse.unquote(href)
        if 'characters/' in decoded or decoded.startswith('../characters/'):
            text = m.group(1).strip().replace(' (char)', '')
            return text
    return None

rows = []
for p in sorted(SYLLABLES_DIR.glob('*.md')):
    if p.name == 'Syllables.md':
        continue
    fm, text = parse_frontmatter(p)
    name = p.stem
    issues = []

    for field in required_fields:
        if field not in fm or fm[field] is None or fm[field] == '':
            issues.append(f'missing {field}')

    dlp = fm.get('date-last-perfect')
    if dlp is None or dlp == '':
        issues.append('not perfected')

    if 'dataviewjs' in text:
        issues.append('still has dataviewjs placeholder')

    # Extract the Characters section
    char_section_match = re.search(r'## Characters\s*\n(.*?)(?=\n## |\Z)', text, re.S)
    listed_chars = set()
    if char_section_match:
        section = char_section_match.group(1)
        for line in section.split('\n'):
            line = line.strip()
            # Numbered list item or bullet
            if re.match(r'^(\d+\.|[-*])\s+', line):
                char_name = extract_first_char_link(line)
                if char_name:
                    listed_chars.add(char_name)

    # Also handle pages with no ## Characters heading but entries before first ##
    if not char_section_match:
        # Find lines before any ## heading that look like list entries
        body = text.split('---', 2)[2] if text.startswith('---') else text
        before_heading = re.split(r'\n## ', body, 1)[0]
        for line in before_heading.split('\n'):
            line = line.strip()
            if re.match(r'^(\d+\.|[-*])\s+', line):
                char_name = extract_first_char_link(line)
                if char_name:
                    listed_chars.add(char_name)

    # Expected characters from database
    bopomofo = fm.get('注音')
    hangul = fm.get('諺文')
    expected_chars = set()
    if bopomofo:
        expected_chars.update(chars_by_bopomofo.get(bopomofo, set()))
    if hangul:
        expected_chars.update(chars_by_hangul.get(hangul, set()))
    expected_base = {n.replace(' (char)', '') for n in expected_chars}

    size = fm.get('size')
    if size is not None and isinstance(size, int):
        if len(listed_chars) != size:
            issues.append(f'size mismatch: frontmatter says {size}, counted {len(listed_chars)} character entries')

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
for r in perfect[:20]:
    print(f'  {r["file"]}  dlp={r["dlp"]}  size={r["size"]}')
if len(perfect) > 20:
    print(f'  ... and {len(perfect)-20} more')
print()

print(f'Imperfect ({len(not_perfect)}):')
for r in sorted(not_perfect, key=lambda x: (x['dlp'] or '0000-00-00', x['file'])):
    print(f'\n  {r["file"]}')
    print(f'    dlp={r["dlp"]}  size={r["size"]}  listed={r["listed"]}  expected_chars={r["expected"]}')
    for issue in r['issues']:
        print(f'    - {issue}')

print('\n--- Summary by issue type ---')
counts = defaultdict(int)
for r in rows:
    for issue in r['issues']:
        key = issue.split(':')[0]
        counts[key] += 1
for key, cnt in sorted(counts.items(), key=lambda x: -x[1]):
    print(f'{cnt:4d}  {key}')
