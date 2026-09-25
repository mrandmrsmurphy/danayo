---
date-last-perfect: 2026-09-24
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 3 :

Every single one is the sickness radical!
1. no
2. no
3. no
4. [SKIP-3-5-4](lookup/SKIP/SKIP-3/SKIP-3-5-4.md): 疫
5. [SKIP-3-5-5](lookup/SKIP/SKIP-3/SKIP-3-5-5.md): 疱, 疲, 疽, 疾, 病, 症
6. [SKIP-3-5-6](lookup/SKIP/SKIP-3/SKIP-3-5-6.md): 痕
7. [SKIP-3-5-7](lookup/SKIP/SKIP-3/SKIP-3-5-7.md): 痘, 痛, 痢, 痩
8. [SKIP-3-5-8](lookup/SKIP/SKIP-3/SKIP-3-5-8.md): 痰, 痴, 痺
9. [SKIP-3-5-9](lookup/SKIP/SKIP-3/SKIP-3-5-9.md): 瘋, 瘍
10. [SKIP-3-5-10](lookup/SKIP/SKIP-3/SKIP-3-5-10.md): 瘡
11. no
12. [SKIP-3-5-12](lookup/SKIP/SKIP-3/SKIP-3-5-12.md): 厳, 療, 癇, 癌
13. [SKIP-3-5-13](lookup/SKIP/SKIP-3/SKIP-3-5-13.md): 癒, 癖


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