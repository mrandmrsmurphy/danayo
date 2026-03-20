These have been checked for redirects.
### 마
[瑪](characters/馬%20(char).md) [[痲]] [碼](characters/馬%20(char).md) [媽](characters/媽.md)

### 막
[寞](characters/寞.md) [膜](characters/膜.md) [[邈]]

### 만 
[曼](characters/曼.md) [蔓](characters/蔓.md) [[鏋]] [卍](characters/卍.md) [娩](characters/娩.md) [[巒]] [彎](characters/弯.md) [挽](characters/挽.md) [灣](characters/湾.md) [瞞](characters/𥈞.md) [輓](characters/挽.md) [饅](characters/饅.md) [鰻](characters/曼.md) [蠻](characters/蛮.md)

### 말 
[茉](characters/茉.md) !!唜!! [抹](characters/抹%20(char).md) [沫](characters/沫%20(char).md) [襪](characters/襪.md) [[靺]]

### 망 
[網](characters/網%20(char).md) [[芒]] [[輞]] [[邙]] [莽](characters/莽.md) 

### 매 
[寐](characters/寐.md) [昧](characters/昧%20(char).md) [枚](characters/枚%20(char).md) [煤](characters/煤%20(char).md) [罵](characters/罵.md) [邁](characters/邁.md) [魅](characters/魅.md) [苺](characters/苺%20(char).md)

### 맥 
貊 --> 夷 [[陌]] [[驀]]

### 맹 
[萌](characters/萌.md) [[氓]]

### 멱 
[冪](characters/冪.md) [覓](characters/覓.md)

### 면 
[冕](characters/冕.md) [棉](characters/綿.md) [[沔]] [[眄]] [緬](characters/面.md) [麪](characters/麺%20(char).md)

### 멸 
[蔑](characters/蔑%20(char).md)

### 명 
[溟](characters/冥%20(char).md) [暝](characters/冥%20(char).md) 椧! [皿](characters/皿%20(char).md) [瞑](characters/冥%20(char).md) [[茗]] [[蓂]] [[characters/螟]] [酩](characters/酩.md) [慏](characters/冥%20(char).md) [洺](characters/名%20(char).md) [[眀]] [䳟](characters/明%20(char).md)

### 몌 
[袂 (char)](characters/袂%20(char).md)

### 모 
[摸](characters/摸.md) [牟](characters/牟.md) [[謨]] [姆](characters/母.md) [帽](characters/帽.md) [摹](characters/模.md) [牡](characters/牡.md) [瑁](characters/瑁.md) [[眸]] [耗](characters/耗.md) [芼](characters/芼.md) [茅](characters/茅.md) [矛](characters/矛.md) [[橅]]

### 목 
[穆](characters/穆.md) [[鶩]] [沐](characters/沐.md)

### 몰 
[[歿]]

### 몽 
[朦](characters/蒙.md)

### 묘 
[描](characters/描.md) [[錨]] anchor [畝 (char)](characters/畝%20(char).md) [昴](characters/昴.md) [[杳]] [[渺]] [猫 (char)](characters/猫%20(char).md)

### 무 
[拇](characters/母.md) [[珷]] [撫](characters/撫.md) [[懋]] [巫](characters/巫.md) [憮](characters/無%20(char).md) [[楙]] [毋](characters/母.md) [繆](characters/謬.md) [蕪](characters/蕪.md) [誣](characters/誣.md) [鵡](characters/鵡.md) [[橅]] 

### 문 
[汶](characters/文.md) [[炆]] [紋 (char)](characters/紋%20(char).md) !們! [[刎]] [吻](characters/吻.md) [[紊]] [蚊 (char)](characters/蚊%20(char).md) [[雯]] [[抆]]

### 물 
[[沕]]

### 미 
[[渼]] [薇](characters/薇.md) [彌](characters/弥%20(char).md) [[嵄]] [[媄]] [媚](characters/眉%20(char).md) [嵋](characters/眉%20(char).md) [梶](characters/梶.md) [[楣]] [[湄]] [謎 (char)](characters/謎%20(char).md) [靡](characters/靡.md) [[黴]] [[躾]] [[媺]] [[濔]] [[煝]] [[娓]] [[洣]] [[侎]] [[瑂]]  

### 민 
[[玟]] [旻](characters/旻.md) [旼](characters/旻.md) [閔](characters/閔.md) [珉](characters/珉.md) [[岷]] [[忞]] [[慜]] [[敃]] [[愍]] [[潣]] [暋](characters/暋.md) [[䪸]] [[泯]] [悶](characters/悶.md) [[緡]] [[𩔉]] [[鍲]] [[脗]] [[閩]] [[盿]]

### 밀 
[謐](characters/謐.md)

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