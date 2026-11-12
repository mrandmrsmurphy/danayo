---
stroke_count: 8
date-last-perfect: 2026-11-12
size: 8
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 4
> [Stroke 08](lookup/Stroke/Stroke%2008.md)

These are the 漢字 of 8 strokes in total, by subtype (1 top line, 2 bottom line, 3 vertical line, 4 none of these).

1. [SKIP-4-8-1](lookup/SKIP/SKIP-4/SKIP-4-8-1.md): 雨
2. [SKIP-4-8-2](lookup/SKIP/SKIP-4/SKIP-4-8-2.md): 隹, 垂
3. [SKIP-4-8-3](lookup/SKIP/SKIP-4/SKIP-4-8-3.md): 乖, 事, 東, 秉
4. [SKIP-4-8-4](lookup/SKIP/SKIP-4/SKIP-4-8-4.md): 兎

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-8")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```