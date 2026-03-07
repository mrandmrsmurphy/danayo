---
date-last-perfect:
---
> [[SKIP]] : 1

```dataviewjs
const pages = dv.pages()
  .where(p => p.skip_number === "1-4-3")
// or stricter: .where(p => p["your_property"] === "value")
// or for numbers/strings/etc: adjust comparison as needed

const titles = pages
  .map(p => p.file.name)
  .sort()                    // optional: alphabetical sort
  .join(", ");

dv.paragraph(titles || "No matching pages");
````

1. [SKIP-1-4-1](lookup/SKIP/SKIP-1/SKIP-1-4-1.md): 札, 礼
2. [SKIP-1-4-2](lookup/SKIP/SKIP-1/SKIP-1-4-2.md): 刑, 列, 印, 朴, 朽, 此, 灯, 肋, 肌
3. [SKIP-1-4-3](lookup/SKIP/SKIP-1/SKIP-1-4-3.md)
4. [SKIP-1-4-4](lookup/SKIP/SKIP-1/SKIP-1-4-4.md)
5. [SKIP-1-4-9](lookup/SKIP/SKIP-1/SKIP-1-4-9.md)
6. [SKIP-1-4-6](lookup/SKIP/SKIP-1/SKIP-1-4-6.md)
7. [SKIP-1-4-7](lookup/SKIP/SKIP-1/SKIP-1-4-7.md)
8. [SKIP-1-4-8](lookup/SKIP/SKIP-1/SKIP-1-4-8.md)
9. [SKIP-1-4-9](lookup/SKIP/SKIP-1/SKIP-1-4-9.md)
10. [SKIP-1-4-10](lookup/SKIP/SKIP-1/SKIP-1-4-10.md)
11. [SKIP-1-4-11](lookup/SKIP/SKIP-1/SKIP-1-4-11.md)
12. [SKIP-1-4-12](lookup/SKIP/SKIP-1/SKIP-1-4-12.md)
13. [SKIP-1-4-13](lookup/SKIP/SKIP-1/SKIP-1-4-13.md)
14. [SKIP-1-4-14](lookup/SKIP/SKIP-1/SKIP-1-4-14.md)
15. [SKIP-1-4-15](lookup/SKIP/SKIP-1/SKIP-1-4-15.md)
16. [SKIP-1-4-16](lookup/SKIP/SKIP-1/SKIP-1-4-16.md)
17. [SKIP-1-4-17](lookup/SKIP/SKIP-1/SKIP-1-4-17.md)
18. [SKIP-1-4-18](lookup/SKIP/SKIP-1/SKIP-1-4-18.md)

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-4")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```