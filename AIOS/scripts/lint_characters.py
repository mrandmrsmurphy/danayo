#!/usr/bin/env python3
"""lint Characters: report-only audit of characters/*.md against checklist_characters.md, then stamp
lookup/Characters.md if clean.

Run from the vault root:  python3 AIOS/scripts/lint_characters.py [--no-stamp] [--deep] [--ids] [--max N]

Files are listed through git (tracked + untracked), so characters/.venv and other non-page files are never read.

Tier A  corpus-wide, every run
  A1  every page has frontmatter and the `character` tag
  A2  `danayo_id`: an integer, unique, inside its grade's block (grade 1 from 1; 2 from 2001; 3 from 3001;
      4 from 4001; 5 from 5001; 6 from 6001; 先進 from 7001; 名 from 8001), and each block is contiguous
      (BASE+1 .. BASE+N, no holes). The next free id per block is printed.
  A3  file name: `X (char).md` exactly when words/X.md exists (a 名専字 never takes the suffix)
Tier B  per page, every run (frontmatter only)
  B1  required keys present; enumerated values legal; stroke_count / mc_id integers; skip_number well formed
  B2  `graphemic_classification` is not the string 形声; `pos` and `stand_in` are not blank
  B3  `注音` names a syllable page, and its 羅馬字 / 諺文 agree with the page's
  B4  `kwin` is true exactly when 諺文 equals `korean` (a final ㄹ counts as ㄷ; 읫 counts as 의)
  B5  `stand_in` is the character itself, an existing word, or 名専字
Tier C  body and cross-file; only pages changed since their own `date-last-perfect` (or unstamped), or all with --deep
  C1  the four Notes bullets exist in order; the SKIP/Stroke, CC and syllable links match the frontmatter
  C2  every word whose `characters:` names this character is in `## Words` with the word's own 注音; every
      `## Words` link resolves. The same for `## Chengyu`.
  C3  `mc_id` equals the rank on lookup/CC/CC 0000-3000.md (only for ranks that appear there)
Not checked: prose, Old Chinese reconstructions, whether a reading is right against sources.

Ground truth is the working tree, so uncommitted edits count. Never edits except the final stamp.
"""
import os, re, subprocess, sys, datetime, collections, urllib.parse

ARGS = sys.argv[1:]
DEEP = '--deep' in ARGS
IDS_ONLY = '--ids' in ARGS
STAMP = '--no-stamp' not in ARGS
MAXN = 12
if '--max' in ARGS:
    MAXN = int(ARGS[ARGS.index('--max') + 1])
TODAY = datetime.date.today()

def sh(*a):
    return subprocess.run(a, capture_output=True, text=True, check=True).stdout

def listing(folder):
    out = sh('git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z', folder)
    return sorted(f for f in out.split('\0') if f.endswith('.md') and '/' in f and f.count('/') == 1 and os.path.exists(f))

def read(p):
    try:
        return open(p, errors='ignore').read()
    except OSError:
        return None

def split_fm(t):
    m = re.match(r'---\n(.*?)\n---\n?', t, re.S)
    return (m.group(1), t[m.end():]) if m else (None, t)

def fm_get(fm, key):
    m = re.search(rf'^{re.escape(key)}:[ \t]*(.*)$', fm, re.M)
    if not m:
        return None
    v = m.group(1).strip()
    if v == '' or v == '|':
        items = re.findall(r'^\s+-\s*(.*)$', fm[m.end():].split('\n', 1)[1] if '\n' in fm[m.end():] else '', re.M)
        # only the contiguous list immediately after the key
        block = []
        for line in fm[m.end():].split('\n')[1:]:
            mm = re.match(r'^\s+-\s*(.*)$', line)
            if mm:
                block.append(mm.group(1).strip().strip('"\''))
            else:
                break
        return block if block else ''
    if len(v) >= 2 and v[0] in '"\'' and v[-1] == v[0]:
        v = v[1:-1]
    return v

problems = collections.OrderedDict()
todo = collections.Counter()
def add(code, msg, who):
    problems.setdefault((code, msg), []).append(who)

