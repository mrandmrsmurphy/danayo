---
date-last-perfect:
tags:
  - lookup
---
> [SKIP](lookup/SKIP/SKIP.md) : 2

Top component has 6 strokes. Dominant components: 竹, 貝, 羽, 見.

1. ø
2. [SKIP-2-6-2](lookup/SKIP/SKIP-2/SKIP-2-6-2.md): 些, 竺, 其, 典, 阜, 券
3. [SKIP-2-6-3](lookup/SKIP/SKIP-2/SKIP-2-6-3.md): 卑, 型, 変, 契, 姿, 専, 巻, 要…
4. [SKIP-2-6-4](lookup/SKIP/SKIP-2/SKIP-2-6-4.md): 恐, 恩, 恭, 息, 拳, 書, 笑, 骨, 鬼…
5. [SKIP-2-6-5](lookup/SKIP/SKIP-2/SKIP-2-6-5.md): 基, 盗, 票, 祭, 笛, 笠, 符, 第, 習…
6. [SKIP-2-6-6](lookup/SKIP/SKIP-2/SKIP-2-6-6.md): 筆, 等, 筋, 答, 策, 粟, 紫, 衆, 装…
7. [SKIP-2-6-7](lookup/SKIP/SKIP-2/SKIP-2-6-7.md): 資, 節, 鼠, 賃, 農, 豊
8. [SKIP-2-6-8](lookup/SKIP/SKIP-2/SKIP-2-6-8.md): 箋, 箏, 箕, 算, 管, 翟, 翠, 鼻…
9. [SKIP-2-6-9](lookup/SKIP/SKIP-2/SKIP-2-6-9.md): 器, 箭, 箸, 範, 篆, 篇, 葩
10. [SKIP-2-6-10](lookup/SKIP/SKIP-2/SKIP-2-6-10.md): 築, 篤
11. [SKIP-2-6-11](lookup/SKIP/SKIP-2/SKIP-2-6-11.md): 篠, 糞, 繊, 翼, 鵉
12. [SKIP-2-6-12](lookup/SKIP/SKIP-2/SKIP-2-6-12.md): 簞, 簡, 覆
13. [SKIP-2-6-13](lookup/SKIP/SKIP-2/SKIP-2-6-13.md): 簫, 簾, 簿, 蟹, 覇
14. [SKIP-2-6-14](lookup/SKIP/SKIP-2/SKIP-2-6-14.md): 籍, 纂
15. [SKIP-2-6-15](lookup/SKIP/SKIP-2/SKIP-2-6-15.md): 籃
16. [SKIP-2-6-16](lookup/SKIP/SKIP-2/SKIP-2-6-16.md): 籠
17. [SKIP-2-6-17](SKIP-2-6-17.md): ø
18. ø
19. [SKIP-2-6-19](SKIP-2-6-19.md): ø

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-2"
        - file.hasLink("SKIP-2-6")
    order:
      - file.name
      - size
      - skip_number
      - stroke_count
      - date-last-perfect
```
