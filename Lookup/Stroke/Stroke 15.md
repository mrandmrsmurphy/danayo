> [[Stroke]]

```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "15" OR stroke_count = 15
SORT file.name ASC