---
size: 32
stroke_count: 13
date-last-perfect:
skip_number:
---
> [[SKIP]] : [[SKIP-1|1]] : [[SKIP-1-7|7]]
> These are all [[Stroke 13]]

## Characters

```dataview
LIST
FROM "characters"
WHERE skip_number = "1-7-6"
```
## Data doublecheck
```dataview
TABLE 注音 AS "Sound", skip_number AS "SKIP", english AS "en"
FROM "characters"
WHERE skip_number = "1-7-6"
SORT file.name ASC