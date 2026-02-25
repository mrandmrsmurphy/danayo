---
size: 6
stroke_count: 13
date-last-perfect:
skip_number: 2-6-7
---
> [[SKIP]] | [[SKIP-2|2]] | [[SKIP-2-6|6]]

- [[資]]
- [[節]]
- [[鼡|鼠]] --> 鼡
- [[賃]]
- [[農]]
- [[豊]]
- [[筐|筺]] --> 筐
- [[賈]]
- [[碁]]
### Data double check
```dataview
TABLE 注音 AS "Sound", skip_number AS "SKIP", english AS "en"
FROM "characters"
WHERE skip_number = "2-6-7"
SORT file.name ASC