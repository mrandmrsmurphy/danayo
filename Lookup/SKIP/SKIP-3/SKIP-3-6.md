---
date-last-perfect: 2026-09-24
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 3

Surrounding component has 6 strokes. Dominant components: 戈, 虍.

1. ø
2. ø
3. [SKIP-3-6-3](lookup/SKIP/SKIP-3/SKIP-3-6-3.md): 咼, 哉, 彦
4. [SKIP-3-6-4](lookup/SKIP/SKIP-3/SKIP-3-6-4.md): 栽, 烏, 馬
5. [SKIP-3-6-5](lookup/SKIP/SKIP-3/SKIP-3-6-5.md): 産
6. [SKIP-3-6-6](lookup/SKIP/SKIP-3/SKIP-3-6-6.md): 裁
7. [SKIP-3-6-7](lookup/SKIP/SKIP-3/SKIP-3-6-7.md): 載
8. [SKIP-3-6-8](lookup/SKIP/SKIP-3/SKIP-3-6-8.md): 截
9. [SKIP-3-6-9](lookup/SKIP/SKIP-3/SKIP-3-6-9.md): 慮
10. ø
11. [SKIP-3-6-11](lookup/SKIP/SKIP-3/SKIP-3-6-11.md): 戴

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-3"
        - file.hasLink("SKIP-3-6")
    order:
      - file.name
      - size
      - date-last-perfect
      - skip_number
      - stroke_count
```
