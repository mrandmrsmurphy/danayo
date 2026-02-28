---
stroke_count: 14
date-last-perfect: 2026-02-28
---
> [[SKIP]] : 4 : 
> [[Stroke 14]]

1. [[SKIP-4-14-1]]: 爾
2. None
3. none
4. none

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-14")
    order:
      - file.name
	  - size
      - skip_number
      - stroke_count
```