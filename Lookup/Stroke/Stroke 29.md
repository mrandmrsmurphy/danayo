> [[Stroke]]

- [[鸛]]

## Data check
```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "29" OR stroke_count = 29
SORT file.name ASC