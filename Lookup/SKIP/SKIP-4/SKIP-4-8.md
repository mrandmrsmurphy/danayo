---
stroke_count: 8
---
> [[SKIP]] : 4
> [[Stroke 08]]

1. [[SKIP-4-8-1]]: 雨
2. [[SKIP-4-8-2]]: 隹, 垂
3. [[SKIP-4-8-3]]: 乖, 事, 東, 秉
4. [[SKIP-4-8-4]]: 兎

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-8")
    order:
      - file.name
	  - size
      - skip_number
      - stroke_count
```