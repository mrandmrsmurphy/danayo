> [[Stroke]]

- <ruby>[[一 (char)|一]]<rt>읻</rt></ruby>
- <ruby>[[乙]]<rt>옫</rt></ruby>

These are all alias of other things:
- 丨
- 丶
- 丿
- 乀
- 乁
- 乚
- 乛
- 亅

### Data check
```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "1" OR stroke_count = 1
SORT file.name ASC