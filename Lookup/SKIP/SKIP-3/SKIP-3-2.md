---
date-last-perfect: 2026-09-24
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 3

1. [SKIP-3-2-1](lookup/SKIP/SKIP-3/SKIP-3-2-1.md): 万, 凡, 勺, 寸, 山
2. [SKIP-3-2-2](lookup/SKIP/SKIP-3/SKIP-3-2-2.md): 仄, 凶, 勻, 勾, 勿, 匹, 区, 厄, 友, 反, 斗, 斤, 月, 止, 氏
3. [SKIP-3-2-3](lookup/SKIP/SKIP-3/SKIP-3-2-3.md): 包, 厉, 句, 可, 右, 叵, 圧, 左, 布, 斥, 用, 石
4. [SKIP-3-2-4](lookup/SKIP/SKIP-3/SKIP-3-2-4.md): 匈, 匠, 匡, 同, 后, 在, 存, 旬, 旭, 有, 灰
5. [SKIP-3-2-5](lookup/SKIP/SKIP-3/SKIP-3-2-5.md): 医, 辰
6. [SKIP-3-2-6](lookup/SKIP/SKIP-3/SKIP-3-2-6.md): 函, 厓, 周, 岡, 画, 罔
7. [SKIP-3-2-7](lookup/SKIP/SKIP-3/SKIP-3-2-7.md): 厘, 厚, 幽, 盾, 風
8. [SKIP-3-2-8](lookup/SKIP/SKIP-3/SKIP-3-2-8.md): 匿, 原
9. [SKIP-3-2-9](lookup/SKIP/SKIP-3/SKIP-3-2-9.md): 凰, 厠
10. [SKIP-3-2-10](lookup/SKIP/SKIP-3/SKIP-3-2-10.md): 厥, 厨, 厩, 雁
11. [SKIP-3-2-11](lookup/SKIP/SKIP-3/SKIP-3-2-11.md): ø
12. [SKIP-3-2-12](lookup/SKIP/SKIP-3/SKIP-3-2-12.md): 歴, 鳳, 暦
13. [SKIP-3-2-13](lookup/SKIP/SKIP-3/SKIP-3-2-13.md): ø
14. none
15. [SKIP-3-2-15](lookup/SKIP/SKIP-3/SKIP-3-2-15.md): ø
16. none
17. [SKIP-3-2-17](lookup/SKIP/SKIP-3/SKIP-3-2-17.md): 贋
18. none
19. none
20. none
21. none
22. [SKIP-3-2-22](lookup/SKIP/SKIP-3/SKIP-3-2-22.md): ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-3"
        - file.hasLink("SKIP-3-2")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```