---
date-last-perfect: 2026-09-24
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 4

1. No SKIP-4-1-2
2. [SKIP-4-2-2](lookup/SKIP/SKIP-4/SKIP-4-2-2.md): 七
3. [SKIP-4-3-2](lookup/SKIP/SKIP-4/SKIP-4-3-2.md): 上, 也, 土, 士, 亡
4. [SKIP-4-4-2](lookup/SKIP/SKIP-4/SKIP-4-4-2.md): 壬, 廿
5. [SKIP-4-5-2](lookup/SKIP/SKIP-4/SKIP-4-5-2.md): 丘, 出, 甘, 由, 白, 世, 生
6. [SKIP-4-6-2](lookup/SKIP/SKIP-4/SKIP-4-6-2.md): 臼, 血, 曲, 自
7. [SKIP-4-7-2](lookup/SKIP/SKIP-4/SKIP-4-7-2.md): 坐
8. [SKIP-4-8-2](lookup/SKIP/SKIP-4/SKIP-4-8-2.md): 垂, 隹
9. [SKIP-4-9-2](lookup/SKIP/SKIP-4/SKIP-4-9-2.md): 重
10. [SKIP-4-10-2](lookup/SKIP/SKIP-4/SKIP-4-10-2.md): ø (redirect only: 埀 --> 垂)

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-0-2")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```