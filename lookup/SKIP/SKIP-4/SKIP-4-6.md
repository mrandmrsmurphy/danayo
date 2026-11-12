---
stroke_count: 6
date-last-perfect: 2026-11-12
size: 22
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 4
> [Stroke 06](lookup/Stroke/Stroke%2006.md)

These are the 漢字 of 6 strokes in total, by subtype (1 top line, 2 bottom line, 3 vertical line, 4 none of these).

1. [SKIP-4-6-1](lookup/SKIP/SKIP-4/SKIP-4-6-1.md): 両, 亙, 再, 卍, 死, 耳, 艮, 西
2. [SKIP-4-6-2](lookup/SKIP/SKIP-4/SKIP-4-6-2.md): 曲, 自, 臼, 血
3. [SKIP-4-6-3](lookup/SKIP/SKIP-4/SKIP-4-6-3.md): 朱, 米, 虫
4. [SKIP-4-6-4](lookup/SKIP/SKIP-4/SKIP-4-6-4.md): 吏, 夷, 戌, 戍, 成, 曳, 舟

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
      - date-last-perfect

```