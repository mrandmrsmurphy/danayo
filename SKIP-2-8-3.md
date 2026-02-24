---
stroke_count: 11
size: 9
---
### Data double check
```dataview
TABLE 注音 AS "Sound", skip_number AS "SKIP", english AS "en"
FROM "characters"
WHERE skip_number = "2-8-3"
SORT file.name ASC
