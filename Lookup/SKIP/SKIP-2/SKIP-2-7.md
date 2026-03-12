---
date-last-perfect:
---
> [SKIP](lookup/SKIP/SKIP.md) : 2

```dataviewjs
const pages = dv.pages()
  .where(p => p.skip_number === "2-7-4")
// or stricter: .where(p => p["your_property"] === "value")
// or for numbers/strings/etc: adjust comparison as needed

const titles = pages
  .map(p => p.file.name)
  .sort()                    // optional: alphabetical sort
  .join(", ");

dv.paragraph(titles || "No matching pages");
````

1. None
2. None
3. [SKIP-2-7-3](lookup/SKIP/SKIP-2/SKIP-2-7-3.md): 
4. [SKIP-2-7-4](lookup/SKIP/SKIP-2/SKIP-2-7-4.md): 
5. [SKIP-2-7-5](lookup/SKIP/SKIP-2/SKIP-2-7-5.md): 番, 盛, 禼, 貿
6. [SKIP-2-7-6](lookup/SKIP/SKIP-2/SKIP-2-7-6.md)
7. [SKIP-2-7-7](lookup/SKIP/SKIP-2/SKIP-2-7-7.md)
8. None
9. [SKIP-2-7-9](lookup/SKIP/SKIP-2/SKIP-2-7-9.md)
10. None
11. [SKIP-2-7-11](lookup/SKIP/SKIP-2/SKIP-2-7-11.md)

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-7")
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