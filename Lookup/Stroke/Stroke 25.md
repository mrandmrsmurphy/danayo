---
size: 5
stroke_count: 25
date-last-perfect: 2026-02-23
tags: [lookup]

---
> [[Stroke]]

- <ruby>[[鼈]]<rt>ㄅㄝㄊ</rt></ruby> - turtle
- <ruby>[[鬣 (char)]]<rt>ㄌㄛㄆ</rt></ruby> - whiskers
- <ruby>[[皺]]<rt>ㄐㄨ</rt></ruby> - wrinkles
- <ruby>[[欖]]<rt>ㄌㄚㄇ</rt></ruby> - olive
- <ruby>[[攬]]<rt>ㄌㄚㄇ</rt></ruby> - monopolize

## Data check
```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "25" OR stroke_count = 25
SORT file.name ASC