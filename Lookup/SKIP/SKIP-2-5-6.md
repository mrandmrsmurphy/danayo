---
size: 11
stroke_count: 11
date-last-perfect:
skip_number: 2-5-6
---
> [[SKIP]] : [[SKIP-2|2]] : [[SKIP-2-5|5]]


## Datacheck
```dataview
TABLE file.link AS "Character", skip_number AS "SKIP"
FROM "characters"
WHERE skip_number = "2-5-6"
SORT file.name ASC
