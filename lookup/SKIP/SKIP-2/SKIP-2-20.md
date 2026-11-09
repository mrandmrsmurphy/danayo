---
date-last-perfect: 2026-11-09
size: 0
tags: [lookup]

---

> [SKIP](lookup/SKIP/SKIP.md) : 2

Top half has 20 strokes.

- SKIP-2-20-1: none
- SKIP-2-20-2: none
- SKIP-2-20-3: none
- SKIP-2-20-4: none
- [SKIP-2-20-5](lookup/SKIP/SKIP-2/SKIP-2-20-5.md): ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-20")
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
