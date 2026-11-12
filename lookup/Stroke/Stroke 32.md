---
size: 0
stroke_count: 32
date-last-perfect: 2026-11-11
tags: [lookup]
---
> [[Stroke]]

## Characters
### In Use

### Aliases

### Forbidden
- ¡籲! - 違法字

## Data check
```dataview
TABLE file.link AS "Character", 注音 AS "Sound", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "32" OR stroke_count = 32
SORT skip_number ASC
```
