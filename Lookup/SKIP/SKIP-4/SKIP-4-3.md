---
date-last-perfect: 2026-02-26
stroke_count: 3
tags: [lookup]

---
> [[SKIP]] : 4
> [[Stroke 03]]

These are all the <ruby>漢字<rt>ㄏㄚㄋㄐㄧ</rt></ruby> of 3 (three) strokes, whether that be a top line, bottom line, middle line, or otherwise.

1. [[SKIP-4-3-1]] = 尸, 夕,	于, 	兀, 	刄,	弓,  己, 	口, 	工, 	下, 	廴, 	叉, 	已, 子,	巳, 	孑,  夊, 	夂, 	囗, 	干, 	久, 	及
2. [[SKIP-4-3-2]] = 彑, 士,	土, 	也, 	上,  亡
3. [[SKIP-4-3-3]] = 巾,  才,  千,  屮,  廾
4. [[SKIP-4-3-4]] = 丸, 女, 丈, 大, 之,  与 , 宀,	幺, 广, 弋

## Base check
```base
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "lookup/SKIP/SKIP-4"
        - file.hasLink("SKIP-4-3")
    order:
      - file.name
	  - size
      - skip_number
      - stroke_count
```
