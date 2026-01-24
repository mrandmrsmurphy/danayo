> [[Stroke]]

- <ruby>[[鼈]]<rt>벋</rt></ruby> - turtle
- <ruby>[[鬣]]<rt>롭</rt></ruby> - whiskers
- <ruby>[[皺]]<rt>주</rt></ruby> - wrinkles
- <ruby>[[欖]]<rt>람</rt></ruby> - olive
- <ruby>[[攬]]<rt>람</rt></ruby> - monopolize

## Data check
```dataview
TABLE file.link AS "Character", stroke_count AS "Stroke", skip_number AS "SKIP"
FROM "characters"
WHERE stroke_count = "25" OR stroke_count = 25
SORT file.name ASC