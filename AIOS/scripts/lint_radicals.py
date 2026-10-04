#!/usr/bin/env python3
"""lint Radicals: report-only audit of the radical pages and lookup/Radicals/Radicals.md, then stamp Radicals.md if clean.

Run from the vault root:  python3 AIOS/scripts/lint_radicals.py [--no-stamp] [--days N]

Ground truth is the `radical:` field of every character page; each radical page `Radical NNN.md` carries its own
`radical:` value, which is the key that joins characters to pages.

Checks (all must pass before Radicals.md is stamped):
  1. Every radical page (Radical 001 .. 214) has a `date-last-perfect` no older than N days (default 30).
  2. Every character has a `radical:` value, and it names an existing radical page (no character is orphaned).
  3. Radicals.md lists every radical page exactly once (none missing, none duplicated).
  4. Every link on Radicals.md points at a radical page that exists (none wanted).
  5. The "(N characters)" count after each bullet on Radicals.md equals the number of characters whose
     `radical:` is that page's radical (the counts are up to date).
Also reported as warnings, not blocking: a radical page whose `size:` differs from the ground-truth count.

On a clean run it sets `date-last-perfect:` in Radicals.md to today's date. It edits no other file.
Exit status 0 if clean, 1 otherwise.
"""
import re, subprocess, sys, datetime, os, collections

DAYS = 30
if '--days' in sys.argv:
    DAYS = int(sys.argv[sys.argv.index('--days') + 1])
STAMP = '--no-stamp' not in sys.argv
TODAY = datetime.date.today()
CUTOFF = TODAY - datetime.timedelta(days=DAYS)
INDEX = 'lookup/Radicals/Radicals.md'

def git_files(prefix):
    return [f for f in subprocess.check_output(['git', 'ls-files', '-z', prefix], text=True).split('\0') if f.endswith('.md')]

def fm_block(t):
    m = re.match(r'---\n(.*?)\n---', t, re.S)
    return m.group(1) if m else ''

def fm_get(t, key):
    k = re.search(r'^%s:[ \t]*"?([^"\n]*)"?[ \t]*$' % re.escape(key), fm_block(t), re.M)
    return k.group(1).strip() if k else None

problems = collections.OrderedDict()
warnings = collections.OrderedDict()
def add(d, k, v): d.setdefault(k, []).append(v)

# --- radical pages
pages = {}      # number string -> (radical glyph, size, date)
for f in git_files('lookup/Radicals/'):
    m = re.search(r'Radical (\d{3})\.md$', f)
    if not m:
        continue
    t = open(f).read()
    pages[m.group(1)] = (fm_get(t, 'radical'), fm_get(t, 'size'), fm_get(t, 'date-last-perfect'))

# 1. freshness
for n, (glyph, size, d) in sorted(pages.items()):
    if not d:
        add(problems, 'radical page has no date-last-perfect', f'Radical {n}')
        continue
    try:
        dd = datetime.date.fromisoformat(d)
    except ValueError:
        add(problems, 'unparseable date-last-perfect', f'Radical {n}: {d}')
        continue
    if dd < CUTOFF:
        add(problems, f'radical page date-last-perfect older than {DAYS} days', f'Radical {n}: {d}')
    if not glyph:
        add(problems, 'radical page has no `radical:` field', f'Radical {n}')

glyph_to_page = collections.defaultdict(list)
for n, (glyph, _, _) in pages.items():
    if glyph:
        glyph_to_page[glyph].append(n)
for g, ns in glyph_to_page.items():
    if len(ns) > 1:
        add(problems, 'two radical pages share one `radical:` value', f'{g}: {sorted(ns)}')

# --- characters (ground truth)
count = collections.Counter()
nchars = 0
for f in git_files('characters/'):
    try:
        t = open(f).read()
    except OSError:
        continue
    h = fm_block(t)
    if not re.search(r'^tags:[\s\S]*?-\s*character', h, re.M):
        continue
    nchars += 1
    name = os.path.basename(f)[:-3]
    r = fm_get(t, 'radical')
    if not r:
        add(problems, 'character has no `radical:`', name)
    elif r not in glyph_to_page:
        add(problems, 'character `radical:` names no radical page', f'{name} -> {r}')
    else:
        count[r] += 1

# --- Radicals.md
text = open(INDEX).read()
if STAMP is not None:
    pass
bullets = {}
for line in text.split('\n'):
    if not line.startswith('- '):
        continue
    m = re.search(r'Radical[ %20]*(\d{3})', line)
    if not m:
        continue
    n = m.group(1)
    c = re.search(r'\((\d+) characters?\)', line)
    bullets.setdefault(n, []).append((int(c.group(1)) if c else None, line.strip()[:60]))

for n in sorted(set(pages) - set(bullets)):
    add(problems, 'radical page not listed on Radicals.md', f'Radical {n}')
for n in sorted(set(bullets) - set(pages)):
    add(problems, 'wanted: Radicals.md links a radical page that does not exist', f'Radical {n}')
for n, lst in sorted(bullets.items()):
    if len(lst) > 1:
        add(problems, 'radical listed more than once on Radicals.md', f'Radical {n} x{len(lst)}')
    c, line = lst[0]
    if n in pages:
        truth = count.get(pages[n][0], 0)
        if c is None:
            add(problems, 'bullet on Radicals.md has no "(N characters)" count', f'Radical {n}')
        elif c != truth:
            add(problems, 'count on Radicals.md is out of date', f'Radical {n} ({pages[n][0]}): page says {c}, characters say {truth}')
        sz = pages[n][1]
        if sz is not None and sz.isdigit() and int(sz) != truth:
            add(warnings, 'radical page `size:` differs from the characters', f'Radical {n}: size {sz}, characters {truth}')

print(f'{len(pages)} radical pages, {len(bullets)} bullets on Radicals.md, {nchars} characters, cutoff {CUTOFF}')
total = 0
for k, v in problems.items():
    total += len(v)
    print(f'\n{k}: {len(v)}')
    for x in v[:25]:
        print('   ', x)
    if len(v) > 25:
        print(f'    ... and {len(v) - 25} more')
for k, v in warnings.items():
    print(f'\n(warning) {k}: {len(v)}')
    for x in v[:10]:
        print('   ', x)

if total:
    print(f'\nFAIL: {total} problems; Radicals.md not stamped.')
    sys.exit(1)

print('\nPASS: all checks clean.')
if STAMP:
    new = re.sub(r'^(date-last-perfect:)[ \t]*.*$', r'\1 ' + TODAY.isoformat(), text, count=1, flags=re.M)
    open(INDEX, 'w').write(new)
    print(f'Stamped {INDEX} date-last-perfect: {TODAY.isoformat()}')
