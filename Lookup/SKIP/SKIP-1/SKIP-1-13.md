---
date-last-perfect: 2026-03-07
---
> [SKIP](lookup/SKIP/SKIP.md) : 1 :

1. No
2. [SKIP-1-13-2](lookup/SKIP/SKIP-1/SKIP-1-13-2.md): 劇, 劉
3. No
4. No
5. No
6. [SKIP-1-13-6](lookup/SKIP/SKIP-1/SKIP-1-13-6.md): 艶

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