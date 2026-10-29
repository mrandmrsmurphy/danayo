---
tags:
  - lookup
date-last-perfect: 2026-10-29
---
# Lint Report

Generated 2026-10-29 by `AIOS/scripts/make_lint_report.py` from the linters' own output. Every flagged page is a clickable link. Re-run any section with the command shown.

> Related: [[lookup/Characters|Characters]] · [[lookup/Words|Words]] · [[AIOS/skills/skill_lint|Lint skill]] · [[AIOS/checklists/checklist_words|Words checklist]] · [[AIOS/checklists/checklist_characters|Characters checklist]]

## Linter status

| Linter | Command | State today |
|---|---|---|
| Syllables | `python3 AIOS/scripts/lint_syllables.py` | Pass; stamped 2026-10-29 |
| SKIP | `python3 AIOS/scripts/lint_skip.py` | Pass; stamped 2026-10-29 |
| Radicals | `python3 AIOS/scripts/lint_radicals.py` | Pass; stamped 2026-10-29 |
| CC | `python3 AIOS/scripts/lint_cc.py` | Pass; stamped 2026-10-29 |
| Stroke | `python3 AIOS/scripts/lint_stroke.py` | Clean (does not stamp) |
| Chengyu | `python3 AIOS/scripts/lint_chengyu.py`, `lint_chengyu_groups.py` | Clean; grouping pages stamped 2026-10-29 |
| Characters | `python3 AIOS/scripts/lint_characters.py` | Default run clean; stamped 2026-10-29. `--deep`: C1 21 |
| **Words** | `python3 AIOS/scripts/lint_words.py` | Fails: C3 9. `--deep`: C1 56, C2 23, C3 41 |

## Contents

