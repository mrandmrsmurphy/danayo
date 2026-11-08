#!/usr/bin/env python3
"""Build the `## Aliases` section of a character page (see AIOS/checklists/checklist_characters.md).

  alias_tool.py evidence 字         # print EDRDG, Unihan, CC-rank and Wiktionary evidence for each alias
  alias_tool.py apply 字 spec.json  # write the section and the Stroke/SKIP/Radical redirects

spec.json maps each alias to {"text": "...", "skip": "1-2-3" (optional), "strokes": 9 (optional), "guess": true}.
`skip`/`strokes` override EDRDG/Unihan; set "guess": true when the SKIP number is computed, which also appends
a row to AIOS/projects/project_alias_skip_guesses.md. Run from the vault root with --cache DIR (a directory
outside the vault) to keep the Unihan download and Wiktionary cache, e.g. --cache $SCRATCH/alias_cache.
"""
import re,os,sys,json,glob,time,unicodedata,urllib.request,urllib.parse,zipfile
args=sys.argv[1:]; cache="/tmp/alias_cache"
if "--cache" in args: i=args.index("--cache"); cache=args[i+1]; del args[i:i+2]
os.makedirs(cache,exist_ok=True)
UA={"User-Agent":"danayo-vault/1.0"}
def get(url,t=25):
    for _ in range(4):
        try: return urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=t).read()
        except Exception: time.sleep(6)
    return b""
def unihan():
    z=f"{cache}/Unihan.zip"
    if not os.path.exists(z): open(z,"wb").write(get("https://www.unicode.org/Public/UCD/latest/ucd/Unihan.zip",120))
    uni={}
    with zipfile.ZipFile(z) as zf:
        for fn in ("Unihan_IRGSources.txt","Unihan_Variants.txt"):
            for l in zf.read(fn).decode("utf-8").split("\n"):
                if l.startswith("#") or not l.strip(): continue
                u,k,v=l.split("\t",2); uni.setdefault(chr(int(u[2:],16)),{})[k]=v
    return uni
def wikitext(w):
    cf=f"{cache}/wk.json"; C=json.load(open(cf,encoding="utf-8")) if os.path.exists(cf) else {}
    if w not in C:
        d=json.loads(get("https://en.wiktionary.org/w/api.php?action=query&prop=revisions&rvprop=content&rvslots=main&format=json&titles="+urllib.parse.quote(w)) or b"{}")
        try: p=list(d["query"]["pages"].values())[0]; C[w]=p["revisions"][0]["slots"]["main"]["*"]
        except Exception: C[w]=""
        json.dump(C,open(cf,"w",encoding="utf-8"),ensure_ascii=False); time.sleep(2.5)
    return C[w]
def edrdg(a):
    h=get("http://www.edrdg.org/cgi-bin/wwwjdic/wwwjdic?1MMJ"+urllib.parse.quote(a)).decode("utf-8","replace")
    sk=re.search(r"SKIP code</td><td><b>([\d-]+)",h); st=re.search(r"Stroke count</td><td><b>(\d+)",h); rd=re.search(r"Radical[^<]*</td><td>[^<]*<b>([^<]*)",h)
    time.sleep(1.2); return (sk and sk.group(1), st and st.group(1), rd and rd.group(1))
def cpath(c): return f"characters/{c} (char).md" if os.path.exists(f"characters/{c} (char).md") else f"characters/{c}.md"
def fm(t,k):
    m=re.search(rf"^{k}:\s*(.*)$",t,re.M); return m.group(1).strip().strip('"') if m else None
def aliases(t):
    m=re.search(r"^aliases:\n((?:\s*- .*\n?)+)",t,re.M); return [a.strip() for a in re.findall(r"^\s*- (.+)$",m.group(1),re.M)] if m else []
def ccranks():
    r={}
    for p in glob.glob("lookup/CC/CC *.md"):
        for l in open(p,encoding="utf-8"):
            m=re.match(r"^>?\s*(\d+)\.\s*\[?([^\s\]\(]+)",l)
            if m: r[m.group(2)]=int(m.group(1))
    return r
def radchar(n): return unicodedata.normalize("NFKC",chr(0x2F00+n-1))
def ctx(t,w):
    pat=r"variant|simplified|traditional|alternative|archaic|obsolete|ancient|form of|Han compound|Han simp|zh-see|zh-forms|ja-see|phonetic series|derivative|original"
    return [l.strip()[:220] for l in t.split("\n") if w in l and re.search(pat,l,re.I)][:6]
def add_redirect(path,alias,main):
    t=open(path,encoding="utf-8").read(); line=f"- {alias} --> {main}"
    if line in t: return
    if "### Aliases" in t:
        i=t.index("### Aliases"); j=t.find("\n## ",i)
        if j<0: t=t.rstrip("\n")+"\n"+line+"\n"
        else: t=t[:i]+t[i:j].rstrip("\n")+"\n"+line+"\n"+t[j:]
    else:
        blk=f"### Aliases\n{line}\n\n"; k=re.search(r"\n## Data ?check",t)
        t=t[:k.start()+1]+blk+t[k.start()+1:] if k else t.rstrip("\n")+"\n\n"+blk
    open(path,"w",encoding="utf-8").write(t)
