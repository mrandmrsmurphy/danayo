---
stroke_count: 10
---
> [SKIP](lookup/SKIP/SKIP.md) : 4 
> [Stroke 10](lookup/Stroke/Stroke%2010.md)

1. No
2. [SKIP-4-10-2](lookup/SKIP/SKIP-4/SKIP-4-10-2.md): _only redirect_
3. [SKIP-4-10-3](lookup/SKIP/SKIP-4/SKIP-4-10-3.md): ø
4. No

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