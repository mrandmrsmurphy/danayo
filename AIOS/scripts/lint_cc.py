#!/usr/bin/env python3
"""lint CC: report-only audit of lookup/CC/initials, lookup/CC/finals and grammar/文法 - 99韻図.md, then stamp
lookup/CC/Classical Chinese.md if clean.

Run from the vault root:  python3 AIOS/scripts/lint_cc.py [--no-stamp] [--days N] [--min-d PCT]

Ground truth is the `middle_chinese_initial:` and `middle_chinese_final:` fields of every character page. Each
聲 X.md / 韻 X.md page carries its own value of that field, which joins pages to characters.

Checks (all blocking except the last):
  Characters  1. every character's initial and final value is the value of an existing 聲 / 韻 page (no stray or
                 look-alike glyphs such as script ɡ for g, or a for ɑ)
  Pages       2. `size` equals the number of characters carrying the page's value
              3. the page's Datacheck base filters on file.inFolder("characters") and on its own value
              4. date-last-perfect no older than N days (default 30)
  Zero pages  5. pages with no characters are listed (legitimate for a few marginal rime-table slots; reported only)
  Rime table  6. grammar/文法 - 99韻図.md: every 韻 page is a row of the Vowels table exactly once, every link in the
                 table points at a page that exists, and the Consonants/Names tables link every 聲 page
              7. the Dan'a'yo (D) column of the Vowels table "need only be 80% accurate": scored against the 羅馬字
                 of the characters of each final, ignoring the stop-final spelling (g/d/b = k/t/p) and a leading y/w
                 medial, the table as a whole must reach --min-d percent (default 80). Rows below 80% are listed as
                 advisory only.
  Links       8. no wanted (red) links: every [[wikilink]] and (relative path) link on a CC page or the 韻図 page resolves
  Top page    9. Classical Chinese.md carries the Initials Check and Finals Check base queries on the right folders

On a clean run it sets `date-last-perfect:` in Classical Chinese.md to today's date (adding the field if absent).
It edits no other file. Exit status 0 if clean, 1 otherwise.
"""
import re, subprocess, sys, datetime, collections

DAYS = 30
MIND = 80.0
if '--days' in sys.argv:
    DAYS = int(sys.argv[sys.argv.index('--days') + 1])
if '--min-d' in sys.argv:
    MIND = float(sys.argv[sys.argv.index('--min-d') + 1])
STAMP = '--no-stamp' not in sys.argv
TODAY = datetime.date.today()
CUTOFF = TODAY - datetime.timedelta(days=DAYS)
TOP = 'lookup/CC/Classical Chinese.md'
TABLE = 'grammar/文法 - 99韻図.md'

def git_files(prefix):
    return [f for f in subprocess.check_output(['git', 'ls-files', '-z', prefix], text=True).split('\0') if f.endswith('.md')]

def fm_block(t):
    m = re.match(r'---\n(.*?)\n---', t, re.S)
    return m.group(1) if m else ''

def fm_get(t, key):
    k = re.search(r'^%s:[ \t]*"?([^"\n]*)"?[ \t]*$' % re.escape(key), fm_block(t), re.M)
    return k.group(1).strip() if k else None

problems = collections.OrderedDict()
advisory = collections.OrderedDict()
def add(k, v): problems.setdefault(k, []).append(v)
def note(k, v): advisory.setdefault(k, []).append(v)

# ---------- ground truth
ini = collections.Counter(); fin = collections.Counter()
roman = collections.defaultdict(list)       # final value -> [romanization]
chars_of = {'initial': collections.defaultdict(list), 'final': collections.defaultdict(list)}
for f in git_files('characters/'):
    t = open(f).read()
    name = f.split('/')[-1][:-3].replace(' (char)', '')
    a = fm_get(t, 'middle_chinese_initial'); b = fm_get(t, 'middle_chinese_final'); r = fm_get(t, '羅馬字')
    if a: ini[a] += 1; chars_of['initial'][a].append(name)
    if b:
        fin[b] += 1; chars_of['final'][b].append(name)
        if r: roman[b].append(r)

