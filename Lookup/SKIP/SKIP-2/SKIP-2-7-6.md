---
size: 1
stroke_count: 13
---
> [[SKIP]] : 2 : [[SKIP-2-7|7]]
> [[Stroke 13]]
## Characters
1. [[資]]
## Datacheck
```dataview
TABLE 注音 AS "Sound", skip_number AS "SKIP", english AS "en"
FROM "characters"
WHERE skip_number = "2-7-6"
SORT file.name ASC