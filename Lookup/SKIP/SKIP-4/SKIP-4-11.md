---
stroke_count: 11
---
> [SKIP](lookup/SKIP/SKIP.md) : 4
> [[Stroke 11]]

1. ?
2. ?
3. ?
4. ?

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-11")
    order:
      - file.name
	  - size
      - skip_number
      - stroke_count
```