# ---------- pages
def load(kind, folder, prefix, field):
    pages = {}      # value -> (name, size, text)
    for f in git_files(folder):
        m = re.search(r'/%s (.*)\.md$' % prefix, f)
        if not m:
            continue
        t = open(f).read()
        v = fm_get(t, field)
        nm = prefix + ' ' + m.group(1)
        if v is None:
            add('page has no %s' % field, nm); continue
        if v in pages:
            add('two pages share one value', f'{nm} and {pages[v][0]} ({v})')
        pages[v] = (nm, fm_get(t, 'size'), t)
    return pages

ipages = load('initial', 'lookup/CC/initials/', '聲', 'middle_chinese_initial')
fpages = load('final', 'lookup/CC/finals/', '韻', 'middle_chinese_final')

for kind, counter, pages in (('initial', ini, ipages), ('final', fin, fpages)):
    for v in sorted(set(counter) - set(pages)):
        add(f'character {kind} value with no page (stray or look-alike glyph?)',
            f'{v!r}: {counter[v]} characters {chars_of[kind][v][:6]}')
    for v, (nm, size, t) in sorted(pages.items(), key=lambda x: x[1][0]):
        n = counter.get(v, 0)
        if size is None or not size.isdigit():
            add('page has no size', nm)
        elif int(size) != n:
            add('page size differs from the characters carrying its value', f'{nm}: size {size}, characters {n}')
        if 'file.inFolder("characters")' not in t:
            add('Datacheck lacks the file.inFolder("characters") filter', nm)
        field = 'middle_chinese_%s' % kind
        if not re.search(r'%s == "%s"' % (field, re.escape(v)), t):
            add('Datacheck does not filter on the page\'s own value', nm)
        d = fm_get(t, 'date-last-perfect')
        if not d:
            add('no date-last-perfect', nm)
        else:
            try:
                if datetime.date.fromisoformat(d) < CUTOFF:
                    add(f'date-last-perfect older than {DAYS} days', f'{nm} ({d})')
            except ValueError:
                add('unparseable date-last-perfect', f'{nm} ({d})')
        if n == 0:
            note('pages with no characters (legitimate empty rime-table slots)', nm)

# ---------- rime table
tab = open(TABLE).read()
linked_fin = re.findall(r'韻(?:%20| )([^\]|)\s]+?)(?:\.md)?\]\]?\)?', tab)
rows = []
for l in tab.split('\n'):
    m = re.match(r'\|\s*(\d{3})\s*\|\s*\[\[?(?:韻 )?([^\]|]+?)(?:\]\([^)]*\)|\]\])?\s*\|\s*([^|]*)\|(.*)\|\s*([^|]*)\|?\s*$', l)
    if m:
        rows.append((m.group(1), m.group(2).strip(), m.group(5)))
names_f = {v[0][2:].strip(): k for k, v in fpages.items()}     # '東一' -> value
seen = collections.Counter(n for _, n, _ in rows)
for n in sorted(set(names_f) - set(seen)):
    add('final page is not a row of the 韻図 Vowels table', f'韻 {n}')
for n, c in seen.items():
    if c > 1:
        add('final appears twice in the 韻図 Vowels table', f'韻 {n}')
    if n not in names_f:
        add('Vowels table row names a final page that does not exist', f'韻 {n}')
for n in set(re.findall(r'lookup/CC/initials/聲(?:%20| )([^)\]|]+?)\.md', tab)):
    if not any(v[0] == '聲 ' + n for v in ipages.values()):
        add('Consonants table links an initial page that does not exist', f'聲 {n}')
linked_i = set(re.findall(r'lookup/CC/initials/聲(?:%20| )([^)\]|]+?)\.md', tab))
for v, (nm, _, _) in ipages.items():
    if nm[2:].strip() not in linked_i:
        add('initial page is not linked from the 韻図 consonant tables', nm)

def rime(r, loose=True):
    x = re.sub(r'^[^aeiouyw]*', '', r.lower())
    if re.search(r'[aeiouw]g$', x):
        x = x[:-1] + 'k'
    x = re.sub(r'd$', 't', x); x = re.sub(r'b$', 'p', x)
    if loose:
        x = re.sub(r'^[yw]+(?=[aeiou])', '', x)
    return x

