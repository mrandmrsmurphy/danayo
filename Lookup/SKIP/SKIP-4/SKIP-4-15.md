---
stroke_count: 15
date-last-perfect: 2026-03-06
---
> SKIP : 4
> [Stroke 15](lookup/Stroke/Stroke%2015.md)

1. None
2. None
3. None
4. [SKIP-4-15-4](lookup/SKIP/SKIP-4/SKIP-4-15-4.md): 畿

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-15")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```