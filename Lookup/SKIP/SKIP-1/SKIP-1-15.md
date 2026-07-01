---
date-last-perfect: 2026-07-01
tags:
  - lookup
---

> [[SKIP]] : 1

1. no
2. no
3. no
4. no
5. [SKIP-1-15-5](lookup/SKIP/SKIP-1/SKIP-1-15-5.md): 齢

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-15")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```
