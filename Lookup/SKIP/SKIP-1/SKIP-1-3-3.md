---
size: 20
stroke_count: 6
skip_number: 1-3-3
---
> [[SKIP]] : 1 : [[SKIP-1-3|3]]
> [[Stroke 06]]

## Characters

### Datacheck
```dataview
TABLE 注音 AS "Sound", english AS "en"
FROM "characters"
WHERE skip_number = "1-6-6"
SORT file.name ASC