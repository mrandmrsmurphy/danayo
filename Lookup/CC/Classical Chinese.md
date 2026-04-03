
The written Chinese language used from the Zhou Dynasty (1045 B.C.) (especially the Spring and Autumn Period), through to the end of the Han Dynasty (220 A.D.). In Chinese, [[古文]] (“Ancient Writing”) or, formally, [[古典]][[漢語]] (“Classical Chinese”). The language of many classics of Chinese literature.

The language used after the fall of the Han Dynasty is Literary Chinese – [[文言]] (“literary writing”).

We list the most popular characters from across these time period, 1000 at a time
- [CC 0000](/lookup/CC/CC%200000.md)
- [CC 1000](/lookup/CC/CC%201000.md)
- [CC 2000](/lookup/CC/CC%202000.md)
- [CC 3000](CC%203000.md)

From the Late Medieval (~1200), there come the Rime Tables of sounds


```base
filters:
  and:
    - file.inFolder("lookup/CC/finals")
views:
  - type: table
    name: Table
    order:
      - file.name
      - size
      - middle_chinese_final
    sort:
      - property: size
        direction: ASC

```