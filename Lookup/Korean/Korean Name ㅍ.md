---
tags: [lookup]
---
Redirected checked for
### 파 
[巴 (char)](characters/巴%20(char).md) [芭](characters/芭.md) [琶](characters/琶.md) [坡](characters/坂.md) [杷](characters/把.md) [婆](characters/婆.md) [擺](characters/擺.md) [爬](characters/爬.md) [跛](characters/坂.md)

### 판 
[阪](characters/坂.md) [坂](characters/坂.md) 弁<--瓣 [辦](characters/辦.md) [鈑](characters/板.md)

### 팔 
[叭](characters/叭.md) [捌 (char)](characters/捌%20(char).md) 

### 패 
[[浿]] [佩](characters/佩.md) [牌 (char)](characters/牌%20(char).md) [唄 (char)](characters/唄%20(char).md) [悖](characters/悖.md) [沛](characters/沛.md) [狽](characters/狽.md) [稗](characters/稗.md) [霸](characters/覇.md)

### 팽 
[彭](characters/彭.md) [[澎]] [[烹]] [膨](characters/膨.md) 

### 퍅 
[[愎]] 

### 편 
[扁](characters/扁.md) [[翩]] [鞭](characters/鞭.md) [騙 (char)](characters/騙%20(char).md)

### 폄 
[[貶]] 

### 평 
[坪 (char)](characters/坪%20(char).md) [[枰]] [[泙]] [[萍]] 

### 폐 
[陛](characters/陛.md) [[../../characters/吠]] [[嬖]] [[斃]] 

### 포 
[葡](characters/葡.md) [褒 (char)](characters/褒%20(char).md) [砲](characters/砲.md) [[鋪]] [[佈]] [匍](characters/爬.md) [[匏]] [[咆]] [哺](characters/哺.md) [圃](characters/圃.md) [怖](characters/怖.md) [暴 (char)](characters/暴%20(char).md) [泡](characters/泡.md) [疱](characters/疱.md) [[脯]] [[苞]] [蒲](characters/蒲.md) [[袍]] [[逋]] [鮑 (char)](characters/鮑%20(char).md) [拋](characters/抛.md)

### 폭 
[[曝]] [瀑](characters/瀑.md) [[輻]] 

### 표 
[[杓]] [豹](characters/豹.md) [彪](characters/彪.md) [[驃]] [俵](characters/俵.md) [[剽]] [慓](characters/票%20(char).md) [瓢](characters/瓢.md) [[飄]] [[飆]] 

### 품 
[稟](characters/稟.md)

### 풍 
[[諷]] [馮](characters/馮.md) [楓](characters/楓.md)

### 피 
[披 (char)](characters/披%20(char).md) [[陂]] 

### 필 
[弼](characters/弼.md) 泌 (done) [[珌]] [[苾]] [[馝]] [[鉍]] [[佖]] [疋](characters/疋.md)

### 핍 
[乏](characters/乏.md) [逼](characters/逼.md)

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
