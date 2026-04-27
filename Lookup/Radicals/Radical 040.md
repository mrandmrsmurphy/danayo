---
size: 45
radical: 宀
tags: [lookup]

---
> [[Radicals]]

1. 宅
2. 宇
3. 守
4. 安
5. 宋
6. 完
7. 宕
8. 宗
9. 官
10. 宙 (char)
11. 定
12. 宛
13. 宜
14. 宝
15. 実
16. 客
17. 宣
18. 室
19. 宮
20. 宰
21. 害
22. 宴
23. 宵
24. 家
25. 容 (char)
26. 宿
27. 寂
28. 寄 (char)
29. 寅
30. 密 (char)
31. 寇
32. 富
33. 寐
34. 寒
35. <ruby>[寓](/characters/寓.md)<rt>ㄨ</rt></ruby>
36. 寛
37. 寝 (char)
38. <ruby>[寞](/characters/寞.md)<rt>ㄇㄚㄎ</rt></ruby>
39. 察
40. 寡
41. 寧
42. 寨
43. 審
44. 寮
45. 寵

## Notes
- [字 (char)](../../characters/字%20(char).md) is not officially listed here, but bares this radical

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - radical == "宀"
    order:
      - file.name
      - danayo_id
      - english
      - 注音
      - skip_number
      - stroke_count
    sort:
      - property: stroke_count
        direction: ASC
    columnSize:
      note.danayo_id: 64
      note.english: 236
      note.skip_number: 76
      note.stroke_count: 92

```