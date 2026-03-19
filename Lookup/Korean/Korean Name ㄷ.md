
### 다 
[[爹]] [[𥥸]] [[𣘻]] [[茤]] 

### 단 
[[緞]] [[鍛]] [[亶]] [[彖]] [[湍]] [[簞]] [[蛋]] [[袒]] [[鄲]] [[煓]] [[㫜]]

### 달  
[[撻]] [[澾]] [[獺]] [[疸]]

### 담  
[[譚]] [[膽]] [[澹]] [[覃]] [[啖]] [[坍]] [[憺]] [[曇]] [[湛]] [[痰]] [[聃]] [[蕁]] [[錟]] [[潭]] [[倓]]

### 답  
[[沓]] [[遝]]

### 당 
[[塘]] [[鐺]] [[撞]] [[幢]] [[戇]] [[棠]] [[螳]]

### 대  
[[垈]] [[玳]] [[袋]] [[戴]] [[擡]] [[旲]] [[岱]] [[黛]] 

### 도  
[[堵]] [[棹]] [[濤]] [[燾]] [[禱]] [[鍍]] [[蹈]] [[屠]] [[悼]] [[掉]] [[搗]] [[櫂]] [[淘]] [[滔]] [[睹]] [[萄]] [[覩]] [[賭]] [[韜]] [[馟]] 

### 독  
[[瀆]] [[牘]] [[犢]] [[禿]] [[纛]]

### 돈 
[[墩]] [[惇]] [[暾]] [[燉]] [[頓]] [[旽]] [[沌]] [[焞]]

### 돌  
乭

### 동  
[[棟]] [[董]] [[潼]] [[垌]] [[瞳]] [[蝀]] [[憧]] 疼 [[胴]] [[桐]] [[朣]] [[曈]] [[彤]] [[烔]] [[橦]] 

### 두  
[[杜]] [[枓]] [兜](characters/兜%20(char).md) [[痘]] [[竇]] [[荳]] [[讀]] [[逗]] [[阧]]

### 둔  
[[遁]] [[臀]] [[芚]] [[遯]]

### 둘  
乧!

### 등  
[[藤]] [[謄]] [[鄧]] [[嶝]] [[橙]]

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
