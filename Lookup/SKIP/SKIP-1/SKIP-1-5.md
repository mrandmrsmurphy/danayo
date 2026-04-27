---
date-last-perfect: 2026-03-06
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 1

1. No
2. [SKIP-1-5-2](lookup/SKIP/SKIP-1/SKIP-1-5-2.md): 初, 判, 別, 利, 刪, 助, 劫, 劭, 励, 即, 却, 町, 私
3. [SKIP-1-5-3](lookup/SKIP/SKIP-1/SKIP-1-5-3.md): 和, 的, 知, 社, 祀, 突, 邱, 邵, 邸
4. [SKIP-1-5-4](lookup/SKIP/SKIP-1/SKIP-1-5-4.md): 叚, 叛, 政, 故, 段, 盼, 研, 砕, 祝, 秋, 科, 秒, 級, 胡, 袂
5. [SKIP-1-5-5](lookup/SKIP/SKIP-1/SKIP-1-5-5.md): 弱, 既, 玆, 畔, 眠, 矩, 砥, 砧, 砭, 砲, 破, 祚, 神, 秘, 租, 秩, 称, 站, 袖, 被
6. [SKIP-1-5-6](lookup/SKIP/SKIP-1/SKIP-1-5-6.md): 務, 甜, 略, 眺, 眼, 硅, 移, 袴
7. [SKIP-1-5-7](lookup/SKIP/SKIP-1/SKIP-1-5-7.md): 甥, 疎, 皓, 短, 硝, 硫, 硬, 硯, 祷, 程, 稍, 税, 竦, 裕, 補
8. [SKIP-1-5-8](lookup/SKIP/SKIP-1/SKIP-1-5-8.md): 睛, 睡, 睦, 矮, 碍, 碗, 祿, 禍, 稗, 稚, 稜, 蜂, 裸, 裾, 褐, 雅, 雉, 雌, 靖
9. [SKIP-1-5-9](lookup/SKIP/SKIP-1/SKIP-1-5-9.md): 暢, 碑, 碩, 磁, 種, 稲, 端, 複, 頗, 領, 颯, 𥈞
10. [SKIP-1-5-10](lookup/SKIP/SKIP-1/SKIP-1-5-10.md): 確, 碼, 磋, 稷, 稼, 稽, 稿, 穂
11. [SKIP-1-5-11](lookup/SKIP/SKIP-1/SKIP-1-5-11.md): 磚, 穆, 積, 穏, 鴔, 鴨
12. [SKIP-1-5-12](lookup/SKIP/SKIP-1/SKIP-1-5-12.md): 瞬, 瞭, 瞳, 矯, 磯, 礁, 襖
13. [SKIP-1-5-13](lookup/SKIP/SKIP-1/SKIP-1-5-13.md): 瞻, 瞼, 礎, 穫, 襟
14. [SKIP-1-5-14](lookup/SKIP/SKIP-1/SKIP-1-5-14.md): 襪
15. No
16. No
17. [SKIP-1-5-17](lookup/SKIP/SKIP-1/SKIP-1-5-17.md): 穣

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-1"
        - file.hasLink("SKIP-1-5")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect

```