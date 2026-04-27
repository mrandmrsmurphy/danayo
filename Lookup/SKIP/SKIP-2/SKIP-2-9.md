---
date-last-perfect:
tags: [lookup]

---
> [[SKIP]] : 2 

1. None
2. [[SKIP-2-9-2]]: 
3. [[SKIP-2-9-3]]
4. [[SKIP-2-9-4]]
5. [[SKIP-2-9-5]]
6. [[SKIP-2-9-6]]
7. [[SKIP-2-9-7]]
8. None
9. None
10. None
11. None
12. [[SKIP-2-9-12]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-9")
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