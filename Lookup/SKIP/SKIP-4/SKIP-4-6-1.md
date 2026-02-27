---
size: 8
skip_number: 4-6-1
stroke_count: 6
---
> [[SKIP]] : 4 : [[SKIP-4-6|6]] | [[SKIP-4-0-1]]

## Datacheck
```dataview
TABLE 注音 AS "Sound", skip_number AS "SKIP", english AS "en"
FROM "characters"
WHERE skip_number = "4-6-1"
SORT file.name ASC