> [[Stroke]]

- 嚼 --> 爵
- <ruby>[[欄]]<rt>란</rt></ruby> - railing
- <ruby>[[灋]]<rt>폽</rt></ruby> - sphinx
- 

## Data check
```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "21" OR stroke_count = 21
SORT file.name ASC