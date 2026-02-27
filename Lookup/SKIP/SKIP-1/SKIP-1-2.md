---
aliases:
---
> [[SKIP]] : 1

1. no
2. [[SKIP-1-2-2]]: 什, 仁, 仇, 仍, 切, 刈, 化, 双, 収, 比
3. [[SKIP-1-2-3]]: 他, 仗, 付, 仙, 代, 以, 加, 氷
4. [[SKIP-1-2-4]]: 仮, 仰, 仲, 件, 任, 伊, 伍, 伎, 伏, 伐, 休, 伝, 佤, 州, 次
5. [[SKIP-1-2-5]]: 伯, 伴, 伶, 伸, 伺, 伽, 似, 佃, 但, 佇, 位, 低, 住, 佐, 佑, 体, 何, 作, 佛, 佞, 冴, 冶, 冷
6. [[SKIP-1-2-6|6]]
7. [[SKIP-1-2-7|7]]
8. [[SKIP-1-2-8|8]]
9. [[SKIP-1-2-9|9]]
10. [[SKIP-1-2-10|10]]
11. [[SKIP-1-2-11|11]]
12. [[SKIP-1-2-12|12]]
13. [[SKIP-1-2-13|13]]
14. [[SKIP-1-2-14|14]]
15. [[SKIP-1-2-15|15]]

```dataview
LIST
FROM "characters"
WHERE skip_number = "1-2-5"
```

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-1-2")
    order:
      - file.name
	  - size
      - skip_number
      - stroke_count
```