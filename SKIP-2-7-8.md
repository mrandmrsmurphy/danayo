---
size: 5
stroke_count: 15
---
> [[SKIP]] : 2 : [[SKIP-2-7|7]]
> [[Stroke 15]]

## Datacheck
```dataview
TABLE 注音 AS "Sound", skip_number AS "SKIP", english AS "en"
FROM "characters"
WHERE skip_number = "2-7-3"
SORT file.name ASC