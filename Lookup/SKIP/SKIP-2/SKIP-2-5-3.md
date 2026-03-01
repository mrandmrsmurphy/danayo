---
size: 9
stroke_count: 8
skip_number: 2-5-3
---
> [[SKIP]] : 2 : [[SKIP-2-5|5]] 
> [[Stroke 08]]

## Characters
1. [[長]] - long

### Data doublecheck
```dataview
TABLE 注音 AS "Sound", skip_number AS "SKIP", english AS "en"
FROM "characters"
WHERE skip_number = "2-5-3"
SORT file.name ASC