---
aliases:
date-last-perfect: 2026-02-02
---
> [SKIP](../SKIP.md) : 3

```dataviewjs
const pages = dv.pages()
  .where(p => p.skip_number === "3-4-12")
// or stricter: .where(p => p["your_property"] === "value")
// or for numbers/strings/etc: adjust comparison as needed

const titles = pages
  .map(p => p.file.name)
  .sort()                    // optional: alphabetical sort
  .join(", ");

dv.paragraph(titles || "No matching pages");
````

1. No
2. [[SKIP-3-4-2]]
3. [[SKIP-3-4-3]]
4. [[SKIP-3-4-4]]
5. [[SKIP-3-4-5]]
6. [[SKIP-3-4-6]]
7. [[SKIP-3-4-7]]
8. [[SKIP-3-4-8]]
9. [[SKIP-3-4-9]]
10. [[SKIP-3-4-10]]
11. [[SKIP-3-4-11]]
12. [[SKIP-3-4-12]]
13. [[SKIP-3-4-13]]: 遽, 邁
14. [[SKIP-3-4-14]]: ø
15. [[SKIP-3-4-15]]: ø
16. none
17. none
18. none
19. [[SKIP-3-4-19]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-3"
        - file.hasLink("SKIP-3-4")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```