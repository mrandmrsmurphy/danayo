#!/usr/bin/env python3
"""lint Chengyu: report-only audit of chengyu leaf pages against checklist_chengyu.md.

Run from the vault root:  python3 AIOS/scripts/lint_chengyu.py [--all]
Prints, oldest `date-last-perfect` first, every leaf with at least one defect, grouped by page.
Never edits. Order of the `characters:` list is NOT checked (user decision 2026-10-04).
Not automated (needs a source lookup, done by the page perfecter): citation verification.
The three grouping pages are checked by lint_chengyu_groups.py (run at the end).
"""
import os, re, subprocess, sys, collections
try:
    import yaml
except ImportError:
    yaml = None

CATLINK = {'単亜語': "Dan'a'yo%20Chengyu.md", 'Bible': 'Biblical%20Chengyu.md'}
MISC = 'Misc.%20Chengyu.md'
SECTIONS = ['Literal Meaning', 'Extended Meaning', 'Source and Origin', 'Pronunciations',
            'Cultural Notes', 'Example Sentences', 'Sentiment']
SCALARS = ['mandarin', 'cantonese', 'japanese', 'korean', 'vietnamese', '諺文', '羅馬字', '注音', 'origin']

def leaves():
    out = subprocess.check_output(['git', 'ls-files', '-z', 'chengyu/'], text=True).split('\0')
    return [f for f in out if f.endswith('.md') and not f.endswith('Chengyu.md')]

def charfile(c):
    for cand in (f'characters/{c}.md', f'characters/{c} (char).md'):
        if os.path.exists(cand):
            return cand

def scalar(d, k):
    v = d.get(k)
    return v if isinstance(v, str) else ''

def check(f):
    probs = []
    name = f[len('chengyu/'):-3]
    text = open(f).read()
    m = re.match(r'---\n(.*?)\n---\n(.*)', text, re.S)
    if not m:
        return None, ['no frontmatter']
    raw, body = m.groups()
    keys = [l.split(':')[0] for l in raw.split('\n') if re.match(r'^[^\s#-][^:]*:', l)]
    for k, v in collections.Counter(keys).items():
        if v > 1:
            probs.append(f'duplicate frontmatter key: {k}')
    try:
        d = yaml.safe_load(raw) if yaml else {}
    except Exception as e:
        return None, [f'invalid YAML: {str(e)[:60]}']
    date = str(d.get('date-last-perfect') or '')
    if not date:
        probs.append('no date-last-perfect')
    for k in SCALARS:
        v = d.get(k)
        if v is None or v == '':
            probs.append(f'blank {k}')
        elif not isinstance(v, str):
            probs.append(f'{k} is not a scalar')
    al = d.get('aliases')
    if al is None:
        probs.append('aliases blank/missing (use [] if none)')
    eng_raw = d.get('english')
    eng_list = eng_raw if isinstance(eng_raw, list) else ([eng_raw] if isinstance(eng_raw, str) else [])
    eng_ok = {e for e in eng_list} | {'; '.join(eng_list)}
    eng = eng_list[0] if eng_list else ''
    origin = scalar(d, 'origin')
    # body opening and category link
    if not body.lstrip().startswith('```meta-bind-embed'):
        probs.append('meta-bind-embed not first')
    want = CATLINK.get(origin, MISC)
    if f'](chengyu/{want})' not in body:
        probs.append(f'category link missing/wrong (want {want})')
    for s in SECTIONS:
        if not re.search(r'^##\s+' + re.escape(s), body, re.M):
            probs.append(f'missing ## {s}')
    if re.search(r'^###\s', body, re.M) and not re.search(r'^## Literal', body, re.M):
        probs.append('### used for main sections')
    # readings vs constituent characters (character order from the name itself; dots ignored)
    zy = scalar(d, '注音').replace('·', '')
    segs, unresolved = [], []
    for c in name:
        cf = charfile(c)
        if not cf:
            unresolved.append(c)
            continue
        ct = open(cf).read()
        z = re.search(r'^注音:\s*"?([^"\n]*)', ct, re.M)
        segs.append(z.group(1).strip().replace('·', '') if z else '')
        # back-link check on the character's own ## Chengyu section
        sec = re.search(r'^## Chengyu\s*\n(.*?)(?=^## |\Z)', ct, re.S | re.M)
        line = None
        if sec:
            for l in sec.group(1).split('\n'):
                if f'[[{name}]]' in l or f'{name}.md' in l:
                    line = l
                    break
        if line is None:
            probs.append(f'back-link missing on {c}')
        else:
            rt = re.search(r'<rt>([^<]*)</rt>', line)
            if not rt:
                probs.append(f'back-link on {c} has no ruby')
            elif rt.group(1).replace('·', '') != zy:
                probs.append(f'back-link on {c} has stale 注音')
            if eng and not any(f'"{e}"' in line for e in eng_ok):
                probs.append(f'back-link on {c} gloss differs from english')
            if '](/' in line:
                probs.append(f'back-link on {c} uses an absolute path')
    if not unresolved and ''.join(segs) != zy and zy:
        probs.append('注音 differs from constituent characters\' 注音 concatenation')
    ko = scalar(d, 'korean')
    if re.search(r'[가-힣]', ko) and len(ko.replace(' ', '')) != len(name):
        probs.append(f'korean length {len(ko)} vs {len(name)} characters')
    return date or '0000', probs

def main():
    rows = []
    for f in leaves():
        date, probs = check(f)
        rows.append((date or '0000', f, probs))
    rows.sort()
    bad = [(d, f, p) for d, f, p in rows if p]
    for d, f, p in bad:
        print(f'{d}  {f}')
        for x in p:
            print('    -', x)
    print(f'\n{len(bad)} of {len(rows)} leaf pages have defects.')
    cat = collections.Counter(re.sub(r' on .*| \(want.*|: .*', '', x) for _, _, p in bad for x in p)
    for k, v in cat.most_common():
        print(f'  {v:4}  {k}')
    r = subprocess.run([sys.executable, 'AIOS/scripts/lint_chengyu_groups.py'], capture_output=True, text=True)
    print('\ngrouping pages:', 'OK' if r.returncode == 0 else 'DRIFT\n' + r.stdout)
    sys.exit(1 if bad or r.returncode else 0)

if __name__ == '__main__':
    main()
