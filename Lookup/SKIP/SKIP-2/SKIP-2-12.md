---
date-last-perfect:
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 2 :

## Characters

1. no
2. no
3. [[lookup/SKIP/SKIP-2/SKIP-2-12-3]]
4. [[lookup/SKIP/SKIP-2/SKIP-2-12-4]]
5. [[lookup/SKIP/SKIP-2/SKIP-2-12-5]]
6. No
7. [[lookup/SKIP/SKIP-2/SKIP-2-12-7]]
8. [[SKIP-2-12-8]]
9. no
10. no
11. no
12. no
13. [[lookup/SKIP/SKIP-2/SKIP-2-12-13]]
14. [[lookup/SKIP/SKIP-2/SKIP-2-12-14]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-12")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```