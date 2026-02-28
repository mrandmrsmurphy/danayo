---
stroke_count: 15
date-last-perfect:
---
> [[SKIP]] : 4
> [[Stroke 15]]

1. None
2. None
3. None
4. [[SKIP-4-15-4]]: 畿

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-15")
    order:
      - file.name
	  - size
      - skip_number
      - stroke_count
```