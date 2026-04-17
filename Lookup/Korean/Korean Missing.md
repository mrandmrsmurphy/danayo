---
size: 99
---



## Datacheck
```dataview
TABLE 注音 AS "Sound", english AS "en", tags AS "tags"
FROM "characters"
WHERE hanmun_edu_level = "無"
SORT file.name ASC