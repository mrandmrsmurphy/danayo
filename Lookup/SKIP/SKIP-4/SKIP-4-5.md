---
date-last-perfect: 2026-07-05
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 4
> [Stroke 05](lookup/Stroke/Stroke%2005.md)

- [SKIP-4-5-1](lookup/SKIP/SKIP-4/SKIP-4-5-1.md): 且, 丙, 冊, 凸, 凹, 平, 正, 母, 玉, 瓦, 甲, 疋, 皿
- [SKIP-4-5-2](lookup/SKIP/SKIP-4/SKIP-4-5-2.md): 丘, 出, 甘, 由, 白, 世, 生
- [SKIP-4-5-3](lookup/SKIP/SKIP-4/SKIP-4-5-3.md): 乎, 未, 本, 禾, 冉, 半, 末, 朮, 申
- [SKIP-4-5-4](lookup/SKIP/SKIP-4/SKIP-4-5-4.md): 史, 央, 失, 弗, 戊, 犮

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-5")
    order:
      - file.name
      - size
      - date-last-perfect
      - skip_number
      - stroke_count
```
