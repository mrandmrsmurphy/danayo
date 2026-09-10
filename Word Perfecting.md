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

### 2026-09-09, iteration 3741 — [[words/鶏鳴|鶏鳴]]
No cranberry (both 鶏's and 鳴's own `stand_in` point to themselves — neither points here). **Fixed the recurring `characters:` disambiguation bug on BOTH constituents**: bare "鶏"/"鳴" despite `words/鶏.md` and `words/鳴.md` both existing. Pronunciation fields (geimyeng/게명/ㄍㄝㄧㄇ⼶ㄫ) already matched constituents exactly — no bug. Both character pages already cited 鶏鳴 correctly. Filled blank `cantonese: gai1 ming4`/`korean: 계명`/`vietnamese: ke minh` and added missing `kwin: false` (AND-rule: 鶏 false, 鳴 true). Removed blank `hsk_level`/`swadesh`, consolidated Etymology into `## Notes`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found only substring hits on the longer chengyu 鶏鳴狗盗 — no genuine collision.

Next: 鶴.

### 2026-09-09, iteration 3742 — [[words/鶴|鶴]]
Already fully perfected (stamped 2026-08-31): self-standing bare-character word, pronunciation fields (hag/학/ㄏㄚㄎ), `kwin: true`, and the documented genuine 3-way homophone group with [[核]]/[[嚇]] all confirmed correct — verified both are themselves legitimized bare words. No changes needed — a clean pass.

Next: 鷹.

