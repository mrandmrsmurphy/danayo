---
size: 3
stroke_count: 2
skip_number: 4-2-1
---
> [[SKIP]] : 4 : [[SKIP-4-2|2]] | [[SKIP-4-0-1]]
> All are [[Stroke 02]].
## Characters
### Used
1. 丁
2. 了
3. 又
### Aliases
### Forbidden

## Datacheck
```dataview
TABLE 注音 AS "Sound", skip_number AS "SKIP", english AS "en"
FROM "characters"
WHERE skip_number = "4-2-1"
SORT file.name ASC