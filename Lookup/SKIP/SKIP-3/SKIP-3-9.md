---
date-last-perfect:
---
> [SKIP](lookup/SKIP/SKIP.md) : 3 :

1. NO
2. [[SKIP-3-9-2]]
3. no
4. no
5. no
6. no
7. no
8. no
9. [[SKIP-3-9-9]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-3"
        - file.hasLink("SKIP-3-9")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```