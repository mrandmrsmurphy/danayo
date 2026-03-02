---
date-last-perfect: 2026-02-01
---
> [[SKIP]] : 2

- [[SKIP-2-1-1]] (only 二)
- [[SKIP-2-1-2]] (only 三)
- [[SKIP-2-1-3]]
- [[SKIP-2-1-4]]
- [[SKIP-2-1-5]]
- [[SKIP-2-1-6]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-1")
    order:
      - file.name
	  - size
      - skip_number
      - stroke_count
```