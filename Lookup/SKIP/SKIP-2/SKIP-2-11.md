---
date-last-perfect: 2026-07-05
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 2

Top component has 11 strokes.

1. none
2. [SKIP-2-11-2](lookup/SKIP/SKIP-2/SKIP-2-11-2.md): 勢, 準
3. [SKIP-2-11-3](lookup/SKIP/SKIP-2/SKIP-2-11-3.md): 塾, 墊
4. [SKIP-2-11-4](lookup/SKIP/SKIP-2/SKIP-2-11-4.md): 勲, 撃, 暫, 熟, 熱, 黙, 慙, 摯, 熬, 慰, 熨
5. [SKIP-2-11-5](lookup/SKIP/SKIP-2/SKIP-2-11-5.md): 整
6. [SKIP-2-11-6](lookup/SKIP/SKIP-2/SKIP-2-11-6.md): 繋, 蟄
7. [SKIP-2-11-7](lookup/SKIP/SKIP-2/SKIP-2-11-7.md): 麌, 謦, 豐, 贄, 贅, 蹙, 醫
8. ø
9. [SKIP-2-11-9](lookup/SKIP/SKIP-2/SKIP-2-11-9.md): 響, 馨
10. ø
11. ø
12. none
13. ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-11")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```
