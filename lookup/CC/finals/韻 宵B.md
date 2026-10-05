---
size: 20
middle_chinese_final: ɣiᴇu
date-last-perfect: 2026-10-05
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 宵B** splits by initial type: ⼘ㄨ (default) vs ㄚㄨ (retroflex initials) (see below)

## CJKV Evolution
宵B [ɣiᴇu] lands 14 of 20 characters on **⼘ㄨ**, matching the y-glide quality of the Vowels table's documented winner (`yau`). The remaining 6 form a genuinely clean initial-conditioned group: every single one (趙, 潮, 肇, 超, 兆, 朝) has a retroflex MC initial (ɖ or ʈʰ), and no retroflex-initial character appears anywhere in the main ⼘ㄨ group — a real rule, not homophony overflow.

## Characters
### In Use
- ⼘ㄨ: <ruby>[[苗]]<rt>ㄇ⼘ㄨ</rt></ruby>, <ruby>[[廟]]<rt>ㄇ⼘ㄨ</rt></ruby>, <ruby>[[表]]<rt>ㄅ⼘ㄨ</rt></ruby>, <ruby>[[僑]]<rt>ㄍ⼘ㄨ</rt></ruby>, <ruby>[[喬]]<rt>ㄎ⼘ㄨ</rt></ruby>, <ruby>[[俵]]<rt>ㄅ⼘ㄨ</rt></ruby>, <ruby>[[票 (char)|票]]<rt>ㄆ⼘ㄨ</rt></ruby>, <ruby>[[嬌]]<rt>ㄍ⼘ㄨ</rt></ruby>, <ruby>[[橋 (char)|橋]]<rt>ㄍ⼘ㄨ</rt></ruby>, <ruby>[[矯]]<rt>ㄍ⼘ㄨ</rt></ruby>, <ruby>[[蕎]]<rt>ㄍ⼘ㄨ</rt></ruby>, <ruby>[[猫 (char)|猫]]<rt>ㄇ⼘ㄨ</rt></ruby>, <ruby>[[描]]<rt>ㄇ⼘ㄨ</rt></ruby>, <ruby>[[妖]]<rt>⼘ㄨ</rt></ruby>
- ㄚㄨ: <ruby>[[趙]]<rt>ㄐㄚㄨ</rt></ruby>, <ruby>[[潮]]<rt>ㄑㄚㄨ</rt></ruby>, <ruby>[[肇]]<rt>ㄐㄚㄨ</rt></ruby>, <ruby>[[超 (char)|超]]<rt>ㄊㄚㄨ</rt></ruby>, <ruby>[[兆]]<rt>ㄐㄚㄨ</rt></ruby>, <ruby>[[朝 (char)|朝]]<rt>ㄐㄚㄨ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final ɣiᴇu
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "ɣiᴇu"
    order:
      - file.name
      - mandarin
      - cantonese
      - korean
      - middle_chinese_initial
      - middle_chinese_final
      - 注音
    sort:
      - property: 羅馬字
        direction: ASC
      - property: middle_chinese_initial
        direction: ASC
      - property: characters
        direction: DESC
      - property: grade_level
        direction: ASC
    columns:
      - file
      - file.path
      - file.links.length
    columnSize:
      note.mandarin: 59
      note.cantonese: 71
      note.korean: 43
      note.middle_chinese_initial: 97

```
