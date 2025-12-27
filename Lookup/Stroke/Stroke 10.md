> [[Stroke]]

```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "10" OR stroke_count = 10
SORT file.name ASC