---
date-last-perfect:
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 2

```dataviewjs
const pages = dv.pages()
  .where(p => p.skip_number === "2-4-7")
// or stricter: .where(p => p["your_property"] === "value")
// or for numbers/strings/etc: adjust comparison as needed

const titles = pages
  .map(p => p.file.name)
  .sort()                    // optional: alphabetical sort
  .join(", ");

dv.paragraph(titles || "No matching pages");
````

1. [SKIP-2-4-1](lookup/SKIP/SKIP-2/SKIP-2-4-1.md): 丕, 旦, 氐
2. [SKIP-2-4-2](lookup/SKIP/SKIP-2/SKIP-2-4-2.md): 先, 光, 共, 劣, 早
3. [SKIP-2-4-3](lookup/SKIP/SKIP-2/SKIP-2-4-3.md)
4. [SKIP-2-4-4](lookup/SKIP/SKIP-2/SKIP-2-4-4.md)
5. [SKIP-2-4-5](lookup/SKIP/SKIP-2/SKIP-2-4-5.md)
6. [SKIP-2-4-6](lookup/SKIP/SKIP-2/SKIP-2-4-6.md)
7. [SKIP-2-4-7](lookup/SKIP/SKIP-2/SKIP-2-4-7.md): 旋, 曼, 覓, 貨, 貫, 責, 雀, 黄
8. [SKIP-2-4-8](lookup/SKIP/SKIP-2/SKIP-2-4-8.md): 喬, 普, 景, 晶, 暑, 最, 森, 歯
9. [SKIP-2-4-9](lookup/SKIP/SKIP-2/SKIP-2-4-9.md): 愛, 暈, 歳, 爺, 盞, 舜, 誉
10. [SKIP-2-4-10](lookup/SKIP/SKIP-2/SKIP-2-4-10.md): ø
11. [SKIP-2-4-11](lookup/SKIP/SKIP-2/SKIP-2-4-11.md): 暴, 靠
12. [SKIP-2-4-12](lookup/SKIP/SKIP-2/SKIP-2-4-12.md): 曇, 燕
13. [SKIP-2-4-13](lookup/SKIP/SKIP-2/SKIP-2-4-13.md): 爵
14. missing
15. missing
16. missing
17. [SKIP-2-4-17](lookup/SKIP/SKIP-2/SKIP-2-4-17.md): ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-4")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```