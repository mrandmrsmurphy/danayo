---
date-last-perfect:
---
> [SKIP](lookup/SKIP/SKIP.md) : 3 :

1. No
2. [[SKIP-3-8-2]]
3. [[SKIP-3-8-3]]
4. [[SKIP-3-8-4]]
5. No
6. [[SKIP-3-8-6]]
7. [[SKIP-3-8-7]]
8. [[SKIP-3-8-8]]
9. [[SKIP-3-8-9]]
10. [[SKIP-3-8-10]]


## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-3"
        - file.hasLink("SKIP-3-8")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```