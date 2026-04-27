---
date-last-perfect:
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 3 :

1. No
2. [[SKIP-3-7-2]]: 赴
3. [[SKIP-3-7-3]]
4. [[SKIP-3-7-4]]
5. [[SKIP-3-7-5]]
6. No
7. [[SKIP-3-7-7]]
8. [[SKIP-3-7-8]]
9. [[SKIP-3-7-9]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-3"
        - file.hasLink("SKIP-3-7")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```