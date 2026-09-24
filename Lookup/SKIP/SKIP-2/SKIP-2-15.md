---
date-last-perfect: 2026-09-24
tags:
  - lookup
---
> [SKIP](lookup/SKIP/SKIP.md) : 2

Top component has 15 strokes.

1. none
2. [SKIP-2-15-2](lookup/SKIP/SKIP-2/SKIP-2-15-2.md): 輿

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