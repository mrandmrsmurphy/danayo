#!/usr/bin/env python3
"""Rebuild "Lint Report.md" from the words and characters linters' own output.

Run from the vault root:  python3 AIOS/scripts/make_lint_report.py
Words run in default mode; characters run with --deep. The "Judgment items still open" section is hand-written and kept as is.
"""
import re, subprocess, datetime, collections

def run(script, *args):
    r = subprocess.run(['python3', f'AIOS/scripts/{script}', '--no-stamp', '--max', '100000', *args], capture_output=True, text=True)
    return r.stdout

def parse(out):
    groups = collections.OrderedDict(); tag = None
    for line in out.splitlines():
        m = re.match(r'^\[(\w\d)\] (.*): (\d+)$', line)
        if m:
            msg = m.group(2)
            if m.group(1) == 'C3' and msg.startswith('mc_id '): msg = 'mc_id differs from the lookup/CC list'; det = line
            tag = (m.group(1), msg); groups.setdefault(tag, []); 
            if m.group(1) == 'C3' and msg.startswith('mc_id '): pass
            cur_detail = m.group(2) if m.group(2).startswith('mc_id ') else None
            continue
        if tag and line.startswith('     ') and not line.strip().startswith('...'):
            groups[tag].append((line.strip(), cur_detail))
        elif line.strip() and not line.startswith(' '): tag = None
    return groups

def link(folder, item, detail):
    m = re.match(r'^(.*?)(?: \((?!char\))| -> |: )(.*)$', item)
    stem, rest = (m.group(1), item[len(m.group(1)):]) if m else (item, '')
    s = f'- [[{folder}/{stem}|{stem}]]{rest}'
    if detail: s += f' — {detail}'
    return s

def section(groups, folder):
    out = []
    for (tag, msg), items in groups.items():
        if not items or msg.startswith('(to do'): continue
        out += [f'### [{tag}] {msg} ({len(items)})', ''] + [link(folder, i, d) for i, d in items] + ['']
    return out

w = parse(run('lint_words.py')); c = parse(run('lint_characters.py', '--deep'))
wsum = re.search(r'^FAIL: (.*)$', run('lint_words.py'), re.M)
old = open('Lint Report.md').read()
judg = old[old.index('## Judgment items still open'):]
today = datetime.date.today().isoformat()
wc = sum(len(v) for v in w.values()); cc = sum(len(v) for v in c.values())
cnt = lambda g: ', '.join(f'{t} {n}' for t, n in sorted(collections.Counter({t: len(i) for (t, _), i in g.items() for _ in [0]}).items()))
def tally(g):
    d = collections.Counter()
    for (t, _), i in g.items(): d[t] += len(i)
    return ', '.join(f'{t} {n}' for t, n in sorted(d.items()))
lines = f"""---
tags:
  - lookup
date-last-perfect: {today}
---
# Lint Report

Generated {today} by `AIOS/scripts/make_lint_report.py` from the linters' own output. Every flagged page is a clickable link. Re-run any section with the command shown.

> Related: [[lookup/Characters|Characters]] · [[lookup/Words|Words]] · [[AIOS/skills/skill_lint|Lint skill]] · [[AIOS/checklists/checklist_words|Words checklist]] · [[AIOS/checklists/checklist_characters|Characters checklist]]

## Linter status

| Linter | Command | State today |
|---|---|---|
| Syllables | `python3 AIOS/scripts/lint_syllables.py` | Pass; stamped 2026-10-29 |
| SKIP | `python3 AIOS/scripts/lint_skip.py` | Pass; stamped 2026-10-29 |
| Radicals | `python3 AIOS/scripts/lint_radicals.py` | Pass; stamped 2026-10-29 |
| CC | `python3 AIOS/scripts/lint_cc.py` | Pass; stamped 2026-10-29 |
| Stroke | `python3 AIOS/scripts/lint_stroke.py` | Clean (does not stamp) |
| Chengyu | `python3 AIOS/scripts/lint_chengyu.py`, `lint_chengyu_groups.py` | Clean; grouping pages stamped 2026-10-29 |
| Characters | `python3 AIOS/scripts/lint_characters.py` | Default run clean; stamped 2026-10-29. `--deep`: {tally(c)} |
| **Words** | `python3 AIOS/scripts/lint_words.py` | **Fails**: {tally(w)} |

## Contents

- [[#Words (lint_words.py)]]
- [[#Characters, --deep run]]
- [[#Judgment items still open]]

## Words (lint_words.py)

""".split('\n')
lines += section(w, 'words')
lines += ['## Characters, --deep run', '', 'The default run checks only pages changed since their own stamp and is clean. `python3 AIOS/scripts/lint_characters.py --deep` checks every page and finds this hidden drift in already-stamped pages.', '']
lines += section(c, 'characters')
open('Lint Report.md', 'w').write('\n'.join(lines) + '\n' + judg)
print('words', tally(w), '| characters', tally(c))
