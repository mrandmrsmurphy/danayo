---
date-last-perfect: 2026-09-24
tags: [lookup]

---
> [[SKIP]] : 4

These are <ruby>漢字<rt>ㄏㄚㄋㄐㄧ</rt></ruby> with a top line, organized by stroke count -- which is the **middle** number of SKIP-4. There are no 10's, 11's, 12's, or 15's.

| [[SKIP-4-1-1]] | [[SKIP-4-2-1]] | [[SKIP-4-3-1]] |
|---|---|---|
| 乙 | 丁 了 又 | 下 久 于 叉 及 口 已 弓 兀 夕 子 工 己 巳 干 |
| [[SKIP-4-4-1]] | [[SKIP-4-5-1]] | [[SKIP-4-6-1]] |
| 尺 尹 天 五 王 不 丹 互 弔 牙 丐 巴 歹 𡈼 丑 | 且 丙 冊 凸 凹 平 正 母 玉 瓦 甲 疋 皿 | 両 亙 再 卍 死 耳 艮 西 |
| [[SKIP-4-7-1]] | [[SKIP-4-8-1]] | [[SKIP-4-9-1]] |
| 里 酉 豕 更 巫 亜 | 雨 | 飛 |
| [[SKIP-4-13-1]] | [[SKIP-4-14-1]] | |
| 鼎 | 爾 | |



## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-0-1")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```
