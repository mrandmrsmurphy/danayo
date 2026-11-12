---
date-last-perfect: 2026-11-12
size: 0
tags: [lookup]

---

> [SKIP](lookup/SKIP/SKIP.md) : 2

Top half has 19 strokes.

- SKIP-2-19-1: none
- SKIP-2-19-2: none
- [SKIP-2-19-3](lookup/SKIP/SKIP-2/SKIP-2-19-3.md): ø
- [SKIP-2-19-4](lookup/SKIP/SKIP-2/SKIP-2-19-4.md): ø
- SKIP-2-19-5: none
- SKIP-2-19-6: none
- SKIP-2-19-7: none
- SKIP-2-19-8: none
- SKIP-2-19-9: none
- SKIP-2-19-10: none
- [SKIP-2-19-11](lookup/SKIP/SKIP-2/SKIP-2-19-11.md): ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-19")
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
