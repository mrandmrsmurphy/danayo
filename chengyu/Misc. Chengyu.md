---
date-last-perfect:
---

- <ruby>[一刀両断](chengyu/一刀両断.md)<rt>ㄧㄊㄊㄚˇㄌ˙ㄚㄥㄉˇㄚㄋ</rt></ruby> - cut in two with one stroke
- <ruby>[一刻千金](chengyu/一刻千金.md)<rt>ㄧㄊㄎㄨㄎㄑㄝㄋㄍㄧㄇ</rt></ruby> - time passed quickly
- <ruby>[一帆風順](chengyu/一帆風順.md)<rt>ㄧㄊㄆㄚㄇㄆㄨㄥㄙ˙ㄨㄋ</rt></ruby> - smooth sailing
- <ruby>[一攫千金](chengyu/一攫千金.md)<rt>ㄧㄊㄍˇㄚㄋㄑㄝㄋㄍㄧㄇ</rt></ruby> - make a fortune in an instant
- <ruby>[一日三秋](chengyu/一日三秋.md)<rt>ㄧㄊㄋㄞㄊㄙㄚㄇㄑㄨˇ</rt></ruby> - one day is like three autumns
- <ruby>[一朝一夕](chengyu/一朝一夕.md)<rt>ㄧㄊㄐㄚˇ·ㄧㄊㄙㄝㄎ</rt></ruby> - one morning one evening
- <ruby>[一期一会](chengyu/一期一会.md)<rt>ㄧㄜㄎㄧ·ㄧㄊㄏˇㄝ</rt></ruby>  - one lifetime, one meeting
- <ruby>[一目瞭然](chengyu/一目瞭然.md)<rt>ㄧㄊㄇㄨㄎㄌ˙ㄚˇㄋ˙ㄝㄋ</rt></ruby> - obvious
- <ruby>[八紘一宇](chengyu/八紘一宇.md)<rt>ㄅㄚㄊㄏˇㄝㄥ·ㄧㄊ·ㄨ</rt></ruby> - Manifest Destiny
- <ruby>[一石二鳥](chengyu/一石二鳥.md)<rt>ㄧㄊㄙㄝㄎㄋ˙ㄧㄑㄛˇ</rt></ruby> - two birds with one stone
- <ruby>[日月星辰](chengyu/日月星辰.md)<rt>ㄋㄧㄊ·ˇㄝㄊㄙㄝㄥㄙㄧㄋ</rt></ruby> - Sun, moon, stars, constellations
- <ruby>[一触即発](chengyu/一触即発.md)<rt>ㄧㄊㄑㄛㄎㄐㄧㄎㄆㄚㄊ</rt></ruby> - touch and go
- <ruby>[鶏鳴狗盗](chengyu/鶏鳴狗盗.md)<rt>ㄍㄝ˙ㄇ˙ㄝㄥㄍㄛˇㄉㄚˇ</rt></ruby> - bad people use dirty tricks
- <ruby>[金城湯池](chengyu/金城湯池.md)<rt>ㄍㄧㄇㄙㄧㄥㄊㄚㄥㄐㄨ˙</rt></ruby> - impregnable 
- <ruby>[魑魅罔両](chengyu/魑魅罔両.md)<rt>ㄑㄧㄇㄧ˙ㄇㄚㄥㄌ˙ㄚㄥ</rt></ruby> - all the demons
- <ruby>[乾坤一擲](chengyu/乾坤一擲.md)<rt>ㄍ˙ㄝㄋㄎㄛㄋ·ㄧㄊㄐㄝㄎ</rt></ruby> - all in


## Base check
```base
filters:
  and:
    - file.folder == "chengyu"
    - origin != "単亜語"
    - origin != "Bible"
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "chengyu"
        - origin != "単亜語"
        - origin != "Bible"
    order:
      - file.name
      - english
      - date-last-perfect
      - 注音
      - 羅馬字
      - 韓文
    sort:
      - property: date-last-perfect
        direction: ASC
      - property: size
        direction: ASC
    columnSize:
      file.name: 87
      note.date-last-perfect: 131
      note.注音: 81

```