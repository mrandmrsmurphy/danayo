## 指事 by Stroke
一, 乂, 二, 八, 十

(char), 丈 (char), 三 (char), 上 (char), 下 (char), 与 (char), 丘 (char), 両 (char), 中 (char), , 之 (char), 乏, 予,  (char), 亙 (char), 亡, 亦 (char), 介, 光 (char),  (char), 六 (char), 共 (char), 具, 典, 刃, 十, 占, 厄, 古, 台 (char), 品 (char), 四 (char), 図, 坐 (char), 央, 夹, 学, 寸 (char), 小 (char), 尹, 尺 (char), 幻, 弗, 斉, 旦, 昷, 曲, 末, 本 (char), 柬 (char), 欠 (char), 石 (char), 虫, 行 (char), 見 (char), 言 (char), 音, 㐱

### 1 and 2
1. <ruby>[一](/characters/一%20(char).md)<rt>ㄧㄊ</rt></ruby> - one
2. <ruby>[乂](/characters/乂.md)<rt>˙ㄚ˙</rt></ruby> - govern, originally "to cut with scissors"
3. <ruby>[二](/characters/二%20(char).md)<rt>ㄋㄧ˙</rt></ruby> - two
4. <ruby>[八](/characters/八%20(char).md)<rt>ㄅㄚㄊ</rt></ruby> - eight, originally 
   "divide"
5. <ruby>[十](/characters/十.md)<rt>ㄙㄧㄆ</rt></ruby> - ten, originally just a vertical mark
### 3
6. <ruby>[三](/characters/三%20(char).md)<rt>ㄙㄚㄇ</rt></ruby> - three
7. <ruby>[丈 (char)](/characters/丈%20(char).md)<rt>ㄑㄚㄥ</rt></ruby> - only
8. 上
9. 下
10. 亡
11. 之 (char)
12. 与 (char)
### 4
13. 中 (char)
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
      - graphemic_classification
      - english
      - stroke_count
      - date-last-perfect
    sort:
      - property: stroke_count
        direction: ASC
    columnSize:
      note.graphemic_classification: 84
      note.english: 147

```