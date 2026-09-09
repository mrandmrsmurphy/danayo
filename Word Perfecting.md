# Word Perfecting

Running log for the word-perfecting backlog sweep (see [[AIOS/checklists/checklist_words.md|Checklist: Word Pages]]). The first log (iterations 1–1040) grew to ~8,500 lines and was archived by the user to `Word Perfecting.md.zip`; a second log (iterations 1041–1782) was archived to `Word Perfecting 2.md.zip`; a third log (iterations 1783–2922) was archived to `Word Perfecting 3.md.zip`; a fourth log (iterations 2923–3555) was archived to `Word Perfecting 4.md.zip`. This file continues from there. Iteration numbering continues unbroken from the archived logs.

**Process**: one word per iteration (per standing pacing preference). Find the next candidate via `grep -L "^date-last-perfect" words/*.md`, sorted alphabetically by filename (Unicode/`LC_ALL=C` order), continuing from the last-processed filename's position in that sort. Check the word's own `characters:` constituents for a `stand_in` match (add the stand-in note if so), verify `羅馬字`/`諺文`/`注音` are the correct concatenation of each constituent's own fields, verify `kwin` via the AND-rule (all constituents' own `kwin` must be `true` for the compound to be `true`), fill blank cross-linguistic fields only when a real value can be verified (leave deliberately blank with a reason otherwise), and check for genuine Dan'a'yo-level homophones (not just same-spelling coincidences in a real language) before stamping `date-last-perfect`.

Next: 静寂.

### 2026-09-08, iteration 3556 — [[words/静寂|静寂]]
Legitimizing note added (静's own `stand_in` is [[静寂]] itself; 寂's own `stand_in` is [[寂滅]], so transitivity fails — no `#cranberry`). Pronunciation fields (jengjeg/정적/ㄐㄝㄫㄐㄝㄎ) and `kwin: true` (AND-rule: both constituents' own kwin true) already matched exactly — no bug. Confirmed `mandarin`'s two comma-joined tone variants (jìngjì, jìngjí) are both genuinely attested, not contamination. Both character pages already cited 静寂 correctly, 静's side with the `(stand-in for 静)` annotation. Filled blank `vietnamese: tĩnh tịch` — attested, mainly Buddhist register, noting Chinese/Vietnamese also freely reverse the order (寂静/tịch tĩnh, corresponding to the vault's own separate [[寂静]]). Removed blank `hsk_level`/`swadesh`, converted flow-style `aliases` to block-list. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 非常.

### 2026-09-08, iteration 3557 — [[words/非常|非常]]
No cranberry (非's own `stand_in` is itself, 常's is [[日常]] — neither points here). **Found and fixed a real bug**: `羅馬字`/`諺文` had been contaminated to `pisyang`/`피샹` instead of the correct concatenation of 非's own stored fields (`fi`/`삐`) — confirmed against the already-correct [[非洲]]/[[南非]], both correctly preserving `fi`/`삐`. `注音` had already stayed correct. `kwin: false` already correct (AND-rule, both constituents false). Filled blank `vietnamese: phi thường` — confirmed standard, everyday term. **Fixed a malformed citation** on `characters/非 (char).md` (bare "[[非常]] ..." text lacking ruby markup, unlike its siblings) and **added a missing citation** to `characters/常.md`'s `## Words` list. Quoted `hsk_level`, removed blank `swadesh`/empty `aliases`. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 面田.

### 2026-09-08, iteration 3558 — [[words/面田|面田]]
No cranberry (面's own `stand_in` is [[表面]], 田's is [[田野]] — neither points here; 面/田 serve as phonetic transliteration characters standing in for the real 緬甸's own 緬/甸). **Found and fixed a real bug**: `注音` had a wrong glyph in its first syllable (ㄇ⼔ㄋ using ⼔, instead of 面's own stored ⼶) — corrected to ㄇ⼶ㄋㄉㄝㄋ, matching `羅馬字`/`諺文`'s already-correct myenden/면던. The same wrong-glyph bug had propagated into both `characters/面.md`'s and `characters/田.md`'s existing citations — fixed both. `kwin: false` already correct (AND-rule). Confirmed all five real-language fields (Miǎndiàn/min5din6/めんでん/면전/Miến Điện) are the real reading of the actual word 緬甸, per the same convention as the 露-transliteration family — めんでん and 면전 verified as real, historically dated (1798/1930) readings, now superseded by ミャンマー/미얀마 respectively but still correct as documented. Removed the redundant duplicate `品詞` field (kept `pos`). Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 革命.

### 2026-09-08, iteration 3559 — [[words/革命|革命]]
No cranberry (革's own `stand_in` is [[皮革]], 命's is [[運命]] — neither points here). **Found and fixed a real bug**: `羅馬字` had been contaminated to `gagmyeng` instead of the correct concatenation of 革's own stored field (`kig`) — `諺文`/`注音` had already stayed correct (킥명/ㄎㄧㄎㄇ⼶ㄫ). `kwin: false` already correct (AND-rule: 革 false, 命 true). Both character pages already cited 革命 correctly. Confirmed `vietnamese`'s two comma-joined forms (cách mệnh, cách mạng) are both genuinely attested — modern standard vs. older literal reading — not contamination. Removed blank `hsk_level`/`swadesh`/empty `aliases`. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 鞀鼓.

