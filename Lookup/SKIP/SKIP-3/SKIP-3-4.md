---
date-last-perfect: 2026-09-24
tags: [lookup]

---
> [SKIP](../SKIP.md) : 3

1. none
2. [SKIP-3-4-2](lookup/SKIP/SKIP-3/SKIP-3-4-2.md): 危, 戎, 気, 老, 考, 肉
3. [SKIP-3-4-3](lookup/SKIP/SKIP-3/SKIP-3-4-3.md): 君, 孝, 戒
4. [SKIP-3-4-4](lookup/SKIP/SKIP-3/SKIP-3-4-4.md): 或, 武, 者, 虎, 迎
5. [SKIP-3-4-5](lookup/SKIP/SKIP-3/SKIP-3-4-5.md): 扁, 眉, 看, 虐, 迥
6. [SKIP-3-4-6](lookup/SKIP/SKIP-3/SKIP-3-4-6.md): 翅, 迷
7. [SKIP-3-4-7](lookup/SKIP/SKIP-3/SKIP-3-4-7.md): 圄, 扈, 虚, 逍, 逑, 逗, 逞, 速, 逢
8. [SKIP-3-4-8](lookup/SKIP/SKIP-3/SKIP-3-4-8.md): 量
9. [SKIP-3-4-9](lookup/SKIP/SKIP-3/SKIP-3-4-9.md): 虜, 虞, 逾, 遊, 過, 遒
10. [SKIP-3-4-10](lookup/SKIP/SKIP-3/SKIP-3-4-10.md): ø
11. [SKIP-3-4-11](lookup/SKIP/SKIP-3/SKIP-3-4-11.md): 膚, 適
12. [SKIP-3-4-12](lookup/SKIP/SKIP-3/SKIP-3-4-12.md): 盧
13. [SKIP-3-4-13](lookup/SKIP/SKIP-3/SKIP-3-4-13.md): 遽, 邁
14. [SKIP-3-4-14](lookup/SKIP/SKIP-3/SKIP-3-4-14.md): ø
15. [SKIP-3-4-15](lookup/SKIP/SKIP-3/SKIP-3-4-15.md): ø
16. none
17. none
18. none
19. [SKIP-3-4-19](lookup/SKIP/SKIP-3/SKIP-3-4-19.md): 邏

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-3"
        - file.hasLink("SKIP-3-4")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```