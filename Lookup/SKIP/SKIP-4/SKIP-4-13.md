---
stroke_count: 13
tags: [lookup]

---
> [[SKIP]] : 4 
> [[Stroke 13]]

1. [[SKIP-4-13-1]]: 鼎
2. None
3. [[SKIP-4-13-3]]: alias only
4. None

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-13")
    order:
      - file.name
	  - size
      - skip_number
      - stroke_count
```