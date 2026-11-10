---
date-last-perfect: 2026-11-09
size: 0
tags: [lookup]

---

> [SKIP](lookup/SKIP/SKIP.md) : 1

Left half has 16 strokes.

- SKIP-1-16-1: none
- SKIP-1-16-2: none
- SKIP-1-16-3: none
- [SKIP-1-16-4](lookup/SKIP/SKIP-1/SKIP-1-16-4.md): ø
- SKIP-1-16-5: none
- SKIP-1-16-6: none
- SKIP-1-16-7: none
- SKIP-1-16-8: none
- SKIP-1-16-9: none
- SKIP-1-16-10: none
- [SKIP-1-16-11](lookup/SKIP/SKIP-1/SKIP-1-16-11.md): ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-16")
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
