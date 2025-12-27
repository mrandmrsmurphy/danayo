> [[Stroke]]

```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "13" OR stroke_count = 13
SORT file.name ASC