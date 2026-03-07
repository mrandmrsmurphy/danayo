---
date-last-perfect: 2026-02-01
---
> [SKIP](lookup/SKIP/SKIP.md) : 2

1. [[SKIP-2-1-1]] (only 二)
2. [[SKIP-2-1-2]] (only 三)
3. [[SKIP-2-1-3]]
4. [[SKIP-2-1-4]]
5. [[SKIP-2-1-5]]
6. [[SKIP-2-1-6]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-1")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```