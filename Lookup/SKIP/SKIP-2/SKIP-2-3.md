---
date-last-perfect: 2026-05-24
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 2

Top component has 3 strokes. Dominant components: 艹, 宀, 山, 穴.

1. [SKIP-2-3-1](lookup/SKIP/SKIP-2/SKIP-2-3-1.md): 太
2. [SKIP-2-3-2](lookup/SKIP/SKIP-2/SKIP-2-3-2.md): 兄, 冬, 去, 只, 号, 穴, 艾
3. [SKIP-2-3-3](lookup/SKIP/SKIP-2/SKIP-2-3-3.md): 各, 吉, 名, 多, 安, 羊, 至, 舌…
4. [SKIP-2-3-4](lookup/SKIP/SKIP-2/SKIP-2-3-4.md): 呂, 声, 完, 忍, 志, 花, 赤, 走, 足…
5. [SKIP-2-3-5](lookup/SKIP/SKIP-2/SKIP-2-3-5.md): 奇, 宗, 官, 定, 空, 若, 苦, 英…
6. [SKIP-2-3-6](lookup/SKIP/SKIP-2/SKIP-2-3-6.md): 前, 単, 品, 客, 室, 美, 茶, 草, 荒…
7. [SKIP-2-3-7](lookup/SKIP/SKIP-2/SKIP-2-3-7.md): 兼, 員, 容, 宮, 害, 益, 穿, 華…
8. [SKIP-2-3-8](lookup/SKIP/SKIP-2/SKIP-2-3-8.md): 寄, 密, 宿, 崖, 崩, 窓, 羞, 菊, 菜…
9. [SKIP-2-3-9](lookup/SKIP/SKIP-2/SKIP-2-3-9.md): 善, 喜, 寒, 尋, 尊, 葉, 落, 萬, 葱…
10. [SKIP-2-3-10](lookup/SKIP/SKIP-2/SKIP-2-3-10.md): 塞, 墓, 寝, 義, 蒸, 蓄, 蓮, 蒲, 蓬…
11. [SKIP-2-3-11](lookup/SKIP/SKIP-2/SKIP-2-3-11.md): 嘉, 奪, 察, 寡, 寧, 蔑, 蔓, 蕉, 蜜…
12. [SKIP-2-3-12](lookup/SKIP/SKIP-2/SKIP-2-3-12.md): 審, 寮, 窮, 蔬, 蔵, 蕎, 蕩, 賓, 養
13. [SKIP-2-3-13](lookup/SKIP/SKIP-2/SKIP-2-3-13.md): 奮, 憲, 薫, 薬, 薄, 薔, 薦, 薪…
14. [SKIP-2-3-14](lookup/SKIP/SKIP-2/SKIP-2-3-14.md): 嶺, 蔔, 薩, 藁, 賽
15. [SKIP-2-3-15](lookup/SKIP/SKIP-2/SKIP-2-3-15.md): 竄, 繭, 藍, 藤, 藩, 藷
16. [SKIP-2-3-16](lookup/SKIP/SKIP-2/SKIP-2-3-16.md): 寵, 藻, 蘇, 蘭
17. [SKIP-2-3-17](SKIP-2-3-17.md): ø
18. [SKIP-2-3-18](SKIP-2-3-18.md): ø
19. [SKIP-2-3-19](lookup/SKIP/SKIP-2/SKIP-2-3-19.md): 蘿
20. [SKIP-2-3-20](SKIP-2-3-20.md): ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-3")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```
