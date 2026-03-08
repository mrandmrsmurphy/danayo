---
aliases:
---
> [[SKIP]] : 2

1. None
2. [[SKIP-2-8-2]]: 隼
3. [[SKIP-2-8-3]]: 啓, 堂, 堕, 娶, 婁, 婆, 彗, 雪
4. [[SKIP-2-8-4]]
5. [[SKIP-2-8-5]]
6. [[SKIP-2-8-6]]
7. [[SKIP-2-8-7]]
8. [[SKIP-2-8-8]]
9. [[SKIP-2-8-9]]
10. [[SKIP-2-8-10]]
11. [[SKIP-2-8-11]]
12. No
13. [[SKIP-2-8-13]]
14. none
15. none
16. [[SKIP-2-8-16]]


## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-8")
    order:
      - file.name
	  - size
      - skip_number
      - stroke_count
```