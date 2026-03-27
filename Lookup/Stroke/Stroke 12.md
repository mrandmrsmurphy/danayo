---
stroke_count: 12
date-last-perfect:
size: 344
---
> [Stroke](Stroke.md)

- <ruby>[[裂]]<rt>럭</rt></ruby>

```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "12" OR stroke_count = 12
SORT skip_number ASC