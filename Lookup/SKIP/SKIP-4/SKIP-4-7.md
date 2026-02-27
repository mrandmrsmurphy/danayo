---
stroke_count: 7
---
> [[SKIP]] : 4
> [[Stroke 07]]


```dataview
LIST
FROM "characters"
WHERE skip_number = "4-4-4"
```



## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-7")
    order:
      - file.name
	  - size
      - skip_number
      - stroke_count
```