---
date-last-perfect: 2026-11-11
size: 3
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 1

Left half has 13 strokes.

1. SKIP-1-13-1: none
2. [SKIP-1-13-2](lookup/SKIP/SKIP-1/SKIP-1-13-2.md): 劇, 劉
3. [SKIP-1-13-3](lookup/SKIP/SKIP-1/SKIP-1-13-3.md): ø
4. [SKIP-1-13-4](lookup/SKIP/SKIP-1/SKIP-1-13-4.md): ø
5. SKIP-1-13-5: none
6. [SKIP-1-13-6](lookup/SKIP/SKIP-1/SKIP-1-13-6.md): 艶

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-13")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```