---
size: 2
stroke_count: 14
---
> [[SKIP]] : 2 : [[SKIP-2-7|7]]
> [[Stroke 14]]

## Datacheck
```dataview
TABLE 注音 AS "Sound", skip_number AS "SKIP", english AS "en"
FROM "characters"
WHERE skip_number = "2-7-7"
SORT file.name ASC