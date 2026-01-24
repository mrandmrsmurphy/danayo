> [[Stroke]]

## Gold
- <ruby>[[鑽]]<rt>잔</rt></ruby> - auger
- <ruby>[[鑼]]<rt>라</rt></ruby> - gong

## Fish
- <ruby>[[鱸]]<rt>로</rt></ruby> - bass

## Data check
```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "27" OR stroke_count = 27
SORT file.name ASC