# ---------------------------------------------------------------- load
cfiles = listing('characters')
chars = {}
for f in cfiles:
    t = read(f)
    stem = os.path.basename(f)[:-3]
    if t is None:
        add('A1', 'unreadable file', stem); continue
    fm, body = split_fm(t)
    if fm is None:
        add('A1', 'no frontmatter', stem); continue
    chars[stem] = dict(file=f, fm=fm, body=body)

BASE = {'1': 0, '2': 2000, '3': 3000, '4': 4000, '5': 5000, '6': 6000, '先進': 7000, '名': 8000}
GRADES = set(BASE)

# ---------------------------------------------------------------- Tier A
by_grade = collections.defaultdict(list)
idowner = collections.defaultdict(list)
for stem, c in chars.items():
    if 'character' not in (fm_get(c['fm'], 'tags') or []) and not re.search(r'^\s+-\s*character\b', c['fm'], re.M):
        add('A1', 'missing the `character` tag', stem)
    g = fm_get(c['fm'], 'grade_level')
    did = fm_get(c['fm'], 'danayo_id')
    if g not in GRADES:
        add('A2', f'grade_level {g!r} is not one of 1-6, 先進, 名', stem)
        continue
    if not did or not str(did).isdigit():
        add('A2', 'danayo_id missing or not an integer', stem)
        continue
    d = int(did)
    c['gid'] = d; c['grade'] = g
    by_grade[g].append((d, stem))
    idowner[d].append(stem)
for d, owners in sorted(idowner.items()):
    if len(owners) > 1:
        add('A2', f'danayo_id {d} used more than once', ' / '.join(owners))
nextfree = {}
for g, lst in by_grade.items():
    base = BASE[g]; n = len(lst)
    nextfree[g] = base + n + 1
    for d, stem in lst:
        if not (base < d <= base + 999):
            add('A2', f'danayo_id {d} is outside the {g} block ({base + 1}..{base + 999})', stem)
    ids = sorted(d for d, _ in lst)
    want = list(range(base + 1, base + n + 1))
    if ids != want:
        holes = sorted(set(want) - set(ids))
        stray = sorted(set(ids) - set(want))
        if holes:
            add('A2', f'grade {g}: ids missing from {base + 1}..{base + n}', ', '.join(map(str, holes[:40])) + (' ...' if len(holes) > 40 else ''))
        if stray:
            add('A2', f'grade {g}: ids beyond {base + n} (or duplicates)', ', '.join(map(str, stray[:40])) + (' ...' if len(stray) > 40 else ''))

words = {os.path.basename(f)[:-3] for f in listing('words')}
for stem, c in chars.items():
    bare = stem[:-7] if stem.endswith(' (char)') else stem
    suffixed = stem.endswith(' (char)')
    sin = fm_get(c['fm'], 'stand_in')
    if bare in words and not suffixed and sin != '名専字':
        add('A3', 'a word of the same name exists, so the file needs the " (char)" suffix', stem)
    if suffixed and bare not in words:
        add('A3', 'has the " (char)" suffix but no word of that name exists', stem)

# ---------------------------------------------------------------- Tier B
JOYO = {'1', '2', '3', '4', '5', '6', '高等', '表外字', '日本人名用漢字'}
HSK = {'無', '1', '2', '3', '4', '5', '6'}
HANMUN = {'中', '高等', '名', '無'}
REQ = ['mandarin', 'cantonese', 'korean', 'middle_chinese_initial', 'middle_chinese_final', 'stroke_count',
       'radical', 'skip_number', 'grade_level', 'pos', 'english', '羅馬字', '諺文', 'joyo_level', 'hsk_level',
       'hanmun_edu_level', 'danayo_id', 'mc_id', 'graphemic_classification', 'stand_in', '注音', 'kwin']

syl = {}
for f in listing('syllables'):
    t = read(f)
    if not t: continue
    fm, _ = split_fm(t)
    if fm is None: continue
    syl[os.path.basename(f)[:-3]] = (fm_get(fm, '羅馬字'), fm_get(fm, '諺文'))

