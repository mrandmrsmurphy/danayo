---
date-last-perfect: 2026-07-05
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 2

Top component has 9 strokes. Dominant components: 心, 臣, 大.

1. none
2. [SKIP-2-9-2](lookup/SKIP/SKIP-2/SKIP-2-9-2.md): 兜
3. [SKIP-2-9-3](lookup/SKIP/SKIP-2/SKIP-2-9-3.md): 喪, 堅, 堡, 奥, 幇
4. [SKIP-2-9-4](lookup/SKIP/SKIP-2/SKIP-2-9-4.md): 想, 惹, 愁, 愚, 感, 暋, 楽, 照, 聖, 腎
5. [SKIP-2-9-5](lookup/SKIP/SKIP-2/SKIP-2-9-5.md): 碧
6. [SKIP-2-9-6](lookup/SKIP/SKIP-2/SKIP-2-9-6.md): 緊
7. [SKIP-2-9-7](lookup/SKIP/SKIP-2/SKIP-2-9-7.md): 豎, 賢
8. none
9. none
10. none
11. none
12. [SKIP-2-9-12](lookup/SKIP/SKIP-2/SKIP-2-9-12.md): 蠢

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-9")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```
