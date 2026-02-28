---
size: 1
stroke_count: 11
skip_number: 2-9-2
---
> [[SKIP]] : 2 : [[SKIP-2-9|9]]
> [[Stroke 11]]

## Characters
1. [[兜 (char)]]

## Datacheck
```dataview
TABLE 注音 AS "Sound", skip_number AS "SKIP", english AS "en"
FROM "characters"
WHERE skip_number = "2-9-2"
SORT file.name ASC