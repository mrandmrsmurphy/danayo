---
date-last-perfect: 2026-03-06
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 3 :

```dataviewjs
const pages = dv.pages()
  .where(p => p.skip_number === "3-5-13")
// or stricter: .where(p => p["your_property"] === "value")
// or for numbers/strings/etc: adjust comparison as needed

const titles = pages
  .map(p => p.file.name)
  .sort()                    // optional: alphabetical sort
  .join(", ");

dv.paragraph(titles || "No matching pages");
````

## Characters
Every, single one is the sickness radical!
1. no
2. no
3. no
4. [[SKIP-3-5-4]]: 疫
5. [SKIP-3-5-5](SKIP-3-5-5.md): 疱, 疲, 疽, 疾, 病, 症
6. [[SKIP-3-5-6]]: 痕
7. [[SKIP-3-5-7]]: 痘, 痛, 痢, 痩
8. [[SKIP-3-5-8]]: 痰, 痴
9. [[SKIP-3-5-9]]: 瘋, 瘍
10. [[SKIP-3-5-10]]: 瘡
11. No
12. [[SKIP-3-5-12]]: 厳, 療, 癇, 癌
13. [SKIP-3-5-13](SKIP-3-5-13.md): 癒, 癖


## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-3"
        - file.hasLink("SKIP-3-5")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```