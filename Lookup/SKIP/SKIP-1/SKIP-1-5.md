---
date-last-perfect: 2026-03-06
---
> SKIP : 1


```dataviewjs
const pages = dv.pages()
  .where(p => p.skip_number === "1-5-9")
// or stricter: .where(p => p["your_property"] === "value")
// or for numbers/strings/etc: adjust comparison as needed

const titles = pages
  .map(p => p.file.name)
  .sort()                    // optional: alphabetical sort
  .join(", ");

dv.paragraph(titles || "No matching pages");
````

1. No
2. [[SKIP-1-5-2]]: 初, 判, 別, 利, 刪, 助, 劫, 劭, 励, 即, 却, 町, 私
3. [[SKIP-1-5-3]]: 和, 的, 知, 社, 祀, 突, 邱, 邵, 邸
4. [[SKIP-1-5-4]]: 叚, 叛, 政, 故, 段, 盼, 研, 砕, 祝, 秋, 科, 秒, 級, 胡, 袂
5. [[SKIP-1-5-5]]: 弱, 既, 玆, 畔, 眠, 矩, 砥, 砧, 砭, 砲, 破, 祚, 神, 秘, 租, 秩, 称, 站, 袖, 被
6. [[SKIP-1-5-6]]: 務, 甜, 略, 眺, 眼, 硅, 移, 袴
7. [[SKIP-1-5-7]]: 甥, 疎, 皓, 短, 硝, 硫, 硬, 硯, 祷, 程, 稍, 税, 竦, 裕, 補
8. [[SKIP-1-5-8]]: 睛, 睡, 睦, 矮, 碍, 碗, 祿, 禍, 稗, 稚, 稜, 蜂, 裸, 裾, 褐, 雅, 雉, 雌, 靖
9. [[SKIP-1-5-9]]: 暢, 碑, 碩, 磁, 種, 稲, 端, 複, 頗, 領, 颯, 𥈞
10. [[SKIP-1-5-10]]: 確, 碼, 磋, 稷, 稼, 稽, 稿, 穂
11. [[SKIP-1-5-11]]: 磚, 穆, 積, 穏, 鴔, 鴨
12. [[SKIP-1-5-12]]: 瞬, 瞭, 瞳, 矯, 磯, 礁, 襖
13. [[SKIP-1-5-13]]: 瞻, 瞼, 礎, 穫, 襟
14. [[SKIP-1-5-14]]: 襪
15. No
16. No
17. [SKIP-1-5-17](lookup/SKIP/SKIP-1/SKIP-1-5-17.md): 穣

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-5")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```