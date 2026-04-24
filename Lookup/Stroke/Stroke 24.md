---
size: 4
stroke_count: 24
date-last-perfect: 2026-02-23
---
> [[Stroke]]

- <ruby>[[熊]]<rt>ㄨㄫ</rt></ruby> - bear
- <ruby>[[靄]]<rt>ㄚ˙</rt></ruby> - cloudy
- 鱧 --> 豊
- <ruby>[[鷹 (char)]]<rt>ㄧㄫ</rt></ruby> - hawk
- <ruby>[[麟]]<rt>ㄌㄧㄋ</rt></ruby> - female unicorn

## Data check
```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "24" OR stroke_count = 24
SORT file.name ASC