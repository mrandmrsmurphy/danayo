---
date-last-perfect: 2026-07-05
tags: [lookup]

---

> [SKIP](lookup/SKIP/SKIP.md) : 1

Left half has 14 strokes.

- SKIP-1-14-1: none
- [SKIP-1-14-2](lookup/SKIP/SKIP-1/SKIP-1-14-2.md): 叡

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-14")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
    sort:
      - property: size
        direction: DESC

```
