---
date-last-perfect: 2026-07-05
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 2

Top component has 7 strokes. Dominant components: 辰, 里, 亜, 釆.

1. ø
2. ø
3. [SKIP-2-7-3](lookup/SKIP/SKIP-2/SKIP-2-7-3.md): 哲, 唇, 尃, 差, 辱
4. [SKIP-2-7-4](lookup/SKIP/SKIP-2/SKIP-2-7-4.md): 黒, 軣, 梨, 梁, 望, 曹, 悪, 患, 悠, 悉
5. [SKIP-2-7-5](lookup/SKIP/SKIP-2/SKIP-2-7-5.md): 番, 盛, 禼, 貿
6. [SKIP-2-7-6](lookup/SKIP/SKIP-2/SKIP-2-7-6.md): 資, 嗇
7. [SKIP-2-7-7](lookup/SKIP/SKIP-2/SKIP-2-7-7.md): 誓, 墨
8. ø
9. [SKIP-2-7-9](lookup/SKIP/SKIP-2/SKIP-2-7-9.md): 餐
10. ø
11. [SKIP-2-7-11](lookup/SKIP/SKIP-2/SKIP-2-7-11.md): 嚢

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-7")
    order:
      - file.name
      - size
      - date-last-perfect
      - skip_number
      - stroke_count
```
