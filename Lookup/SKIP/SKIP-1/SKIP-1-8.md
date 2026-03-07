---
date-last-perfect:
---
> [SKIP](lookup/SKIP/SKIP.md)

```dataviewjs
const pages = dv.pages()
  .where(p => p.skip_number === "1-8-2")
// or stricter: .where(p => p["your_property"] === "value")
// or for numbers/strings/etc: adjust comparison as needed

const titles = pages
  .map(p => p.file.name)
  .sort()                    // optional: alphabetical sort
  .join(", ");

dv.paragraph(titles || "No matching pages");
````

## Characters
1. no
2. [SKIP-1-8-2](lookup/SKIP/SKIP-1/SKIP-1-8-2.md)
3. [SKIP-1-8-3](lookup/SKIP/SKIP-1/SKIP-1-8-3.md)
4. [[SKIP-1-8-4]]
5. [[SKIP-1-8-5]]
6. [[SKIP-1-8-6]]
7. [[SKIP-1-8-7]]
8. [[SKIP-1-8-8]]
9. [[SKIP-1-8-9]]
10. [[SKIP-1-8-10]]
11. [[SKIP-1-8-11]]
12. [[SKIP-1-8-12]]

## Radicals
### 金
### ⾷


## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-8")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```