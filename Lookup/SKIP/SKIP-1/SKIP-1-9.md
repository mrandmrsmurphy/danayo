---
date-last-perfect:
tags: [lookup]

---
> [[SKIP]] : 1 


1. no
2. [[SKIP-1-9-2]]
3. [[SKIP-1-9-3]]
4. [[SKIP-1-9-4]]
5. [[SKIP-1-9-5]]
6. [[SKIP-1-9-6]]
7. [[SKIP-1-9-7]]
8. [[SKIP-1-9-8]]
9. [[SKIP-1-9-9]]
10. [[SKIP-1-9-10]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-9")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```