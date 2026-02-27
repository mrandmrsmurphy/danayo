---
aliases:
date-last-perfect: 2026-02-06
---
> [[SKIP]] : 4 

1. [[SKIP-4-2-1]]: 厂, 又, 了, 冂, 冖, 几, 匚, 匸, 卩, 丁
2. [[SKIP-4-2-2]]: 七, 亠, 凵
3. [[SKIP-4-2-3]]: 十
4. [[SKIP-4-2-4]]: 九, 人, 入, 卜, 力, 乂, 勹, 厶


## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-2")
    order:
      - file.name
	  - size
      - skip_number
      - stroke_count
```