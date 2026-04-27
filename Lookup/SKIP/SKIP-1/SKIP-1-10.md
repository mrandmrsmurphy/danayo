---
size:
tags: [lookup]

---

> [SKIP](../SKIP.md) : 1

```dataviewjs
const pages = dv.pages()
  .where(p => p.skip_number === "1-10-4")
// or stricter: .where(p => p["your_property"] === "value")
// or for numbers/strings/etc: adjust comparison as needed

const titles = pages
  .map(p => p.file.name)
  .sort()                    // optional: alphabetical sort
  .join(", ");

dv.paragraph(titles || "No matching pages");
````

1. No
2. [[SKIP-1-10-2]]: 凱, 割, 創, 勤, 馭
3. [[SKIP-1-10-3]]: 鄒, 馳, 馴
4. [[SKIP-1-10-4]]
5. [[SKIP-1-10-5]]
6. [[SKIP-1-10-6]]
7. [[SKIP-1-10-7]]
8. [[SKIP-1-10-8]]
9. [[SKIP-1-10-9]]
10. [[SKIP-1-10-10]]
11. [[SKIP-1-10-11]] 
12. [[SKIP-1-10-12]] 
13. [[SKIP-1-10-13]] 
14. [[SKIP-1-10-14]] 
15. No
16. [[SKIP-1-10-16]]
17. [[SKIP-1-10-17]]
18. [[SKIP-1-10-18]]
19. [[SKIP-1-10-19]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-10")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```