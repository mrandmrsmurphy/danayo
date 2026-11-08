#!/usr/bin/env python3
"""Migrate a grouped-style Radical page to the in-group standard (checklist_radicals.md, "Non-numbered entries within stroke groups").

  radical_migrate.py 85        # lookup/Radicals/Radical 085.md

Moves the bottom `### Aliases` and `### Forbidden` sections into the `### +N Strokes` groups (N = the glyph's own stroke count minus
the radical's Kangxi strokes, via radical_fmt.radical_put) and shortens each forbidden line to `- ¡X! - 違法字`. Stroke counts come from the
Stroke pages (aliases) and the 筆画 field of 文法 - 98違法字 (forbidden). A glyph with no known count is reported and left in its old section.
Run from the vault root.
"""
import re,sys,glob,os
sys.path.insert(0,os.path.dirname(__file__))
from radical_fmt import radical_put
n=int(sys.argv[1]); P=f"lookup/Radicals/Radical {n:03d}.md"
L=open(P,encoding="utf-8").read().split("\n")
def grab(name):
    if f"### {name}" not in L: return None,None,[]
    i=L.index(f"### {name}"); j=i+1
    while j<len(L) and not L[j].startswith("#"): j+=1
    return i,j,[l for l in L[i+1:j] if l.strip()]
ia,ja,al=grab("Aliases"); ifb,jfb,fb=grab("Forbidden")
sp={}
for f in glob.glob("lookup/Stroke/Stroke *.md"):
    m=re.search(r"Stroke (\d+)\.md",f)
    if not m: continue
    for l in open(f,encoding="utf-8"):
        k=re.match(r"- ¡?(\S+?)!? (?:-->|-) ",l)
        if k: sp.setdefault(k.group(1),int(m.group(1)))
master=open("grammar/文法 - 98違法字.md",encoding="utf-8").read()
ms={m.group(1):int(m.group(2)) for m in re.finditer(r"^#### (\S+)\n- 筆画: (\d+)",master,re.M)}
keep_al=[];keep_fb=[];todo=[]
for l in al:
    g=re.match(r"- (\S+) -->",l)
    s=sp.get(g.group(1)) if g else None
    (todo.append((l,s,"Aliases")) if s else keep_al.append(l))
for l in fb:
    g=re.match(r"- ¡?(\S+?)!?(?: - .*)?$",l).group(1)
    s=ms.get(g) or sp.get(g)
    (todo.append((f"- ¡{g}! - 違法字",s,"Forbidden")) if s else keep_fb.append(l))
# drop the old sections, then re-add anything left behind
for (i,j) in sorted([x for x in [(ia,ja),(ifb,jfb)] if x[0] is not None],reverse=True): del L[i:j]
cut=next((i for i,l in enumerate(L) if re.match(r"## (?!Strokes)",l)),len(L))
extra=[]
if keep_al: extra+=["### Aliases"]+keep_al+[""]
if keep_fb: extra+=["### Forbidden"]+keep_fb+[""]
L[cut:cut]=extra
open(P,"w",encoding="utf-8").write("\n".join(L))
for l,s,sec in todo: radical_put(P,l,s,n,sec)
print("moved",len(todo),"left behind",keep_al+keep_fb)
