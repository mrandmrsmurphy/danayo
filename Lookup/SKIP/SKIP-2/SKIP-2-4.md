---
date-last-perfect: 2026-06-14
tags: [lookup]

---
> [SKIP](lookup/SKIP/SKIP.md) : 2

Top component has 4 strokes. Dominant components: 日, 火, 月, 言.

1. [SKIP-2-4-1](lookup/SKIP/SKIP-2/SKIP-2-4-1.md): 丕, 旦, 氐
2. [SKIP-2-4-2](lookup/SKIP/SKIP-2/SKIP-2-4-2.md): 先, 光, 共, 劣, 早
3. [SKIP-2-4-3](lookup/SKIP/SKIP-2/SKIP-2-4-3.md): 否, 吾, 告, 呑, 妥, 孚, 巠, 弄 …
4. [SKIP-2-4-4](lookup/SKIP/SKIP-2/SKIP-2-4-4.md): 受, 念, 忽, 斧, 昆, 旻, 昂, 昇 …
5. [SKIP-2-4-5](lookup/SKIP/SKIP-2/SKIP-2-4-5.md): 冒, 昜, 星, 是, 昴, 昷, 柔, 査 …
6. [SKIP-2-4-6](lookup/SKIP/SKIP-2/SKIP-2-4-6.md): 奚, 挙, 晃, 晏, 爹, 素, 索, 蚕 …
7. [SKIP-2-4-7](lookup/SKIP/SKIP-2/SKIP-2-4-7.md): 覓, 貨, 貫, 雀, 責, 曼, 旋, 黄
8. [SKIP-2-4-8](lookup/SKIP/SKIP-2/SKIP-2-4-8.md): 歯, 暑, 最, 普, 景, 晶, 森, 喬
9. [SKIP-2-4-9](lookup/SKIP/SKIP-2/SKIP-2-4-9.md): 愛, 暈, 歳, 爺, 盞, 舜, 誉
10. [SKIP-2-4-10](lookup/SKIP/SKIP-2/SKIP-2-4-10.md): ø
11. [SKIP-2-4-11](lookup/SKIP/SKIP-2/SKIP-2-4-11.md): 暴, 靠
12. [SKIP-2-4-12](lookup/SKIP/SKIP-2/SKIP-2-4-12.md): 曇, 燕
13. [SKIP-2-4-13](lookup/SKIP/SKIP-2/SKIP-2-4-13.md): 爵
14. none
15. none
16. none
17. [SKIP-2-4-17](lookup/SKIP/SKIP-2/SKIP-2-4-17.md): (aliases/redirects only)

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-4")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```
