---
stroke_count: 11
---
> [SKIP](lookup/SKIP/SKIP.md) : 4
> [[Stroke 11]]

```dataviewjs
const pages = dv.pages()
  .where(p => p.skip_number === "4-11-4")
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
3. [SKIP-4-11-3](SKIP-4-11-3): 粛
4. [[SKIP-4-11-4]]: 戚, 爽

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
```