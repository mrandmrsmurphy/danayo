#!/usr/bin/env python3
"""lint SKIP: report-only audit of lookup/SKIP/, then stamp lookup/SKIP/SKIP.md if clean.

Run from the vault root:  python3 AIOS/scripts/lint_skip.py [--no-stamp] [--days N]

Ground truth is the `skip_number:` field of every character page. Pages are of three kinds:
  leaf   SKIP-a-b-c.md       one per code; lists the characters with that code (may be empty: forbidden/alias only)
  stem   SKIP-a-b.md         lists the leaves SKIP-a-b-*  (SKIP-4-0-K instead lists the leaves SKIP-4-*-K)
  top    SKIP.md             links every SKIP-a-b stem and the four SKIP-4-0-K pages

Checks (all must pass before SKIP.md is stamped):
  Leaves  1. a leaf exists for every skip_number that some character carries
          2. frontmatter has stroke_count, size, skip_number, date-last-perfect; skip_number matches the file name
          3. the numbered entries are exactly the characters carrying that code, and `size` equals their count
             (aliases, forbidden marks and redirects are not entries; a leaf with no entries and size 0 is fine)
          4. the Datacheck query's skip_number equals the frontmatter
  Stems   5. `size` equals the sum of its leaves' sizes
          6. every existing leaf is linked, every position from 1 to the highest is listed (missing ones say none/no)
          7. each preview shows exactly the characters in its leaf (no truncation, no extras)
          8. a `## Base check` block is present
  Top     9. SKIP.md `size` equals the total character count; every stem and SKIP-4-0-K page is linked as a real link
  All    10. every leaf and stem has a date-last-perfect no older than N days (default 30)

On a clean run it sets `date-last-perfect:` in SKIP.md to today's date. It edits no other file.
Exit status 0 if clean, 1 otherwise.
"""
import re, subprocess, sys, datetime, collections

DAYS = 30
if '--days' in sys.argv:
    DAYS = int(sys.argv[sys.argv.index('--days') + 1])
STAMP = '--no-stamp' not in sys.argv
TODAY = datetime.date.today()
CUTOFF = TODAY - datetime.timedelta(days=DAYS)
TOP = 'lookup/SKIP/SKIP.md'
CJK = re.compile('[⺀-鿿㐀-䶿豈-﫿\U00020000-\U0003ffff]')

def git_files(prefix):
    return [f for f in subprocess.check_output(['git', 'ls-files', '-z', prefix], text=True).split('\0') if f.endswith('.md')]

def fm_block(t):
    m = re.match(r'---\n(.*?)\n---', t, re.S)
    return m.group(1) if m else ''

def fm_get(t, key):
    k = re.search(r'^%s:[ \t]*"?([^"\n]*)"?[ \t]*$' % re.escape(key), fm_block(t), re.M)
    return k.group(1).strip() if k else None

problems = collections.OrderedDict()
def add(k, v): problems.setdefault(k, []).append(v)

def fresh(name, t):
    d = fm_get(t, 'date-last-perfect')
    if not d:
        add('no date-last-perfect', name); return
    try:
        if datetime.date.fromisoformat(d) < CUTOFF:
            add(f'date-last-perfect older than {DAYS} days', f'{name} ({d})')
    except ValueError:
        add('unparseable date-last-perfect', f'{name} ({d})')

# ---------- ground truth
truth = collections.defaultdict(set)
for f in git_files('characters/'):
    t = open(f).read()
    k = fm_get(t, 'skip_number')
    if k:
        truth[k].add(f.split('/')[-1][:-3].replace(' (char)', ''))
total_chars = sum(len(v) for v in truth.values())

