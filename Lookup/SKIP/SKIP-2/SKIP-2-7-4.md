---
size: 10
stroke_count: 11
---
> [[SKIP]] : 2 : [[SKIP-2-7|7]]
> [[Stroke 11]]

## Datacheck
```dataview
TABLE 注音 AS "Sound", skip_number AS "SKIP", english AS "en"
FROM "characters"
WHERE skip_number = "2-7-4"
SORT file.name ASC