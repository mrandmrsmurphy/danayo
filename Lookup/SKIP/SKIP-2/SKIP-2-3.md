---
date-last-perfect: 2026-07-05
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 2

Top component has 3 strokes. Dominant components: 艹, 宀, 山, 穴.

1. [SKIP-2-3-1](lookup/SKIP/SKIP-2/SKIP-2-3-1.md): 太
2. [SKIP-2-3-2](lookup/SKIP/SKIP-2/SKIP-2-3-2.md): 兄, 冬, 去, 只, 号, 穴, 艾
3. [SKIP-2-3-3](lookup/SKIP/SKIP-2/SKIP-2-3-3.md): 各, 吉, 名, 圭, 多, 妄, 字, 宅, 宇, 守, 安, 寺, 当, 尖, 尗, 糸, 羊, 至, 舌, 芋, 芝
4. [SKIP-2-3-4](lookup/SKIP/SKIP-2/SKIP-2-3-4.md): 呆, 呈, 吝, 呂, 壱, 声, 売, 宋, 完, 忌, 忍, 志, 忝, 条, 灸, 災, 牢, 究, 芡, 芥, 芦, 芬, 芭, 芮, 花, 芳, 芸, 芼, 赤, 走, 足, 邑, 宏
5. [SKIP-2-3-5](lookup/SKIP/SKIP-2/SKIP-2-3-5.md): 並, 奄, 奇, 奈, 孟, 宙, 宕, 宗, 官, 定, 宛, 宜, 宝, 実, 尚, 岸, 岩, 𡿺, 帚, 幸, 显, 盂, 空, 穹, 苔, 若, 苦, 苺, 茎, 䒦, 芽, 苑, 苗, 苛, 英, 苹, 茂, 茅, 茉
6. [SKIP-2-3-6](lookup/SKIP/SKIP-2/SKIP-2-3-6.md): 前, 単, 品, 奔, 姦, 客, 宣, 室, 彖, 炭, 窃, 美, 茶, 草, 茜, 茫, 茸, 荇, 荊, 荒, 荘, 莽
7. [SKIP-2-3-7](lookup/SKIP/SKIP-2/SKIP-2-3-7.md): 兼, 㒼, 員, 套, 容, 宮, 宰, 害, 宴, 宵, 家, 悖, 案, 益, 穿, 窄, 窆, 窈, 荷, 荻, 莉, 莱, 華, 袁, 豈, 貢, 韋
8. [SKIP-2-3-8](lookup/SKIP/SKIP-2/SKIP-2-3-8.md): 剪, 壷, 寄, 密, 宿, 寂, 寅, 寇, 崖, 崩, 崇, 崔, 崙, 巣, 窒, 窓, 窕, 羞, 菊, 菱, 菅, 菌, 菜, 菩, 菫, 萄, 萌, 萎, 菲
9. [SKIP-2-3-9](lookup/SKIP/SKIP-2/SKIP-2-3-9.md): 募, 善, 喜, 奢, 寐, 寒, 寓, 尋, 尊, 嵌, 嵐, 葉, 葛, 葺, 茨, 萩, 萬, 萱, 落, 葡, 董, 葬, 葱, 韮
10. [SKIP-2-3-10](lookup/SKIP/SKIP-2/SKIP-2-3-10.md): 喿, 塞, 墓, 寝, 寛, 寞, 嵩, 幕, 彙, 慈, 潮, 煎, 窟, 羨, 義, 莫, 蒸, 蓄, 蓮, 葦, 蒋, 蒐, 蒲, 蓋, 蓬
11. [SKIP-2-3-11](lookup/SKIP/SKIP-2/SKIP-2-3-11.md): 嘉, 奪, 察, 寡, 寧, 寨, 暮, 窩, 窪, 蔑, 䔥, 蓼, 蔓, 蔡, 蕉, 蜜, 鳶
12. [SKIP-2-3-12](lookup/SKIP/SKIP-2/SKIP-2-3-12.md): 審, 寮, 窯, 窮, 蔬, 蔵, 蔽, 蕃, 蕎, 蕩, 蕪, 賓, 養, 蕤
13. [SKIP-2-3-13](lookup/SKIP/SKIP-2/SKIP-2-3-13.md): 奮, 憲, 窺, 蒼, 薫, 薬, 蒙, 薄, 薇, 薔, 薛, 薦, 薨, 薪, 嬴
14. [SKIP-2-3-14](lookup/SKIP/SKIP-2/SKIP-2-3-14.md): 嶺, 蔔, 薩, 藁, 賽
15. [SKIP-2-3-15](lookup/SKIP/SKIP-2/SKIP-2-3-15.md): 竄, 繭, 藍, 薮, 藤, 藩, 藷
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