# ---------- leaves
leaves = {}   # code -> (size, entries)
for f in git_files('lookup/SKIP/'):
    m = re.search(r'SKIP-(\d)-(\d+)-(\d+)\.md$', f)
    if not m or m.group(2) == '0':
        continue
    code = '-'.join(m.groups())
    t = open(f).read()
    name = f'SKIP-{code}'
    fresh(name, t)
    for key in ('stroke_count', 'size', 'skip_number', 'date-last-perfect'):
        if fm_get(t, key) is None:
            add('leaf frontmatter field missing', f'{name}: {key}')
    if fm_get(t, 'skip_number') not in (None, code):
        add('skip_number differs from file name', f'{name}: {fm_get(t, "skip_number")}')
    body = re.split(r'^## Data ?check', t, maxsplit=1, flags=re.M)[0]
    body = re.split(r'^###? (?:Aliases|Forbidden)', body, maxsplit=1, flags=re.M)[0]
    ents = set()
    for l in re.findall(r'(?m)^\d+\. (.*)$', body):
        if '-->' in l:
            add('alias formatted as a numbered entry', f'{name}: {l[:40]}')
            continue
        m2 = re.search(r'\[\[([^\]|]+?)(?:\||\]\])', l) or re.search(r'\[([^\]]+)\]\(', l)
        if m2:
            ents.add(m2.group(1).replace(' (char)', ''))
    size = fm_get(t, 'size')
    if size is not None and size.isdigit() and int(size) != len(ents):
        add('leaf size differs from entry count', f'{name}: size {size}, entries {len(ents)}')
    tr = truth.get(code, set())
    if ents != tr:
        add('leaf entries differ from the characters carrying the code',
            f'{name}: missing {sorted(tr - ents)} extra {sorted(ents - tr)}')
    q = re.search(r'skip_number = "([^"]*)"', t)
    if q and q.group(1) != code:
        add('Datacheck skip_number differs from frontmatter', f'{name}: {q.group(1)}')
    elif not q:
        add('leaf has no Datacheck skip_number query', name)
    leaves[code] = (len(ents), ents)

for code in sorted(set(truth) - set(leaves)):
    add('character code with no leaf file', f'SKIP-{code} ({len(truth[code])} characters)')

# ---------- stems
def children(stem):
    """Return the leaf codes belonging to a stem page named SKIP-a-b or SKIP-4-0-K."""
    a, b = stem[0], stem[1]
    if b == 0:
        return {c: v for c, v in leaves.items() if c.split('-')[0] == str(a) and c.split('-')[2] == str(stem[2])}
    return {c: v for c, v in leaves.items() if c.split('-')[:2] == [str(a), str(b)]}

