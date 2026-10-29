#!/usr/bin/env python3
"""lint Words: report-only audit of words/*.md against checklist_words.md, then stamp lookup/Words.md if clean.

Run from the vault root:  python3 AIOS/scripts/lint_words.py [--no-stamp] [--deep] [--max N]

Files are listed through git (tracked + untracked, skipping any that no longer exist), so nothing outside the
page files is read.

Tier A  corpus-wide, every run
  A1  frontmatter present; the `word` tag
  A2  every `characters:` entry is the exact name of a character file (`X.md` or `X (char).md`)
  A3  the file name is the characters joined, or its distinct characters listed once each in first-appearance
      order (a repeated character need not be listed again); affix words named with － and the V pattern are exempt
  A4  homophones: words with the same 注音 each carry a `>[!warning] Homophones` callout naming all the others
Tier B  per page, every run (frontmatter only)
  B1  required keys; the four languages mandarin/cantonese/japanese/korean are counted as a to-do, not a failure
  B2  `pos` is one of the legal values and not blank
  B3  `english` is a non-empty list
  B4  `kwin` is true exactly when 諺文 equals `korean` (final ㄹ counts as ㄷ; 읫 counts as 의)
  B5  注音 / 羅馬字 / 諺文 equal the constituent characters' values joined (dots and apostrophes ignored);
      the character page is the authority, so a stale word is the defect
Tier C  body and cross-file; only pages changed since their own `date-last-perfect` (or unstamped), or all with --deep
  C1  `## Notes` exists and the meta-bind-embed comes before it
  C2  every markdown link and [[wikilink]] in the body resolves to a file
  C3  the `lexipedia:` property and the "- See [Domain](../lexipedia/Domain.md)" bullets name the same domains,
      and each domain page links the word
Not checked: prose, readings against outside sources, syllable-boundary dots (the vault-wide audit of
2026-09-28 owns those; the legal-syllable grammar is too large to re-derive here).

Ground truth is the working tree, so uncommitted edits count. Never edits except the final stamp.
"""
import os, re, subprocess, sys, datetime, collections, urllib.parse

ARGS = sys.argv[1:]
DEEP = '--deep' in ARGS
STAMP = '--no-stamp' not in ARGS
MAXN = int(ARGS[ARGS.index('--max') + 1]) if '--max' in ARGS else 12
TODAY = datetime.date.today()

# Words whose sound deliberately departs from their characters (documented in the word's or character's Notes)
SOUND_EXCEPTIONS = {'棕枝', '棕枝主日', '反乱', '就鳥', '海就', '白頭就', '禿就', '得点', '特点',
                    '杜選', '瞻妄', '統率', '率性', '釩金', '蓬藁'}

def sh(*a):
    return subprocess.run(a, capture_output=True, text=True, check=True).stdout

def listing(folder):
    out = sh('git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z', folder)
    return sorted(f for f in out.split('\0') if f.endswith('.md') and f.count('/') == 1 and os.path.exists(f))

def read(p):
    try:
        return open(p, errors='ignore').read()
    except OSError:
        return None

def split_fm(t):
    m = re.match(r'---\n(.*?)\n---\n?', t, re.S)
    return (m.group(1), t[m.end():]) if m else (None, t)

def fm_scalar(fm, key):
    m = re.search(rf'^{re.escape(key)}:[ \t]*(.*)$', fm, re.M)
    if not m: return None
    v = m.group(1).strip()
    if len(v) >= 2 and v[0] in '"\'' and v[-1] == v[0]: v = v[1:-1]
    return v

def fm_list(fm, key):
    m = re.search(rf'^{re.escape(key)}:[ \t]*(.*)$', fm, re.M)
    if not m: return None
    out = []
    for line in fm[m.end():].split('\n')[1:]:
        mm = re.match(r'^\s*-\s*(.*)$', line)
        if mm: out.append(mm.group(1).strip().strip('"\''))
        else: break
    return out

