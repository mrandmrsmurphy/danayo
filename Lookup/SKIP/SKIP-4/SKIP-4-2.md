---
stroke_count: 2
date-last-perfect: 2026-09-24
tags: [lookup]

---
> [[SKIP]] : 4 

1. [[SKIP-4-2-1]]: 丁, 了, 又
2. [[SKIP-4-2-2]]: 七
3. [[SKIP-4-2-3]]: 十
4. [[SKIP-4-2-4]]: 九, 人, 入, 卜, 力, 乂


## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-2")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```