- [[#Words (lint_words.py)]]
- [[#Words, --deep run]]
- [[#Characters, --deep run]]
- [[#Judgment items still open]]

## Words (lint_words.py)


### [C3] the lexipedia domain page does not link this word (9)

- [[words/䔥国|䔥国]] -> China
- [[words/中原|中原]] -> Geography
- [[words/中央情報局|中央情報局]] -> Geography
- [[words/九州|九州]] -> Geography
- [[words/九龍|九龍]] -> Geography
- [[words/予州|予州]] -> Geography
- [[words/亜細亜|亜細亜]] -> Geography
- [[words/徳|徳]] -> Periodic Table
- [[words/邾国|邾国]] -> China

## Words, --deep run

The default run checks the body only of pages changed since their own stamp. `python3 AIOS/scripts/lint_words.py --deep` checks every word and finds this drift in already-stamped pages.

### [C1] no `## Notes` section (56)

- [[words/天地|天地]]
- [[words/太始|太始]]
- [[words/深淵|深淵]]
- [[words/焦思|焦思]]
- [[words/焦点|焦点]]
- [[words/熊猫|熊猫]]
- [[words/熟練|熟練]]
- [[words/熱烈|熱烈]]
- [[words/爬虫|爬虫]]
- [[words/牆壁|牆壁]]
- [[words/片仮名|片仮名]]
- [[words/版図|版図]]
- [[words/版本|版本]]
- [[words/版権|版権]]
- [[words/牡丹|牡丹]]
- [[words/牢獄|牢獄]]
- [[words/牧民|牧民]]
- [[words/物証|物証]]
- [[words/物質|物質]]
- [[words/犬吠|犬吠]]
- [[words/犯罪|犯罪]]
- [[words/狂想曲|狂想曲]]
- [[words/狐狸|狐狸]]
- [[words/狗吠|狗吠]]
- [[words/狗盗|狗盗]]
- [[words/狗肉|狗肉]]
- [[words/猛禽|猛禽]]
- [[words/猩猩|猩猩]]
- [[words/猿痘|猿痘]]
- [[words/獄吏|獄吏]]
- [[words/玩具|玩具]]
- [[words/班長|班長]]
- [[words/現象|現象]]
- [[words/球体|球体]]
- [[words/球場|球場]]
- [[words/理想|理想]]
- [[words/理論|理論]]
- [[words/琢磨|琢磨]]
- [[words/環境|環境]]
- [[words/甘味|甘味]]
- [[words/甘藷|甘藷]]
- [[words/甘露|甘露]]
- [[words/産量|産量]]
- [[words/用度|用度]]
- [[words/男性|男性]]
- [[words/畝|畝]]
- [[words/異体|異体]]
- [[words/異常|異常]]
- [[words/異音|異音]]
- [[words/畳|畳]]
- [[words/疲労|疲労]]
- [[words/痕跡|痕跡]]
- [[words/盤|盤]]
- [[words/般|般]]
- [[words/遺憾|遺憾]]
- [[words/黒暗|黒暗]]

### [C2] a [[wikilink]] does not resolve (23)

- [[words/一|一]]: [[nav/Numerals]]
- [[words/七|七]]: [[nav/Numerals]]
- [[words/九|九]]: [[nav/Numerals]]
- [[words/偕者|偕者]]: [[助偕]]
- [[words/偕者|偕者]]: [[誰偕]]
- [[words/光|光]]: [[卩]]
- [[words/兮|兮]]: [[丂]]
- [[words/凶|凶]]: [[凵]]
- [[words/出|出]]: [[凵]]
- [[words/十|十]]: [[nav/Numerals]]
- [[words/反|反]]: [[厂]]
- [[words/合|合]]: [[亼]]
- [[words/喚|喚]]: [[奐]]
- [[words/特点|特点]]: [[特徵]]
- [[words/神道教|神道教]]: [[仏教]]
- [[words/禁書|禁書]]: [[書經]]
- [[words/第|第]]: [[nav/Numerals]]
- [[words/股|股]]: [[殳]]
- [[words/肥脊|肥脊]]: [[瘠]]
- [[words/肺臓|肺臓]]: [[肺腑]]
- [[words/重畳|重畳]]: [[迂言]]
- [[words/零|零]]: [[nav/Numerals]]
- [[words/龍|龍]]: [[wikilink]]

### [C3] the lexipedia domain page does not link this word (41)

- [[words/䔥国|䔥国]] -> China
- [[words/中原|中原]] -> Geography
- [[words/中央情報局|中央情報局]] -> Geography
- [[words/九州|九州]] -> Geography
- [[words/九龍|九龍]] -> Geography
- [[words/予州|予州]] -> Geography
- [[words/亜細亜|亜細亜]] -> Geography
- [[words/内乱|内乱]] -> Geography
- [[words/分布|分布]] -> Geography
- [[words/協議|協議]] -> Geography
- [[words/商路|商路]] -> Geography
- [[words/地域|地域]] -> Geography
- [[words/地理|地理]] -> Geography
- [[words/地龍|地龍]] -> Animals
- [[words/報応|報応]] -> Law
- [[words/多様|多様]] -> Geography
- [[words/多辺|多辺]] -> Geography
- [[words/大韓民国|大韓民国]] -> Geography
- [[words/媒体|媒体]] -> Geography
- [[words/宇宙観|宇宙観]] -> Geography
- [[words/対外|対外]] -> Geography
- [[words/希州|希州]] -> Geography
- [[words/徐州|徐州]] -> Geography
- [[words/徳|徳]] -> Periodic Table
- [[words/持続|持続]] -> Geography
- [[words/揚州|揚州]] -> Geography
- [[words/東伝|東伝]] -> Geography
- [[words/梁州|梁州]] -> Geography
- [[words/殖民|殖民]] -> Geography
- [[words/漢城|漢城]] -> Geography
- [[words/熱帯|熱帯]] -> Geography
- [[words/珈啡因|珈啡因]] -> Food
- [[words/界水|界水]] -> Geography
- [[words/界線|界線]] -> Geography
- [[words/蘇連|蘇連]] -> Geography
- [[words/要地|要地]] -> Geography
- [[words/語言|語言]] -> Geography
- [[words/資源|資源]] -> Geography
- [[words/邾国|邾国]] -> China
- [[words/雍州|雍州]] -> Geography
- [[words/青州|青州]] -> Geography

## Characters, --deep run

The default run checks only pages changed since their own stamp and is clean. `python3 AIOS/scripts/lint_characters.py --deep` checks every page and finds this hidden drift in already-stamped pages.

### [C1] ancient-sound bullet lacks the CC initial/final links (10)

- [[characters/䎎|䎎]]
- [[characters/䒦|䒦]]
- [[characters/傘|傘]]
- [[characters/哱|哱]]
- [[characters/拐|拐]]
- [[characters/搭|搭]]
- [[characters/灋|灋]]
- [[characters/袋 (char)|袋 (char)]]
- [[characters/賠|賠]]
- [[characters/𡈼|𡈼]]

### [C1] ancient-sound bullet does not link its syllable (10)

- [[characters/䎎|䎎]]
- [[characters/䒦|䒦]]
- [[characters/傘|傘]]
- [[characters/哱|哱]]
- [[characters/拐|拐]]
- [[characters/搭|搭]]
- [[characters/灋|灋]]
- [[characters/袋 (char)|袋 (char)]]
- [[characters/賠|賠]]
- [[characters/𡈼|𡈼]]

### [C1] no Classical Chinese / ancient-sound bullet (1)

- [[characters/佤|佤]]

## Judgment items still open

- **Default words run:** clean and stamped. The words `--deep` run (above) shows the drift in already-stamped pages: C1 56 (no Notes section), C2 87 (unresolved links) and C3 54 (domain placement). The C2 markdown links and the C3 placements on this page's default scope were fixed in bulk; the deep ones are the same kinds of fix.
- **Three words naming a lexipedia domain page that doesn't exist:** [[words/信条|信条]], [[words/傾向|傾向]], [[words/六府|六府]].
- **Sound exceptions (B5, resolved):** 13 words keep a documented divergence from their characters and are exempt via `SOUND_EXCEPTIONS` in `lint_words.py`: 反乱, 就鳥, 海就, 白頭就, 禿就, 得点, 特点, 杜選, 瞻妄, 統率, 率性, 釩金, 蓬藁 (plus 棕枝 and 棕枝主日).
- **`mc_id` drift (characters C3, resolved):** all 24 fixed.