### 2026-09-08, iteration 3560 — [[words/鞀鼓|鞀鼓]]
No cranberry (鞀's own `stand_in` is [[鞀鼓]] itself — already documented in this file's pre-existing Notes; 鼓's own `stand_in` is 鼓 itself, so transitivity fails). Pronunciation fields (daugo/닷고/ㄉㄚㄨㄍㄛ) and `kwin: false` already matched constituents exactly — no bug. **Added missing "(stand-in for 鞀)" annotation** to `characters/鞀.md`'s existing citation (鼓's own citation needs none, correctly). Filled blank `vietnamese: đào cổ` — confirmed real, attested term for the same classical pellet-drum instrument. Quoted/reformatted `mandarin`/`cantonese`/`korean` for consistency. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 鞍装.

### 2026-09-08, iteration 3561 — [[words/鞍装|鞍装]]
Legitimizing note added (鞍's own `stand_in` is [[鞍装]] itself; 装's own `stand_in` is [[装]] itself, so transitivity fails — no `#cranberry`). `羅馬字`/`諺文` ('anjwang/안좡) already correctly matched constituents. **Found and fixed three real bugs**: `mandarin` had held [[鞍子]]'s own reading (ānzi) instead of this compound's own (ānzhuāng, a real attested term for "saddle equipment"); `japanese` had held 鞍's bare native reading (くら) instead of the compound's own on'yomi (あんそう, confirmed real via horse-racing terminology 装鞍所); `注音` had a spurious extra ㄋ before the final ㄫ, also propagated into both character pages' citations — all three fixed. Filled blank `cantonese: on1 zong1` and `vietnamese: yên ngựa` (the horse-specific term, vs. the more bicycle-associated yên xe). Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 鞭打.

### 2026-09-08, iteration 3562 — [[words/鞭打|鞭打]]
No cranberry (打's own `stand_in` is [[打撃]], not this word — transitivity fails; 鞭's own `stand_in` is [[鞭打]] itself, already documented in the file's pre-existing Notes bullet). Pronunciation fields (byenda/변다/ㄅ⼶ㄋㄉㄚ) and `kwin: false` already matched constituents exactly — no bug. **Added missing "(stand-in for 鞭)" annotation** to `characters/鞭.md`'s existing citation (打's own citation needs none, correctly). All real-language fields (biāndǎ/bin1daa2/べんだ/편타/tiên đả) confirmed already correct, standard/attested words — a clean case. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check (grep hung briefly on the CJK glyphs, resolved via task notification) found no collision.

Next: 韓国.

### 2026-09-08, iteration 3563 — [[words/韓国|韓国]]
Legitimizing note added (韓's own `stand_in` is [[韓国]] itself; 国's own `stand_in` is [[国家]], so transitivity fails — no `#cranberry`). Pronunciation fields (hangog/한곡/ㄏㄚㄋㄍㄛㄎ) and `kwin: false` already matched constituents exactly — no bug. Both character pages already cited 韓国 correctly, 韓's side with the `(stand-in for 韓)` annotation. All real-language fields (Hánguó/hon4gwok3/かんこく/한국/Hàn Quốc) already correct, standard words in full agreement across all five languages — a clean case; just needed the Notes section written. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 韓国語.

### 2026-09-08, iteration 3564 — [[words/韓国語|韓国語]]
No cranberry (no constituent's own `stand_in` points here — 韓's is [[韓国]], 国's is [[国家]], 語's is [[言語]]). Pronunciation fields (hangog'yo/한곡요/ㄏㄚㄋㄍㄛㄎ·⼄) and `kwin: false` already matched constituents exactly — no bug. **Found and fixed two real bugs**: `mandarin` had held the shorter [[韓語]]'s own colloquial reading (Hányǔ) instead of this compound's own official/textbook term (Hánguóyǔ, distinct from 朝鮮語 for North Korean usage); `cantonese` was likewise missing the middle `gwok3` syllable (hon4jyu5 → hon4gwok3jyu5). **Added a missing citation** to `characters/韓.md`'s `## Words` list (国's/語's own lists already had it). Confirmed `vietnamese: tiếng Hàn Quốc` (fuller/precise form vs. colloquial tiếng Hàn) correctly matches this word's own "(South)" sense. Background exact-match homophone check (hung briefly on a plain-ASCII pattern for unclear reasons, resolved via task notification) found no collision. Stamped `date-last-perfect: 2026-09-08`.

Next: 韓服.

### 2026-09-08, iteration 3565 — [[words/韓服|韓服]]
No cranberry (韓's own `stand_in` is [[韓国]], 服's is [[服事]] — neither points here). Pronunciation fields (hanbug/한북/ㄏㄚㄋㄅㄨㄎ) and `kwin: false` already matched constituents exactly — no bug (한북 uses 服's own Dan'a'yo-derived 북, correctly distinct from real Korean's 한복). Both character pages already cited 韓服 correctly. Fixed `vietnamese`: was the bare English/Korean loanword "Hanbok" — replaced with the formal Sino-Vietnamese term Hàn phục (paralleling áo dài/sườn xám/kimono as national-dress terms), documenting that the loanword Hanbok remains more common in everyday use. Documented that Japanese real usage borrows the Korean pronunciation directly as ハンボク rather than using compositional on'yomi かんふく. Removed blank `hsk_level`/`swadesh`. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 韮金.

### 2026-09-08, iteration 3566 — [[words/韮金|韮金]]
韮金 is 韮's own legitimizing compound (韮's `stand_in` points here, already noted in its own citation); 金's own `stand_in` is 金 itself, so transitivity fails, no `#cranberry`. Pronunciation fields (gyugim/규김/ㄍ⼜ㄍㄧㄇ) and `kwin: false` already correct. Per this neologism series' established convention (cf. [[丹金]], [[霓金]], [[露金]], [[青素]]), verified `mandarin`/`cantonese` (pǔ/pou2) correctly hold the real avoided element character's (镨/鐠) own reading — no bug found, a clean case. 韮's own citation already correctly annotated; 金 (char).md's citation gap is part of the already-documented ~55-file backlog. Removed the redundant duplicate `品詞` field (kept `pos`). Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check (hung again on this environment, resolved via task notification) found no collision.

Next: 音声.

### 2026-09-08, iteration 3567 — [[words/音声|音声]]
No cranberry (音's own `stand_in` is [[音楽]], 声's is [[発声]] — neither points here). Pronunciation fields ('umsing/움싱/ㄨㄇㄙㄧㄫ) already matched constituents exactly — **added entirely missing `kwin: false`** (AND-rule, both constituents false). Fixed comma-joined native-synonym contamination in `korean` (음성, 말소리 → 음성 alone), documenting 말소리 as the native Korean alternative in Notes. Filled blank `vietnamese: âm thanh` — the ordinary, everyday Vietnamese word for "sound." Both character pages already cited 音声 correctly. Quoted `hsk_level`, converted flow-style `aliases` to block-list, removed blank `swadesh`. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 音律.

### 2026-09-08, iteration 3568 — [[words/音律|音律]]
No cranberry (音's own `stand_in` is [[音楽]], 律's is [[法律]] — neither points here). Pronunciation fields ('umlud/움룯/ㄨㄇㄌㄨㄊ) and `kwin: false` already matched constituents exactly — no bug. Confirmed `korean: 음률` is correctly unshifted (no 렬/률→열/율 rule application, since 음 ends in ㅁ not a vowel/ㄴ) — not a bug. All other real-language fields (yīnlǜ/jam1leot6/おんりつ/âm luật) already correct standard terms for musical temperament/rhythm. **Added missing citation** to `characters/律.md`'s `## Words` list (音's own list already had it). Removed empty `aliases: []`, blank `hsk_level`/`swadesh`. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 音波.

### 2026-09-08, iteration 3569 — [[words/音波|音波]]
No cranberry (音's own `stand_in` is [[音楽]], 波's is [[波浪]] — neither points here). Pronunciation fields ('umba/움바/ㄨㄇㄅㄚ) and `kwin: false` already matched constituents exactly — no bug. Both character pages already cited 音波 correctly. All real-language fields (yīnbō/jam1bo1/おんぱ/음파/âm ba) already correct standard words for "soundwave" — a clean case. Reformatted cantonese spacing, removed empty `aliases: []`/blank `hsk_level`/`swadesh`. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 音程.

### 2026-09-08, iteration 3570 — [[words/音程|音程]]
No cranberry (音's own `stand_in` is [[音楽]], 程's is [[程度]] — neither points here). Pronunciation fields ('umding/움딩/ㄨㄇㄉㄧㄫ) and `kwin: false` already matched constituents exactly — no bug (おんてい confirmed correct: 程's own on'yomi is genuinely TEI). **Added missing citation** to `characters/程.md`'s `## Words` list (音's own list already had it). Filled blank `vietnamese: âm trình` — confirmed real, attested academic music-theory term (paralleling more common quãng âm). Removed empty `aliases: []`, blank `hsk_level`/`swadesh`. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 音符.

### 2026-09-08, iteration 3571 — [[words/音符|音符]]
No cranberry (音's own `stand_in` is [[音楽]], 符's is [[符号]] — neither points here). Pronunciation fields ('umbu/움부/ㄨㄇㄅㄨ) and `kwin: false` already matched constituents exactly — no bug. Confirmed `korean: 음부` is a genuine real synonym of the more common 음표, not a bug. Both character pages already cited 音符 correctly. Filled blank `vietnamese: âm phù` — confirmed real, attested term. Incorporated the file's leftover raw `opposite 意符` note into proper Notes prose, documenting 音符's distinct linguistic sense ("phonetic component" vs. 意符 "semantic component" of a character) and flagging that 意符 has no vault word page yet. Removed empty `aliases: []`, blank `hsk_level`/`swadesh`. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found only an expected substring hit within [[注音符号]]'s own longer compound — no genuine collision.

Next: 音節.

### 2026-09-08, iteration 3572 — [[words/音節|音節]]
No cranberry (音's own `stand_in` is [[音楽]], 節's is 節 itself — neither points here). Pronunciation fields ('umjed/움젇/ㄨㄇㄐㄝㄊ) and `kwin: false` already matched constituents exactly — no bug. Both character pages already cited 音節 correctly. **Found and fixed a real bug**: `aliases` had wrongly listed 音節 (the headword's own traditional form, identical to the filename) as an alias of itself — trimmed to just the genuine simplified variant 音节. All real-language fields (yīnjié/jam1zit3/おんせつ/음절/âm tiết) already correct standard words for "syllable" — a clean case otherwise. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 音素.

### 2026-09-08, iteration 3573 — [[words/音素|音素]]
No cranberry (音's own `stand_in` is [[音楽]], 素's is [[要素]] — neither points here). Pronunciation fields ('umso/움소/ㄨㄇㄙㄛ) and `kwin: false` already matched constituents exactly — no bug. **Found and fixed a real bug**: `japanese` had いんそ, using 音's secondary on'yomi IN instead of the compound's correct primary reading ON — confirmed おんそ is the sole correct linguistics reading, いんそ explicitly non-standard. Both character pages already cited 音素 correctly. All other real-language fields (yīnsù/jam1sou3/음소/âm tố) already correct standard terms for "phoneme." Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 音韻.

### 2026-09-08, iteration 3574 — [[words/音韻|音韻]]
No cranberry (音's own `stand_in` is [[音楽]], 韻's is [[押韻]] — neither points here). Pronunciation fields ('um'un/움운/ㄨㄇㄨㄋ) already matched constituents exactly — **added entirely missing `kwin: false`** (AND-rule: 音 false, 韻 true). **Found and fixed a real bug**: `vietnamese` had held "Âm vị," which is actually derived from the different compound 音位 ("phoneme," using 位) rather than 音韻 (韻's own vietnamese field is vần/vận) — corrected to the compositionally accurate âm vận. Fixed comma-joined native-synonym contamination in `korean` (음운, 목소리 → 음운 alone). Documented the systemic "phonology" sense of 音韻 vs. [[音素]]'s more individual "phoneme" sense, adding `phonology` to `english`. Both character pages already cited 音韻 correctly. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 韻母.

### 2026-09-08, iteration 3575 — [[words/韻母|韻母]]
No cranberry (韻's own `stand_in` is [[押韻]], 母's is [[母親]] — neither points here). Pronunciation fields ('unmou/운못/ㄨㄋㄇㄛㄨ) and `kwin: false` already matched constituents exactly — no bug. **Found and fixed a real bug**: `cantonese` had `wan5` instead of 韻's own stored jyutping `wan6` — corrected to `wan6 mou5`. Both character pages already cited 韻母 correctly. All other real-language fields (yùnmǔ/いんぼ/운모/vận mẫu) already correct standard terms for the phonological "final/rime." Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 頂点.

### 2026-09-08, iteration 3576 — [[words/頂点|頂点]]
Legitimizing note added (頂's own `stand_in` is [[頂点]] itself; 点's own `stand_in` is 点 itself, so transitivity fails — no `#cranberry`). Pronunciation fields (jengdem/정덤/ㄐㄝㄫㄉㄝㄇ) and `kwin: false` already matched constituents exactly — no bug. Both character pages already cited 頂点 correctly, 頂's side with the `(stand-in for 頂)` annotation. Filled blank `vietnamese: đỉnh điểm` — confirmed standard, everyday term. Fixed `characters:` disambiguation-suffix mismatch (点→点 (char)). A clean case otherwise — all real-language fields already correct standard words. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 頃.

### 2026-09-08, iteration 3577 — [[words/頃|頃]]
Legitimizing note added (this bare-character word is 頃's own legitimizer, `stand_in` points here). Pronunciation fields (keng/컹/ㄎㄝㄫ) already matched the character's own stored values exactly — no bug. **Found and fixed the literal-"null"-string bug** in `vietnamese` — replaced with `khoảnh` (attested, e.g. in khoảnh khắc "an instant"). Added entirely missing `kwin: false`, `pos: 名詞`, and `japanese: ころ` (documenting that this character functions as a standalone word almost exclusively via its native kun'yomi, not on'yomi ケイ). Fixed heading level (`# Notes`→`## Notes`) and the character page's own citation annotation (was "(stand-in for 頃 (char))", now the conventional "(stand-in for 頃)"). Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found a shared syllable with [[傾]] (also ㅋㅔㅇ/ㄎㄝㄫ), but 傾's own `stand_in` is [[傾向]], not itself — no genuine word-level collision.

Next: 順序.

### 2026-09-08, iteration 3578 — [[words/順序|順序]]
Legitimizing note added (序's own `stand_in` is [[順序]] itself; 順's own `stand_in` is [[順次]], so transitivity fails — no `#cranberry`; incorporated the file's leftover raw "Stand-in for [[序]]" note into proper Notes prose). Pronunciation fields (syunsyo/슌쇼/ㄙ⼜ㄋㄙ⼄) and `kwin: false` already matched constituents exactly — no bug. **Added missing "(stand-in for 序)" annotation** to `characters/序.md`'s existing citation (順's own citation needs none, correctly). Filled blank `vietnamese: thuận tự` — confirmed real, attested term (alongside the more everyday native thứ tự). A clean case otherwise — all other real-language fields already correct standard words. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 順次.

### 2026-09-08, iteration 3579 — [[words/順次|順次]]
Legitimizing note added (順's own `stand_in` is [[順次]] itself, already annotated in its own citation; 次's own `stand_in` is [[次第]], so transitivity fails — no `#cranberry`; incorporated the file's leftover raw "Stand-in for [[順]]" note into proper Notes prose). Pronunciation fields (syunciǝ/슌츼/ㄙ⼜ㄋㄑㄧㄜ) and `kwin: false` already matched constituents exactly — no bug. Both character pages already cited 順次 correctly. Removed the redundant duplicate `品詞` field (kept `pos`). Filled blank `vietnamese: thuận thứ` — compositionally straightforward but not independently attested (modern Vietnamese uses native lần lượt/tuần tự instead). Removed blank `hsk_level`/`swadesh`. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 頗.

### 2026-09-08, iteration 3580 — [[words/頗|頗]]
Legitimizing note added (this bare-character word is 頗's own legitimizer, `stand_in` points here; already annotated on the character's own citation). Pronunciation fields (fa/빠/ㄈㄚ) already matched the character's own stored values exactly — no bug (deliberately vacant-syllable-filling, not derived from real readings). Added entirely missing `pos: 修飾語`, `japanese: は` (documenting real Japanese more commonly uses native すこぶる), and `vietnamese: phả`. Reformatted `mandarin`'s two space-separated tone variants to comma-separated (both genuinely attested — pō standard, pǒ archaic/Classical). Fixed heading level (`# Notes`→`## Notes`). Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found only the character's own page (expected), no genuine collision.

Next: 領土.

### 2026-09-08, iteration 3581 — [[words/領土|領土]]
Legitimizing note added (領's own `stand_in` is [[領土]] itself, already annotated in its own citation; 土's own `stand_in` is 土 itself, so transitivity fails — no `#cranberry`). Pronunciation fields (lingto/링토/ㄌㄧㄫㄊㄛ) and `kwin: false` already matched constituents exactly — no bug. **Found and fixed a real bug**: `korean` had 령토 (North Korean orthography) instead of the South Korean standard 영토, matching the same fix pattern as [[霊魂]]→영혼/[[霊柩]]→영구. **Added missing citation** to `characters/土 (char).md`'s `## Words` list (領's own list already had it). Fixed `characters:` disambiguation-suffix mismatch (土→土 (char)). Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 頬.

### 2026-09-08, iteration 3582 — [[words/頬|頬]]
Legitimizing note added (this bare-character word is 頬's own legitimizer, `stand_in` points here; already annotated on the character's own citation). Pronunciation fields (geb/겁/ㄍㄝㄆ) already matched the character's own stored values exactly — no bug. **Found and fixed the literal-"null"-string bug** in `vietnamese` — replaced with `giáp` (the character's own stored reading). Added entirely missing `pos: 名詞` and `japanese: きょう` (matching the precedent already set on the reciprocal homophone [[鋏]], documenting native ほお as the everyday reading). Fixed heading level (`# Notes`→`## Notes`) and `characters:` unquoted-scalar format. Stamped `date-last-perfect: 2026-09-08`. Confirmed the existing [[鋏]] homophone callout remains correctly reciprocal — no new collisions.

Next: 頭.

### 2026-09-08, iteration 3583 — [[words/頭|頭]]
Legitimizing note added (this bare-character word is 頭's own legitimizer, `stand_in` points here; already annotated on the character's own citation). Pronunciation fields (tou/톳/ㄊㄛㄨ) already matched the character's own stored values exactly — no bug. Added entirely missing `pos: 名詞`, `japanese: あたま` (the ordinary native word; on'yomi とう/ず survive only bound), and `vietnamese: đầu`. **In passing**, filled a real gap on `characters/頭 (char).md`: `japanese_native` was stored as `ø` despite あたま/かしら being well-attested — added both. **Discovered and documented a genuine 3-way Dan'a'yo homophone cluster**: 頭/[[套]]/[[透]] all share 톳/ㄊㄛㄨ and are each their own legitimizer — none had been cross-referenced before (套 was already fully perfected but missing this; 透 not yet perfected). Added reciprocal `>[!warning] Homophones` callouts to all three files (透's other bugs left for when the sweep naturally reaches it). Stamped `date-last-perfect: 2026-09-08` on 頭.

Next: 頭骨.

### 2026-09-08, iteration 3584 — [[words/頭骨|頭骨]]
No cranberry (both 頭's and 骨's own `stand_in` are themselves). **Found and fixed a real bug**: `諺文`/`注音` had both been contaminated to a wrong-vowel form of 骨's syllable (굳/ㄍㄨㄊ instead of correct 곧/ㄍㄛㄊ) — `羅馬字` had already stayed correct (tougod). The same error had propagated into `characters/骨 (char).md`'s existing citation — fixed there too. `kwin: false` already correct. Both character pages already cited 頭骨 correctly (skulls-side annotation none needed). Filled blank `vietnamese: đầu cốt` — attested medical/anatomical term, everyday Vietnamese preferring native sọ/hộp sọ. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 頻.

### 2026-09-08, iteration 3585 — [[words/頻|頻]]
Legitimizing note added (this bare-character word is 頻's own legitimizer, `stand_in` points here; already annotated on the character's own citation). Pronunciation fields (pim/핌/ㄆㄧㄇ) already matched the character's own stored values exactly — no bug. Added entirely missing `kwin: false`, `pos: 修飾語`, and `japanese: ひん` (documenting native しきりに as the everyday word). `vietnamese: tần` was already correctly filled. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 題目.

### 2026-09-08, iteration 3586 — [[words/題目|題目]]
No cranberry (題's own `stand_in` is [[標題]], 目's is 目 itself — neither points here). Pronunciation fields (teimug/테묵/ㄊㄝㄧㄇㄨㄎ) and `kwin: false` already matched constituents exactly — no bug (だいもく confirmed correct: 題's own on'yomi is genuinely DAI, not TEI, distinct from its Dan'a'yo romanization). Both character pages already cited 題目 correctly. A clean case — all real-language fields (tímù/tai4muk6/だいもく/제목/đề mục) already correct standard words. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 額頭.

### 2026-09-08, iteration 3587 — [[words/額頭|額頭]]
Legitimizing note added (額's own `stand_in` is [[額頭]] itself, already annotated in its own citation; 頭's own `stand_in` is 頭 itself, so transitivity fails — no `#cranberry`). Pronunciation fields ('agtou/악톳/ㄚㄎㄊㄛㄨ) and `kwin: false` already matched constituents exactly — no bug. Both character pages already cited 額頭 correctly. Confirmed `japanese`/`korean`/`vietnamese` (ひたい/이마/trán) are correctly native forms, not compositional-reading bugs — none of the three languages has a live Sino-derived compound for "forehead," documented in Notes. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 顔色.

### 2026-09-08, iteration 3588 — [[words/顔色|顔色]]
No cranberry (顔's own `stand_in` is [[顔面]], 色's is [[色彩]] — neither points here). **Found and fixed a real bug**: `cantonese` had `yan2 se2`, an invalid non-jyutping romanization unrelated to either constituent — corrected to `ngaan4 sik1`, matching 顔's own `ngaan4` and 色's own `sik1`. Pronunciation fields ('ansig/안식/ㄚㄋㄙㄧㄎ) and `kwin: false` already matched constituents exactly. Filled blank `vietnamese: nhan sắc` — real and attested but narrowed specifically to "(a woman's) beauty" rather than the broader "complexion" sense elsewhere. **Fixed a malformed citation** on `characters/顔.md` (bare "[[顔色]] - complexion" lacking ruby/bopomofo, unlike its siblings; 色's own citation was already correctly formatted). Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 顔面.

### 2026-09-08, iteration 3589 — [[words/顔面|顔面]]
Legitimizing note added (顔's own `stand_in` is [[顔面]] itself; 面's own `stand_in` is [[表面]], so transitivity fails — no `#cranberry`). Pronunciation fields ('anmyen/안면/ㄚㄋㄇ⼶ㄋ) already matched constituents exactly — **added entirely missing `kwin: true`** (AND-rule: both constituents' own kwin true, a rarer case). Fixed comma-joined native-synonym contamination in `korean` (안면, 얼굴, 낯 → 안면 alone). Confirmed `vietnamese: mặt` is correct as-is (native, no live Sino "nhan diện" attested). **Fixed a malformed citation** on `characters/顔.md` (bare "[[顔面]] - face" lacking ruby/bopomofo and the "(stand-in for 顔)" annotation it needs). Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 顕現.

### 2026-09-08, iteration 3590 — [[words/顕現|顕現]]
No cranberry (顕's own `stand_in` is [[顕著]], 現's is 現 itself — neither points here). Pronunciation fields (henhyen/헌현/ㄏㄝㄋㄏ⼶ㄋ) and `kwin: false` already matched constituents exactly — no bug. Both character pages already cited 顕現 correctly. A clean case — all real-language fields (xiǎnxiàn/hin2jin6/けんげん/현현/hiển hiện) already correct standard terms, often in philosophical/religious registers. Removed blank `hsk_level`/`swadesh`. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 顕示.

### 2026-09-08, iteration 3591 — [[words/顕示|顕示]]
No cranberry (顕's own `stand_in` is [[顕著]], 示's is [[開示]] — neither points here). Pronunciation fields (henge/헌거/ㄏㄝㄋㄍㄝ) already matched constituents exactly — **added entirely missing `kwin: false`**. **Found and fixed a real bug**: `cantonese` had `xian3 si4`, garbled pinyin-like text unrelated to either constituent's own jyutping — corrected to `hin2 si6`. Filled entirely blank `japanese: けんじ` and `korean: 현시` (both confirmed real, attested). `vietnamese: hiển thị` was already correctly filled (a common technical-display term today). Both character pages already cited 顕示 correctly. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 願意.

### 2026-09-08, iteration 3592 — [[words/願意|願意]]
Legitimizing note added (願's own `stand_in` is [[願意]] itself; 意's own `stand_in` is [[意味]], so transitivity fails — no `#cranberry`). Pronunciation fields ('wen'ǝ/원으/⼔ㄋㄜ) already matched constituents exactly — **added entirely missing `kwin: false`**. Both character pages already cited 願意 correctly, 願's side with the `(stand-in for 願)` annotation. Confirmed `japanese: がんい` is real but carries a narrower "content of a wish/petition" sense (formal/religious register) rather than plain "willing." Filled blank `vietnamese: nguyện ý` — confirmed real, standard term. `korean: 원의` already correctly filled. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 顚癇.

### 2026-09-08, iteration 3593 — [[words/顚癇|顚癇]]
**Added missing `#cranberry` tag**: both 顚's own `stand_in` and 癇's own `stand_in` point here to 顚癇 itself (A=B=AB, full transitivity) — neither character can stand alone, yet the tag was absent. **Found and fixed a real bug**: `羅馬字` had `dinhan` instead of the correct concatenation of 顚's own stored field (`den`) — `諺文`/`注音` had already stayed correct. Added entirely missing `kwin: false`. Fixed comma-joined contamination in `korean` (간질, 땡깡 → 간질 alone) — documented that 땡깡, though genuinely borrowed from Japanese てんかん, has fully shifted meaning to "tantrum" in modern Korean and is discouraged slang, not interchangeable with 간질. Confirmed `vietnamese: điên giản` is compositionally exact but not the standard medical term (native động kinh is standard). Both character pages already correctly cited and annotated. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 類人猿.

### 2026-09-08, iteration 3594 — [[words/類人猿|類人猿]]
No cranberry (no constituent's own `stand_in` points here). Pronunciation fields (luinin'on/뤼닌온/ㄌㄨㄧㄋㄧㄋㄛㄋ) and `kwin: false` already matched constituents exactly — no bug. **Found and fixed a real bug**: `japanese` had るいじんゑん, using the obsolete kana ゑ (abolished 1946) instead of modern え. Confirmed `korean: 유인원` is correct (류→유 word-initial 두음법칙). Filled blank `vietnamese: vượn người` — native, reversed-order standard term (no live Sino equivalent). **Added missing citation** to `characters/人 (char).md`'s `## Words` list and **fixed a malformed citation** on `characters/猿.md` (bare "[[類人猿]] - simian" lacking ruby/bopomofo). Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 類似.

### 2026-09-08, iteration 3595 — [[words/類似|類似]]
No cranberry (類's own `stand_in` is [[種類]], 似's is 似 itself — neither points here). Pronunciation fields (luisa/뤼사/ㄌㄨㄧㄙㄚ) already matched constituents exactly — **added entirely missing `kwin: false`**. Fixed comma-joined native-synonym contamination in `korean` (유사,비슷 → 유사 alone). Fixed `characters:` disambiguation-suffix mismatch (似→似 (char)). Filled blank `vietnamese: loại tự` — compositionally straightforward but not independently attested; documented that the actual standard Vietnamese term, tương tự, is built on the different compound 相似 rather than 類似's own characters. Both character pages already cited 類似 correctly. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 類似格.

### 2026-09-08, iteration 3596 — [[words/類似格|類似格]]
No cranberry (no constituent's own `stand_in` points here). Pronunciation fields (luisagag/뤼사각/ㄌㄨㄧㄙㄚㄍㄚㄎ) and `kwin: false` already matched constituents exactly — no bug. All three character pages already cited 類似格 correctly. Filled blank `vietnamese: loại tự cách`, matching the established case-name convention (cf. [[呼格]] hô cách, [[属格]] thuộc cách) — this word names Dan'a'yo's own similative grammatical case, so the five real-language fields are compositional linguistic terminology rather than independently common words. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 風刺.

### 2026-09-08, iteration 3597 — [[words/風刺|風刺]]
No cranberry (both 風's and 刺's own `stand_in` are themselves). Pronunciation fields (fungcig/뿡칙/ㄈㄨㄫㄑㄧㄎ) and `kwin: false` already matched constituents exactly — no bug. Documented that this word is written with the alias 諷/讽 rather than bare 風, and that 諷 has its own distinct real-language readings for the "satirize" sense (fěng, phúng) differing from 風's own "wind" readings — a reading-split pattern. **Found and fixed real bugs**: `mandarin` had a spurious second variant `fèngcì` (諷 has no attested fèng reading) — trimmed to `fěngcì` alone; `english` had a typo (satarize→satirize). Filled blank `vietnamese: phúng thích` (attested, though châm biếm/trào phúng are more everyday). **In passing, fixed a real bug on `characters/風 (char).md`'s own self-citation** (showed ㄆㄨㄫ instead of the character's own stored ㄈㄨㄫ) **and on `words/風.md` itself** (same ㄆ→ㄈ typo, an already-stamped word page). Stamped `date-last-perfect: 2026-09-08` on 風刺. Background exact-match homophone check found no collision.

Next: 風潮.

### 2026-09-08, iteration 3598 — [[words/風潮|風潮]]
No cranberry (風's own `stand_in` is 風 itself, 潮's is [[潮汐]] — neither points here). Pronunciation fields (fungcau/뿡찻/ㄈㄨㄫㄑㄚㄨ) and `kwin: false` already matched constituents exactly — no bug. **Added missing "trend" to `english`** (already documented on the character page's own citation gloss, and confirmed the actual most common modern sense of 風潮). All real-language fields (fēngcháo/fung1ciu4/ふうちょう/풍조/phong trào) already correct — Vietnamese phong trào has narrowed specifically to the "movement, trend" sense and is one of the most common words in the language. Removed empty `aliases: []`, blank `hsk_level`/`swadesh`. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 風笛.

### 2026-09-08, iteration 3599 — [[words/風笛|風笛]]
No cranberry (風's own `stand_in` is 風 itself, 笛's is [[口笛]] — neither points here). Pronunciation fields (fungdeg/뿡덕/ㄈㄨㄫㄉㄝㄎ) and `kwin: false` already matched constituents exactly — no bug. **Found and fixed a real bug**: `japanese` had バグパイプ (the bare English loanword) instead of the real, attested compositional alternate name ふうてき — confirmed both terms exist in Japanese, with バグパイプ more common in everyday use (documented in Notes). Confirmed `korean: 백파이프` (the loanword) is correct as-is — 풍적 exists but denotes wind-pipes more broadly, not the Scottish bagpipe specifically. `vietnamese: kèn túi` was already correct (native, no live Sino equivalent). Both character pages already cited 風笛 correctly. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 風采.

### 2026-09-08, iteration 3600 — [[words/風采|風采]]
Legitimizing note added (采's own `stand_in` is [[風采]] itself; 風's own `stand_in` is 風 itself, so transitivity fails — no `#cranberry`). Pronunciation fields (fungcai/뿡채/ㄈㄨㄫㄑㄚㄧ) already matched constituents exactly — **added entirely missing `kwin: false`**. **Fixed real empty-string bugs** in both `korean` and `vietnamese` (both `""`) — filled with confirmed real, standard terms 풍채 and phong thái. Removed the redundant duplicate `品詞` field (kept `pos`). Both character pages already cited 風采 correctly, 采's side with the `(stand-in for 采)` annotation. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 颯.

### 2026-09-08, iteration 3601 — [[words/颯|颯]]
Legitimizing note added (this bare-character word is 颯's own legitimizer, `stand_in` points here). Pronunciation fields (sab/삽/ㄙㄚㄆ) already matched the character's own stored values exactly — no bug. Added entirely missing `kwin: true` (matching the character's own kwin) and `japanese: さつ` (on'yomi, surviving mainly in 颯爽). **Added missing "(stand-in for 颯)" annotation** to the character's own citation. Fixed heading level (`# Notes`→`## Notes`). Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 飛報.

### 2026-09-08, iteration 3602 — [[words/飛報|飛報]]
No cranberry (both 飛's and 報's own `stand_in` are themselves). **Found and fixed a real bug**: `羅馬字`/`諺文` had been contaminated to `pibau`/`피밧`, using 飛's other reading branch (ㄆㄧ, seen in [[飛行机]]/[[飛語]]) instead of this word's own primary branch — `注音` had already stayed correct (ㄈㄝㄧㄅㄚㄨ), confirmed against 飛's own citation of this exact word. `kwin: false` already correct. Both character pages already cited 飛報 correctly. Filled blank `vietnamese: phi báo` — confirmed real, attested term. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 飛机.

### 2026-09-08, iteration 3603 — [[words/飛机|飛机]]
No cranberry (飛's own `stand_in` is 飛 itself, 机's is [[机会]] — neither points here). **Found and fixed a real bug**: `羅馬字`/`諺文` had been contaminated to `pigiǝ`/`피긔`, using 飛's other reading branch (ㄆㄧ, seen in [[飛行机]]) instead of this word's own primary branch — confirmed via both 飛's and 机's own citations of this exact word. Added entirely missing `kwin: false`. Filled blank `korean: 비행기` (the real everyday word, built on the fuller 飛行機 rather than 飛机's own literal characters — same pattern as japanese ひこうき, already correctly filled). `vietnamese: phi cơ` already correctly matched 飛机's own literal characters. Both character pages already cited 飛机 correctly. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 飛行机.

### 2026-09-08, iteration 3604 — [[words/飛行机|飛行机]]
No cranberry (no constituent's own `stand_in` points here). Pronunciation fields (pihanggiǝ/피항긔/ㄆㄧㄏㄚㄫㄍㄧㄜ) and `kwin: false` already matched constituents exactly — confirmed correct as the ㄆㄧ-branch long form of [[飛机]] (verified via all three constituents' own citations). Filled blank `vietnamese: phi hành cơ` — compositionally straightforward but not independently attested (phi cơ or native máy bay are the actual Vietnamese terms). All three character pages already cited 飛行机 correctly. Removed empty `aliases: []`, blank `hsk_level`/`swadesh`. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 飛語.

### 2026-09-08, iteration 3605 — [[words/飛語|飛語]]
No cranberry (飛's own `stand_in` is 飛 itself, 語's is [[言語]] — neither points here). Pronunciation fields (pi'yo/피요/ㄆㄧ·⼄) and `kwin: false` already matched constituents exactly — confirmed correct as the ㄆㄧ-branch (verified via both constituents' own citations). Both character pages already cited 飛語 correctly. Filled blank `vietnamese: phi ngữ` — confirmed real, attested term for "baseless rumor," matching the idiom 流言飛語/流言蜚語 already documented on the Japanese ひご side too. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 飛鳥.

### 2026-09-08, iteration 3606 — [[words/飛鳥|飛鳥]]
No cranberry (both 飛's and 鳥's own `stand_in` are themselves). **Found and fixed a real bug**: `羅馬字`/`諺文` had been contaminated to `picou`/`피촛`, using 飛's other reading branch (ㄆㄧ) instead of this word's own primary branch — confirmed via both 飛's and 鳥's own citations of this exact word (`注音` had already stayed correct). `kwin: false` already correct. Confirmed the three distinct `japanese` readings (ひちょう/とぶとり/あすか, including the special Asuka place-name reading) are all genuinely real and not contamination. Removed the redundant duplicate `品詞` field. Both character pages already cited 飛鳥 correctly. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 食堂.

### 2026-09-08, iteration 3607 — [[words/食堂|食堂]]
No cranberry (食's own `stand_in` is 食 itself, 堂's is [[会堂]] — neither points here). Pronunciation fields (sigdang/식당/ㄙㄧㄎㄉㄚㄫ) and `kwin: true` (AND-rule: both constituents' own kwin true) already matched constituents exactly — no bug. Both character pages already cited 食堂 correctly. Filled blank `vietnamese: thực đường` — compositionally straightforward but not independently attested (native nhà ăn or loanword căng tin are the actual Vietnamese terms). Removed empty `aliases: []`, blank `hsk_level`/`swadesh`. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 食指.

### 2026-09-08, iteration 3608 — [[words/食指|食指]]
No cranberry (食's own `stand_in` is 食 itself, 指's is [[手指]] — neither points here). Pronunciation fields (sigjiǝ/식즤/ㄙㄧㄎㄐㄧㄜ) and `kwin: false` already matched constituents exactly — no bug. **Found and fixed a real bug**: `cantonese` had `si2 zi3`, matching neither constituent's own stored reading — corrected to `sik6 zi2`. Filled blank `vietnamese: thực chỉ` — confirmed real, attested term (also used to mean "number of diners"). Confirmed `japanese: しょくし` and `korean: 식지` are both real, formal alternatives to the more common native terms (人差し指/검지). Both character pages already cited 食指 correctly. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 食費.

### 2026-09-08, iteration 3609 — [[words/食費|食費]]
No cranberry (both 食's and 費's own `stand_in` are themselves). **Found and fixed a real bug**: `mandarin` had held the longer alias 伙食费's own reading (huǒ shí fèi, with an extra 伙) instead of this word's own two-character reading — corrected to `shífèi`. Pronunciation fields (sigfai/식빼/ㄙㄧㄎㄈㄚㄧ) already matched constituents exactly — **added entirely missing `kwin: false`**. Fixed comma-joined native-synonym contamination in `korean` (식비, 밥값 → 식비 alone). Filled blank `vietnamese: thực phí` — confirmed real, attested term. Both character pages already cited 食費 correctly. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 食酢.

### 2026-09-08, iteration 3610 — [[words/食酢|食酢]]
Legitimizing note added (酢's own `stand_in` is [[食酢]] itself; 食's own `stand_in` is 食 itself, so transitivity fails — no `#cranberry`). Pronunciation fields (sigjag/식작/ㄙㄧㄎㄐㄚㄎ) and `kwin: false` already matched constituents exactly — no bug. Confirmed a genuine reading-split on 酢: classical "toast" sense (zuò, matching its own Dan'a'yo derivation) vs. modern "vinegar" sense (merged with 醋's own cù/cou3 in Mandarin/Cantonese) — `mandarin: shí cù` was already correct for the vinegar sense (reformatted spacing); **filled blank `cantonese: sik6 cou3`** using the correct vinegar-sense reading, not 酢's own stored zok6. Confirmed `japanese: しょくす` (the official JAS 1979 term) and `korean: 식초` are both correct, using 酢's own real reading rather than the vault's Dan'a'yo derivation. Filled blank `vietnamese: thực thố` — compositionally straightforward but not independently attested (native giấm/giấm ăn are the actual terms). Both character pages already cited 食酢 correctly. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 飢餓.

### 2026-09-08, iteration 3611 — [[words/飢餓|飢餓]]
Confirmed existing `#cranberry` tag is correct: both 飢's own `stand_in` and 餓's own `stand_in` point here to 飢餓 itself (A=B=AB, full transitivity). Pronunciation fields (giǝ'a/긔아/ㄍㄧㄜ·ㄚ) already matched constituents exactly. **Found and fixed a real bug**: `cantonese` had `ei1 ngo6`, missing 飢's own initial `g` — corrected to `gei1 ngo6`. Added entirely missing `kwin: false`. Fixed comma-joined native-synonym contamination in `korean` (기아, 굶주림 → 기아 alone). Fixed `vietnamese` from the native đói to the compositionally-attested Sino form cơ ngạ, documenting đói as the everyday native word. **In passing**, removed a duplicate `品詞` field and fixed the heading level (`# Notes`→`## Notes`) on `characters/餓.md`. Both character pages already cited 飢餓 correctly. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 飯店.

### 2026-09-08, iteration 3612 — [[words/飯店|飯店]]
No cranberry (飯's own `stand_in` is [[米飯]], 店's is [[商店]] — neither points here). Pronunciation fields (bondem/본덤/ㄅㄛㄋㄉㄝㄇ) already matched constituents exactly — **added entirely missing `kwin: false`**. Filled blank `korean: 반점` and `vietnamese: phạn điếm` — confirmed both real; documented that Japanese はんてん and Korean 반점 have narrowed specifically to "Chinese restaurant," while Sino-Vietnamese phạn điếm keeps the fuller original "restaurant/hotel" range matching Mandarin. Both character pages already cited 飯店 correctly. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 飲.

### 2026-09-08, iteration 3613 — [[words/飲|飲]]
Legitimizing note added (this bare-character word is 飲's own legitimizer, `stand_in` points here). Pronunciation fields ('um/움/ㄨㄇ) already matched the character's own stored values exactly. **Found and fixed a real bug**: `kwin` was `true`, contradicting the character's own stored `kwin: false` — corrected to match. Added entirely missing `pos: 事詞`, `japanese: いん`, `korean: 음`, and `vietnamese: ẩm` (as in ẩm thực, "food and drink"). **Added missing self-citation** ("(stand-in for 飲)") to the character's own Words list. Fixed heading level (`# Notes`→`## Notes`). Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found a shared syllable with [[音]] (also 'um/움/ㄨㄇ), but 音's own `stand_in` is [[音楽]], not itself — no genuine word-level collision.

Next: 飲食.

### 2026-09-08, iteration 3614 — [[words/飲食|飲食]]
No cranberry (both 飲's and 食's own `stand_in` are themselves). Pronunciation fields ('umsig/움식/ㄨㄇㄙㄧㄎ) and `kwin: false` already matched constituents exactly — no bug. Both character pages already cited 飲食 correctly. A clean case — all real-language fields (yǐnshí/jam2sik6/いんしょく/음식/ẩm thực) already correct standard everyday words. Fixed `characters:`/`aliases:` flow-style formatting. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found only an expected substring hit within [[飲食物]]'s own longer compound — no genuine collision.

Next: 飲食物.

### 2026-09-08, iteration 3615 — [[words/飲食物|飲食物]]
No cranberry (no constituent's own `stand_in` points here). Pronunciation fields ('umsigmud/움식묻/ㄨㄇㄙㄧㄎㄇㄨㄊ) and `kwin: false` already matched constituents exactly — no bug. All three character pages already cited 飲食物 correctly. Filled blank `cantonese: jam2 sik6 mat6` (compositional) and `vietnamese: ẩm thực vật` — compositionally exact but flagged as a real ambiguity risk, since it shares its last two syllables with 植物 (thực vật, "plant") and could be misparsed as "plant-based cuisine"; modern Vietnamese instead uses native phrases like đồ ăn thức uống. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 飽.

### 2026-09-08, iteration 3616 — [[words/飽|飽]]
Legitimizing note added (this bare-character word is 飽's own legitimizer, `stand_in` points here). Pronunciation fields (byau/뱟/ㄅ⼘ㄨ) already matched the character's own stored values exactly. **Found and fixed the literal-"null"-string bug** in `vietnamese` — replaced with `bão` (the character's own stored reading). Added entirely missing `pos: 性詞` and `japanese: ほう`. **Added missing self-citation** ("(stand-in for 飽)") to the character's own Words list. Fixed heading level (`# Notes`→`## Notes`). Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found several syllable-mates (砲/包/表/俵/豹/胞/跑) but none is itself a legitimized single-character word — no genuine collision.

Next: 飽足.

### 2026-09-08, iteration 3617 — [[words/飽足|飽足]]
No cranberry (both 飽's and 足's own `stand_in` are themselves). Pronunciation fields (byaujog/뱟족/ㄅ⼘ㄨㄐㄛㄎ) already matched constituents exactly — **added entirely missing `kwin: false`**. Filled entirely blank `japanese: ほうそく`, `korean: 포족`, and `vietnamese: bão túc` (japanese/korean confirmed real and attested; vietnamese compositional but not independently attested, native no đủ/thỏa mãn are the actual terms). Fixed `characters:` disambiguation-suffix mismatch (飽→飽 (char), 足→足 (char)). Both character pages already cited 飽足 correctly. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 養成.

### 2026-09-08, iteration 3618 — [[words/養成|養成]]
No cranberry (養's own `stand_in` is [[養育]], 成's is 成 itself — neither points here). Pronunciation fields ('yangsing/양싱/⼘ㄫㄙㄧㄫ) and `kwin: false` already matched constituents exactly — no bug. Both character pages already cited 養成 correctly. Confirmed the existing [[陽性]] homophone callout remains correctly reciprocal on both pages. Filled blank `vietnamese: dưỡng thành` — confirmed real, attested term. A clean case otherwise. Stamped `date-last-perfect: 2026-09-08`.

Next: 養殖.

### 2026-09-08, iteration 3619 — [[words/養殖|養殖]]
No cranberry (養's own `stand_in` is [[養育]], 殖's is [[繁殖]] — neither points here). Pronunciation fields ('yangsig/양식/⼘ㄫㄙㄧㄎ) and `kwin: true` (AND-rule: both constituents' own kwin true) already matched constituents exactly — no bug. **Fixed non-standard homophone callout format** (was a bare "[!tip]" line) to the standard `>[!warning] Homophones` block on both this file and its reciprocal partner [[様式]] — confirmed the collision itself is genuine, matching pronunciation fields on both sides. Filled blank `vietnamese: dưỡng thực` — compositionally straightforward but not independently attested (native nuôi trồng is the actual term). Both character pages already cited 養殖 correctly. Stamped `date-last-perfect: 2026-09-08`.

Next: 養母.

### 2026-09-08, iteration 3620 — [[words/養母|養母]]
No cranberry (養's own `stand_in` is [[養育]], 母's is [[母親]] — neither points here). Pronunciation fields ('yangmou/양못/⼘ㄫㄇㄛㄨ) and `kwin: false` already matched constituents exactly — no bug. Both character pages already cited 養母 correctly. Filled blank `vietnamese: dưỡng mẫu` — confirmed real, standard, synonymous with the more everyday native mẹ nuôi. A clean case otherwise. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 養父.

### 2026-09-08, iteration 3621 — [[words/養父|養父]]
No cranberry (養's own `stand_in` is [[養育]], 父's is [[父親]] — neither points here). Pronunciation fields ('yangbu/양부/⼘ㄫㄅㄨ) and `kwin: true` (AND-rule: both constituents' own kwin true) already matched constituents exactly — no bug. Both character pages already cited 養父 correctly. Filled blank `vietnamese: dưỡng phụ` — confirmed real, standard formal/literary term (vs. everyday native cha nuôi). A clean case otherwise. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 養生.

### 2026-09-08, iteration 3622 — [[words/養生|養生]]
No cranberry (養's own `stand_in` is [[養育]], 生's is [[生活]] — neither points here). Pronunciation fields ('yangsang/양상/⼘ㄫㄙㄚㄫ) and `kwin: false` already matched constituents exactly — no bug. Both character pages already cited 養生 correctly. Filled blank `vietnamese: dưỡng sinh` — confirmed real, very common traditional-wellness term across all five languages (also used for concrete curing in Korean construction contexts). A clean case otherwise. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 養育.

### 2026-09-08, iteration 3623 — [[words/養育|養育]]
Legitimizing note added (養's own `stand_in` is [[養育]] itself, already annotated in its own citation; 育's own `stand_in` is 育 itself, so transitivity fails — no `#cranberry`). Pronunciation fields ('yang'yug/양육/⼘ㄫ⼜ㄎ) and `kwin: true` (AND-rule: both constituents' own kwin true) already matched constituents exactly — no bug. Both character pages already cited 養育 correctly. `vietnamese: dưỡng dục` was already correctly filled. A clean case otherwise — all real-language fields already correct standard words. Fixed `characters:`/`aliases:` flow-style formatting. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 餐.

### 2026-09-08, iteration 3624 — [[words/餐|餐]]
Legitimizing note added (this bare-character word is 餐's own legitimizer, `stand_in` points here). Pronunciation fields (can/찬/ㄑㄚㄋ) already matched the character's own stored values exactly. Added entirely missing `japanese: さん` (documenting native たべる as the everyday verb). Flattened `vietnamese` from a 3-item list (xan/san/xun) to the single representative `xan`, matching word-page convention (character pages document all attested forms; word pages pick one). **Fixed a malformed self-citation** on the character's own Words list (bare "[餐](words/餐.md)..." lacking ruby/bopomofo and the standard "(stand-in for 餐)" annotation format). Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found syllable-mates 燦/竄 but neither is itself a legitimized single-character word — no genuine collision.

Next: 餓鬼.

### 2026-09-08, iteration 3625 — [[words/餓鬼|餓鬼]]
No cranberry (餓's own `stand_in` is [[飢餓]], 鬼's is [[鬼神]] — neither points here). Pronunciation fields ('agui/아귀/ㄚㄍㄨㄧ) and `kwin: true` (AND-rule: both constituents' own kwin true) already matched constituents exactly — no bug. A clean case — all real-language fields (èguǐ/ngo6gwai2/がき/아귀/ngạ quỷ) already correct standard Buddhist terms. **In passing, added an entirely missing `## Words` section** to `characters/餓.md`, which had none at all (citing both [[飢餓]] with its "(stand-in for 餓)" annotation and 餓鬼). Fixed `characters:` flow-style formatting. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 饅頭.

### 2026-09-08, iteration 3626 — [[words/饅頭|饅頭]]
Legitimizing note added (饅's own `stand_in` is [[饅頭]] itself, already annotated in its own citation; 頭's own `stand_in` is 頭 itself, so transitivity fails — no `#cranberry`). Pronunciation fields (mantou/만톳/ㄇㄚㄋㄊㄛㄨ) and `kwin: false` already matched constituents exactly — no bug. **Found and fixed a real bug**: `japanese` had まんぢゆう, mixing the historical kana ぢ with an outright typo (big ゆ instead of small ゅ) — corrected to modern standard まんじゅう. Documented a genuine semantic divergence: Japanese まんじゅう usually means a filled sweet bun, Korean 만두 has diverged further to mean dumplings generally, while Mandarin/Cantonese/Vietnamese keep the plain-bun sense. **In passing, fixed a wrong "wonton" gloss** on `characters/頭 (char).md`'s citation of this exact word (should say "steamed bun"). Quoted `hsk_level`, removed blank `swadesh`/empty `aliases`. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 首尾.

### 2026-09-08, iteration 3627 — [[words/首尾|首尾]]
No cranberry (首's own `stand_in` is [[首長]], 尾's is 尾 itself — neither points here). Pronunciation fields (syumui/슈뮈/ㄙ⼜ㄇㄨㄧ) and `kwin: false` (AND-rule: both constituents' own kwin false) already matched constituents exactly — no bug. Verified `characters: [首, "尾 (char)"]` disambiguation was actually already correct (no `words/首.md` exists, so bare 首 is right; `words/尾.md` does exist, hence 尾's disambiguated citation). Both character pages already cited 首尾 correctly. Filled blank `vietnamese: thủ vĩ` — confirmed real literary/technical term (thủ vĩ tương ứng). Removed blank `hsk_level`/`swadesh`/empty `aliases`, consolidated Etymology into a proper `## Notes` section. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 首都.

### 2026-09-08, iteration 3628 — [[words/首都|首都]]
Re-perfected from an older stamp (`date-last-perfect: 2026-06-28`, pre-dating current conventions). Legitimizing note added (都's own `stand_in` is [[首都]] itself, already annotated in its own citation; 首's own `stand_in` is [[首長]], so transitivity fails — no `#cranberry`) — this was entirely missing from the existing Notes despite otherwise being a rich, well-written page. Pronunciation fields (syudo/슈도/ㄙ⼜ㄉㄛ) and `kwin: false` (AND-rule: 首 false, 都 true) already matched constituents exactly — no bug. `characters: [首, 都]` already correct (no `words/都.md` exists, so bare 都 is right). Both character pages already cited 首都 correctly. `vietnamese: thủ đô` already correctly filled. Left the page's existing detailed kwin-divergence paragraph intact (substantively correct, just an older stylistic convention). Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found a substring false-positive (受動's 注音 ㄙ⼜ㄉㄛㄫ merely starts with ㄙ⼜ㄉㄛ) — not a genuine collision.

Next: 首長.

### 2026-09-08, iteration 3629 — [[words/首長|首長]]
Already well-perfected (stamped 2026-08-30): legitimizing note for 首 (首's own `stand_in` is [[首長]] itself; 長's own `stand_in` is 長 itself, so transitivity fails — no `#cranberry`) already correctly documented in Notes. Pronunciation fields (syujang/슈장/ㄙ⼜ㄐㄚㄫ) and `kwin: false` (AND-rule: 首 false, 長 true) already matched constituents exactly — no bug. `characters: [首, "長 (char)"]` disambiguation already correct (`words/長.md` does exist, confirming 長's disambiguated citation is required). Existing homophone warning with [[手掌]] (both ㄙ⼜ㄐㄚㄫ) already correctly documented as a genuine coincidence between two unrelated real words. **Found and fixed a real gap**: `characters/長 (char).md`'s own `## Words` list was entirely missing a citation of 首長 despite 首長 being one of its two-character compounds — added. No changes needed to the word file itself; left `date-last-perfect` as-is since the word page itself required no edits (only the character page's citation gap was fixed).

Next: 首領.

### 2026-09-08, iteration 3630 — [[words/首領|首領]]
Re-perfected from an old stamp (`date-last-perfect: 2026-05-26`). No cranberry (首's own `stand_in` is [[首長]], 領's is [[領土]] — neither points here). Pronunciation fields (syuling/슈링/ㄙ⼜ㄌㄧㄫ) and `kwin: false` (AND-rule: both constituents' own kwin false) already matched constituents exactly — no bug. Both character pages already cited 首領 correctly. All real-language fields (shǒulǐng/sau2 ling5/しゅりょう/수령/thủ lĩnh) and the rich Notes on 수령's historical use as Kim Il-sung's title were already correct and well-written — left as-is. **Fixed minor formatting**: quoted `mandarin`/`cantonese`/`korean` for consistency with current convention (were bare unquoted scalars). Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found only an incidental mention in `lookup/Korean/Korea.md` (not a word/character page) — no genuine collision.

Next: 香気.

### 2026-09-08, iteration 3631 — [[words/香気|香気]]
Legitimizing note added (香's own `stand_in` is [[香気]] itself, already annotated in its own citation; 気's own `stand_in` is 気 itself, so transitivity fails — no `#cranberry`). Pronunciation fields (hyangkiǝ/향킈/ㄏ⼘ㄫㄎㄧㄜ) and `kwin: false` (AND-rule: 香 true, 気 false) already matched constituents exactly — no bug. `characters: [香, "気 (char)"]` disambiguation already correct (no `words/香.md` exists; `words/気.md` does). Both character pages already cited 香気 correctly. Filled blank `vietnamese: hương khí` — a real, if more literary/classical, Sino-Vietnamese term (everyday speech prefers native mùi hương/hương thơm). Removed blank `hsk_level`/`swadesh`, cleaned up a stray orphaned "positive connotation" fragment sitting outside any heading by writing it into a proper Notes sentence contrasting 香気 with neutral/negative smell-words. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 香港.

### 2026-09-08, iteration 3632 — [[words/香港|香港]]
No cranberry (香's own `stand_in` is [[香気]], 港's is [[港湾]] — neither points here). Pronunciation fields (hyanghong/향홍/ㄏ⼘ㄫㄏㄛㄫ) and `kwin: false` (AND-rule: 香 true, 港 false) already matched constituents exactly — no bug. Both character pages already cited 香港 correctly. **Investigated a suspected bug that turned out correct**: `korean: 향항` looked wrong at first (modern colloquial Korean says 홍콩) until cross-checking sibling toponym words [[北京]] (북경), [[東京]] (동경), [[上海]] (상해) confirmed this vault consistently records the classical/literary Sino-Korean hanja reading for CJK place names rather than the modern transliteration — documented this convention explicitly in Notes. `vietnamese: Hương Cảng` and `japanese: ホンコン` were already correctly filled. Removed blank `hsk_level`/`swadesh`/empty `aliases`, consolidated Etymology into a proper `## Notes` section. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 香芝.

### 2026-09-08, iteration 3633 — [[words/香芝|香芝]]
No cranberry (香's own `stand_in` is [[香気]], 芝's is the special `名専字` "name-only character" marker — neither points here). Pronunciation fields (hyangji/향지/ㄏ⼘ㄫㄐㄧ) and `kwin: true` (AND-rule: both constituents' own kwin true) already matched constituents exactly — no bug. Both character pages already cited 香芝 correctly. **Found and fixed a real bug**: `pos: 名詞` should be `固有名詞` (this is a proper-noun place name; cross-checked against sibling toponyms [[北京]], [[東京]], [[台湾]], [[上海]], [[香港]], all of which correctly use 固有名詞). Filled entirely missing `vietnamese: Hương Chi` (compositional Hán Việt, following the same always-fill convention already established for obscure toponyms like [[奈良]]'s Nại Lương). **Also fixed a wording slip** in the existing Notes ("The character 香芝 was added to the Jōyō kanji list" — should read "The character 芝", since 芝 alone is the late addition, not the two-character compound). Quoted `mandarin`/`cantonese`/`korean`. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 香蒲.

### 2026-09-08, iteration 3634 — [[words/香蒲|香蒲]]
Legitimizing note added (蒲's own `stand_in` is [[香蒲]] itself, already annotated in its own citation; 香's own `stand_in` is [[香気]], so transitivity fails — no `#cranberry`) — the existing Notes already said this substantively, just reworded to match current convention phrasing. Pronunciation fields (hyangbo/향보/ㄏ⼘ㄫㄅㄛ) and `kwin: false` (AND-rule: 香 true, 蒲 false) already matched constituents exactly — no bug. Both character pages already cited 香蒲 correctly. Filled entirely missing `vietnamese: hương bồ` — confirmed real, attested Sino-Vietnamese name for cattail/Typha. **Fixed formatting**: `mandarin: xiāng pú` had a stray space (should be a single joined pinyin string `xiāngpú` per convention); quoted `mandarin`/`cantonese`/`korean`. Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 香蕉.

### 2026-09-08, iteration 3635 — [[words/香蕉|香蕉]]
No cranberry (香's own `stand_in` is [[香気]], 蕉's is [[甘蕉]] — neither points here). Pronunciation fields (hyangjou/향좃/ㄏ⼘ㄫㄐㄛㄨ) and `kwin: false` (AND-rule: 香 true, 蕉 false) already matched constituents exactly — no bug. `japanese: バナナ`/`korean: 바나나` (English loanwords) already correctly reflect real-world usage rather than compositional readings — bananas being a later-introduced fruit in Japan/Korea with no felt need for the Sino compound, while Mandarin/Cantonese 香蕉/hoeng1ziu1 are the genuine native terms. **Found and fixed a real gap**: `characters/蕉.md`'s own `## Words` list was missing a citation of 香蕉 (had only [[甘蕉]], its actual `stand_in`) — added. Filled entirely missing `vietnamese: hương tiêu` (compositional Hán Việt; documented that everyday Vietnamese instead uses the native word chuối, paralleling the JA/KO divergence). Stamped `date-last-perfect: 2026-09-08`. Background exact-match homophone check found no collision.

Next: 馬.

### 2026-09-09, iteration 3636 — [[words/馬|馬]]
Already well-perfected (stamped 2026-09-04): stand-in note, pronunciation fields (ma/마/ㄇㄚ), `kwin: true` (matches character's own kwin), and the existing 3-way homophone warning with [[碼]]/[[磨]] were all already correct — verified both are themselves legitimized words (own `stand_in` = themselves) with exact-matching ma/마/ㄇㄚ, confirming the collision is genuine. **Found and fixed a real bug** on `characters/馬 (char).md`: its `aliases` field wrongly included 瑪 ("agate", unrelated meaning) and 碼 ("yard", already separately and correctly listed in Derived Characters) — aliases should only hold true orthographic variants of 馬 itself (kept 马, the genuine simplified form; removed the other two, which are phonetic derivatives, not variants). Checked 魔/麻/罵/媽 (all same ㄇㄚ syllable) for a broader collision — none are themselves legitimized words (`stand_in` points elsewhere for all four), so no additional homophone. No changes needed to the word page itself.

Next: 馬上.

### 2026-09-09, iteration 3637 — [[words/馬上|馬上]]
No cranberry (both 馬's and 上's own `stand_in` point to themselves — neither points here). Pronunciation fields (masyang/마샹/ㄇㄚㄙ⼘ㄫ) and `kwin: false` (AND-rule: 馬 true, 上 false) already matched constituents exactly — no bug. **Decoded a stray design note**: an orphaned "not "immediately"" fragment sitting outside any heading turned out to be a real, important scope note — 馬上 very commonly means "immediately, right away" in colloquial modern Mandarin, but this Dan'a'yo word deliberately excludes that idiomatic extension and keeps only the literal "horseback" sense; wrote this up properly in Notes. Filled entirely missing `vietnamese: mã thượng` (compositional; noted everyday Vietnamese prefers the native phrase trên lưng ngựa). **Found and fixed two real bugs on `characters/上 (char).md`**: (1) its own `## Words` list was missing a citation of 馬上 entirely — added; (2) its Classical-Chinese-frequency line was malformed, with the initial/final wikilinks (聲 禪, 韻 陽開) dangling bare outside any sentence instead of the standard "Nth most used character..." template — reconstructed using its own `mc_id: 29`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 馬厩.

### 2026-09-09, iteration 3638 — [[words/馬厩|馬厩]]
Legitimizing note added (厩's own `stand_in` is [[馬厩]] itself; 馬's own `stand_in` is 馬 itself, so transitivity fails — no `#cranberry`). Pronunciation fields (magyu/마규/ㄇㄚㄍ⼜) and `kwin: false` (AND-rule: 馬 true, 厩 false) already matched constituents exactly — no bug. **Investigated and explained a real divergence**: `korean: 마구간` doesn't match compositional 마구 — cross-referenced `characters/厩.md`'s own `korean_native: 마구간` field and the alias `馬廏間`, confirming the actual real Korean word for "stable" is structurally the longer compound 馬廏間, not bare 馬厩; documented this in Notes rather than treating it as a bug. Filled blank `cantonese: maa5 gau3` and entirely missing `vietnamese: mã cứu` (compositional; noted everyday Vietnamese prefers native chuồng ngựa). Fixed a stray space in `mandarin: mǎ jiù`→`mǎjiù`. **In passing, fixed `characters/厩.md`'s own citation** of 馬厩, which was missing its "(stand-in for 厩)" annotation despite 厩's own `stand_in` pointing there. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 馬来西亜.

### 2026-09-09, iteration 3639 — [[words/馬来西亜|馬来西亜]]
No cranberry (none of the four constituents' own `stand_in` points here). Pronunciation fields (malaisei'a/마래세아/ㄇㄚㄌㄚㄧㄙㄝㄧ·ㄚ) and `kwin: false` (AND-rule: 馬 true, 来 true, 西 false, 亜 true) already matched constituents exactly — no bug. `characters: ["馬 (char)", "来 (char)", 西, 亜]` disambiguation already correct (`words/来.md` exists; `words/西.md`/`words/亜.md` don't). All four character pages already cited 馬来西亜 correctly. All real-language fields (Mandarin's dual-tone variant, Cantonese, Japanese/Korean English-loanword transliterations, Vietnamese's dual phonetic/Sino-Vietnamese forms) were already correctly filled — a clean case. Removed blank `hsk_level`/`swadesh`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found only an incidental mention in `lexipedia/Geography.md` (not a word/character page) — no genuine collision.

Next: 馬脚.

### 2026-09-09, iteration 3640 — [[words/馬脚|馬脚]]
No cranberry (both 馬's and 脚's own `stand_in` point to themselves — neither points here). Pronunciation fields (magyag/마갹/ㄇㄚㄍ⼘ㄎ) and `kwin: false` (AND-rule: both constituents' own kwin false/true → false) already matched constituents exactly — no bug. **Found and fixed a real disambiguation bug**: `characters: [馬, 脚]` used bare names despite `words/馬.md` and `words/脚.md` both existing (confirmed by the Etymology section already correctly linking to the disambiguated "馬 (char)"/"脚 (char)" pages) — fixed to match. Both character pages already cited 馬脚 correctly. All real-language fields (mǎjiǎo/maa5goek3/ばきゃく/마각/mã cước) were already correct standard readings. Removed blank `hsk_level`/`swadesh`, consolidated Etymology into a proper `## Notes` section. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 馬蹄.

### 2026-09-09, iteration 3641 — [[words/馬蹄|馬蹄]]
No cranberry (both 馬's and 蹄's own `stand_in` point to themselves — neither points here). Pronunciation fields (madei/마데/ㄇㄚㄉㄝㄧ) and `kwin: false` (AND-rule: 馬 true, 蹄 false) already matched constituents exactly — no bug. **Fixed the same disambiguation bug pattern as the previous two words**: `characters: [馬, 蹄]` used bare names despite both `words/馬.md`/`words/蹄.md` existing. **Explained a real divergence**: `korean: 말굽` is a native Korean compound (말 "horse" + 굽 "hoof"), not the Sino-Korean reading 마제 (confirmed via 蹄's own `korean`/`korean_native` fields) — 말굽 is genuinely the everyday term, 마제 being confined to technical compounds like 마제형. Filled entirely missing `vietnamese: mã đề`, documenting a real semantic narrowing: it names the plantain herb (leaf shaped like a hoofprint), not "horse hoof" literally. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 馬𡿺.

### 2026-09-09, iteration 3642 — [[words/馬𡿺|馬𡿺]]
Legitimizing note added (𡿺's own `stand_in` is [[馬𡿺]] itself, already annotated in its own citation; 馬's own `stand_in` is 馬 itself, so transitivity fails — no `#cranberry`). **Found and fixed a significant real bug spanning multiple files**: `characters/𡿺.md`'s own `羅馬字`/`諺文`/`注音` (nuo/눗/ㄋㄨㄛ) were an outlier inconsistent with every other `middle_chinese_final: ɑu` character in the entire vault, all of which map to Dan'a'yo "-au" — including its own semantic siblings [[脳 (char)|脳]]/[[悩 (char)|悩]] ("brain"/"angered"), both nau/낫/ㄋㄚㄨ. Corrected to nau/낫/ㄋㄚㄨ, which cascaded into: this word's own `羅馬字`/`諺文`/`注音` (mano/마노/ㄇㄚㄋㄛ → manau/마낫/ㄇㄚㄋㄚㄨ); `characters/馬 (char).md`'s citation of this word; a stray reference on `syllables/ㄍㄚ.md`'s entry for [[珂]] (another pageless "agate" name-only character that also points here); moved 𡿺 itself from the now-empty syllable page `ㄋㄨㄛ` (rewritten to size 0) into `ㄋㄚㄨ` (now size 3). Removed a duplicate `品詞: 名詞` field (redundant with `pos: 名詞`). All five real-language fields (mǎnǎo/maa5nou5/마노/めのう/mã não) were already correctly filled with the real "agate" word's readings, distinct from the constructed Dan'a'yo pronunciation — the vault represents this word with the rare/hapax placeholder 𡿺 rather than the common 瑪瑙 orthography, whose many spelling variants are recorded as aliases. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check on the corrected reading found no collision (all hits were this word's own touched files).

Next: 馳.

### 2026-09-09, iteration 3643 — [[words/馳|馳]]
Self-standing bare-character word (own `stand_in` is 馳 itself). Pronunciation fields (cǝ/츠/ㄑㄜ) and `kwin: false` already matched the character's own stored values exactly — no bug. Existing homophone warning with [[此]] confirmed genuine (its own `stand_in` is 此 itself, exact-matching cǝ/츠/ㄑㄜ). **Found and fixed a real gap**: `japanese` was entirely missing from the word's frontmatter — added `ち` (on'yomi, matching the vault's default convention for bare-character words, e.g. [[気]] き, [[長]] ちょう). **Fixed a malformed self-citation** on `characters/馳 (char).md`'s Words list (bare, non-ruby "[馳](words/馳.md)..." format instead of the standard `<ruby>...(stand-in for 馳)` template). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check confirmed no additional collision beyond the already-documented 此.

Next: 馿.

### 2026-09-09, iteration 3644 — [[words/馿|馿]]
Self-standing bare-character word (own `stand_in` is 馿 itself). **Found and fixed a cluster of real bugs**: `korean: "null"` was a literal string bug (corrected to 려, the character's own stored value); `vietnamese: null` was likewise a literal-null bug (filled with lừa, the real everyday word for "donkey," documenting the character's other stored variant lư as the more literal/literary alternative); `characters: "馿 (char)"` was a bare string instead of a proper list; heading was `# Notes` (level 1) instead of `## Notes`; `pos`/`kwin`/`date-last-perfect` were all entirely missing. Added missing `japanese: ろ` (bare on'yomi, per default convention), documenting that real standalone Japanese instead uses the compound ロバ (roba, itself built from this character's own on'yomi + 馬). Checked the ㄌ⼄ syllable for a homophone: 慮/旅/呂/侶 all share this reading but none is itself a legitimized bare word — no collision.

Next: 駄.

### 2026-09-09, iteration 3645 — [[words/駄|駄]]
Self-standing bare-character word (own `stand_in` is 駄 itself). Existing homophone warning with [[舵]] confirmed genuine (its own `stand_in` is 舵 itself, exact-matching da/다/ㄉㄚ) — checked the full ㄉㄚ syllable set (朶/打/爹/駝/陀) for any other collision, none are themselves legitimized bare words. **Fixed the same bug cluster as the previous two words**: bare-string `characters:` instead of a list, `# Notes` heading level, missing `pos`/`kwin`/`date-last-perfect`. Added missing `japanese: だ` — **deliberately chose the second-listed on'yomi over the first** (TA, DA, TAI, DAI on the character page), since だ is the practically-attested reading (無駄, 駄目, 駄菓子) while た is essentially unused in real vocabulary, matching the precedent set by [[食]] (which similarly picked its third-listed reading じき over first-listed しょく for the correct standalone sense). Self-caught and fixed a subject/object reversal I introduced while rewriting the homophone warning line. Stamped `date-last-perfect: 2026-09-09`.

Next: 駅.

### 2026-09-09, iteration 3646 — [[words/駅|駅]]
Already well-perfected (stamped 2026-07-26): self-standing bare-character word, rich existing Notes on the 驛→駅 Japan-coined shinjitai narrowing and the cross-language "post station" vs. "modern station" divergence, and the existing homophone warning with [[䋇]] all confirmed correct — checked the full ⼶ㄎ syllable set (役/易/疫/液/訳), none are themselves legitimized bare words, so no additional collision. **Found and fixed a real bug**: duplicate `pos`/`品詞` fields (same recurring bug type as 馬𡿺 and 食). Re-stamped `date-last-perfect: 2026-09-09`.

Next: 駆.

### 2026-09-09, iteration 3647 — [[words/駆|駆]]
Self-standing bare-character word (own `stand_in` is 駆 itself). All real-language fields (qū/keoi1/く/구/xúi) already matched the character's own stored values exactly — no bug. Checked ㄎㄨ syllable-mate [[区]] for a homophone collision — not itself a legitimized bare word (`stand_in` points to [[区域]]), so none exists. **Fixed the recurring bug cluster**: duplicate `pos`/`品詞` fields (4th instance this session) and bare-string `characters:` instead of a list. Stamped `date-last-perfect: 2026-09-09`.

Next: 駆逐.

### 2026-09-09, iteration 3648 — [[words/駆逐|駆逐]]
No cranberry (駆's own `stand_in` is 駆 itself, 逐's is [[追逐]] — neither points here). Pronunciation fields (kudug/쿠둑/ㄎㄨㄉㄨㄎ) and `kwin: false` (AND-rule: both constituents' own kwin false) already matched constituents exactly — no bug. **Fixed the recurring `characters:` disambiguation bug**: bare "駆" despite `words/駆.md` existing (confirmed `words/逐.md` doesn't, so bare 逐 was already correct). Both character pages already cited 駆逐 correctly. All real-language fields (qūzhú/keoi1zuk6/くちく/구축/khu trục) already correct standard readings. Quoted `hsk_level`, removed blank `swadesh`/empty `aliases`, consolidated Etymology into a proper `## Notes` section. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found only a substring false-positive on 駆逐艦 — no genuine collision.

Next: 駆逐艦.

### 2026-09-09, iteration 3649 — [[words/駆逐艦|駆逐艦]]
No cranberry (none of the three constituents' own `stand_in` points here). Pronunciation fields (kudugham/쿠둑함/ㄎㄨㄉㄨㄎㄏㄚㄇ) and `kwin: false` (AND-rule: 駆 false, 逐 false, 艦 true → false) already matched constituents exactly — no bug. **Fixed the same recurring `characters:` disambiguation bug**: bare "駆" despite `words/駆.md` existing (confirmed `words/逐.md`/`words/艦.md` don't exist, so bare 逐/艦 were already correct). All three character pages already cited 駆逐艦 correctly. All real-language fields already correct standard readings. Removed blank `hsk_level`/`swadesh`, consolidated Etymology into a proper `## Notes` section. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 駐屯.

### 2026-09-09, iteration 3650 — [[words/駐屯|駐屯]]
Legitimizing note reworded to convention (駐's own `stand_in` is [[駐屯]] itself; 屯's own `stand_in` is 屯 itself, so transitivity fails — no `#cranberry`) — the existing Notes already said this substantively. Pronunciation fields (dudun/두둔/ㄉㄨㄉㄨㄋ) and `kwin: false` (AND-rule: 駐 false, 屯 true) already matched constituents exactly — no bug. `characters: [駐, "屯 (char)"]` disambiguation already correct (`words/駐.md` doesn't exist; `words/屯.md` does). Filled entirely missing `vietnamese: đồn trú` — a real, very common military/administrative term that reverses the Sino word order (屯-then-駐), joining the vault's small set of documented Vietnamese word-order-reversal cases ([[限定詞]], [[除外]]). **In passing, added a missing `đồn` reading** to `characters/屯 (char).md`'s own `vietnamese` list (previously only had `truân`). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 駝背.

### 2026-09-09, iteration 3651 — [[words/駝背|駝背]]
Already fully perfected (stamped 2026-07-27): legitimizing note for 駝 (its own `stand_in` is [[駝背]] itself; 背's is 背 itself, so no `#cranberry`), pronunciation fields (daboi/다뵈/ㄉㄚㄅㄛㄧ), `kwin: false` (AND-rule: both false), `characters:` disambiguation, both character-page citations, and an unusually thorough Notes section (already distinguishing 背's multiple Vietnamese reading candidates by sense, and noting Vietnamese đà bối as literary vs. everyday native gù) were all already correct. Background exact-match homophone check found no collision. No changes needed — left `date-last-perfect` untouched.

Next: 駱駝.

### 2026-09-09, iteration 3652 — [[words/駱駝|駱駝]]
Legitimizing note added (駱's own `stand_in` is [[駱駝]] itself; 駝's own `stand_in` is [[駝背]], so transitivity fails — no `#cranberry`). Pronunciation fields (lagda/락다/ㄌㄚㄎㄉㄚ), `kwin: false` (AND-rule: 駱 true, 駝 false), and `vietnamese`/`japanese` (lạc đà; らくだ, a rendaku-voiced compound) already matched constituents exactly — no bug there. **Found and fixed a real bug**: `korean: 낙타` used the South Korean 두음법칙-softened form instead of the North Korean compositional form 락타 (violating the vault's standing Korean-reading rule) — corrected, while documenting that 낙타 is what both character pages' `korean_native` fields cite as the universal real-world word. **Found and fixed two real citation gaps**: `characters/駝.md`'s own `## Words` list was entirely missing a citation of 駱駝 (added); `characters/駱.md`'s existing citation was missing its "(stand-in for 駱)" annotation despite 駱's own `stand_in` pointing there (added). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 騎乗.

### 2026-09-09, iteration 3653 — [[words/騎乗|騎乗]]
No cranberry (騎's own `stand_in` is [[騎馬]], 乗's is 乗 itself — neither points here). Pronunciation fields (guisung/귀숭/ㄍㄨㄧㄙㄨㄫ) and `kwin: false` (AND-rule: both constituents' own kwin false) already matched constituents exactly — no bug. Both character pages already cited 騎乗 correctly. **Found and investigated a systemic bug**: `pos: 動詞` — cross-checked the vault's own grammar documentation (`文法 - 05形態.md`), which defines a canonical four-way word-class system (名詞/性詞/事詞/固有名詞) and uses 動詞 only as a general linguistic term ("verb phrase," "verb morphology"), never as a frontmatter category; corrected to `事詞`, matching both constituent characters. **This same non-canonical `動詞` value appears on 181 other word files** — likely an older-era term never migrated to `事詞`; flagged as a bulk-cleanup candidate rather than something to keep hand-fixing one at a time. Fixed a stray space in `mandarin: qí chéng`→`qíchéng`. Filled entirely missing `vietnamese: kỵ thừa` (compositional; noted the everyday term is native cưỡi ngựa). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 騎馬.

### 2026-09-09, iteration 3654 — [[words/騎馬|騎馬]]
Legitimizing note reworded to convention (騎's own `stand_in` is [[騎馬]] itself; 馬's own `stand_in` is 馬 itself, so transitivity fails — no `#cranberry`) — the existing Notes already said this substantively. Pronunciation fields (guima/귀마/ㄍㄨㄧㄇㄚ) and `kwin: false` (AND-rule: 騎 false, 馬 true) already matched constituents exactly — no bug. Both character pages already cited 騎馬 correctly. **Fixed the same `pos: 動詞` bug as the previous word** — corrected to `事詞`, matching 騎's own `pos`. Flattened `vietnamese` from a single-item list to scalar `kị mã`, matching word-page convention. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 騒.

### 2026-09-09, iteration 3655 — [[words/騒|騒]]
Already well-perfected (stamped 2026-08-30): self-standing bare-character word, pronunciation fields (sau/삿/ㄙㄚㄨ), `kwin: false`, and the existing homophone warning with [[掻]] were all already correct — verified 掻's own `stand_in` points to itself, confirming the collision genuine. **Closed a gap the word's own Notes had explicitly flagged for later**: `characters/騒 (char).md`'s own `vietnamese` field was blank despite the word's Notes already documenting tao as the well-attested real Vietnamese reading — filled it in now rather than deferring further, since the answer was already established right here. Re-stamped `date-last-perfect: 2026-09-09`.

Next: 験.

### 2026-09-09, iteration 3656 — [[words/験|験]]
Self-standing bare-character word (own `stand_in` is 験 itself). Pronunciation fields ('em/엄/ㄝㄇ) and `kwin: false` already matched the character's own stored values exactly — no bug. Checked the ㄝㄇ syllable set (俺/炎) for a homophone — neither is itself a legitimized bare word, so none exists. **Found and fixed three real bugs on `characters/験 (char).md`**: (1) `japanese_native` was malformed YAML — a bare scalar あかし immediately followed by a misindented `- いさお` list item, rather than a proper two-item list; (2) its self-citation read "(stand-in for 験 (char))," wrongly including the filename-disambiguation suffix in the prose parenthetical, instead of the standard bare "(stand-in for 験)"; (3) the Classical-Chinese-frequency line was malformed exactly like the earlier `上 (char).md` case — dangling bare initial/final wikilinks instead of the standard "Nth most used character..." sentence — reconstructed using `mc_id: 1136`. Stamped `date-last-perfect: 2026-09-09`.

Next: 騙.

### 2026-09-09, iteration 3657 — [[words/騙|騙]]
Already fully perfected (stamped 2026-09-05): self-standing bare-character word, pronunciation fields (pyen/편/ㄆ⼶ㄋ), `kwin: true`, and the documented genuine 3-way homophone group with [[篇]]/[[偏]] were all already correct — verified both are themselves legitimized bare words with exact-matching readings. Character page citation format also already correct. No changes needed — a clean pass.

Next: 騰貴.

### 2026-09-09, iteration 3658 — [[words/騰貴|騰貴]]
Legitimizing note added (騰's own `stand_in` is [[騰貴]] itself; 貴's own `stand_in` is [[貴重]], so transitivity fails — no `#cranberry`). Pronunciation fields (dǝnggui/등귀/ㄉㄜㄫㄍㄨㄧ) and `kwin: true` (AND-rule: both constituents' own kwin true) already matched constituents exactly — no bug. Initially misread both constituent character pages' `vietnamese` fields as blank from a truncated grep, but a full re-read showed both already correctly filled (騰: dằng/đằng; 貴: quí) — filled the word's own entirely missing `vietnamese: đằng quí` accordingly, noting the everyday native alternative vật giá leo thang. **Fixed the recurring `pos: 動詞` bug on both this word and `characters/騰.md` itself** — the first character-page instance of this bug found so far, suggesting the bulk-cleanup scope extends beyond word files. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 驟雨.

### 2026-09-09, iteration 3659 — [[words/驟雨|驟雨]]
Legitimizing note reworded to convention (驟's own `stand_in` is [[驟雨]] itself; 雨's own `stand_in` is 雨 itself, so transitivity fails — no `#cranberry`) — the existing Notes already said this substantively. Pronunciation fields (sau'u/삿우/ㄙㄚㄨ·ㄨ) and `kwin: false` (AND-rule: 驟 false, 雨 true) already matched constituents exactly — no bug. `characters: [驟, "雨 (char)"]` disambiguation already correct. **Fixed the recurring duplicate `pos`/`品詞` bug.** **Found and fixed a real citation gap**: `characters/驟.md`'s own citation of 驟雨 was missing its "(stand-in for 驟)" annotation despite 驟's own `stand_in` pointing there. Filled entirely missing `vietnamese: sậu vũ` (compositional; noted the everyday native term mưa rào). Kept the existing rich Notes distinguishing 驟雨 from its near-synonym [[俄雨]] by intensity vs. brevity. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 骨.

### 2026-09-09, iteration 3660 — [[words/骨|骨]]
Already fully perfected (stamped 2026-08-03): self-standing bare-character word with an unusually thorough Notes section already documenting a real `kwin` bug fix (곧/GOD vs 골/GOL, the same MC-checked-coda-vs-Korean-liquid pattern as 月/越/舌) and the character's large anatomical compound family. Verified pronunciation fields, `kwin: false`, and the character page's self-citation format all still correct — no new issues found. No changes needed — a clean pass.

Next: 骨格.

### 2026-09-09, iteration 3661 — [[words/骨格|骨格]]
No cranberry (both 骨's and 格's own `stand_in` point to themselves — neither points here). Pronunciation fields (godgag/곧각/ㄍㄛㄊㄍㄚㄎ) already matched constituents exactly — no bug. `characters: ["骨 (char)", "格 (char)"]` disambiguation already correct (both `words/骨.md`/`words/格.md` exist). Both character pages already cited 骨格 correctly. **Fixed a real contamination bug**: `korean: "골격, 뼈대"` comma-joined the correct Sino compositional reading (골격) with an unrelated native synonym (뼈대, "bone-frame") — corrected to just 골격, matching the AND-rule concatenation. Filled entirely missing `vietnamese: cốt cách`, documenting a genuine figurative drift in everyday Vietnamese (now means "bearing, character" rather than literal skeleton). Removed blank `hsk_level`/`swadesh`/empty `aliases`. Added entirely missing `kwin: false`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found only an incidental mention in `lexipedia/Body.md` — no genuine collision.

Next: 骨盤.

### 2026-09-09, iteration 3662 — [[words/骨盤|骨盤]]
No cranberry (both 骨's and 盤's own `stand_in` point to themselves — neither points here). Pronunciation fields (godban/곧반/ㄍㄛㄊㄅㄚㄋ) already matched constituents exactly — no bug. `characters:` disambiguation already correct. Both character pages already cited 骨盤 correctly. **Found and fixed a real `kwin` bug**: was `true`, but the AND-rule requires both constituents' own kwin true — 骨's is false, giving the correct value `false`. Filled entirely missing `vietnamese: cốt bàn` (compositional; noted the everyday native term xương chậu). Removed blank `hsk_level`/`swadesh`/empty `aliases`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 骨肉.

### 2026-09-09, iteration 3663 — [[words/骨肉|骨肉]]
No cranberry (both 骨's and 肉's own `stand_in` point to themselves — neither points here). Pronunciation fields (godnug/곧눅/ㄍㄛㄊㄋㄨㄎ) and `kwin: false` (AND-rule: both constituents' own kwin false) already matched constituents exactly — no bug. Both character pages already cited 骨肉 correctly. All real-language fields (gǔròu/gwat1juk6/こつにく/골육/cốt nhục) already correct standard readings, paralleling the Biblical idiom already noted on [[骨]]. Quoted `hsk_level`, removed blank `swadesh`/empty `aliases`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found only substring hits on the longer chengyu 骨肉相連 — no genuine collision.

Next: 骨髄.

### 2026-09-09, iteration 3664 — [[words/骨髄|骨髄]]
Legitimizing note reworded to convention (髄's own `stand_in` is [[骨髄]] itself; 骨's own `stand_in` is 骨 itself, so transitivity fails — no `#cranberry`) — the existing Notes already said this substantively. Pronunciation fields (godsui/곧쉬/ㄍㄛㄊㄙㄨㄧ) and `kwin: false` (AND-rule: both false) already matched constituents exactly — no bug. `characters:` disambiguation already correct. **Found and fixed a real gap**: `characters/髄.md`'s existing citation of 骨髄 was missing its "(stand-in for 髄)" annotation despite 髄's own `stand_in` pointing there. All real-language fields already correct standard readings. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 骸骨.

### 2026-09-09, iteration 3665 — [[words/骸骨|骸骨]]
No cranberry (骸's own `stand_in` is [[死骸]], 骨's is 骨 itself — neither points here). Pronunciation fields (hyegod/혀곧/ㄏ⼶ㄍㄛㄊ) and `kwin: false` (AND-rule: both false) already matched constituents exactly — no bug. **Fixed the recurring `characters:` disambiguation bug**: bare "骨" despite `words/骨.md` existing (confirmed `words/骸.md` doesn't, so bare 骸 was already correct). Both character pages already cited 骸骨 correctly. Filled entirely missing `vietnamese: hài cốt` — confirmed the standard, everyday Vietnamese term for "remains/skeleton," already referenced in passing on [[骨]]'s own Notes. Removed blank `hsk_level`/`swadesh`/empty `aliases`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 高.

### 2026-09-09, iteration 3666 — [[words/高|高]]
Already fully perfected (stamped 2026-08-03): self-standing bare-character word with an unusually thorough Notes section — periodic-table prefix role for gallium (高素), a documented genuine phonetic-family homophone with [[稿]] (already cross-checked against all other ㄍㄚㄨ-reading characters), and the `japanese_native: ø`-despite-common-たかい gap already flagged as a known pattern (cf. 手/玉/飛). Verified pronunciation fields and `kwin: false` still match the character page exactly. No changes needed — a clean pass.

Next: 高人.

### 2026-09-09, iteration 3667 — [[words/高人|高人]]
No cranberry (both 高's and 人's own `stand_in` point to themselves — neither points here). Pronunciation fields (gaunin/갓닌/ㄍㄚㄨㄋㄧㄋ) and `kwin: false` (AND-rule: both false) already matched constituents exactly — no bug. `characters:` disambiguation already correct. **Found and fixed a real gap**: `japanese` was entirely blank — added こうじん (favoring the more common じん reading for 人-compounds like 個人/老人 over the Dan'a'yo-internal にん derivation). Filled entirely missing `vietnamese: cao nhân`. **Noted a large-scale formatting backlog**: `characters/人 (char).md`'s own `## Words` list has a ~35-item numbered stub sub-list (citations like "29. [[高人]]" lacking ruby/gloss) below its properly-formatted entries — fixed only the one entry relevant here (#29, 高人); the rest remains a bulk-cleanup candidate, not something to fix piecemeal. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 高句麗.

### 2026-09-09, iteration 3668 — [[words/高句麗|高句麗]]
Already fully perfected (stamped 2026-06-19): rich historical Notes on the Goguryeo–Baekje–Silla Three Kingdoms period and an explicit callout of the irregular Mandarin gōu-vs-jù reading exception (correctly noting Dan'a'yo doesn't follow it). Verified pronunciation fields (gaugule/갓구러/ㄍㄚㄨㄍㄨㄌㄝ), `kwin: false` (AND-rule: 高 false, 句 true, 麗 false), `characters:` disambiguation, and all three character-page citations — all already correct. No changes needed — a clean pass.

Next: 高山.

### 2026-09-09, iteration 3669 — [[words/高山|高山]]
No cranberry (both 高's and 山's own `stand_in` point to themselves — neither points here). Pronunciation fields (gausan/갓산/ㄍㄚㄨㄙㄚㄋ) and `kwin: false` (AND-rule: 高 false, 山 true) already matched constituents exactly — no bug. Both character pages already cited 高山 correctly. Filled entirely missing `vietnamese: cao sơn` — confirmed real, attested in the classical idiom cao sơn lưu thủy (高山流水, a metaphor for deep friendship). Kept the existing note distinguishing this from the unrelated Takayama place-name reading of the same two characters. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 高峰.

### 2026-09-09, iteration 3670 — [[words/高峰|高峰]]
Already fully perfected (stamped 2026-05-26): legitimizing note for 峰 (own `stand_in` is [[高峰]] itself, already annotated), an unusually thorough Notes section covering figurative/diplomatic extensions (高峰期, 高峰會議) and per-language native-vs-Sino register contrasts across all five languages. Verified pronunciation fields (gaufong/갓뽕/ㄍㄚㄨㄈㄛㄫ), `kwin: false` (AND-rule: both false), and both character-page citations all still correct. No changes needed — a clean pass.

Next: 高校.

### 2026-09-09, iteration 3671 — [[words/高校|高校]]
No cranberry (校's own `stand_in` is [[学校]], 高's is 高 itself — neither points here). Pronunciation fields (gauhyau/갓햣/ㄍㄚㄨㄏ⼘ㄨ) and `kwin: false` (AND-rule: both false) already matched constituents exactly — no bug (double-checked the ⼶/⼘-glide bopomofo notation against [[香気]]'s ㄏ⼘ㄫ pattern before concluding no mismatch). Both character pages already cited 高校 correctly. Filled entirely missing `vietnamese: cao hiệu` (compositional; noted the everyday native term trường trung học). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 高盧.

### 2026-09-09, iteration 3672 — [[words/高盧|高盧]]
Already fully perfected (stamped 2026-05-26): no cranberry (盧's own `stand_in` is the special `名専字` marker, 高's is 高 itself), rich historical Notes on Caesar's Gallic Wars already noting that modern Japanese/Korean prefer phonetic ガリア/갈리아 over the Sino-readings used here. Verified pronunciation fields (gaulo/갓로/ㄍㄚㄨㄌㄛ), `kwin: false` (AND-rule: 高 false, 盧 true), and both character-page citations all still correct. No changes needed — a clean pass.

Next: 高等.

### 2026-09-09, iteration 3673 — [[words/高等|高等]]
Already fully perfected (stamped 2026-07-11): no cranberry (both 高's and 等's own `stand_in` point to themselves), rich Notes already documenting a genuine Vietnamese semantic narrowing (cao đẳng → a specific junior-college tier, not the general "advanced" sense retained in Chinese/Japanese/Korean). Verified pronunciation fields (gaudung/갓둥/ㄍㄚㄨㄉㄨㄫ), `kwin: false` (AND-rule: both false), `characters:` disambiguation, and both character-page citations all still correct. No changes needed — a clean pass.

Next: 高素.

### 2026-09-09, iteration 3674 — [[words/高素|高素]]
Periodic-table neologism series (gallium): already correctly following the special convention — `mandarin`/`cantonese` (jiā/gaa1) give the avoided real element character 鎵/镓's own readings, not a compositional reading; `korean`/`japanese`/`vietnamese` (갈륨/ガリウム/gali) are the loanword element names; `kwin: false` correctly compares Dan'a'yo 갓소 against Korean 갈륨 (clearly different) rather than an AND-rule. Dan'a'yo pronunciation fields (gauso/갓소/ㄍㄚㄨㄙㄛ) still correctly follow normal compositional concatenation of 高+素. Both character pages already cited 高素 correctly. **Fixed a stale cross-reference**: the homophone note claimed [[告訴]] was "still unperfected," but it was stamped 2026-08-28, after this word's prior 2026-07-27 stamp — updated the wording and re-verified the collision is still genuine (exact-matching gauso/갓소/ㄍㄚㄨㄙㄛ). Stamped `date-last-perfect: 2026-09-09`.

Next: 高綿.

### 2026-09-09, iteration 3675 — [[words/高綿|高綿]]
No cranberry (both 高's and 綿's own `stand_in` point elsewhere — neither points here). Pronunciation fields (gaumyen/갓면/ㄍㄚㄨㄇ⼶ㄋ) already matched constituents exactly — no bug. Both character pages already cited 高綿 correctly. **Fixed the recurring duplicate `pos`/`品詞` bug**, added entirely missing `kwin: false` (AND-rule: 高 false, 綿 true). Filled entirely blank `korean`/`japanese` fields with the modern phonetic loanwords 캄보디아/カンボジア rather than a compositional Sino-reading — following the same real-name-over-compositional-reading pattern established on [[馬来西亜]]. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found only an incidental mention in `lexipedia/Geography.md` — no genuine collision.

Next: 高考.

### 2026-09-09, iteration 3676 — [[words/高考|高考]]
No cranberry (高's own `stand_in` is 高 itself, 考's is [[考慮]] — neither points here). Pronunciation fields (gaukau/갓캇/ㄍㄚㄨㄎㄚㄨ) already matched constituents exactly — no bug. Both character pages already cited 高考 correctly. **Fixed the recurring duplicate `pos`/`品詞` bug**, added missing `kwin: false` (AND-rule: 高 false, 考 false). Filled entirely blank `korean`/`japanese` with phonetic transliterations of Mandarin (가오카오/ガオカオ) rather than compositional Sino-readings — reasoned that Japanese likely avoids compositional こうこう specifically to prevent collision with [[高校]]'s own reading. Removed blank `swadesh`, consolidated Etymology into a proper `## Notes` section. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 高興.

### 2026-09-09, iteration 3677 — [[words/高興|高興]]
No cranberry (both 高's and 興's own `stand_in` point to themselves — neither points here). **Fixed a real romanization typo**: `羅馬字: gauhing` should be `gauhǝng` (興's own stored 羅馬字 uses the schwa ǝ, not "i") — the 諺文/注音 fields were already correct concatenations, only 羅馬字 had drifted. **Decoded a stray design note** ("platonic version of 興奮. Only J lacks this term!") into a proper Notes section: 高興 is a calm "glad, pleased" sense contrasting with the more intense [[興奮]] ("excited, aroused"), and Japanese genuinely lacks this compound as an attested word despite 興 having viable on'yomi — confirmed the character page's own blank `japanese` field is consistent with this, so left it blank rather than guessing a reading. Both character pages already cited 高興 correctly. Quoted `hsk_level`, removed blank `swadesh`/empty `aliases`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 高麗.

### 2026-09-09, iteration 3678 — [[words/高麗|高麗]]
Already fully perfected (stamped 2026-06-19): no cranberry (both 高's and 麗's own `stand_in` point elsewhere), exceptionally rich historical Notes on the Goryeo dynasty and its role as the direct source of the English exonym "Korea" (via Persian/Arab/Marco Polo transliterations). Verified pronunciation fields (gaule/갓러/ㄍㄚㄨㄌㄝ), `kwin: false` (AND-rule: both false), and both character-page citations all still correct. No changes needed — a clean pass.

Next: 鬚髯.

### 2026-09-09, iteration 3679 — [[words/鬚髯|鬚髯]]
**Found and fixed a real missed-cranberry bug**: both 鬚's and 髯's own `stand_in` point to [[鬚髯]] itself, and both characters' own meanings ("beard") are identical to each other and to the compound — full transitivity, a genuine `#cranberry` case that had gone untagged. Added `#cranberry`, added the missing "(stand-in for 鬚)" annotation on 鬚's own citation, and added this word to [[lookup/List of 連綿詞]] (native alliterative binome category), incrementing its `size` to 47. Pronunciation fields (sunom/수놈/ㄙㄨㄋㄛㄇ) and `kwin: false` (AND-rule: 鬚 true, 髯 false) already matched constituents exactly — no bug. Filled entirely missing `japanese: しゅぜん`/`vietnamese: tu nhiêm`. Noted 수염 (Korean) is both the compositional Sino-Korean reading and 鬚's own attested native gloss — a case where the Sino compound became the everyday word. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no genuine collision.

Next: 鬣.

### 2026-09-09, iteration 3680 — [[words/鬣|鬣]]
Already well-perfected (stamped 2026-09-03): self-standing bare-character word, pronunciation fields (lob/롭/ㄌㄛㄆ), `kwin: false`, and the existing homophone warning with [[獵]] all confirmed correct — verified 獵's own `stand_in` points to itself, exact-matching reading. Only fix was quoting `hsk_level: 無` for consistency. Stamped `date-last-perfect: 2026-09-09`.

Next: 鬼婆.

### 2026-09-09, iteration 3681 — [[words/鬼婆|鬼婆]]
No cranberry (鬼's own `stand_in` is [[鬼神]], 婆's is [[婆婆]] — neither points here). Pronunciation fields (guiba/귀바/ㄍㄨㄧㄅㄚ) already matched constituents exactly — no bug. Both character pages already cited 鬼婆 correctly. `japanese: おにばば` already correctly identified as a native kun'yomi folklore compound (Onibaba/Yamamba), not a Sino reading. Filled entirely missing `korean: 귀파`/`vietnamese: quỷ bà` (compositional) and added missing `kwin: false` (AND-rule: 鬼 true, 婆 false). Removed blank `hsk_level`/`swadesh`/empty `aliases`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found only a substring false-positive on 閨房 — no genuine collision.

Next: 鬼火.

### 2026-09-09, iteration 3682 — [[words/鬼火|鬼火]]
No cranberry (鬼's own `stand_in` is [[鬼神]], 火's is 火 itself — neither points here). Pronunciation fields (guihwa/귀화/ㄍㄨㄧㄏ⺢) already matched constituents exactly — no bug. Both character pages already cited 鬼火 correctly. `japanese: おにび` already correctly a native folklore compound, not Sino. Filled entirely missing `korean: 귀화`/`vietnamese: quỷ hỏa` (compositional; noted native alternative ma trơi) and missing `kwin: true` (AND-rule: both constituents' own kwin true). Removed blank `hsk_level`/`swadesh`/empty `aliases`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found only a substring false-positive on 帰還 — no genuine collision.

Next: 鬼神.

### 2026-09-09, iteration 3683 — [[words/鬼神|鬼神]]
Legitimizing note added (鬼's own `stand_in` is [[鬼神]] itself, already annotated in its own citation; 神's own `stand_in` is 神 itself, so transitivity fails — no `#cranberry`). Pronunciation fields (guisin/귀신/ㄍㄨㄧㄙㄧㄋ) and `kwin: true` (AND-rule: both constituents' own kwin true) already matched constituents exactly — no bug. Both character pages already cited 鬼神 correctly. **Fixed a real contamination bug**: `japanese: きじん, おにがみ` comma-joined two genuinely distinct real readings (on'yomi vs. native kun'yomi) in one field — picked きじん as the representative form, documenting おにがみ as the folkloric alternate in Notes rather than dropping it entirely. Filled entirely missing `vietnamese: quỷ thần` — confirmed real, common phrase ("ghosts and spirits"). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found only incidental prose/gloss mentions (神霊's Notes, Korean mnemonic lists) — no genuine collision.

Next: 鬼老.

### 2026-09-09, iteration 3684 — [[words/鬼老|鬼老]]
No cranberry (鬼's own `stand_in` is [[鬼神]], 老's is 老 itself — neither points here). Pronunciation fields (guilau/귀랏/ㄍㄨㄧㄌㄚㄨ) already matched constituents exactly — no bug. **Fixed the recurring `characters:` disambiguation bug**: bare "老" despite `words/老.md` existing. Both character pages already cited 鬼老 correctly. **Enriched the `english` gloss**: the alias 鬼佬 (gwai2lou2) is a well-known, extremely common Cantonese colloquial term for a Western foreigner, far more prevalent in real usage than the literal "male demon" sense — added "foreigner (Cantonese slang)" alongside the literal gloss and documented this in Notes. Filled entirely blank `japanese`/`korean`/`vietnamese` with compositional readings and missing `kwin: false`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 鬼金.

### 2026-09-09, iteration 3685 — [[words/鬼金|鬼金]]
Periodic-table neologism series (cobalt): already correctly following convention — `mandarin`/`cantonese` (gǔ/gu2) give the avoided real element character 钴's own readings; `korean`/`japanese`/`vietnamese` (코발트/コバルト/coban) are the loanword element names; `kwin: false` correctly compares Dan'a'yo 귀김 against Korean 코발트 (clearly different). Dan'a'yo pronunciation fields (guigim/귀김/ㄍㄨㄧㄍㄧㄇ) still correctly follow normal compositional concatenation of 鬼+金. 鬼's own character page already cites 鬼金 correctly (with a special note on its neologism role); `characters/金 (char).md` doesn't cite it, consistent with that character's already-documented, deliberately out-of-scope ~55+ file citation gap. Fixed the recurring duplicate `pos`/`品詞` bug and a stray trailing space in the `japanese` list item; flattened single-item `japanese`/`vietnamese` lists to scalars. Kept the unusually extensive, well-researched Notes on the Kobold/cobalt etymology intact. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found only an incidental mention in `lexipedia/Periodic Table.md` — no genuine collision.

Next: 魂.

### 2026-09-09, iteration 3686 — [[words/魂|魂]]
Self-standing bare-character word (own `stand_in` is 魂 itself). Pronunciation fields (hon/혼/ㄏㄛㄋ) and `kwin: true` already matched the character's own stored values exactly — no bug. Checked the full ㄏㄛㄋ syllable set (喧/昏/棍/婚/混) for a homophone — none are themselves legitimized bare words, so no collision. Flattened `vietnamese` from a 2-item list to scalar `hồn` (the standard modern form), matching word-page convention. Stamped `date-last-perfect: 2026-09-09`.

Next: 魂魄.

### 2026-09-09, iteration 3687 — [[words/魂魄|魂魄]]
Legitimizing note added (魄's own `stand_in` is [[魂魄]] itself, already annotated in its own citation; 魂's own `stand_in` is 魂 itself, so transitivity fails — no `#cranberry`) — this was the only real gap in an otherwise exceptionally rich, already-thorough Notes section covering classical hun/po cosmology, the *Suwen*'s three-hun-seven-po count, and per-language register contrasts (JA konpaku formal vs. tamashii vernacular; native Vietnamese hồn alone vs. the Sino calque). Pronunciation fields (honbag/혼박/ㄏㄛㄋㄅㄚㄎ) and `kwin: false` (AND-rule: 魂 true, 魄 false) already matched constituents exactly — no bug. Quoted `mandarin`/`cantonese`/`korean`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 魅惑.

### 2026-09-09, iteration 3688 — [[words/魅惑|魅惑]]
Legitimizing note reworded to convention (魅's own `stand_in` is [[魅惑]] itself; 惑's own `stand_in` is 惑 itself, so transitivity fails — no `#cranberry`) — the existing Notes already said this substantively. Pronunciation fields (miǝhog/믜혹/ㄇㄧㄜㄏㄛㄎ) and `kwin: false` (AND-rule: 魅 false, 惑 true) already matched constituents exactly — no bug. `characters:` disambiguation already correct. Both character pages already cited 魅惑 correctly. Filled entirely missing `vietnamese: mị hoặc` — confirmed real, standard Sino-Vietnamese term for "to charm, bewitch." Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 魏国.

### 2026-09-09, iteration 3689 — [[words/魏国|魏国]]
Legitimizing note added (魏's own `stand_in` is [[魏国]] itself, already annotated in its own citation; 国's own `stand_in` is [[国家]], so transitivity fails — no `#cranberry`). Pronunciation fields ('egog/어곡/ㄝㄍㄛㄎ) and `kwin: false` (AND-rule: both false) already matched constituents exactly — no bug. **Investigated and explained a real, deliberate divergence**: `japanese`/`korean`/`vietnamese` (ぎ/위/Ngụy) give only 魏's own bare reading, not a compositional reading of the full compound — confirmed this is because Chinese historical Three-Kingdoms-era states are conventionally referred to by their bare name alone (unlike modern nations, which take "-国"), documented in Notes. **In passing, fixed 魏's own citation**, which was missing its "(stand-in for 魏)" annotation. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 魏峨.

### 2026-09-09, iteration 3690 — [[words/魏峨|魏峨]]
No cranberry (魏's own `stand_in` is [[魏国]], 峨's is [[峨峨]] — neither points here). Pronunciation fields ('e'a/어아/ㄝㄚ) and `kwin: false` (AND-rule: 魏 false, 峨 true) already matched constituents exactly — no bug. Both character pages already cited 魏峨 correctly. Exceptionally rich existing Notes already explained a "Component + Translation" substitution for the out-of-character-set 巍 (from the *Analects*), and the Dan'a'yo-identity-vs-compound-reading divergence paralleling [[六楽]]/[[楽]] — left entirely intact. Only fixes were the recurring duplicate `pos`/`品詞` bug and quoting `mandarin`/`cantonese`/`korean`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 魏晋.

### 2026-09-09, iteration 3691 — [[words/魏晋|魏晋]]
No cranberry (魏's own `stand_in` is [[魏国]], 晋's is [[晋升]] — neither points here). Pronunciation fields ('ejin/어진/ㄝㄐㄧㄋ) already matched constituents exactly — no bug. **Found and fixed three real bugs on `characters/晋.md`**: (1) malformed `japanese` YAML with a zero-indent list item; (2) a literal empty-string `korean_native: ''`; (3) its own `## Words` list was entirely missing a citation of 魏晋 — added all three fixes. Filled entirely missing `japanese: ぎしん`/`korean: 위진`/`vietnamese: Ngụy Tấn` and `kwin: false` (AND-rule: 魏 false, 晋 true) — contrasted with [[魏国]]'s bare-reading convention, since this compound period-name (cf. 魏晋南北朝) is read compositionally rather than by bare state name. Fixed duplicate `pos`/`品詞` and a bare-string `aliases`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no genuine collision.

Next: 魑魅.

### 2026-09-09, iteration 3692 — [[words/魑魅|魑魅]]
Legitimizing note added (魑's own `stand_in` is [[魑魅]] itself; 魅's own `stand_in` is [[魅惑]], so transitivity fails — no `#cranberry`). Pronunciation fields (cimiǝ/치믜/ㄑㄧㄇㄧㄜ) and `kwin: false` (AND-rule: 魑 true, 魅 false) already matched constituents exactly — no bug. **Investigated and explained a real irregular reading**: `korean: 이매` doesn't match naive compositional 치매 — confirmed 이매 is the genuine, attested reading (surviving in the classical idiom 이매망량/魑魅魍魎), and noted 치매 would collide with modern Korean "dementia." **Found and fixed a real bug**: `hsk_level: "1"` was clearly wrong for this obscure literary term (neither constituent has hsk_level "1"; 魑's own is 無) — corrected to `"無"`. **Found and fixed a structural mislabeling**: `characters/魑.md` had no `## Words` section at all — its citation of the actual word 魑魅 was miscategorized under `## Chengyu` (alongside the genuine 4-character idiom 魑魅罔両) — split into a proper `## Words` section, and added the missing "(stand-in for 魑)" annotation. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found only substring hits on the longer chengyu — no genuine collision.

Next: 魔力.

### 2026-09-09, iteration 3693 — [[words/魔力|魔力]]
No cranberry (魔's own `stand_in` is [[魔鬼]], 力's is 力 itself — neither points here). Pronunciation fields (malig/마릭/ㄇㄚㄌㄧㄎ) and `kwin: false` (AND-rule: 魔 true, 力 false) already matched constituents exactly — no bug. Both character pages already cited 魔力 correctly. **Fixed a real contamination bug**: `japanese: まりょく, まりま` comma-joined the standard, correct compositional reading with a bogus second form that doesn't correspond to any of 魔's or 力's own listed readings — dropped まりま entirely. Filled entirely missing `vietnamese: ma lực` — confirmed real, common term. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 魔女.

### 2026-09-09, iteration 3694 — [[words/魔女|魔女]]
Already fully perfected (stamped 2026-05-20): no cranberry (both 魔's and 女's own `stand_in` point elsewhere), exceptionally rich Notes tracing the concept from classical Chinese 妖女/女巫 through Buddhist 魔羅 demonology to Japan's dual folkloric/魔法少女 traditions (Kiki's Delivery Service, Madoka Magica). Verified pronunciation fields (manǝ/마느/ㄇㄚㄋㄜ), `kwin: false` (AND-rule: 魔 true, 女 false), and both character-page citations all still correct. No changes needed — a clean pass.

Next: 魔羅.

### 2026-09-09, iteration 3695 — [[words/魔羅|魔羅]]
Already fully perfected (stamped 2026-05-20): no cranberry (both 魔's and 羅's own `stand_in` point elsewhere), exceptionally rich Notes on Māra's assault on the Buddha under the Bodhi tree, the earth-touching gesture, and the Japanese Heian-era semantic shift to anatomical slang (independently preserved across Ryukyuan dialects). Verified pronunciation fields (malo/마로/ㄇㄚㄌㄛ), `kwin: false` (AND-rule: 魔 true, 羅 false), and both character-page citations all still correct. No changes needed — a clean pass.

Next: 魔銅.

### 2026-09-09, iteration 3696 — [[words/魔銅|魔銅]]
Periodic-table neologism series (nickel): `mandarin`/`cantonese` (niè/nip6) give the avoided real element character 鎳/镍's own readings; `korean`/`japanese`/`vietnamese` (니켈/ニッケル/nikel) are the loanword element names; `kwin: false` correctly compares Dan'a'yo 마동 against Korean 니켈 (clearly different). Dan'a'yo pronunciation fields (madong/마동/ㄇㄚㄉㄛㄫ) still correctly follow normal compositional concatenation of 魔+銅. Both character pages already cited 魔銅 correctly. Fixed the recurring duplicate `pos`/`品詞` bug; flattened single-item `japanese`/`vietnamese` lists to scalars. Kept the well-researched Notes on the Kupfernickel/"nick" folklore etymology intact. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found only an incidental mention in `lexipedia/Periodic Table.md` — no genuine collision.

Next: 魔鬼.

### 2026-09-09, iteration 3697 — [[words/魔鬼|魔鬼]]
Legitimizing note added (魔's own `stand_in` is [[魔鬼]] itself, already annotated in its own citation; 鬼's own `stand_in` is [[鬼神]], so transitivity fails — no `#cranberry`). Pronunciation fields (magui/마귀/ㄇㄚㄍㄨㄧ) and `kwin: true` (AND-rule: both constituents' own kwin true) already matched constituents exactly — no bug. Both character pages already cited 魔鬼 correctly. All real-language fields (móguǐ/mo1gwai2/まき/마귀/ma quỉ) already correct standard readings. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found only incidental prose mentions (e.g. 烏鳥's Korean gloss 까마귀 containing "마귀" as a substring) — no genuine collision.

Next: 魚.

### 2026-09-09, iteration 3698 — [[words/魚|魚]]
Self-standing bare-character word, already richly perfected (stamped 2026-06-29) with a detailed kwin explanation (Dan'a'yo 요 vs Korean 어, the MC 魚韻→-o correspondence also seen in [[且]]). **Found and fixed a real gap — a previously undocumented 3-way homophone cluster**: checked the full ⼄ syllable set and found [[与]] ("and, with") and [[輿]] ("palanquin") are BOTH themselves legitimized self-standing bare words with the exact same reading 'yo/요/⼄, yet none of the three pages had ever documented this collision. Added full reciprocal `>[!warning] Homophones` callouts to all three. Checked the remaining ⼄-reading characters (余/予/漁/圄/御/語/誉/馭) — none is itself a self-standing word, confirming the cluster is exactly these three. **In passing**, fixed a duplicate `pos`/`品詞` bug and flow-style `characters:` on 与.md, and fixed 輿.md's `# Notes` heading level and bare-string `characters:` field (its other gaps — missing `kwin`/`date-last-perfect` — left for when the sweep naturally reaches it). Fixed the duplicate `pos`/`品詞` bug on 魚.md itself. Re-stamped `date-last-perfect: 2026-09-09`.

Next: 魚叉.

### 2026-09-09, iteration 3699 — [[words/魚叉|魚叉]]
No cranberry (need not check — neither 魚's nor 叉's own `stand_in` points here). Pronunciation fields ('yocai/요채/⼄ㄑㄚㄧ) and `kwin: false` (AND-rule: both false) already matched constituents exactly — no bug. Rich existing Notes on harpoon history (Paleolithic origins, Svend Foyn's 1864 cannon) and the 漁叉/魚叉 written-form variance kept intact. **Fixed a malformed citation** on `characters/叉 (char).md` (bare asterisk-bullet "* [[魚叉]] harpoon" instead of the standard ruby template). Filled entirely missing `japanese: ぎょさ`/`vietnamese: ngư xoa`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 魚翅.

### 2026-09-09, iteration 3700 — [[words/魚翅|魚翅]]
Legitimizing note reworded to convention (翅's own `stand_in` is [[魚翅]] itself; 魚's own `stand_in` is 魚 itself, so transitivity fails — no `#cranberry`) — the existing Notes already said this substantively. Pronunciation fields ('yosi/요시/⼄ㄙㄧ) already matched constituents exactly — no bug. Both character pages already cited 魚翅 correctly. Added missing `kwin: false` (AND-rule: 魚 false, 翅 true) and filled entirely missing `vietnamese: ngư sí`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found only substring false-positives (標識/灰色/鼠色, all longer readings) — no genuine collision.

Next: 魚雷.

### 2026-09-09, iteration 3701 — [[words/魚雷|魚雷]]
No cranberry (both 魚's and 雷's own `stand_in` point to themselves — neither points here). Pronunciation fields ('yoloi/요뢰/⼄ㄌㄛㄧ) and `kwin: false` (AND-rule: 魚 false, 雷 true) already matched constituents exactly — no bug. Both character pages already cited 魚雷 correctly. All real-language fields already correct standard readings — a clean case. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 魚類.

### 2026-09-09, iteration 3702 — [[words/魚類|魚類]]
No cranberry (魚's own `stand_in` is 魚 itself, 類's is [[種類]] — neither points here). Pronunciation fields ('yolui/요뤼/⼄ㄌㄨㄧ) and `kwin: false` (AND-rule: both false) already matched constituents exactly — no bug. **Fixed a real contamination bug**: `mandarin: "yúlèi ; hû-luī"` had a Southern Min/Taiwanese Hokkien romanization (POJ-style "hû-luī") jammed into the Mandarin field entirely — removed, keeping just yúlèi. Filled blank `cantonese: jyu4 leoi6` and missing `vietnamese: ngư loại`. **In passing, fixed a real citation gap**: `characters/魚 (char).md`'s own Words list was missing 魚類 entirely — added. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found only a substring false-positive on 鼠類 — no genuine collision.

Next: 魚鰭.

### 2026-09-09, iteration 3703 — [[words/魚鰭|魚鰭]]
Legitimizing note reworded to convention (鰭's own `stand_in` is [[魚鰭]] itself; 魚's own `stand_in` is 魚 itself, so transitivity fails — no `#cranberry`) — the existing Notes already said this substantively. Pronunciation fields ('yogiǝ/요긔/⼄ㄍㄧㄜ) and `kwin: false` (AND-rule: both false) already matched constituents exactly — no bug. Both character pages already cited 魚鰭 correctly. Filled entirely missing `vietnamese: ngư kì`. Quoted `mandarin`/`cantonese`/`korean`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 魶.

### 2026-09-09, iteration 3704 — [[words/魶|魶]]
Self-standing bare-character word (own `stand_in` is 魶 itself). **Found and fixed a real bug**: `mandarin: dàní` was a two-syllable reading belonging to 大鯢 (the actual modern Mandarin word for "giant salamander") rather than 魶's own single-character reading — corrected to `nà` per the character page, documenting in Notes that 魶 itself is obsolete in Standard Chinese and modern usage universally prefers 大鯢. Filled blank `cantonese: naap6`; left `vietnamese` blank since the character page's own field is explicitly marked `ø` (no attested reading), not merely absent. Fixed the recurring duplicate `pos`/`品詞` bug and bare-string `characters:`. Checked the ㄋㄨㄆ syllable for a homophone — 魶 is the sole occupant, none found. Stamped `date-last-perfect: 2026-09-09`.

Next: 鮎.

### 2026-09-09, iteration 3705 — [[words/鮎|鮎]]
Already well-perfected (stamped 2026-09-05): self-standing bare-character word, pronunciation fields (nem/넘/ㄋㄝㄇ), `kwin: false`, and the existing homophone warning with [[粘]] all confirmed correct — verified 粘's own `stand_in` points to itself, exact-matching reading. Notes already correctly document Japanese's unique semantic divergence to あゆ ("sweetfish") vs. the original Chinese catfish/sheatfish sense. No changes needed.

Next: 鮑.

### 2026-09-09, iteration 3706 — [[words/鮑|鮑]]
Self-standing bare-character word. Pronunciation fields (bau/밧/ㄅㄚㄨ) and `kwin: false` already matched the character's own stored values exactly — no bug. **Found a real homophone already anticipated by its counterpart**: `words/報.md` already carried a homophone warning for 鮑 (added when 報 was perfected earlier this sweep, correctly flagging 鮑 as "still unperfected") — added the reciprocal warning here now that 鮑 is done, and fixed the now-stale "still unperfected" phrasing on 報.md. Checked the remaining ㄅㄚㄨ-reading characters (抱/堡/保/宝) — none is itself a legitimized bare word, confirming the cluster is exactly 鮑/報. Fixed duplicate `pos`/`品詞`, bare-string `characters:`, and flattened a 3-item `vietnamese` list to scalar `bào`. Stamped `date-last-perfect: 2026-09-09`.

Next: 鮫魚.

### 2026-09-09, iteration 3707 — [[words/鮫魚|鮫魚]]
Legitimizing note added (鮫's own `stand_in` is [[鮫魚]] itself, already annotated in its own citation; 魚's own `stand_in` is 魚 itself, so transitivity fails — no `#cranberry`). **Fixed a real romanization typo**: `羅馬字: gyau'yo` should be `gyou'yo` (鮫's own stored 羅馬字 uses "gyou," not "gyau") — the 諺文/注音 fields were already correct. **Fixed the recurring `characters:` disambiguation bug**: bare "魚" despite `words/魚.md` existing. Fixed a stray space in `mandarin: jiāo yú`→`jiāoyú`. Filled blank `cantonese: gaau1 jyu4`/`vietnamese: giao ngư` (compositional; `japanese: さめ` already correctly the native everyday word). **Investigated and removed an unverifiable stray claim** ("homophone of *make*") — checked exact-match candidates including [[交]] (shares 鮫's own partial reading, not the full compound's) and found nothing that confirms it. Self-caught and fixed a stray "英語:" field I accidentally introduced while rewriting. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no genuine collision.

Next: 鮮少.

### 2026-09-09, iteration 3708 — [[words/鮮少|鮮少]]
No cranberry (鮮's own `stand_in` is [[新鮮]], 少's is 少 itself — neither points here). Pronunciation fields (syensou/션솟/ㄙ⼶ㄇㄙㄛㄨ) already matched constituents exactly — no bug. **Clarified `pos: 実詞` is NOT a bug** — cross-checked the vault's own grammar docs (`文法 - 04句法.md`, `文法 - 97品詞.md`), which establish 実詞 as the legitimate umbrella "content word" category (encompassing 名詞/事詞/性詞/系詞), distinct from the earlier-confirmed non-canonical `動詞`; verified via a 310-file scope check that 実詞 is a well-established, intentional frontmatter value, not an artifact — left unchanged. `characters:` disambiguation already correct. Both character pages already cited 鮮少 correctly. Added missing `kwin: false` (AND-rule: both false) and filled blank `korean: 선소`/`vietnamese: tiên thiểu`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no genuine collision.

Next: 鮮美.

### 2026-09-09, iteration 3709 — [[words/鮮美|鮮美]]
No cranberry (鮮's own `stand_in` is [[新鮮]], 美's is 美 itself — neither points here). **Found and fixed a real bug**: `羅馬字`/`諺文` were syenmi/션미, an unexplained -n substitution for 鮮's own -m coda, inconsistent with the word's own `注音` field (ㄙ⼶ㄇㄇㄧ, already correctly showing -m) — corrected to syemmi/셤미 to match straightforward concatenation. `kwin: false` (AND-rule: 鮮 false, 美 true) already correct. Both character pages already cited 鮮美 correctly. Filled entirely missing `vietnamese: tiên mĩ`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check on the corrected reading found no collision.

Next: 鮮花.

### 2026-09-09, iteration 3710 — [[words/鮮花|鮮花]]
No cranberry (鮮's own `stand_in` is [[新鮮]], 花's is [[草花]] — neither points here). **Fixed the same systematic bug found on this word's siblings**: `羅馬字`/`諺文` had the same -n-for-鮮's-own-m substitution as [[鮮少]] and [[鮮美]] — corrected to syemhwa/셤화, matching `注音`. **Went back and fixed [[鮮少]] too**: caught only now that all three 鮮-prefixed words were checked side by side, its own syensou/션솟 (from iteration 3708, logged as already-correct at the time) actually had the identical bug — self-corrected. Confirmed via a vault-wide check that no other word uses 鮮 as its first constituent, so the bug is now fully resolved across all three affected files. **Fixed a malformed citation** on `characters/花.md` (bare "- [[鮮花]]" with no ruby/gloss). Filled entirely missing `vietnamese: tiên hoa`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 鯖魚.

### 2026-09-09, iteration 3711 — [[words/鯖魚|鯖魚]]
Legitimizing note added (鯖's own `stand_in` is [[鯖魚]] itself, already annotated in its own citation; 魚's own `stand_in` is 魚 itself, so transitivity fails — no `#cranberry`). Pronunciation fields (ceng'yo/청요/ㄑㄝㄫ⼄) and `kwin: false` (AND-rule: 鯖 true, 魚 false) already matched constituents exactly — no bug. Fixed the recurring `characters:` disambiguation bug (bare "魚" despite `words/魚.md` existing) and a typo in `english` (mackrel→mackerel). `japanese`/`korean`/`vietnamese` (さば/고등어/cá thu) already correctly the real native everyday words rather than Sino readings. Both character pages already cited 鯖魚 correctly. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 鯤魚.

### 2026-09-09, iteration 3712 — [[words/鯤魚|鯤魚]]
Already well-perfected (stamped 2026-06-06): legitimizing note for 鯤 (own `stand_in` is [[鯤魚]] itself, already annotated), rich Notes on the Zhuangzi's 鯤-鵬 transformation parable. Verified pronunciation fields (gon'yo/곤요/ㄍㄛㄋ⼄), `kwin: false` (AND-rule: 鯤 true, 魚 false), and both character-page citations all still correct. Only fix was quoting `mandarin`/`cantonese`/`korean`. Re-stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no genuine collision.

Next: 鯨魚.

### 2026-09-09, iteration 3713 — [[words/鯨魚|鯨魚]]
Already fully perfected (stamped 2026-08-30): legitimizing note for 鯨, `japanese: くじら` already correctly the native word, and the homophone warning with [[敬語]] already confirmed genuine (verified again: exact-matching gyeng'yo/경요/ㄍ⼶ㄫ⼄). Verified pronunciation fields and `kwin: false` (AND-rule: 鯨 true, 魚 false) still correct. No changes needed — a clean pass.

Next: 鰌魚.

### 2026-09-09, iteration 3714 — [[words/鰌魚|鰌魚]]
Legitimizing note already substantively documented (鰌's own `stand_in` is [[鰌魚]] itself). **Found and fixed a real gap**: `characters/鰌.md`'s own citation of 鰌魚 was missing its "(stand-in for 鰌)" annotation despite 鰌's own `stand_in` pointing there. Pronunciation fields (cuyo/추요/ㄑㄨ⼄) and `kwin: false` (AND-rule: 鰌 true, 魚 false) already matched constituents exactly — no bug. Exceptionally rich existing Notes on the loach's barometric-sensitivity folklore, Edo-period 柳川鍋/どじょう-ya culture, and Korean 추어탕/Jeolla regional cuisine kept fully intact. Quoted `mandarin`/`cantonese`/`korean`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 鰐梨.

### 2026-09-09, iteration 3715 — [[words/鰐梨|鰐梨]]
No cranberry (鰐's own `stand_in` is [[鰐魚]], 梨's is 梨 itself — neither points here). Pronunciation fields ('agliǝ/악릐/ㄚㄎㄌㄧㄜ) and `kwin: false` (AND-rule: 鰐 true, 梨 false) already matched constituents exactly — no bug. `characters:` disambiguation already correct. Both character pages already cited 鰐梨 correctly. **Fixed a likely-wrong real-language field**: `japanese: ワニナシ` (a literal "alligator-pear" calque) was swapped for アボカド, the overwhelmingly dominant real modern Japanese word — matching Korean's already-correct loanword 아보카도. Filled entirely missing `vietnamese: bơ` (native, from French *beurre*, "butter"). Removed blank `hsk_level`/`swadesh`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 鰐魚.

### 2026-09-09, iteration 3716 — [[words/鰐魚|鰐魚]]
Legitimizing note added (鰐's own `stand_in` is [[鰐魚]] itself, already annotated in its own citation; 魚's own `stand_in` is 魚 itself, so transitivity fails — no `#cranberry`). Pronunciation fields ('ag'yo/악요/ㄚㄎ·⼄) and `kwin: false` (AND-rule: 鰐 true, 魚 false) already matched constituents exactly — no bug. **In passing, fixed 鰐's own citation**, which was missing its "(stand-in for 鰐)" annotation. Filled entirely missing `vietnamese: ngạc ngư` (compositional; noted native cá sấu). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 鱏.

### 2026-09-09, iteration 3717 — [[words/鱏|鱏]]
Self-standing bare-character word (own `stand_in` is 鱏 itself). Pronunciation fields (him/힘/ㄏㄧㄇ) and `kwin: false` already matched the character's own stored values exactly — no homophone. **Fixed a real bug**: `pos`/`品詞` were both entirely blank (duplicate empty fields) — consolidated to a single `pos: 名詞`, matching the character page. Filled entirely missing `vietnamese: tầm`. Stamped `date-last-perfect: 2026-09-09`.

Next: 鱗.

### 2026-09-09, iteration 3718 — [[words/鱗|鱗]]
Self-standing bare-character word. **Found and fixed a real gap — a previously undocumented homophone**: checked the full ㄌㄧㄋ syllable set and found [[隣]] ("neighbor") is itself a legitimized self-standing bare word with the exact same reading lin/린/ㄌㄧㄋ, yet neither page had ever documented this collision (checked 吝/燐/麟 too — none is self-standing, confirming the cluster is exactly these two). Added reciprocal `>[!warning] Homophones` callouts to both. Fixed duplicate `pos`/`品詞` and a bare-string `characters:` field. Stamped `date-last-perfect: 2026-09-09`.

Next: 鳥.

### 2026-09-09, iteration 3719 — [[words/鳥|鳥]]
Self-standing bare-character word, already richly perfected with a detailed kwin explanation (Dan'a'yo 촛 vs Korean 조, the shared MC 端母+蕭韻 palatalization with different aspiration/diphthong outcomes). Checked the full ㄑㄛㄨ syllable set (招/湊/彫/釣/取) for a homophone — none is itself a legitimized bare word, so none exists. Only fix was the recurring duplicate `pos`/`品詞` bug. Re-stamped `date-last-perfect: 2026-09-09`.

Next: 鳥嘴.

### 2026-09-09, iteration 3720 — [[words/鳥嘴|鳥嘴]]
Legitimizing note added (嘴's own `stand_in` is [[鳥嘴]] itself, already annotated in its own citation; 鳥's own `stand_in` is 鳥 itself, so transitivity fails — no `#cranberry`). Pronunciation fields (coucui/촛취/ㄑㄛㄨㄑㄨㄧ) and `kwin: false` (AND-rule: 鳥 false, 嘴 true) already matched constituents exactly — no bug. `japanese: くちばし`/`korean: 부리` already correctly the real native everyday words, matching 嘴's own `japanese_native`/`korean_native` fields exactly. **In passing, fixed a real gap**: `characters/嘴.md`'s own citation of 鳥嘴 was missing its "(stand-in for 嘴)" annotation. Filled entirely missing `vietnamese: điểu chuỷ` (compositional; noted native mỏ). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found only an incidental mention in `lexipedia/Body.md` — no genuine collision.

Next: 鳥巣.

### 2026-09-09, iteration 3721 — [[words/鳥巣|鳥巣]]
Legitimizing note added (巣's own `stand_in` is [[鳥巣]] itself, already annotated in its own citation; 鳥's own `stand_in` is 鳥 itself, so transitivity fails — no `#cranberry`). Pronunciation fields (coujau/촛잣/ㄑㄛㄨㄐㄚㄨ) already matched constituents exactly — no bug. **Fixed a real contamination bug**: `korean: 둥지, 새집` comma-joined two native synonyms — kept 둥지 (standard), moved 새집 to prose. **Fixed a real semantic-mismatch bug**: `vietnamese: làm tổ` was a verb phrase ("to build a nest") rather than the noun this word actually is — corrected to tổ chim. Filled blank `cantonese: niu5 caau4` and added missing `kwin: false` (AND-rule: both false). Removed blank `hsk_level`/`swadesh`/empty `aliases`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 鳥籠.

### 2026-09-09, iteration 3722 — [[words/鳥籠|鳥籠]]
No cranberry (both 鳥's and 籠's own `stand_in` point to themselves — neither points here). Pronunciation fields (coulong/촛롱/ㄑㄛㄨㄌㄛㄫ) and `kwin: false` (AND-rule: 鳥 false, 籠 true) already matched constituents exactly — no bug. `characters:` disambiguation already correct. Both character pages already cited 鳥籠 correctly. `japanese: とりかご`/`korean: 새장` already correctly native compounds. Filled entirely missing `vietnamese: lồng chim` — a real, reversed-word-order term, a 4th confirmed instance of the Vietnamese reversal pattern. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 鳥類.

### 2026-09-09, iteration 3723 — [[words/鳥類|鳥類]]
No cranberry (鳥's own `stand_in` is 鳥 itself, 類's is [[種類]] — neither points here). Pronunciation fields (coului/촛뤼/ㄑㄛㄨㄌㄨㄧ) and `kwin: false` (AND-rule: both false) already matched constituents exactly — no bug. Both character pages already cited 鳥類 correctly. Filled entirely missing `vietnamese: điểu loại`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no genuine collision.

Next: 鳩鳥.

### 2026-09-09, iteration 3724 — [[words/鳩鳥|鳩鳥]]
Legitimizing note added (鳩's own `stand_in` is [[鳩鳥]] itself; 鳥's own `stand_in` is 鳥 itself, so transitivity fails — no `#cranberry`). Pronunciation fields (kyucou/큐촛/ㄎ⼜ㄑㄛㄨ) and `kwin: false` (AND-rule: both false) already matched constituents exactly — no bug. **Found and fixed a cluster of real bugs**: `mandarin: jiū` was missing 鳥's own reading entirely (corrected to jiūniǎo); `cantonese` comma-joined an unexplained extra "kau1" and was missing 鳥's own niu5 (corrected to gau1 niu5); `japanese` comma-joined the correct はと with an unrecognizable "きう" matching neither of 鳩's own on'yomi (dropped); `vietnamese` was over-specified "domestic pigeon" relative to this word's plain sense (simplified to bồ câu). **Also fixed `characters/鳩.md` itself**: its own `## Words` list was missing a citation of 鳩鳥 entirely, the [[狙鳩]] entry had no ruby/gloss, [[斑鳩]] used an inconsistent asterisk bullet, and its Classical-Chinese-frequency line was the same dangling-bare-wikilinks bug seen before — all reformatted/reconstructed. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 鳳凰.

### 2026-09-09, iteration 3725 — [[words/鳳凰|鳳凰]]
Already fully perfected (stamped 2026-06-27) and correctly tagged `#cranberry` — verified both 鳳's and 凰's own `stand_in` point to [[鳳凰]] itself, confirming genuine transitivity for this "dead paired-gender" compound, matching its own listed category on `lookup/List of 連綿詞`. Rich existing Notes on the Shangshu/Zuozhuan omen tradition and the 龍鳳 imperial pairing kept intact. **Found and fixed a real gap**: `characters/凰.md`'s own citation of 鳳凰 was missing its "(stand-in for 凰)" annotation despite 凰's own `stand_in` pointing there (鳳's citation already had it). Quoted `mandarin`/`cantonese`/`korean`. Stamped `date-last-perfect: 2026-09-09`.

Next: 鳳梨.

### 2026-09-09, iteration 3726 — [[words/鳳梨|鳳梨]]
No cranberry (鳳's own `stand_in` is [[鳳凰]], 梨's is 梨 itself — neither points here). Pronunciation fields (pungliǝ/풍릐/ㄆㄨㄫㄌㄧㄜ) and `kwin: false` (AND-rule: both false) already matched constituents exactly — no bug. **Fixed a real bug**: `japanese: ほうり` was a compositional Sino reading, but real Japanese universally uses the loanword パイナップル (matching Korean's already-correct 파인애플) — swapped. Fixed a malformed citation on `characters/鳳.md` (bare "[[鳳梨]] "pineapple"" with no ruby/注音). Filled entirely missing `vietnamese: dứa` — the real native word. Removed blank `hsk_level`/`swadesh`/empty `aliases`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 鳳笙.

### 2026-09-09, iteration 3727 — [[words/鳳笙|鳳笙]]
Legitimizing note added (笙's own `stand_in` is [[鳳笙]] itself, already annotated in its own citation; 鳳's own `stand_in` is [[鳳凰]], so transitivity fails — no `#cranberry`). Pronunciation fields (pungsang/풍상/ㄆㄨㄫㄙㄚㄫ) and `kwin: false` (AND-rule: both false) already matched constituents exactly — no bug. Both character pages already cited 鳳笙 correctly. Rich existing Notes on the gagaku ほうしょう's technical vs. Chinese poetic register kept intact. Filled entirely missing `vietnamese: phượng sinh`. Quoted `mandarin`/`cantonese`/`korean`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 鳴.

### 2026-09-09, iteration 3728 — [[words/鳴|鳴]]
Already fully perfected (stamped 2026-08-30): self-standing bare-character word, pronunciation fields (myeng/명/ㄇ⼶ㄫ), `kwin: true`, and the documented genuine 3-way homophone group with [[皿]]/[[明]] all confirmed correct — verified both are themselves legitimized bare words with exact-matching readings. No changes needed — a clean pass.

Next: 鳶.

### 2026-09-09, iteration 3729 — [[words/鳶|鳶]]
Already fully perfected (stamped 2026-09-03) with an unusually thorough Notes section documenting its own prior romanization-typo fix and a genuine 3-way homophone discovery (演/鉛), already cross-checked against the full ⼶ㄋ syllable set. Verified pronunciation fields ('yen/연/⼶ㄋ) and `kwin: true` still match the character page exactly. No changes needed — a clean pass.

Next: 鴎.

### 2026-09-09, iteration 3730 — [[words/鴎|鴎]]
Self-standing bare-character word (own `stand_in` is 鴎 itself). Pronunciation fields ('ou/옷/ㄛㄨ) already matched the character's own stored values exactly — no homophone (checked full ㄛㄨ syllable set: 偶/殴/𧦅/呕/欧, none self-standing). **Found and fixed a real bug**: `pos` was `固有名詞` (proper noun) despite "seagull" plainly being a common noun — corrected to `名詞`, matching the character's own `pos`. Fixed the recurring duplicate `pos`/`品詞` bug and bare-string `characters:` field. Stamped `date-last-perfect: 2026-09-09`.

Next: 鴛鴦.

### 2026-09-09, iteration 3731 — [[words/鴛鴦|鴛鴦]]
Already correctly `#cranberry`-tagged — verified both 鴛's and 鴦's own `stand_in` point to [[鴛鴦]] itself with genuine transitivity (both independently mean "mandarin duck"), matching its listed entry on `lookup/List of 連綿詞`. Pronunciation fields ('on'ang/온앙/ㄛㄋ·ㄚㄫ), `kwin: false` (AND-rule: 鴛 false, 鴦 true), and all real-language fields already correct. **Found and fixed a real structural gap**: both `characters/鴛.md` and `characters/鴦.md` had no `## Words` section at all despite each documenting the cranberry relationship extensively in prose — added proper citation entries with stand-in annotations to both. Removed blank `hsk_level`/`swadesh`/empty `aliases`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no genuine collision.

Next: 鴨.

### 2026-09-09, iteration 3732 — [[words/鴨|鴨]]
Already fully perfected (stamped 2026-08-30): self-standing bare-character word with a detailed explanation of the Cantonese/Japanese sub-syllable distinction Dan'a'yo's coarser 注音 merges (aap3 vs. 押's aat3; corrected on-reading おう vs. garbled あふ). Verified pronunciation fields ('ab/압/ㄚㄆ), `kwin: true`, and the homophone warning with [[押]] all still correct — 押's own `stand_in` points to itself, exact-matching reading. No changes needed — a clean pass.

Next: 鴻鵠.

### 2026-09-09, iteration 3733 — [[words/鴻鵠|鴻鵠]]
Legitimizing note already substantively documented (鵠's own `stand_in` is [[鴻鵠]] itself). Pronunciation fields (honghog/홍혹/ㄏㄛㄫㄏㄛㄎ) and `kwin: false` (AND-rule: 鴻 true, 鵠 false) already matched constituents exactly — no bug. Both character pages already cited 鴻鵠 correctly. **Found and fixed a real bug**: `pos: 事詞` was wrong for a noun ("swan") — corrected to `名詞`, matching both constituent characters' own `pos`. Rich existing Notes on the Shiji's 燕雀安知鴻鵠之志哉 saying and 鴻's 名専字 status kept intact. Fixed duplicate `pos`/`品詞`, quoted real-language fields. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 鵉鳳.

### 2026-09-09, iteration 3734 — [[words/鵉鳳|鵉鳳]]
Legitimizing note reworded to convention (鵉's own `stand_in` is [[鵉鳳]] itself; 鳳's own `stand_in` is [[鳳凰]], so transitivity fails — no `#cranberry`) — the existing Notes already said this substantively. Pronunciation fields (lanpung/란풍/ㄌㄚㄋㄆㄨㄫ) and `kwin: false` (AND-rule: 鵉 true, 鳳 false) already matched constituents exactly — no bug. Both character pages already cited 鵉鳳 correctly. Filled entirely missing `japanese: らんほう`/`vietnamese: loan phượng`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 鵖鴔.

### 2026-09-09, iteration 3735 — [[words/鵖鴔|鵖鴔]]
Already correctly `#cranberry`-tagged — verified both 鵖's and 鴔's own `stand_in` point to [[鵖鴔]] itself, matching its listed entry on `lookup/List of 連綿詞`. Pronunciation fields (bubbib/붑빕/ㄅㄨㄆㄅㄧㄆ) already matched constituents exactly — no bug. **Found and fixed a real bug**: `pos: 固有名詞` was wrong for a bird species name (a common noun) — corrected to `名詞`, matching both constituent characters. **Decoded a terse stray note** ("Different from a 戴勝") into proper Notes: 鵖鴔 is a classical/archaic hoopoe name distinct from the modern standard 戴勝; filled `japanese: ヤツガシラ`/`korean: 핍핍` (compositional) and flattened `vietnamese` from a list to scalar `đầu rìu`. Flagged, without resolving, an apparent discrepancy on 鵖's own character page (its native gloss points to goldcrest, not hoopoe). In passing fixed a missing stand-in annotation on 鵖's citation and the recurring duplicate `pos`/`品詞` bug. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no genuine collision.

Next: 鵝鳥.

### 2026-09-09, iteration 3736 — [[words/鵝鳥|鵝鳥]]
Legitimizing note added (鵝's own `stand_in` is [[鵝鳥]] itself, already annotated in its own citation; 鳥's own `stand_in` is 鳥 itself, so transitivity fails — no `#cranberry`). Pronunciation fields ('acou/아촛/ㄚㄑㄛㄨ) and `kwin: false` (AND-rule: 鵝 true, 鳥 false) already matched constituents exactly — no bug. **Fixed a real bug**: `mandarin: è` was missing 鳥's own reading entirely — corrected to compositional éniǎo. Filled blank `cantonese: ngo4 niu5`/`vietnamese: nga điểu` (compositional; noted the everyday native word ngỗng). `japanese: がちょう`/`korean: 거위` already correctly native. In passing, fixed 鵝's own citation, which was missing its "(stand-in for 鵝)" annotation. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found only a substring false-positive on 詐取 — no genuine collision.

Next: 鵰.

### 2026-09-09, iteration 3737 — [[words/鵰|鵰]]
Self-standing bare-character word. Pronunciation fields (cuo/춧/ㄑㄨㄛ) already matched the character's own stored values exactly — the existing homophone warning with [[秋]] confirmed genuine (own `stand_in` points to itself). **Found and fixed the same recurring `pos: 固有名詞`→`名詞` bug** seen on 鴎/鴻鵠 — "eagle" is a common noun, not a proper noun, matching the character's own `pos`. Fixed duplicate `pos`/`品詞`, a bare-string `characters:` field, and a stray trailing space on `vietnamese`. Stamped `date-last-perfect: 2026-09-09`.

Next: 鶏.

### 2026-09-09, iteration 3738 — [[words/鶏|鶏]]
Self-standing bare-character word. `pos: 名詞` already correct this time (unlike the recent 鴎/鴻鵠/鵰 mistagging pattern). Pronunciation fields (gei/게/ㄍㄝㄧ) already matched the character's own stored values exactly — checked the full ㄍㄝㄧ syllable set (係/稽/計/継), none self-standing, so no homophone. Fixed duplicate `pos`/`品詞`, a bare-string `characters:` field, and flattened single-item `japanese`/`vietnamese` lists to scalars. Stamped `date-last-perfect: 2026-09-09`.

Next: 鶏卵.

### 2026-09-09, iteration 3739 — [[words/鶏卵|鶏卵]]
No cranberry (鶏's own `stand_in` is 鶏 itself, 卵's is [[卵子]] — neither points here). Pronunciation fields (geilan/게란/ㄍㄝㄧㄌㄚㄋ) and `kwin: false` (AND-rule: 鶏 false, 卵 true) already matched constituents exactly — no bug. Both character pages already cited 鶏卵 correctly. **Fixed a real bug**: `cantonese: ji1 dan4` matched neither constituent's own reading (dan4/蛋 being a different, unrelated Cantonese word for "egg") — corrected to gai1 leon2. **Fixed a malformed `vietnamese` field**: had an odd embedded parenthetical "trứng (thức ăn)" — replaced with the cleaner real term trứng gà, a native word-order reversal joining the vault's documented set of such cases. Removed blank `hsk_level`/`swadesh`, consolidated Etymology into `## Notes`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 鶏肉.

### 2026-09-09, iteration 3740 — [[words/鶏肉|鶏肉]]
No cranberry (both 鶏's and 肉's own `stand_in` point to themselves — neither points here). Pronunciation fields (geinug/게눅/ㄍㄝㄧㄋㄨㄎ) and `kwin: false` (AND-rule: both false) already matched constituents exactly — no bug. Both character pages already cited 鶏肉 correctly. Rich existing Notes on the JA on'yomi/native-hybrid readings and cross-language native-vs-Sino divergence kept intact. Filled entirely missing `vietnamese: kê nhục` (compositional; already correctly described in prose as losing out to native thịt gà, now named explicitly). Quoted `mandarin`/`cantonese`/`korean`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 鶏鳴.
