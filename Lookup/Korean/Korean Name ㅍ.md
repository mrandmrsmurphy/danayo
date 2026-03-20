### 파 
[巴 (char)](characters/巴%20(char).md) [芭](characters/芭.md) [琶](characters/琶.md) [[坂|坡 [[把|杷]] [[婆]] [[擺]] [[爬]] [[坂|跛]]

### 판 
[[坂|阪]] [[坂]] 弁<--瓣 [[辦]] [[板|鈑]]

### 팔 
[[叭]] [[捌]] 

### 패 
[[浿]] [[佩]] [[牌]] [唄 (char)](characters/唄%20(char).md) [[悖]] [[沛]] [[狽]] [[稗]] [[覇|霸]]

### 팽 
[[彭]] [[澎]] [[烹]] [[膨]] 

### 퍅 
[[愎]] 

### 편 
[[扁]] [[翩]] [[鞭]] [[騙]]

### 폄 
[[貶]] 

### 평 
[[坪]] [[枰]] [[泙]] [[萍]] 

### 폐 
[[陛]] [[吠]] [[嬖]] [[斃]] 

### 포 
[[葡]] [[褒]] [[砲]] [[鋪]] [[佈]] [[匍]] [[匏]] [[咆]] [[哺]] [[圃]] [[怖]] [[暴]] [[泡]] [[疱]] [[脯]] [[苞]] [[蒲]] [[袍]] [[逋]] [[鮑 (char)]] [[拋]]

### 폭 
[[曝]] [[瀑]] [[輻]] 

### 표 
[[杓]] [[豹]] [[彪]] [[驃]] [[俵]] [[剽]] [[慓]] [[瓢]] [[飄]] [[飆]] 

### 품 
[[稟]]

### 풍 
[[諷]] [[馮]] [[楓]]

### 피 
[[披]] [[陂]] 

### 필 
[[弼]] 泌 (done) [[珌]] [[苾]] [[馝]] [[鉍]] [[佖]] [[疋]]

### 핍 
[[乏]] [[逼]]

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
