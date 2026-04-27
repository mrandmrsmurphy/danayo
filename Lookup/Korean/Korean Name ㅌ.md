---
tags: [lookup]
---
These have all been checked for redirects.

### 타 
 [[咤]] [唾](characters/唾.md) [惰](characters/惰.md) [拖](characters/拖.md) [朶](characters/朶.md) [舵 (char)](characters/舵%20(char).md) [陀](characters/陀.md) [馱](characters/駄%20(char).md) [駝](characters/駝.md) [橢](characters/楕.md)

### 탁  
度 (done) [[倬]] [[琸]] [[晫]] [託](characters/託.md) [擢](characters/擢.md) [鐸](characters/鈬%20(char).md) [拓](characters/拓.md) [啄 (char)](characters/啄%20(char).md) [[坼]] [[柝]] [琢](characters/琢.md) [[踔]] [橐](characters/橐.md)

### 탄  
[呑](characters/呑.md) [坦](characters/坦.md) [灘 (char)](characters/灘%20(char).md) [嘆 (char)](characters/嘆%20(char).md) [憚](characters/惮.md) [綻](characters/綻.md)

### 탐  
 [耽 (char)](characters/耽%20(char).md) [[眈]]

### 탑  
[[榻]]

### 탕  
[宕](characters/宕.md) [[帑]] [糖 (char)](characters/糖%20(char).md) [蕩](characters/蕩.md)

### 태  
[汰](characters/汰.md) [[兌]]! [台](characters/台%20(char).md) [胎](characters/胎.md) [[邰]] [[笞]] [苔 (char)](characters/苔%20(char).md) [跆](characters/跆.md) [颱](characters/台%20(char).md) [[鈦]] [[珆]] [鮐](characters/鮐.md)

### 택  
[[垞]] 

### 탱  
[撑](characters/撐.md)

### 터  
[攄](characters/攄.md)

### 토  
[兔](characters/兎%20(char).md)

### 통  
[桶 (char)](characters/桶%20(char).md) [慟](characters/動%20(char).md) 洞 (done) [筒 (char)](characters/筒%20(char).md) 

### 퇴  
[堆](characters/堆.md) [槌 (char)](characters/槌%20(char).md) [腿](characters/腿.md) [[褪]] [[頹]] 

### 투  
[偸](characters/偷.md) [套 (char)](characters/套%20(char).md) [妬](characters/妬.md) 

### 특  
[[慝]] 

### 틈  
[闖](characters/闖.md)
 
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

