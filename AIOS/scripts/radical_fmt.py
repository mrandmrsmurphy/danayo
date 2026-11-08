"""Shared helper: file an alias or forbidden line inside the right `### +N Strokes` group of a grouped-style Radical page.

Rule (checklist_radicals.md, "Non-numbered entries within stroke groups"): N = the glyph's own stroke count
(Japanese way, as on its Stroke page) minus the radical's Kangxi stroke count; the line goes after that group's
numbered entries, unnumbered. Prosaic-style pages (no `### +N` groups) keep a bottom `### Aliases` / `### Forbidden`.
"""
import re
# Kangxi radical number ranges -> stroke count of the radical itself
_R=[(1,6,1),(7,29,2),(30,60,3),(61,94,4),(95,117,5),(118,146,6),(147,166,7),(167,175,8),(176,186,9),(187,194,10),(195,200,11),(201,204,12),(205,208,13),(209,210,14),(211,211,15),(212,213,16),(214,214,17)]
def radical_strokes(n):
    for a,b,s in _R:
        if a<=n<=b: return s
    raise ValueError(n)
def heading(n): return f"### +{n} Stroke" + ("" if n==1 else "s")
def _hn(l):
    m=re.match(r"### ([+-]\d+) Strokes?$",l); return int(m.group(1)) if m else None
def radical_put(path,line,total_strokes,radical_number,section="Aliases"):
    """Insert `line` into the +N group (N = total_strokes - Kangxi strokes). Prosaic pages: bottom ### section. Replaces an existing line for the same glyph."""
    t=open(path,encoding="utf-8").read(); L=t.split("\n")
    glyph=re.match(r"- ¡?([^\s!]+)",line).group(1)
    L=[l for l in L if not re.match(rf"- ¡?{re.escape(glyph)}(!|\s|$)",l)] if section=="Forbidden" else L
    if line in L: return
    if not any(_hn(l) is not None for l in L):          # prosaic style
        sec=f"### {section}"
        if sec in L:
            i=L.index(sec); j=i+1
            while j<len(L) and not L[j].startswith("#"): j+=1
            while j>i+1 and not L[j-1].strip(): j-=1
            L[j:j]=[line]
        else:
            k=next((x for x,l in enumerate(L) if re.match(r"## Data ?check",l)),len(L)); L[k:k]=[sec,line,""]
        open(path,"w",encoding="utf-8").write("\n".join(L)); return
    n=int(total_strokes)-radical_strokes(radical_number)
    heads=[(i,_hn(l)) for i,l in enumerate(L) if _hn(l) is not None]
    cut=next((i for i,l in enumerate(L) if re.match(r"## (?!Strokes)",l) or re.match(r"### (?!\+|-)",l)),len(L))   # end of the Strokes block
    for i,h in heads:
        if h==n:
            j=i+1
            while j<cut and not L[j].startswith("#"): j+=1
            while j>i+1 and not L[j-1].strip(): j-=1
            L[j:j]=[line]; break
    else:
        pos=next((i for i,h in heads if h>n),None)
        if pos is None:
            pos=cut
            while pos>0 and not L[pos-1].strip(): pos-=1
            L[pos:pos]=["",heading(n),line]
        else: L[pos:pos]=[heading(n),line,""]
    open(path,"w",encoding="utf-8").write("\n".join(L))
