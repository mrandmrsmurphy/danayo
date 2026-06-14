---
date-last-perfect: 2026-06-14
size: 13
radical: 寸
tags: [lookup]

---
> [[Radicals]]
> The 寸 radical depicts a hand with a measuring point at the wrist, "inch."

## Strokes

### +0 Strokes
1. <ruby>[寸](../../characters/寸%20(char).md)<rt>ㄑㄛㄋ</rt></ruby> - inch, measurement

### +3 Strokes
2. <ruby>[寺](../../characters/寺.md)<rt>ㄙㄚ</rt></ruby> - temple (Buddhist)

### +4 Strokes
3. <ruby>[寿](../../characters/寿.md)<rt>ㄙ⼜</rt></ruby> - old age, long life
4. <ruby>[対](../../characters/対.md)<rt>ㄉㄛㄧ</rt></ruby> - oppose

### +6 Strokes
5. <ruby>[封](../../characters/封%20(char).md)<rt>ㄈㄛㄫ</rt></ruby> - seal
6. <ruby>[専](../../characters/専.md)<rt>ㄐ⼔ㄋ</rt></ruby> - special, dedicated

### +7 Strokes
7. <ruby>[尃](../../characters/尃.md)<rt>ㄈㄛ</rt></ruby> - scatter crops
8. <ruby>[射](../../characters/射.md)<rt>ㄙ⼘</rt></ruby> - shoot, eject
9. <ruby>[将](../../characters/将%20(char).md)<rt>ㄐ⺢ㄫ</rt></ruby> - will, shall

### +8 Strokes
10. <ruby>[尉](../../characters/尉%20(char).md)<rt>ㄨㄊ</rt></ruby> - officer

### +9 Strokes
11. <ruby>[尋](../../characters/尋%20(char).md)<rt>ㄙㄧㄇ</rt></ruby> - inquire for, seek
12. <ruby>[尊](../../characters/尊.md)<rt>ㄐㄛㄋ</rt></ruby> - revere, honored

### +12 Strokes
13. <ruby>[導](../../characters/導.md)<rt>ㄉㄚㄨ</rt></ruby> - guide, lead

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "寸"
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
WHERE radical = "寸"
SORT stroke_count ASC
```
