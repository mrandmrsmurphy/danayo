#!/usr/bin/env python3
"""Check the three chengyu grouping pages against the leaf pages (checklist_chengyu.md, "Grouping pages").

Run from the vault root: python3 AIOS/scripts/lint_chengyu_groups.py
Reports, per grouping page: a missing or wrong `size` property, missing / extra / duplicate entries, entries whose ruby 注音 differs from the
leaf's, entries with no ruby, no gloss, a wikilink style, an absolute path, or a stray mark. Exit 1 if any.
Report only; it never edits. Entry order is unconstrained (unordered bullets).
"""
import re, subprocess, sys, urllib.parse, collections

def git_files():
    out = subprocess.check_output(['git', 'ls-files', '-z', 'chengyu/'], text=True)
    return [f for f in out.split('\0') if f.endswith('.md')]

GROUPS = {"Dan'a'yo Chengyu": lambda o: o == '単亜語',
          'Biblical Chengyu': lambda o: o == 'Bible',
          'Misc. Chengyu': lambda o: o not in ('単亜語', 'Bible')}

leaf = {}
for f in git_files():
    if f.endswith('Chengyu.md'):
        continue
    fm = re.match(r'---\n(.*?)\n---', open(f).read(), re.S).group(1)
    name = f[len('chengyu/'):-3]
    origin = re.search(r'^origin:\s*(.*)', fm, re.M).group(1).strip().strip('"')
    zy = re.search(r'^注音:\s*(.*)', fm, re.M).group(1).strip().strip('"')
    leaf[name] = (origin, zy)

bad = 0
for g, test in GROUPS.items():
    text = open(f'chengyu/{g}.md').read()
    body = text.split('## Base check')[0].split('---', 2)[2]
    want = {n for n, (o, _) in leaf.items() if test(o)}
    names, problems = [], []
    for line in body.split('\n'):
        if not line.startswith('- '):
            continue
        m = re.match(r'- <ruby>\[([^\]]+)\]\(chengyu/([^)]+)\.md\)<rt>([^<]*)</rt></ruby> - (\S.*)$', line)
        if not m:
            problems.append(f'malformed entry: {line[:70]}')
            m2 = re.search(r'\[\[?([^\]|]+)', line)
            if m2:
                names.append(urllib.parse.unquote(m2.group(1)))
            continue
        label, target, zy, gloss = m.groups()
        target = urllib.parse.unquote(target)
        names.append(target)
        if label != target:
            problems.append(f'label/target differ: {label} / {target}')
        if target in leaf and leaf[target][1] != zy:
            problems.append(f'注音 differs from leaf: {target}')
        if '✅' in line:
            problems.append(f'stray mark: {target}')
    c = collections.Counter(names)
    missing, extra = sorted(want - set(names)), sorted(set(names) - want)
    dup = [k for k, v in c.items() if v > 1]
    print(f'== {g}: expected {len(want)}, listed {len(names)}')
    sz = re.search(r'^size:\s*(\d+)', text.split('---', 2)[1], re.M)
    if not sz:
        problems.append('no size property')
    elif int(sz.group(1)) != len(names):
        problems.append(f'size {sz.group(1)} != {len(names)} entries')
    for label, items in (('missing', missing), ('extra', extra), ('duplicate', dup), ('problem', problems)):
        if items:
            bad += len(items)
            print(f'  {label}: {items}')
sys.exit(1 if bad else 0)
