> [[SKIP]] | [[SKIP-2|2]] | [[SKIP-2-1|1]]

Only
- <ruby>[[二]]<rt>늬</rt></ruby>

### Data double check
```dataview
TABLE 注音 AS "Sound", skip_number AS "SKIP", english AS "en"
FROM "characters"
WHERE skip_number = "2-1-1"
SORT file.name ASC
