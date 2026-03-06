---
date-last-perfect: 2026-02-06
---
> [SKIP](lookup/SKIP/SKIP.md) : 4

1. No SKIP-4-1-2
2. [SKIP-4-2-2](lookup/SKIP/SKIP-4/SKIP-4-2-2.md): 七	亠	凵
3. [SKIP-4-3-2](lookup/SKIP/SKIP-4/SKIP-4-3-2.md): 彑	士	土	也	上 亡
4. [SKIP-4-4-2](lookup/SKIP/SKIP-4/SKIP-4-4-2.md): 廿	壬
5. [SKIP-4-5-2](lookup/SKIP/SKIP-4/SKIP-4-5-2.md): 白	由	丘	甘	丗 出	世	生
6. [SKIP-4-6-2](lookup/SKIP/SKIP-4/SKIP-4-6-2.md): 臼	曲	血	自
7. [SKIP-4-7-2](lookup/SKIP/SKIP-4/SKIP-4-7-2.md): 坐
8. [SKIP-4-8-2](lookup/SKIP/SKIP-4/SKIP-4-8-2.md): 垂	隹
9. [[SKIP-4-9-2]]: 重	韭
10. [[lookup/SKIP/SKIP-4/SKIP-4-10-2]]: 埀

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