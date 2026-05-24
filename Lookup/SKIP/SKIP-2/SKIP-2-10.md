---
date-last-perfect: 2026-05-24
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 2

Top component has 10 strokes. Dominant components: 髟, 能, 莫, 般.

1. ø
2. [SKIP-2-10-2](lookup/SKIP/SKIP-2/SKIP-2-10-2.md): 粤
3. [SKIP-2-10-3](lookup/SKIP/SKIP-2/SKIP-2-10-3.md): 奨, 塑, 塗
4. [SKIP-2-10-4](lookup/SKIP/SKIP-2/SKIP-2-10-4.md): 愨, 態, 慕, 敲, 熙...
5. [SKIP-2-10-5](lookup/SKIP/SKIP-2/SKIP-2-10-5.md): 監, 盤, 磐, 髯
6. [SKIP-2-10-6](lookup/SKIP/SKIP-2/SKIP-2-10-6.md): 繁
7. [SKIP-2-10-7](lookup/SKIP/SKIP-2/SKIP-2-10-7.md): 覧, 醤
8. [SKIP-2-10-8](lookup/SKIP/SKIP-2/SKIP-2-10-8.md): ø
9. ø
10. [SKIP-2-10-10](lookup/SKIP/SKIP-2/SKIP-2-10-10.md): ø
11. [SKIP-2-10-11](lookup/SKIP/SKIP-2/SKIP-2-10-11.md): 鶯, 鬘
12. [SKIP-2-10-12](lookup/SKIP/SKIP-2/SKIP-2-10-12.md): 鬚
13. [SKIP-2-10-13](lookup/SKIP/SKIP-2/SKIP-2-10-13.md): 驚
14. [SKIP-2-10-14](lookup/SKIP/SKIP-2/SKIP-2-10-14.md): 熊
15. [SKIP-2-10-15](lookup/SKIP/SKIP-2/SKIP-2-10-15.md): 鬣
16. [SKIP-2-10-16](lookup/SKIP/SKIP-2/SKIP-2-10-16.md): 蠶

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-10")
    order:
      - file.name
      - size
      - date-last-perfect
      - skip_number
      - stroke_count
```
