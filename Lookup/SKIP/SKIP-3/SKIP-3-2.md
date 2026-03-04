---
date-last-perfect: 2026-02-01
---
> [SKIP](lookup/SKIP/SKIP.md) : 3

1. [SKIP-3-2-1](lookup/SKIP/SKIP-3/SKIP-3-2-1.md)
2. [[SKIP-3-2-2]]
3. [[SKIP-3-2-3]]
4. [[SKIP-3-2-4]]
5. [[SKIP-3-2-5]]
6. [[SKIP-3-2-6]]
7. [[SKIP-3-2-7]]
8. [[SKIP-3-2-8]]
9. [[SKIP-3-2-9]]
10. [[SKIP-3-2-10]]
11. [[SKIP-3-2-11]]
12. [SKIP-3-2-12](lookup/SKIP/SKIP-3/SKIP-3-2-12.md)
13. [[SKIP-3-2-13]]
14. none
15. [[SKIP-3-2-15]]
16. none
17. [[SKIP-3-2-17]]
18. none
19. none
20. none
21. none
22. [SKIP-3-2-22](lookup/SKIP/SKIP-3/SKIP-3-2-22.md)

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-3"
        - file.hasLink("SKIP-3-2")
    order:
      - file.name
	  - size
      - skip_number
      - stroke_count
```