---
date-last-perfect: 2026-05-24
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 3

Surrounding component has 9 strokes. Dominant component: 是.

1. ø
2. [SKIP-3-9-2](lookup/SKIP/SKIP-3/SKIP-3-9-2.md): 匙
3. ø
4. ø
5. ø
6. ø
7. ø
8. ø
9. [SKIP-3-9-9](lookup/SKIP/SKIP-3/SKIP-3-9-9.md): 題

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-3"
        - file.hasLink("SKIP-3-9")
    order:
      - file.name
      - size
      - date-last-perfect
      - skip_number
      - stroke_count
```
