---
aliases:
---
> [[SKIP]] : 1

1. [[SKIP-1-3-1]]: 孔, 幻, 引
2. [[SKIP-1-3-2]]: 刊, 功, 北, 卯, 叩, 叫, 叭, 叱, 外, 夗, 奴, 巧, 幼, 弘, 打, 氾, 汀, 汁, 犯
3. [[SKIP-1-3-3]]: 兆 吐 (char) 吸 (char) 地 (char) 壮 好 (char) 如 (char) 妃 帆 (char) 弛 忙 扱 (char) 汎 (char) 汗 (char) 汚 (char) 汝 (char) 江 池 (char) 竹 (char) 羽 行 (char)
4. [[SKIP-1-3-4]]
5. [[SKIP-1-3-5]]
6. [[SKIP-1-3-6]]
7. [[SKIP-1-3-7]]
8. [[SKIP-1-3-8]]
9. [[SKIP-1-3-9]]
10. [[SKIP-1-3-10]]
11. [[SKIP-1-3-11]]
12. [[SKIP-1-3-12]]
13. [[SKIP-1-3-13]]
14. [[SKIP-1-3-14]]
15. [[SKIP-1-3-15]]
16. [[SKIP-1-3-16]]
17. [[SKIP-1-3-17]]
18. [[SKIP-1-3-18]]
19. [[SKIP-1-3-19]]
20. no
21. [[SKIP-1-3-21]]

```dataview
LIST
FROM "characters"
WHERE skip_number = "1-3-3"
```

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-3")
    order:
      - file.name
	  - size
      - skip_number
      - stroke_count
```