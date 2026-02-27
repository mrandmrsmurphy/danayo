---
stroke_count: 5
date-last-perfect:
---
> [[SKIP]] : 4
> [[Stroke 05]]

- [[SKIP-4-5-1]] - 正	凹	且	瓦	玉	甲 冊	皿	凸	疋	丙	平	母	册	旡
- [[SKIP-4-5-2]] - 白	由	丘	甘	丗 出	世	生
- [[SKIP-4-5-3]] - 禾	乎 申	半	本	末	未	朮
- [[SKIP-4-5-4]] - 央 史	失	弗	戊	丼	冉	戉

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-5")
    order:
      - file.name
	  - size
      - skip_number
      - stroke_count
```