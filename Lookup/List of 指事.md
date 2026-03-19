1. <ruby>[一](/characters/一%20(char).md)<rt>ㄧㄊ</rt></ruby> - one
2. <ruby>[乂](/characters/乂.md)<rt>˙ㄚ˙</rt></ruby> - govern
3. <ruby>[二 (char)](/characters/二%20(char).md)<rt>ㄋㄧ˙</rt></ruby> - two
4. <ruby>[三 (char)](/characters/三%20(char).md)<rt>ㄙㄚㄇ</rt></ruby> - three
5. <ruby>[四 (char)](/characters/四%20(char).md)<rt>ㄙㄧ˙</rt></ruby> - four
6. 八
7. 半
8. 分
9. 刀
10. 刃
11. 十
12. 世
13. 百
14. 上
15. 下
16. 本
17. 末
18. 大
19. 天
20. 夫
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