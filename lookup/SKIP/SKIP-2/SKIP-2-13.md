---
date-last-perfect: 2026-11-11
size: 7
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 2

Top component has 13 strokes.

1. SKIP-2-13-1: none
2. SKIP-2-13-2: none
3. [SKIP-2-13-3](lookup/SKIP/SKIP-2/SKIP-2-13-3.md): 墾, 壁
4. [SKIP-2-13-4](lookup/SKIP/SKIP-2/SKIP-2-13-4.md): 懇, 檗, 檠
5. [SKIP-2-13-5](lookup/SKIP/SKIP-2/SKIP-2-13-5.md): 璧
6. [SKIP-2-13-6](lookup/SKIP/SKIP-2/SKIP-2-13-6.md): ø
7. [SKIP-2-13-7](lookup/SKIP/SKIP-2/SKIP-2-13-7.md): ø
8. SKIP-2-13-8: none
9. [SKIP-2-13-9](lookup/SKIP/SKIP-2/SKIP-2-13-9.md): 饗
10. SKIP-2-13-10: none
11. [SKIP-2-13-11](lookup/SKIP/SKIP-2/SKIP-2-13-11.md): ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-13")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```