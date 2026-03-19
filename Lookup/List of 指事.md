## 指事 by Stroke
### 1 and 2
1. <ruby>[一](/characters/一%20(char).md)<rt>ㄧㄊ</rt></ruby> - one
2. <ruby>[乂](/characters/乂.md)<rt>˙ㄚ˙</rt></ruby> - govern, originally "to cut with scissors"
3. <ruby>[二](/characters/二%20(char).md)<rt>ㄋㄧ˙</rt></ruby> - two
4. <ruby>[八](/characters/八%20(char).md)<rt>ㄅㄚㄊ</rt></ruby> - eight, originally 
   "divide"
5. <ruby>[十](/characters/十.md)<rt>ㄙㄧㄆ</rt></ruby> - ten
### 3
1. 刀
2. <ruby>[四](/characters/四%20(char).md)<rt>ㄙㄧ˙</rt></ruby> - four, originally "breathing"
3. <ruby>[三](/characters/三%20(char).md)<rt>ㄙㄚㄇ</rt></ruby> - three
4. 半
5. 分
6. 刃
7. 世
8. 百
9. 上
10. 下
11. 本
12. 末
13. 大
14. 天
15. 夫
16. 元
17. 立
18. 位
19. 並
20. 普
21. 替
22. 望
23. 呈
24. 程
25. 聖
26. 廷
27. 庭
28. 氏
29. 底
30. 低
31. 邸
32. 弟
33. 第
34. 姉

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