problems = collections.OrderedDict()
todo = collections.Counter()
def add(code, msg, who):
    problems.setdefault((code, msg), []).append(who)

# ---------------------------------------------------------------- load
LEGAL_POS = {'事詞', '名詞', '性詞', '固有名詞', '数詞', '修飾語', '量詞', '実詞', '副用名詞', '感詞', '格助詞', '関詞',
             '代詞', '連接詞', '副詞', '系詞', '助詞', '派生辞', '擬詞'}
chars = {}
for f in listing('characters'):
    t = read(f)
    if not t: continue
    fm, _ = split_fm(t)
    if fm is None: continue
    chars[os.path.basename(f)[:-3]] = dict(r=fm_scalar(fm, '羅馬字') or '', h=fm_scalar(fm, '諺文') or '', z=fm_scalar(fm, '注音') or '')

words = {}
for f in listing('words'):
    stem = os.path.basename(f)[:-3]
    t = read(f)
    if t is None:
        add('A1', 'unreadable file', stem); continue
    fm, body = split_fm(t)
    if fm is None:
        add('A1', 'no frontmatter', stem); continue
    words[stem] = dict(file=f, fm=fm, body=body)

# ---------------------------------------------------------------- Tier A / B
def strip_marks(x): return x.replace('·', '').replace("'", '').replace('’', '')
def final_ld(x):
    # kwin rules: a Korean final ㄹ counts as ㄷ (any syllable); 읫 counts as 의
    if not x: return x
    x = x.replace('읫', '의')
    out = []
    for c in x:
        o = ord(c) - 0xAC00
        if 0 <= o < 11172 and o % 28 == 8: c = chr(ord(c) - 1)
        out.append(c)
    return ''.join(out)

by_sound = collections.defaultdict(list)
for stem, w in words.items():
    fm = w['fm']; g = lambda k: fm_scalar(fm, k)
    tags = fm_list(fm, 'tags') or []
    if 'word' not in tags and not re.search(r'^\s+-\s*word\b', fm, re.M):
        add('A1', 'missing the `word` tag', stem)
    stems = fm_list(fm, 'characters') or []
    w['stems'] = stems
    for s in stems:
        if s not in chars:
            hint = ' (' + s + ' (char) exists)' if s + ' (char)' in chars else ''
            add('A2', '`characters:` entry is not an exact character file name' + ('' if not hint else ' (the file carries the " (char)" suffix)'), f'{stem}: {s}')
    exempt = stem.startswith('－') or 'V' in stem
    have = [s.replace(' (char)', '') for s in stems]
    need = list(dict.fromkeys(stem))                  # distinct characters, first-appearance order
    if stems and not exempt and ''.join(have) != stem and have != need:
        add('A3', 'file name is not the characters joined (a repeated character may be listed once)', f'{stem} ({" ".join(stems)})')
    w['deduped'] = bool(stems) and not exempt and ''.join(have) != stem and have == need
    zy = g('注音')
    if zy: by_sound[zy].append(stem)
    for k in ('characters', '羅馬字', '諺文', 'english', 'pos', '注音', 'kwin', 'date-last-perfect', 'tags'):
        if not re.search(rf'^{re.escape(k)}:', fm, re.M):
            add('B1', f'missing key `{k}`', stem)
    for k in ('mandarin', 'cantonese', 'japanese', 'korean'):
        if not re.search(rf'^{k}:', fm, re.M):
            todo[f'no `{k}` field (omitted, not yet sourced)'] += 1
    pos = g('pos')
    if pos == '':
        pos_list = fm_list(fm, 'pos') or []                   # several parts of speech are written as a YAML list
        for q in pos_list:
            if q not in LEGAL_POS: add('B2', f'pos {q!r} is not a legal part of speech', stem)
        if not pos_list: add('B2', 'pos is blank', stem)
    elif pos is not None and pos not in LEGAL_POS:
        add('B2', f'pos {pos!r} is not a legal part of speech', stem)
    en = fm_list(fm, 'english')
    if re.search(r'^english:', fm, re.M) and not en and not g('english'):
        add('B3', 'english is empty', stem)
    kw, ko, hg = g('kwin'), g('korean'), g('諺文')
    if kw is not None and ko is not None and hg is not None:
        should = 'true' if final_ld(ko) == final_ld(hg) else 'false'
        if str(kw).lower() != should:
            add('B4', f'kwin is {kw} but 諺文 vs korean says {should}', f'{stem} ({hg} vs {ko})')
    seq = stems
    if w.get('deduped'):                              # repeats listed once: take the sound from the file name
        seq = [c if c in chars else (c + ' (char)' if c + ' (char)' in chars else c) for c in stem]
    if stems and all(s in chars for s in seq) and stem not in SOUND_EXCEPTIONS:
        cz = ''.join(chars[s]['z'] for s in seq); cr = ''.join(chars[s]['r'] for s in seq); ch = ''.join(chars[s]['h'] for s in seq)
        if zy and strip_marks(zy) != strip_marks(cz):
            add('B5', '注音 differs from the characters joined', f'{stem} ({zy} vs {cz})')
        rm = g('羅馬字')
        if rm and strip_marks(rm) != strip_marks(cr):
            add('B5', '羅馬字 differs from the characters joined', f'{stem} ({rm} vs {cr})')
        if hg and hg != ch:
            add('B5', '諺文 differs from the characters joined', f'{stem} ({hg} vs {ch})')

