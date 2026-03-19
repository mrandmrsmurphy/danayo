Checked for redirect.

### 다 
[爹](characters/爹.md) [[𥥸]] [[𣘻]] [[茤]] 

### 단 
[[緞]] [鍛](characters/鍛.md) [亶](characters/亶.md) [彖](characters/彖.md) [[湍]] [簞](characters/簞.md) [蛋](characters/蛋.md) [[袒]] [[鄲]] [[煓]] [[㫜]]

### 달  
[[撻]] [[澾]] [[獺]] [[疸]]

### 담  
[譚](characters/譚.md) [膽](characters/胆.md) [澹](characters/淡.md) [覃](characters/湛.md) [啖](characters/啖.md) [[坍]] [[憺]] [曇 (char)](characters/曇%20(char).md) [湛](characters/湛.md) [痰 (char)](characters/痰%20(char).md) [[聃]] [[蕁]] [[錟]] [潭](characters/湛.md) [[倓]]

### 답  
[沓](characters/沓.md) [[遝]]

### 당 
[[塘]] [[鐺]] [撞](characters/撞.md) [[幢]] [[戇]] [[棠]] [螳](characters/螳.md)

### 대  
[[垈]] [玳](characters/玳.md) [袋 (char)](characters/袋%20(char).md) [戴 (char)](characters/戴%20(char).md) [擡](characters/擡.md) [[旲]] [[岱]] [黛](characters/黛.md) 

### 도  
[堵](characters/堵.md) [[棹]] [濤](characters/涛.md) [[燾]] [禱](characters/祷.md) [鍍](characters/鍍.md) [蹈](characters/踏.md) [屠](characters/屠.md) [悼 (char)](characters/悼%20(char).md) [[掉]] [[搗]] [櫂](characters/櫂.md) [[淘]] [[滔]] [[睹]] [萄](characters/萄.md) [[覩]] [賭](characters/賭.md) [[韜]] [[馟]] 

### 독  
[瀆](characters/涜.md) [[牘]] [[犢]] [禿 (char)](characters/禿%20(char).md) [[纛]]

### 돈 
[墩](characters/敦.md) [惇](characters/惇.md) [[暾]] [[燉]] [頓](characters/頓.md) [[旽]] [沌](characters/沌.md) [[焞]]

### 돌  
乭

### 동  
[棟](characters/棟.md) [董](characters/董.md) [[潼]] [[垌]] [瞳](characters/瞳.md) [[蝀]] [憧](characters/憧.md) 疼 [胴](characters/胴.md) [桐](characters/桐.md) [[朣]] [[曈]] [彤](characters/彤.md) [[烔]] [[橦]] 

### 두  
[杜](characters/杜.md) [[枓]] [兜](characters/兜%20(char).md) [痘](characters/痘.md) [[竇]] [[荳]] [讀](characters/読.md) [逗](characters/逗.md) [[阧]]

### 둔  
[[遁]] [[臀]] [[芚]] [[遯]]

### 둘  
乧!

### 등  
[藤](characters/藤.md) [謄](characters/謄.md) [鄧](characters/鄧.md) [[嶝]] [橙](characters/橙.md)

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
