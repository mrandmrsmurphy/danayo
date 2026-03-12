---
aliases:
---
## Strokes
[[永字八法]]
[[筆画]]
![forever](images/forever.svg)

1. "dot" or "point" - [点](words/点.md) or [[側]]
2. “horizontal” "left-to-right" - [[横]]画 = [[勒]]
3. “vertical-falling” ([[豎]]画) or perpendicular. Notice the initial dot.  [[弩]]=[[努]]'s come in two kinds
	1. [[懸]][[針]]豎 - hanging needle crossbow - The tip tapers off into a sharp point at the bottom (like the bottom of the character **中**).
	2. [[垂]][[露]]豎 - dropping dew crossbow - The bottom is rounded and blunt, looking like a heavy drop of dew clinging to a needle (like the vertical strokes in **門**).
4. “hook” ([[鉤]]). Some hooks go left, others down = [[趯]]
5. “flick” ([[提]]=[[挑]]) or up-cutting stroke = [[策]]
6. “concave” ([彎](characters/弯.md)) or curving path  = [[掠]]
7. “throw away” ([[撇]]) or left-descending stroke =[[啄]]
8. “press” ([[捺]]) or right-descending stroke

Writing must be in order:
- Top to bottom
- Left to right
- Horizontal then vertical
- Outside then inside
- Fill then close  
- Left descenders then right
- Middle, then left, then right
- Dots at the end

## Stroke Counts
**Stroke count/[[筆画数]]** is an ancient way of categorizing hanji, though not a very effective one.  We preserve it hear, though we prefer other methods, namely the SKIP technique.  Rather than delineating within each page by radical, this is the system we prefer.


1. [[Stroke 01]] (2 characters) ✅
2. [[Stroke 02]] (16 characters) ✅
3. [[Stroke 03]] (39 characters)
4. [[Stroke 04]] (88 characters)
5. [[Stroke 05]] (123 characters)
6. [[Stroke 06]] (143 characters)
7. [[Stroke 07]] (227 characters)
8. [[Stroke 08]] (267 characters)
9. [[Stroke 09]] (290 characters)
10. [[Stroke 10]] (315 characters)
11. [[Stroke 11]] (327 characters)
12. [[Stroke 12]] (352 characters)
13. [[Stroke 13]] (268 characters)
14. [[Stroke 14]] (190 characters)
15. [[Stroke 15]] (201 characters)
16. [[Stroke 16]] (141 characters)
17. [[Stroke 17]] (102 characters)
18. [[Stroke 18]] (75 characters)
19. [[Stroke 19]] (55 characters)
20. [[Stroke 20]] (23 characters)
21. [[Stroke 21]] (14 characters)
22. [[Stroke 22]] (11 characters)
23. [[Stroke 23]] (7 characters) ✅
24. [[Stroke 24]] (4 characters) ✅
25. [[Stroke 25]] (5 characters) ✅
26. [[Stroke 26]] (1 character) ✅
27. [[Stroke 27]] (2 characters) ✅
28. [[Stroke 28]] (1 character) ✅
29. [[Stroke 29]] (1 character) ✅

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/Stroke"
    order:
      - file.name
      - size
      - stroke_count
      - date-last-perfect
    sort:
      - property: file.name
        direction: ASC
      - property: size
        direction: DESC

```