#!/usr/bin/env python3
"""lint Stroke -- audit (and optionally repair) lookup/Stroke/Stroke NN.md against characters/*.md.

Usage (run from the vault root):
  python3 AIOS/scripts/lint_stroke.py                 # audit all pages, report only
  python3 AIOS/scripts/lint_stroke.py 8 9 10          # audit selected pages
  python3 AIOS/scripts/lint_stroke.py --fix 17        # also rewrite ### In Use + size to match ground truth
  python3 AIOS/scripts/lint_stroke.py --fix --stamp   # ...and stamp date-last-perfect on pages that come out clean

Ground truth = every tracked characters/*.md, read from the working tree (so uncommitted edits count).
--fix never touches ### Aliases / ### Forbidden / prose; it only rebuilds the ### In Use bullets
(keeping existing order within a SKIP group, appending new entries) and `size`.
Judgment calls are only REPORTED, never auto-fixed: see the FLAG lines.
"""
import re, subprocess, sys, os, datetime
from collections import defaultdict

def sh(*a): return subprocess.run(a, capture_output=True, text=True, check=True).stdout
args = sys.argv[1:]
FIX = '--fix' in args; STAMP = '--stamp' in args
pages = [int(a) for a in args if a.isdigit()]
TODAY = datetime.date.today().isoformat()
key = lambda s: [int(x) for x in s.split('-')]

# ---- ground truth ---------------------------------------------------------
files = [f for f in sh('git', 'ls-files', 'characters').split('\n') if f.endswith('.md')]
chars = {}   # stem -> dict(stroke, skip, zy)
flags = []
for f in files:
    try: t = open(f).read()
    except OSError: flags.append(f'FLAG unreadable {f}'); continue
    parts = t.split('---')
    if len(parts) < 3: continue
    fm = parts[1]
    g = lambda k: (re.search(rf'^{k}: *"?([^\n"]*)"?\s*$', fm, re.M) or [None, None])[1]
    stem = os.path.basename(f)[:-3]
    chars[stem] = dict(stroke=g('stroke_count'), skip=g('skip_number'), zy=(g('注音') or '').strip())

by_stroke = defaultdict(list)
for stem, d in chars.items():
    s = d['stroke']
    if s is None or not s.strip().isdigit():
        flags.append(f'FLAG {stem}: missing/non-integer stroke_count ({s!r})'); continue
    by_stroke[int(s)].append(stem)
    sk = d['skip']
    if not sk or not re.fullmatch(r'\d+-\d+-\d+', sk):
        flags.append(f'FLAG {stem}: missing/odd skip_number ({sk!r})')
    elif sk.startswith('4-') and int(sk.split('-')[1]) != int(s):
        flags.append(f'FLAG {stem}: SKIP-4 second number {sk} != stroke_count {s} (verify EDRDG; usually stroke_count is the wrong one)')

def link(stem):
    return f'[[{stem}|{stem[:-7]}]]' if stem.endswith(' (char)') else f'[[{stem}]]'
def ruby(stem): return f'<ruby>{link(stem)}<rt>{chars[stem]["zy"]}</rt></ruby>'

