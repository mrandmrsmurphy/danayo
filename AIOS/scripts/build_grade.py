#!/usr/bin/env python3
"""build_grade.py N -- (re)build lookup/Grade N.md from characters/ ground truth.

Usage (vault root):  python3 AIOS/scripts/build_grade.py 3 [--stamp]

Writes: frontmatter (language 単亜語, size, optional date-last-perfect), the intro line
(第N等級 + 包含 + 字<count>個) with the 種類 bullets (形声/象形/会意/指事, counts from
graphemic_classification; any value other than the three type names is a 形声 phonetic component),
and a numbered list of every character whose grade_level == N: `[[X (char)|X]]` or `[[X]]` links,
ruby = the character's own 注音, gloss = first three `english` values. Order = Kangxi radical number,
then stroke_count, keeping the page's previous order for ties. The page's `## Base check` block is kept.
Numerals are Dan'a'yo words (ruby, delinked): 二百 / 五十 / 三 + 百 ...; 零 marks an empty place.
"""
import re, os, sys, subprocess
from collections import Counter
N = sys.argv[1]; STAMP = '--stamp' in sys.argv
ORD = {'1':'一','2':'二','3':'三','4':'四','5':'五','6':'六'}
def sh(*a): return subprocess.run(a, capture_output=True, text=True).stdout
radno = {}
for f in os.listdir('lookup/Radicals'):
    m = re.match(r'Radical (\d+)\.md', f)
    if m:
        r = re.search(r'^radical: *"?([^\n"]*)', open('lookup/Radicals/'+f).read().split('---')[1], re.M)
        if r: radno[r.group(1).strip()] = int(m.group(1))
rows = {}
for f in sh('git', 'ls-files', 'characters').split('\n'):
    if not f.endswith('.md'): continue
    parts = open(f).read().split('---')
    if len(parts) < 3: continue
    fm = parts[1]; st = os.path.basename(f)[:-3]
    g = re.search(r'^grade_level: *["\']?([^\n"\']*)', fm, re.M)
    if not g or g.group(1).strip() != N: continue
    gq = lambda k: (re.search(rf'^{k}: *["\']?([^\n"\']*)["\']?\s*$', fm, re.M) or [0, ''])[1].strip()
    m = re.search(r'^english:\n((?:\s*- .*\n)+)', fm, re.M)
    gc = re.search(r'^graphemic_classification: *["\']?([^\n"\']*)', fm, re.M)
    rows[st] = dict(rad=gq('radical'), sc=int(gq('stroke_count') or 0), zy=gq('注音'),
                    eng=[e.strip() for e in re.findall(r'-\s+(.*)', m.group(1))] if m else [],
                    gc=gc.group(1).strip() if gc else '', did=int(gq('danayo_id') or 0))
path = f'lookup/Grade {N}.md'; t = open(path).read()
body, base = t.split('## Base check', 1)
prev = [re.sub(r'^\.\./characters/', '', l) for l in re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', body)]
idx = {s: i for i, s in enumerate(prev)}
VARIANT = {'已': '己'}   # radical fields with no radical page of their own (flagged: characters/已, 巻 say 已)
for v in rows.values(): v['rad'] = VARIANT.get(v['rad'], v['rad'])
bad = [s for s, v in rows.items() if v['rad'] not in radno]
if bad: sys.exit(f'no radical number for {bad}')
order = sorted(rows, key=lambda s: (radno[rows[s]['rad']], rows[s]['sc'], idx.get(s, 10000 + rows[s]['did'])))
def zy(w):
    return re.search(r'^注音: *"?([^\n"]*)', open(f'words/{w}.md').read().split('---')[1], re.M).group(1).strip()
def ru(w):
    assert os.path.exists(f'words/{w}.md'), f'word missing: {w}'
    return f'<ruby>{w}<rt>{zy(w)}</rt></ruby>'
D = '〇一二三四五六七八九'
def pieces(n):
    p = []; h, r = divmod(n, 100); t_, u = divmod(r, 10)
    if h == 1: p.append('一百')
    elif h == 2: p.append('二百')
    elif h >= 3: p += [D[h], '百']
    if r:
        if h and t_ == 0: p += ['零', D[u]]
        elif t_ == 0: p.append(D[u])
        elif t_ == 1: p.append('十' if u == 0 else '十' + D[u])
        else:
            p.append(D[t_] + '十')
            if u: p.append(D[u])
    return p
num = lambda n: ''.join(ru(x) for x in pieces(n))
c = Counter(v['gc'] if v['gc'] in ('象形', '会意', '指事') else ('形声' if v['gc'] else '(none)') for v in rows.values())
assert c['(none)'] == 0, f'{c["(none)"]} characters have no graphemic_classification'
lines = []
for i, s in enumerate(order, 1):
    label = s[:-7] if s.endswith(' (char)') else s
    link = f'[[{s}|{label}]]' if s.endswith(' (char)') else f'[[{s}]]'
    lines.append(f'{i}. <ruby>{link}<rt>{rows[s]["zy"]}</rt></ruby> - ' + ', '.join(rows[s]['eng'][:3]))
stamp = 'date-last-perfect: ' + __import__('datetime').date.today().isoformat() + '\n' if STAMP else ''
fm = f'---\nlanguage: 単亜語\n{stamp}size: {len(order)}\ntags: [lookup]\n---\n'
head = f"**{ru('第' + ORD[N])}{ru('等級')}** {ru('包含')} {ru('字')}{num(len(order))}{ru('個')}.\n\n{ru('種類')}:\n"
bul = '\n'.join(f"- {ru(k)}{ru('字')}{num(c[k])}{ru('個')}" for k in ['形声', '象形', '会意', '指事'] if c[k])
open(path, 'w').write(fm + head + bul + '\n\n' + '\n'.join(lines) + '\n\n## Base check' + base)
print(N, len(order), dict(c), 'previous entries kept in order:', sum(1 for s in prev if s in rows))
