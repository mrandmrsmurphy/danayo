---
size: 4
stroke_count: 12
---
> [[SKIP]] : 2 : [[SKIP-2-7|7]]
> [[Stroke 12]]

## Datacheck
```dataview
TABLE 注音 AS "Sound", skip_number AS "SKIP", english AS "en"
FROM "characters"
WHERE skip_number = "2-7-5"
SORT file.name ASC