---
date-last-perfect: 2026-06-14
tags: [lookup]

---

> [SKIP](lookup/SKIP/SKIP.md) : 1

Left half has 6 strokes. Dominant components: 糸, 虫, 耳, 米, 舟.

- [SKIP-1-6-1](lookup/SKIP/SKIP-1/SKIP-1-6-1.md): 乱, 耴
- [SKIP-1-6-2](lookup/SKIP/SKIP-1/SKIP-1-6-2.md): 卦, 効, 刻, 刷, 取, 叔, 到, 刮 …
- [SKIP-1-6-3](lookup/SKIP/SKIP-1/SKIP-1-6-3.md): 姻, 封, 帥, 紀, 約, 紅, 缸, 耐 …
- [SKIP-1-6-4](lookup/SKIP/SKIP-1/SKIP-1-6-4.md): 恥, 敏, 料, 朔, 朗, 殺, 殷, 粉 …
- [SKIP-1-6-5](lookup/SKIP/SKIP-1/SKIP-1-6-5.md): 瓶, 粘, 粒, 粗, 細, 紺, 経, 紬 …
- [SKIP-1-6-6](lookup/SKIP/SKIP-1/SKIP-1-6-6.md): 刺, 制, 棘, 粧, 糾, 結, 絡, 絶 …
- [SKIP-1-6-7](lookup/SKIP/SKIP-1/SKIP-1-6-7.md): 継, 続, 絹, 綏, 蛾, 艇, 辞, 聘 …
- [SKIP-1-6-8](lookup/SKIP/SKIP-1/SKIP-1-6-8.md): 精, 維, 綱, 網, 綴, 綻, 綽, 綿 …
- [SKIP-1-6-9](lookup/SKIP/SKIP-1/SKIP-1-6-9.md): 箱, 糊, 線, 締, 編, 緩, 縁, 縄 …
- [SKIP-1-6-10](lookup/SKIP/SKIP-1/SKIP-1-6-10.md): 糖, 緯, 緻, 縛, 縞, 縦, 縫, 艙 …
- [SKIP-1-6-11](lookup/SKIP/SKIP-1/SKIP-1-6-11.md): 糟, 糠, 縮, 績, 繃, 繍, 聴, 螳 …
- [SKIP-1-6-12](lookup/SKIP/SKIP-1/SKIP-1-6-12.md): 糧, 織, 繕, 繞, 職
- [SKIP-1-6-13](lookup/SKIP/SKIP-1/SKIP-1-6-13.md): 繰, 蠖, 疆
- [SKIP-1-6-14](lookup/SKIP/SKIP-1/SKIP-1-6-14.md): 蠕, 耀
- [SKIP-1-6-15](lookup/SKIP/SKIP-1/SKIP-1-6-15.md): 纏, 艦
- [SKIP-1-6-16](lookup/SKIP/SKIP-1/SKIP-1-6-16.md): (aliases/redirects only)
- [SKIP-1-6-17](lookup/SKIP/SKIP-1/SKIP-1-6-17.md): (aliases/redirects only)
- SKIP-1-6-18: none
- SKIP-1-6-19: none
- SKIP-1-6-20: none
- SKIP-1-6-21: none
- [SKIP-1-6-22](lookup/SKIP/SKIP-1/SKIP-1-6-22.md): 纜

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-6")
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
