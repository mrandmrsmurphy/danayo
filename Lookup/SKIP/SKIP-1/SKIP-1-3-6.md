---
size: 58
stroke_count: 9
skip_number: 1-3-6
---
> [[SKIP]] : 1 : [[SKIP-1-3|3]]
> [[Stroke 09]]

## Characters

### Datacheck
```dataview
TABLE 注音 AS "Sound", english AS "en"
FROM "characters"
WHERE skip_number = "1-3-6"
SORT file.name ASC