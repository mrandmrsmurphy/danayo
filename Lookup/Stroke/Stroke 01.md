> [[Stroke]]

- [[一 (char)|一]]
- [[乙]]

### Data check
```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "1" OR stroke_count = 1
SORT file.name ASC