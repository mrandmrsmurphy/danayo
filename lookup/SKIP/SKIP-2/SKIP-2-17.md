---
date-last-perfect: 2026-11-11
size: 0
tags: [lookup]

---

> [SKIP](lookup/SKIP/SKIP.md) : 2

Top half has 17 strokes.

- SKIP-2-17-1: none
- SKIP-2-17-2: none
- SKIP-2-17-3: none
- [SKIP-2-17-4](lookup/SKIP/SKIP-2/SKIP-2-17-4.md): ø
- SKIP-2-17-5: none
- SKIP-2-17-6: none
- SKIP-2-17-7: none
- [SKIP-2-17-8](lookup/SKIP/SKIP-2/SKIP-2-17-8.md): ø
- SKIP-2-17-9: none
- SKIP-2-17-10: none
- SKIP-2-17-11: none
- SKIP-2-17-12: none
- SKIP-2-17-13: none
- SKIP-2-17-14: none
- SKIP-2-17-15: none
- [SKIP-2-17-16](lookup/SKIP/SKIP-2/SKIP-2-17-16.md): ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-17")
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
