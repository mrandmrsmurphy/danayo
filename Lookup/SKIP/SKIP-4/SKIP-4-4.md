---
aliases:
---
> [[SKIP]] : 4
> [[Stroke 04]]

1. [[SKIP-4-4-1|1]]
2. [[SKIP-4-4-2|2]]
3. [[SKIP-4-4-3|3]]
4. [[SKIP-4-4-4|4]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-4")
    order:
      - file.name
	  - size
      - skip_number
      - stroke_count
```