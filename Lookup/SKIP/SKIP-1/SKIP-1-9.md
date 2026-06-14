---
date-last-perfect: 2026-06-14
tags: [lookup]

---

> [SKIP](lookup/SKIP/SKIP.md) : 1

Left half has 9 strokes. Dominant components: 革, 頁, 食.

- [SKIP-1-9-1](lookup/SKIP/SKIP-1/SKIP-1-9-1.md): none
- [SKIP-1-9-2](lookup/SKIP/SKIP-1/SKIP-1-9-2.md): 削, 副, 剰, 勒, 動, 勘, 飢
- [SKIP-1-9-3](lookup/SKIP/SKIP-1/SKIP-1-9-3.md): 彭, 鄂
- [SKIP-1-9-4](lookup/SKIP/SKIP-1/SKIP-1-9-4.md): 献, 鼓, 新, 数, 戦, 殿, 斟, 歇 …
- [SKIP-1-9-5](lookup/SKIP/SKIP-1/SKIP-1-9-5.md): 甄, 鞀, 鞄
- [SKIP-1-9-6](lookup/SKIP/SKIP-1/SKIP-1-9-6.md): 鞋, 鞍, 餃
- [SKIP-1-9-7](lookup/SKIP/SKIP-1/SKIP-1-9-7.md): 辦, 鞘, 頤, 龍
- [SKIP-1-9-8](lookup/SKIP/SKIP-1/SKIP-1-9-8.md): 雖, 鞠, 頻, 餅
- [SKIP-1-9-9](lookup/SKIP/SKIP-1/SKIP-1-9-9.md): 鞭, 額, 顎, 顔, 顕, 類
- [SKIP-1-9-10](lookup/SKIP/SKIP-1/SKIP-1-9-10.md): 韻

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-9")
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
