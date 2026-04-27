---
date-last-perfect: 2026-03-13
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 2 :

1. no
2. [SKIP-2-14-2](lookup/SKIP/SKIP-2/SKIP-2-14-2.md): 興
3. [SKIP-2-14-3](lookup/SKIP/SKIP-2/SKIP-2-14-3.md): 嬰
4. [SKIP-2-14-4](lookup/SKIP/SKIP-2/SKIP-2-14-4.md): 懲
5. [SKIP-2-14-5](lookup/SKIP/SKIP-2/SKIP-2-14-5.md): 璽, 㽉

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-14")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```