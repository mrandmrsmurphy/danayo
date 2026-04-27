---
stroke_count: 6
date-last-perfect: 2026-02-28
tags: [lookup]

---
> [[SKIP]] : 4
> [[Stroke 06]]

1. [[SKIP-4-6-1]]: 両, 亙, 再, 卍, 死, 耳, 艮, 西
2. [[SKIP-4-6-2]]: 曲, 自, 臼, 血
3. [[SKIP-4-6-3]]: 朱, 米, 虫
4. [[SKIP-4-6-4]]: 吏, 夷, 戌, 戍, 成, 曳, 舟

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-6")
    order:
      - file.name
	  - size
      - skip_number
      - stroke_count
```