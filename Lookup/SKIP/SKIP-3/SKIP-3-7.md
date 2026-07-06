---
date-last-perfect: 2026-07-05
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 3

Surrounding component has 7 strokes. Dominant component: 走.

1. ø
2. [SKIP-3-7-2](lookup/SKIP/SKIP-3/SKIP-3-7-2.md): 赴
3. [SKIP-3-7-3](lookup/SKIP/SKIP-3/SKIP-3-7-3.md): 島, 赳, 起
4. [SKIP-3-7-4](lookup/SKIP/SKIP-3/SKIP-3-7-4.md): 鳥
5. [SKIP-3-7-5](lookup/SKIP/SKIP-3/SKIP-3-7-5.md): 着, 超, 越
6. ø
7. [SKIP-3-7-7](lookup/SKIP/SKIP-3/SKIP-3-7-7.md): 趙
8. [SKIP-3-7-8](lookup/SKIP/SKIP-3/SKIP-3-7-8.md): 趣
9. [SKIP-3-7-9](lookup/SKIP/SKIP-3/SKIP-3-7-9.md): 麺

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-3"
        - file.hasLink("SKIP-3-7")
    order:
      - file.name
      - size
      - date-last-perfect
      - skip_number
      - stroke_count
```
