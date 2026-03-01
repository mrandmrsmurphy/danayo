---
size: 21
stroke_count: 6
date-last-perfect:
skip_number: 2-3-3
---
> [[SKIP]] : 2 : [[SKIP-2-3|3]]
> [[Stroke 06]]

## Data double check
```dataview
TABLE 注音 AS "Sound", skip_number AS "SKIP", english AS "en"
FROM "characters"
WHERE skip_number = "2-3-3"
SORT file.name ASC