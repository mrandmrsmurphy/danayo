---
size: 0
stroke_count: 30
date-last-perfect: 2026-04-05
---
> [[Stroke]]

## Redirects 
- 鸞 --> 鵉
- 䆐 --> 国
- 䶑 --> 啼
- 厵 --> 源

## Data check
```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "30" OR stroke_count = 30
SORT file.name ASC