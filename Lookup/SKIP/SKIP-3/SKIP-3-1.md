---
date-last-perfect: 2026-03-07
---
> [SKIP](lookup/SKIP/SKIP.md) : 3 :

1. [SKIP-3-1-4](lookup/SKIP/SKIP-3/SKIP-3-1-4.md): 司

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-3"
        - file.hasLink("SKIP-3-1")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```