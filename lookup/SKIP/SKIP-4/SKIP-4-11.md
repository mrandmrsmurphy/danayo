---
stroke_count: 11
date-last-perfect: 2026-11-12
size: 3
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 4
> [Stroke 11](lookup/Stroke/Stroke%2011.md)

These are the 漢字 of 11 strokes in total, by subtype (1 top line, 2 bottom line, 3 vertical line, 4 none of these).

1. SKIP-4-11-1: none
2. SKIP-4-11-2: none
3. [SKIP-4-11-3](lookup/SKIP/SKIP-4/SKIP-4-11-3.md): 粛
4. [SKIP-4-11-4](lookup/SKIP/SKIP-4/SKIP-4-11-4.md): 戚, 爽

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-11")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```