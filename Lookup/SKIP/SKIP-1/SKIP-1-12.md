---
date-last-perfect: 2026-03-07
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 1 :

1. no
2. [SKIP-1-12-2](lookup/SKIP/SKIP-1/SKIP-1-12-2.md): 劃
3. [SKIP-1-12-3](lookup/SKIP/SKIP-1/SKIP-1-12-3.md): 影, 鄧, 鄭
4. [SKIP-1-12-4](lookup/SKIP/SKIP-1/SKIP-1-12-4.md): 獣
5. [SKIP-1-12-5](lookup/SKIP/SKIP-1/SKIP-1-12-5.md): 黜, 黻
6. [SKIP-1-12-6](lookup/SKIP/SKIP-1/SKIP-1-12-6.md): 翻
7. [SKIP-1-12-7](lookup/SKIP/SKIP-1/SKIP-1-12-7.md): 黼
8. no
9. [SKIP-1-12-9](lookup/SKIP/SKIP-1/SKIP-1-12-9.md): 顧
10. [SKIP-1-12-10](lookup/SKIP/SKIP-1/SKIP-1-12-10.md): 懿

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-12")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```