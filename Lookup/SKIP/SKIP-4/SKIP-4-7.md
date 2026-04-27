---
stroke_count: 7
tags: [lookup]

---
> [[SKIP]] : 4
> [[Stroke 07]]

1. [[SKIP-4-7-1]]: 亜, 巫, 更, 豕, 酉, 里
2. [[SKIP-4-7-2]]: 坐
3. [[SKIP-4-7-3]]: 串, 我, 束, 来, 求, 甫, 身, 車
4. [[SKIP-4-7-4]]: 夹, 寿, 良

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