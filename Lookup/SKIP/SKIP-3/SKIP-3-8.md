---
date-last-perfect:
---
> [SKIP](lookup/SKIP/SKIP.md) : 3 :

## Characters

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