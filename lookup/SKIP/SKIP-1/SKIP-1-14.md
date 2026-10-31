---
date-last-perfect: 2026-10-04
size: 2
tags: [lookup]

---

> [SKIP](lookup/SKIP/SKIP.md) : 1

Left half has 14 strokes.

- SKIP-1-14-1: none
- [SKIP-1-14-2](lookup/SKIP/SKIP-1/SKIP-1-14-2.md): 叡
- [SKIP-1-14-3](lookup/SKIP/SKIP-1/SKIP-1-14-3.md): 鼾

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