# ---- per page -------------------------------------------------------------
ENTRY = re.compile(r'<ruby>\[\[([^\]|]+)(?:\|([^\]]+))?\]\]<rt>([^<]*)</rt></ruby>')
def audit(n):
    p = f'lookup/Stroke/Stroke {n:02d}.md'
    if not os.path.exists(p): return None, [f'MISSING PAGE {p}' if by_stroke.get(n) else f'(no page, no chars)'], False
    t = open(p).read(); out = []
    fm_m = re.match(r'---\n(.*?)\n---\n', t, re.S)
    if not fm_m: return p, ['NO FRONTMATTER'], False
    fm = fm_m.group(1)
    sc = re.search(r'^stroke_count: *(.*)$', fm, re.M)
    if not sc or sc.group(1).strip() != str(n): out.append(f'frontmatter stroke_count {sc and sc.group(1)!r} != {n} (must be unquoted integer)')
    if not re.search(r'^date-last-perfect: *\d{4}-\d\d-\d\d', fm, re.M): out.append('date-last-perfect missing/blank')
    if not re.search(r'^size: *\d+\s*$', fm, re.M): out.append('size missing')
    body = t[fm_m.end():]
    if not re.match(r'\s*> (\[\[Stroke\]\]|\[Stroke\]\(Stroke\.md\))\s*\n', body): out.append('breadcrumb "> [[Stroke]]" not first line after frontmatter')
    for h in ('## Characters', '### In Use', '### Aliases', '## Data check'):
        if not re.search(rf'^{re.escape(h)}\s*$', body, re.M): out.append(f'heading missing: {h}')
    if re.search(r'^#+ Data (search|check)', body, re.M) and not re.search(r'^## Data check\s*$', body, re.M): out.append('wrong Data check heading')
    if body.count('```') % 2: out.append('UNCLOSED code fence')
    want_q = f'WHERE stroke_count = "{n}" OR stroke_count = {n}'
    if want_q not in body or 'TABLE file.link AS "Character", 注音 AS "Sound", skip_number AS "SKIP"' not in body or 'SORT skip_number ASC' not in body:
        out.append('Data check query not canonical')
    # In Use bullets
    prev = None; seen = {}; page_codes = {}
    for line in body.split('\n'):
        m = re.match(r'- (\d+-\d+-\d+): (.*)$', line)
        if not m:
            if re.match(r'\d+\. |#### ', line): out.append(f'old-style line: {line[:50]}')
            continue
        code, rest = m.groups()
        if prev and key(code) <= key(prev): out.append(f'SKIP order/dup group: {prev} then {code}')
        prev = code
        if re.sub(r'<ruby>.*?</ruby>|[ ,]', '', rest): out.append(f'{code}: non-ruby/gloss text in line')
        for mm in ENTRY.finditer(rest):
            lk, disp, rt = mm.groups()
            if lk in seen: out.append(f'DUP {lk}')
            seen[lk] = code
            if lk not in chars: out.append(f'NOFILE {lk}'); continue
            d = chars[lk]
            if d['stroke'] != str(n): out.append(f'misfiled {lk}: its stroke_count is {d["stroke"]}')
            elif d['skip'] != code: out.append(f'wrong group {lk}: page {code}, file {d["skip"]}')
            if d['zy'] != rt.strip(): out.append(f'reading {lk}: page {rt} / file {d["zy"]}')
            if lk.endswith(' (char)') != (disp is not None) or (disp and disp != lk[:-7]): out.append(f'link form {lk}|{disp}')
    truth = set(by_stroke.get(n, []))
    for s in sorted(truth - set(seen)): out.append(f'MISSING {s} ({chars[s]["skip"]})')
    sz = re.search(r'^size: *(\d+)', fm, re.M)
    if sz and int(sz.group(1)) != len(seen): out.append(f'size {sz.group(1)} != entries {len(seen)}')
    return p, out, True

def rebuild(n, p):
    t = open(p).read()
    m = re.search(r'(### In Use\n)(.*?)(?=\n### |\n## )', t, re.S)
    existing = defaultdict(list)
    for line in m.group(2).split('\n'):
        mm = re.match(r'- (\d+-\d+-\d+): (.*)$', line)
        if mm:
            for e in ENTRY.finditer(mm.group(2)):
                if e.group(1) in chars and chars[e.group(1)]['stroke'] == str(n): existing[chars[e.group(1)]['skip']].append(e.group(1))
    groups = defaultdict(list)
    placed = set()
    for code, stems in existing.items():
        for s in stems:
            if s not in placed and chars[s]['skip'] == code: groups[code].append(s); placed.add(s)
    for s in sorted(by_stroke.get(n, [])):
        if s not in placed and chars[s]['skip']:
            groups[chars[s]['skip']].append(s); placed.add(s)
    lines = [f'- {c}: ' + ', '.join(ruby(s) for s in groups[c]) for c in sorted(groups, key=key)]
    t = t[:m.start(2)] + '\n'.join(lines) + '\n' + t[m.end(2):]
    t = re.sub(r'^size: *\d+', f'size: {len(placed)}', t, count=1, flags=re.M)
    open(p, 'w').write(t)

targets = pages or sorted(set(by_stroke) | set(int(re.search(r'(\d+)', f).group(1)) for f in os.listdir('lookup/Stroke') if re.match(r'Stroke \d+\.md', f)))
print('\n'.join(flags) or 'corpus flags: none')
clean_all = True
for n in targets:
    p, out, exists = audit(n)
    if p is None: print(f'Stroke {n:02d}: {out[0]}'); continue
    structural = [o for o in out if not o.startswith(('MISSING ', 'misfiled', 'wrong group', 'reading ', 'size ', 'link form', 'SKIP order', 'DUP'))]
    if FIX and exists and out:
        rebuild(n, p); _, out2, _ = audit(n)
        print(f'Stroke {n:02d}: fixed {len(out) - len(out2)} items; remaining {len(out2)}'); out = out2
    status = 'CLEAN' if not out else f'{len(out)} issue(s)'
    print(f'Stroke {n:02d} ({len(by_stroke.get(n, []))} chars): {status}')
    for o in out[:25]: print('   ', o)
    if len(out) > 25: print(f'    ... {len(out) - 25} more')
    if STAMP and not out and exists:
        t = open(p).read(); t = re.sub(r'^date-last-perfect: .*', f'date-last-perfect: {TODAY}', t, count=1, flags=re.M); open(p, 'w').write(t)