# A4 homophones
def callout_members(body):
    m = re.search(r'>\s*\[!warning\]\s*Homophones\s*\n((?:>.*\n?)*)', body)
    if not m: return None
    block = m.group(1)
    out = set()
    for t in re.findall(r'\[\[([^\]|#]+)(?:\|[^\]]*)?\]\]', block): out.add(urllib.parse.unquote(t).strip())
    for t in re.findall(r'\]\(([^)]*)\)', block):
        t = urllib.parse.unquote(t).rsplit('/', 1)[-1]
        out.add(t[:-3] if t.endswith('.md') else t)
    return out
for zy, ws in by_sound.items():
    if len(ws) < 2: continue
    for w in ws:
        mem = callout_members(words[w]['body'])
        others = set(ws) - {w}
        if mem is None:
            add('A4', 'shares its 注音 with another word but has no Homophones callout', f'{w} ({zy}: also {" ".join(sorted(others))})')
        else:
            gone = others - mem
            if gone:
                add('A4', 'Homophones callout omits a word with the same 注音', f'{w} -> {" ".join(sorted(gone))}')

# ---------------------------------------------------------------- Tier C
def last_modified():
    out = sh('git', 'log', '--name-only', '--format=@%cs', '--', 'words')
    mod = {}; cur = None
    for line in out.split('\n'):
        if line.startswith('@'): cur = line[1:]
        elif line.strip() and cur and line not in mod: mod[line] = cur
    for e in sh('git', 'status', '--porcelain', '-z', '--', 'words').split('\0'):
        if len(e) > 3: mod[e[3:]] = TODAY.isoformat()
    return mod

mod = last_modified()
all_stems = set()
for folder in ('words', 'characters', 'chengyu', 'lexipedia', 'lookup', 'grammar', 'syllables', 'nav', 'AIOS', 'translation', 'bible', 'lessons', 'templates'):
    try:
        for f in sh('git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z', folder).split('\0'):
            if f.endswith('.md') and os.path.exists(f): all_stems.add(os.path.basename(f)[:-3]); all_stems.add(f[:-3])
    except subprocess.CalledProcessError:
        pass
lex_text = {os.path.basename(f)[:-3]: read(f) or '' for f in listing('lexipedia')}