if not IDS_ONLY:
    for stem, c in chars.items():
        fm = c['fm']
        get = lambda k: fm_get(fm, k)
        for k in REQ:
            if get(k) is None:
                add('B1', f'missing key `{k}`', stem)
        if get('joyo_level') not in JOYO and get('joyo_level') is not None:
            add('B1', f'joyo_level {get("joyo_level")!r} not a legal value', stem)
        if get('hsk_level') not in HSK and get('hsk_level') is not None:
            add('B1', f'hsk_level {get("hsk_level")!r} not a legal value', stem)
        if get('hanmun_edu_level') not in HANMUN and get('hanmun_edu_level') is not None:
            add('B1', f'hanmun_edu_level {get("hanmun_edu_level")!r} not a legal value', stem)
        sc = get('stroke_count')
        if sc is not None and not str(sc).isdigit():
            add('B1', 'stroke_count is not an integer', stem)
        mc = get('mc_id')
        if mc is not None and mc == '':
            todo['mc_id blank (not yet checked)'] += 1
        elif mc is not None and not str(mc).isdigit():
            add('B1', 'mc_id is not an integer', stem)
        sk = get('skip_number')
        if sk is not None and not re.fullmatch(r'\d+-\d+-\d+', str(sk)):
            add('B1', f'skip_number {sk!r} is malformed', stem)
        if get('graphemic_classification') == '形声':
            add('B2', 'graphemic_classification is the string 形声 (store the phonetic component)', stem)
        if get('graphemic_classification') == '':
            add('B2', 'graphemic_classification is blank', stem)
        if get('pos') in ('', None):
            add('B2', 'pos is blank', stem)
        sin = get('stand_in')
        if sin == '':
            add('B2', 'stand_in is blank', stem)
        zy = get('注音')
        if zy and zy not in syl:
            add('B3', 'its 注音 names no syllable page', f'{stem} ({zy})')
        elif zy:
            rm, hg = syl[zy]
            def rn(x):
                x = x.replace("'", '')
                return re.sub(r'[bdg]$', lambda m: {'b': 'p', 'd': 't', 'g': 'k'}[m.group(0)], x)
            if rm and get('羅馬字') and rn(get('羅馬字')) != rn(rm):
                add('B3', '羅馬字 differs from its syllable page', f'{stem} ({get("羅馬字")} vs {rm})')
            if hg and get('諺文') and get('諺文') != hg:
                add('B3', '諺文 differs from its syllable page', f'{stem} ({get("諺文")} vs {hg})')
        kw = get('kwin'); ko = get('korean'); hg = get('諺文')
        if kw is not None and ko is not None and hg is not None:
            def kn(x): return x[:-1] + 'ㄷ' if False else x
            def final_ld(x):
                # Korean final ㄹ counts as ㄷ for kwin (user rule): normalize the last syllable's final
                if not x: return x
                if x[-1] == '읫': x = x[:-1] + '의'              # user rule 2026-10-29: 읫 counts as 의
                c = x[-1]; o = ord(c) - 0xAC00
                if 0 <= o < 11172:
                    fin = o % 28
                    if fin == 8: c = chr(ord(c) - 8 + 7)       # ㄹ(8) -> ㄷ(7)
                return x[:-1] + c
            should = 'true' if final_ld(ko) == final_ld(hg) else 'false'
            if str(kw).lower() != should:
                add('B4', f'kwin is {kw} but 諺文 {hg} vs korean {ko}', stem)
        bare = stem[:-7] if stem.endswith(' (char)') else stem
        if sin and sin not in (bare, '名専字', stem) and sin not in words:
            add('B5', 'stand_in is neither the character, a word, nor 名専字', f'{stem} (stand_in {sin})')

# ---------------------------------------------------------------- Tier C
def last_modified():
    """path -> date of the newest commit touching it (untracked/uncommitted -> today)."""
    out = sh('git', 'log', '--name-only', '--format=@%cs', '--', 'characters')
    mod = {}; cur = None
    for line in out.split('\n'):
        if line.startswith('@'): cur = line[1:]
        elif line.strip() and cur and line not in mod: mod[line] = cur
    dirty = sh('git', 'status', '--porcelain', '-z', '--', 'characters').split('\0')
    for e in dirty:
        if len(e) > 3: mod[e[3:]] = TODAY.isoformat()
    return mod

