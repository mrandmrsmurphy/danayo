---
date-last-perfect: 2026-07-05
tags: [lookup]

---

> [SKIP](lookup/SKIP/SKIP.md) : 2

Top half has 16 strokes.

- SKIP-2-16-1: none
- SKIP-2-16-2: none
- SKIP-2-16-3: none
- [SKIP-2-16-4](lookup/SKIP/SKIP-2/SKIP-2-16-4.md): 懸 (char)
- SKIP-2-16-5: none
- [SKIP-2-16-6](lookup/SKIP/SKIP-2/SKIP-2-16-6.md): 聾, 襲, 龔
- [SKIP-2-16-7](lookup/SKIP/SKIP-2/SKIP-2-16-7.md): 讐

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-16")
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
