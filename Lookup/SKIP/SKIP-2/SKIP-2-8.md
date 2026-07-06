---
date-last-perfect: 2026-07-05
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 2

Top component has 8 strokes. Dominant components: 雨, 婁, 隹.

1. none
2. [SKIP-2-8-2](lookup/SKIP/SKIP-2/SKIP-2-8-2.md): 隼 (char)
3. [SKIP-2-8-3](lookup/SKIP/SKIP-2/SKIP-2-8-3.md): 啓, 堂, 堕, 娶, 婁, 婆, 彗, 雪 (char)
4. [SKIP-2-8-4](lookup/SKIP/SKIP-2/SKIP-2-8-4.md): 悲, 惑, 斐, 智, 替, 渠, 焚, 焦, 然, 煮, 犂, 琴, 琵, 琶, 集, 雰, 雲
5. [SKIP-2-8-5](lookup/SKIP/SKIP-2/SKIP-2-8-5.md): 楚, 督, 季, 禁, 雷, 零, 瑟
6. [SKIP-2-8-6](lookup/SKIP/SKIP-2/SKIP-2-8-6.md): 聚, 肇, 裴, 製, 需
7. [SKIP-2-8-7](lookup/SKIP/SKIP-2/SKIP-2-8-7.md): 黎, 賛, 質, 震, 輩 (char), 霊, 慧 (char), 霅
8. [SKIP-2-8-8](lookup/SKIP/SKIP-2/SKIP-2-8-8.md): 錮, 霍, 霓
9. [SKIP-2-8-9](lookup/SKIP/SKIP-2/SKIP-2-8-9.md): 霜, 霞
10. [SKIP-2-8-10](lookup/SKIP/SKIP-2/SKIP-2-8-10.md): ø
11. [SKIP-2-8-11](lookup/SKIP/SKIP-2/SKIP-2-8-11.md): 霧, 霫, 麓
12. none
13. [SKIP-2-8-13](lookup/SKIP/SKIP-2/SKIP-2-8-13.md): 露
14. none
15. none
16. [SKIP-2-8-16](lookup/SKIP/SKIP-2/SKIP-2-8-16.md): 靄, 鑫

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-8")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```
