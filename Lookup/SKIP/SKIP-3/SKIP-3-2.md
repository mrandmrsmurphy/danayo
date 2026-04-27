---
date-last-perfect: 2026-02-01
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 3

1. [SKIP-3-2-1](lookup/SKIP/SKIP-3/SKIP-3-2-1.md)
2. [SKIP-3-2-2](lookup/SKIP/SKIP-3/SKIP-3-2-2.md)
3. [SKIP-3-2-3](lookup/SKIP/SKIP-3/SKIP-3-2-3.md)
4. [SKIP-3-2-4](lookup/SKIP/SKIP-3/SKIP-3-2-4.md)
5. [SKIP-3-2-5](lookup/SKIP/SKIP-3/SKIP-3-2-5.md)
6. [SKIP-3-2-6](lookup/SKIP/SKIP-3/SKIP-3-2-6.md)
7. [SKIP-3-2-7](lookup/SKIP/SKIP-3/SKIP-3-2-7.md)
8. [SKIP-3-2-8](lookup/SKIP/SKIP-3/SKIP-3-2-8.md)
9. [SKIP-3-2-9](lookup/SKIP/SKIP-3/SKIP-3-2-9.md)
10. [SKIP-3-2-10](lookup/SKIP/SKIP-3/SKIP-3-2-10.md)
11. [SKIP-3-2-11](lookup/SKIP/SKIP-3/SKIP-3-2-11.md)
12. [SKIP-3-2-12](lookup/SKIP/SKIP-3/SKIP-3-2-12.md)
13. [SKIP-3-2-13](lookup/SKIP/SKIP-3/SKIP-3-2-13.md): ø
14. none
15. [SKIP-3-2-15](lookup/SKIP/SKIP-3/SKIP-3-2-15.md): ø
16. none
17. [SKIP-3-2-17](lookup/SKIP/SKIP-3/SKIP-3-2-17.md): 贋
18. none
19. none
20. none
21. none
22. [SKIP-3-2-22](lookup/SKIP/SKIP-3/SKIP-3-2-22.md): ø

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
      - date-last-perfect

```