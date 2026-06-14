---
date-last-perfect: 2026-06-14
size: 6
radical: 夕
tags: [lookup]

---
> [[Radicals]]
> The evening radical 夕, depicting a crescent moon, 3 strokes.

## Strokes

### +0 Strokes
1. <ruby>[夕](../../characters/夕.md)<rt>ㄙㄝㄎ</rt></ruby> - sunset

### +2 Strokes
2. <ruby>[外](../../characters/外.md)<rt>⺢ㄧ</rt></ruby> - outside
3. <ruby>[夗](../../characters/夗.md)<rt>⼄ㄋ</rt></ruby> - to turn over when asleep

### +3 Strokes
4. <ruby>[多](../../characters/多%20(char).md)<rt>ㄉㄜ</rt></ruby> - many

### +5 Strokes
5. <ruby>[夜](../../characters/夜%20(char).md)<rt>⼘</rt></ruby> - night

### +10 Strokes
6. <ruby>[夢](../../characters/夢%20(char).md)<rt>ㄇㄨㄫ</rt></ruby> - dream

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "夕"
    order:
      - file.name
      - danayo_id
      - english
      - 注音
      - skip_number
      - stroke_count
    columnSize:
      note.danayo_id: 64
      note.english: 236
```

## Data check
```dataview
TABLE 注音 AS "Sound", english AS "EN"
FROM "characters"
WHERE radical = "夕"
SORT stroke_count ASC
```
