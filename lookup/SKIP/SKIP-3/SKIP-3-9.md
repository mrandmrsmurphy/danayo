---
date-last-perfect: 2026-11-12
size: 2
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 3

Surrounding component has 9 strokes. Dominant component: 是.

1. SKIP-3-9-1: none
2. [SKIP-3-9-2](lookup/SKIP/SKIP-3/SKIP-3-9-2.md): 匙
3. SKIP-3-9-3: none
4. SKIP-3-9-4: none
5. [SKIP-3-9-5](lookup/SKIP/SKIP-3/SKIP-3-9-5.md): ø
6. SKIP-3-9-6: none
7. SKIP-3-9-7: none
8. SKIP-3-9-8: none
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