checked = 0
for stem, w in words.items():
    stamp = fm_scalar(w['fm'], 'date-last-perfect')
    lm = mod.get(w['file'])
    needs = DEEP or not stamp or (lm and stamp and lm > stamp)
    if not stamp: add('C0', 'no date-last-perfect', stem)
    if not needs: continue
    checked += 1
    body = w['body']
    if not re.search(r'^## Notes\s*$', body, re.M):
        add('C1', 'no `## Notes` section', stem)
    em = re.search(r'```meta-bind-embed', body); nm = re.search(r'^## Notes', body, re.M)
    if not em:
        add('C1', 'no meta-bind-embed block', stem)
    elif nm and em.start() > nm.start():
        add('C1', 'the meta-bind-embed comes after `## Notes`', stem)
    # C2 links (skip code fences)
    prose = re.sub(r'```.*?```', '', body, flags=re.S)
    for m in re.finditer(r'(?<!\!)\[[^\]]*\]\(((?:[^()\s]|\([^()]*\))+)\)', prose):
        tgt = m.group(1)
        if re.match(r'^(https?:|mailto:|#)', tgt): continue
        tgt = urllib.parse.unquote(tgt.split('#')[0])
        if not tgt: continue
        base = tgt.lstrip('/')
        cands = [os.path.normpath(os.path.join('words', tgt)), base, os.path.normpath(base)]
        if tgt.startswith('/'): cands = [base]
        if not any(os.path.exists(c) for c in cands) and not any(os.path.exists(c + '.md') for c in cands):
            add('C2', 'a markdown link does not resolve', f'{stem}: {tgt}')
    for m in re.finditer(r'\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]', prose):
        name = urllib.parse.unquote(m.group(1)).strip()
        if name and name not in all_stems and name.rsplit('/', 1)[-1] not in all_stems:
            add('C2', 'a [[wikilink]] does not resolve', f'{stem}: [[{name}]]')
    # C3 lexipedia
    prop = set(fm_list(w['fm'], 'lexipedia') or [])
    bullets = set(urllib.parse.unquote(x) for x in re.findall(r'^- See \[[^\]]*\]\(\.\./lexipedia/([^)]+?)\.md\)', body, re.M))
    if prop != bullets:
        add('C3', '`lexipedia:` property and the "See" bullets name different domains', f'{stem}: property {sorted(prop)} vs bullets {sorted(bullets)}')
    for d in prop:
        if d in lex_text and f'words/{stem}.md' not in lex_text[d].replace('%20', ' ') and f'[[{stem}]]' not in lex_text[d] and f'[[{stem}|' not in lex_text[d]:
            add('C3', 'the lexipedia domain page does not link this word', f'{stem} -> {d}')

print(f'{len(words)} words; Tier C run on {checked} ({"all, --deep" if DEEP else "changed since their stamp, or unstamped"})')
for k, v in sorted(todo.items()):
    print(f'(to do, not a failure) {k}: {v}')

if not problems:
    print('PASS: all checks clean.')
    if STAMP and os.path.exists('lookup/Words.md'):
        p = 'lookup/Words.md'; t = open(p).read()
        open(p, 'w').write(re.sub(r'^date-last-perfect:.*$', f'date-last-perfect: {TODAY.isoformat()}', t, count=1, flags=re.M))
        print(f'Stamped {p} date-last-perfect: {TODAY.isoformat()}')
    sys.exit(0)

byc = collections.Counter()
for (code, msg), who in problems.items(): byc[code] += len(who)
print()
for (code, msg), who in sorted(problems.items(), key=lambda kv: (kv[0][0], -len(kv[1]))):
    print(f'[{code}] {msg}: {len(who)}')
    for x in who[:MAXN]: print(f'     {x}')
    if len(who) > MAXN: print(f'     ... and {len(who) - MAXN} more')
print()
print('FAIL: ' + ', '.join(f'{c} {n}' for c, n in sorted(byc.items())) + ('; lookup/Words.md not stamped.' if STAMP else ''))
sys.exit(1)
