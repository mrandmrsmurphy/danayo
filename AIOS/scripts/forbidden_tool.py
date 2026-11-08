#!/usr/bin/env python3
"""Work through grammar/文法 - 98違法字.md and list its characters under `### Forbidden` on the
Stroke, Radical and SKIP pages (see the Aliases project for the sibling `alias_tool.py`).

  forbidden_tool.py classes          # inventory of Class labels per country section, against ALLOWED
  forbidden_tool.py check [SECTION]  # which entries are incomplete (stroke, class, SKIP, radical, comment)
  forbidden_tool.py line 字          # print the line that would be written
  forbidden_tool.py apply 字 [字..]  # write/replace the line on the character's Stroke, Radical and SKIP pages
  forbidden_tool.py apply --section Korean   # every complete entry in a section

An entry needs all five fields: 筆画 (strokes), Class, SKIP, 部首 (radical), Notes (comment). `apply` refuses an
entry with a blank field, a `?`, or a leftover "check"/"✅" mark, and refuses a Class not in ALLOWED.
Line format on the lookup pages (no replacement is implied; the comment may suggest words to use instead):
    - 丷 - 口訣: Korean 구결 for '하다'
Run from the vault root.
"""
import re,os,sys,unicodedata
SRC="grammar/文法 - 98違法字.md"
# Provisional until agreed with 武明帥 (2026-11-07): the limited set of classifications.
ALLOWED=["官话","方言","中国制造","国字","국자","口訣","異体字","幽霊文字","混乱"]
RADNUM={unicodedata.normalize("NFKC",chr(0x2F00+i)):i+1 for i in range(214)}
def parse():
    t=open(SRC,encoding="utf-8").read(); out={}; sec=None
    for blk in re.split(r"^(?=#{2,4} )",t,flags=re.M):
        m=re.match(r"## (\w+)\n",blk)
        if m and m.group(1) in ("Chinese","Japanese","Korean"): sec=m.group(1); continue
        m=re.match(r"#### (.+)\n",blk)
        if not m or not sec: continue
        f={}
        for k,v in re.findall(r"^- ([^:\n]+?)\s*:[ \t]*(.*)$",blk,re.M): f[k.strip()]=v.strip()
        out[m.group(1).strip()]={"section":sec,"strokes":f.get("筆画",""),"class":f.get("Class",f.get("class","")),
            "skip":f.get("SKIP",""),"radical":f.get("部首",""),"notes":f.get("Notes",""),"alias":f.get("別名","")}
    return out
def problems(e):
    p=[]
    if not re.fullmatch(r"\d+",e["strokes"]): p.append("strokes")
    if not e["class"]: p.append("class")
    elif e["class"] not in ALLOWED: p.append(f"class '{e['class']}' not in ALLOWED")
    if not re.fullmatch(r"\d+-\d+-\d+",e["skip"]): p.append("skip")
    if not e["radical"] or "check" in e["radical"] or "?" in e["radical"]: p.append("radical")
    if not e["notes"]: p.append("notes")
    return p
def radnum(r):
    m=re.search(r"#(\d+)",r)
    if m: return int(m.group(1))
    c=r.strip()[:1]; return RADNUM.get(c)
def line(ch,e): return f"- {ch} - {e['class']}: {e['notes']}"
def pages(e):
    a,b,c=e["skip"].split("-"); rn=radnum(e["radical"])
    return [f"lookup/Stroke/Stroke {int(e['strokes']):02d}.md",f"lookup/Radicals/Radical {rn:03d}.md",f"lookup/SKIP/SKIP-{a}/SKIP-{a}-{b}-{c}.md"]
def put(path,ch,ln):
    t=open(path,encoding="utf-8").read(); L=t.split("\n")
    if "### Forbidden" in t:
        i=L.index("### Forbidden"); j=i+1
        while j<len(L) and not L[j].startswith("#"): j+=1
        body=L[i+1:j]
        for k,x in enumerate(body):
            if re.match(rf"^- {re.escape(ch)}(\s|$)",x): body[k]=ln; break
        else:
            while body and not body[-1].strip(): body.pop()
            body.append(ln)
            if j<len(L) and L[j].startswith("#") and body[-1]!="": pass
        L[i+1:j]=body+([""] if j<len(L) and L[j].startswith("## ") and body else [])
        # keep one blank before a following ## heading
    else:
        if "### Aliases" in t:
            i=L.index("### Aliases"); j=i+1
            while j<len(L) and not L[j].startswith("#"): j+=1
        else:
            j=next((k for k,x in enumerate(L) if x.startswith("## Data")),len(L))
        L[j:j]=["### Forbidden",ln,""]
    out=re.sub(r"(### Forbidden\n(?:- .*\n)+)\n{2,}",r"\1\n","\n".join(L))
    open(path,"w",encoding="utf-8").write(out)
def main():
    a=sys.argv[1:]; cmd=a[0] if a else ""; E=parse()
    if cmd=="classes":
        import collections
        for s in ("Chinese","Japanese","Korean"):
            c=collections.Counter(e["class"] or "(blank)" for e in E.values() if e["section"]==s); print(s,dict(c))
        print("ALLOWED:",ALLOWED); return
    if cmd=="check":
        sec=a[1] if len(a)>1 else None; n=ok=0
        for ch,e in E.items():
            if sec and e["section"]!=sec: continue
            n+=1; p=problems(e)
            if p: print(ch,e["section"],"; ".join(p))
            else: ok+=1
        print(f"{ok}/{n} complete"); return
    if cmd=="line": e=E[a[1]]; print(line(a[1],e)); [print(" ->",x) for x in pages(e)]; return
    if cmd=="apply":
        chars=a[1:]
        if chars[:1]==["--section"]: chars=[c for c,e in E.items() if e["section"]==chars[1] and not problems(e)]
        for ch in chars:
            e=E[ch]; p=problems(e)
            if p: print("SKIP",ch,"-",p); continue
            for pg in pages(e):
                if not os.path.exists(pg): print("MISSING PAGE",pg,"for",ch); continue
                put(pg,ch,line(ch,e)); print("wrote",ch,"->",pg)
        return
    print(__doc__)
main()
