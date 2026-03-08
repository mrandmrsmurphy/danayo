---
date-last-perfect: 2026-03-06
---
> [SKIP](lookup/SKIP/SKIP.md) : 3 :

## Characters
Every, single one is the sickness radical!
1. no
2. no
3. no
4. [[SKIP-3-5-4]]: 疫
5. [[lookup/SKIP/SKIP-3/SKIP-3-5-5]]: 疱, 疲, 疽, 疾, 病, 症
6. [[SKIP-3-5-6]]: 痕
7. [[SKIP-3-5-7]]: 痘, 痛, 痢, 痩
8. [[SKIP-3-5-8]]: 痰, 痴
9. [[SKIP-3-5-9]]: 瘋, 瘍
10. [[SKIP-3-5-10]]: 瘡
11. No
12. [[SKIP-3-5-12]]: 厳, 療, 癇, 癌
13. [[lookup/SKIP/SKIP-3/SKIP-3-5-13]]


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