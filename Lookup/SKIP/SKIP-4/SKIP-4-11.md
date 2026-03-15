---
stroke_count: 11
date-last-perfect: 2026-03-06
---
> [SKIP](lookup/SKIP/SKIP.md) : 4
> [[Stroke 11]]

```dataviewjs
const pages = dv.pages()
  .where(p => p.graphemic_classification === "象形")
// or stricter: .where(p => p["your_property"] === "value")
// or for numbers/strings/etc: adjust comparison as needed

const titles = pages
  .map(p => p.file.name)
  .sort()                    // optional: alphabetical sort
  .join(", ");

dv.paragraph(titles || "No matching pages");
````

1. No
2. No
3. [SKIP-4-11-3](lookup/SKIP/SKIP-4/SKIP-4-11-3.md): 粛
4. [SKIP-4-11-4](lookup/SKIP/SKIP-4/SKIP-4-11-4.md): 戚, 爽

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-11")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```