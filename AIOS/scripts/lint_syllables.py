#!/usr/bin/env python3
"""lint Syllables: report-only audit of the syllable pages, then stamp syllables/Syllables.md if everything passes.

Run from the vault root:  python3 AIOS/scripts/lint_syllables.py [--no-stamp] [--days N]

Checks (all five must pass before Syllables.md is stamped):
  1. Every character's `注音` names an existing syllable page (syllables/<注音>.md). A character with a blank
     or missing 注音 also fails.
  2. Every syllable page (syllables/*.md except Syllables.md) is linked from syllables/Syllables.md.
  3. Nothing on Syllables.md is a plain-text entry for a syllable that actually has a page (an unlinked name
     whose page exists counts as "missing from the list").
  4. Every syllable page has a `date-last-perfect` no older than N days (default 30).
  5. No wanted syllables: no link on Syllables.md, and no character `注音`, points to a syllable page
     that does not exist.

On a clean run it sets `date-last-perfect:` in syllables/Syllables.md to today's date. It never edits any
other file. Exit status 0 if clean, 1 otherwise.
"""
import re, subprocess, sys, datetime, os, urllib.parse, collections

DAYS = 30
if '--days' in sys.argv:
    DAYS = int(sys.argv[sys.argv.index('--days') + 1])
STAMP = '--no-stamp' not in sys.argv
TODAY = datetime.date.today()
CUTOFF = TODAY - datetime.timedelta(days=DAYS)

def git_files(prefix):
    out = subprocess.check_output(['git', 'ls-files', '-z', prefix], text=True).split('\0')
    return [f for f in out if f.endswith('.md')]

def fm_get(text, key):
    m = re.match(r'---\n(.*?)\n---', text, re.S)
    if not m:
        return None
    k = re.search(r'^%s:[ \t]*"?([^"\n]*)"?[ \t]*$' % re.escape(key), m.group(1), re.M)
    return k.group(1).strip() if k else None

syl_files = [f for f in git_files('syllables/') if f != 'syllables/Syllables.md']
syl_names = {os.path.basename(f)[:-3] for f in syl_files}
page = open('syllables/Syllables.md').read()

problems = collections.OrderedDict()
def add(k, v): problems.setdefault(k, []).append(v)

# --- parse Syllables.md: linked names, and the plain-text names in the grid lines
linked = []
for m in re.finditer(r'\[\[([^\]|#]+)(?:\|[^\]]*)?\]\]', page):
    linked.append(urllib.parse.unquote(m.group(1)).strip())
for m in re.finditer(r'\]\((?:\.\./)?(?:syllables/)?([^)]+?)\.md\)', page):
    linked.append(urllib.parse.unquote(m.group(1)).strip())
linked_set = set(linked)
# syllable-shaped tokens in grid bullet lines ("- ㄈ : a, b, c"), linked or not
grid_tokens = set()
for line in page.split('\n'):
    if re.match(r'^- \S+ ?:', line):
        body = line.split(':', 1)[1]
        body = re.sub(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', r'\1', body)
        body = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', body)
        for tok in re.split(r'[,\s]+', body):
            if tok:
                grid_tokens.add(tok)

# --- 2/3: pages missing from the list
for n in sorted(syl_names - linked_set):
    add('syllable page not linked from Syllables.md', n)
# --- 5a: links on Syllables.md with no page
for n in sorted(x for x in linked_set if x not in syl_names and re.fullmatch(r'[ㄅ-ㄩㆠ-ㆺ⼀-⿕⺀-⻳·]+', x)):
    add('wanted: Syllables.md links a syllable with no page', n)

# --- 4: freshness
for f in sorted(syl_files):
    n = os.path.basename(f)[:-3]
    d = fm_get(open(f).read(), 'date-last-perfect')
    if not d:
        add('no date-last-perfect', n)
        continue
    try:
        dd = datetime.date.fromisoformat(d)
    except ValueError:
        add('unparseable date-last-perfect', f'{n}: {d}')
        continue
    if dd < CUTOFF:
        add(f'date-last-perfect older than {DAYS} days', f'{n}: {d}')

# --- 1/5b: characters
nchar = 0
for f in git_files('characters/'):
    try:
        t = open(f).read()
    except OSError:
        continue
    zy = fm_get(t, '注音')
    if zy is None:
        continue_ = False
        # only characters (tagged character) are expected to carry a 注音
        if re.search(r'^tags:[\s\S]*?-\s*character', t[:t.find('\n---', 3)] if t.startswith('---') else '', re.M):
            add('character has no 注音', os.path.basename(f)[:-3])
        continue
    nchar += 1
    zy = zy.replace('·', '')
    if not zy:
        add('character has blank 注音', os.path.basename(f)[:-3])
    elif zy not in syl_names:
        add('wanted: character 注音 has no syllable page', f'{os.path.basename(f)[:-3]} -> {zy}')

print(f'{len(syl_names)} syllable pages, {len(linked_set)} distinct links on Syllables.md, {nchar} characters with a 注音, cutoff {CUTOFF}')
total = 0
for k, v in problems.items():
    total += len(v)
    print(f'\n{k}: {len(v)}')
    for x in v[:25]:
        print('   ', x)
    if len(v) > 25:
        print(f'    ... and {len(v) - 25} more')

if total:
    print(f'\nFAIL: {total} problems; Syllables.md not stamped.')
    sys.exit(1)

print('\nPASS: all five checks clean.')
if STAMP:
    new = re.sub(r'^(date-last-perfect:)[ \t]*.*$', r'\1 ' + TODAY.isoformat(), page, count=1, flags=re.M)
    if new == page and f'date-last-perfect: {TODAY.isoformat()}' not in page:
        print('could not find a date-last-perfect line to update in Syllables.md')
        sys.exit(1)
    open('syllables/Syllables.md', 'w').write(new)
    print(f'Stamped syllables/Syllables.md date-last-perfect: {TODAY.isoformat()}')
