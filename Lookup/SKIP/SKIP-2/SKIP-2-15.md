---
date-last-perfect:
---
> [SKIP](lookup/SKIP/SKIP.md) : 2 :

## Characters
1. [[SKIP-2-15-2]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-15")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```