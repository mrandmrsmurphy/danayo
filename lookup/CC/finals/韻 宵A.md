---
size: 45
middle_chinese_final: iᴇu
date-last-perfect: 2026-07-10
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Final 宵A** splits into ⼄ㄨ vs ㄛㄨ, loosely tracking affricate initials, plus smaller exceptions (see below)

## CJKV Evolution
宵A [iᴇu] splits 27-12 between **⼄ㄨ** and **ㄛㄨ**, matching the Vowels table's documented winner (`ou`). The split loosely tracks initial type — 9 of the 12 ㄛㄨ members are affricate-initial (t͡s/t͡ɕ/d͡ʑ: 椒, 詔, 蕉, 招, 照, 劭, 焦, 昭, 沼), while ⼄ㄨ is dominated by sibilant fricatives, nasals, liquids, and glides — but it isn't a clean rule: **擾** and **繞** share the identical palatal-nasal initial (ȵ) yet land on opposite sides, another instance of the recurring "same initial, arbitrary outcome" pattern.

Three labial-initial characters (標, 漂, 杪) drop the -ㄨ entirely, landing on bare **⼄**; 杪 dodges a 2-member ㄇ⼄ㄨ crowd (妙, 秒), while 標/漂 have no same-initial competitor to explain the shift. **小** and **鞘** (both s-initial) similarly land on bare **ㄛ**. **礁** dodges a 3-member ㄐㄛㄨ crowd (椒, 蕉, 焦, all t͡s-initial like 礁) via a vowel-shift, landing on **ㄚㄨ**.

## Characters
### In Use
- ⼄ㄨ: <ruby>[[姚]]<rt>⼄ㄨ</rt></ruby>, <ruby>[[紹]]<rt>ㄙ⼄ㄨ</rt></ruby>, <ruby>[[肖]]<rt>ㄙ⼄ㄨ</rt></ruby>, <ruby>[[哨]]<rt>ㄙ⼄ㄨ</rt></ruby>, <ruby>[[召]]<rt>ㄙ⼄ㄨ</rt></ruby>, <ruby>[[逍]]<rt>ㄙ⼄ㄨ</rt></ruby>, <ruby>[[妙 (char)|妙]]<rt>ㄇ⼄ㄨ</rt></ruby>, <ruby>[[硝]]<rt>ㄙ⼄ㄨ</rt></ruby>, <ruby>[[笑 (char)|笑]]<rt>ㄙ⼄ㄨ</rt></ruby>, <ruby>[[僚]]<rt>ㄌ⼄ㄨ</rt></ruby>, <ruby>[[秒 (char)|秒]]<rt>ㄇ⼄ㄨ</rt></ruby>, <ruby>[[要]]<rt>⼄ㄨ</rt></ruby>, <ruby>[[消 (char)|消]]<rt>ㄙ⼄ㄨ</rt></ruby>, <ruby>[[宵]]<rt>ㄙ⼄ㄨ</rt></ruby>, <ruby>[[揺 (char)|揺]]<rt>⼄ㄨ</rt></ruby>, <ruby>[[焼]]<rt>ㄙ⼄ㄨ</rt></ruby>, <ruby>[[擾]]<rt>ㄋ⼄ㄨ</rt></ruby>, <ruby>[[瓢]]<rt>ㄅ⼄ㄨ</rt></ruby>, <ruby>[[腰]]<rt>⼄ㄨ</rt></ruby>, <ruby>[[耀]]<rt>⼄ㄨ</rt></ruby>, <ruby>[[謡]]<rt>⼄ㄨ</rt></ruby>, <ruby>[[邵]]<rt>ㄙ⼄ㄨ</rt></ruby>, <ruby>[[窯 (char)|窯]]<rt>⼄ㄨ</rt></ruby>, <ruby>[[遥]]<rt>⼄ㄨ</rt></ruby>, <ruby>[[療]]<rt>ㄌ⼄ㄨ</rt></ruby>, <ruby>[[夭]]<rt>⼄ㄨ</rt></ruby>, <ruby>[[曜]]<rt>⼄ㄨ</rt></ruby>
- ㄛㄨ: <ruby>[[少 (char)|少]]<rt>ㄙㄛㄨ</rt></ruby>, <ruby>[[椒]]<rt>ㄐㄛㄨ</rt></ruby>, <ruby>[[詔]]<rt>ㄐㄛㄨ</rt></ruby>, <ruby>[[套 (char)|套]]<rt>ㄊㄛㄨ</rt></ruby>, <ruby>[[蕉]]<rt>ㄐㄛㄨ</rt></ruby>, <ruby>[[招]]<rt>ㄑㄛㄨ</rt></ruby>, <ruby>[[照 (char)|照]]<rt>ㄐㄛㄨ</rt></ruby>, <ruby>[[劭]]<rt>ㄙㄛㄨ</rt></ruby>, <ruby>[[焦 (char)|焦]]<rt>ㄐㄛㄨ</rt></ruby>, <ruby>[[繞 (char)|繞]]<rt>ㄋㄛㄨ</rt></ruby>, <ruby>[[昭 (char)|昭]]<rt>ㄐㄛㄨ</rt></ruby>, <ruby>[[沼]]<rt>ㄐㄛㄨ</rt></ruby>
- ⼄: <ruby>[[標]]<rt>ㄅ⼄</rt></ruby>, <ruby>[[漂 (char)|漂]]<rt>ㄆ⼄</rt></ruby>, <ruby>[[杪]]<rt>ㄇ⼄</rt></ruby>
- ㄛ: <ruby>[[小 (char)|小]]<rt>ㄙㄛ</rt></ruby>, <ruby>[[鞘]]<rt>ㄙㄛ</rt></ruby>
- ㄚㄨ: <ruby>[[礁]]<rt>ㄐㄚㄨ</rt></ruby>

## Datacheck
```base
version: 1
views:
  - type: table
    name: Final iᴇu
    filters:
      and:
        - file.inFolder("characters")
        - middle_chinese_final == "iᴇu"
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
