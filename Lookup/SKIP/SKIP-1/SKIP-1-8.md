---
date-last-perfect: 2026-06-14
tags: [lookup]

---

> [SKIP](lookup/SKIP/SKIP.md) : 1

Left half has 8 strokes. Dominant components: 金, 食, 阜, 兼, 喬.

- SKIP-1-8-1: none
- [SKIP-1-8-2](lookup/SKIP/SKIP-1/SKIP-1-8-2.md): 釘, 剖, 剣, 剝, 剤, 剛, 針
- [SKIP-1-8-3](lookup/SKIP/SKIP-1/SKIP-1-8-3.md): 乾, 執, 尉, 彩, 彫, 敬, 部, 郭 …
- [SKIP-1-8-4](lookup/SKIP/SKIP-1/SKIP-1-8-4.md): 報, 就, 戟, 敢, 散, 敦, 斯, 朝 …
- [SKIP-1-8-5](lookup/SKIP/SKIP-1/SKIP-1-8-5.md): 嗣, 幹, 盟, 鈴, 鈿, 鉄, 鉗, 鉛 …
- [SKIP-1-8-6](lookup/SKIP/SKIP-1/SKIP-1-8-6.md): 斡, 銀, 銃, 銑, 銘, 銭, 静, 餌
- [SKIP-1-8-7](lookup/SKIP/SKIP-1/SKIP-1-8-7.md): 舗, 銹, 鋏, 鋤, 鋭, 鋳, 餓
- [SKIP-1-8-8](lookup/SKIP/SKIP-1/SKIP-1-8-8.md): 鋸, 鋼, 錆, 錐, 錘, 錠, 錦, 錫 …
- [SKIP-1-8-9](lookup/SKIP/SKIP-1/SKIP-1-8-9.md): 鍋, 鍍, 鍛, 鍬, 鍵, 鍾, 顆
- [SKIP-1-8-10](lookup/SKIP/SKIP-1/SKIP-1-8-10.md): 鎌, 鎖, 鎧, 鎬, 鎮, 韓, 魏
- [SKIP-1-8-11](lookup/SKIP/SKIP-1/SKIP-1-8-11.md): 鏡, 鵡, 鵰, 鶏
- [SKIP-1-8-12](lookup/SKIP/SKIP-1/SKIP-1-8-12.md): 鐘
- SKIP-1-8-13: none
- SKIP-1-8-14: none
- [SKIP-1-8-15](lookup/SKIP/SKIP-1/SKIP-1-8-15.md): 鑑, 鑠

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-8")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
    sort:
      - property: size
        direction: DESC

```
