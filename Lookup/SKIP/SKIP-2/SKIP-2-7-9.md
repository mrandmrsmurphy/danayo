---
size: 1
stroke_count: 16
skip_number: 2-7-9
---
> [[SKIP]] : 2 : [[SKIP-2-7|7]]
> [[Stroke 16]]
## Characters
1. [[餐 (char)]]

## Datacheck
```dataview
TABLE 注音 AS "Sound", skip_number AS "SKIP", english AS "en"
FROM "characters"
WHERE skip_number = "2-7-9"
SORT file.name ASC