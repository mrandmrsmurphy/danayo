These have all been checked for redirects.

### 나  
[[../../characters/奈]] [[柰]] [[娜]] [拏](characters/拿.md) [[儺]] [喇](characters/喇.md) [[懦]] [拿](characters/拿.md) [[𣃽]] [[䏧]] [[挐]] [挪](../../characters/梛.md) [[𡖔]] [梛](characters/梛.md) [[糯]] 

### 난  
[煖](characters/暖%20(char).md)

### 날  
[捺](characters/捺%20(char).md) [捏](characters/捏.md)

### 남  
[楠](characters/楠.md) 湳 [[枏]]

### 납  
[衲](characters/衲.md)

### 낭  
[囊](characters/嚢.md)

### 내  
[[柰]]

### 년  
[[撚]]

### 념  
[[恬]] [[拈]] [捻](characters/捻%20(char).md)

### 녕  
[[獰]] [佞](characters/佞.md)

### 노  
[弩](characters/努.md) [瑙](characters/𡿺.md) [[駑]]

### 농  
[膿](characters/膿%20(char).md) [濃](characters/濃.md)

### 뇨  
[尿](characters/尿%20(char).md) [鬧](characters/閙.md) [[撓]]

### 눈  
[嫩](characters/嫩%20(char).md)

### 눌  
[訥](characters/訥%20(char).md)

### 뉴  
[[紐]] [[鈕]] [[杻]]

### 니  
[尼](characters/尼.md) [[柅]] [[濔]] [[膩]] [[馜]]

### 닉  
[匿](characters/匿.md) [溺](characters/溺%20(char).md)

## Datacheck
```dataviewjs
function norm(v) {
  if (v == null) return "";
  if (Array.isArray(v)) return v.join(", ");
  return String(v);
}

let seen = new Set();
let links = dv.current().file.outlinks;

let pages = links
  .map(l => dv.page(l))
  .filter(p => p && p.file.path.startsWith("characters/"))
  .filter(p => {
    if (seen.has(p.file.path)) return false;
    seen.add(p.file.path);
    return true;
  })
  .sort((a, b) => norm(a.korean).localeCompare(norm(b.korean), "ko"));

dv.table(
  ["Character", "Korean", "Korean Native","Level"],
  pages.map(p => [
    p.file.link,
    norm(p.korean),
    norm(p.korean_native),
    norm(p.hanmun_edu_level)
  ])
);
```