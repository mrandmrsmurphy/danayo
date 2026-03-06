---
stroke_count: 9
---
> [SKIP](lookup/SKIP/SKIP.md) : 4
> [Stroke 09](lookup/Stroke/Stroke%2009.md)

1. [SKIP-4-9-1](lookup/SKIP/SKIP-4/SKIP-4-9-1.md): 飛
2. [SKIP-4-9-2](lookup/SKIP/SKIP-4/SKIP-4-9-2.md): 重
3. [[lookup/SKIP/SKIP-4/SKIP-4-9-3]]: 乗, 柬, 禹, 禺
4. [[SKIP-4-9-4]]: 咸, 威, 為

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
      - skip_number
      - stroke_count
      - date-last-perfect

```