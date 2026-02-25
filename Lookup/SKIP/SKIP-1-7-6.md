---
size: 32
stroke_count: 13
---
> [[SKIP]] : [[SKIP-1|1]] : [[SKIP-1-7|7]]
> These are all [[Stroke 13]]

### Data double check
```dataview
TABLE 注音 AS "Sound", skip_number AS "SKIP", english AS "en"
FROM "characters"
WHERE skip_number = "1-7-6"
SORT file.name ASC