### 2026-09-09, iteration 3743 — [[words/鷹|鷹]]
Already fully perfected (stamped 2026-08-29): self-standing bare-character word, pronunciation fields ('ing/잉/ㄧㄫ), `kwin: false`, and the homophone warning with [[応]] all confirmed correct — 応's own `stand_in` points to itself, exact-matching reading. No changes needed — a clean pass.

Next: 鸚哥.

### 2026-09-09, iteration 3744 — [[words/鸚哥|鸚哥]]
No cranberry (鸚's own `stand_in` is [[鸚鵡]], 哥's is [[哥哥]] — neither points here). Pronunciation fields ('anggǝ/앙그/ㄚㄫㄍㄜ) already matched constituents exactly — no bug. Both character pages already cited 鸚哥 correctly. Filled entirely blank `japanese: おうか`/`vietnamese: anh ca` (compositional; noted everyday Vietnamese prefers native vẹt) and added missing `kwin: false` (AND-rule: both false). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 鸚鵡.

### 2026-09-09, iteration 3745 — [[words/鸚鵡|鸚鵡]]
Already correctly `#cranberry`-tagged — verified both 鸚's and 鵡's own `stand_in` point to [[鸚鵡]] itself, matching its listed entry on `lookup/List of 連綿詞`. Pronunciation fields ('angmu/앙무/ㄚㄫㄇㄨ), `kwin: false` (AND-rule: 鸚 false, 鵡 true), and all real-language fields already correct — `vietnamese: vẹt` confirmed as the real everyday native word (vs. the less common compositional anh vũ), documented in Notes. **Found and fixed the same structural gap as 鴛/鴦**: `characters/鵡.md` had no `## Words` section at all despite documenting the cranberry relationship extensively in prose — added a proper citation with stand-in annotation. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check (precise 注音-only match, ruling out earlier broad substring hits) found no genuine collision.

Next: 鸛鶴.

### 2026-09-09, iteration 3746 — [[words/鸛鶴|鸛鶴]]
Legitimizing note already substantively documented (鸛's own `stand_in` is [[鸛鶴]] itself). Pronunciation fields (gwanhag/관학/ㄍ⺢ㄋㄏㄚㄎ) and `kwin: true` (AND-rule: both true) already matched constituents exactly — no bug. Both character pages already cited 鸛鶴 correctly. Filled entirely missing `vietnamese: quán hạc`. Quoted `mandarin`/`cantonese`/`korean`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 鹸.

### 2026-09-09, iteration 3747 — [[words/鹸|鹸]]
Self-standing bare-character word. Pronunciation fields (cem/첨/ㄑㄝㄇ) and `kwin: true` already matched the character's own stored values exactly — the existing homophone warning with [[諂]] confirmed genuine (own `stand_in` points to itself, per that page's own prior perfecting notes referencing a `homophone_check.py` script). Reformatted the Notes from an unconventional numbered list into proper prose, keeping the useful content: 鹸 serves as the periodic-table abbreviation prefix for sodium via [[鹸素]]. Fixed a bare-string `characters:` field.

Next: 鹸素.

### 2026-09-09, iteration 3748 — [[words/鹸素|鹸素]]
Periodic-table neologism series (sodium): already correctly following convention — `mandarin`/`cantonese` give the avoided real element character 鈉/钠's readings; `korean`/`japanese`/`vietnamese` (나트륨/ナトリウム/natri) are loanwords from "Natrium"; `kwin: false` correctly compares Dan'a'yo against Korean. Dan'a'yo pronunciation fields (cemso/첨소/ㄑㄝㄇㄙㄛ) correctly follow normal compositional concatenation of 鹸+素. `characters:` disambiguation already correct (`words/鹸.md` exists, `words/素.md` doesn't). Both character pages already cited 鹸素 correctly. Rich existing Notes already comparing this semantic (not phonetic) coinage to [[巨金]]/[[惰素]] kept intact. No changes needed — a clean pass.

Next: 鹿.

### 2026-09-09, iteration 3749 — [[words/鹿|鹿]]
Already fully perfected (stamped 2026-08-03): self-standing bare-character word with a detailed record of a prior real `korean` bug fix (녹→록, the same North-Korean-form pattern as [[老]]), and the genuine homophone with [[緑]] confirmed correct — verified 緑's own `stand_in` points to itself, exact-matching reading. `characters/鹿 (char).md`'s own remaining rough state was already flagged as out-of-scope for a future character-perfection sweep, not this word. No changes needed — a clean pass.

Next: 鹿砦.

### 2026-09-09, iteration 3750 — [[words/鹿砦|鹿砦]]
Legitimizing note added (砦's own `stand_in` is [[鹿砦]] itself, already annotated in its own citation; 鹿's own `stand_in` is 鹿 itself, so transitivity fails — no `#cranberry`). Pronunciation fields (logjai/록재/ㄌㄛㄎㄐㄚㄧ) already matched constituents exactly — no bug. **In passing, fixed a real gap**: `characters/砦.md`'s own citation of 鹿砦 was missing its "(stand-in for 砦)" annotation. Filled blank `korean: 록채`/`vietnamese: lộc trại` and added missing `kwin: false` (AND-rule: 鹿 true, 砦 false). Removed blank `hsk_level`/`swadesh`/empty `aliases`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 麒麟.

### 2026-09-09, iteration 3751 — [[words/麒麟|麒麟]]
Already correctly `#cranberry`-tagged — verified both 麒's and 麟's own `stand_in` point to [[麒麟]] itself, matching its listed entry on `lookup/List of 連綿詞`. Pronunciation fields (gilin/기린/ㄍㄧㄌㄧㄋ), `kwin: true` (AND-rule: both true), and all real-language fields already correct. **Unlike 鴛/鴦 and 鵡, both character pages already had proper `## Words` sections** — but both were missing the "(stand-in for X)" annotation despite their own `stand_in` pointing here; fixed both. Removed blank `hsk_level`/`swadesh`/empty `aliases`, quoted real-language fields. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 麒麟羚羊.

### 2026-09-09, iteration 3752 — [[words/麒麟羚羊|麒麟羚羊]]
No cranberry (none of the four constituents' own `stand_in` points here). Pronunciation fields (gilinleng'yang/기린렁양/ㄍㄧㄌㄧㄋㄌㄝㄫ⼘ㄫ) and `kwin: false` (AND-rule: 麒 true, 麟 true, 羚 false, 羊 true → false) already matched constituents exactly — no bug. **Found and fixed the most severe real-language field bug this sweep**: `mandarin: zhōnggúo` was literally "中国" ("China," entirely unrelated) and `cantonese: yǔwén1` was likewise unrelated garbage ("語文"-ish, "language and literature") — both corrected to the compositional qílínlíngyáng/kei4leon4ling4joeng4. Filled entirely missing `vietnamese: kỳ lân linh dương`. **In passing, fixed a real citation gap** on `characters/羊.md`, whose own Words list was missing 麒麟羚羊 entirely. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 麟史.

### 2026-09-09, iteration 3753 — [[words/麟史|麟史]]
No cranberry (麟's own `stand_in` is [[麒麟]], 史's is [[歴史]] — neither points here). Pronunciation fields (linsi/린시/ㄌㄧㄋㄙㄧ) and `kwin: false` (AND-rule: 麟 true, 史 false) already matched constituents exactly — no bug. Both character pages already cited 麟史 correctly. `pos: 固有名詞` already correctly a proper noun (a specific historical text's alternate name, unlike the recent bird-species mistagging cases). **Investigated `korean: 인사`, which deviates from 麟's own stored 린 (the North-Korean-consistent compositional form would be 린사)** — cross-checked the sibling word [[麟経]], which documents the identical 두음법칙 pattern (인경, also deviating from 린) with a specific real-world-attestation rationale; treated as a deliberate, already-reasoned exception rather than a bug, and left unchanged. Only fix was the recurring duplicate `pos`/`品詞` bug. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 麟経.

### 2026-09-09, iteration 3754 — [[words/麟経|麟経]]
No cranberry (麟's own `stand_in` is [[麒麟]], 経's is 経 itself — neither points here). Pronunciation fields (lingeng/린겅/ㄌㄧㄋㄍㄝㄫ) and `kwin: false` (AND-rule: 麟 true, 経 false) already matched constituents exactly — no bug. `characters:` disambiguation already correct. Both character pages already cited 麟経 correctly. `korean: 인경` already correctly the documented deliberate exception (matching 麟史's identical pattern, confirmed last iteration). Only fix was the recurring duplicate `pos`/`品詞` bug and quoting real-language fields. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 麦芽.

### 2026-09-09, iteration 3755 — [[words/麦芽|麦芽]]
No cranberry (麦's own `stand_in` is [[大麦]], 芽's is [[新芽]] — neither points here). Pronunciation fields (mag'a/막아/ㄇㄚㄎㄚ) and `kwin: false` (AND-rule: 麦 false, 芽 true) already matched constituents exactly — no bug (noted the 注音 lacks a syllable-boundary dot before the vowel-initial 芽, unlike some other vowel-initial-second-syllable words this sweep — but 麦's own character page uses the identical undotted form consistently across its own citations, so left as an established pattern rather than guessed at). Both character pages already cited 麦芽 correctly. All real-language fields already correct standard readings. Removed blank `hsk_level`/`swadesh`, consolidated Etymology into `## Notes`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 麦芽糖.

### 2026-09-09, iteration 3756 — [[words/麦芽糖|麦芽糖]]
No cranberry (none of the three constituents' own `stand_in` points here). Pronunciation fields (mag'adwang/막아돵/ㄇㄚㄎㄚㄉ⺢ㄫ) already matched constituents exactly — no bug (same consistently-undotted pattern as [[麦芽]], left alone). **Fixed the recurring `characters:` disambiguation bug**: bare "糖" despite `words/糖.md` existing (Etymology already correctly cited "糖 (char)"). Both character pages already cited 麦芽糖 correctly. Filled entirely missing `vietnamese: mạch nha đường`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 麦茶.

### 2026-09-09, iteration 3757 — [[words/麦茶|麦茶]]
No cranberry (both 麦's and 茶's own `stand_in` point elsewhere — neither points here). Pronunciation fields (magca/막차/ㄇㄚㄎㄑㄚ) already matched constituents exactly — no bug. `characters:` disambiguation already correct. Both character pages already cited 麦茶 correctly. Left `korean` deliberately blank per the existing well-reasoned note (real Korean has no attested Sino form at all, using only native 보리차). Added missing `kwin: false` (AND-rule: both false) and filled entirely missing `vietnamese: mạch trà` (compositional). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 麦酒.

### 2026-09-09, iteration 3758 — [[words/麦酒|麦酒]]
No cranberry (麦's own `stand_in` is [[大麦]], 酒's is [[酒精]] — neither points here). Pronunciation fields (magjuo/막줏/ㄇㄚㄎㄐㄨㄛ) and `kwin: false` (AND-rule: both false) already matched constituents exactly — no bug. Both character pages already cited 麦酒 correctly. **Investigated and explained a real divergence, previously undocumented**: `mandarin`/`cantonese` (píjiǔ/be1zau2) don't match compositional màijiǔ/mak6zau2 — confirmed this is deliberate, giving the real modern standard word 啤酒 (already listed as this word's alias) instead, since 麦酒 itself is the historical Japanese-coined term now largely displaced by ビール — the same real-name-over-compositional convention seen elsewhere; documented in Notes. Removed blank `hsk_level`/`swadesh`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 麺.

### 2026-09-09, iteration 3759 — [[words/麺|麺]]
Self-standing bare-character word. Pronunciation fields (men/먼/ㄇㄝㄋ) already matched the character's own stored values exactly — no homophone. Kept the existing explanation of the flour→noodle metonymy and cross-reference to [[拉麺]] intact. Fixed duplicate `pos`/`品詞` and flattened single-item `japanese`/`vietnamese` lists to scalars. Stamped `date-last-perfect: 2026-09-09`.

Next: 麺包.

### 2026-09-09, iteration 3760 — [[words/麺包|麺包]]
No cranberry (麺's own `stand_in` is 麺 itself, 包's is [[包装]] — neither points here). Pronunciation fields (menbyau/먼뱟/ㄇㄝㄋㄅ⼘ㄨ) and `kwin: false` (AND-rule: both false) already matched constituents exactly — no bug. Both character pages already cited 麺包 correctly. `japanese: パン`/`korean: 빵` already correctly loanwords from Portuguese *pão*. Decoded a stray note ("for pastries and sweet bread, use 餅") into a proper Notes sentence. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found only an incidental Bible-translation mention — no genuine collision.

Next: 麻布.

### 2026-09-09, iteration 3761 — [[words/麻布|麻布]]
No cranberry (麻's own `stand_in` is [[大麻]], 布's is [[亜麻布]] — neither points here). Pronunciation fields (mabo/마보/ㄇㄚㄅㄛ) and `kwin: false` (AND-rule: 麻 true, 布 false) already matched constituents exactly — no bug. **Fixed a real contamination bug**: `japanese: あさふ,あさぬの` comma-joined two forms — kept あさぬの (the more naturally-attested compound). **Fixed a malformed citation** on `characters/麻.md` (markdown-link syntax mixed with orphaned ruby tags instead of the standard wikilink template). Filled entirely missing `vietnamese: ma bố`. Removed blank `hsk_level`/`swadesh`/empty `aliases`, consolidated Etymology into `## Notes`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 麻痺.

### 2026-09-09, iteration 3762 — [[words/麻痺|麻痺]]
Legitimizing note added (痺's own `stand_in` is [[麻痺]] itself, already annotated in its own citation; 麻's own `stand_in` is [[大麻]], so transitivity fails — no `#cranberry`). Pronunciation fields (mabi/마비/ㄇㄚㄅㄧ) and `kwin: true` (AND-rule: both true) already matched constituents exactly — no bug. **Fixed the same malformed-citation pattern found on 麻布, and swept the rest of `characters/麻.md`'s Words list while there**: 麻痺's own citation plus 麻雀/淡麻/胡麻 all used markdown-link syntax instead of wikilinks, and 亜麻 had no ruby/注音 at all — reformatted all five to the standard template (亜麻's 注音 verified against its own word file rather than guessed). **In passing, fixed a real gap**: `characters/痺.md`'s citation was missing its "(stand-in for 痺)" annotation. Filled entirely missing `vietnamese: ma tê`, extending the existing rich Notes on the shared hemp-metaphor etymology. Rich existing content on medical/figurative senses (脳性麻痺, 都市機能が麻痺する) kept intact. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 麻雀.

### 2026-09-09, iteration 3763 — [[words/麻雀|麻雀]]
No cranberry (麻's own `stand_in` is [[大麻]], 雀's is [[麻雀鳥]] — neither points here). Pronunciation fields (majag/마작/ㄇㄚㄐㄚㄎ) and `kwin: true` (AND-rule: both true) already matched constituents exactly — no bug. **Decoded the design behind this word**: 麻雀 is deliberately reserved for "mahjong" while the literal "sparrow" sense uses the extended [[麻雀鳥]] (雀's own actual legitimizer) — documented this disambiguation explicitly in Notes. **In passing, fixed a real citation gap**: `characters/雀.md`'s own Words list was missing 麻雀 entirely (had only its own stand-in 麻雀鳥) — added, and added the missing "(stand-in for 雀)" annotation to the existing 麻雀鳥 citation. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 麻雀鳥.

### 2026-09-09, iteration 3764 — [[words/麻雀鳥|麻雀鳥]]
Legitimizing note added (雀's own `stand_in` is [[麻雀鳥]] itself, already annotated in its own citation; neither 麻's nor 鳥's own `stand_in` points here — no `#cranberry`). Pronunciation fields (majagcou/마작촛/ㄇㄚㄐㄚㄎㄑㄛㄨ) and `kwin: false` (AND-rule: 麻 true, 雀 true, 鳥 false → false) already matched constituents exactly — no bug. All three character pages already cited 麻雀鳥 correctly. `japanese: すずめ`/`korean: 참새` already correctly native. Filled entirely missing `vietnamese: ma tước điểu`. Self-caught and fixed a tone-typo (maa5→maa4) I introduced while drafting the Notes prose. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 黄.

### 2026-09-09, iteration 3765 — [[words/黄|黄]]
Self-standing bare-character word. Pronunciation fields (hwang/황/ㄏ⺢ㄫ) and `kwin: true` already matched the character's own stored values exactly — checked the full ㄏ⺢ㄫ syllable set (徨/横/凰/皇/幌/煌/況/慌/晃/荒), none self-standing, so no homophone. **Found and fixed a real bug**: `cantonese: huang2` was a Mandarin-pinyin-style romanization, not valid Jyutping — corrected to wong4, matching the character's own stored field. Fixed duplicate `pos`/`品詞` and a bare-string `characters:` field. Stamped `date-last-perfect: 2026-09-09`.

Next: 黄昏.

### 2026-09-09, iteration 3766 — [[words/黄昏|黄昏]]
Legitimizing note added (昏's own `stand_in` is [[黄昏]] itself, already annotated in its own citation; 黄's own `stand_in` is 黄 itself, so transitivity fails — no `#cranberry`). Pronunciation fields (hwanghon/황혼/ㄏ⺢ㄫㄏㄛㄋ) and `kwin: true` (AND-rule: both true) already matched constituents exactly — no bug. **Fixed the recurring `characters:` disambiguation bug**: bare "黄" despite `words/黄.md` existing (Etymology already correctly cited "黄 (char)"). Both character pages already cited 黄昏 correctly. All real-language fields already correct standard readings. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 黄檗.

### 2026-09-09, iteration 3767 — [[words/黄檗|黄檗]]
Legitimizing note added (檗's own `stand_in` is [[黄檗]] itself, already annotated in its own citation; 黄's own `stand_in` is 黄 itself, so transitivity fails — no `#cranberry`). Pronunciation fields (hwangbag/황박/ㄏ⺢ㄫㄅㄚㄎ) already matched constituents exactly — no bug. **Found and fixed two real bugs**: `cantonese` had two slash-separated candidates ("wong4 baak3 / wong4 paak3") — kept only paak3, matching 檗's own stored field exactly; `kwin: true` contradicted the AND-rule (檗's own kwin is false) — corrected to `false`. **In passing, fixed a missing stand-in annotation** on 檗's own citation. Filled entirely missing `vietnamese: hoàng bách`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 黄沙.

### 2026-09-09, iteration 3768 — [[words/黄沙|黄沙]]
No cranberry (both 黄's and 沙's own `stand_in` point to themselves — neither points here). Pronunciation fields (hwangsa/황사/ㄏ⺢ㄫㄙㄚ) and `kwin: true` (AND-rule: both true) already matched constituents exactly — no bug. Both character pages already cited 黄沙 correctly. Filled entirely missing `japanese: こうさ`, using 黄's first-listed KOU reading (over OU, the reading its own bare word page uses) — こうさ matches the real, standard Japanese term for this weather phenomenon exactly (though modern Japanese conventionally spells it 黄砂). Filled entirely missing `vietnamese: hoàng sa`, flagging its coincidental overlap with the Paracel Islands' Vietnamese name. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 黄泉.

### 2026-09-09, iteration 3769 — [[words/黄泉|黄泉]]
No cranberry (黄's own `stand_in` is 黄 itself, 泉's is [[源泉]] — neither points here). Pronunciation fields (hwangjwen/황줜/ㄏ⺢ㄫㄐ⼔ㄋ) and `kwin: false` (AND-rule: 黄 true, 泉 false) already matched constituents exactly — no bug. Both character pages already cited 黄泉 correctly. **Fixed a real contamination bug**: `japanese: よみ,こうせん` comma-joined two forms — kept よみ, the real, culturally significant term for the Japanese mythological underworld. `korean: 황천` already correctly compositional. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 黄海.

### 2026-09-09, iteration 3770 — [[words/黄海|黄海]]
No cranberry (both 黄's and 海's own `stand_in` point elsewhere — neither points here). Pronunciation fields (hwanghai/황해/ㄏ⺢ㄫㄏㄚㄧ) and `kwin: true` (AND-rule: both true) already matched constituents exactly — no bug. Both character pages already cited 黄海 correctly. Decoded a stray note ("Koreans call it 西海") into a proper Notes sentence, explaining the Korean colloquial 西海/서해 preference alongside the formal 황해 already used in this word's own `korean` field (kept, since both are genuinely real Korean usage). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 黄金.

### 2026-09-09, iteration 3771 — [[words/黄金|黄金]]
Already fully perfected (stamped 2026-07-27): a real, established compound for gold (unlike the invented-calque periodictable neologisms elsewhere this sweep), correctly tagged `periodictable` without `neologism`, with `kwin: true` correctly following the normal AND-rule rather than the special neologism convention. Verified pronunciation fields (hwanggim/황김/ㄏ⺢ㄫㄍㄧㄇ) and both character-page citations still correct. No changes needed — a clean pass.

Next: 黄銅.

### 2026-09-09, iteration 3772 — [[words/黄銅|黄銅]]
No cranberry (both 黄's and 銅's own `stand_in` point to themselves — neither points here). Pronunciation fields (hwangdong/황동/ㄏ⺢ㄫㄉㄛㄫ) already matched constituents exactly — no bug. Both character pages already cited 黄銅 correctly. **Fixed a likely typo**: `japanese: わうどう` used the archaic historical kana spelling — corrected to おうどう, matching the modern form already established on the sibling word [[黄金]]. Filled blank `korean: 황동`/`vietnamese: hoàng đồng` (compositional; noted native đồng thau) and added missing `kwin: true` (AND-rule: both true). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 黎明.

### 2026-09-09, iteration 3773 — [[words/黎明|黎明]]
Legitimizing note added (黎's own `stand_in` is [[黎明]] itself, already annotated in its own citation; 明's own `stand_in` is 明 itself, so transitivity fails — no `#cranberry`). Pronunciation fields (leimyeng/레명/ㄌㄝㄧㄇ⼶ㄫ) and `kwin: false` (AND-rule: 黎 false, 明 true) already matched constituents exactly — no bug. **Fixed the recurring `characters:` disambiguation bug**: bare "明" despite `words/明.md` existing (Etymology already correctly cited "明 (char)"). **Fixed a real content bug**: the Etymology gloss for 黎 was literally its own romanization "Liǝ" rather than a meaning — corrected to "black" (黎's own stored English gloss), explaining the "black-bright" transition-to-dawn logic. Filled entirely missing `vietnamese: lê minh`. In passing fixed curly quotes and a missing stand-in annotation on 黎's own citation. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 黒.

### 2026-09-09, iteration 3774 — [[words/黒|黒]]
Already fully perfected (stamped 2026-08-03): self-standing bare-character word with a rich Notes section on the soot/smoke-blackened 象形 origin (paralleling [[青]]'s pigment-based etymology), the periodic-table hassium prefix role via [[黒金]], and a detailed kwin explanation. Verified pronunciation fields (hug/훅/ㄏㄨㄎ) and `kwin: false` still match the character page exactly. No changes needed — a clean pass.

Next: 黒暗.

### 2026-09-09, iteration 3775 — [[words/黒暗|黒暗]]
No cranberry (both 黒's and 暗's own `stand_in` point to themselves — neither points here), added to the extensive existing philosophical/cosmological essay covering Daoist 玄, yin, Buddhist 無明, and the moral light/darkness polarity. Pronunciation fields (hug'am/훅암/ㄏㄨㄎ·ㄚㄇ) and `kwin: false` (AND-rule: 黒 false, 暗 true) already matched constituents exactly — no bug. **Found and fixed two real bugs where the frontmatter directly contradicted the essay's own prose**: `korean: 암흑` had the syllables reversed (the prose itself already correctly says 흑암) — corrected; `vietnamese: bóng tối` was a native phrase entirely different from the compositional form the prose explicitly names (hắc ám) — corrected. Also fixed a duplicated "hắc ám or hắc ám" typo in the prose itself, and a real citation gap on `characters/黒 (char).md`, whose Words list was missing 黒暗 entirely. Added missing `date-last-perfect: 2026-09-09`. Background exact-match homophone check found only an incidental Bible-translation mention — no genuine collision.

Next: 黒板.

### 2026-09-09, iteration 3776 — [[words/黒板|黒板]]
No cranberry (黒's own `stand_in` is 黒 itself, 板's is [[木板]] — neither points here). Pronunciation fields (hugpan/훅판/ㄏㄨㄎㄆㄚㄋ) and `kwin: false` (AND-rule: 黒 false, 板 true) already matched constituents exactly — no bug. **Fixed the recurring `characters:` disambiguation bug**: bare "黒" despite `words/黒.md` existing. Both character pages already cited 黒板 correctly. Filled entirely missing `vietnamese: hắc bản`, quoted `hsk_level`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 黒洞.

### 2026-09-09, iteration 3777 — [[words/黒洞|黒洞]]
No cranberry (黒's own `stand_in` is 黒 itself, 洞's is [[洞窟]] — neither points here). Pronunciation fields (hugdong/훅동/ㄏㄨㄎㄉㄛㄫ) and `kwin: false` (AND-rule: 黒 false, 洞 true) already matched constituents exactly — no bug. Both character pages already cited 黒洞 correctly. `japanese: ブラックホール`/`korean: 블랙홀` already correctly English loanwords. Filled entirely missing `vietnamese: hố đen`, a real native word-order-reversed term. Fixed a stray blank Etymology gloss for 黒. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 黒猩.

### 2026-09-09, iteration 3778 — [[words/黒猩|黒猩]]
No cranberry (黒's own `stand_in` is 黒 itself, 猩's is [[猩猩]] — neither points here). Pronunciation fields (hugseng/훅성/ㄏㄨㄎㄙㄝㄫ) and `kwin: false` (AND-rule: 黒 false, 猩 true) already matched constituents exactly — no bug. Both character pages already cited 黒猩 correctly. Rich existing Notes on the 黒猩猩 abbreviation pattern (paralleling 大猩/倭猩) and Jane Goodall's Gombe research kept intact. Only fix was quoting `mandarin`/`cantonese`/`korean`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 黒色.

### 2026-09-09, iteration 3779 — [[words/黒色|黒色]]
No cranberry (黒's own `stand_in` is 黒 itself, 色's is [[色彩]] — neither points here). Pronunciation fields (hugsig/훅식/ㄏㄨㄎㄙㄧㄎ) and `kwin: false` (AND-rule: both false) already matched constituents exactly — no bug. **Fixed the recurring `characters:` disambiguation bug** and **a real comma-joined `vietnamese` contamination bug** (kept đen, the real native word; hắc mentioned as the compositional alternate in Notes). Documented `japanese: くろ`/`korean: 검정` as legitimate real-native-word choices over the compositional こくしょく/흑색, previously unexplained. Removed blank `hsk_level`/`swadesh`/empty `aliases`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 黒貂.

### 2026-09-09, iteration 3780 — [[words/黒貂|黒貂]]
Legitimizing note added (貂's own `stand_in` is [[黒貂]] itself, already annotated in its own citation; 黒's own `stand_in` is 黒 itself, so transitivity fails — no `#cranberry`). Pronunciation fields (hugco/훅초/ㄏㄨㄎㄑㄛ) and `kwin: false` (AND-rule: 黒 false, 貂 true) already matched constituents exactly — no bug. Fixed the recurring `characters:` disambiguation bug. `japanese: くろてん`/`korean: 검은담비` already correctly native compounds. In passing, fixed a missing stand-in annotation on 貂's own citation. Filled entirely missing `vietnamese: hắc điêu`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 黒金.

### 2026-09-09, iteration 3781 — [[words/黒金|黒金]]
Periodic-table neologism series (hassium): already correctly following convention and richly documented — the toponymic coincidence between 黒 ("black") and 黑森州 (Hesse, where hassium was discovered) explained alongside parallels to [[海金]]/[[冥金]]. `mandarin`/`cantonese` give the avoided real element character 𨭆's own reading; `korean`/`japanese`/`vietnamese` are IUPAC-name loanwords; `kwin: false` correctly compares Dan'a'yo against Korean. `characters/金 (char).md` doesn't cite 黒金, consistent with that character's already-documented, deliberately out-of-scope citation gap. No changes needed — a clean pass.

Next: 黙想.

### 2026-09-09, iteration 3782 — [[words/黙想|黙想]]
No cranberry (黙's own `stand_in` is [[沈黙]], 想's is [[思想]] — neither points here). Pronunciation fields (mugsang/묵상/ㄇㄨㄎㄙㄚㄫ) and `kwin: true` (AND-rule: both true) already matched constituents exactly — no bug. Both character pages already cited 黙想 correctly. Filled blank `cantonese: mak6 soeng2`/`vietnamese: mặc tưởng`. Removed blank `hsk_level`/`swadesh`/empty `aliases`, consolidated Etymology into `## Notes`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 黙黙.

### 2026-09-09, iteration 3783 — [[words/黙黙|黙黙]]
Self-reduplication of [[黙]] (own `stand_in` is [[沈黙]], no cranberry logic needed for a same-character pair). Pronunciation fields (mugmug/묵묵/ㄇㄨㄎㄇㄨㄎ) already matched constituents exactly — no bug. Character page already cited 黙黙 correctly. Added missing `kwin: true` (AND-rule: both instances true) and filled entirely missing `vietnamese: mặc mặc`. Quoted `korean`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 黼黻.

### 2026-09-09, iteration 3784 — [[words/黼黻|黼黻]]
Already correctly `#cranberry`-tagged, matching its listed entry on `lookup/List of 連綿詞`. **Investigated a suspected romanization mismatch and resolved it as legitimate**: 黼's own `羅馬字` "fu" appeared to conflict with its own `諺文` "뿌" (a tense ㅃ), but cross-checking `middle_chinese_initial` confirmed both 黼 and 黻 share the same MC f- initial, and the tense-ㅃ 諺文 spelling is a consistent vault convention for approximating this class (Korean lacking a native /f/) — the word's own concatenation (뿌뿓/ㄈㄨㄈㄨㄊ) already correctly follows this pattern; left `黼 (char).md`'s own possibly-inconsistent `羅馬字` alone rather than guess-fix it. Filled entirely missing `vietnamese: phủ phất`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 鼈.

### 2026-09-09, iteration 3785 — [[words/鼈|鼈]]
Self-standing bare-character word. **Found a real homophone already anticipated by its counterpart**: `words/別.md` already carried a homophone warning for 鼈 (correctly flagging it as "awaiting its own turn") — added the reciprocal warning here and fixed the now-stale wording on 別.md. Pronunciation fields (bed/벋/ㄅㄝㄊ) already matched the character's own stored values exactly — checked the full ㄅㄝㄊ syllable set (閥/罰), neither self-standing, confirming the cluster is exactly 鼈/別. Filled entirely missing `japanese: すっぽん`, the real native word (a well-known culinary delicacy) rather than a Sino on'yomi. Fixed `# Notes` heading level, bare-string `characters:`, and added missing `pos`/`kwin`/`date-last-perfect`.

Next: 鼎.

### 2026-09-09, iteration 3786 — [[words/鼎|鼎]]
Already fully perfected (stamped 2026-08-03): self-standing bare-character word with the anticipated reciprocal homophone callout to [[呈]] completed, and the character page's own rough state already flagged out-of-scope (a tenth instance of that pattern this sweep). Verified pronunciation fields (ding/딩/ㄉㄧㄫ) and `kwin: false` still match the character page exactly. No changes needed — a clean pass.

Next: 鼓.

### 2026-09-09, iteration 3787 — [[words/鼓|鼓]]
Self-standing bare-character word, already largely perfected: pronunciation fields (go/고/ㄍㄛ), `pos: 名詞`, `kwin: true`, and all real-language fields already matched `characters/鼓 (char).md` exactly, and the real three-way homophone group with [[股]]/[[錮]] was already fully cross-linked from a previous pass. **Fixed a stale-note bug**: the word's own Notes claimed `characters/鼓 (char).md` was "genuinely unperfected" (blank `pos`, dangling CC wikilinks, no `date-last-perfect`) — but the character page is actually already fully perfected (stamped 2026-08-05, proper `## Words` list, complete `mc_id`/`stand_in`), evidently completed by a separate later pass after this word's own note was written. Corrected the Notes accordingly and aligned the etymology description with the character page's own documented components (壴 + 攴, not "支"). Stamped `date-last-perfect: 2026-09-09`.

Next: 鼓舞.

### 2026-09-09, iteration 3788 — [[words/鼓舞|鼓舞]]
No cranberry (鼓's own `stand_in` is 鼓 itself, 舞's is [[跳舞]] — neither points here). Fixed the recurring `characters:` disambiguation bug (bare "鼓" despite `words/鼓.md` existing; "舞" correctly left bare, no `words/舞.md`). Pronunciation fields (gomu/고무/ㄍㄛㄇㄨ) and `kwin: true` (AND-rule: both true) already matched constituents exactly. **Found a genuine hidden-character bug**: the `japanese` field's displayed text "こぶ" silently contained a zero-width space (U+200B) between the two kana — invisible on render but a corrupted field value; removed it. Converted lone `## Etymology` heading to standard `## Notes` template with cranberry-status line and explanatory prose (Japanese こぶ real attested on'yomi compound, Vietnamese cổ vũ real everyday verb). Removed blank `hsk_level`/`swadesh`/`aliases`. Added missing `date-last-perfect: 2026-09-09`. Both character pages' `## Words` citations already correct. Background exact-match homophone check found no collision.

Next: 鼠色.

### 2026-09-09, iteration 3789 — [[words/鼠色|鼠色]]
No cranberry (鼠's own `stand_in` is [[熊鼠]], 色's is [[色彩]] — neither points here). Pronunciation fields (syosig/쇼식/ㄙ⼄ㄙㄧㄎ) and `kwin: false` (AND-rule: both false) already matched constituents exactly. `characters:` already correctly bare (neither `words/鼠.md` nor `words/色.md` exists). **Fixed a real citation gap**: `characters/鼠.md`'s `## Words` list was missing 鼠色 entirely (色's own list already had it). **Removed a redundant self-referential `aliases: [鼠色]` entry** — same bug variant previously fixed on [[熊鼠]] (the field is for genuine variant written forms, not a copy of the filename). Confirmed `mandarin`/`cantonese` (huīsè/fui1 sik1, "grey" proper rather than a literal mouse-color calque) and filled entirely missing `vietnamese: xám chuột` (real native "mouse grey" color term) — both following the real-attested-usage-over-compositional convention; Japanese ねずみいろ/Korean 쥐색 already correctly real mouse-color compounds. Stamped `date-last-perfect: 2026-09-09` (previously stale at 2026-03-27). Background exact-match homophone check found no collision.

Next: 鼠類.

### 2026-09-09, iteration 3790 — [[words/鼠類|鼠類]]
No cranberry (鼠's own `stand_in` is [[熊鼠]], 類's is [[種類]] — neither points here). Both character pages already cited 鼠類 correctly. Pronunciation fields (syolui/쇼뤼/ㄙ⼄ㄌㄨㄧ) and `kwin: false` (AND-rule: both false) already matched. **Fixed two real bugs**: `mandarin` was truncated to bare "shǔ" (missing 類's own "lèi"); `cantonese` held "su3," an unrelated garbage value matching neither constituent's own stored reading — both corrected to compositional shǔlèi/syu2 leoi6. **Fixed a contaminated `aliases` entry**: "即鼠總科" had a stray leading "即" ("namely") — explanatory prose accidentally left inside the alias value — trimmed to the real alternate title 鼠總科. Filled entirely missing `vietnamese: thử loại`, matching the plain-compositional convention already used on sibling words [[鳥類]]/[[魚類]]; Japanese ネズミ上科/Korean 쥐상과 already correctly real taxonomic compounds. Converted `## Etymology` to `## Notes`. Removed blank `hsk_level`/`swadesh`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 鼻.

### 2026-09-09, iteration 3791 — [[words/鼻|鼻]]
Self-standing bare-character word, already fully perfected: pronunciation fields (bi/비/ㄅㄧ), `pos: 名詞`, `kwin: true`, and `vietnamese: tị` all matched `characters/鼻 (char).md` exactly, and the character page's own `## Words`/`## Chengyu` citations for 鼻/鼻水/阿鼻/阿鼻叫喚 were already correct. No-homophone conclusion (checked 碑/痺/脾/琵/婢/皮, none self-standing) reconfirmed via background exact-match grep. Only fix was the stale `date-last-perfect` (2026-08-03 → 2026-09-09) — a clean pass otherwise.

Next: 鼻水.

### 2026-09-09, iteration 3792 — [[words/鼻水|鼻水]]
No cranberry (both 鼻's and 水's own `stand_in` point to themselves — neither points here). Both character pages already cited 鼻水 correctly. Fixed the recurring `characters:` disambiguation bug (bare "鼻"/"水" despite both `words/鼻.md` and `words/水.md` existing). Added missing `kwin: true` (AND-rule: both constituents individually true). **Fixed a comma-joined `korean` contamination bug**: `"비수, 콧물"` — kept 콧물, the real native "nose-water" compound (the everyday word for snot), documented 비수 (the literal compositional form) as the rejected alternate in prose, noting 비수 is additionally a real unrelated Korean word for "dagger" (匕首). Filled entirely missing `vietnamese: nước mũi`, a native word-order-reversed compound ("water of nose") matching the established pattern. `japanese: はなみず` already correctly the real native compound. Removed blank `hsk_level`/`swadesh`/`aliases`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 龍.

### 2026-09-09, iteration 3793 — [[words/龍|龍]]
Self-standing bare-character word. Pronunciation fields (lyong/룡/ㄌ⼄ㄫ), `pos: 名詞`, `kwin: true`, and `vietnamese: long` all matched `characters/龍 (char).md` exactly. **Fixed the duplicate `品詞`/`pos` field bug** (part of the known 590-file scope, fixed for free here since the sweep reached it directly). **Fixed a real citation gap**: the character page's `## Words` list was missing 龍's own self-citation entirely (`stand_in: 龍`, self-pointing) — added it. The character page otherwise remains in a rough, largely-unperfected state (bare unformatted `[[link]] - gloss` bullets throughout, nonstandard `### Related Characters` heading, two dangling CC-initial/final wikilinks after `## Chengyu`) — flagged for the character-perfection sweep, not rebuilt here. Background exact-match homophone check found no collision. Stamped `date-last-perfect: 2026-09-09`.

Next: 龍巻.

### 2026-09-09, iteration 3794 — [[words/龍巻|龍巻]]
`characters:` already correctly disambiguated (both `words/龍.md` and `words/巻.md` exist). Both character pages already cited 龍巻 correctly. Pronunciation fields (lyonggwen/룡권/ㄌ⼄ㄫㄍ⼔ㄋ) already matched; mandarin's lóngjuǎn correctly reflects 巻's minority "to roll" verb-sense reading (juǎn) rather than its stored default noun-sense (juàn) — same reading-split pattern as [[拓]]/[[間]], not a bug. **Fixed a real `kwin` bug**: was `false`, contradicting the AND-rule (both 龍 and 巻 individually true) — corrected to `true`. **Filled the deliberately-left-blank `vietnamese` field**: prose had already researched and explained vòi rồng ("dragon's spout") as the real independently-coined Vietnamese term, but per the established real-attested-usage convention the field itself should hold it rather than stay blank — added `vietnamese: vòi rồng`. Korean's already-corrected `용오름` (from a prior pass) and Japanese たつまき were already correct. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 龍断.

### 2026-09-09, iteration 3795 — [[words/龍断|龍断]]
No cranberry (龍's own `stand_in` is 龍 itself, 断's is [[割断]] — neither points here). `characters:` already correctly disambiguated/bare as appropriate. Both character pages already cited 龍断 correctly. Fixed the duplicate `品詞`/`pos` field bug (590-file scope, fixed opportunistically). **Investigated and explained, rather than "fixed," an elaborate real-language-field divergence**: mandarin `lǒngduàn` (not `lóngduàn`), cantonese `lung5` (not `lung4`), korean `롱단` (not `룡단`), and vietnamese `lũng đoạn` (not matching 龍's own "long") all deliberately follow the real attested word 壟斷, not a naive compositional reading of 龍's own stored fields — traced directly to the word's own quoted Mencius passage, where 龍 was originally a phonetic loan for 壟 ("mound"); Dan'a'yo's own headword spelling/reading preserves the loan-form 龍 while every real-language field correctly tracks the actual pronunciation of 壟斷 (Korean's `롱단`/`농단` being the word behind the well-known 2016 "국정농단" scandal name). Japanese ろうだん already correctly uses 龍's own alternate on'yomi ROU. Fixed a stray "=" (should be "+") in the Notes citation line. Added missing `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 龍王.

### 2026-09-09, iteration 3796 — [[words/龍王|龍王]]
No cranberry (both 龍's and 王's own `stand_in` point to themselves — neither points here). `characters:` already correctly disambiguated (both `words/龍.md` and `words/王.md` exist). Both character pages already cited 龍王 correctly. Pronunciation fields (lyong'wang/룡왕/ㄌ⼄ㄫ·⺢ㄫ) and `kwin: true` (AND-rule: both true) already matched. **Fixed a real orthography bug**: `japanese` was written in obsolete historical kana spelling ("りゆうわう") instead of modern hiragana — corrected to りゅうおう, matching every sibling 王-compound's already-consistent "-おう" spelling ([[帝王]], [[冥王]], [[国王]], [[天王星]], [[海王星]]). Added an entirely missing `## Notes` section. Removed blank `hsk_level`/`swadesh`/empty `aliases: []`. Added missing `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 龍眼.

### 2026-09-09, iteration 3797 — [[words/龍眼|龍眼]]
No cranberry (龍's own `stand_in` is 龍 itself, 眼's is [[眼球]] — neither points here). `characters:` already correctly disambiguated/bare as appropriate; both character pages already cited 龍眼 correctly. Pronunciation fields (lyong'an/룡안/ㄌ⼄ㄫ·ㄚㄋ) and `kwin: true` (AND-rule: both true) already matched, including a previously-fixed `korean: 롱안→룡안` phonetic-borrowing bug already documented in the word's own rich existing prose. Fixed the duplicate `品詞`/`pos` field bug (590-file scope, fixed opportunistically). Quoted `mandarin`/`cantonese` for consistency. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 龍蝦.

### 2026-09-09, iteration 3798 — [[words/龍蝦|龍蝦]]
No cranberry (龍's own `stand_in` is 龍 itself, 蝦's is [[毛蝦]] — neither points here). `characters:` already correctly disambiguated/bare as appropriate; both character pages already cited 龍蝦 correctly. Pronunciation fields (lyongha/룡하/ㄌ⼄ㄫㄏㄚ) already matched. **Fixed a real `kwin` bug**: was `false`, contradicting the AND-rule (龍 true, 蝦 true) — corrected to `true`. **Fixed a real garbage-adjacent bug**: `korean` was `가재` ("crayfish/crawfish," a related but distinct freshwater crustacean) rather than lobster — corrected to `바닷가재` ("sea crayfish"), the real standard Korean word for lobster. Japanese イセエビ/Vietnamese tôm hùm already correctly real, everyday words. Converted informal `## Word` heading with a stray joke-bullet ("lobster's are the dragons of the shrimp world!") into a standard `## Notes` template with proper citation and explanatory prose. Removed blank `hsk_level`/`swadesh`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 龕.

### 2026-09-09, iteration 3799 — [[words/龕|龕]]
Self-standing bare-character word ("shrine, alcove"), found in a very incomplete state: bare frontmatter (`vietnamese: ''`, unlisted `characters: "龕 (char)"`, no `pos`, no `date-last-perfect`, no `japanese`) and only an empty `# Notes` heading with no content. **Found a real anticipated homophone**: both `words/勘.md` and `words/堪.md` already carried a reciprocal Homophones callout for 龕, flagged "still unperfected"/"awaiting its own turn" — added the reciprocal callout here (completing a genuine three-way Dan'a'yo homophone group, all reading kam/캄/ㄎㄚㄇ) and fixed the now-stale wording on both siblings. Filled `japanese: こん` (on'yomi, matching the character's own stored KON, with native ずし noted in prose as the narrower everyday term) and `vietnamese: khám` (Hán Việt, attested in khám thờ "shrine niche" — coincidentally the same spelling already used by [[勘]] for an unrelated sense, a genuine cross-language homophone collision, not a bug). Added missing `pos: 名詞`, converted `characters:` to proper list format with disambiguation, rebuilt `## Notes` with full etymology/pronunciation prose and `kwin` explanation (false: MC aspirated 溪母 kʰ → Dan'a'yo aspirated ㅋ vs Korean's plain ㄱ). Stamped `date-last-perfect: 2026-09-09`.

Next: 𧦅歌.

### 2026-09-09, iteration 3800 — [[words/𧦅歌|𧦅歌]]
Legitimizing note (𧦅's own `stand_in` is this exact compound; 歌's own is [[歌曲]] — transitivity fails, no `#cranberry`), already essentially present in prose though not labeled as such — labeled explicitly. `characters:` already correctly bare (no `words/𧦅.md`/`words/歌.md`). Both character pages already cited 𧦅歌 correctly. Pronunciation fields (`'ougǝ`/옷그/ㄛㄨㄍㄜ) and `kwin: false` (AND-rule: both false) already matched. **Fixed the non-canonical `pos: 動詞`** → `事詞` (matching 𧦅's own stored `pos`). Filled entirely missing `japanese: おうか` and `vietnamese: âu ca`, both real attested compounds corresponding to 謳歌 (𧦅 being a listed graphic-variant alias of 謳); `korean: 구가` already correct and additionally a real attested Sino-Korean word. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

**MILESTONE — FULL PASS COMPLETE**: 𧦅歌 was the alphabetically-last file in `words/*.md` under `LC_ALL=C` sort. The sweep now wraps around to the alphabetically-first word, [[㪘]], resuming iteration count without reset (per standing convention — iteration numbers track total words processed, not position within a single pass).

Next: 㪘.

### 2026-09-09, iteration 3801 — [[words/㪘|㪘]]
First iteration of the sweep's second pass. Self-standing bare-character word ("to gather, collect, restrain"), reciprocal Homophones callout with [[廉]] already correctly in place on both pages. `characters:` already correctly disambiguated. Pronunciation fields (lyem/렴/ㄌ⼶ㄇ) and `kwin: true` already matched. **Fixed the non-canonical `pos: 動詞`** on both this word page and `characters/㪘 (char).md` → `事詞`. **Fixed an empty-string `hsk_level: ""` bug** on the character page → `無` (not ranked). Quoted `mandarin`/`cantonese`/`korean` for consistency. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found only itself and 廉, both already cross-linked.

Next: 䋇.

### 2026-09-09, iteration 3802 — [[words/䋇|䋇]]
Self-standing bare-character word ("unravel, explain"). Reciprocal Homophones callout with [[駅]] (coincidental phonetic-series collision, already explained in prose) already correctly in place on both pages. All pronunciation and real-language fields (`'yeg`/역/⼶ㄎ, mandarin yì, cantonese jik6, korean 역, japanese やく, vietnamese dịch) already matched `characters/䋇 (char).md` exactly; `kwin: true` and `pos: 事詞` both correct. A fully clean pass — only quoted `mandarin`/`cantonese`/`korean` for consistency and refreshed the date stamp.

Next: 䔥国.

### 2026-09-09, iteration 3803 — [[words/䔥国|䔥国]]
Legitimizing note (䔥's own `stand_in` is this exact compound; 国's own is [[国家]] — transitivity fails, no `#cranberry`), already essentially present in prose, labeled explicitly. `characters:` already correctly bare (no `words/䔥.md`/`words/国.md`). Both character pages already cited 䔥国 correctly. Pronunciation fields (syaugog/샷곡/ㄙ⼘ㄨㄍㄛㄎ) and `kwin: false` (AND-rule: both false) already matched. Normalized `mandarin` from spaced lowercase "xiāo guó" to capitalized-proper-noun "Xiāoguó," matching sibling ancient-state words ([[蜀国]], [[鄂国]], [[斉国]]). Filled entirely missing `vietnamese: Tiêu quốc`, same capitalization convention. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 䦧.

### 2026-09-09, iteration 3804 — [[words/䦧|䦧]]
Self-standing bare-character word ("quarrel"). `characters:` already correctly disambiguated. Character page already cited 䦧 correctly. Pronunciation fields (heg/헉/ㄏㄝㄎ), `kwin: false`, and `pos: 事詞` all matched the character page exactly; japanese せめぐ already correctly the real native kun-reading over rarer on'yomi. **Fixed a comma-joined `vietnamese` contamination bug**: `"huých, huỵch"` — kept huých (the character's own stored reading), removed huỵch (an unrelated onomatopoeia for a thudding sound). Quoted `mandarin`/`cantonese`/`korean` for consistency. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 䦧神星.

### 2026-09-09, iteration 3805 — [[words/䦧神星|䦧神星]]
Celestial-body proper noun ("Eris, dwarf planet"), no stand-in relationship (all three constituents are their own stand-ins). All three character pages already cited 䦧神星 correctly. Pronunciation fields (hegsinseng/헉신성/ㄏㄝㄎㄙㄧㄋㄙㄝㄫ) and japanese けきしんせい already matched compositionally. **Added missing `kwin: false`** (AND-rule: 䦧 false, 神 true, 星 true — this word follows the plain AND-rule, not the periodic-table-neologism exception, consistent with sibling celestial words 冥王星/天王星). **Fixed `vietnamese` capitalization**: lowercase "huých thần tinh" → "Huých Thần Tinh," matching the proper-noun capitalization convention already used on 冥王星's "Diêm Vương Tinh" and 天王星's "Thiên Vương Tinh". Quoted `mandarin`/`cantonese`/`korean`. Added missing `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 一.

### 2026-09-09, iteration 3806 — [[words/一|一]]
Self-standing bare-character word ("one"), reciprocal three-way Homophones callout with [[壱]]/[[逸]] already correctly cross-linked on all three pages. Pronunciation fields (`'id`/읻/ㄧㄊ), `pos: 数詞`, `hsk_level`, `swadesh: 22`, and `vietnamese: nhất` all already matched `characters/一 (char).md` exactly. **Found and fixed a real frontmatter/prose self-contradiction bug**: frontmatter had `kwin: true`, but the word's own extensive prose paragraph explicitly explains and derives `kwin` as false (Dan'a'yo 읻 preserving the MC -t coda vs. Korean 일's historical -t→-l lenition) — matching the character page's own stored `kwin: false`. Corrected the frontmatter to `false`. Fixed the duplicate `品詞`/`pos` field bug (590-file scope, fixed opportunistically). Quoted `mandarin`/`cantonese`/`korean`. Stamped `date-last-perfect: 2026-09-09`.

Next: 一万.

### 2026-09-09, iteration 3807 — [[words/一万|一万]]
Legitimizing note (万's own `stand_in` is this exact compound — 万's reading 몬 is phonologically "overfull" and must always be spoken as 一万; 一's own `stand_in` is 一 itself — transitivity fails, no `#cranberry`). **Fixed a real bug on `characters/万.md`**: its own stored `cantonese` was `mak6`, phonologically implausible for this non-entering-tone MC final — corrected to `maan6`, matching what this word's own field already correctly used (the word itself was right; the character page was wrong). **Fixed a real citation gap**: `characters/一 (char).md`'s `## Words` list was missing 一万 entirely. Fixed a comma-joined `vietnamese` contamination bug (`"mười nghìn, vạn"` — kept vạn, the character's own stored and everyday-attested reading; mười nghìn noted in prose as the native numeral-phrase alternative). Removed the duplicate `品詞` field and restructured a stray "Stand-in for [[万]]" fragment into a proper `## Notes` template. Kept `hsk_level`/`swadesh`/`aliases: []` blank, matching the established convention for numeral-compound words (cf. [[十一]]). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 一体.

### 2026-09-09, iteration 3808 — [[words/一体|一体]]
No cranberry (体's own `stand_in` is [[体系]], 一's is 一 itself — neither points here). Both character pages already cited 一体 correctly. Pronunciation fields (`'idtei`/읻테/ㄧㄊㄊㄝㄧ) and `kwin: false` already matched, with the divergence already correctly explained in existing prose. **Fixed a real factual-accuracy bug in the prose itself** (not a frontmatter/field bug, a new variant): the Notes claimed 一's own `nhất` and 体's own `thể` were "blank on their individual character pages" and that this word's vietnamese field was independently researched rather than inherited — false on both counts; both character pages already stored these exact values, and had done so even before this word's own prior perfecting date. Corrected the claim. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 一億.

### 2026-09-09, iteration 3809 — [[words/一億|一億]]
Legitimizing note (億's own `stand_in` is this exact compound; 一's own is 一 itself — transitivity fails, no `#cranberry`). **Fixed a real citation gap**: `characters/一 (char).md`'s `## Words` list was missing 一億 entirely (億's own list already had it). Pronunciation fields (`'id'ig`/읻익/ㄧㄊ·ㄧㄎ) and `kwin: false` (AND-rule: both false) already matched. **Fixed a real bug**: `japanese` was `いち かた` — a stray space plus かた matching neither of 億's own stored on'yomi — corrected to いちおく (ICHI+OKU), the real standard word. Vietnamese `ức` confirmed correct (used alone, without a "one" prefix, matching [[一万]]'s established precedent for Vietnamese numeral compounds). Fixed the duplicate `品詞`/`pos` field bug and restructured a stray `>[!warn]` tip fragment into a proper template. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 一兆.

### 2026-09-09, iteration 3810 — [[words/一兆|一兆]]
No `#cranberry` (兆's own `stand_in` is [[前兆]], 一's is 一 itself — neither points here). **Fixed the exact structural bug already flagged reciprocally from [[一朝]]'s own page**: a plain-text "Stand-in for [[兆]]" line before the meta-bind-embed block — converted to a proper `>[!warning] Homophones` callout. **Fixed real "one"-prefix-dropped bugs**: `mandarin` was bare `zhào` (missing 一's yī) and `cantonese` was bare `siu6` (missing jat1) — both corrected, restoring the prefix pattern already established on [[一万]]/[[一億]]. **Fixed `japanese`**: was bare ちょう, missing the いち prefix and its expected sokuon assimilation (documented precedent: [[一体]]'s いったい) — corrected to いっちょう. Vietnamese `một triệu triệu` confirmed correct as the real Vietnamese circumlocution for "trillion" (kept, not reduced to a misleading bare "triệu" = "million"). Fixed a real citation gap on `characters/一 (char).md`. `kwin: false` already correct, matching the now-familiar 一-root-cause pattern (documented on 一定/一斉/一旦/一朝). Stamped `date-last-perfect: 2026-09-09`.

Next: 一処.

### 2026-09-09, iteration 3811 — [[words/一処|一処]]
`characters:` already correctly disambiguated (処's own `stand_in` is 処 itself — self-standing, no legitimizing note needed). Character page already cited 一処 correctly. Pronunciation fields (`'idco`/읻초/ㄧㄊㄑㄛ) and `kwin: false` already matched, with the divergence already explained in prose. **Fixed a real field-contamination bug**: `korean` jammed two candidates together with a period instead of proper separation, `"한데. 한곳"` — resolved to a single value, `한곳` (using 処's own stored native reading 곳), with 한데 kept as a documented near-synonym alternate in prose rather than in the field. Fixed the duplicate `品詞`/`pos` field bug. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 一切.

### 2026-09-09, iteration 3812 — [[words/一切|一切]]
`characters:` already correctly disambiguated. Character page already cited 一切 correctly. Pronunciation fields (`'idced`/읻첟/ㄧㄊㄑㄝㄊ) already matched. **Fixed a real garbage-adjacent bug**: `cantonese` was `jat1chai3` — missing the word-space and, worse, a second syllable (`chai3`) matching neither 切's own stored cantonese (`cit3`) nor any plausible reading — corrected to `jat1 cit3`. **Added a missing `kwin: false`** (AND-rule: both constituents individually false). Fixed the duplicate `品詞`/`pos` field bug. Korean's already-documented 일체/일절 doublet-reading fork and Vietnamese's already-documented semantic drift (nhất thiết, "necessarily," far from the Buddhist "all dharmas" source) were both already correct and richly explained. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 一千.

### 2026-09-09, iteration 3813 — [[words/一千|一千]]
Legitimizing note (千's own `stand_in` is this exact compound; 一's own is 一 itself — transitivity fails, no `#cranberry`). Character page already cited 一千 correctly. Pronunciation fields (`'idcen`/읻천/ㄧㄊㄑㄝㄋ) already matched. **Fixed a real `kwin` bug**: was `true`, contradicting the AND-rule (一 false, 千 true) — corrected to `false`. **Fixed `japanese`**: was bare せん, missing the いち prefix and its expected sokuon assimilation (same pattern as [[一体]]/[[一兆]]) — corrected to いっせん. Vietnamese một nghìn confirmed correct (real native numeral phrase, matching [[一万]]'s established preference over Sino-Vietnamese). Fixed the duplicate `品詞` field and restructured a stray "Stand-in for : [[千]]" fragment into a proper `## Notes` template. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 一半.

### 2026-09-09, iteration 3814 — [[words/一半|一半]]
Legitimizing note (半's own `stand_in` is this exact compound; 一's own is 一 itself — transitivity fails, no `#cranberry`). Character page already cited 一半 correctly, reciprocal Homophones callout with [[一般]] already correctly cross-linked on both pages. **Fixed a real comma-joined `mandarin` contamination bug**: `"yībànr,yībàn"` — kept the standard yībàn, moved the Beijing-dialect erhua variant to prose (already separately recorded among `aliases`). **Fixed a real `kwin` bug**: was `true`, contradicting the AND-rule (一 false, 半 true) — corrected to `false`. **New pattern noted**: `japanese: いっぱん` is not a bug despite superficially resembling 一般's own reading — it's the phonologically regular sokuon-assimilated form of いち+はん (半's own on'yomi HAN), and coincidentally matches 一般's real pronunciation exactly, a genuine cross-language homophone paralleling the already-documented Dan'a'yo-level one. Fixed the duplicate `品詞`/`pos` field. Kept `hsk_level`/`swadesh`/`aliases` per the numeral-word convention. Stamped `date-last-perfect: 2026-09-09`.

Next: 一定.

### 2026-09-09, iteration 3815 — [[words/一定|一定]]
No `#cranberry` (定's own `stand_in` is [[決定]], 一's is 一 itself — neither points here). Character page already cited 一定 correctly. All pronunciation and real-language fields (`'idjeng`/읻정/ㄧㄊㄐㄝㄫ, mandarin, cantonese, japanese いってい, korean, vietnamese nhất định) already matched `characters/定.md` exactly, `kwin: false` already correct — this word is the source of the earlier-documented 一(char) root-cause `kwin` fix. A fully clean pass — only refreshed the date stamp. Background exact-match homophone check found no collision.

Next: 一斉.

### 2026-09-09, iteration 3816 — [[words/一斉|一斉]]
Legitimizing note (斉's own `stand_in` is this exact compound) already correctly documented. Both character pages already cited 一斉 correctly. Confirmed `pos: 副詞` (adverb) is a legitimate category, widely used across 32 other files — not part of the confirmed `動詞`-only bug pattern. All pronunciation/real-language fields and `kwin: false` already correct from a prior thorough pass (which itself documented the same 一-root-cause kwin fix found on [[一定]]). A fully clean pass — only refreshed the date stamp. Background exact-match homophone check found no collision.

Next: 一日.

### 2026-09-09, iteration 3817 — [[words/一日|一日]]
No `#cranberry` (both 一's and 日's own `stand_in` point to themselves — neither points here). `characters:` already correctly disambiguated. Both character pages already cited 一日 correctly. Pronunciation fields and `kwin: false` already matched. Fixed a stray trailing "l" typo in `mandarin` (`yīrìl`→`yīrì`). **Fixed a comma-joined `japanese` contamination bug**: `"ついたち, いちにち"` — this compound genuinely covers two senses that Japanese splits into two distinct real words (ついたち for "1st of the month," いちにち for "one day" duration); kept ついたち as the field value (matching the word's first-listed calendrical sense) with いちにち documented in prose as the sense-specific alternate for the duration meaning. Restructured a stray `## Etymology` heading below a numbered `## Notes` list into a single standard `## Notes` template. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 一旦.

### 2026-09-09, iteration 3818 — [[words/一旦|一旦]]
Character page already cited 一旦 correctly. Confirmed `pos: 副用名詞` is a legitimate, widely-used category (38 files). All pronunciation/real-language fields and `kwin: false` already correct from a prior thorough pass (structural + korean contamination bugs already fixed there). A fully clean pass — only refreshed the date stamp. Background exact-match homophone check found no collision.

Next: 一月.

### 2026-09-09, iteration 3819 — [[words/一月|一月]]
No `#cranberry` (both 一's and 月's own `stand_in` point to themselves). Both character pages already cited 一月, though with a typo. **Fixed a real `kwin` bug**: was `true`, contradicting the AND-rule (一 false, 月 false) — corrected to `false`, the same recurring 一-root-cause pattern. **Fixed a real cantonese bug**: `jat1jut6` — missing both the word-space and the glide in 月's own stored `jyut6` — corrected to `jat1 jyut6`. **Fixed a real 注音 typo**: `ㄧㄊ·⼔ㄋ` (wrong final consonant) → `ㄧㄊ·⼔ㄊ`, fixed both in this word's own frontmatter and in its citation on `characters/月 (char).md`'s `## Words` list. **Flagged, not fixed**: the identical typo appears to also affect [[三月]]/[[十一月]]'s own citations on the same character page — left for when the sweep reaches those words directly. Vietnamese `tháng giêng` confirmed correct (a real native idiom specific to January, distinct from every other numbered month). Fixed the duplicate `品詞`/`pos` field. Stamped `date-last-perfect: 2026-09-09`.

Next: 一朝.

### 2026-09-09, iteration 3820 — [[words/一朝|一朝]]
No `#cranberry` (both 一's and 朝's own `stand_in` point to themselves). `characters:` already correctly disambiguated, character page already cited 一朝 correctly. Pronunciation fields and `kwin: false` already correct from a prior thorough pass. **Extended the already-documented reading-split observation**: confirmed the same by-sense split already noted for Vietnamese (triêu "morning" vs triều "dynasty") also holds for Mandarin (zhāo vs the character page's stored default cháo) and Cantonese (ziu1 vs stored ciu4) — all three now correctly using the morning-sense reading, not a bug. Fixed a stale cross-reference: the prose noted the reciprocal structural bug on [[一兆]] as "not yet fixed since perfecting it is a separate task" — 一兆 has since been perfected earlier in this sweep, so updated the wording. Stamped `date-last-perfect: 2026-09-09`.

Next: 一溝.

### 2026-09-09, iteration 3821 — [[words/一溝|一溝]]
`characters:` already correctly disambiguated. Pronunciation/real-language fields and `kwin: false` already correct from a prior thorough pass (including a deliberate, correctly-justified blank `vietnamese`). Japanese いっこう confirmed correct (regular sokuon assimilation of いち+こう). **Fixed a real citation gap**: `characters/一 (char).md`'s `## Words` list was missing 一溝 entirely (溝's own list already had it). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 一点.

### 2026-09-09, iteration 3822 — [[words/一点|一点]]
No `#cranberry` (both 一 and 点 are bare self-standing characters, own `stand_in` pointing to themselves). `characters:` already correctly disambiguated, both character pages already cited 一点 correctly. Pronunciation fields and `kwin: false` already correct from a prior thorough pass (including a real content bug already fixed there: gloss corrected from the literal "dot, speck" to the primary everyday "a little, a bit" quantifier sense). A fully clean pass — only refreshed the date stamp. Background exact-match homophone check found no collision.

Next: 一百.

### 2026-09-09, iteration 3823 — [[words/一百|一百]]
No `#cranberry` (both 一's and 百's own `stand_in` point to themselves). Character page already cited 一百 correctly. **Fixed the recurring `characters:` disambiguation bug**: bare "百" despite `words/百.md` existing (a genuine miss, unlike the many already-correct 一-cluster words checked so far). **Fixed a real japanese bug**: `いち ひゃく` (bare space-joined, no assimilation) → `いっぴゃく` (regular sokuon + h→p devoicing, same pattern as 一半/一体/一千). Vietnamese một trăm confirmed correct (real native numeral, matching 一万/一千's established preference). Fixed the duplicate `品詞` field and added an entirely missing `## Notes` section. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 一瞥.

### 2026-09-09, iteration 3824 — [[words/一瞥|一瞥]]
Legitimizing note (瞥's own `stand_in` is this exact compound; 一's own is 一 itself — transitivity fails, no `#cranberry`), already essentially present in prose, labeled explicitly. Character page already cited 一瞥 correctly. All pronunciation and real-language fields already matched `characters/瞥.md` exactly, `kwin: false` correct. A fully clean pass — added a brief explanatory pronunciation paragraph and refreshed the date stamp. Background exact-match homophone check found no collision.

Next: 一瞬.

### 2026-09-09, iteration 3825 — [[words/一瞬|一瞬]]
Legitimizing note (瞬's own `stand_in` is this exact compound; 一's own is 一 itself — transitivity fails, no `#cranberry`). Character page already cited 一瞬 correctly. Filled entirely missing `pos`, `korean: 일순`, `vietnamese: nhất thuấn`, and `kwin: false` (AND-rule: both false). **Fixed a real spelling-consistency bug**: `cantonese` was `jat1 seon3` — corrected to `jat1 seun3`, matching both 瞬's own stored cantonese and the already-perfected sibling [[瞬間]]'s own field. Japanese いっしゅん already correctly assimilated. Added an entirely missing `## Notes` section. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 一端.

### 2026-09-09, iteration 3826 — [[words/一端|一端]]
No `#cranberry` (端's own `stand_in` is [[末端]], 一's is 一 itself — neither points here). Character page already cited 一端 correctly. All pronunciation and real-language fields, `kwin: false`, already correct from a prior thorough pass (including a nicely-documented coincidental cross-language homophone with [[一旦]] in Japanese specifically, いったん, despite the two being semantically unrelated). A fully clean pass — only refreshed the date stamp. Background exact-match homophone check found no Dan'a'yo-level collision.

Next: 一致.

### 2026-09-09, iteration 3827 — [[words/一致|一致]]
No `#cranberry` (both 一's and 致's own `stand_in` point to themselves). `characters:` already correctly disambiguated, character page already cited 一致 correctly. All pronunciation and real-language fields already matched, `kwin: false` correct. Fixed the duplicate `品詞`/`pos` field, quoted `hsk_level`, and added an entirely missing `## Notes` section. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 一般.

### 2026-09-09, iteration 3828 — [[words/一般|一般]]
No `#cranberry` (both 一's and 般's own `stand_in` point to themselves). `characters:` already correctly disambiguated, character page already cited 一般 correctly, reciprocal Homophones callout with [[一半]] already correctly cross-linked (fixed a few iterations ago). `mandarin: yìbān` already correctly reflects regular tone-sandhi (一's yī→yì before a 1st-tone syllable) — clarified in prose, not a bug. **Fixed a real `kwin` bug**: was `true`, contradicting the AND-rule (一 false, 般 true) — corrected to `false`, the same recurring 一-root-cause pattern found repeatedly this stretch. Stamped `date-last-perfect: 2026-09-09`.

Next: 一角獣.

### 2026-09-09, iteration 3829 — [[words/一角獣|一角獣]]
`characters:` already correctly disambiguated (角's own word file exists, 獣's doesn't). All pronunciation and real-language fields, `kwin: false` (AND-rule: all three constituents false), already correct from a prior exceptionally thorough pass — including well-documented real divergences: cantonese/mandarin using the actually-attested 獨角獸/独角兽 alias form rather than a literal calque, and Vietnamese's genuine terminological conflation with the unrelated native 麒麟/qilin creature (kỳ lân), both correctly left as real cross-linguistic facts rather than "fixed." **Found a real citation gap**: `characters/角 (char).md`'s `## Words` list was missing 一角獣 entirely (獣's own list already had it). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 丁.

### 2026-09-09, iteration 3830 — [[words/丁|丁]]
Self-standing bare-character word ("fourth on a list of four"), reciprocal three-way Homophones callout with [[艇]]/[[釘]] already correctly cross-linked on all three pages. All pronunciation and real-language fields already matched `characters/丁 (char).md` exactly, `kwin: false` correct. Confirmed `pos: 修飾語` (a widely-used category, 52 files) is a legitimate divergence from the character's own stored `名詞` — the word's specific ordinal-modifier sense differs grammatically from the character's general noun sense. A fully clean pass — only refreshed the date stamp.

Next: 丁丁.

### 2026-09-09, iteration 3831 — [[words/丁丁|丁丁]]
Self-reduplication of [[丁]] (no cranberry logic needed). Character page already cited 丁丁 correctly. Confirmed `pos: 擬詞` (onomatopoeia) is a legitimate category (13 files). Pronunciation fields and `kwin: false` already correct, with a nicely-flagged classical-commentary detail (a historical zhēngzhēng reading distinct from the vault's modern dīng-based convention, left as a documented note rather than overhauled). Fixed a missing word-space in `cantonese` (`ding1ding1`→`ding1 ding1`). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 丁香.

### 2026-09-09, iteration 3832 — [[words/丁香|丁香]]
Both character pages already cited 丁香 correctly. All pronunciation and real-language fields, `kwin: false` (AND-rule: 丁 false, 香 true → false), already correct from a prior thorough pass — including a nicely-documented note on Japanese's more common but differently-written 丁子/丁字 (ちょうじ) form versus this word's own literal-spelling ちょうこう reading. A fully clean pass — only refreshed the date stamp. Background exact-match homophone check found no collision.

Next: 七.

### 2026-09-09, iteration 3833 — [[words/七|七]]
Self-standing bare-character word ("seven"), reciprocal Homophones callout with [[漆]] already correctly cross-linked. All pronunciation and real-language fields, `kwin: false`, already correct from a prior thorough pass. Fixed the duplicate `品詞`/`pos` field bug. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision beyond the already-documented 漆.

Next: 七万.

### 2026-09-09, iteration 3834 — [[words/七万|七万]]
All pronunciation and real-language fields, `kwin: false`, already correct from a prior thorough pass (which had already caught and fixed a serious prior bug: the whole page had once been a mistaken copy of [[七千]]'s content). **Fixed a real citation gap**: `characters/万.md`'s `## Words` list was missing 七万 entirely (七's own list already had it). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 七事.

### 2026-09-09, iteration 3835 — [[words/七事|七事]]
No `#cranberry` (both 七's and 事's own `stand_in` point to themselves). `characters:` already correctly disambiguated, both character pages already cited 七事 correctly. Pronunciation/kwin already correct. Filled entirely missing `vietnamese: thất sự` (plain compositional, classical/historical term). Quoted `mandarin`/`cantonese`/`korean`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 七十.

---
**LOOP MODE CHANGE**: user said "stop the loop and switch to continuous word perfecting" — cron job 070ee753 cancelled via CronDelete; processing now continues back-to-back within this single turn per [[feedback_continuous_loop_trigger]], no more waiting for 5-minute cron fires.

### 2026-09-09, iteration 3836 — [[words/七十|七十]]
No `#cranberry` (both 七's and 十's own `stand_in` point to themselves). Both character pages already cited 七十 correctly. **Fixed the recurring `characters:` disambiguation bug**: bare "十" despite `words/十.md` existing. **Fixed a real `kwin` bug**: was `true`, contradicting the AND-rule (七 false, 十 true) — corrected to `false`. Fixed two empty-string bugs (`vietnamese: ""`, `swadesh: ""`) and filled `vietnamese: bảy mươi`, the real native tens-numeral for "seventy." Japanese ななじゅう already correctly using native なな over しち. Fixed the duplicate `品詞` field. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 七千.

### 2026-09-09, iteration 3837 — [[words/七千|七千]]
Both character pages already cited 七千 correctly. All fields and `kwin: false` already correct from a prior thorough pass (this word was itself the source of the 七(char) kwin root-cause fix and the discovery of 七万's duplicated-content bug). A fully clean pass — only refreshed the date stamp.

Next: 七夕.

### 2026-09-09, iteration 3838 — [[words/七夕|七夕]]
No `#cranberry` (夕's own `stand_in` is [[夕陽]], 七's is 七 itself — neither points here). Character page already cited 七夕 correctly. **Fixed a real `kwin` bug**: was `true`, contradicting the AND-rule (七 false, 夕 true) — corrected to `false`. Fixed a missing word-space in `cantonese` (`cat1zik6`→`cat1 zik6`) and the duplicate `品詞` field. Japanese たなばた confirmed correct (a real native jukujikun reading for the whole compound, not built from individual on'yomi). Added an entirely missing `## Notes` section. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 七宝.

### 2026-09-09, iteration 3839 — [[words/七宝|七宝]]
No `#cranberry` (宝's own `stand_in` is [[宝物]], 七's is 七 itself — neither points here). Character page already cited 七宝 correctly. Pronunciation fields and `kwin: false` already matched. **Fixed a real bug**: `japanese` was しちほう, a bare unassimilated concatenation — corrected to しっぽう (real word, sokuon+devoicing, same pattern as 一半/一百). Quoted `mandarin`/`cantonese`/`korean`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 七対子.

### 2026-09-09, iteration 3840 — [[words/七対子|七対子]]
No `#cranberry` (none of the three constituents' own `stand_in` points here). Both remaining character pages already cited 七対子 correctly. Pronunciation fields, `kwin: false`, and Japanese ちいといつ (previously fixed malformed hiragana) already correct. Documented the deliberately-blank `vietnamese` field (no attested Vietnamese mahjong term found). Quoted `mandarin`/`cantonese`/`korean`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 七情.

### 2026-09-09, iteration 3841 — [[words/七情|七情]]
Both character pages already cited 七情 correctly (fixed a trivial `[[words/七情]]`→`[[七情]]` wikilink-path formatting slip on `七 (char).md` while there). All pronunciation and real-language fields, `kwin: false`, already correct from an exceptionally thorough prior pass (three-tradition emotion-enumeration comparison, Vietnamese idiom cross-check). A fully clean pass content-wise — only refreshed the date stamp.

Next: 七日.

### 2026-09-09, iteration 3842 — [[words/七日|七日]]
Both character pages already cited 七日 correctly. All pronunciation and real-language fields, `kwin: false`, already correct from a prior thorough pass, including a well-documented irregular native Japanese calendar reading (なのか, part of the same fossilized day-counting family as 一日/八日). A fully clean pass — only refreshed the date stamp.

Next: 七星.

### 2026-09-09, iteration 3843 — [[words/七星|七星]]
No `#cranberry` (both 七's and 星's own `stand_in` point to themselves). Both character pages already cited 七星 correctly. Pronunciation fields and `kwin: false` already matched. Filled entirely missing `vietnamese: thất tinh` and quoted the other real-language fields. Korean 칠성 confirmed as a real, well-known term (the Big Dipper deity in Korean folk religion/Buddhism). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 七曜.

### 2026-09-09, iteration 3844 — [[words/七曜|七曜]]
No `#cranberry` (曜's own `stand_in` is [[曜日]], 七's is 七 itself — neither points here). Character page already cited 七曜 correctly. Pronunciation fields and `kwin: false` already matched. Filled entirely missing `vietnamese: thất diệu` (a real Vietnamese astrological term). In passing, fixed an empty-string `hsk_level: ""` bug on `characters/曜.md` itself → `無`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 七月.

### 2026-09-09, iteration 3845 — [[words/七月|七月]]
No `#cranberry` (both 七's and 月's own `stand_in` point to themselves). Both character pages already cited 七月 correctly (no typo this time, unlike 一月's earlier ⼔ㄋ bug). **Fixed a real `kwin` bug**: was `true`, contradicting the AND-rule (七 false, 月 false) — corrected to `false`. **Fixed a real cantonese bug**: `cat1jut6` — missing both the word-space and the glide in 月's own stored `jyut6` — corrected to `cat1 jyut6`, the identical bug pattern already found on [[一月]]. Fixed the duplicate `品詞` field. Vietnamese tháng bảy confirmed correct (real native month-name). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 七百.

### 2026-09-09, iteration 3846 — [[words/七百|七百]]
Both character pages already cited 七百 correctly. All fields and `kwin: false` already correct from a prior thorough pass. A fully clean pass — only refreshed the date stamp.

Next: 七色.

### 2026-09-09, iteration 3847 — [[words/七色|七色]]
No `#cranberry` (色's own `stand_in` is [[色彩]], 七's is 七 itself — neither points here). Both character pages already cited 七色 correctly. Pronunciation and real-language fields, `kwin: false`, already correct. Japanese なないろ confirmed correct (real everyday word, not compositional しちしょく). Added missing `date-last-perfect: 2026-09-09` and quoted fields.

Next: 七角形.

### 2026-09-09, iteration 3848 — [[words/七角形|七角形]]
No `#cranberry` (none of the three constituents' own `stand_in` points here). All three character pages already cited 七角形 correctly. Pronunciation fields, `kwin: false` (AND-rule: all three false), already matched. Filled entirely missing `vietnamese: hình bảy góc`, matching the native "hình + number + góc" polygon-naming pattern already established on sibling [[三角形]]'s "hình ba góc" (not a Sino-Vietnamese thất giác form). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 七面鳥.

### 2026-09-09, iteration 3849 — [[words/七面鳥|七面鳥]]
No `#cranberry` (面's own `stand_in` is [[表面]], 七's and 鳥's are themselves — none points here). All three character pages already cited 七面鳥 correctly. Pronunciation fields, `kwin: false`, already matched. Filled entirely missing `vietnamese: gà tây` ("western chicken," the real everyday Vietnamese word, no compositional connection to the "seven faces" imagery — matching the real-attested-usage convention). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 万乗.

### 2026-09-09, iteration 3850 — [[words/万乗|万乗]]
No `#cranberry` (both 万's and 乗's own `stand_in` point to themselves). **Fixed a real citation gap**: `characters/万.md`'s `## Words` list was missing 万乗 entirely. **Fixed two real bugs**: `mandarin` had a stray internal space (`wàn chéng`), and `cantonese` carried the same `mak6` typo for 万 already found and fixed on the character page — corrected to `maan6 sing4`. Filled entirely missing `vietnamese: vạn thừa`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 万年.

### 2026-09-09, iteration 3851 — [[words/万年|万年]]
Both character pages already cited 万年 correctly. Pronunciation and real-language fields already correct — cantonese already correctly `maan6` (no propagated `mak6` typo here, unlike [[万乗]]). Only fix was the duplicate `品詞`/`pos` field. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 万歳.

### 2026-09-09, iteration 3852 — [[words/万歳|万歳]]
Both character pages already cited 万歳 correctly. Confirmed `pos: 感詞` (interjection) is a legitimate category (19 files). All pronunciation/real-language fields, `kwin: false`, already correct from an exceptionally thorough prior pass (Japanese ばんざい/まんざい dual-reading split, Korean 3.1 Movement history, Chinese imperial-taboo history all well documented). Only fix was the duplicate `品詞`/`pos` field. Stamped `date-last-perfect: 2026-09-09`.

Next: 万物.

### 2026-09-09, iteration 3853 — [[words/万物|万物]]
No `#cranberry` (万's own `stand_in` is [[一万]], 物's is 物 itself — neither points here). **Fixed a real citation gap**: `characters/万.md`'s `## Words` list was missing 万物 entirely (物's own list already had it). Confirmed the 萬物/万物 大字 (anti-falsification) pairing already correctly documented on 萬物's own page — mirrored that documentation onto this page, keeping `aliases: []` empty per the established 萬/万 non-cross-listing precedent. Fixed the duplicate `品詞` field and normalized `vietnamese` from a single-item list to a bare string. Stamped `date-last-perfect: 2026-09-09`.

Next: 万象.

### 2026-09-09, iteration 3854 — [[words/万象|万象]]
No `#cranberry` (万's own `stand_in` is [[一万]], 象's is [[大象]] — neither points here). Both character pages already cited 万象 correctly. Pronunciation fields, `kwin: false`, already matched. **Fixed a real semantic-mismatch bug**: `vietnamese` was capitalized `Vạn Tượng` — the real Vietnamese name for Vientiane (capital of Laos), a coincidentally-homographic but completely unrelated proper noun — corrected to lowercase `vạn tượng`, matching 象's own stored reading and the word's actual meaning. Fixed the duplicate `品詞` field. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 万邦.

### 2026-09-09, iteration 3855 — [[words/万邦|万邦]]
No `#cranberry` (万's own `stand_in` is [[一万]], 邦's is [[連邦]] — neither points here). Both character pages already cited 万邦 correctly. Filled an entirely missing `cantonese: maan6 bong1`. Fixed the duplicate `品詞` field. `kwin: false` already correct. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision. This closes out the 万-prefixed word cluster.

Next: 丈.

### 2026-09-09, iteration 3856 — [[words/丈|丈]]
Self-standing bare-character word ("zhang," unit of length). Pronunciation fields and `kwin: false` already matched `characters/丈 (char).md` exactly. Fixed the duplicate `品詞`/`pos` field and normalized single-item `japanese`/`vietnamese` lists to bare strings. **Fixed a real citation gap**: the character page had no `## Words` section at all (only a nonstandard `## Definition` heading) — added a minimal `## Words` section with the missing self-citation, leaving the rest of the rough character page for the character-perfection sweep. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 丈人.

### 2026-09-09, iteration 3857 — [[words/丈人|丈人]]
`characters:` already correctly disambiguated. **Fixed a real internal-consistency bug**: `羅馬字`/`注音` had been stored using the wrong unaspirated onset (`jangnin`/`ㄐㄚㄫㄋㄧㄋ`) — inconsistent with this word's own already-correct `諺文: 창닌` and with 丈's own stored triple (cang/창/ㄑㄚㄫ) — corrected to `cangnin`/`ㄑㄚㄫㄋㄧㄋ`. The identical typo had also propagated into this word's own citation on `characters/丈 (char).md`'s Words list, fixed there too. Fixed a real citation gap on `characters/人 (char).md`'s Words list (missing 丈人 entirely). `kwin: false` already correct regardless. Stamped `date-last-perfect: 2026-09-09`.

Next: 丈夫.

### 2026-09-09, iteration 3858 — [[words/丈夫|丈夫]]
No `#cranberry` (both 丈's and 夫's own `stand_in` point to themselves). **Found and fixed a significant real bug**: `羅馬字`/`諺文`/`注音` had been built from the SINO-KOREAN compositional reading (jangbu/장부/ㄐㄚㄫㄅㄨ, i.e. 丈's own Korean 장 + 夫's own Korean 부) rather than Dan'a'yo's own derivation — corrected to the proper mechanical concatenation of each constituent's own stored Dan'a'yo triple (cangfǝ/창쁘/ㄑㄚㄫㄈㄜ). The identical error had propagated into this word's own citations on both `丈 (char).md` and `夫 (char).md`'s Words lists, fixed there too. Documented Japanese じょうぶ as a genuine false-friend divergence (means "robust/healthy" in Japanese, not "husband," despite being the real reading of this exact written compound) and Korean 장부's own real meaning ("a great man," not "husband" — reinforcing why the native 남편 is correctly used instead). Fixed the duplicate `品詞` field. Stamped `date-last-perfect: 2026-09-09`.

Next: 丈母.

### 2026-09-09, iteration 3859 — [[words/丈母|丈母]]
No `#cranberry` (丈's own `stand_in` is 丈 itself, 母's is [[母親]] — neither points here). **Fixed the same Sino-Korean-vs-Dan'a'yo mix-up already found on [[丈夫]]**: `羅馬字`/`諺文`/`注音` had been built from 丈's Korean 장 rather than Dan'a'yo's own 창 — corrected to `cangmou`/`창못`/`ㄑㄚㄫㄇㄛㄨ`. Same propagated typo fixed on both character-page citations. Filled entirely missing `vietnamese: mẹ vợ` (real native compound, matching [[丈人]]'s "bố vợ"). Normalized single-item `japanese` list to a bare string. Stamped `date-last-perfect: 2026-09-09`. This closes out the 丈-prefixed word cluster.

Next: 三.

### 2026-09-09, iteration 3860 — [[words/三|三]]
Self-standing bare-character word ("three"). Pronunciation fields and `kwin: true` already matched `characters/三 (char).md` exactly (self-standing). **Found and corrected a real over-claim in the prose**: the Notes asserted 三 "has a dedicated anti-forgery/financial variant... [[参]]," matching the completed [[一]]/[[壱]] and [[七]]/[[漆]] pairs — but `characters/参.md`'s own `stand_in` actually points to [[参加]], not to itself, and no `words/参.md` exists; corrected the claim to flag this as NOT yet implemented rather than asserting it as done. Fixed the duplicate `品詞`/`pos` field and removed a stray misplaced `hanmun_edu_level` field (a character-page-only field that had leaked into this word file). Normalized the non-standard opening tip line to the standard `>[!tip]` callout format. Stamped `date-last-perfect: 2026-09-09`.

Next: 三位一体.

### 2026-09-09, iteration 3861 — [[words/三位一体|三位一体]]
No `#cranberry` (none of the four constituents' own `stand_in` points here). All four character pages already cited 三位一体 correctly. All pronunciation and real-language fields, `kwin: false`, already correct. Japanese さんみいったい confirmed correct (a real special classical/Buddhist alternate on'yomi for 位, み instead of い — not a bug). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 三十.

### 2026-09-09, iteration 3862 — [[words/三十|三十]]
Both character pages already cited 三十 correctly. Pronunciation fields and `kwin: true` (AND-rule: both true) already matched. **Fixed the recurring `characters:` disambiguation bug**: bare "十" despite `words/十.md` existing. Vietnamese ba mươi and Japanese みそじ/さんじゅう split already correctly documented. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 三十一日.

### 2026-09-09, iteration 3863 — [[words/三十一日|三十一日]]
No stand-in relationship (all four constituents independent). **Fixed several real bugs**: `mandarin`/`cantonese` had been entirely blank; `japanese` held a stray middle-dot separator instead of plain concatenation; `vietnamese` held the cardinal-number phrase "ba mươi mốt" ("thirty-one") rather than the compositional day-of-month form matching sibling words [[十一日]]/[[七日]]. Fixed the recurring `characters:` disambiguation bug and the duplicate `品詞` field. Confirmed (matching precedent on [[十一日]]) that day-numbered compounds like this one are not systematically cross-cited on every constituent character's own Words list, only on 日's — not a bug, left as-is. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 三十日.

### 2026-09-09, iteration 3864 — [[words/三十日|三十日]]
No stand-in relationship. Character page already cited 三十日 correctly. Japanese みそか confirmed correct (real special native reading, not the expected compositional さんじゅうにち — same "last day of month" irregular-reading family as [[一日]]'s ついたち). Filled entirely missing `vietnamese: tam thập nhật`. Fixed the recurring `characters:` disambiguation bug and the duplicate `品詞` field. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 三叉.

### 2026-09-09, iteration 3865 — [[words/三叉|三叉]]
`characters:` already correctly disambiguated. Both character pages already cited 三叉 correctly. All pronunciation and real-language fields, `kwin: false`, already correct from a prior thorough pass (trigeminal-nerve medical-vocabulary cross-check, Vietnamese native-phrase divergence both already documented). A fully clean pass — only refreshed the date stamp.

Next: 三国.

### 2026-09-09, iteration 3866 — [[words/三国|三国]]
Both character pages already cited 三国 correctly. Pronunciation fields, `kwin: false`, already matched. **Fixed a structural formatting bug**: the reciprocal homophone with [[三角]] was expressed as a non-standard `>[!tip]` line before the meta-bind-embed block instead of a proper `>[!warning] Homophones` callout — converted (the identical issue exists on 三角's own reciprocal side, flagged for when that word is reached). Quoted `mandarin`/`cantonese`/`korean`. Stamped `date-last-perfect: 2026-09-09`.

Next: 三日.

### 2026-09-09, iteration 3867 — [[words/三日|三日]]
No stand-in relationship. Character page already cited 三日 correctly. Japanese みっか confirmed correct (real special native reading, same irregular-day-reading family as 一日/三十日). Filled entirely missing `mandarin`/`cantonese`/`vietnamese`. Fixed the duplicate `品詞` field. `kwin: false` correct. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 三月.

### 2026-09-09, iteration 3868 — [[words/三月|三月]]
No stand-in relationship. **Fixed three real bugs, the same family already found on [[一月]]/[[七月]]**: `cantonese` missing 月's glide (jut6→jyut6); `注音` carrying the ⼔ㄋ-for-⼔ㄊ typo (fixed here and in this word's own citation on `月 (char).md`); `kwin: true` contradicting the AND-rule (三 true, 月 false) — corrected to `false`. Fixed the duplicate `品詞` field. Stamped `date-last-perfect: 2026-09-09`.

Next: 三焦.

### 2026-09-09, iteration 3869 — [[words/三焦|三焦]]
No stand-in relationship. Both character pages already cited 三焦 correctly. **Fixed a real orthography bug**: `japanese` was obsolete historical kana (さんせう) instead of modern さんしょう, the same bug family as [[龍王]]. Filled entirely missing `vietnamese: tam tiêu` (real standard TCM term). Fixed the duplicate `品詞` field. **Found a genuine new Dan'a'yo homophone**: shares its exact reading with [[参照]] ("refer to, cross-reference") — added reciprocal `>[!warning] Homophones` callouts on both pages; in passing on 参照 also fixed its non-canonical `pos: 動詞`→`事詞` and quoted its real-language fields. Stamped `date-last-perfect: 2026-09-09` on both files.

Next: 三猿.

### 2026-09-09, iteration 3870 — [[words/三猿|三猿]]
`characters:` fine (猿 bound but usable in other compounds beyond its own stand_in legitimizer [[猿猩]]). Character citation present (bare-format, on the already-flagged rough 三(char) page). **Fixed a comma-joined `japanese` contamination bug**: さんざる (the real, famous popular reading for this cultural icon, Nikkō Tōshō-gū's "see/hear/speak no evil" monkeys) kept, さんえん removed as a less-common alternate. **Fixed a real garbage-value bug**: `vietnamese` was `phiên âm` ("phonetic transcription," totally unrelated) → `tam viên` (compositional, matching 猿's own stored `viên`). Fixed the duplicate `品詞` field. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 三稜鏡.

### 2026-09-09, iteration 3871 — [[words/三稜鏡|三稜鏡]]
All three character pages already cited 三稜鏡 correctly. All pronunciation and real-language fields, `kwin: false`, already correct from an exceptionally thorough prior pass (Korean loanword divergence, Vietnamese etymology cross-check both already documented). Added an explicit legitimizing-note label (稜's own `stand_in` is this exact compound). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 三綱.

### 2026-09-09, iteration 3872 — [[words/三綱|三綱]]
Character page already cited 三綱 correctly. All pronunciation and real-language fields, `kwin: true` (AND-rule: both true), already correct from a prior thorough pass (Dong Zhongshu/Chunqiu Fanlu history, Vietnamese scholarship cross-check already documented). A fully clean pass — only refreshed the date stamp.

Next: 三菱.

### 2026-09-09, iteration 3873 — [[words/三菱|三菱]]
Fixed a real citation gap on `characters/菱 (char).md`'s Words list. Added missing `kwin: true` (AND-rule: both true) and filled missing `vietnamese: Mitsubishi` (loanword, matching Korean's own phonetic-loan approach). Fixed the duplicate `品詞` field. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 三角.

### 2026-09-09, iteration 3874 — [[words/三角|三角]]
Both character pages already cited 三角 correctly. Pronunciation fields, `kwin: false`, already matched. **Fixed the reciprocal structural bug already flagged from [[三国]]'s own page**: non-standard `>[!tip]` homophone line before the meta-bind-embed block — converted to a proper `>[!warning] Homophones` callout. Fixed the duplicate `品詞` field and quoted real-language fields. Stamped `date-last-perfect: 2026-09-09`.

Next: 三角形.

### 2026-09-09, iteration 3875 — [[words/三角形|三角形]]
No `#cranberry` (none of the three constituents' own `stand_in` points here). Fixed a real citation gap on `characters/角 (char).md`'s Words list. Fixed the duplicate `品詞` field, added an entirely missing `## Notes` section. All other fields already correct — this is the source precedent for the vietnamese hình-N-góc polygon-naming pattern later applied to 七角形. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 三角法.

### 2026-09-09, iteration 3876 — [[words/三角法|三角法]]
No `#cranberry`. Fixed real citation gaps on both `characters/三 (char).md` and `characters/角 (char).md`'s Words lists (法's own list already had it). Fixed the duplicate `品詞` field, added an entirely missing `## Notes` section. Vietnamese lượng giác học confirmed correct (real standard term, not a calque). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision. This closes out the 三-prefixed word cluster.

Next: 上.

### 2026-09-09, iteration 3877 — [[words/上|上]]
Self-standing bare-character word ("above"), reciprocal three-way Homophones callout with [[尚]]/[[賞]] already correctly cross-linked on all three pages. Pronunciation fields and `kwin: false` already matched. **Fixed a real YAML-structure bug**: `characters: 上 (char)` was a bare scalar instead of a proper list. Fixed the duplicate `品詞`/`pos` field and normalized single-item `japanese`/`vietnamese` lists to bare strings. Stamped `date-last-perfect: 2026-09-09`.

Next: 上位.

### 2026-09-09, iteration 3878 — [[words/上位|上位]]
Both character pages already cited 上位 correctly. All fields and `kwin: false` already correct from a prior thorough pass. A fully clean pass — only quoted fields and refreshed the date stamp.

Next: 上半期.

### 2026-09-09, iteration 3879 — [[words/上半期|上半期]]
No `#cranberry`. All three character pages already cited 上半期 correctly. Pronunciation fields, `kwin: false`, already matched. Filled entirely missing `vietnamese: thượng bán kì`. Quoted real-language fields. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 上帝.

### 2026-09-09, iteration 3880 — [[words/上帝|上帝]]
No `#cranberry` (帝's own `stand_in` is [[帝王]], 上's is 上 itself — neither points here). Fixed a real citation gap on `characters/上 (char).md`'s Words list. **Fixed a cantonese spelling-consistency bug**: `soeng6 dai3` → `seong6 dai3`, matching 上's own stored cantonese; noted a genuine seong6/soeng6 split exists across the vault's 上-word family (roughly half each way) worth a fuller audit later. `kwin: false` already correct. Stamped `date-last-perfect: 2026-09-09`.

Next: 上弦.

### 2026-09-09, iteration 3881 — [[words/上弦|上弦]]
No `#cranberry`. Fixed a real citation gap on `characters/上 (char).md`'s Words list (弦's own list already had it). Filled entirely missing `vietnamese: thượng huyền`. Quoted real-language fields. `kwin: false` correct. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 上旬.

### 2026-09-09, iteration 3882 — [[words/上旬|上旬]]
No `#cranberry` (旬's own `stand_in` is [[旬日]], 上's is 上 itself). **Fixed a real garbage-value bug**: `cantonese` was `sang4 xun2` — neither syllable real Jyutping; `xun2` appears to be leftover Mandarin pinyin (旬's own mandarin is xún) misplaced into the cantonese field — corrected to `seong6 ceon4`. Fixed a missing citation on `characters/上 (char).md`'s Words list and the duplicate `品詞` field. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 上昇.

### 2026-09-09, iteration 3883 — [[words/上昇|上昇]]
Legitimizing note already present (昇's own `stand_in` is this exact compound). All content already correct from a prior thorough pass. Fixed the recurring cantonese `soeng6`→`seong6` spelling bug and a missing citation on `characters/上 (char).md`'s Words list. Stamped `date-last-perfect: 2026-09-09`.

Next: 上海.

### 2026-09-09, iteration 3884 — [[words/上海|上海]]
No `#cranberry`. Reciprocal homophone with [[傷害]] already correctly cross-linked. **Fixed a structural bug**: the Homophones callout sat before the meta-bind-embed block, violating the required order — moved. Fixed the recurring cantonese `soeng6`→`seong6` spelling bug and a missing citation on `characters/上 (char).md`'s Words list. Japanese しゃんはい confirmed correct (real proper-noun reading). Stamped `date-last-perfect: 2026-09-09`. This finishes the run of 上(char) citation-gap fixes found this stretch (上帝/上弦/上旬/上/上半期/上昇/上海 — seven gaps in a row).

Next: 上知.

### 2026-09-09, iteration 3885 — [[words/上知|上知]]
Both character pages already cited 上知 correctly. All content already correct from a prior thorough pass (Analects/Joseon-scholar historical detail already well documented). Fixed the recurring cantonese `soeng6`→`seong6` spelling bug and quoted fields. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 上述.

### 2026-09-09, iteration 3886 — [[words/上述|上述]]
Both character pages already cited 上述 correctly (上's own citation in the already-flagged rough bare-link format). All content already correct from a prior thorough pass. Fixed the recurring cantonese `soeng6`→`seong6` spelling bug. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 上面.

### 2026-09-09, iteration 3887 — [[words/上面|上面]]
Both character pages already cited 上面 correctly. All content already correct from a prior thorough pass (register-comparison across five languages already well documented). Fixed the recurring cantonese `soeng6`→`seong6` spelling bug. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision. This closes out the 上-prefixed word cluster.

Next: 下.

### 2026-09-09, iteration 3888 — [[words/下|下]]
Self-standing bare-character word ("down, under"), reciprocal Homophones callout with [[何]] already correctly cross-linked. Pronunciation fields and `kwin: true` already matched. Fixed the duplicate `品詞`/`pos` field and normalized single-item `japanese`/`vietnamese` lists to bare strings. Stamped `date-last-perfect: 2026-09-09`.

Next: 下位.

### 2026-09-09, iteration 3889 — [[words/下位|下位]]
Both character pages already cited 下位 correctly. All content already correct, including japanese かい (correctly compositional KA+I). A fully clean pass — only quoted fields and refreshed the date stamp.

Next: 下半期.

### 2026-09-09, iteration 3890 — [[words/下半期|下半期]]
No `#cranberry`. All three character pages already cited 下半期 correctly. Filled entirely missing `vietnamese: hạ bán kì` (matching sibling 上半期's own pattern). Quoted real-language fields. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 下弦.

### 2026-09-09, iteration 3891 — [[words/下弦|下弦]]
Both character pages already cited 下弦 correctly. Filled entirely missing `vietnamese: hạ huyền` (matching sibling 上弦's own thượng huyền). Quoted real-language fields. `kwin: false` correct. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 下愚.

### 2026-09-09, iteration 3892 — [[words/下愚|下愚]]
Both character pages already cited 下愚 correctly. `kwin: true` (AND-rule: both true) already correct; the注音 dot-disambiguation from [[好]]/[[毫]] (both genuinely ㄏㄚㄨ without a dot) already correctly explained in prose — confirmed not a real collision, just a documented near-miss. Quoted fields. Stamped `date-last-perfect: 2026-09-09`.

Next: 下旬.

### 2026-09-09, iteration 3893 — [[words/下旬|下旬]]
No `#cranberry`. Both character pages already cited 下旬 correctly. **Fixed a real garbage-value bug identical to the one found on [[上旬]]**: `cantonese` was `xia4 xun2` — leftover Mandarin pinyin syllables mistakenly placed in the cantonese field — corrected to `haa6 ceon4`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 下痢.

### 2026-09-09, iteration 3894 — [[words/下痢|下痢]]
Legitimizing note (痢's own `stand_in` is this exact compound) already essentially present, labeled explicitly. Character page already cited 下痢 correctly. All content already correct from an exceptionally thorough prior pass (Korean 설사-vs-하리 divergence, Japanese げり coincidental-match, Vietnamese classical-vs-modern register all well documented). Stamped `date-last-perfect: 2026-09-09`.

Next: 下降.

### 2026-09-09, iteration 3895 — [[words/下降|下降]]
Legitimizing note (降's own `stand_in` is this exact compound). Both character pages already cited 下降 correctly. Filled entirely missing `vietnamese: hạ giáng` and added an entirely missing `## Notes` section. `kwin: true` (AND-rule: both true) correct. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 下顎.

### 2026-09-09, iteration 3896 — [[words/下顎|下顎]]
Legitimizing note (顎's own `stand_in` is this exact compound). **Fixed a real 注音 typo**: missing middle-dot before 顎's vowel-initial reading (ㄏㄚㄚㄎ→ㄏㄚ·ㄚㄎ), matching the already-correct citation on `characters/下 (char).md` but fixing the same wrong typo propagated onto `characters/顎.md`'s own citation. **Fixed a real `kwin` bug**: was `false`, contradicting the AND-rule (both 下 and 顎 individually true) — corrected to `true`. Japanese あご/Korean 턱/Vietnamese xương hàm all confirmed correct (real native words). Removed blank `hsk_level`/`swadesh`/`aliases`. Stamped `date-last-perfect: 2026-09-09`. This closes out the 下-prefixed word cluster.

Next: 不.

### 2026-09-09, iteration 3897 — [[words/不|不]]
Self-standing bare-character word ("not"), the core negation particle. Pronunciation fields and `kwin: false` already matched. Confirmed `pos: 修飾語` legitimate. Fixed the duplicate `品詞`/`pos` field and quoted real-language fields. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 不丹.

### 2026-09-09, iteration 3898 — [[words/不丹|不丹]]
Both character pages already cited 不丹 correctly, reciprocal homophone with [[不但]] already correctly cross-linked. All content already correct from an exceptionally thorough prior pass (Bhutan etymology, Dzongkha name, UN history all well documented). Only quoted fields and refreshed the date stamp.

Next: 不亦V乎.

### 2026-09-09, iteration 3899 — [[words/不亦V乎|不亦V乎]]
Special discontinuous-circumfix entry (Classical Chinese rhetorical-question frame, 不亦……乎), already thoroughly perfected with well-reasoned deliberate-blank-field justification for the daughter-language fields (no independent life outside Classical Chinese literary grammar). Fixed a real citation gap: `characters/不 (char).md`'s Words list was missing this entry (亦/乎's own lists already had it). Stamped `date-last-perfect: 2026-09-09`.

Next: 不但.

### 2026-09-09, iteration 3900 — [[words/不但|不但]]
Reciprocal homophone with [[不丹]] already correctly cross-linked. Deliberate blank japanese/korean/vietnamese fields already correctly justified (a genuinely Mandarin-specific grammatical particle with no cross-linguistic parallel at all). **Fixed the recurring `characters:` disambiguation bug**: bare "但" despite `words/但.md` existing — corrected to "但 (char)", and fixed the prose's stale claim to match. Stamped `date-last-perfect: 2026-09-09`.

Next: 不信.

### 2026-09-09, iteration 3901 — [[words/不信|不信]]
Both character pages already cited 不信 correctly. Pronunciation fields and `kwin: false` already correct. Documented Korean 불신 (not 부신) as a real regular Sino-Korean assimilation rule (matching 불가능/불편), not a bug. Fixed the duplicate `品詞` field. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 不及.

### 2026-09-09, iteration 3902 — [[words/不及|不及]]
Both character pages already cited 不及 correctly. **Fixed a real bug**: `korean` was `부급` (naive concatenation) — the real attested reading (confirmed via the famous idiom 과유불급) is `불급`, following the same 不→불 assimilation rule just documented on [[不信]]. Quoted real-language fields. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 不可.

### 2026-09-09, iteration 3903 — [[words/不可|不可]]
Fixed a real citation gap on `characters/不 (char).md`'s Words list (可's own list already had it). Korean 불가 already correctly following the 不→불 assimilation rule. Added an entirely missing `## Notes` section and `date-last-perfect: 2026-09-09`.

Next: 不可不.

### 2026-09-09, iteration 3904 — [[words/不可不|不可不]]
No `#cranberry`. Both character pages already cited 不可不 correctly. Filled entirely missing `cantonese: bat1 ho2 bat1`. Added missing `date-last-perfect: 2026-09-09`. Completes the modal square with [[可]]/[[不可]]/[[可不]] already cross-linked in prose.

Next: 不可以.

### 2026-09-09, iteration 3905 — [[words/不可以|不可以]]
All three character pages already cited 不可以 correctly. All content already correct from an exceptionally thorough prior pass (deliberate blank japanese/korean already justified, Vietnamese attestation caveat already documented). A fully clean pass — only refreshed the date stamp.

Next: 不同.

### 2026-09-09, iteration 3906 — [[words/不同|不同]]
Both character pages already cited 不同 correctly. Korean 부동 confirmed correct (no 불 assimilation here; the famous 不同/不動 homophone-collision already well documented). Fixed a missing word-space in `cantonese`. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 不均.

### 2026-09-09, iteration 3907 — [[words/不均|不均]]
Both character pages already cited 不均 correctly. Filled entirely missing `japanese: ふきん` and `korean: 불균` — the real attested reading (confirmed via 불균형 "imbalance"), following the 不→불 assimilation rule (3rd confirmed instance: 不信/不及/不均). Quoted fields. Stamped `date-last-perfect: 2026-09-09`.

Next: 不安.

### 2026-09-09, iteration 3908 — [[words/不安|不安]]
Both character pages already cited 不安 correctly. All content already correct from an exceptionally thorough prior pass (Heidegger/Kierkegaard translation history, 不穏 contrast all well documented). Korean 불안 already correctly following the assimilation rule. Only quoted fields and refreshed the date stamp.

Next: 不定.

### 2026-09-09, iteration 3909 — [[words/不定|不定]]
Both character pages already cited 不定 correctly. All content already correct from an exceptionally thorough prior pass (grammatical/mathematical/general-usage tricategorization all well documented). Fixed a stray internal space in `mandarin` (bù dìng→bùdìng). Quoted fields. Stamped `date-last-perfect: 2026-09-09`.

Next: 不平.

### 2026-09-09, iteration 3910 — [[words/不平|不平]]
Both character pages already cited 不平 correctly. Fixed a missing word-space in `cantonese` and quoted `hsk_level`. Korean 불평 already correctly following the assimilation rule (4th confirmed instance), additionally the everyday word for "complaint." Added an entirely missing `## Notes` section and removed blank `swadesh`/`aliases`. Stamped `date-last-perfect: 2026-09-09`.

Next: 不幸.

### 2026-09-09, iteration 3911 — [[words/不幸|不幸]]
Both character pages already cited 不幸 correctly. Fixed a missing word-space in `cantonese` and quoted `hsk_level`. Korean 불행 already correctly following the assimilation rule. Added an entirely missing `## Notes` section and removed blank `swadesh`/`aliases`. Stamped `date-last-perfect: 2026-09-09`.

Next: 不当.

### 2026-09-09, iteration 3912 — [[words/不当|不当]]
Both character pages already cited 不当 correctly. Korean 부당 confirmed correct (不→불 assimilation does not apply before this consonant, a genuine non-application). Added an entirely missing `## Notes` section and removed blank `hsk_level`/`swadesh`. Stamped `date-last-perfect: 2026-09-09`.

Next: 不断.

### 2026-09-09, iteration 3913 — [[words/不断|不断]]
Both character pages already cited 不断 correctly. All content already correct from an exceptionally thorough prior pass (行/朝-style Vietnamese reading-split, ふだん/普段 true-homophone documentation both well done). **Fixed a comma-joined `cantonese` contamination bug**: `"bat1 dyun6, bat1 tyun5"` — kept bat1 dyun6, matching 断's own stored reading. Stamped `date-last-perfect: 2026-09-09`.

Next: 不満.

### 2026-09-09, iteration 3914 — [[words/不満|不満]]
Both character pages already cited 不満 correctly. Pronunciation fields, `kwin: false`, already correct. Korean 불만 confirmed correct. Added an entirely missing Notes prose paragraph. Stamped `date-last-perfect: 2026-09-09`.

Next: 不用.

### 2026-09-09, iteration 3915 — [[words/不用|不用]]
Both character pages already cited 不用 correctly. This word's own prose independently CONFIRMS the exact 不→불/부 rule already deduced this stretch ("不 reads 부 mainly before ㄷ/ㅈ-initial syllables and 불 otherwise") — nice corroboration. Also documents a genuine Japanese 不用/不要 near-homophone collision and a real Vietnamese gap (no calque exists, honestly left blank). Fixed a missing word-space in `cantonese`. Stamped `date-last-perfect: 2026-09-09`.

Next: 不穏.

### 2026-09-09, iteration 3916 — [[words/不穏|不穏]]
Both character pages already cited 不穏 correctly. All content already correct from an exceptionally thorough prior pass (Chinese-concrete/Japanese-ominous/Korean-politically-charged register comparison already well documented). Fixed a stray internal space in `mandarin`. Quoted fields. Stamped `date-last-perfect: 2026-09-09`.

Next: 不穏素.

### 2026-09-09, iteration 3917 — [[words/不穏素|不穏素]]
Periodic-table neologism series (astatine): already correctly following convention (mandarin/cantonese give the avoided real element character 砹's own reading; korean/japanese/vietnamese are IUPAC-name loanwords; `kwin: false` correctly compares Dan'a'yo against Korean). Fixed a real citation gap: `characters/不 (char).md`'s Words list was missing this entry. Fixed the duplicate `品詞` field. Stamped `date-last-perfect: 2026-09-09`.

Next: 不要.

### 2026-09-09, iteration 3918 — [[words/不要|不要]]
Both character pages already cited 不要 correctly. All content already correct from a thorough prior pass (Mandarin-prohibitive vs Japanese/Korean-descriptive-only false-friend split already well documented). Fixed a missing word-space in `cantonese`. Quoted fields. Stamped `date-last-perfect: 2026-09-09`.

Next: 不許.

### 2026-09-09, iteration 3919 — [[words/不許|不許]]
Both character pages already cited 不許 correctly. All content already correct from a prior thorough pass. A fully clean pass — only refreshed the date stamp.

Next: 不過.

### 2026-09-09, iteration 3920 — [[words/不過|不過]]
Both character pages already cited 不過 correctly. All content already correct from a prior thorough pass (dual limiting-adverb/conjunction sense, deliberate blank japanese, Vietnamese exact-match all well documented). A fully clean pass — only refreshed the date stamp. This closes out the 不-prefixed word cluster.

Next: 与.

### 2026-09-09, iteration 3921 — [[words/与|与]]
Self-standing bare-character word ("and, with"), reciprocal three-way Homophones callout with [[魚]]/[[輿]] already correctly cross-linked on all three pages. All content already correct from an exceptionally thorough prior pass (full CJKV conjunction-vocabulary comparison, MC-vowel-correspondence explanation already well documented). A fully clean pass — only refreshed the date stamp.

Next: 与格.

### 2026-09-09, iteration 3922 — [[words/与格|与格]]
Both character pages already cited 与格 correctly. All content already correct from a prior thorough pass (case-name suffix pattern cross-linking to 8 sibling case-terms already documented). Fixed the duplicate `品詞` field, quoted fields, tidied trailing blank lines. Stamped `date-last-perfect: 2026-09-09`. This closes out the 与-prefixed word cluster.

Next: 丑月.

### 2026-09-09, iteration 3923 — [[words/丑月|丑月]]
No `#cranberry`. `kwin: false` (AND-rule: 丑 true, 月 false) correct. Fixed a real citation gap: `characters/丑.md` had no `## Words` section at all — added minimal section with the self-relevant citation, leaving the page's other rough spots (duplicate `## Notes` heading, dangling CC wikilinks) flagged out-of-scope. Fixed the duplicate `品詞` field and normalized single-item `japanese`/`vietnamese` lists to bare strings. Stamped `date-last-perfect: 2026-09-09`.

Next: 且.

### 2026-09-09, iteration 3924 — [[words/且|且]]
Self-standing bare-character word ("also, too"). **Fixed a real self-reference bug in the reciprocal homophone callout**: both this page and [[処]]'s own page had their callouts pointing to themselves instead of the other party ("[[且]] is a homophone of [[処]]" written ON 且's own page, and the mirror-image error on 処's) — corrected both to the standard format naming only the OTHER word. Fixed the duplicate `品詞` field. Stamped `date-last-perfect: 2026-09-09`.

Next: 且爵.

### 2026-09-09, iteration 3925 — [[words/且爵|且爵]]
Both character pages already cited 且爵 correctly. **Fixed the non-canonical `pos: 動詞`** → `事詞`. Clarified an imprecise prose claim: 爵's "stand-in for 嚼" role here is a special ad-hoc graphemic reuse specific to this one compound only, distinct from 爵's own official `stand_in` ([[男爵]], "baron," unrelated in meaning) — corrected the character-page citation format label too ("stand-in for 嚼"→"stand-in for 咀嚼", matching 爵's own page). Deliberately-blank vietnamese already correctly justified. Stamped `date-last-perfect: 2026-09-09`.

Next: 世仇.

### 2026-09-09, iteration 3926 — [[words/世仇|世仇]]
`characters:` already correctly bare (no words/世.md or words/仇.md). Both character pages already cited 世仇 correctly. Filled entirely missing `vietnamese: thế cừu` and added missing `date-last-perfect: 2026-09-09`. Quoted fields. `kwin: false` correct.

Next: 世代.

### 2026-09-09, iteration 3927 — [[words/世代|世代]]
Legitimizing note (代's own `stand_in` is this exact compound). Both character pages already cited 世代 correctly. Fixed a missing word-space in `cantonese`. Added an entirely missing `## Notes` section. Stamped `date-last-perfect: 2026-09-09`.

Next: 世宗.

### 2026-09-09, iteration 3928 — [[words/世宗|世宗]]
Both character pages already cited 世宗 correctly. Added missing `kwin: false` (AND-rule: 世 false, 宗 true). Quoted `korean`. Stamped `date-last-perfect: 2026-09-09`.

Next: 世界.

### 2026-09-09, iteration 3929 — [[words/世界|世界]]
Legitimizing note (世's own `stand_in` is this exact compound; 界's own is [[境界]] — transitivity fails, no `#cranberry`). **Fixed a real 注音 typo** propagated onto `characters/世.md`'s own citation (ㄙㄝㄐ⼶→ㄙㄝㄍ⼶, wrong onset). Added an entirely missing `## Notes` section and `date-last-perfect: 2026-09-09`.

Next: 世界観.

### 2026-09-09, iteration 3930 — [[words/世界観|世界観]]
No `#cranberry`. All three character pages already cited 世界観 correctly. Added an entirely missing `## Notes` section and `date-last-perfect: 2026-09-09`.

Next: 世界語.

### 2026-09-09, iteration 3931 — [[words/世界語|世界語]]
No `#cranberry`. All three character pages already cited 世界語 correctly (界's own citation clarifies "Esperanto" specifically). Added an entirely missing `## Notes` section clarifying the specific Esperanto referent and `date-last-perfect: 2026-09-09`.

Next: 世紀.

### 2026-09-09, iteration 3932 — [[words/世紀|世紀]]
Legitimizing note (紀's own `stand_in` is this exact compound) already present. Both character pages already cited 世紀 correctly, along with a large family of sibling 世紀-compounds. A fully clean pass — only refreshed the date stamp.

Next: 世紀中.

### 2026-09-09, iteration 3933 — [[words/世紀中|世紀中]]
No `#cranberry`. Fixed a real citation gap on `characters/中 (char).md`'s Words list (世/紀's own lists already had it). Filled entirely missing `vietnamese: giữa thế kỷ` (native word-order-reversed, real natural phrase). Quoted fields. Stamped `date-last-perfect: 2026-09-09`.

Next: 世紀初.

### 2026-09-09, iteration 3934 — [[words/世紀初|世紀初]]
No `#cranberry`. All three character pages already cited 世紀初 correctly. Filled entirely missing `vietnamese: đầu thế kỷ` (native word-order-reversed, matching sibling 世紀中's pattern). Quoted fields. Stamped `date-last-perfect: 2026-09-09`.

Next: 世紀末.

### 2026-09-09, iteration 3935 — [[words/世紀末|世紀末]]
No `#cranberry`. All three character pages already cited 世紀末 correctly. Filled entirely missing `vietnamese: cuối thế kỷ` (matching sibling 世紀中/世紀初 pattern). Quoted fields. Stamped `date-last-perfect: 2026-09-09`.

Next: 世間.

### 2026-09-09, iteration 3936 — [[words/世間|世間]]
Both character pages already cited 世間 correctly. All content already correct from an exceptionally thorough prior pass (Ruth Benedict/Chie Nakane cultural-concept documentation, 間's own reading-split correctly using the "between" default sense, not "interval"). Only quoted fields and refreshed the date stamp. This closes out the 世-prefixed word cluster.

Next: 丘.

### 2026-09-09, iteration 3937 — [[words/丘|丘]]
Self-standing bare-character word ("hill"), reciprocal Homophones callout with [[九]] already correctly cross-linked. All content already correct from a prior thorough pass (Confucius naming-taboo, khâu/khưu Vietnamese variant, native おか/언덕 alternates all well documented). A fully clean pass — only refreshed the date stamp.

Next: 丘引.

### 2026-09-09, iteration 3938 — [[words/丘引|丘引]]
`characters:` already correctly disambiguated. Both character pages already cited 丘引 correctly. Filled entirely missing `vietnamese: giun đất` (real native word, matching the established real-attested-usage convention) and added a missing `## Notes` section. Japanese みみず confirmed correct (real native word, not compositional きゅういん). `kwin` false correct (AND-rule: 丘 false alone determines the result). Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 丙.

### 2026-09-09, iteration 3939 — [[words/丙|丙]]
Self-standing bare-character word ("third class, tertiary"). **Fixed stale wording**: the three-way homophone group with [[坪]]/[[柄]] was described as "still awaiting their own turn" — both are now already perfected, so corrected to reflect the completed mutual cross-link (matching the established 鮑/報-style stale-wording fix pattern). Filled a previously-missing `japanese: へい` field. In passing, fixed a stray blank line inside [[柄]]'s own Homophones callout. Stamped `date-last-perfect: 2026-09-09`.

Next: 両.

### 2026-09-09, iteration 3940 — [[words/両|両]]
Self-standing bare-character word ("both"), reciprocal three-way Homophones callout with [[梁]]/[[糧]] already correctly cross-linked. All content already correct from a prior thorough pass (兩/両/輛 shinjitai-collapse history, tael/vehicle-classifier senses, Korean North-Korean-form note all well documented). Normalized single-item `japanese`/`vietnamese` lists to bare strings. In passing, fixed the same stray-blank-line glitch (already seen on 柄) in both [[梁]]'s and [[糧]]'s own Homophones callouts. Stamped `date-last-perfect: 2026-09-09`.

Next: 両親.

### 2026-09-09, iteration 3941 — [[words/両親|両親]]
Both character pages already cited 両親 correctly. All content already correct from an exceptionally thorough prior pass (父母 register comparison, 双親/song thân Vietnamese near-synonym caveat, Korean 두음법칙-adjacent divergence all well documented). Cantonese loeng5 (vs 両's own stored loeng2) confirmed as a real, standard Cantonese tone divergence for this specific compound, not a bug — left as-is. A fully clean pass — only refreshed the date stamp.

Next: 並.

### 2026-09-09, iteration 3942 — [[words/並|並]]
Self-standing bare-character word ("side by side"). **Fixed stale wording**: [[瓶]] was described as "still awaiting its own turn" — it's already perfected and already reciprocally cross-linked, so corrected the phrasing. Filled a previously-missing `japanese: へい` field. Stamped `date-last-perfect: 2026-09-09`.

Next: 並列.

### 2026-09-09, iteration 3943 — [[words/並列|並列]]
No `#cranberry`. `characters:` already correctly disambiguated/bare as appropriate, both character pages already cited 並列 correctly. Filled entirely missing `vietnamese: tịnh liệt`. **Fixed a redundant self-referential `aliases: [並列]` entry** — same bug variant previously fixed on [[熊鼠]]/[[鼠色]]. Quoted fields. Stamped `date-last-perfect: 2026-09-09`.

Next: 並立.

### 2026-09-09, iteration 3944 — [[words/並立|並立]]
Both character pages already cited 並立 correctly. All content already correct from a prior thorough pass (five-way cross-linguistic attestation, including Vietnamese tịnh lập confirmed via web search, all well documented). A fully clean pass — only refreshed the date stamp. This closes out the 並-prefixed word cluster.

Next: 中.

### 2026-09-09, iteration 3945 — [[words/中|中]]
Self-standing bare-character word (the progressive aspect marker "-ing"). Pronunciation fields and `kwin: true` already matched. All content already correct from a prior thorough pass (full CJKV progressive-aspect comparison chart, [[公]] phonological parallel already documented). Fixed the duplicate `品詞`/`pos` field and quoted real-language fields. Stamped `date-last-perfect: 2026-09-09`. Background exact-match homophone check found no collision.

Next: 中世.

### 2026-09-09, iteration 3946 — [[words/中世|中世]]
Both character pages already cited 中世 correctly. All content already correct from a prior thorough pass (Vietnamese trung thế's narrower Japanese-periodization-specific scope vs. broader trung đại/trung cổ already well documented). A fully clean pass — only refreshed the date stamp.

Next: 中亜.

### 2026-09-09, iteration 3947 — [[words/中亜|中亜]]
Both character pages already cited 中亜 correctly. Added missing `kwin: true` (AND-rule: both 中 and 亜 individually true). Quoted `korean`. Stamped `date-last-perfect: 2026-09-09`.

Next: 中原.

### 2026-09-09, iteration 3948 — [[words/中原|中原]]
**Fixed a real bug the word's own prose had already diagnosed but never corrected**: `japanese` was なかはら, a coincidental Japanese surname/placename unrelated in meaning — the prose itself said so, but the wrong value stayed in the field — corrected to ちゅうげん, the real on'yomi compositional reading used in Japanese sinological writing. Filled an entirely missing `注音` field. Fixed real citation gaps on both `characters/中 (char).md` (was a bare unformatted wikilink) and `characters/原.md`'s (missing entirely) Words lists. Fixed the duplicate `品詞` field.

Next: 中古.

### 2026-09-09, iteration 3949 — [[words/中古|中古]]
**Fixed a real garbled-value bug**: `vietnamese` was `đồ đả dùng qua` (wrong word "đả" for "đã," non-standard word order) — corrected to trung cổ, the real, standard Sino-Vietnamese word for "medieval," matching the word's own senses 2/3; noted the real native phrase (đồ đã qua sử dụng) for the distinct "secondhand goods" sense in prose. Fixed a missing citation on `characters/中 (char).md`'s Words list. Normalized `english` from a bare string to a proper list. Quoted real-language fields. Stamped `date-last-perfect: 2026-09-09`.

Next: 中国.

### 2026-09-09, iteration 3950 — [[words/中国|中国]]
**Fixed a real citation gap my own earlier full-scan false-negatived**: `characters/中 (char).md` had no proper `## Words` citation for 中国, only a bare "short for [[中国]]" mention under a separate `## Definitions` list — the earlier scan's substring match wrongly counted that as satisfying the check. Added the proper ruby-formatted citation. Fixed the duplicate `品詞` field. `国`'s own citation and the systematic 곡/국 divergence explanation (already generalized to [[中国人]]/[[中国語]]/[[中華民国]]) were already correct. Stamped `date-last-perfect: 2026-09-09`.

Next: 中国人.

### 2026-09-09, iteration 3951 — [[words/中国人|中国人]]
**Fixed a real missing-field bug**: `注音` was entirely absent from the frontmatter — added `ㄐㄨㄫㄍㄛㄎㄋㄧㄋ`, matching 国's own citation. Fixed real citation gaps on both `characters/中 (char).md` (was a bare unformatted wikilink) and `characters/人 (char).md` (missing entirely). Fixed the duplicate `品詞` field and lowercased an over-capitalized `vietnamese` ("Người Trung Quốc"→"người Trung Quốc," only the country name warrants capitals).

Next: 中国語.

### 2026-09-09, iteration 3952 — [[words/中国語|中国語]]
**Fixed a real missing-field bug**: `注音` was entirely absent — added `ㄐㄨㄫㄍㄛㄎ⼄`, matching 語's/国's own citations. Fixed a real citation gap on `characters/中 (char).md` (bare unformatted wikilink). Fixed the duplicate `品詞` field and an over-capitalized `vietnamese` ("Tiếng Trung Quốc"→"tiếng Trung Quốc," matching [[中国人]]'s fix).

Next: 中央.

### 2026-09-09, iteration 3953 — [[words/中央|中央]]
Legitimizing note (央's own `stand_in` is this exact compound). **Fixed a real `kwin` bug**: was `true`, contradicting the AND-rule (中 true, 央 false) — corrected to `false`. Fixed a citation gap on `characters/中 (char).md` (bare "short for" mention upgraded to proper ruby citation). Quoted `hsk_level`, removed blank `swadesh`/`aliases`. Added an entirely missing `## Notes` section. Stamped `date-last-perfect: 2026-09-09`.

Next: 中央情報局.

### 2026-09-09, iteration 3954 — [[words/中央情報局|中央情報局]]
`characters:` already correctly bare/disambiguated. All five constituent character pages already cited 中央情報局 correctly. All content already correct from a prior thorough pass (CIA/1947 National Security Act history, KCIA borrowing history both well documented). `kwin: false` correct. A fully clean pass — only refreshed the date stamp.

Next: 中子.

### 2026-09-09, iteration 3955 — [[words/中子|中子]]
All content already exceptionally thoroughly documented from a prior pass (the "middle son" vs. "neutron" homograph carefully disambiguated, Vietnamese deliberately left blank with full justification). **Fixed a real duplicate-citation bug**: `characters/中 (char).md`'s Words list had cited 中子 twice — once correctly and once erroneously glossed "neutron" with a garbled non-matching 注音 — removed the erroneous duplicate (this vault has no separate neutron word file). Stamped `date-last-perfect: 2026-09-09`.

Next: 中学校.

### 2026-09-09, iteration 3956 — [[words/中学校|中学校]]
**Fixed a real missing-field bug**: `注音` was entirely absent — added `ㄐㄨㄫㄏㄚㄎㄏ⼘ㄨ`, matching 学's own citation. Fixed a real citation gap on `characters/校.md` (missing entirely) and upgraded a bare unformatted citation on `characters/中 (char).md`. Fixed the duplicate `品詞` field.

Next: 中庭.

### 2026-09-09, iteration 3957 — [[words/中庭|中庭]]
Legitimizing note (庭's own `stand_in` is this exact compound). **Fixed several real bugs**: `注音` was entirely missing — added `ㄐㄨㄫㄉㄝㄫ`, matching 庭's own citation; upgraded a bare unformatted citation on `characters/中 (char).md`; removed the duplicate `品詞` field.

Next: 中庸.

### 2026-09-09, iteration 3958 — [[words/中庸|中庸]]
No `#cranberry`. Both character pages already cited 中庸 correctly. **Fixed the recurring `characters:` disambiguation bug**: both "中" and "庸" needed the "(char)" suffix (both `words/中.md` and `words/庸.md` exist) — a double instance in one word. `kwin: true` (AND-rule: both true) correct. Removed blank `hsk_level`/`swadesh`/`aliases`. Added an entirely missing `## Notes` section.

Next: 中心.

### 2026-09-09, iteration 3959 — [[words/中心|中心]]
Both character pages already cited 中心 correctly (中's own upgraded from bare to proper ruby format). All other content already correct from a prior thorough pass. Fixed the duplicate `品詞` field. Stamped `date-last-perfect: 2026-09-09`.

Next: 中性子.

### 2026-09-09, iteration 3960 — [[words/中性子|中性子]]
Confirms [[中子]]'s own claim: this IS the vault's separate "neutron" word (中 "neutral" + 性 "charge/nature" + 子 "particle"), distinct from 中子's "middle son" sense — no conflict. All content already exceptionally thoroughly documented (Chadwick 1932 discovery, Japanese Meiji-Taishō scientific-coinage system, Vietnamese phonetic-borrowing choice all well documented). Upgraded two bare unformatted citations on `characters/子.md` and `characters/中 (char).md` to proper ruby format. Stamped `date-last-perfect: 2026-09-09`.

Next: 中指.

### 2026-09-09, iteration 3961 — [[words/中指|中指]]
No `#cranberry`. Both character pages already cited 中指 correctly. **Fixed a real cantonese bug**: `zong1 zi3` → `zung1 zi2`, the proper compositional concatenation. **Removed a false, already-disproven homophone claim**: the page asserted "same sound as [[曽子]]," but [[曽子]]'s own page had already investigated and rejected this exact claim (注音 ㄐㄜㄫㄐㄜ vs this word's ㄐㄨㄫㄐㄧㄜ, no match) — the reciprocal stale claim on this side was simply never cleaned up. Restructured into standard `## Notes` template. Stamped `date-last-perfect: 2026-09-09`.

Next: 中文.

### 2026-09-09, iteration 3962 — [[words/中文|中文]]
Both character pages already cited 中文 correctly (中's own upgraded from bare to proper ruby format). All other content already correct from a prior thorough pass. Fixed the duplicate `品詞` field. Stamped `date-last-perfect: 2026-09-09`.

Next: 中日韓越.

### 2026-09-09, iteration 3963 — [[words/中日韓越|中日韓越]]
`characters:` already correctly disambiguated/bare as appropriate. **Fixed several real bugs**: `cantonese` used non-breaking spaces (U+00A0) instead of regular spaces AND was missing 越's own syllable entirely — required a Python-based fix since the invisible NBSP characters didn't match ordinary Edit tool string matching; `mandarin` had a tone-mark placement typo (Yùe→Yuè, matching 越's own stored yuè). Fixed a missing citation on `characters/韓.md`'s Words list and the duplicate `品詞` field. Added an entirely missing `## Notes` section.

Next: 中旬.

### 2026-09-09, iteration 3964 — [[words/中旬|中旬]]
Both character pages already cited 中旬 correctly (中's own upgraded from bare to proper ruby format). Cantonese zung1 ceon4 already correctly matches the fix pattern established on sibling 上旬/下旬. All other content already correct from a prior thorough pass. Fixed the duplicate `品詞` field. Stamped `date-last-perfect: 2026-09-09`.

Next: 中止.

### 2026-09-09, iteration 3965 — [[words/中止|中止]]
Legitimizing note (止's own `stand_in` is this exact compound) already essentially present, labeled explicitly. Both character pages already cited 中止 correctly. Filled entirely missing `vietnamese: trung chỉ`. Stamped `date-last-perfect: 2026-09-09`.

Next: 中秋節.

### 2026-09-09, iteration 3966 — [[words/中秋節|中秋節]]
All three character pages already cited 中秋節 correctly. All content already correct from a prior thorough pass (嫦娥/后羿 mythology, Korean 추석/Chuseok structural contrast, cross-referenced 仲秋/桂月/秋分 all well documented). Fixed the duplicate `品詞` field and quoted fields. Stamped `date-last-perfect: 2026-09-09`.

Next: 中等.

### 2026-09-09, iteration 3967 — [[words/中等|中等]]
Found and fixed a duplicate-citation bug on `characters/等 (char).md`: an old bare-format `## Words` list (中等/初等/同等/優等/劣等, plus still-unique 平等/恒等式/等分/等待) sat alongside a newer properly ruby-formatted list further down that had re-added 高等/中等/初等/同等/優等/劣等 with correct 注音. Removed the 5 confirmed-duplicated old bare entries, keeping 平等/恒等式/等分/等待 (not yet migrated) untouched. `kwin: false` on 中等 itself confirmed correct via AND-rule (中's kwin true + 等's own kwin false = false). Content (三-tier 初等/中等/高等 hierarchy, 等's bamboo-tablet etymology) already thorough from a prior pass. Quoted mandarin/cantonese/korean fields, no homophone collision on ㄐㄨㄫㄉㄨㄫ. Stamped `date-last-perfect: 2026-09-09`.

Next: 中耳.

### 2026-09-09, iteration 3968 — [[words/中耳|中耳]]
Citation on `中(char)` was still bare-format (`[[中耳]]`); upgraded to proper ruby-formatted entry matching `耳(char)`'s already-correct citation. Fixed duplicate `pos`/`品詞` field, quoted mandarin/cantonese. `kwin: false` confirmed correct via AND-rule (中 true + 耳's own kwin false = false). No homophone collision on ㄐㄨㄫㄋㄧ. Content already thorough (anatomy, MC 日-initial n-/∅ split cross-referenced with 中国人's 人). Stamped `date-last-perfect: 2026-09-09`.

Next: 中華.

### 2026-09-09, iteration 3969 — [[words/中華|中華]]
Substantially incomplete before this pass: `characters:` used undisambiguated `中` despite `words/中.md` existing, `date-last-perfect` was entirely absent, `hsk_level`/`swadesh` sat as dangling empty fields, `pos` was 性詞 (adjective-like) rather than 固有名詞 to match sibling proper-noun culture/place terms (中国/中亜/中日韓越), and the whole Notes section was a single stray fragment ("syn . 台湾") instead of real content. Disambiguated 中→中 (char), removed empty fields, fixed pos, normalized aliases to block-list form, wrote full Notes (civilizational-vs-political contrast with 中国, 中華民国/中華人民共和国, 中華料理 in Japanese, Vietnamese Trung Hoa vs Trung Quốc). `kwin: true` confirmed correct via AND-rule (中/華 both true). Citations already present and correctly ruby-formatted on both `中(char)` and `華.md`. No homophone collision on ㄐㄨㄫㄏ⺢. Stamped `date-last-perfect: 2026-09-09`.

Next: 中華民国.

### 2026-09-09, iteration 3970 — [[words/中華民国|中華民国]]
Citation on `中(char)` was still bare-format (`[[中華民国]]`); upgraded to proper ruby entry matching the already-correct citations on 華/民/国. Fixed duplicate `pos`/`品詞` field, quoted mandarin/cantonese, caught my own mistyped korean old_string on the first Edit attempt (typed hanja 中華民国 instead of the actually-stored Hangul 중화민국 — same recurring self-transcription error) and corrected on retry. `kwin: false` confirmed via 4-way AND-rule (中/華/民 true, 国 false). Content already thorough (ROC vs PRC distinction, 곡/국 divergence cross-referenced with 中国人/中国語). No homophone collision. Stamped `date-last-perfect: 2026-09-09`.

Next: 中間.

### 2026-09-09, iteration 3971 — [[words/中間|中間]]
Found the systemic missing-注音 bug: frontmatter had no `注音` field at all. Derived and added ㄐㄨㄫㄍㄚㄋ (中's ㄐㄨㄫ + 間's own ㄍㄚㄋ), matching 間.md's own citation. Also upgraded 中(char)'s still-bare citation (`[[中間]]`) to proper ruby format, fixed duplicate `pos`/`品詞`, quoted mandarin/cantonese. `kwin: true` confirmed via AND-rule (中/間 both true). Content already thorough (間's "interval/gap" contrast with 中心's "core/hub" sense). No homophone collision. Stamped `date-last-perfect: 2026-09-09`. This closes out the 中-prefixed word cluster; next word begins a new initial (串).

Next: 串.

### 2026-09-09, iteration 3972 — [[words/串|串]]
Found a missing `japanese` field entirely absent from frontmatter despite Notes discussing both Japanese readings (セン/カン on'yomi, くし kun'yomi). Established (via cross-checking 上/丁/丙, all of which pick their character page's first-listed on'yomi for the stand-in word) that the vault convention is: first-listed on'yomi wins. 串(char)'s own `japanese: [SEN, KAN]` → added せん. Documented the convention explicitly in the word's own Notes. `kwin: false` trivially confirmed (single constituent, character's own kwin false). No homophone collision on ㄐ⺢ㄇ. Stamped `date-last-perfect: 2026-09-09`.

Next: 丹砂.

### 2026-09-09, iteration 3973 — [[words/丹砂|丹砂]]
Already fully correct from a prior pass: `characters:` bare 丹 confirmed right (no `words/丹.md` exists), `沙 (char)` disambiguation correct, `kwin: true` confirmed via AND-rule, legitimizing note (丹's own `stand_in: 丹砂`) confirmed, citations correctly ruby-formatted on both character pages, and the reciprocal Homophones callout with [[単詞]] (real, anchored-grep-confirmed collision on 注音 ㄉㄚㄋㄙㄚ) already in standard format on both pages. Just refreshed `date-last-perfect: 2026-09-09`.

Next: 丹金.

### 2026-09-09, iteration 3974 — [[words/丹金|丹金]]
Periodic-table-neologism word (hafnium, via Copenhagen→Denmark→丹 two-step toponymic reduction) — `kwin` correctly uses the neologism exception (compares word's own 諺文 vs its own korean field directly, not constituent AND-rule), already thoroughly explained in Notes. Found and fixed a missing citation on `金 (char).md` (丹金 wasn't listed at all); added it with the periodic-table-neologism annotation matching its siblings (蛍金/隠金/難金/雷金). No homophone collision on ㄉㄚㄋㄍㄧㄇ. Stamped `date-last-perfect: 2026-09-09`.

Next: 丹麦.

### 2026-09-09, iteration 3975 — [[words/丹麦|丹麦]]
Fixed an unspaced cantonese field ("daan1mak6"→"daan1 mak6") to match the vault's overwhelming space-separated-syllable convention. `characters:` bare 丹/麦 both confirmed correct (neither has a `words/*.md` conflict). `kwin: false` confirmed via AND-rule (丹 true, 麦 false). Citations correct on both character pages. No homophone collision. Cross-checked the terse "Purely phonetic" Notes style against [[瑞典]] (same pattern) — confirmed this is the accepted vault convention for transliterated country names, not a content gap; noted 瑞典's own separate bugs (duplicate 品詞, malformed vietnamese field) for when its turn comes up alphabetically. Stamped `date-last-perfect: 2026-09-09`.

Next: 主人.

### 2026-09-09, iteration 3976 — [[words/主人|主人]]
Substantially incomplete: `date-last-perfect` entirely absent, dangling empty `swadesh`/`aliases` fields, vietnamese wrongly capitalized ("Chủ nhân"→"chủ nhân", common noun not proper noun), and no `## Notes` section at all. Wrote full Notes covering the legitimizing note (主's own `stand_in: 主人`), cross-CJKV usage (主人公/女主人/男主人, Japanese しゅじん's "one's own husband" sense, 주인공/주인의식, chủ nhân của), and the kwin explanation (人's MC 日-initial n-/∅ split, same as [[中国人]]/[[中耳]]). Found and fixed a missing citation on `人(char).md`. `kwin: false` confirmed via AND-rule (主 true, 人 false). No homophone collision. Stamped `date-last-perfect: 2026-09-09`.

Next: 主婦.

### 2026-09-09, iteration 3977 — [[words/主婦|主婦]]
Already fully correct from a prior pass: `characters:` disambiguation confirmed right on both sides (bare 主, disambiguated `婦 (char)`), `kwin: false` confirmed via AND-rule, citations correctly ruby-formatted on both character pages, no homophone collision confirmed via anchored grep. Just refreshed `date-last-perfect: 2026-09-09`.

Next: 主宰.

### 2026-09-09, iteration 3978 — [[words/主宰|主宰]]
Found a missing legitimizing note: 宰's own page carries `stand_in: "主宰"`, but this word's own Notes never documented the reciprocal relationship. Added it. `characters:` confirmed correct (bare 主/宰, neither has a conflicting `words/*.md`), `kwin: true` confirmed via AND-rule, citations correctly ruby-formatted on both character pages (including the sibling compound 主宰万物), no homophone collision. Content otherwise already thorough (cosmic/philosophical vs mundane administrative sense, Vietnamese chủ tể's matching dual weight). Stamped `date-last-perfect: 2026-09-09`.

Next: 主導.

### 2026-09-09, iteration 3979 — [[words/主導|主導]]
Same missing-legitimizing-note pattern as the previous iteration: 導's own page carries `stand_in: "主導"`, not documented reciprocally here — added it. `characters:` confirmed correct (bare 主/導), `kwin: false` confirmed via AND-rule, citations correctly ruby-formatted on both character pages, no homophone collision. Content otherwise already thorough (主導 vs 主宰 register contrast, the yet-uncreated 指導/引導/領導 family noted). Stamped `date-last-perfect: 2026-09-09`.

Next: 主席.

### 2026-09-09, iteration 3980 — [[words/主席|主席]]
Substantially incomplete: `date-last-perfect` entirely absent, dangling empty `swadesh`/`aliases` fields, and no real `## Notes` — just a stray non-standard homophone line. `characters:` confirmed correct (bare 主/席, no conflicting words/*.md; 席's own `stand_in` is a different word, 坐席, so no legitimizing note applies here). `kwin: true` confirmed via AND-rule. Reformatted the homophone claim into the standard `>[!warning] Homophones` callout and verified it's real via anchored grep (both 主席 and [[朱錫]] share 注音 ㄐㄨㄙㄝㄎ). Wrote full Notes (国家主席 head-of-state usage, North Korean 주석 as a historical head-of-state title, Vietnamese Chủ tịch nước parallel). **Flagged for later**: 朱錫.md's own side of this homophone still uses a non-standard callout format and carries a stray gibberish line ("This very K word is necessary because 'seg' is so full") — awaiting its alphabetical turn. Stamped `date-last-perfect: 2026-09-09`.

Next: 主幹.

### 2026-09-09, iteration 3981 — [[words/主幹|主幹]]
Already fully correct from a prior pass: legitimizing note present (幹's `stand_in: 主幹` correctly documented), `characters:` confirmed correct, `kwin: true` confirmed via AND-rule, citations correctly ruby-formatted on both character pages, no homophone collision. Just refreshed `date-last-perfect: 2026-09-09`.

Next: 主従.

### 2026-09-09, iteration 3982 — [[words/主従|主従]]
Found: `date-last-perfect` entirely absent, `vietnamese` field entirely missing, mandarin/cantonese/korean unquoted, and caught my own recurring korean-hanja-instead-of-Hangul transcription slip on the first Edit attempt (corrected on retry). Filled vietnamese with chủ tớ — the real, everyday native+SV idiom for "master and servant" (quan hệ chủ tớ), preferred over the compositional-but-unattested chủ tùng. `characters:` confirmed correct (従's own `stand_in` is itself, not this compound — so no legitimizing note needed here despite the 主-compound cluster pattern). `kwin: true` confirmed via AND-rule. Citations correct on both character pages, no homophone collision. Stamped `date-last-perfect: 2026-09-09`.

Next: 主意.

### 2026-09-09, iteration 3983 — [[words/主意|主意]]
Found two real bugs: `kwin` field entirely missing from frontmatter (added `false`, via AND-rule: 主 true + 意 false = false), and a citation inconsistency on `主.md` — its 主意 entry used rt `ㄐㄨ·ㄧ` while the word's own stored `注音` and `意.md`'s own citation both correctly use `ㄐㄨ·ㄜ`; fixed `主.md`'s citation to match. `characters:` confirmed correct (both bare, no conflicting words/*.md). Content already excellent (the 主意/注意 homophone pair thoroughly cross-explained, cross-strait Mandarin tone split, Korean's identical collision). No other homophone collisions beyond the already-documented 注意. Stamped `date-last-perfect: 2026-09-09`.

Next: 主掌.

### 2026-09-09, iteration 3984 — [[words/主掌|主掌]]
Fixed duplicate `pos`/`品詞` field and quoted mandarin/cantonese/korean (self-caught a transcription slip mid-edit: the korean field was already correct Hangul 주장, not hanja as I first mistyped in old_string). `characters:` confirmed correct (bare 主/掌, no conflicting words/*.md). `kwin: true` confirmed via AND-rule. Citations correct on both character pages. Verified no Dan'a'yo-level homophone collision (注音 ㄐㄨㄐㄚㄫ unique) — the Korean-only 主張/主掌 collision already well-documented in prose is real but Korean-specific, not a Dan'a'yo pair (主張 doesn't even exist as a word file yet). Content otherwise already excellent (周禮 citation). Stamped `date-last-perfect: 2026-09-09`.

Next: 主教.
