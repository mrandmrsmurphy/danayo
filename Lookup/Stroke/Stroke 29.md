---
stroke_count: 29
date-last-perfect: 2026-02-23
size: 1
---
> [[Stroke]]

- <ruby>[[鸛]]<rt>ㄍㆼㄋ</rt></ruby> - stork

That's it!

## Data check
```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "29" OR stroke_count = 29
SORT file.name ASC