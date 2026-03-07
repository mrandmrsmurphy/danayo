---
date-last-perfect:
---
> [SKIP](lookup/SKIP/SKIP.md) : 1 :

1. no
2. [[SKIP-1-12-2]]
3. [[SKIP-1-12-3]]
4. [[SKIP-1-12-4]]
5. [[SKIP-1-12-5]]
6. [[SKIP-1-12-6]]
7. [[SKIP-1-12-7]]
8. no
9. [[SKIP-1-12-9]]
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