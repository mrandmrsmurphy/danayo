---
stroke_count: 10
tags: [lookup]
date-last-perfect: 2026-11-12
size: 0
---
> [SKIP](lookup/SKIP/SKIP.md) : 4
> [Stroke 10](lookup/Stroke/Stroke%2010.md)

These are the 漢字 of 10 strokes in total, by subtype (1 top line, 2 bottom line, 3 vertical line, 4 none of these).

1. SKIP-4-10-1: none
2. [SKIP-4-10-2](lookup/SKIP/SKIP-4/SKIP-4-10-2.md): ø
3. [SKIP-4-10-3](lookup/SKIP/SKIP-4/SKIP-4-10-3.md): ø
4. [SKIP-4-10-4](lookup/SKIP/SKIP-4/SKIP-4-10-4.md): ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-10")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```