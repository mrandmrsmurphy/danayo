---
stroke_count: 4
tags: [lookup]

---
> [[SKIP]] : 4
> [[Stroke 04]]

1. [[SKIP-4-4-1]]: 不, 丐, 丹, 互, 五, 天, 尹, 尺, 巴, 弔, 歹, 牙, 王, 𡈼
2. [[SKIP-4-4-2]]: 壬, 廿
3. [[SKIP-4-4-3]]: 中, 井, 升, 屯, 手, 木, 毛, 牛
4. [[SKIP-4-4-4]]: 内, 夫, 夭, 少, 戈, 火, 片, 犬

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