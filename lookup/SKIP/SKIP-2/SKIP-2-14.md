---
date-last-perfect: 2026-11-11
size: 5
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 2

Top component has 14 strokes.

1. SKIP-2-14-1: none
2. [SKIP-2-14-2](lookup/SKIP/SKIP-2/SKIP-2-14-2.md): 興
3. [SKIP-2-14-3](lookup/SKIP/SKIP-2/SKIP-2-14-3.md): 嬰
4. [SKIP-2-14-4](lookup/SKIP/SKIP-2/SKIP-2-14-4.md): 懲
5. [SKIP-2-14-5](lookup/SKIP/SKIP-2/SKIP-2-14-5.md): 璽, 㽉
6. SKIP-2-14-6: none
7. SKIP-2-14-7: none
8. SKIP-2-14-8: none
9. SKIP-2-14-9: none
10. SKIP-2-14-10: none
11. SKIP-2-14-11: none
12. SKIP-2-14-12: none
13. SKIP-2-14-13: none
14. SKIP-2-14-14: none
15. [SKIP-2-14-15](lookup/SKIP/SKIP-2/SKIP-2-14-15.md): ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-14")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```