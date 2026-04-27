---
date-last-perfect: 2026-03-06
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 3 
These are character with a surrounding element of ten-strokes, typically either the demon-radical or the door-radical.

Below are the number of strokes for the other material, that is, that which is surrounded:
1. Does not exist
2. Does not exist
3. Does not exist
4. [SKIP-3-10-4](lookup/SKIP/SKIP-3/SKIP-3-10-4.md): 魁
5. [SKIP-3-10-5](lookup/SKIP/SKIP-3/SKIP-3-10-5.md): ø
6. Does not exist
7. Does not exist
8. [SKIP-3-10-8](lookup/SKIP/SKIP-3/SKIP-3-10-8.md): ø
9. Does not exist
10. [SKIP-3-10-10](lookup/SKIP/SKIP-3/SKIP-3-10-10.md): ø
11. [SKIP-3-10-11](lookup/SKIP/SKIP-3/SKIP-3-10-11.md): 魑
12. Does not exist
13. Does not exist
14. Does not exist
15. Does not exist
16. [SKIP-3-10-16](lookup/SKIP/SKIP-3/SKIP-3-10-16.md): ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-3"
        - file.hasLink("SKIP-3-10")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```