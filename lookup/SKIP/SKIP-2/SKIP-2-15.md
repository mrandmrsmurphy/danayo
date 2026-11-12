---
date-last-perfect: 2026-11-11
size: 1
tags: [lookup]
---
> [SKIP](lookup/SKIP/SKIP.md) : 2

Top component has 15 strokes.

1. SKIP-2-15-1: none
2. [SKIP-2-15-2](lookup/SKIP/SKIP-2/SKIP-2-15-2.md): 輿
3. SKIP-2-15-3: none
4. SKIP-2-15-4: none
5. SKIP-2-15-5: none
6. SKIP-2-15-6: none
7. [SKIP-2-15-7](lookup/SKIP/SKIP-2/SKIP-2-15-7.md): ø
8. [SKIP-2-15-8](lookup/SKIP/SKIP-2/SKIP-2-15-8.md): ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-15")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```