stems = {}
for f in git_files('lookup/SKIP/'):
    m = re.search(r'SKIP-(\d)-(\d+)\.md$', f)
    m0 = re.search(r'SKIP-4-0-(\d)\.md$', f)
    if not (m or m0):
        continue
    key = (4, 0, int(m0.group(1))) if m0 else (int(m.group(1)), int(m.group(2)))
    t = open(f).read()
    name = 'SKIP-' + '-'.join(map(str, key))
    fresh(name, t)
    kids = children(key)
    want = sum(v[0] for v in kids.values())
    size = fm_get(t, 'size')
    if size is None:
        add('stem has no size', name)
    elif size != str(want):
        add('stem size differs from the sum of its leaves', f'{name}: size {size}, leaves sum {want}')
    stems[key] = want
    if not re.search(r'^## Base check', t, re.M):
        add('stem has no Base check block', name)
    # position -> (code or None, preview text); numbered lists carry the position as the list number,
    # gaps are bare lines (none / no / ø); SKIP-4-0-1 uses a table of (header link, characters) cell pairs
    pos = lambda code: int(code.split('-')[2]) if key[1] != 0 else int(code.split('-')[1])
    entries = {}     # position -> (code or None, text)
    lines = t.split('\n')
    for k, l in enumerate(lines):
        mn = re.match(r'(?:(\d+)\.|[-*]) (.*)$', l)
        if mn:
            body = mn.group(2)
            mm = re.search(r'SKIP[-/](\d)[-/](\d+)[-/](\d+)', body)
            if mm:
                code = '-'.join(mm.groups())
                islink = bool(re.search(r'\]\(|\[\[SKIP', body))
                rest = re.sub(r'\[\[SKIP[^\]]*\]\]|\[[^\]]*\]\([^)]*\)', '', body, count=1)
                entries[pos(code)] = (code, rest if islink else None)
            elif mn.group(1):
                entries[int(mn.group(1))] = (None, body)
        elif l.startswith('|') and k + 2 < len(lines) and '[[SKIP-' in l:
            heads = [c.strip() for c in l.strip().strip('|').split('|')]
            nxt = k + 2 if lines[k + 1].startswith('|-') else k + 1
            row = [c.strip() for c in lines[nxt].strip().strip('|').split('|')]
            for h, r in zip(heads, row):
                mm = re.search(r'SKIP-(\d)-(\d+)-(\d+)', h)
                if mm:
                    entries[pos('-'.join(mm.groups()))] = ('-'.join(mm.groups()), r)
    for code, (n, ents) in sorted(kids.items(), key=lambda x: [int(p) for p in x[0].split('-')]):
        got = entries.get(pos(code))
        if not got or got[0] != code or got[1] is None:
            add('stem does not link an existing leaf', f'{name}: SKIP-{code}')
            continue
        text = got[1]
        if '...' in text or '\u2026' in text:
            add('stem preview is truncated', f'{name}: SKIP-{code}')
        shown = set(CJK.findall(re.sub(r'\(.*?\)', '', text)))
        if shown != ents:
            add('stem preview differs from its leaf', f'{name}: SKIP-{code} missing {sorted(ents - shown)} extra {sorted(shown - ents)}')
    for p_, (code, text) in entries.items():
        if code and text is not None and code not in kids:
            add('stem links a leaf that does not exist', f'{name}: SKIP-{code}')
        if code is None and not re.fullmatch(r'\s*(none|no|\u00f8)\b.*', text, re.I):
            add('stem gap line is not none/no/\u00f8', f'{name}: position {p_}: {text[:30]}')
    top_pos = max([pos(c) for c in kids] + list(entries) + [0])
    gaps = [p_ for p_ in range(1, top_pos + 1) if p_ not in entries]
    if gaps:
        add('stem leaves positions unlisted (write none/no)', f'{name}: {gaps}')

# ---------- top page
t = open(TOP).read()
size = fm_get(t, 'size')
if size is None:
    add('top page has no size', 'SKIP.md')
elif size != str(total_chars):
    add('top size differs from the total character count', f'SKIP.md: size {size}, characters {total_chars}')
links = set(re.findall(r'\]\(lookup/SKIP/SKIP-\d/SKIP-(\d+-\d+(?:-\d+)?)\.md\)', t))
for key in stems:
    s = '-'.join(map(str, key))
    if s not in links:
        add('top page does not link a stem as a real link', f'SKIP-{s}')

# ---------- report
n_leaf, n_stem = len(leaves), len(stems)
if problems:
    for k, v in problems.items():
        print(f'{k} ({len(v)}):')
        for x in v[:40]:
            print('  ', x)
        if len(v) > 40:
            print(f'   ... and {len(v) - 40} more')
    print(f'\nFAIL: {sum(len(v) for v in problems.values())} problems across {n_leaf} leaves and {n_stem} stems; SKIP.md not stamped.')
    sys.exit(1)

print(f'OK: {n_leaf} leaves and {n_stem} stems agree with {total_chars} characters.')
if STAMP:
    t2 = re.sub(r'(?m)^date-last-perfect: .*$', f'date-last-perfect: {TODAY.isoformat()}', t, count=1)
    if t2 != t:
        open(TOP, 'w').write(t2)
    print(f'Stamped SKIP.md date-last-perfect: {TODAY.isoformat()}')
else:
    print('(--no-stamp: SKIP.md not stamped)')
