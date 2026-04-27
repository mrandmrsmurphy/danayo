---
stroke_count: 12
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 4
> [Stroke 12](lookup/Stroke/Stroke%2012.md)

1. ??
2. ??
3. ??
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