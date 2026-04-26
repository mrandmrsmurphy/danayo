---
date-last-perfect:
tags:
  - chengyu
---

- <ruby>[一刀両断](chengyu/一刀両断.md)<rt>ㄧㄊㄊㄚㄨㄌ⼘ㄫㄉ⺢ㄋ</rt></ruby> - cut in two with one stroke
- <ruby>[一刻千金](chengyu/一刻千金.md)<rt>ㄧㄊㄎㄨㄎㄑㄝㄋㄍㄧㄇ</rt></ruby> - time passed quickly
- <ruby>[一帆風順](chengyu/一帆風順.md)<rt>ㄧㄊㄆㄚㄇㄆㄨㄫㄙ⼜ㄋ</rt></ruby> - smooth sailing
- <ruby>[一攫千金](chengyu/一攫千金.md)<rt>ㄧㄊㄍ⺢ㄋㄑㄝㄋㄍㄧㄇ</rt></ruby> - make a fortune in an instant
- <ruby>[一日三秋](chengyu/一日三秋.md)<rt>ㄧㄊㄋㄞㄊㄙㄚㄇㄑㄨㄛ</rt></ruby> - one day is like three autumns
- <ruby>[一朝一夕](chengyu/一朝一夕.md)<rt>ㄧㄊㄐㄚㄨ·ㄧㄊㄙㄝㄎ</rt></ruby> - one morning one evening
- <ruby>[一期一会](chengyu/一期一会.md)<rt>ㄧㄜㄎㄧ·ㄧㄊㄏ⼔</rt></ruby>  - one lifetime, one meeting
- <ruby>[一目瞭然](chengyu/一目瞭然.md)<rt>ㄧㄊㄇㄨㄎㄌ⼘ㄨㄋ⼶ㄋ</rt></ruby> - obvious
- <ruby>[八紘一宇](chengyu/八紘一宇.md)<rt>ㄅㄚㄊㄏ⼔ㄫ·ㄧㄊ·ㄨ</rt></ruby> - Manifest Destiny
- <ruby>[一石二鳥](chengyu/一石二鳥.md)<rt>ㄧㄊㄙㄝㄎㄋㄧㄑㄛㄨ</rt></ruby> - two birds with one stone
- <ruby>[日月星辰](chengyu/日月星辰.md)<rt>ㄋㄧㄊ·⼔ㄊㄙㄝㄫㄙㄧㄋ</rt></ruby> - Sun, moon, stars, constellations
- <ruby>[一触即発](chengyu/一触即発.md)<rt>ㄧㄊㄑㄛㄎㄐㄧㄎㄆㄚㄊ</rt></ruby> - touch and go
- <ruby>[鶏鳴狗盗](chengyu/鶏鳴狗盗.md)<rt>ㄍㄝㄧㄇ⼶ㄫㄍㄛㄨㄉㄚㄨ</rt></ruby> - bad people use dirty tricks
- <ruby>[金城湯池](chengyu/金城湯池.md)<rt>ㄍㄧㄇㄙㄧㄫㄊㄚㄫㄐㄨㄧ</rt></ruby> - impregnable 
- <ruby>[魑魅罔両](chengyu/魑魅罔両.md)<rt>ㄑㄧㄇㄧㄜㄇㄚㄫㄌ⼘ㄫ</rt></ruby> - all the demons
- <ruby>[乾坤一擲](chengyu/乾坤一擲.md)<rt>ㄍ⼶ㄋㄎㄛㄋ·ㄧㄊㄐㄝㄎ</rt></ruby> - all in
- <ruby>[茫然自失](chengyu/茫然自失.md)<rt>ㄇㄚㄫㄋ⼶ㄋㄐㄧㄜㄙㄧㄊ</rt></ruby> - dazed and confused
- <ruby>[孤軍奮闘](chengyu/孤軍奮闘.md)<rt>ㄍㄛㄍㄨㄋㄅㄨㄋㄉㄛㄨ</rt></ruby> - to fight on alone
- <ruby>[風声鶴唳](chengyu/風声鶴唳.md)<rt>ㄆㄨㄫㄙㄧㄫㄏㄚㄎㄌ·ㄝ</rt></ruby> - panic attack
- <ruby>[空中楼閣](chengyu/空中楼閣.md)<rt>ㄎㄛㄫㄐㄨㄫㄌㄛㄨㄍㄚㄎ</rt></ruby> - castle in the sky
- <ruby>[重文軽武](chengyu/重文軽武.md)<rt>ㄑㄛㄫㄇㄨㄋㄎㄧㄫㄇㄨ</rt></ruby> - weighty culture, light war
- <ruby>[金科玉律](chengyu/金科玉律.md)<rt>ㄍㄧㄇㄎ⺢ㄎ·⼜ㄎㄌㄨㄊ</rt></ruby> - golden rules and jade statutes
- <ruby>[人山人海](/chengyu/人山人海.md)<rt>ㄋㄧㄋㄙㄚㄋㄋㄧㄋㄏㄚㄧ</rt></ruby> - a sea of people
- <ruby>[貪官汚吏](/chengyu/貪官汚吏.md)<rt>ㄊㄚㄇㄍ⺢ㄋ·ㄛㄌㄧ</rt></ruby> - corrupt official


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
      - vietnamese
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