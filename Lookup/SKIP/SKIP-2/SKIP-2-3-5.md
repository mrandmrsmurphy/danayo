---
stroke_count: 8
size: 39
date-last-perfect:
skip_number: 2-3-5
---
> [SKIP](lookup/SKIP/SKIP.md) : 2 : [[SKIP-2-3|3]]
> [[Stroke 08]]

## Data doublecheck
```dataview
TABLE 注音 AS "Sound", skip_number AS "SKIP", english AS "en"
FROM "characters"
WHERE skip_number = "2-3-5"
SORT file.name ASC