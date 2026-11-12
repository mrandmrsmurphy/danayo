---
stroke_count: 12
tags: [lookup]
date-last-perfect: 2026-11-12
size: 1
---
> [SKIP](lookup/SKIP/SKIP.md) : 4
> [Stroke 12](lookup/Stroke/Stroke%2012.md)

These are the 漢字 of 12 strokes in total, by subtype (1 top line, 2 bottom line, 3 vertical line, 4 none of these).

1. SKIP-4-12-1: none
2. SKIP-4-12-2: none
3. SKIP-4-12-3: none
4. [SKIP-4-12-4](lookup/SKIP/SKIP-4/SKIP-4-12-4.md): 幾

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-12")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```