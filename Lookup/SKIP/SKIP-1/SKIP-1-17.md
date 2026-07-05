---
date-last-perfect: 2026-07-05
tags: [lookup]

---

> [SKIP](lookup/SKIP/SKIP.md) : 1

Left half has 17 strokes.

- SKIP-1-17-1: none
- SKIP-1-17-2: none
- SKIP-1-17-3: none
- SKIP-1-17-4: none
- SKIP-1-17-5: none
- SKIP-1-17-6: none
- SKIP-1-17-7: none
- SKIP-1-17-8: none
- SKIP-1-17-9: none
- SKIP-1-17-10: none
- [SKIP-1-17-11](lookup/SKIP/SKIP-1/SKIP-1-17-11.md): 鸚

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-17")
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
