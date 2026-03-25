---
size: 56
---

## 指事 by Stroke
### 1 and 2
1. <ruby>[一](/characters/一%20(char).md)<rt>ㄧㄊ</rt></ruby> - one
2. <ruby>[乂](/characters/乂.md)<rt>˙ㄚ˙</rt></ruby> - govern, originally "to cut with scissors"
3. <ruby>[二](/characters/二%20(char).md)<rt>ㄋㄧ˙</rt></ruby> - two
4. <ruby>[八](/characters/八%20(char).md)<rt>ㄅㄚㄊ</rt></ruby> - eight, originally 
   "divide"
5. <ruby>[十](/characters/十.md)<rt>ㄙㄧㄆ</rt></ruby> - ten, originally just a vertical mark
### 3
6. <ruby>[三](/characters/三%20(char).md)<rt>ㄙㄚㄇ</rt></ruby> - three
7. <ruby>[上 (char)](/characters/上%20(char).md)<rt>ㄙ˙ㄚㄥ</rt></ruby>
8. <ruby>[下 (char)](/characters/下%20(char).md)<rt>ㄏㄚ</rt></ruby>
9. <ruby>[亡](/characters/亡.md)<rt>ㄇㄚㄥ</rt></ruby>
10. <ruby>[之 (char)](/characters/之%20(char).md)<rt>ㄊㄧ</rt></ruby>
11. <ruby>[与 (char)](/characters/与%20(char).md)<rt>˙ㄛ</rt></ruby>
### 4
13. <ruby>[中 (char)](/characters/中%20(char).md)<rt>ㄐㄨㄥ</rt></ruby>

| file name |           english            | stroke_count |
| --------- | ---------------------------- | ------------ |
|     乏     |        scarcity, lack        |      4       |
|     予     |          beforehand          |      4       |
| 今 (char)  |             now              |      4       |
|     介     |           mediator           |      4       |
| 六 (char)  |            six, 6            |      4       |
|     厄     |       burden, trouble        |      4       |
|     尹     |       govern, oversee        |      4       |
| 尺 (char)  |       foot (distance)        |      4       |
|     幻     |     dillusion, illusion      |      4       |
| 欠 (char)  |             yawn             |      4       |
| 丘 (char)  |             hill             |      5       |
|     占     |            occupy            |      5       |
|     古     |         ancient, old         |      5       |
| 台 (char)  | pedestal, platform, machines |      5       |
| 四 (char)  |           four, 4            |      5       |
|     央     |        center, middle        |      5       |
|     弗     |           fluorine           |      5       |
|     旦     |           daybreak           |      5       |
|     末     |           end, tip           |      5       |
| 本 (char)  |          foundation          |      5       |
| 石 (char)  |             rock             |      5       |
|     㐱     |    black hair, thick hair    |      5       |
| 両 (char)  |             both             |      6       |
| 亙 (char)  |       across, athwart        |      6       |
| 亦 (char)  |             too              |      6       |
| 光 (char)  |            light             |      6       |
| 共 (char)  |        with, together        |      6       |
|     曲     |          tune, bend          |      6       |
|     虫     |             bug              |      6       |
| 行 (char)  |        attend, go to         |      6       |
|     図     |           diagram            |      7       |
| 坐 (char)  |             sit              |      7       |
|     夹     |         clip, holder         |      7       |
| 見 (char)  |             see              |      7       |
| 言 (char)  |             say              |      7       |
|     典     |   dictionary, subject book   |      8       |
|     学     |            learn             |      8       |
|     斉     |         simultaneous         |      8       |
| 品 (char)  |        article, item         |      9       |
|     昷     |       feed a prisoner        |      9       |
| 柬 (char)  |      letter, invitation      |      9       |
|     音     |            sound             |      9       |
|     具     |       tool, impliment        |      12      |

### 5
14. <ruby>[四](/characters/四%20(char).md)<rt>ㄙㄧ˙</rt></ruby> - four, originally "breathing"
15. 半
16. 世
17. 百
18. 本
19. 末
20. [夫 (char)](characters/夫%20(char).md)
21. 元
22. 立
23. 位
24. 並
25. 普
26. 替
27. 望
28. 呈
29. 程
30. 聖
31. 廷
32. 庭
33. 氏
34. 底
35. 低
36. 邸
37. 弟
38. 第
39. 姉
### 9
40. [[昷]]

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "characters"
        - graphemic_classification == "指事"
    order:
      - file.name
      - english
      - stroke_count
      - date-last-perfect
      - danayo_id
    sort:
      - property: stroke_count
        direction: ASC
    columnSize:
      note.english: 147
      note.stroke_count: 81
      note.date-last-perfect: 121

```