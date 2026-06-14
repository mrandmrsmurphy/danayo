---
date-last-perfect: 2026-06-14
tags: [lookup]

---

> [SKIP](lookup/SKIP/SKIP.md) : 1

Left half has 10 strokes. Dominant components: 馬, 鳥, 龍, 角, 言.

- [SKIP-1-10-1](lookup/SKIP/SKIP-1/SKIP-1-10-1.md): none
- [SKIP-1-10-2](lookup/SKIP/SKIP-1/SKIP-1-10-2.md): 凱, 割, 創, 勤, 馭
- [SKIP-1-10-3](lookup/SKIP/SKIP-1/SKIP-1-10-3.md): 鄒, 馳, 馴
- [SKIP-1-10-4](lookup/SKIP/SKIP-1/SKIP-1-10-4.md): 歌, 穀, 馿, 駁, 駄, 駅, 駆
- [SKIP-1-10-5](lookup/SKIP/SKIP-1/SKIP-1-10-5.md): 駐, 駒, 駝
- [SKIP-1-10-6](lookup/SKIP/SKIP-1/SKIP-1-10-6.md): 骸, 駱, 融
- [SKIP-1-10-7](lookup/SKIP/SKIP-1/SKIP-1-10-7.md): ø
- [SKIP-1-10-8](lookup/SKIP/SKIP-1/SKIP-1-10-8.md): 雛, 難, 騎, 騒, 験
- [SKIP-1-10-9](lookup/SKIP/SKIP-1/SKIP-1-10-9.md): 願, 顚, 騙, 髄
- [SKIP-1-10-10](lookup/SKIP/SKIP-1/SKIP-1-10-10.md): 競
- [SKIP-1-10-11](lookup/SKIP/SKIP-1/SKIP-1-10-11.md): 鶴
- [SKIP-1-10-12](lookup/SKIP/SKIP-1/SKIP-1-10-12.md): ø
- [SKIP-1-10-13](lookup/SKIP/SKIP-1/SKIP-1-10-13.md): ø
- [SKIP-1-10-14](lookup/SKIP/SKIP-1/SKIP-1-10-14.md): 驟
- [SKIP-1-10-15](lookup/SKIP/SKIP-1/SKIP-1-10-15.md): none
- [SKIP-1-10-16](lookup/SKIP/SKIP-1/SKIP-1-10-16.md): ø
- [SKIP-1-10-17](lookup/SKIP/SKIP-1/SKIP-1-10-17.md): ø
- [SKIP-1-10-18](lookup/SKIP/SKIP-1/SKIP-1-10-18.md): ø
- [SKIP-1-10-19](lookup/SKIP/SKIP-1/SKIP-1-10-19.md): ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-10")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
    sort:
      - property: size
        direction: DESC

```
