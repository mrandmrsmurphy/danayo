---
aliases:
---
> [[SKIP]] : 2

1. [[SKIP-2-3-1]]
2. [[SKIP-2-3-2]]
3. [[SKIP-2-3-3]]
4. [[SKIP-2-3-4]]
5. [[SKIP-2-3-5]]
6. [[SKIP-2-3-6]]
7. [[SKIP-2-3-7]]
8. [[SKIP-2-3-8]]
9. [[SKIP-2-3-9]]
10. [[SKIP-2-3-10]]
11. [[SKIP-2-3-11]]
12. [[SKIP-2-3-12]]
13. [[SKIP-2-3-13]]
14. [[SKIP-2-3-14]]
15. [[SKIP-2-3-15]]
16. [[SKIP-2-3-16]]
17. [[SKIP-2-3-17]]
18. [[SKIP-2-3-18]]
19. [[SKIP-2-3-19]]
20. [[SKIP-2-3-20]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-3")
    order:
      - file.name
	  - size
      - skip_number
      - stroke_count
```