> [[Stroke]]

- <ruby>[[肥]]<rt>ブイ</rt></ruby> - fertile
## Data check
```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "8" OR stroke_count = 8
SORT file.name ASC