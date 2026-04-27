---
date-last-perfect: 
tags: [lookup]

---
> [[SKIP]] : 1
> Radicals : 糸 米 舟 耳 由虫

```dataviewjs
const pages = dv.pages()
  .where(p => p.skip_number === "1-6-2")
// or stricter: .where(p => p["your_property"] === "value")
// or for numbers/strings/etc: adjust comparison as needed

const titles = pages
  .map(p => p.file.name)
  .sort()                    // optional: alphabetical sort
  .join(", ");

dv.paragraph(titles || "No matching pages");
````

1. [SKIP-1-6-1](lookup/SKIP/SKIP-1/SKIP-1-6-1.md): 乱, 耴
2. [SKIP-1-6-2](lookup/SKIP/SKIP-1/SKIP-1-6-2.md)
3. [SKIP-1-6-3](lookup/SKIP/SKIP-1/SKIP-1-6-3.md)
4. [SKIP-1-6-4](lookup/SKIP/SKIP-1/SKIP-1-6-4.md)
5. [SKIP-1-6-5](lookup/SKIP/SKIP-1/SKIP-1-6-5.md)
6. [SKIP-1-6-6](lookup/SKIP/SKIP-1/SKIP-1-6-6.md)
7. [SKIP-1-6-7](lookup/SKIP/SKIP-1/SKIP-1-6-7.md)
8. [SKIP-1-6-8](lookup/SKIP/SKIP-1/SKIP-1-6-8.md)
9. [SKIP-1-6-9](lookup/SKIP/SKIP-1/SKIP-1-6-9.md)
10. [SKIP-1-6-10](lookup/SKIP/SKIP-1/SKIP-1-6-10.md)
11. [SKIP-1-6-11](lookup/SKIP/SKIP-1/SKIP-1-6-11.md)
12. [SKIP-1-6-12](lookup/SKIP/SKIP-1/SKIP-1-6-12.md)
13. [SKIP-1-6-13](lookup/SKIP/SKIP-1/SKIP-1-6-13.md)
14. [SKIP-1-6-14](lookup/SKIP/SKIP-1/SKIP-1-6-14.md)
15. [SKIP-1-6-15](lookup/SKIP/SKIP-1/SKIP-1-6-15.md)
16. [SKIP-1-6-16](lookup/SKIP/SKIP-1/SKIP-1-6-16.md)
17. [SKIP-1-6-17](lookup/SKIP/SKIP-1/SKIP-1-6-17.md)
18. no
19. no
20. no
21. no
22. [SKIP-1-6-22](lookup/SKIP/SKIP-1/SKIP-1-6-22.md)

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-6")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```