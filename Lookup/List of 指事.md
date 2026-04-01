---
size: 56
---
# 指事 — Simple Indicatives
## Explained
### Definition
**指事** refers to characters that represent **abstract or relational concepts** by means of **symbolic marks or modifications**, rather than by pictorial depiction. Instead of drawing an object (as in 象形), these characters “point to” an idea through convention.

Typical examples include:
- 上 “above”
- 下 “below”
- 本 “root, base” (a mark at the base of 木)
- 末 “tip, end” (a mark at the top of 木)

In traditional accounts of the 六書, this is a small class used to encode concepts that cannot be easily drawn.

### Structural Characteristics
A character is best analyzed as 指事 when:
1. **The meaning is abstract, positional, or relational**  
    Not a concrete object, but something like direction, location, or logical distinction.
2. **The form uses marks, lines, or slight modifications**  
    These indicate or “point to” a feature rather than depict it.
3. **There is no phonetic component**  
    The graph does not include an element chosen for sound.
4. **The structure is minimal and non-compositional**  
    It is not a combination of independent semantic units.

### Contrast with Other Categories
**vs. 象形 (pictographs)**
- 指事 encodes an idea symbolically
- 象形 depicts a visible object

Example contrast:
- 上 (above) → 指事
- 山 (mountain) → 象形

**vs. 会意 (compound ideographs)**
- 指事 uses a single symbolic structure
- 会意 combines multiple meaningful elements

Example contrast:
- 本 (root: mark on 木) → 指事
- 林 (grove: 木 + 木) → 会意

Note: 本 may look composite, but the added stroke is not an independent semantic unit. It is an indicator.

**vs. 形声 (phono-semantic compounds)**
- 指事 has no phonetic element
- 形声 includes a phonetic component

Example contrast:
- 上 → 指事
- 正 (in many analyses: phonetic component + semantic development) → not 指事

### How to Classify a Character as 指事
Use the following decision process:
1. **Is the meaning abstract or relational (e.g., position, degree, logical distinction)?**
    - Yes → continue
    - No → consider 象形 or 会意
2. **Does the graph rely on a simple mark or modification rather than a full depiction?**
    - Yes → continue
    - No → consider 象形
3. **Can the character be decomposed into multiple meaningful parts?**
    - Yes → 会意 or 形声
    - No → continue
4. **Is there any phonetic component?**
    - Yes → 形声
    - No → 指事

Ambiguous cases often involve characters like 本 or 末. The key test is whether the added element is an independent semantic component (会意) or merely a positional indicator (指事).

### Notes for Dan’a’yo Classification
- 指事 remains a **small, tightly defined class**  
    It is primarily suited for:
    - spatial relations (上, 下)
    - intrinsic parts (本, 末)
    - simple conceptual distinctions
- We avoid expanding 指事 into general abstraction  
    Most abstract meanings in practice are better handled by:
    - 会意 (compositional meaning), or
    - lexical assignment to existing forms
- We remain cautious with “marked pictographs”  
    If a base form is modified by a stroke:
    - If the stroke _points to a feature_ → 指事
    - If it _adds a new semantic component_ → 会意

In a constructed system, 指事 is best treated as a **minimal symbolic layer**, used sparingly where pictorial representation is impossible and compositional structure would be excessive.

## 指事 by Stroke
### 1 and 2
1. <ruby>[一](/characters/一%20(char).md)<rt>ㄧㄊ</rt></ruby> - one
2. <ruby>[乂](/characters/乂.md)<rt>˙ㄚ˙</rt></ruby> - govern, originally "to cut with scissors"
3. <ruby>[二](/characters/二%20(char).md)<rt>ㄋㄧ˙</rt></ruby> - two
4. <ruby>[八](/characters/八%20(char).md)<rt>ㄅㄚㄊ</rt></ruby> - eight, originally "divide"
5. <ruby>[十](/characters/十.md)<rt>ㄙㄧㄆ</rt></ruby> - ten, originally just a vertical mark
### 3
6. <ruby>[三](/characters/三%20(char).md)<rt>ㄙㄚㄇ</rt></ruby> - three
7. <ruby>[上](/characters/上%20(char).md)<rt>ㄙ˙ㄚㄥ</rt></ruby> - up
8. <ruby>[下 (char)](/characters/下%20(char).md)<rt>ㄏㄚ</rt></ruby> - down
9. <ruby>[亡](/characters/亡.md)<rt>ㄇㄚㄥ</rt></ruby> die - "edge of a knife"
### 4
11. <ruby>[中](/characters/中%20(char).md)<rt>ㄐㄨㄥ</rt></ruby> center of a square
12. 乏
13. 予
14. 今 (char)
15. 介
16. 六 (char)
17. 厄
18. 尹
19. [[尺 (char)]] A man (人) with a mark (乙) on his leg to indicate 10 cun (寸) above the foot.
20. 幻
21. 欠
### 5
22. <ruby>[四](/characters/四%20(char).md)<rt>ㄙㄧ˙</rt></ruby> - four, originally "breathing"
23. 丘 (char)
24. 占
25. 古
26. 台 (char)
27. 央
28. 本 (char)
29. 末
30. 央
31. 弗
32. 旦
33. 石 (char)
34. 㐱
### 6
- 両 (char)
- 亙 (char)
- 亦 (char)
- 光 (char)
- 共 (char)
- 曲
- 虫
 - 行 (char)
### 7
- 図
- 坐 (char)
- 夹
- 見 (char)
- 言 (char)

### 8
- 典
- 学
- 斉



15. 半
16. 世
17. 百
18. [夫 (char)](characters/夫%20(char).md)
19. 元
20. 立
21. 位
22. 並
23. 普
24. 替
25. 望
26. 呈
27. 程
28. 聖
29. 廷
30. 庭
31. 氏
32. 底
33. 低
34. 邸
35. 弟
36. 第
37. 姉
### 9
40. [[昷]]
41. [[品 (char)]]
42. [[柬 (char)]]
43. [[音]]
44. [[具]]

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