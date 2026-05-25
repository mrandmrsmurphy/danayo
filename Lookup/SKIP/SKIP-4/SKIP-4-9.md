---
date-last-perfect: 2026-05-24
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 4
> [Stroke 09](lookup/Stroke/Stroke%2009.md)

- [SKIP-4-9-1](lookup/SKIP/SKIP-4/SKIP-4-9-1.md): 飛
- [SKIP-4-9-2](lookup/SKIP/SKIP-4/SKIP-4-9-2.md): 重
- [SKIP-4-9-3](lookup/SKIP/SKIP-4/SKIP-4-9-3.md): 乗, 柬, 禹, 禺
- [SKIP-4-9-4](lookup/SKIP/SKIP-4/SKIP-4-9-4.md): 咸, 威, 為

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-9")
    order:
      - file.name
      - size
      - date-last-perfect
      - skip_number
      - stroke_count
```
