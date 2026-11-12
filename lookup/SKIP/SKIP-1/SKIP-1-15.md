---
date-last-perfect: 2026-11-11
size: 1
tags: [lookup]
---

> [SKIP](lookup/SKIP/SKIP.md) : 1

Left half has 15 strokes.

1. SKIP-1-15-1: none
2. SKIP-1-15-2: none
3. SKIP-1-15-3: none
4. [SKIP-1-15-4](lookup/SKIP/SKIP-1/SKIP-1-15-4.md): ø
5. [SKIP-1-15-5](lookup/SKIP/SKIP-1/SKIP-1-15-5.md): ø
6. [SKIP-1-15-6](lookup/SKIP/SKIP-1/SKIP-1-15-6.md): 齦
7. SKIP-1-15-7: none
8. SKIP-1-15-8: none
9. [SKIP-1-15-9](lookup/SKIP/SKIP-1/SKIP-1-15-9.md): ø
10. [SKIP-1-15-10](lookup/SKIP/SKIP-1/SKIP-1-15-10.md): ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-15")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```
