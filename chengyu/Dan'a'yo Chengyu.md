---
date-last-perfect: 2026-09-12
tags:
  - chengyu
---

- <ruby>[合漢再決](chengyu/合漢再決.md)<rt>ㄍㄛㄆㄏㄚㄋㄐㄚㄧㄎ⼔ㄊ</rt></ruby> - The Renew Sinosphere Chooses Unity
- <ruby>[一字一音](chengyu/一字一音.md)<rt>ㄧㄊㄐㄧ·ㄧㄊ·ㄨㄇ</rt></ruby> - one character, one sound
- <ruby>[覧昭和決](chengyu/覧昭和決.md)<rt>ㄌㄚㄇㄐㄛㄨㄏ⺢ㄎ⼔ㄊ</rt></ruby> - Shōwa decides the look
- <ruby>[朝鮮正音](chengyu/朝鮮正音.md)<rt>ㄐㄚㄨㄙ⼶ㄋㄐㄧㄫ·ㄨㄇ</rt></ruby> - Joseon standardizes the sound
- <ruby>[保頭断尾](chengyu/保頭断尾.md)<rt>ㄅㄚㄨㄊㄛㄨㄉ⺢ㄋㄇㄨㄧ</rt></ruby> - guard the core, prune the periphery
- <ruby>[文言継承](chengyu/文言継承.md)<rt>ㄇㄨㄋ·ㄝㄋㄍㄝㄧㄙㄨㄫ</rt></ruby> - continuity with the classical written standard
- <ruby>[現代適応](chengyu/現代適応.md)<rt>ㄏ⼶ㄋㄉㄚㄧㄙㄝㄎㄧㄫ</rt></ruby> - adaptation to modern speech
- <ruby>[日用必備](chengyu/日用必備.md)<rt>ㄋㄧㄊ⼄ㄫㄅㄧㄊㄅㄧㄜ</rt></ruby> - daily use, always needed
- <ruby>[修飾先行](chengyu/修飾先行.md)<rt>ㄙㄨㄛㄙㄧㄎㄙㄝㄋㄏㄚㄫ</rt></ruby> - modifiers precede
- <ruby>[先題後述](chengyu/先題後述.md)<rt>ㄙㄝㄋㄊㄝㄧㄏㄨㄛㄙㄨㄊ</rt></ruby> - Topic-Comment
- <ruby>[単語熟語](chengyu/単語熟語.md)<rt>ㄉㄚㄋ⼄ㄙㄨㄎ⼄</rt></ruby> - words and set phrases, Dan'a'yo's two lexical tiers
- <ruby>[声形和決](chengyu/声形和決.md)<rt>ㄙㄧㄫㄏㄝㄫㄏ⺢ㄎ⼔ㄊ</rt></ruby> - the harmony of sound and form, settled as principle; the rule that phonology and character are displayed together
- <ruby>[形助顕理](chengyu/形助顕理.md)<rt>ㄏㄝㄫㄐㄛㄏㄝㄋㄌㄧ</rt></ruby> - form helps reveal structure
- <ruby>[文体並存](chengyu/文体並存.md)<rt>ㄇㄨㄋㄊㄝㄧㄅㄝㄫㄐㄛㄋ</rt></ruby> - Styles coexist
- <ruby>[文言現代](chengyu/文言現代.md)<rt>ㄇㄨㄋ·ㄝㄋㄏ⼶ㄋㄉㄚㄧ</rt></ruby> - Classical Chinese, Modern Day
- <ruby>[文音共決](chengyu/文音共決.md)<rt>ㄇㄨㄋ·ㄨㄇㄍ⼄ㄫㄎ⼔ㄊ</rt></ruby> - script and sound resolved together
- <ruby>[東亜自通](chengyu/東亜自通.md)<rt>ㄉㄛㄫ·ㄚㄐㄧㄜㄊㄛㄫ</rt></ruby> - East Asian self-communication
- <ruby>[毎字明意](chengyu/毎字明意.md)<rt>ㄇㄛㄧㄐㄧㄇ⼔ㄫ·ㄧ</rt></ruby> - Per Character Clear Meaning
- <ruby>[異体不容](chengyu/異体不容.md)<rt>ㄧㄊㄝㄧㄅㄛㄊ⼄ㄫ</rt></ruby> - variant forms are not permitted
- <ruby>[百家共承](chengyu/百家共承.md)<rt>ㄅㄚㄎㄐㄚㄍ⼄ㄫㄙㄨㄫ</rt></ruby> - Hundred schools jointly inherited
- <ruby>[義以立名](chengyu/義以立名.md)<rt>ㄜㄧ·ㄧㄌㄧㄆㄇㄧㄫ</rt></ruby> - By meaning one establishes names
- <ruby>[義重於音](chengyu/義重於音.md)<rt>ㄨㄧㄫㄑㄛㄫ·ㄛㄇ·ㄨㄇ</rt></ruby> - Meaning is more important than sound
- <ruby>[詞彙兼容](chengyu/詞彙兼容.md)<rt>ㄙㄚㄏㄨㄍㄝㄇ·⼄ㄫ</rt></ruby> - The lexicon is capable of inclusion
- <ruby>[選士唯賢](chengyu/選士唯賢.md)<rt>ㄙ⼔ㄋㄙㄚㄧ·⼶ㄧㄏㄝㄋ</rt></ruby> - select candidates solely by worthiness; meritocracy as the sole basis of authority
- <ruby>[鼠世桃源](chengyu/鼠世桃源.md)<rt>ㄙ⼄ㄙㄝㄉㄚㄨ⼔ㄋ</rt></ruby> - the rat-world's Peach Blossom Spring

## Base check
```base
filters:
  and:
    - file.folder == "chengyu"
    - origin == "単亜語"
views:
  - type: table
    name: Table
    filters:
      and:
        - file.folder == "chengyu"
        - origin == "単亜語"
    order:
      - file.name
      - date-last-perfect
      - 注音
      - english
    sort:
      - property: date-last-perfect
        direction: ASC
      - property: size
        direction: ASC
    columnSize:
      note.date-last-perfect: 131
      note.注音: 81

```