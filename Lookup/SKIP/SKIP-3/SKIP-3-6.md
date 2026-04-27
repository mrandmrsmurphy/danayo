---
date-last-perfect:
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 3 :

1. no
2. no
3. [SKIP-3-6-3](lookup/SKIP/SKIP-3/SKIP-3-6-3.md)
4. [SKIP-3-6-4](lookup/SKIP/SKIP-3/SKIP-3-6-4.md)
5. [SKIP-3-6-5](lookup/SKIP/SKIP-3/SKIP-3-6-5.md)
6. [SKIP-3-6-6](lookup/SKIP/SKIP-3/SKIP-3-6-6.md)
7. [SKIP-3-6-7](lookup/SKIP/SKIP-3/SKIP-3-6-7.md)
8. [SKIP-3-6-8](lookup/SKIP/SKIP-3/SKIP-3-6-8.md)
9. [SKIP-3-6-9](lookup/SKIP/SKIP-3/SKIP-3-6-9.md)
10. no
11. [SKIP-3-6-11](lookup/SKIP/SKIP-3/SKIP-3-6-11.md)

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-3"
        - file.hasLink("SKIP-3-6")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```