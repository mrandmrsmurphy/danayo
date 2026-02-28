---
date-last-perfect:
---
> [[SKIP]] : 2

1. None
2. None
3. [[SKIP-2-7-3]]: 
4. [[SKIP-2-7-4]]: 
5. [[SKIP-2-7-5]]
6. [[SKIP-2-7-6]]
7. [[SKIP-2-7-7]]
8. [[SKIP-2-7-8]]
9. [[SKIP-2-7-9]]
10. [[SKIP-2-7-10]]
11. [[SKIP-2-7-11]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-7")
    order:
      - file.name
      - size
      - date-last-perfect
      - skip_number
      - stroke_count
    columnSize:
      note.danayo_id: 64
      note.english: 236
```