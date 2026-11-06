---
date-last-perfect: 2026-10-04
size: 5
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 2 :

1. no
2. [SKIP-2-14-2](lookup/SKIP/SKIP-2/SKIP-2-14-2.md): 興
3. [SKIP-2-14-3](lookup/SKIP/SKIP-2/SKIP-2-14-3.md): 嬰
4. [SKIP-2-14-4](lookup/SKIP/SKIP-2/SKIP-2-14-4.md): 懲
5. [SKIP-2-14-5](lookup/SKIP/SKIP-2/SKIP-2-14-5.md): 璽, 㽉
6. none
7. none
8. none
9. none
10. none
11. none
12. none
13. none
14. none
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