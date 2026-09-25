---
size: 0
stroke_count: 30
date-last-perfect: 2026-07-09
tags: [lookup]
---
> [[Stroke]]

## Characters
### In Use

### Aliases
- 鸞 --> 鵉
- 䆐 --> 国
- 䶑 --> 啼
- 厵 --> 源

## Data check
```dataview
TABLE file.link AS "Character", 注音 AS "Sound", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "30" OR stroke_count = 30
SORT skip_number ASC
```
