---
date-last-perfect: 2026-07-05
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 2

Top component has 1 stroke. Dominant components: 一, 丶.

1. [SKIP-2-1-1](lookup/SKIP/SKIP-2/SKIP-2-1-1.md): 二
2. [SKIP-2-1-2](lookup/SKIP/SKIP-2/SKIP-2-1-2.md): 三
3. [SKIP-2-1-3](lookup/SKIP/SKIP-2/SKIP-2-1-3.md): 乏, 元, 戸
4. [SKIP-2-1-4](lookup/SKIP/SKIP-2/SKIP-2-1-4.md): 主, 永, 示
5. [SKIP-2-1-5](lookup/SKIP/SKIP-2/SKIP-2-1-5.md): 亘
6. [SKIP-2-1-6](lookup/SKIP/SKIP-2/SKIP-2-1-6.md): 戻, 系, 言, 豆
7. [SKIP-2-1-7](lookup/SKIP/SKIP-2/SKIP-2-1-7.md): 房, 肩
8. ø
9. [SKIP-2-1-9](lookup/SKIP/SKIP-2/SKIP-2-1-9.md): 扇
10. ø
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
