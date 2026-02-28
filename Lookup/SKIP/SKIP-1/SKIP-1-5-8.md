---
size: 19
stroke_count: 13
date-last-perfect:
skip_number: 1-5-8
---
> [[SKIP]] : 1 : [[SKIP-1-5|5]]
> [[Stroke 13]]

## Datacheck
```dataview
TABLE 注音 AS "Sound", english AS "en"
FROM "characters"
WHERE skip_number = "1-5-8"
SORT file.name ASC