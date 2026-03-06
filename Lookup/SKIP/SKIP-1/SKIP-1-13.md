---
date-last-perfect:
---
> [SKIP](lookup/SKIP/SKIP.md) : 1 :

## Characters

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-13")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```