def main():
    cmd,ch=args[0],args[1]; p=cpath(ch); t=open(p,encoding="utf-8").read(); als=aliases(t)
    if not als: print("no aliases"); return
    uni=unihan(); cc=ccranks(); mc=fm(t,"mc_id")
    if cmd=="evidence":
        print(f"{ch}: mc_id {mc}, own CC rank {cc.get(ch)}, radical {fm(t,'radical')}, strokes {fm(t,'stroke_count')}")
        tm=wikitext(ch)
        for a in als:
            u=uni.get(a,{}); sk,st,rd=edrdg(a); ta=wikitext(a)
            print(f"== {a}: EDRDG skip {sk} strokes {st} radical {rd} | Unihan strokes {u.get('kTotalStrokes')} rs {u.get('kRSUnicode')} | CC rank {cc.get(a)}")
            print("   variants:",{k:v for k,v in u.items() if 'Variant' in k})
            print(f"   [{a} page mentions {ch}]"); [print("     ",x) for x in ctx(ta,ch)]
            print(f"   [{ch} page mentions {a}]"); [print("     ",x) for x in ctx(tm,a)]
            print("   definitions:",[l[:90] for l in ta.split("\n") if l.startswith("# ")][:2])
        return
    spec=json.load(open(args[2],encoding="utf-8")); radnum={radchar(n):n for n in range(1,215)}; radnum.update({"龜":213,"亀":213})
    mrad=radnum.get(fm(t,"radical")); secs=[]; mainrank=cc.get(ch); guesses=[]
    ranks=[int(mc)] if mc and mc.isdigit() and int(mc)>0 else []
    ranks+=[cc[a] for a in als if cc.get(a)]
    newmc=min(ranks) if ranks else 0
    for a in als:
        s=spec[a]; u=uni.get(a,{}); sk,st,rd=edrdg(a)
        skip=s.get("skip") or sk; strokes=s.get("strokes") or st or u.get("kTotalStrokes")
        rn=int(re.match(r"(\d+)",u["kRSUnicode"]).group(1)) if u.get("kRSUnicode") else (int(rd) if rd and rd.isdigit() else None)  # Unihan first: EDRDG's radical field is often the Nelson number
        assert skip and strokes,(a,"no skip/strokes: give them in the spec")
        txt=s["text"]+f" SKIP {skip}"+(" (computed: EDRDG does not list it)" if s.get("guess") else "")+f"; {strokes} stroke"+("" if str(strokes)=="1" else "s")+"."
        if rn and rn!=mrad: txt+=f" Radical {rn:03d} {radchar(rn)}."
        r=cc.get(a)
        if r:
            if r==newmc and r<(mainrank or 10**9): txt+=f" It ranks {r} in the Classical Chinese lists, the lowest among the page's forms, so it sets the page's `mc_id`."
            else: txt+=f" It ranks {r} in the Classical Chinese lists, a higher number than the page's `mc_id`."
        else: txt+=" It has no rank of its own in the Classical Chinese lists."
        secs.append((a,txt,skip,strokes,rn if rn and rn!=mrad else None))
        if s.get("guess"): guesses.append((a,skip,s["text"]))
    i=t.find("\n## Words"); assert i>0 and "\n## Aliases" not in t
    block="## Aliases\n\n"+"\n\n".join(f"### {a}\n{x}" for a,x,*_ in secs)+"\n"
    t2=t[:i].rstrip("\n")+"\n\n"+block+t[i:]
    if str(newmc)!=mc:
        t2=re.sub(r"^mc_id:.*$",f"mc_id: {newmc}",t2,count=1,flags=re.M)
        who=[a for a in als if cc.get(a)==newmc]
        if who:
            sent=f"{newmc}{'st' if newmc%10==1 and newmc%100!=11 else 'nd' if newmc%10==2 and newmc%100!=12 else 'rd' if newmc%10==3 and newmc%100!=13 else 'th'} most used character in Classical Chinese, the rank of its alias {who[0]}"+(f" ({ch} itself ranks {mainrank})" if mainrank else f" ({ch} itself is not on the lists)")+"."
            t2,n=re.subn(r"^- (?:\d+(?:st|nd|rd|th) most used character in Classical Chinese[^.\n]*(?:\([^)]*\))?[^.\n]*\.|Not (?:present in|among)[^\n]*?(?:ranking|lists|Classical Chinese)[^.\n]*\.)",lambda m:"- "+sent,t2,count=1,flags=re.M)
            if not n: print("WARNING: rank bullet not rewritten; edit it by hand to:",sent)
    open(p,"w",encoding="utf-8").write(t2)
    for a,x,skip,strokes,rn in secs:
        add_redirect(f"lookup/Stroke/Stroke {int(strokes):02d}.md",a,ch)
        sa,sb,sc=skip.split("-"); lp=f"lookup/SKIP/SKIP-{sa}/SKIP-{sa}-{sb}-{sc}.md"
        if not os.path.exists(lp): print("MISSING LEAF",lp,"- create a size-0 redirect leaf and an index entry with ø")
        else: add_redirect(lp,a,ch)
        add_redirect(f"lookup/Radicals/Radical {(rn or mrad):03d}.md",a,ch)
    if guesses:
        gp="AIOS/projects/project_alias_skip_guesses.md"; g=open(gp,encoding="utf-8").read().rstrip("\n")
        for a,skip,why in guesses: g+=f"\n| {ch} | {a} | {skip} | computed from its parts |"
        open(gp,"w",encoding="utf-8").write(g+"\n")
    print("written; mc_id now",newmc)
main()