if not IDS_ONLY:
    mod = last_modified()
    word_chars = collections.defaultdict(list)    # char stem -> [(word, 注音)]
    for f in listing('words'):
        t = read(f)
        if not t: continue
        fm, _ = split_fm(t)
        if fm is None: continue
        zy = fm_get(fm, '注音') or ''
        m = re.search(r'^characters:\s*\n((?:\s+-.*\n?)+)', fm + '\n', re.M)
        if not m: continue
        w = os.path.basename(f)[:-3]
        for it in re.findall(r'^\s+-\s*(.*)$', m.group(1), re.M):
            word_chars[it.strip().strip('"\'')].append((w, zy))
    cy_chars = collections.defaultdict(list)
    for f in listing('chengyu'):
        t = read(f)
        if not t: continue
        fm, _ = split_fm(t)
        if fm is None: continue
        zy = fm_get(fm, '注音') or ''
        m = re.search(r'^characters:\s*\n((?:\s+-.*\n?)+)', fm + '\n', re.M)
        if not m: continue
        w = os.path.basename(f)[:-3]
        if w.endswith('Chengyu'): continue
        for it in re.findall(r'^\s+-\s*(.*)$', m.group(1), re.M):
            cy_chars[it.strip().strip('"\'')].append((w, zy))
    ccrank = {}
    for n in ('0000', '1000', '2000', '3000'):
        t = read(f'lookup/CC/CC {n}.md')
        if not t: continue
        for r, ch in re.findall(r'^(\d+)\. (\S)\s*$', t, re.M):
            ccrank[ch] = int(r)

    def section(body, name):
        m = re.search(rf'^## {re.escape(name)}\s*$(.*?)(?=^## |\Z)', body, re.M | re.S)
        return m.group(1) if m else None

    def ruby_entries(sec):
        """(target, reading) for every <ruby>[[target]] / [[target|label]] / [label](path/target.md)<rt>reading</rt></ruby>."""
        out = []
        for m in re.finditer(r'<ruby>(.*?)<rt>([^<]*)</rt></ruby>', sec):
            inner, rt = m.group(1), m.group(2)
            w = re.search(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', inner)
            if w:
                out.append((urllib.parse.unquote(w.group(1)).strip(), rt)); continue
            w = re.search(r'\]\(([^)]*)\)', inner)
            if w:
                tgt = urllib.parse.unquote(w.group(1))
                tgt = tgt.rsplit('/', 1)[-1]
                tgt = tgt[:-3] if tgt.endswith('.md') else tgt
                out.append((tgt, rt))
        return out

    def plain_entries(sec):
        """bullets that link a word but carry no <ruby> reading."""
        out = set()
        for line in sec.split('\n'):
            if not line.startswith('-') or '<ruby>' in line: continue
            for w in re.finditer(r'\[\[([^\]|]+)(?:\|[^\]]*)?\]\]', line):
                out.add(urllib.parse.unquote(w.group(1)).strip())
            for w in re.finditer(r'\]\(([^)]*words/[^)]*)\)', line):
                t = urllib.parse.unquote(w.group(1)).rsplit('/', 1)[-1]
                out.add(t[:-3] if t.endswith('.md') else t)
        return out

    checked = 0
    for stem, c in chars.items():
        stamp = fm_get(c['fm'], 'date-last-perfect')
        lm = mod.get(c['file'])
        needs = DEEP or not stamp or (lm and stamp and lm > stamp)
        if not stamp:
            add('C0', 'no date-last-perfect', stem)
        if not needs: continue
        checked += 1
        body = c['body']; get = lambda k: fm_get(c['fm'], k)
        notes = section(body, 'Notes')
        if notes is None:
            add('C1', 'no `## Notes` section', stem)
        else:
            bl = [l for l in notes.split('\n') if l.startswith('- ')]
            sk, st, zy = get('skip_number'), get('stroke_count'), get('注音')
            skb = next((l for l in bl if re.search(r'SKIP-\d', l)), None)
            mcb = next((l for l in bl if re.search(r'most used character in Classical Chinese|Not present|Genuinely absent|Ancient \[\[', l)), None)
            if skb is None:
                add('C1', 'no SKIP/Stroke bullet', stem)
            else:
                if sk and f'SKIP-{sk}' not in skb:
                    add('C1', 'SKIP bullet does not link the SKIP leaf of its skip_number', stem)
                if st and str(st).isdigit() and f'Stroke%20{int(st):02d}' not in skb and f'Stroke {int(st):02d}' not in skb:
                    add('C1', 'Stroke link is not its zero-padded Stroke page (e.g. Stroke%2004)', stem)
            if mcb is None:
                add('C1', 'no Classical Chinese / ancient-sound bullet', stem)
            else:
                if '聲 ' not in mcb or '韻 ' not in mcb:
                    add('C1', 'ancient-sound bullet lacks the CC initial/final links', stem)
                if zy and f'syllables/{zy}.md' not in mcb:
                    add('C1', 'ancient-sound bullet does not link its syllable', stem)
            for b in (skb, mcb):
                if b and re.search(r'\]\((lookup|syllables|words|characters)/', b):
                    add('C1', 'link in a Notes bullet is missing the `../` prefix', stem); break
        mcv = get('mc_id')
        bare = stem[:-7] if stem.endswith(' (char)') else stem
        if mcv and str(mcv).isdigit() and int(mcv) and bare in ccrank and ccrank[bare] != int(mcv):
            add('C3', f'mc_id {mcv} but lookup/CC lists it at {ccrank[bare]}', stem)
        w_sec = section(body, 'Words')
        listed = ruby_entries(w_sec) if w_sec else []
        expect = {w: zy for w, zy in word_chars.get(stem, [])}
        got = {t: z for t, z in listed}
        plain = plain_entries(w_sec) if w_sec else set()
        for w, zy in expect.items():
            if w not in got and w in plain:
                add('C2', 'word is listed in ## Words without a <ruby> reading', f'{stem} -> {w}')
            elif w not in got:
                add('C2', 'word using this character is missing from ## Words', f'{stem} -> {w}')
            elif zy and got[w] != zy.strip('"'):
                add('C2', 'ruby reading in ## Words differs from the word\'s 注音', f'{stem} -> {w} ({got[w]} vs {zy})')
        for t in got:
            if t not in words and not os.path.exists(f'words/{t}.md'):
                add('C2', '## Words links a word that has no file', f'{stem} -> {t}')
        y_sec = section(body, 'Chengyu')
        ylisted = ruby_entries(y_sec) if y_sec else []
        yexpect = {w: zy for w, zy in cy_chars.get(stem, [])}
        ygot = {t: z for t, z in ylisted}
        for w, zy in yexpect.items():
            if w not in ygot:
                add('C2', 'chengyu using this character is missing from ## Chengyu', f'{stem} -> {w}')
            elif zy and ygot[w] != zy.strip('"'):
                add('C2', 'ruby reading in ## Chengyu differs from the chengyu\'s 注音', f'{stem} -> {w}')
    print(f'{len(chars)} pages; Tier C run on {checked} ({"all, --deep" if DEEP else "changed since their stamp, or unstamped"})')
else:
    print(f'{len(chars)} pages; Tier A only')

for k, v in todo.items():
    print(f'(to do, not a failure) {k}: {v}')
print('next free danayo_id per block: ' + ', '.join(f'{g} {v}' for g, v in sorted(nextfree.items(), key=lambda x: BASE[x[0]])))

# ---------------------------------------------------------------- report
if not problems:
    print('PASS: all checks clean.')
    if STAMP and not IDS_ONLY and os.path.exists('lookup/Characters.md'):
        p = 'lookup/Characters.md'; t = open(p).read()
        t2 = re.sub(r'^date-last-perfect:.*$', f'date-last-perfect: {TODAY.isoformat()}', t, count=1, flags=re.M)
        open(p, 'w').write(t2)
        print(f'Stamped {p} date-last-perfect: {TODAY.isoformat()}')
    sys.exit(0)

byc = collections.Counter()
for (code, msg), who in problems.items():
    byc[code] += len(who)
print()
cur = None
for (code, msg), who in sorted(problems.items(), key=lambda kv: (kv[0][0], -len(kv[1]))):
    print(f'[{code}] {msg}: {len(who)}')
    for w in who[:MAXN]:
        print(f'     {w}')
    if len(who) > MAXN:
        print(f'     ... and {len(who) - MAXN} more')
print()
print('FAIL: ' + ', '.join(f'{c} {n}' for c, n in sorted(byc.items())) + ('; lookup/Characters.md not stamped.' if STAMP and not IDS_ONLY else ''))
sys.exit(1)
