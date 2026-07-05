---
date-last-perfect: 2026-07-05
tags:
  - lookup
---

> [[SKIP]] : 1

1. no
2. no
3. no
4. no
5. [SKIP-1-15-5](lookup/SKIP/SKIP-1/SKIP-1-15-5.md): 齢
6. [SKIP-1-15-6](lookup/SKIP/SKIP-1/SKIP-1-15-6.md): 齦
7. no
8. no
9. no
10. [SKIP-1-15-10](lookup/SKIP/SKIP-1/SKIP-1-15-10.md): 皺

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
