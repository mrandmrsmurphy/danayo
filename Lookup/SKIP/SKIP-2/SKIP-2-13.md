---
aliases: 
---
> [[SKIP]] : 2

1. no
2. no
3. [SKIP-2-13-3](lookup/SKIP/SKIP-2/SKIP-2-13-3.md)
4. [[SKIP-2-13-4]]
5. [[SKIP-2-13-5]]
6. q
7. q
8. q
9. [[SKIP-2-13-9]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-13")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```