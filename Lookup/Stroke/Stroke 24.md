> [[Stroke]]

- <ruby>[[熊]]<rt>웅</rt></ruby> - bear
- <ruby>[[靄]]<rt>애</rt></ruby> - cloudy
- 鱧 --> 豊
- <ruby>[[鷹 (char)]]<rt>잉</rt></ruby> - hawk
- <ruby>[[麟]]<rt>린</rt></ruby> - female unicorn

## Data check
```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "24" OR stroke_count = 24
SORT file.name ASC