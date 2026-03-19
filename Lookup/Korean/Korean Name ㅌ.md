
### 타 
  [[咤]] [[唾]] [[惰]] [[拖]] [[朶]] [[舵]] [[陀]] [[馱]] [[駝]] [[橢]]

### 탁  
[[度]] [[倬]] [[琸]] [[晫]] [[託]] [[擢]] [[鐸]] [[拓]] [[啄]] [[坼]] [[柝]] [[琢]] [[踔]] [[橐]]

### 탄  
[[呑]] [[坦]] [[灘]] [[嘆]] [憚](characters/惮.md) [[綻]]

### 탐  
 [[耽]] [[眈]] 

### 탑  
 [[榻]] 

### 탕  
 [[宕]] [[帑]] [[糖]] [[蕩]]

### 태  
[[汰]] [[兌]]! [[台]] [[胎]] [[邰]] [[笞]] [[苔]] [[跆]] [[颱]] [[鈦]] [[珆]] [[鮐]]

### 택  
 [[垞]] 

### 탱  
 [[撑]]

### 터  
 [[攄]]

### 토  
 [[兔]]

### 통  
[[桶]] [[慟]] [[洞]] [[筒]] 

### 퇴  
[[堆]] [[槌]] [[腿]] [[褪]] [[頹]] 

### 투  
 [[偸]] [[套]] [[妬]] 

### 특  
 [[慝]] 

### 틈  
 [[闖]]
 
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

