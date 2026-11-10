---
date-last-perfect: 2026-10-04
size: 12
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 2

Top component has 12 strokes. Dominant components: 道, 敬, 敝.

1. ø
2. ø
3. [SKIP-2-12-3](lookup/SKIP/SKIP-2/SKIP-2-12-3.md): 墜, 導, 幣, 弊
4. [SKIP-2-12-4](lookup/SKIP/SKIP-2/SKIP-2-12-4.md): 憩, 憑 (char)
5. [SKIP-2-12-5](lookup/SKIP/SKIP-2/SKIP-2-12-5.md): 瞥
6. [SKIP-2-12-6](lookup/SKIP/SKIP-2/SKIP-2-12-6.md): ø
7. [SKIP-2-12-7](lookup/SKIP/SKIP-2/SKIP-2-12-7.md): 攀, 警
8. [SKIP-2-12-8](lookup/SKIP/SKIP-2/SKIP-2-12-8.md): 礬
9. [SKIP-2-12-9](lookup/SKIP/SKIP-2/SKIP-2-12-9.md): ø
10. [SKIP-2-12-10](lookup/SKIP/SKIP-2/SKIP-2-12-10.md): ø
11. [SKIP-2-12-11](lookup/SKIP/SKIP-2/SKIP-2-12-11.md): ø
12. [SKIP-2-12-12](lookup/SKIP/SKIP-2/SKIP-2-12-12.md): ø
13. [SKIP-2-12-13](lookup/SKIP/SKIP-2/SKIP-2-12-13.md): 鼈
14. [SKIP-2-12-14](lookup/SKIP/SKIP-2/SKIP-2-12-14.md): 欝
15. [SKIP-2-12-15](lookup/SKIP/SKIP-2/SKIP-2-12-15.md): ø
16. [SKIP-2-12-16](lookup/SKIP/SKIP-2/SKIP-2-12-16.md): ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-12")
    order:
      - file.name
      - size
      - date-last-perfect
      - skip_number
      - stroke_count
```
