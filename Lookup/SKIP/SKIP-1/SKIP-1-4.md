---
date-last-perfect: 2026-06-14
tags: [lookup]

---

> [SKIP](lookup/SKIP/SKIP.md) : 1

Left half has 4 strokes. Dominant components: 木, 火, 礻, 月.

- [SKIP-1-4-1](lookup/SKIP/SKIP-1/SKIP-1-4-1.md): 札, 礼
- [SKIP-1-4-2](lookup/SKIP/SKIP-1/SKIP-1-4-2.md): 刑, 列, 印, 朴, 朽, 此, 灯, 肋, 肌 …
- [SKIP-1-4-3](lookup/SKIP/SKIP-1/SKIP-1-4-3.md): 卵, 対, 形, 彤, 杆, 杉, 材, 村 …
- [SKIP-1-4-4](lookup/SKIP/SKIP-1/SKIP-1-4-4.md): 所, 放, 於, 旺, 明, 朋, 服, 杪 …
- [SKIP-1-4-5](lookup/SKIP/SKIP-1/SKIP-1-4-5.md): 俎, 施, 映, 昧, 昨, 昭, 枯, 柄 …
- [SKIP-1-4-6](lookup/SKIP/SKIP-1/SKIP-1-4-6.md): 旅, 時, 晒, 晦, 朕, 栓, 校, 株 …
- [SKIP-1-4-7](lookup/SKIP/SKIP-1/SKIP-1-4-7.md): 彬, 族, 晨, 桶, 梓, 梗, 梛, 梢 …
- [SKIP-1-4-8](lookup/SKIP/SKIP-1/SKIP-1-4-8.md): 勝, 斑, 晩, 晴, 暁, 期, 棋, 棍 …
- [SKIP-1-4-9](lookup/SKIP/SKIP-1/SKIP-1-4-9.md): 暇, 暖, 暗, 椰, 椿, 楊, 楓, 楔 …
- [SKIP-1-4-10](lookup/SKIP/SKIP-1/SKIP-1-4-10.md): 旗, 概, 槍, 様, 榴, 構, 槐, 槙 …
- [SKIP-1-4-11](lookup/SKIP/SKIP-1/SKIP-1-4-11.md): 槻, 槽, 標, 樟, 権, 横, 璃, 膣 …
- [SKIP-1-4-12](lookup/SKIP/SKIP-1/SKIP-1-4-12.md): 橋, 橘, 樹, 樽, 橄, 橙, 燃, 燐 …
- [SKIP-1-4-13](lookup/SKIP/SKIP-1/SKIP-1-4-13.md): 曖, 櫛, 檀, 燥, 燦, 燭, 牆, 犠 …
- [SKIP-1-4-14](lookup/SKIP/SKIP-1/SKIP-1-4-14.md): 曜, 檬, 檳, 檸, 櫂, 瓊
- [SKIP-1-4-15](lookup/SKIP/SKIP-1/SKIP-1-4-15.md): 爆, 臓
- [SKIP-1-4-16](lookup/SKIP/SKIP-1/SKIP-1-4-16.md): 朧, 騰
- [SKIP-1-4-17](lookup/SKIP/SKIP-1/SKIP-1-4-17.md): 欄, 爛
- [SKIP-1-4-18](lookup/SKIP/SKIP-1/SKIP-1-4-18.md): ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-4")
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
