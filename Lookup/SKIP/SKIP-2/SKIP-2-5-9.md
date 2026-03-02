---
size: 3
skip_number: 2-5-9
stroke_count: 14
---

> [[SKIP]] | [[SKIP-2|2]] | [[SKIP-2-5|5]]

- <ruby>[[嘗]]<rt>샹</rt></ruby> - taste
- <ruby>[[裳]]<rt>샹</rt></ruby> - clothes
- <ruby>[[罰]]<rt>벋</rt></ruby> - penalty
- [[尽|盡]] --> 尽


### Data double check
```dataview
TABLE 注音 AS "Sound", skip_number AS "SKIP", english AS "en"
FROM "characters"
WHERE skip_number = "2-5-9"
SORT file.name ASC