tot = ok = 0
low = []
for n, name, d in rows:
    v = names_f.get(name)
    if v is None or not roman.get(v):
        continue
    opts = [re.sub(r'^[yw]+(?=[aeiou])', '', o.strip()) for o in re.sub(r'[*~]', '', d).split('/') if o.strip()]
    rs = roman[v]
    hit = sum(1 for r in rs if rime(r) in opts)
    tot += len(rs); ok += hit
    if hit * 100 < 80 * len(rs):
        low.append((n, name, d.strip(' *'), len(rs), round(100 * hit / len(rs))))
pct = 100.0 * ok / tot if tot else 0.0
if pct < MIND:
    add('Dan\'a\'yo (D) column of the 韻図 Vowels table is below the accuracy bar', f'{pct:.1f}% < {MIND:.0f}%')
for n, name, d, cnt, p in low:
    note('rows of the Vowels table whose D column covers under 80% of the final\'s characters',
         f'{n} 韻 {name}: D = {d}, {p}% of {cnt}')

# ---------- wanted links on CC pages and the rime table
import os, urllib.parse
all_files = set(subprocess.check_output(['git', 'ls-files', '-z'], text=True).split('\0'))
base_names = {os.path.basename(f)[:-3] if f.endswith('.md') else os.path.basename(f) for f in all_files}
for f in git_files('lookup/CC/') + [TABLE]:
    t = re.sub(r'```.*?```', '', open(f).read(), flags=re.S)
    label = f.split('/')[-1][:-3]
    for m in re.finditer(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', t):
        x = m.group(1).split('#')[0].strip()
        if x and not (x in all_files or x + '.md' in all_files or os.path.basename(x) in base_names
                      or os.path.basename(x)[:-3] in base_names):
            add('wanted (red) wikilink', f'{label}: [[{m.group(1)}]]')
    for m in re.finditer(r'\]\(((?:[^()]|\([^)]*\))*)\)', t):
        p = urllib.parse.unquote(m.group(1)).split('#')[0].strip()
        if not p or re.match(r'(https?:|mailto:)', p):
            continue
        if not any(c in all_files for c in (os.path.normpath(os.path.join(os.path.dirname(f), p)), p.lstrip('/'))):
            add('wanted (red) path link', f'{label}: ({p})')

# ---------- top page
top = open(TOP).read()
for label, folder in (('Initials Check', 'lookup/CC/initials'), ('Finals Check', 'lookup/CC/finals')):
    m = re.search(r'^## %s\s*\n```base\n(.*?)```' % label, top, re.S | re.M)
    if not m:
        add('Classical Chinese.md lacks a base block', label)
    elif 'file.inFolder("%s")' % folder not in m.group(1):
        add('Classical Chinese.md base block filters the wrong folder', label)

# ---------- report
for k, v in advisory.items():
    print(f'[advisory] {k} ({len(v)}):')
    for x in v[:12]:
        print('   ', x)
    if len(v) > 12:
        print(f'    ... and {len(v) - 12} more')
print(f'[info] 韻図 Dan\'a\'yo column accuracy: {pct:.1f}% of {tot} characters (bar {MIND:.0f}%)\n')
if problems:
    for k, v in problems.items():
        print(f'{k} ({len(v)}):')
        for x in v[:30]:
            print('  ', x)
        if len(v) > 30:
            print(f'   ... and {len(v) - 30} more')
    print(f'\nFAIL: {sum(len(v) for v in problems.values())} problems; Classical Chinese.md not stamped.')
    sys.exit(1)

print(f'OK: {len(ipages)} initial pages and {len(fpages)} final pages agree with the characters.')
if STAMP:
    if re.match(r'---\n', top) and re.search(r'(?m)^date-last-perfect:', fm_block(top)):
        top2 = re.sub(r'(?m)^date-last-perfect: .*$', f'date-last-perfect: {TODAY.isoformat()}', top, count=1)
    else:
        top2 = re.sub(r'^---\n', f'---\ndate-last-perfect: {TODAY.isoformat()}\n', top, count=1)
    open(TOP, 'w').write(top2)
    print(f'Stamped Classical Chinese.md date-last-perfect: {TODAY.isoformat()}')
else:
    print('(--no-stamp: Classical Chinese.md not stamped)')
