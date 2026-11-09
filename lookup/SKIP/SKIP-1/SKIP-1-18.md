---
date-last-perfect: 2026-11-09
size: 0
tags: [lookup]

---

> [SKIP](lookup/SKIP/SKIP.md) : 1

Left half has 18 strokes.

- SKIP-1-18-1: none
- SKIP-1-18-2: none
- SKIP-1-18-3: none
- SKIP-1-18-4: none
- SKIP-1-18-5: none
- SKIP-1-18-6: none
- SKIP-1-18-7: none
- SKIP-1-18-8: none
- SKIP-1-18-9: none
- [SKIP-1-18-10](lookup/SKIP/SKIP-1/SKIP-1-18-10.md): ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-18")
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
