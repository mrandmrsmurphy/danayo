---
date-last-perfect: 2026-03-07
---
> [SKIP](lookup/SKIP/SKIP.md) : 3 :

1. [SKIP-3-1-1](SKIP-3-1-1.md): 匕
2. no
3. no
4. [SKIP-3-1-4](lookup/SKIP/SKIP-3/SKIP-3-1-4.md): 司
5. no
6. no
7. [SKIP-3-1-7](lookup/SKIP/SKIP-3/SKIP-3-1-7.md): 直, 虱

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