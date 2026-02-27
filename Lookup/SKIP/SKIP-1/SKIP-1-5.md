---
aliases:
---
> [[SKIP]] : 1

1. No
2. [[SKIP-1-5-2]]
3. [[SKIP-1-5-3]]
4. [[SKIP-1-5-4]]
5. [[SKIP-1-5-5]]
6. [[SKIP-1-5-6]]
7. [[SKIP-1-5-7]]
8. [[SKIP-1-5-8]]
9. [[SKIP-1-5-9]]
10. [[SKIP-1-5-10]]
11. [[SKIP-1-5-11]]
12. [[SKIP-1-5-12]]
13. [[SKIP-1-5-13]]
14. [[SKIP-1-5-14]]
15. [[SKIP-1-5-15]]
16. [[SKIP-1-5-16]]
17. [[SKIP-1-5-17]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-5")
    order:
      - file.name
	  - size
      - skip_number
      - stroke_count
```