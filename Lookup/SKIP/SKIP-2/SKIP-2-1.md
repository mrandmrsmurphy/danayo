---
date-last-perfect: 2026-02-01
---
> [SKIP](lookup/SKIP/SKIP.md) : 2

```dataviewjs
const pages = dv.pages()
  .where(p => p.skip_number === "2-1-11")
// or stricter: .where(p => p["your_property"] === "value")
// or for numbers/strings/etc: adjust comparison as needed

const titles = pages
  .map(p => p.file.name)
  .sort()                    // optional: alphabetical sort
  .join(", ");

dv.paragraph(titles || "No matching pages");
````

1. [SKIP-2-1-1](lookup/SKIP/SKIP-2/SKIP-2-1-1.md): 二
2. [SKIP-2-1-2](lookup/SKIP/SKIP-2/SKIP-2-1-2.md): 三
3. [SKIP-2-1-3](lookup/SKIP/SKIP-2/SKIP-2-1-3.md): 乏, 元, 戸
4. [SKIP-2-1-4](lookup/SKIP/SKIP-2/SKIP-2-1-4.md): 主, 永, 示
5. [SKIP-2-1-5](lookup/SKIP/SKIP-2/SKIP-2-1-5.md): 亘
6. [SKIP-2-1-6](lookup/SKIP/SKIP-2/SKIP-2-1-6.md): 戻, 系, 言, 豆
7. [SKIP-2-1-7](lookup/SKIP/SKIP-2/SKIP-2-1-7.md): 房, 肩
8. No
9. [SKIP-2-1-9](lookup/SKIP/SKIP-2/SKIP-2-1-9.md): 扇
10. No
11. [SKIP-2-1-11](lookup/SKIP/SKIP-2/SKIP-2-1-11.md): 扉, 雇

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-1")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```