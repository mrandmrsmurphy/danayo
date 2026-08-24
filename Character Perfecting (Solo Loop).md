# Character Perfecting (Solo Loop)

Running log for the character-perfecting backlog sweep (see [[AIOS/checklists/checklist_characters.md|Checklist: Character Pages]]). The prior logs (iterations 1–464, 465–981, 982–1543, 1544–2049, and 2050–2260) grew large and were archived to `Character Perfecting (Solo Loop).md.zip`, `Character Perfecting (Solo Loop) 2.md.zip`, `Character Perfecting (Solo Loop) 3.md.zip`, `Character Perfecting (Solo Loop) 4.md.zip`, and `Character Perfecting (Solo Loop) 5.md.zip` respectively; this file continues from there. Iteration numbering continues unbroken from the archived logs.

**Process**: one character per iteration. Find the next never-perfected character via `danayo_id` ascending (`grep -L "^date-last-perfect" characters/*.md`, sorted by each file's own `danayo_id` frontmatter value — not alphabetical, unlike the word sweep). Verify/fill all required frontmatter (`graphemic_classification`, `stand_in`, `mc_id`, `danayo_id`, `pos`, level fields), write or correct the four fixed `## Notes` bullets (graphemic → SKIP/Stroke → MC rank+phonology → levels), cross-check `## Words` against every real word citing this character as a constituent, add `## Chengyu`/`## Derived Characters` when real hits exist, then stamp `date-last-perfect`.

Next never-perfected character by `danayo_id`: 爰 (8535; 244 characters remaining).

### 2026-08-23, iteration 2261 — [[characters/爰|爰]]

`graphemic_classification: 會意` reconfirmed correct — en.Wiktionary gives an explicit ideogrammic-compound breakdown (爫 "hand" + 丨 + 又 "hand," two hands holding/pulling); zh.Wiktionary corroborates the reading and sense without detailing components. `radical: 爪` reconfirmed correct — genuine "Used" listing (item 3) on `Lookup/Radicals/Radical 087.md`. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `stand_in: 名専字` reconfirmed correct — zero hits for 爰 anywhere in `words/`, matching its listing (item 267) on `Lookup/名専字.md`. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-4-5.md` (item 10), `Lookup/Stroke/Stroke 09.md`, `Lookup/List of 会意.md`, and `Lookup/Korean/Korean Name ㅇ.md`'s `### 원` section.

**`mc_id` off-by-one bug found and fixed**: stored `1559` was actually 它's rank; correct rank for 爰 is `1560` (`CC 1000.md`: `1559. 它`, `1560. 爰`).

**`cantonese` completeness gap found and fixed**: stored `wun4` only; both en.Wiktionary and zh.Wiktionary independently attest a second genuine jyutping reading, `jyun4`; added, converting the field from scalar to list per the vault's multi-reading convention.

**`vietnamese` typo found and fixed**: stored `vèn` (grave accent) — hvdic.thivien.net's genuine Âm Nôm reading is actually `vén` (acute accent); corrected.

**`japanese`/`japanese_native` bugs found and fixed**: `japanese: [EN]` (kan-on) was missing a second genuine on'yomi, the go-on `ON`; both ja.Wiktionary and weblio.jp independently confirm it; added. `japanese_native: ここ` was a truncated fragment, not the real reading — both ja.Wiktionary and weblio.jp give the genuine kun'yomi as `ここに`; corrected.

**`joyo_level` filled**: was blank. Both ja.Wiktionary and weblio.jp confirm 爰 as 表外字 (outside the Jōyō/Jinmeiyō lists but genuinely read); added as item 536 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`pos` filled**: was blank. Filled as `連接詞`, matching the primary classical sense "thereupon; therefore" (a sentence-connecting particle), corroborated by both en.Wiktionary and zh.Wiktionary.

**`english` completeness gap found and fixed**: was `[lead on to]` only, missing the dual-source-attested primary conjunctive sense; added `thereupon`.

**`## Derived Characters` section added**: four real 形声 hits citing 爰 as phonetic component — [[characters/媛|媛]], [[characters/援|援]], [[characters/緩|緩]], [[characters/暖 (char)|暖 (char)]] — cross-checked via each page's own `graphemic_classification` field.

**Cross-reference typo found and fixed**: `Lookup/Radicals/Radical 087.md` glossed item 3 as "lean on to," inconsistent with both the character's own `english` field and its correct gloss ("lead on to") on `Lookup/SKIP/SKIP-2/SKIP-2-4-5.md`; corrected to "lead on to."

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 犀 (8537; 243 characters remaining).

### 2026-08-23, iteration 2262 — [[characters/犀|犀]]

`graphemic_classification: 尾` (dual-source confirmed 形声, semantic 牛 + phonetic 尾, OC \*sliːl) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 牛` reconfirmed correct — genuine listing (item 11, "+8 Strokes") on `Lookup/Radicals/Radical 093.md`. `cantonese: sai1` reconfirmed complete — both sources give only this one reading. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 370, corroborated directly by ja.Wiktionary's own status line. `stand_in: 犀牛` reconfirmed correct — sole genuine `characters:` citer is [[words/犀牛|犀牛]]; the second grep hit, [[words/牛|牛]], is a false-positive prose mention (犀牛 appearing only as an example compound in 牛's own etymology note), not a genuine citation. Already correctly cross-listed on `Lookup/SKIP/SKIP-3/SKIP-3-3-9.md` (item 6), `Lookup/Stroke/Stroke 12.md`, and `Lookup/Korean/Korean Name ㅅ.md`.

**`mc_id` off-by-one bug found and fixed**: stored `1750` was actually 希's rank; correct rank for 犀 is `1751` (`CC 1000.md`: `1750. 希`, `1751. 犀`).

**`japanese_native` bug found and fixed — sentinel used despite genuine kun'yomi**: stored `ø` ("confirmed no kun'yomi"), but both en.Wiktionary and ja.Wiktionary independently attest two genuine kun'yomi tied to the "sharp; hard" sense — `かた-い` and `するど-い`; both added, correcting the sentinel.

**`english` completeness gap found and fixed**: was `[rhinoceros, rhino]` only; both en.Wiktionary and zh.Wiktionary independently attest a second genuine sense, "sharp" (cf. 犀利, 心有靈犀), corroborated by the newly-added kun'yomi; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the primary nominal sense "rhinoceros" (the character's sole bound Chinese usage, in 犀牛).

**`aliases` filled**: was blank. One genuine dual-source variant, [[屖]], cross-listed as 異體字/alternative form by both en.Wiktionary and zh.Wiktionary, with no independent page in this vault; added. A second candidate, the obscure never-adopted second-round-simplification form 𰠨, was left out — consistent with this session's established practice of excluding abolished/unused simplification-scheme forms.

**`## Derived Characters` section added**: one real 形声 hit citing 犀 as phonetic component — [[characters/遅 (char)|遅 (char)]] (traditional 遲; simplified 迟 replaces 犀 with 尺).

**Section-ordering bug found and fixed**: the `## Words` section appeared BEFORE the (malformed, wrong-heading-level) `# Notes` section — reversed from this vault's established Notes→Words→Derived-Characters convention (cf. `characters/丁 (char).md`); reordered, with the pre-existing `## Words` section (citing [[words/犀牛|犀牛]]) left otherwise untouched.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet, wrong section order relative to Words) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 狽 (8539; 242 characters remaining).

### 2026-08-23, iteration 2263 — [[characters/狽|狽]]

`graphemic_classification: 貝` (dual-source confirmed 形声, semantic 犬 + phonetic 貝, OC \*paːds) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 犬` reconfirmed correct — genuine listing (item 15) on `Lookup/Radicals/Radical 094.md`. `japanese: [HAI, BAI]` reconfirmed complete — both sources give only go-on/kan-on はい and the customary ばい. `japanese_native: ø` reconfirmed correct — neither source attests any kun'yomi. `vietnamese: [bái]` reconfirmed complete via hvdic.thivien.net (identical Âm Hán Việt and Âm Nôm). `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md` item 210. `stand_in: 狼狽` reconfirmed correct — sole citer, the word's own independent page. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-3-7.md` (item 59), `Lookup/Stroke/Stroke 10.md`, and `Lookup/Korean/Korean Name ㅍ.md`. `mc_id: 6584` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`hsk_level` bug found and fixed — genuine level hiding under simplified sibling glyph**: stored `無`, matching a listing on `Lookup/HSK/HSK No.md`, but `Old HSK 6.md` has a genuine plain-numbered entry under the simplified sibling glyph 狈 (`432. [狈](../../characters/狽.md)`) — the colon-count entries on `Old HSK 4.md` (both 狈 and 狽) are not genuine and were correctly ignored. Corrected `hsk_level` to `6`, and removed the now-stale entry from `Lookup/HSK/HSK No.md`.

**`english` mistranslation found and fixed**: stored `[werewolf]` — genuinely wrong; both en.Wiktionary and zh.Wiktionary independently identify 狽 as a legendary wolf-like beast with short forelegs and long hind legs (the pair-creature of the idiom 狼狽, not a "werewolf" in any sense). Corrected to `[mythical wolf-like beast, distressed]` (the second sense being the idiom's genuine figurative extension). Propagated the same gloss fix to the two cross-reference pages that had copied the error verbatim — `Lookup/Radicals/Radical 094.md` (item 15) and `Lookup/SKIP/SKIP-1/SKIP-1-3-7.md` (item 59) — both now read "wolf-like beast." Note for the word-perfecting sweep: [[words/狼狽|狼狽]]'s own `english` field (`[werewolf, flustering, confusion]`) carries the same mistranslation and is out of scope for this character-perfecting pass.

**`pos` filled**: was blank. Filled as `名詞`, matching the primary nominal sense (naming the mythical creature).

**`aliases` completeness gap found and fixed**: had `狈` (simplified form) only; zh.Wiktionary's own 異體字 listing gives a second genuine variant, `䟺`, with no independent page in this vault; added.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format; `## Chengyu` (citing [[chengyu/周章狼狽|周章狼狽]], ruby verified against the chengyu's own `注音` field) reconfirmed correct, no changes. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 玲 (8541; 241 characters remaining).

### 2026-08-23, iteration 2264 — [[characters/玲|玲]]

`graphemic_classification: 令` (dual-source confirmed 形声, semantic 玉 + phonetic 令, OC \*reŋ) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 玉` reconfirmed correct — genuine listing (item 5) on `Lookup/Radicals/Radical 096.md`. `cantonese: ling4` reconfirmed complete — both sources give only this one reading. `japanese_native: ø` reconfirmed correct — ja.Wiktionary explicitly states 玲 has no standard kun'yomi, only 名乗り (name-only readings あきら/たま/れ, a distinct category this vault's `japanese_native` field doesn't cover). `korean_native: ""` reconfirmed correct — a purely Sino-Korean name character with no native gloss, consistent with 52 other pages using the same blank-string convention. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 373. `stand_in: 名専字` reconfirmed correct — zero hits for 玲 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-4-5.md` (item 26), and `Lookup/Korean/Korean Name ㄹ.md`. `mc_id: 6718` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`hsk_level` bug found and fixed**: stored `4`, traced only to a colon-count entry on `Old HSK 4.md` (`[[玲]]: 2`, not genuine) — no plain-numbered entry exists in any `Old HSK N.md` file, and `Lookup/HSK/HSK No.md` itself already correctly lists 玲 among characters confirmed to have no genuine HSK level. Corrected to `hsk_level: 無`.

**`japanese` typo found and fixed**: stored `[REI, ROU]` — `ROU` was a corrupted go-on reading, missing the ⟨y⟩; both ja.Wiktionary and en.Wiktionary give the genuine go-on as リョウ, romanized `RYOU` per this vault's established convention (cf. `characters/涼.md`, `characters/両 (char).md`). Corrected to `[REI, RYOU]`.

**`vietnamese` bug found and fixed — unattested reading**: stored `[lanh, leng, linh, liếng, lẻng]`; hvdic.thivien.net's genuine readings (1 Âm Hán Việt + 3 Âm Nôm) are exactly `linh, lanh, leng, liếng` — `lẻng` appears nowhere in the source and was removed as an unattested/fabricated reading (likely confusion with the unrelated onomatopoeia "leng keng").

**`english` accuracy gap found and fixed**: stored `[jade]` — this names the semantic radical, not the character's own meaning; both en.Wiktionary and zh.Wiktionary agree 玲 denotes the tinkling sound of jade, extended to "clever; exquisite." Corrected to `[tinkling of jade, clever]`. Propagated the same gloss correction to `Lookup/Radicals/Radical 096.md` (item 5) and `Lookup/SKIP/SKIP-1/SKIP-1-4-5.md` (item 26), both of which had copied the old "jade" gloss.

**`pos` filled**: was blank. Filled as `性詞`, matching the dominant adjectival modern sense ("clever, exquisite," as used in given names).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 玳 (8542; 240 characters remaining).

### 2026-08-23, iteration 2265 — [[characters/玳|玳]]

`graphemic_classification: 代` (dual-source confirmed 形声, semantic 玉 + phonetic 代, OC \*l'ɯːɡs) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 玉` reconfirmed correct — genuine listing (item 6) on `Lookup/Radicals/Radical 096.md`. `vietnamese: [đại, đồi]` reconfirmed complete and exact against en.Wiktionary (Hán Việt đại; Chữ Nôm đồi, đại). `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `stand_in: 玳瑁` reconfirmed correct — sole citer, the word's own independent page. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-4-5.md` (item 27) and `Lookup/Korean/Korean Name ㄷ.md`. `mc_id: 4865` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`joyo_level` filled**: was blank. Both ja.Wiktionary and en.Wiktionary confirm 玳 as 表外字; added as item 537 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`japanese` completeness gap found and fixed**: was `[TAI]` (kan-on) only; both ja.Wiktionary and en.Wiktionary independently attest a genuine go-on, `DAI`; added. A further candidate pair from en.Wiktionary alone (`どく`/`とく`, DOKU/TOKU) was left out — not corroborated by ja.Wiktionary, the authoritative source for Japanese readings, per this session's established dual-source practice.

**`japanese_native` bug found and fixed — compound reading mistaken for kun'yomi**: stored `たいまい`, but both en.Wiktionary and zh.Wiktionary are explicit that 玳 "is used only in 玳瑁" and has no standalone kun'yomi — たいまい is the reading of the two-character compound 玳瑁, not of 玳 alone (ja.Wiktionary independently lists no kun'yomi at all for this character). Corrected to the `ø` sentinel.

**`pos` filled**: was blank. Filled as `名詞`, matching the sole nominal sense (short form of 玳瑁, "hawksbill sea turtle").

**`aliases` filled**: was blank. One genuine dual-source variant, [[瑇]], cross-listed as 異體字/alternative form by both en.Wiktionary and zh.Wiktionary, with no independent page in this vault; added.

**`## Words` section added**: citing [[words/玳瑁|玳瑁]], ruby verified against the word's own `注音` field.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet, no `## Words` section) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 琥 (8544; 239 characters remaining).

### 2026-08-23, iteration 2266 — [[characters/琥|琥]]

`graphemic_classification: 虎` (dual-source confirmed 形声, semantic 玉 + phonetic 虎, OC \*qʰlaːʔ) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 玉` reconfirmed correct — genuine listing (item 20) on `Lookup/Radicals/Radical 096.md`. `vietnamese: [hổ]` reconfirmed complete and exact against hvdic.thivien.net (identical Âm Hán Việt and Âm Nôm). `japanese_native: ø` reconfirmed correct — ja.Wiktionary lists no kun'yomi. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 377. `english: [amber]` reconfirmed correct and deliberately narrow — zh.Wiktionary also attests historical "jade tally/ritual object" senses, but [[words/琥珀|琥珀]]'s own Notes already establish those senses aren't attested anywhere in this vault's data, so they were correctly left out. `stand_in: 琥珀` and the `cranberry` tag reconfirmed correct — sole citer [[words/琥珀|琥珀]] documents genuine transitivity (neither 琥 nor 珀 has independent life elsewhere, matching `korean_native` glosses). `aliases` (blank) reconfirmed correct — zh.Wiktionary attests no genuine variant forms distinct from 琥 itself. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-4-8.md` (item 26) and `Lookup/Korean/Korean Name ㅎ.md`. `mc_id: 5480` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`japanese` completeness gap found and fixed**: was `[KO]` (kan-on) only; both ja.Wiktionary and en.Wiktionary independently attest a genuine go-on, `KU`; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the sole nominal sense (amber).

**`## Words` section added**: citing [[words/琥珀|琥珀]], ruby verified against the word's own `注音` field.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, a stray unlinked-format Words bullet folded into Notes instead of its own section, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format plus a proper `## Words` section. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 琳 (8545; 238 characters remaining).

### 2026-08-23, iteration 2267 — [[characters/琳|琳]]

`graphemic_classification: 林` (dual-source confirmed 形声, semantic 玉 + phonetic 林) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 玉` reconfirmed correct — genuine listing (item 21) on `Lookup/Radicals/Radical 096.md`. `japanese: [RIN]` reconfirmed complete — both sources give an identical go-on/kan-on りん. `vietnamese: [lam, lâm]` reconfirmed complete against en.Wiktionary's Hán Nôm readings. `korean: 림` reconfirmed correct as the North Korean/문화어 form (not the South Korean 두음법칙-shifted 임 that en.Wiktionary also notes). `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 254. `stand_in: 名専字` reconfirmed correct — zero hits for 琳 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-4-8.md` (item 27) and `Lookup/Korean/Korean Name ㄹ.md`. `mc_id: 4036` reconfirmed as trusted long-tail (just above the 4000-rank ceiling of `CC 3000.md`, not cross-checked per policy).

**`hsk_level` gap filled — genuinely absent, not just unfilled**: was the empty-string sentinel; thoroughly checked all four `Old HSK N.md` files and `Lookup/HSK/HSK No.md` and found zero hits for 琳 anywhere (unlike the usual bug pattern of a stale/wrong value, this character had simply never been indexed). Filled `hsk_level: 無` and added 琳 to `Lookup/HSK/HSK No.md`'s list.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses "jade; gem."

**`aliases` filled**: was blank. One genuine dual-source variant, [[玪]], cross-listed as an alternative form by both en.Wiktionary and zh.Wiktionary, with no independent page in this vault; added.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 琺 (8546; 237 characters remaining).

### 2026-08-23, iteration 2268 — [[characters/琺|琺]]

`graphemic_classification: 法` (dual-source confirmed 形声, semantic 玉 + phonetic 法) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 玉` reconfirmed correct — genuine listing (item 25) on `Lookup/Radicals/Radical 096.md`. `japanese: [HOU]` reconfirmed complete — both en.Wiktionary and ja.Wiktionary give only this one on'yomi. `japanese_native: ø` reconfirmed correct — ja.Wiktionary lists no kun'yomi. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `mc_id: 0` reconfirmed correct — genuinely absent from all four `CC N000.md` files. `pos: 名詞` and `aliases: [珐]` reconfirmed correct (simplified form, matching both sources). `stand_in: 琺瑯` reconfirmed correct — sole citer, the word's own independent page. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-4-8.md` (item 28) and `Lookup/Korean/Korean Name ㅂ.md`.

**`joyo_level` cross-reference gap found and fixed**: the field itself already correctly said `表外字` (confirmed genuine via ja.Wiktionary), but the character was missing from `Lookup/Japanese/Hyōgai.md` itself; added as item 538.

**`cantonese` completeness gap found and fixed**: stored `faat3` only; zh.Wiktionary independently attests a second genuine jyutping reading, `fat3` (also corroborated by en.Wiktionary), converting the field from scalar to list per the vault's multi-reading convention.

**`vietnamese` gap found and fixed — field left entirely empty**: both en.Wiktionary and hvdic.thivien.net attest a genuine Âm Hán Việt reading, `pháp`; added (the field previously had no value at all).

**`## Words` section added**: the pre-existing bare bullet citing [[words/琺瑯|琺瑯]] (ruby verified against the word's own `注音` field) was folded directly into the malformed `# Notes` block instead of its own section; separated out properly.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet, `## Words` content misplaced inside Notes) into the standard `## Notes` four-bullet format plus a proper `## Words` section. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 瑁 (8547; 236 characters remaining).

### 2026-08-23, iteration 2269 — [[characters/瑁|瑁]]

`graphemic_classification: 冒` (dual-source confirmed 形声, semantic 玉 + phonetic 冒) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 玉` reconfirmed correct — genuine listing (item 27) on `Lookup/Radicals/Radical 096.md`. `cantonese: mou6` reconfirmed correct (the etymology-1 "ceremonial jade" reading; the unrelated etymology-2 mui6 belongs to a different, non-attested sense). `japanese_native: ø` reconfirmed correct — ja.Wiktionary lists no kun'yomi. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `pos: 名詞` reconfirmed correct. `aliases` (blank) reconfirmed correct — zh.Wiktionary's variant-form list (㺺, 𤣽, 𤲰, 蝐, 珼/𫞥, etc.) is entirely obscure/unencodable forms, consistent with this session's practice of excluding such forms. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-4-9.md` (item 22) and `Lookup/Korean/Korean Name ㅁ.md`.

**`mc_id` off-by-one bug found and fixed**: stored `3732` was actually 凋's rank; correct rank for 瑁 is `3733` (`CC 3000.md`: `3732. 凋`, `3733. 瑁`).

**`stand_in` bug found and fixed**: stored `名専字` despite a genuine citer — [[words/玳瑁|玳瑁]]'s own `characters:` field lists both 玳 and 瑁. Corrected to `玳瑁`. Note: unlike the parallel [[characters/琥|琥]]/珀 pair (tagged `#cranberry`), 瑁 genuinely has an independent, non-bound sense (etymology 1, "ceremonial jade of the Son of Heaven") distinct from the compound's meaning, so the cranberry tag does not apply here — transitivity fails (瑁's independent meaning ≠ 玳瑁's meaning).

**`japanese` completeness gap found and fixed**: was `[BOU, MOU, MAI]`, missing a fourth genuine on'yomi; both ja.Wiktionary and en.Wiktionary independently attest go-on/kan-on `バイ` (BAI); added.

**`vietnamese` completeness gap found and fixed**: was `[mao, mùi, mạo, mồi]`; hvdic.thivien.net's genuine readings (2 Âm Hán Việt + 3 Âm Nôm) additionally include `mội`; added. A further candidate from en.Wiktionary alone, `mại`, was left out — not corroborated by hvdic, this vault's Vietnamese authority.

**`joyo_level` cross-reference gap found and fixed**: the field itself already correctly said `表外字` (confirmed genuine via ja.Wiktionary), but the character was missing from `Lookup/Japanese/Hyōgai.md` itself; added as item 539.

**`## Words` section added**: citing [[words/玳瑁|玳瑁]], ruby verified against the word's own `注音` field.

Rebuilt the malformed `## Notes` (missing SKIP/Stroke-format bullet consistency, unlinked bare-glyph references, no mc_id-rank bullet, no four-level-links bullet, two floating unlinked CC wikilinks, no `## Words` section) into the standard four-bullet format plus `## Words`. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 瑛 (8548; 235 characters remaining).

### 2026-08-23, iteration 2270 — [[characters/瑛|瑛]]

`graphemic_classification: 英` (dual-source confirmed 形声, semantic 玉 + phonetic 英) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 玉` reconfirmed correct — genuine listing (item 26) on `Lookup/Radicals/Radical 096.md`. `japanese: [EI, YOU]` reconfirmed complete — both en.Wiktionary and ja.Wiktionary give only kan-on えい and go-on よう. `japanese_native: ø` reconfirmed correct — both sources' kun'yomi are entirely 名乗り (name-only readings), not standard kun'yomi. `vietnamese: [anh]` reconfirmed complete — en.Wiktionary's sole reading. `korean: 영` reconfirmed correct (no 두음법칙 concern — the syllable doesn't begin with ㄹ/ㄴ). `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 238. `stand_in: 名専字` reconfirmed correct — zero hits for 瑛 anywhere in `words/`. `aliases: [瑩]` reconfirmed correct — 瑩 has no independent page and is explicitly redirected to 瑛 on both `Lookup/Korean/Korean Name ㅎ.md` ("瑩-->瑛") and `Korean Name ㅇ.md`. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-4-8.md` (item 29). `mc_id: 7338` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`english` completeness gap found and fixed**: was `[luster]` only; zh.Wiktionary independently attests a second genuine gloss, "crystal," corroborating en.Wiktionary's own "luster of jade; beautiful jade" senses; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 甬 (8550; 234 characters remaining).

### 2026-08-23, iteration 2271 — [[characters/甬|甬]]

`graphemic_classification: 用` reconfirmed correct, but with a genuine three-way source conflict investigated and documented: zh.Wiktionary treats 甬 as 形声 with phonetic 用 (matching the stored value); en.Wiktionary instead claims 甬 is 象形, a bronze-bell pictograph whose lower part later became 用; ja.Wiktionary offers yet a third account (a purely decorative graphic variant of 用, not a standard etymological category at all). Kept `用` since only one source attests the pictograph theory. `radical: 用` reconfirmed correct — genuine listing (item 3) on `Lookup/Radicals/Radical 101.md`. `mc_id: 3150` reconfirmed exact match (`CC 3000.md`: `3149. 淹`, `3150. 甬`, `3151. 湎`). `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `stand_in: 名専字` reconfirmed correct — zero hits for 甬 anywhere in `words/`. `aliases` (blank) reconfirmed correct — zh.Wiktionary's "variant characters" 埇/筩 are contradicted by en.Wiktionary's explicit "no variant forms," and neither has an independent page in this vault to test against; left unadded absent stronger corroboration. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-2-5.md` (item 9) and `Lookup/Korean/Korean Name ㅇ.md`.

**`japanese` completeness gap found and fixed**: was `[YOU]` (kan-on) only; ja.Wiktionary directly attests a genuine go-on, `ユウ`, romanized `YUU` per this vault's convention (cf. `characters/又 (char).md`, `characters/幽 (char).md`); added. En.Wiktionary's claimed kun'yomi (つね/つかう/おどる) were NOT added — ja.Wiktionary, the authoritative source, explicitly lists no kun'yomi at all, so `japanese_native: ø` stands reconfirmed.

**`joyo_level` filled**: was blank. ja.Wiktionary directly confirms 甬 as 表外字; added as item 540 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`vietnamese` bug found and fixed**: stored `[dũng, giõng]`; hvdic.thivien.net's genuine readings are `dũng, dõng` — `giõng` appears nowhere in the source (likely a corruption of the genuine-but-missing `dõng`, which was also absent). Corrected to `[dũng, dõng]`.

**`english` completeness gap found and fixed**: was `[Yong River]` only; both en.Wiktionary and zh.Wiktionary independently attest a second genuine sense, "path" (a walled/screened walkway); added.

**`pos` filled**: was blank. Filled as `固有名詞`, matching this vault's established convention for river-name characters (cf. `characters/洛.md`, `characters/淮.md`).

**`## Derived Characters` section added**: seven real 形声 hits citing 甬 as phonetic component — [[characters/通 (char)|通]], [[characters/痛|痛]], [[characters/誦 (char)|誦]], [[characters/湧 (char)|湧]], [[characters/桶 (char)|桶]], [[characters/踊|踊]], [[characters/勇|勇]].

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 町 (8551; 233 characters remaining).

### 2026-08-23, iteration 2272 — [[characters/町|町]]

`graphemic_classification: 丁` (dual-source confirmed 形声, semantic 田 + phonetic 丁) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 田` reconfirmed correct — genuine listing (item 5) on `Lookup/Radicals/Radical 102.md`. `mc_id: 3710` reconfirmed exact match (`CC 3000.md`: `3710. 町`). `japanese: [CHOU, TEI]` reconfirmed complete — both en.Wiktionary and ja.Wiktionary give only go-on ちょう/kan-on てい. `japanese_native: まち` reconfirmed correct; a second candidate from en.Wiktionary alone (あぜみち) was left out — not corroborated by ja.Wiktionary, the authoritative source. `joyo_level: 1` reconfirmed correct — ja.Wiktionary directly confirms 町 as a Grade 1 kyōiku kanji, genuine at `Lookup/Japanese/Jōyō - Kyōiku.md` item 64. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-5-2.md` (item 12) and `Lookup/Korean/Korean Name ㅈ.md`.

**`stand_in` bug found and fixed — real citer buried among false positives**: stored `名専字`, but a `characters:`-field grep turned up four apparent hits; three ([[words/安土|安土]], [[words/中庭|中庭]], [[words/桃山|桃山]]) checked out as false-positive prose mentions (their own `characters:` fields cite unrelated constituents), but the fourth, [[words/室町|室町]], genuinely lists 町 in its `characters:` field. Corrected `stand_in` to `室町`.

**`cantonese` completeness gap found and fixed**: stored `ting2` (from the tǐng reading) only; both en.Wiktionary and zh.Wiktionary independently attest a second genuine jyutping reading, `ding1` (from the dīng reading), converting the field from scalar to list.

**`vietnamese` gap found and fixed — field left entirely empty**: hvdic.thivien.net attests two genuine Âm Hán Việt readings, `đinh` and `đỉnh`; added (en.Wiktionary's own candidate second reading, `thĩnh`, disagreed with hvdic and was not used, per this vault's practice of treating hvdic as the Vietnamese authority).

**`aliases` filled**: was blank. Two genuine variants added: [[圢]] (dual-source confirmed by en.Wiktionary and zh.Wiktionary, no independent page) and [[䵺]] (already independently documented as a redirect to 町 on this vault's own `Lookup/Radicals/Radical 206.md`, but never propagated to the character's own `aliases` field until now).

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses ("ridge between fields," "boundary").

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format; `## Words` (citing [[words/室町|室町]], ruby verified against the word's own `注音` field) reconfirmed correct, no changes. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 疱 (8552; 232 characters remaining).

### 2026-08-23, iteration 2273 — [[characters/疱|疱]]

`graphemic_classification: 包` (dual-source confirmed 形声, semantic 疒 + phonetic 包) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 疒` reconfirmed correct — genuine listing (item 2) on `Lookup/Radicals/Radical 104.md`. `cantonese: paau3` reconfirmed complete — both sources give only this one reading. `japanese_native: もがさ` reconfirmed correct; a second candidate from en.Wiktionary alone (にきび) was left out — ja.Wiktionary, the authoritative source, doesn't list it (and the word file [[words/面疱|面疱]]'s own Notes already correctly attribute にきび to the *word*, not the character). `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md` item 182. `stand_in: 面疱` reconfirmed correct — sole citer, the word's own independent page. `aliases: [皰]` reconfirmed correct — the traditional form 疱 simplifies from, with no independent page in this vault. Already correctly cross-listed on `Lookup/SKIP/SKIP-3/SKIP-3-5-5.md` (item 1) and `Lookup/Korean/Korean Name ㅍ.md`. `mc_id: 9417` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`japanese` completeness gap found and fixed**: was `[HOU]` (kan-on) only; both en.Wiktionary and ja.Wiktionary independently attest a genuine go-on, `HYOU`; added.

**`vietnamese` completeness gap found and fixed**: was `[bào, bỏng]`; hvdic.thivien.net's genuine readings (2 Âm Hán Việt + 2 Âm Nôm) additionally include a second Âm Hán Việt, `pháo`; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the sole nominal sense (acne).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format; `## Words` (citing [[words/面疱|面疱]], ruby verified against the word's own `注音` field) reconfirmed correct, no changes. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 疽 (8553; 231 characters remaining).

### 2026-08-23, iteration 2274 — [[characters/疽|疽]]

`graphemic_classification: 且` (dual-source confirmed 形声, semantic 疒 + phonetic 且) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 疒` reconfirmed correct — genuine listing (item 4) on `Lookup/Radicals/Radical 104.md`. `cantonese: zeoi1` reconfirmed correct and complete — en.Wiktionary's claimed second reading `ceoi1` isn't corroborated by zh.Wiktionary, which gives only `zeoi1`; left unadded. `japanese: [SHO, SO]` reconfirmed complete — both sources give only kan-on しょ/go-on そ. `vietnamese: [thư]` reconfirmed complete and exact against hvdic.thivien.net. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md` item 268. `stand_in: 用疽` reconfirmed correct — sole citer, the word's own independent page. `aliases` (blank) reconfirmed correct — neither source lists any variant forms. Already correctly cross-listed on `Lookup/Korean/Korean Name ㅈ.md`.

**`mc_id` off-by-one bug found and fixed**: stored `2810` was actually 抽's rank; correct rank for 疽 is `2811` (`CC 2000.md`: `2810. 抽`, `2811. 疽`).

**注音 three-way inconsistency found and fixed — genuine bug isolated**: the character's own `注音` field (`ㄐㄜ`) matched this vault's own carefully-dated `Lookup/CC/finals/韻 魚.md` analysis page (2026-07-10, which explicitly places 疽 as a ㄐ-initial singleton on the **ㄜ** sub-final, distinct from the ㄙ-initial cluster discussed in that page's phonology notes), but two derivative cross-references had drifted to the stale/wrong `ㄐㄛ`: `Lookup/SKIP/SKIP-3/SKIP-3-5-5.md` (item 3) and [[words/用疽|用疽]]'s own `注音` field (`⼄ㄫㄐㄛ`, predating the finals-page analysis by several months). Corrected both to `ㄐㄜ`.

**`japanese_native` completeness gap found and fixed**: was `かさ` only; ja.Wiktionary independently attests a second genuine kun'yomi, `はれもの`; added, converting the field to a list.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses (ulcer, abscess).

Rebuilt the malformed `## Notes` (bare unlinked "requires" line instead of a proper `## Words` section, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet, two floating unlinked CC wikilinks) into the standard `## Notes` four-bullet format plus a proper `## Words` section. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 瘡 (8554; 230 characters remaining).

### 2026-08-23, iteration 2275 — [[characters/瘡|瘡]]

`graphemic_classification: 倉` (dual-source confirmed 形声, semantic 疒 + phonetic 倉, OC \*sʰraŋ, sharing its word origin with 創) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 疒` reconfirmed correct — genuine listing (item 18) on `Lookup/Radicals/Radical 104.md`. `japanese: [SOU, SHOU]` reconfirmed complete — both sources give only go-on しょう/kan-on そう. `japanese_native: かさ` reconfirmed correct; a second candidate from en.Wiktionary alone (くさ) was left out — not corroborated by ja.Wiktionary, the authoritative source. `vietnamese: [sang]` reconfirmed complete and exact against hvdic.thivien.net. `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md` item 226. `aliases: [疮]` reconfirmed correct and complete — zh.Wiktionary's second listed variant, 創, already has its own robust independent page in this vault and fails the "no independent use" alias test, so correctly excluded. `stand_in: 瘡口` reconfirmed correct — of three apparent citers, only [[words/瘡口|瘡口]]'s own `characters:` field genuinely lists 瘡; [[words/窓口|窓口]] and [[words/潰瘍|潰瘍]] were false-positive hits (unrelated `characters:` fields). Already correctly cross-listed on `Lookup/SKIP/SKIP-3/SKIP-3-5-10.md` (item 1) and `Lookup/Korean/Korean Name ㅊ.md`.

**`mc_id` off-by-one bug found and fixed**: stored `2966` was actually 膀's rank; correct rank for 瘡 is `2967` (`CC 2000.md`: `2966. 膀`, `2967. 瘡`).

**`hsk_level` bug found and fixed**: stored `4`, traced only to colon-count entries on `Old HSK 4.md` (both `[疮]: 1` and `[[瘡]]: 1`, neither genuine) — thoroughly checked all four `Old HSK N.md` files and found no genuine plain-numbered entry anywhere, and 瘡 was also entirely absent from `Lookup/HSK/HSK No.md`. Corrected to `hsk_level: 無` and added 瘡 to `Lookup/HSK/HSK No.md`'s list.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses (wound, sore).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet, `## Words` placed before Notes instead of after) into the standard `## Notes` four-bullet format, reordered before the pre-existing `## Words` section (citing [[words/瘡口|瘡口]], ruby verified against the word's own `注音` field). Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 皓 (8556; 229 characters remaining).

### 2026-08-23, iteration 2276 — [[characters/皓|皓]]

`graphemic_classification: 告` (dual-source confirmed 形声, semantic 白 + phonetic 告) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 白` reconfirmed correct — genuine listing (item 8) on `Lookup/Radicals/Radical 106.md`. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 385. `stand_in: 名専字` reconfirmed correct — the sole grep hit, [[words/好|好]], is a false-positive prose mention (皓 listed only among a homophone-survey of ㄏㄚㄨ-reading characters, its own Notes explicitly confirming none has a self-pointing `stand_in`), not a genuine citation. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-5-7.md` (item 3).

**`mc_id` off-by-one bug found and fixed**: stored `2513` was actually 諧's rank; correct rank for 皓 is `2514` (`CC 2000.md`: `2513. 諧`, `2514. 皓`).

**`cantonese` completeness gap found and fixed**: stored `hou6` only; both en.Wiktionary and zh.Wiktionary independently attest a second genuine (rarer) jyutping reading, `gou2`; added.

**`japanese` completeness gap found and fixed**: was `[KOU]` (kan-on) only; both ja.Wiktionary and en.Wiktionary independently attest a genuine go-on, `GOU`; added.

**`japanese_native` bug found and fixed**: stored `しろ`, a truncated fragment missing both its okurigana and a second reading — both ja.Wiktionary and en.Wiktionary agree on two genuine kun'yomi, `しろい` and `ひかる`; corrected to both, full forms.

**`vietnamese` completeness gap found and fixed**: was `[hạo]` only; hvdic.thivien.net's genuine readings additionally include two further Âm Hán Việt, `cáo` and `cảo`; added.

**`aliases` filled**: was blank. Three genuine dual-source variants — [[晧]], [[暠]], [[皜]] (both en.Wiktionary and zh.Wiktionary agree on all three) — none with independent pages in this vault; added. A fourth single-sourced candidate from en.Wiktionary alone, 㬶, was left out. Propagated the fix to `Lookup/Korean/Korean Name ㅎ.md`, where 晧 had been sitting as an un-redirected bare entry; converted to the established `晧-->皓` redirect notation (cf. `甬`/`瑩`'s redirect on the same page style).

**`pos` filled**: was blank. Filled as `性詞`, matching the adjectival senses ("luminous, clear, bright white").

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 睾 (8557; 228 characters remaining).

### 2026-08-23, iteration 2277 — [[characters/睾|睾]]

`graphemic_classification: 幸` reconfirmed correct, with a genuine source conflict investigated and documented: zh.Wiktionary corroborates 幸 (a character series derived from it, matching the stored value), while en.Wiktionary instead names 皋 as phonetic and treats 睾 as an alternative form of 皋 entirely, not even attesting the "testicle" sense (which comes solely from zh.Wiktionary). Kept `幸` since it's the source that actually accounts for this page's bound modern meaning. `radical: 目` reconfirmed correct — genuine listing (item 20) on `Lookup/Radicals/Radical 109.md`. `cantonese: gou1` and `vietnamese: [cao]` reconfirmed complete against en.Wiktionary and hvdic.thivien.net respectively. `japanese: [KOU]` reconfirmed complete — both on'yomi (go-on and kan-on) share the identical reading こう. `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md` item 119. `stand_in: 睾丸` reconfirmed correct — of two apparent citers, only [[words/睾丸|睾丸]] genuinely cites 睾 in its `characters:` field; [[words/高|高]] was a false-positive prose mention (its own Notes explicitly confirm 睾 has no self-pointing `stand_in`). Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-6-8.md` (item 1) and `Lookup/Korean/Korean Name ㄱ.md`. `mc_id: 7262` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`japanese_native` bug found and fixed — sentinel used despite genuine kun'yomi**: stored `ø` ("confirmed no kun'yomi"), but both en.Wiktionary and ja.Wiktionary independently attest two genuine kun'yomi, `さわ` and `きんたま`; both added. Two further single-sourced candidates from ja.Wiktionary alone (さつき, おお) were left out — not corroborated by en.Wiktionary.

**`aliases` filled**: was blank. Two genuine dual-source variants — [[睪]] (the traditional form, still used in modern Taiwan per en.Wiktionary) and [[皋]] (explicitly listed as 異體字 by zh.Wiktionary) — neither with an independent page in this vault; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the sole bound sense (testicle).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, a bare unlinked-format Words bullet folded into Notes instead of its own section, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format plus a proper `## Words` section. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 瞼 (8558; 227 characters remaining).

### 2026-08-23, iteration 2278 — [[characters/瞼|瞼]]

`graphemic_classification: 㑒` investigated and reconfirmed correct — both en.Wiktionary and zh.Wiktionary name the textbook phonetic component as 僉, but this vault's own [[characters/㑒|㑒]] page lists 僉 in its own `aliases` field (pointing to 㑒 as the parent form), so citing the parent-form page 㑒 here is the correct application of this vault's established alias-citation convention, not a bug. `radical: 目` reconfirmed correct — genuine listing (item 28) on `Lookup/Radicals/Radical 109.md`. `japanese: [KEN]` reconfirmed complete — both sources give an identical single on'yomi. `japanese_native: まぶた` reconfirmed correct; a second candidate from en.Wiktionary alone (まなぶた) was left out — not corroborated by ja.Wiktionary, the authoritative source. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md` item 103. `stand_in: 眼瞼` and `aliases: [睑]` reconfirmed correct. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-5-13.md` (item 2) and `Lookup/Korean/Korean Name ㄱ.md`. `mc_id: 10070` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`cantonese` completeness gap found and fixed**: stored `gim2` only; both en.Wiktionary and zh.Wiktionary independently attest a second genuine jyutping reading, `lim4`; added.

**`vietnamese` bug found and fixed — unattested readings mixed with a genuine gap**: stored `[him, kiểm, kèm, kẻm, lim]`; hvdic.thivien.net's genuine readings are exactly `kiểm, kèm, lim` — `him` appears in neither source (clear fabrication/typo) and `kẻm` is attested only by en.Wiktionary, not hvdic (this vault's Vietnamese authority); both removed, leaving the three hvdic-confirmed readings.

**`pos` filled**: was blank. Filled as `名詞`, matching the sole nominal sense (eyelid).

**Missing reverse cross-reference found and fixed**: [[characters/㑒|㑒]]'s own `### Descendants` list (which already tracked [[characters/検|検]] and [[characters/鹸 (char)|鹸]] as phonetic descendants) was missing 瞼 itself; added.

Rebuilt the malformed `## Notes` (two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard four-bullet format; `## Words` (citing [[words/眼瞼|眼瞼]], ruby verified against the word's own `注音` field) reconfirmed correct, no changes. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 砦 (8559; 226 characters remaining).

### 2026-08-23, iteration 2279 — [[characters/砦|砦]]

`graphemic_classification: 此` (dual-source confirmed 形声, semantic 石 + phonetic 此, OC \*zraːds) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 石` reconfirmed correct — genuine listing (item 10) on `Lookup/Radicals/Radical 112.md`. `japanese_native: とりで` reconfirmed complete. `vietnamese: [trại]` reconfirmed complete and exact against hvdic.thivien.net. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 387. `stand_in: 鹿砦` reconfirmed correct — sole citer, the word's own independent page. `aliases` (blank) reconfirmed correct — en.Wiktionary's candidates 塁 and 寨 both already have independent pages in this vault (塁.md, 寨.md), failing the alias test regardless of zh.Wiktionary's narrower single-variant claim (寨 only). Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-6-5.md` (item 3) and `Lookup/Korean/Korean Name ㅊ.md`. `mc_id: 9194` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`japanese` completeness gap found and fixed**: was `[SAI]` (kan-on) only; both ja.Wiktionary and en.Wiktionary independently attest a genuine go-on, `ZE`; added.

**`english` completeness gap found and fixed**: was `[abatis]` only; both en.Wiktionary and zh.Wiktionary independently attest the character's actual primary senses, "fort" (stockade) and "brothel" — abatis is a narrower military term that happens to match the bound compound 鹿砦's specific sense but understates the character's own broader meaning; added both.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet, no `## Words` section) into the standard `## Notes` four-bullet format plus a `## Words` section citing [[words/鹿砦|鹿砦]] with ruby verified against the word's own `注音` field. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 磊 (8561; 225 characters remaining).

### 2026-08-23, iteration 2280 — [[characters/磊|磊]]

`graphemic_classification: 會意` (dual-source confirmed ideogrammic triplication of 石, "pile of rocks") reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 石` reconfirmed correct — genuine listing (item 26) on `Lookup/Radicals/Radical 112.md`. `japanese: [RAI]` reconfirmed complete — both go-on and kan-on share the identical reading らい. `japanese_native: ø` reconfirmed correct — ja.Wiktionary explicitly lists no kun'yomi. `cantonese: leoi5` and `korean: 뢰` (the North Korean/문화어 form, not the South Korean 두음법칙-shifted 뇌) reconfirmed correct. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `pos: 名詞` reconfirmed correct. `stand_in: 名専字` reconfirmed correct — zero hits for 磊 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-5-10.md` (item 1) and `Lookup/Korean/Korean Name ㄹ.md`. `mc_id: 5446` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`vietnamese` major bug found and fixed — four unattested readings mixed into a real 11-reading set**: stored 15 readings; cross-checked every one against hvdic.thivien.net (this vault's Vietnamese authority) and en.Wiktionary. Eleven are genuine (1 Âm Hán Việt `lỗi` + 10 Âm Nôm: `dội, giỏi, lẫn, lòi, lối, rủi, sói, trọi, trổi, xổi`, all confirmed by hvdic). Four — `lọi, lỏi, sõi, sỏi` — appear in neither source (not even `sõi`, which does appear in en.Wiktionary's Nôm list but not hvdic's, so was dropped per this session's practice of treating hvdic as authoritative on conflicts) and were removed as fabrications/typos.

**`joyo_level` cross-reference gap found and fixed**: the field itself already correctly said `表外字` (confirmed genuine via ja.Wiktionary), but the character was missing from `Lookup/Japanese/Hyōgai.md` itself; added as item 541.

**`english` completeness gap found and fixed**: was `[pile of rocks]` only; both en.Wiktionary and zh.Wiktionary independently attest a second genuine sense, "great; magnificent" (also underlying the figurative "open and honest" of 磊落); added.

**`aliases` filled**: was blank. Two genuine dual-source variants, [[磥]] and [[礌]] (both en.Wiktionary and zh.Wiktionary agree), neither with an independent page in this vault; added.

Rebuilt the malformed `## Notes` (unlinked bare "Components" bullet instead of a proper etymology bullet, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 禼 (8562; 224 characters remaining).

### 2026-08-23, iteration 2281 — [[characters/禼|禼]]

`graphemic_classification: 象形` (dual-source confirmed pictograph of a worm/insect) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 禸` reconfirmed correct — genuine listing (item 3) on `Lookup/Radicals/Radical 114.md`. `cantonese: sit3` reconfirmed correct. `japanese: [SETSU]`/`japanese_native: ø` left unchanged — 禼 is too obscure to appear on ja.Wiktionary at all (404), and weblio.jp explicitly flags it as "not commonly used in Japanese" without giving readings, so neither confirming nor overturning the existing value was possible; `joyo_level` correspondingly stays blank rather than guessing 表外字, now with that reasoning documented in Notes rather than left silent. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `stand_in: 名専字` reconfirmed correct — the sole grep hit, [[words/舌|舌]], is a false-positive prose mention (禼 listed only among a homophone-survey of ㄙㄝㄊ-reading characters, its own Notes explicitly confirming none has a self-pointing `stand_in`), not a genuine citation. `aliases` (blank) reconfirmed correct — both sources' listed historical variants (𥜽, 𥝁, 𠨄, 𠨁, 𠨆, 𠨈) are too obscure/unencodable, consistent with this session's established exclusion practice. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-7-5.md` (item 3) and `Lookup/Korean/Korean Name ㅅ.md`. `mc_id: 6012` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`english` accuracy bug found and fixed**: stored `[old names]`, an inaccurate gloss; both en.Wiktionary and zh.Wiktionary agree the primary sense is "a type of worm/insect" — corrected to `[insect]`. Both sources separately note 禼 as an ancient form of [[偰]] (an already-independent character in this vault, not merged), which is the likely source of the old "names" framing but isn't itself the character's primary meaning. Propagated the gloss fix to `Lookup/Radicals/Radical 114.md` (item 3) and `Lookup/SKIP/SKIP-2/SKIP-2-7-5.md` (item 3), both of which had copied the old gloss.

**`vietnamese` gap found and fixed — field left entirely empty**: hvdic.thivien.net attests a genuine Âm Hán Việt reading, `tiết`; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (insect).

**`## Derived Characters` section added**: one real 形聲 hit citing 禼 as phonetic component — [[characters/窃|窃]] ("to steal").

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 秉 (8563; 223 characters remaining).

### 2026-08-23, iteration 2282 — [[characters/秉|秉]]

`graphemic_classification: 會意` (dual-source confirmed, [[禾]] "plant" + [[又]] "hand," a hand holding a plant by the stalk) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 禾` reconfirmed correct — genuine listing (item 5) on `Lookup/Radicals/Radical 115.md`. `cantonese: bing2`, `vietnamese: [bảnh, bỉnh]`, `korean: 병` all reconfirmed complete and correct against en.Wiktionary. `mc_id: 1245` reconfirmed exact match (`CC 1000.md`: `1245. 秉`). `stand_in: 名専字` reconfirmed correct — the sole grep hit, [[words/柄国|柄国]], cites `characters: ["柄 (char)", 国]`, not 秉 itself (秉國 appears only in that word's `aliases` field as an alternate spelling, not a genuine constituent citation). `aliases` (blank) reconfirmed correct — en.Wiktionary explicitly denies any variant forms while zh.Wiktionary lists four (㨀, 抦, 柄, 棅); given the direct contradiction and that 柄 already has independent use in this vault, left unadded pending stronger corroboration. Already correctly cross-listed on `Lookup/SKIP/SKIP-4/SKIP-4-8-3.md` (item 4) and `Lookup/Korean/Korean Name ㅂ.md`.

**`hsk_level` bug found and fixed**: stored `4`, traced only to a colon-count entry on `Old HSK 4.md` (`[[秉]]: 1`, not genuine) — no plain-numbered entry exists in any `Old HSK N.md` file, and `Lookup/HSK/HSK No.md` itself already correctly lists 秉 among characters confirmed to have no genuine HSK level. Corrected to `hsk_level: 無`.

**`japanese` completeness gap found and fixed**: was `[HEI]` (kan-on) only; both ja.Wiktionary and en.Wiktionary independently attest a genuine go-on, `HYOU`; added.

**`japanese_native` bug found and fixed**: stored `と`, a truncated fragment; both en.Wiktionary and ja.Wiktionary agree on the genuine kun'yomi `とる`; corrected. Several further single-sourced candidates from ja.Wiktionary alone (いなたばり, いねたば, え, まもる) were left out — not corroborated by en.Wiktionary.

**`joyo_level` filled**: was blank. ja.Wiktionary directly confirms 秉 as 表外字; added as item 542 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`english` completeness gap found and fixed**: was `[bundle]` only; both en.Wiktionary and zh.Wiktionary independently attest further genuine senses, "to grasp; to hold" and "authority"; added as `grasp` and `authority`.

**`pos` filled**: was blank. Filled as `事詞`, matching the dominant verbal senses ("to grasp, to hold, to preside over").

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 郎 (8564; 222 characters remaining).

### 2026-08-23, iteration 2283 — [[characters/郎|郎]]

`graphemic_classification: 良` (dual-source confirmed 形声, semantic 邑 + phonetic 良) reconfirmed correct via en.Wiktionary and zh.Wiktionary — but the page's own malformed Notes bullet had the semantic/phonetic roles reversed ("semantic 良 + phonetic 邑"), fixed to match the field. `radical: 邑` reconfirmed correct — genuine listing (item 12) on `Lookup/Radicals/Radical 163.md`. `japanese: [ROU]` reconfirmed complete — both sources give an identical go-on/kan-on ろう. `japanese_native: おとこ` reconfirmed correct; three further single-sourced candidates from ja.Wiktionary alone (とう, もん, いら) were left out — not corroborated by en.Wiktionary. `mc_id: 499` reconfirmed exact match (`CC 0000.md`: `499. 郎`). `joyo_level: 高等` reconfirmed correct — genuine at `Lookup/Japanese/Jōyō - Kōtō.md` item 2124. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-6-3.md` (item 16) and `Lookup/Korean/Korean MS.md`.

**`stand_in` bug found and fixed — real citers hiding among five false positives**: stored `名専字` despite the page's own malformed Notes already loosely citing [[words/牛郎星|牛郎星]] and [[words/牛郎|牛郎]] as bound compounds. Ran a full `characters:`-field check on all seven grep hits: [[words/牛郎|牛郎]] and [[words/牛郎星|牛郎星]] genuinely cite 郎; [[words/銀河|銀河]], [[words/織女|織女]], [[words/牛|牛]], [[words/弓道|弓道]], and [[words/瘋顚|瘋顚]] were all false-positive prose mentions. Corrected `stand_in` to `牛郎`.

**`hsk_level` bug found and fixed**: stored `2`, traced only to colon-count entries on `Old HSK 2.md` and `Old HSK 4.md` (neither genuine). `Old HSK 6.md` has a genuine plain-numbered entry (`460. [[郎]]`); corrected to `hsk_level: 6`.

**`vietnamese` bug found and fixed**: stored 7 readings; hvdic.thivien.net's genuine readings are exactly `lang, loang, loen, sang` — the other three (`loẻn, lảng, lẳng`) appear in neither hvdic nor en.Wiktionary and were removed as unattested.

**`aliases` completeness gap found and fixed**: had `郞` (already correct) only; both en.Wiktionary and zh.Wiktionary independently attest a second genuine variant, `郒`, with no independent page in this vault; added. A third single-sourced candidate from en.Wiktionary alone, 𨝥, was left out.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses.

**`## Derived Characters` completeness gap found and fixed**: the malformed notes listed only [[characters/螂|螂]]; a full grep turned up two further genuine 形声 hits citing 郎 as phonetic — [[characters/廊|廊]] and [[characters/榔|榔]]; added.

Rebuilt the malformed `## Notes` (reversed semantic/phonetic roles, a stray "Derived characters" sub-heading with no proper `##` section, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet, `## Words` bullets folded loosely into Notes) into the standard `## Notes` four-bullet format plus proper `## Words` and `## Derived Characters` sections. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 訛 (8565; 221 characters remaining).

### 2026-08-23, iteration 2284 — [[characters/訛|訛]]

`graphemic_classification: 化` (dual-source confirmed 形声, semantic 言 + phonetic 化, OC \*hŋʷraːls) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 言` reconfirmed correct — genuine listing (item 10) on `Lookup/Radicals/Radical 149.md`. `japanese: [KA, GA]` reconfirmed complete — both sources give go-on/kan-on が (GA) and kan'yō-on か (KA). `korean: 와` reconfirmed correct. `stand_in: 名専字` reconfirmed correct — zero hits for 訛 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-7-4.md` (item 10) and `Lookup/Korean/Korean Name ㅇ.md`.

**`mc_id` off-by-one bug found and fixed**: stored `3295` was actually 駙's rank; correct rank for 訛 is `3296` (`CC 3000.md`: `3295. 駙`, `3296. 訛`).

**`hsk_level` bug found and fixed**: stored `4`, traced only to colon-count entries on `Old HSK 4.md` (both `[讹]: 1` and `[[訛]]: 1`, neither genuine) — thoroughly checked all four `Old HSK N.md` files and found no genuine plain-numbered entry anywhere, and 訛 was also entirely absent from `Lookup/HSK/HSK No.md`. Corrected to `hsk_level: 無` and added 訛 to `Lookup/HSK/HSK No.md`'s list.

**`joyo_level` filled**: was blank. ja.Wiktionary directly confirms 訛 as 表外字; added as item 543 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`japanese_native` bug found and fixed**: stored `あやま`, a truncated fragment; both en.Wiktionary and ja.Wiktionary agree on three genuine kun'yomi, `なまる`, `なまり`, `あやまる`; corrected to all three, full forms.

**`vietnamese` bug found and fixed**: stored `[ngoa, ngoả]`; hvdic.thivien.net's sole genuine reading (identical Âm Hán Việt and Âm Nôm) is `ngoa` — `ngoả` traced only to en.Wiktionary, which itself presented it ambiguously ("ngỏa/ngoả"), and wasn't corroborated by hvdic; removed.

**`aliases` completeness gap found and fixed**: had `讹` (simplified form) only; both en.Wiktionary and zh.Wiktionary independently attest two further genuine variants, `吪` and `䚰`, neither with an independent page in this vault; added. A third single-sourced candidate from zh.Wiktionary alone, 譌, was left out.

**`pos` filled**: was blank. Filled as `事詞`, matching the dominant verbal sense ("to swindle, cheat, deceive, extort").

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 稜 (8567; 220 characters remaining).

### 2026-08-23, iteration 2285 — [[characters/稜|稜]]

`graphemic_classification: 夌` (dual-source confirmed 形声, semantic 禾 + phonetic 夌) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 禾` reconfirmed correct — genuine listing (item 20) on `Lookup/Radicals/Radical 115.md`. `cantonese: ling4` reconfirmed correct and complete — en.Wiktionary's claimed second reading `ling6` isn't corroborated by zh.Wiktionary, which gives only `ling4`; left unadded. `korean: 릉` reconfirmed correct (the North Korean/문화어 form, not the South Korean 두음법칙-shifted 능). `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 392. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-5-8.md` (item 12) and `Lookup/Korean/Korean Name ㄹ.md`. `mc_id: 4473` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`stand_in` bug found and fixed**: stored `名専字` despite a genuine citer — of three apparent hits, only [[words/三稜鏡|三稜鏡]]'s own `characters:` field genuinely lists 稜 ([[words/塑膠|塑膠]] and [[words/下痢|下痢]] were false-positive prose mentions). Corrected `stand_in` to `三稜鏡`.

**`japanese` completeness gap found and fixed**: was `[RYOU]` (the kan'yō-on/conventional reading) only; both en.Wiktionary and ja.Wiktionary independently attest a genuine go-on/kan-on, `ROU`; added.

**`japanese_native` completeness gap found and fixed**: was `いつ` only (genuine, not truncated); both sources independently attest a second genuine kun'yomi, `かど`; added.

**`vietnamese` completeness gap found and fixed**: was `[lăng]` only; hvdic.thivien.net's genuine readings additionally include a second Âm Hán Việt, `lắng`; added.

**`aliases` filled**: was blank. One genuine dual-source variant, [[棱]] (the simplified form, explicitly listed as 異體字 by zh.Wiktionary and as "Simplified: 棱" by en.Wiktionary), with no independent page in this vault; added. A second single-sourced candidate from en.Wiktionary alone, 楞, was left out (楞 also already sits unredirected on `Lookup/Korean/Korean Name ㄹ.md`, but without dual-source confirmation it wasn't converted to a redirect).

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet, no `## Words` section) into the standard `## Notes` four-bullet format plus a `## Words` section citing [[words/三稜鏡|三稜鏡]] with ruby verified against the word's own `注音` field. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 窩 (8569; 219 characters remaining).

### 2026-08-23, iteration 2286 — [[characters/窩|窩]]

`graphemic_classification: 咼` (dual-source confirmed 形聲, semantic 穴 + phonetic 咼, OC \*kʰʷroːl) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 穴` reconfirmed correct — genuine listing (item 15) on `Lookup/Radicals/Radical 116.md`. `japanese: [KA, WA]` reconfirmed complete — both sources give go-on/kan-on わ (WA) and kan'yō-on か (KA). `japanese_native: むろ` reconfirmed correct and complete. `vietnamese: [oa]` reconfirmed correct and complete against hvdic.thivien.net — en.Wiktionary's claimed "ổ" wasn't corroborated by hvdic (this vault's authority) and was correctly left out already. `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md` item 17. `mc_id: 0` reconfirmed correct — genuinely absent from all four `CC N000.md` files. `stand_in: 名専字` reconfirmed correct — zero hits for 窩 anywhere in `words/`. `aliases: [窝]` reconfirmed correct — a second single-sourced candidate from zh.Wiktionary alone, 䆧, wasn't corroborated by en.Wiktionary and was left out. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-11.md` (item 8) and `Lookup/Korean/Korean Name ㅇ.md`.

**`hsk_level` bug found and fixed**: stored `4`, traced only to colon-count entries on `Old HSK 4.md` (both `[窝]: 2` and `[[窩]]: 2`, neither genuine). `Old HSK 6.md` has a genuine plain-numbered entry (`371. [窝]`); corrected to `hsk_level: 6`.

**`english` completeness gap found and fixed**: was `[fossa]` only, an unusually narrow anatomical-loan gloss for what both en.Wiktionary and zh.Wiktionary attest as much broader core senses; added `nest` and `cave`.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 筍 (8571; 218 characters remaining).

### 2026-08-23, iteration 2287 — [[characters/筍|筍]]

`graphemic_classification: 旬` (dual-source confirmed 形聲, semantic 竹 + phonetic 旬, OC \*sqʰʷinʔ) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 竹` reconfirmed correct — genuine listing (item 15) on `Lookup/Radicals/Radical 118.md`. `japanese: [JUN, SHUN]` reconfirmed complete — matches ja.Wiktionary's kan'yō-on ジュン and go-on/kan-on シュン exactly. `mc_id: 4606` reconfirmed as trusted long-tail (>4000, not cross-checked per policy). `stand_in: 竹筍` reconfirmed correct — sole citer, the word's own independent page. `aliases: [笋, 荀]` reconfirmed correct — 荀 has no independent page and `Lookup/Korean/Korean Name ㅅ.md` already explicitly points its own `[荀]` entry directly at `characters/筍.md`, corroborating the alias internally. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-6-6.md` (item 8).

**`hsk_level` bug found and fixed**: stored `4`, traced only to colon-count entries on `Old HSK 4.md` (both `[笋]: 1` and `[[筍]]: 1`, neither genuine) — thoroughly checked all four `Old HSK N.md` files and found no genuine plain-numbered entry anywhere, and 筍 was also entirely absent from `Lookup/HSK/HSK No.md`. Corrected to `hsk_level: 無` and added 筍 to `Lookup/HSK/HSK No.md`'s list.

**`joyo_level` filled**: was blank. ja.Wiktionary directly confirms 筍 as 表外字; added as item 544 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`japanese_native` completeness gap found and fixed**: was `たかんな` only; both en.Wiktionary and ja.Wiktionary independently attest a second genuine kun'yomi, `たけのこ` (also this page's own `english` gloss, "bamboo shoot"); added.

**`vietnamese` major bug found and fixed — malformed field plus a large completeness gap**: stored as a single un-listified string `duẩn duẫn` (a YAML formatting bug, not a proper list); hvdic.thivien.net's genuine readings are six in total — `duẩn, duẫn, tuân, tuẩn, tuận, tấn` — corrected to a proper list with all six. En.Wiktionary's own candidates (sũn, hũn) weren't corroborated by hvdic and were left out.

Rebuilt the malformed `## Notes`/`## Words` ordering (Words appeared before the wrong-heading-level `# Notes`, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard Notes-then-Words convention. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 箏 (8572; 217 characters remaining).

### 2026-08-23, iteration 2288 — [[characters/箏|箏]]

`graphemic_classification: 争` (dual-source confirmed 形声, semantic 竹 + phonetic 爭/争, OC \*ʔsreːŋ) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 竹` reconfirmed correct — genuine listing (item 22) on `Lookup/Radicals/Radical 118.md`. `japanese: [SOU, SHOU]` and `japanese_native: こと` reconfirmed complete — both sources agree exactly. `vietnamese: [giành, tranh]` reconfirmed complete and exact against hvdic.thivien.net. `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md`. `korean_native: 쟁` (identical to the Sino-Korean reading) reconfirmed plausible — a specialized loanword-instrument character with no distinct native Korean gloss, consistent with similar cases; not flagged without contrary evidence. `stand_in: 古箏` reconfirmed correct — sole citer, the word's own independent page. `aliases: [筝]` reconfirmed correct (simplified form, matching both sources). Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-6-8.md` (item 3) and `Lookup/Korean/Korean Name ㅈ.md`. `mc_id: 5163` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`cantonese` completeness gap found and fixed**: stored `zang1` only; both en.Wiktionary and zh.Wiktionary independently attest a second genuine (literary) jyutping reading, `zaang1`; added.

**`hsk_level` bug found and fixed**: stored `4`, traced only to colon-count entries on `Old HSK 4.md` (both `[筝]: 1` and `[[箏]]: 1`, neither genuine) — thoroughly checked all four `Old HSK N.md` files and found no genuine plain-numbered entry anywhere, and 箏 was also entirely absent from `Lookup/HSK/HSK No.md`. Corrected to `hsk_level: 無` and added 箏 to `Lookup/HSK/HSK No.md`'s list.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (zither instrument).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format; `## Words` (citing [[words/古箏|古箏]], ruby verified against the word's own `注音` field) reconfirmed correct, no changes. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 篆 (8573; 216 characters remaining).

### 2026-08-23, iteration 2289 — [[characters/篆|篆]]

`graphemic_classification: 彖` (dual-source confirmed 形声, semantic 竹 "bamboo, the writing material" + phonetic 彖) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 竹` reconfirmed correct — genuine listing (item 31) on `Lookup/Radicals/Radical 118.md`. `japanese_native: ø` reconfirmed correct — ja.Wiktionary explicitly lists no kun'yomi, despite en.Wiktionary's single-sourced claim of こしきしば. `vietnamese: [chệ, chệnh, triển, triện]` reconfirmed complete and exact against hvdic.thivien.net. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md` item 288. `stand_in: 篆書` reconfirmed correct — sole citer, the word's own independent page. `aliases` (blank) reconfirmed correct — zh.Wiktionary's single-sourced variant candidate 蒃 wasn't corroborated by en.Wiktionary. A chengyu-citation grep hit, [[chengyu/異体不容|異体不容]], was checked and confirmed a false positive — 篆 appears only inside the prose discussion (小篆), not among the chengyu's own four characters. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-6-9.md` (item 5) and `Lookup/Korean/Korean Name ㅈ.md`.

**`mc_id` off-by-one bug found and fixed**: stored `3421` was actually 跗's rank; correct rank for 篆 is `3422` (`CC 3000.md`: `3421. 跗`, `3422. 篆`).

**`japanese` completeness gap found and fixed**: was `[TEN]` (kan-on) only; both ja.Wiktionary and en.Wiktionary independently attest a genuine go-on, `DEN`; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (seal script).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format; `## Words` (citing [[words/篆書|篆書]], ruby verified against the word's own `注音` field) reconfirmed correct, no changes. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 篠 (8574; 215 characters remaining).

### 2026-08-23, iteration 2290 — [[characters/篠|篠]]

`radical: 竹` reconfirmed correct — genuine listing (item 35) on `Lookup/Radicals/Radical 118.md`. `japanese: [SHOU]` reconfirmed complete — both go-on and kan-on share the identical reading しょう. `vietnamese: [tiểu]` reconfirmed complete and exact against hvdic.thivien.net. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 243. `stand_in: 篠竹` reconfirmed correct. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-6-11.md` (item 1) and `Lookup/Korean/Korean Name ㅅ.md`. `mc_id: 6223` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`graphemic_classification` alias-citation bug found and fixed**: stored `條` — dual-source confirmed as the textbook phonetic component (en.Wiktionary and zh.Wiktionary both name it), but 條 has no independent page in this vault; [[characters/条 (char)|条 (char)]]'s own `aliases` field lists 條 as pointing to it. Per this vault's established alias-citation convention (cf. `characters/瞼.md`/㑒), corrected to cite the parent-form page `条` instead.

**`hsk_level` gap filled — genuinely absent, not just unfilled**: was the empty-string sentinel; thoroughly checked all four `Old HSK N.md` files and `Lookup/HSK/HSK No.md` and found zero hits for 篠 anywhere. Filled `hsk_level: 無` and added 篠 to `Lookup/HSK/HSK No.md`'s list.

**`japanese_native` completeness gap found and fixed**: was `ささ` only; both en.Wiktionary and ja.Wiktionary independently attest a second genuine kun'yomi, `しの`; added. Two further single-sourced candidates from en.Wiktionary alone (しぬ, すず) were left out — not corroborated by ja.Wiktionary.

**`aliases` filled**: was blank. Three genuine dual-source variants — [[筱]], [[𥴽]], [[𥭪]] (all attested by both en.Wiktionary and zh.Wiktionary) — none with independent pages in this vault; added. A fourth single-sourced candidate from zh.Wiktionary alone, 筿, was left out.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (dwarf bamboo).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet, `## Words` placed before Notes instead of after) into the standard `## Notes` four-bullet format, reordered before the pre-existing `## Words` section. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 簞 (8575; 214 characters remaining).

### 2026-08-23, iteration 2291 — [[characters/簞|簞]]

`graphemic_classification: 単` reconfirmed correct — both en.Wiktionary and zh.Wiktionary name the textbook phonetic as traditional 單, but 單 has no independent page in this vault; [[characters/単|単]]'s own `aliases` field lists both 單 and 单 as pointing to it, confirming the parent-form citation is correct per this session's established alias-citation convention (cf. [[characters/篠|篠]]/条 earlier this session). `radical: 竹` reconfirmed correct — genuine listing (item 36) on `Lookup/Radicals/Radical 118.md`. `japanese: [TAN]` and `japanese_native: はこ` reconfirmed complete and correct — dual-source exact match. `vietnamese: [đan]` reconfirmed complete and exact against hvdic.thivien.net. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 402. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `stand_in: 名専字` reconfirmed correct — zero hits for 簞 anywhere in `words/`, and no chengyu citations either (the classical idiom 簞食瓢飲 doesn't yet exist as a page in this vault). Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-6-12.md` (item 1) and `Lookup/Korean/Korean Name ㄷ.md`.

**`mc_id` off-by-one bug found and fixed**: stored `3273` was actually 劭's rank; correct rank for 簞 is `3274` (`CC 3000.md`: `3273. 劭`, `3274. 簞`).

**`aliases` bug found and fixed — a genuinely unrelated character mistaken for a variant**: stored `[蓧, 箪]`; 箪 (the simplified form) is dual-source confirmed and correct, but 蓧 checked out as a wholly distinct character with its own unrelated readings (diào/tiáo/dí, "weeding basket/implement") — neither en.Wiktionary's nor zh.Wiktionary's entries for 簞 itself mention 蓧 as a variant, and 蓧's own en.Wiktionary entry doesn't cross-reference 簞 either. Removed as a false alias.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (bamboo basket).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 簫 (8576; 213 characters remaining).

### 2026-08-23, iteration 2292 — [[characters/簫|簫]]

`radical: 竹` reconfirmed correct — genuine listing (item 38) on `Lookup/Radicals/Radical 118.md`. `japanese: [SHOU]` and `japanese_native: ふえ` reconfirmed correct and complete — a second ja.Wiktionary-only kun'yomi candidate, しょうのふえ (a compound "shō's flute" reading), was left out as not a standalone genuine kun'yomi. `vietnamese: [tiu, tiêu]` reconfirmed complete and exact against en.Wiktionary. `hsk_level: 無` reconfirmed correct. `stand_in: 洞簫` reconfirmed correct — sole citer, the word's own independent page. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-6-13.md` (item 1) and `Lookup/Korean/Korean Name ㅅ.md`.

**`graphemic_classification` alias-citation bug found and fixed**: stored `肅` — dual-source confirmed as the textbook phonetic component (en.Wiktionary and zh.Wiktionary both name it), but 肅 has no independent page in this vault; [[characters/粛|粛]]'s own `aliases` field lists both 肅 and 肃 as pointing to it. Per this session's established alias-citation convention (cf. 篠/条 and 簞/単 earlier this session), corrected to cite the parent-form page `粛` instead.

**`mc_id` off-by-one bug found and fixed**: stored `3041` was actually 縷's rank; correct rank for 簫 is `3042` (`CC 3000.md`: `3041. 縷`, `3042. 簫`).

**`joyo_level` filled**: was blank. ja.Wiktionary directly confirms 簫 as 表外字; added as item 545 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`aliases` completeness gap found and fixed**: had `箫` (simplified form) only; both en.Wiktionary and zh.Wiktionary independently attest two further genuine variants, `箾` and `簘`, neither with an independent page in this vault; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (the xiao flute).

Rebuilt the malformed `## Notes`/`## Words` ordering (Words appeared before the wrong-heading-level `# Notes`, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard Notes-then-Words convention. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 簾 (8577; 212 characters remaining).

### 2026-08-23, iteration 2293 — [[characters/簾|簾]]

`graphemic_classification: 廉` (dual-source confirmed 形声, semantic 竹 + phonetic 廉, OC \*ɡ·rem) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 竹` reconfirmed correct — genuine listing (item 39) on `Lookup/Radicals/Radical 118.md`. `japanese: [REN]` reconfirmed complete — both go-on and kan-on share the identical reading れん. `vietnamese: [liêm, rèm]` reconfirmed complete and exact against hvdic.thivien.net. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 403. `stand_in: 暖簾` reconfirmed correct — sole citer, the word's own independent page. `aliases: [帘]` reconfirmed correct — zh.Wiktionary's single-sourced second candidate 𢅖 wasn't corroborated by en.Wiktionary. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-6-13.md` (item 2) and `Lookup/Korean/Korean Name ㄹ.md`. `mc_id: 5629` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`hsk_level` bug found and fixed — genuine level hiding under simplified sibling glyph**: stored `3`, matching a colon-count entry on `Old HSK 3.md` (`[帘]: 1`, not genuine) and a listing on `Lookup/HSK/HSK No.md` (implying no genuine level) — but `Old HSK 5.md` has a genuine plain-numbered entry under the simplified sibling glyph 帘 (`500. [帘]`). Corrected `hsk_level` to `5` and removed the now-stale entry from `Lookup/HSK/HSK No.md`.

**`japanese_native` completeness gap found and fixed**: was `す` only; both en.Wiktionary and ja.Wiktionary independently attest a second genuine kun'yomi, `すだれ` (the everyday name for the object); added, keeping both.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses (blind, screen, curtain).

Rebuilt the malformed `## Notes` (two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard four-bullet format; `## Words` (citing [[words/暖簾|暖簾]], ruby verified against the word's own `注音` field) reconfirmed correct, no changes. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 紗 (8579; 210 characters remaining).

### 2026-08-23, iteration 2294 — [[characters/紗|紗]]

`graphemic_classification: 少` reconfirmed correct, with a genuine source conflict investigated and documented: zh.Wiktionary corroborates 少 (matching the stored value), while en.Wiktionary instead names 沙 as phonetic. Kept `少` per zh.Wiktionary, consistent with this session's practice on such conflicts (cf. 甬, 睾). `radical: 糸` reconfirmed correct — genuine listing (item 12) on `Lookup/Radicals/Radical 120.md`. `japanese: [SA, SHA]` reconfirmed complete — dual-source exact match. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 406. `vietnamese: [sa]` reconfirmed correct. `stand_in: 名専字` reconfirmed correct — zero hits for 紗 anywhere in `words/`. `aliases: [纱]` reconfirmed correct. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-6-4.md` (item 17) and `Lookup/Korean/Korean Name ㅅ.md`. `mc_id: 5668` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`english` accuracy bug found and fixed**: stored `[gauze, yard]` — en.Wiktionary explicitly denies "yard" (the unit of measurement) as a sense of this character, which relates to textile fabrics and threads, not distance; replaced with the dual-source-confirmed sense `yarn`.

**`hsk_level` bug found and fixed**: stored `3`, traced only to colon-count entries on `Old HSK 3.md` (both `[纱]: 1` and `[[紗]]: 1`, neither genuine) — thoroughly checked all four `Old HSK N.md` files and found no genuine plain-numbered entry anywhere, and 紗 was also entirely absent from `Lookup/HSK/HSK No.md`. Corrected to `hsk_level: 無` and added 紗 to `Lookup/HSK/HSK No.md`'s list.

**`japanese_native` completeness gap found and fixed**: was `うすぎぬ` only; both en.Wiktionary and ja.Wiktionary independently attest two further genuine kun'yomi, `すず` and `たえ`; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 紘 (8580; 209 characters remaining).

### 2026-08-23, iteration 2295 — [[characters/紘|紘]]

`graphemic_classification: 厷` reconfirmed correct — en.Wiktionary's own composition breakdown ("⿰糹厷") directly confirms 厷 is literally embedded in the glyph; zh.Wiktionary's "phonetic 宏" describes the broader phonetic series (宏 itself uses 厷 as phonetic — cf. [[characters/宏|宏]]), not a contradiction. `radical: 糸` reconfirmed correct — genuine listing (item 13) on `Lookup/Radicals/Radical 120.md`. `vietnamese: [hoành]` reconfirmed complete and exact against both en.Wiktionary and hvdic.thivien.net. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 246. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `japanese_native: おおづな` reconfirmed correct; further single-sourced candidates from each side (en.Wiktionary's ひも; ja.Wiktionary's つな, つなぐ) were left out, uncorroborated by the other source. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-6-4.md` (item 18) and `Lookup/Korean/Korean Name ㄱ.md`.

**`stand_in` bug found and fixed**: stored `名専字` despite a genuine citer — [[words/八紘|八紘]]'s own `characters:` field lists both 八 and 紘. Corrected to `八紘`.

**`mc_id` off-by-one bug found and fixed**: stored `3697` was actually 疥's rank; correct rank for 紘 is `3698` (`CC 3000.md`: `3697. 疥`, `3698. 紘`).

**`japanese` completeness gap found and fixed**: was `[KOU, GYOU]`; both en.Wiktionary and ja.Wiktionary independently attest a further genuine go-on, `OU`; added.

**`english` completeness gap found and fixed**: was `[string, cord]` only; both en.Wiktionary and zh.Wiktionary independently attest a second genuine sense, "vast; expansive"; added.

**`aliases` completeness gap found and fixed**: had `纮` (simplified form) only; both en.Wiktionary and zh.Wiktionary independently attest a second genuine variant, `紭`, with no independent page in this vault; added. Further single-sourced candidates from each side (en.Wiktionary's 綋/𫟄/𰬋; zh.Wiktionary's 絋) were left out.

**`## Chengyu` section added**: a real hit, [[chengyu/八紘一宇|八紘一宇]], genuinely contains 紘 among its four characters; ruby verified against the chengyu's own `注音` field.

Rebuilt the entirely bare-linked page (no `# Notes`/`## Notes` heading at all, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet, no `## Words` section) into the standard `## Notes` four-bullet format plus `## Words` and `## Chengyu`. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 紬 (8581; 208 characters remaining).

### 2026-08-23, iteration 2296 — [[characters/紬|紬]]

`graphemic_classification: 由` (dual-source confirmed 形声, semantic 糸 + phonetic 由, OC \*lɯw) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 糸` reconfirmed correct — genuine listing (item 20) on `Lookup/Radicals/Radical 120.md`. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 247. `stand_in: 名専字` reconfirmed correct — zero hits for 紬 anywhere in `words/`. `aliases: [綢, 䌷]` reconfirmed correct — 綢 is explicitly redirected to `characters/紬.md` on `Lookup/Korean/Korean Name ㅈ.md`, corroborating this vault's own established treatment of 紬 as standing in for 綢. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-6-5.md` (item 8) and `Lookup/Korean/Korean Name ㅈ.md`. `mc_id: 5682` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`hsk_level` gap filled — genuine level hiding under simplified sibling glyph**: was blank; `Old HSK 5.md` has a genuine plain-numbered entry under the simplified sibling glyph 绸 (`350. [绸]`) — the colon-count entries on `Old HSK 4.md` (both 绸 and 綢) are not genuine and were correctly ignored. Filled `hsk_level: 5`.

**`cantonese` completeness gap found and fixed**: stored `cau4` only; both en.Wiktionary and zh.Wiktionary independently attest a second genuine jyutping reading, `cau1` (tied to the obsolete "draw out; collect" senses); added.

**`japanese` completeness gap found and fixed**: was `[CHUU]` (kan-on) only; both ja.Wiktionary and en.Wiktionary independently attest a genuine go-on, `JUU`; added.

**`japanese_native` bug found and fixed**: stored `つむ`, a truncated fragment; both en.Wiktionary and ja.Wiktionary agree on two genuine kun'yomi in full form, `つむぎ` and `つむぐ`; corrected.

**`vietnamese` bug found and fixed**: stored `[dò, trìu, trừu]`; hvdic.thivien.net's genuine readings are exactly `dò, trừu` — `trìu` appears in neither hvdic nor en.Wiktionary and was removed as unattested.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses (silk fabric).

**`## Chengyu` bullet reformatted**: the existing bare `[[未雨紬謬]]` link (a real hit — this vault's own `chengyu/未雨紬謬.md` deliberately uses 紬 as a stand-in for 綢, with 未雨綢繆 recorded among its own `aliases`) lacked ruby; added, verified against the chengyu's own `注音` field.

Rebuilt the malformed `## Notes` (no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet, two floating unlinked CC wikilinks dangling after the Chengyu section) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 絨 (8582; 207 characters remaining).

### 2026-08-23, iteration 2297 — [[characters/絨|絨]]

`graphemic_classification: 戎` (dual-source confirmed 形声, semantic 糸 + phonetic 戎, OC \*njuŋ) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 糸` reconfirmed correct — genuine listing (item 39) on `Lookup/Radicals/Radical 120.md`. `mc_id: 0` reconfirmed correct — genuinely absent from all four `CC N000.md` files. `japanese_native: ø` reconfirmed correct — ja.Wiktionary explicitly lists no kun'yomi; en.Wiktionary's single-sourced candidates (ねりいと, けおり) weren't corroborated and stayed unadded. `vietnamese: [nhung]` reconfirmed complete and exact against hvdic.thivien.net. `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md` item 152. `stand_in: 天鵝絨` reconfirmed correct — sole citer, the word's own independent page. `aliases: [绒]` reconfirmed correct and complete — zh.Wiktionary's enormous list of further variants (𦶪, 𦔋, 狨, 毧, 羢, etc.) wasn't corroborated by en.Wiktionary for any single one, so none were added. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-6-6.md` (item 11) and `Lookup/Korean/Korean Name ㅇ.md`.

**`cantonese` bug found and fixed**: stored `jung2`, matching neither source — both en.Wiktionary and zh.Wiktionary agree on `jung4`; corrected.

**`hsk_level` bug found and fixed**: stored `4`, traced only to colon-count entries on `Old HSK 4.md` (both `[[絨]]: 1` and `[绒]: 1`, neither genuine). `Old HSK 6.md` has a genuine plain-numbered entry under the simplified sibling glyph 绒 (`504. [绒]`); corrected to `hsk_level: 6`.

**`japanese` completeness gap found and fixed**: was `[JUU]` (kan-on) only; both ja.Wiktionary and en.Wiktionary independently attest a genuine go-on, `NYUU`; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (velvet).

**Stray out-of-scope note removed**: a bare `天鵞絨 --> 天鵝絨` bullet documented a spelling-variant redirect for the *word* [[words/天鵝絨|天鵝絨]] (not corroborated in that word's own `aliases` field either), unrelated to 絨 the character itself; removed during the Notes rebuild.

Rebuilt the malformed `## Notes` (two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet, the stray word-redirect note) into the standard `## Notes` four-bullet format; `## Words` (citing [[words/天鵝絨|天鵝絨]], ruby verified against the word's own `注音` field) reconfirmed correct, no changes. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 緋 (8583; 206 characters remaining).

### 2026-08-23, iteration 2298 — [[characters/緋|緋]]

`graphemic_classification: 非` (dual-source confirmed 形声, semantic 糸 + phonetic 非, OC \*pɯl) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 糸` reconfirmed correct — genuine listing (item 53) on `Lookup/Radicals/Radical 120.md`. `japanese: [HI]` reconfirmed complete — both go-on and kan-on share the identical reading ひ. `cantonese: fei1`, `vietnamese: [phi]` reconfirmed correct and complete. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 1. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `english: [scarlet, dark red, crimson, purple]` reconfirmed correct — the "purple" sense, despite reading oddly, is corroborated (if imperfectly transcribed) by zh.Wiktionary's own entry. `stand_in: 名専字` reconfirmed correct — the sole grep hit, [[words/火紅|火紅]], is a false-positive prose mention (緋 appearing only in a comparative-reading note), not a genuine citation. `aliases: [绯]` reconfirmed correct. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-6-8.md` (item 9) and `Lookup/Korean/Korean Name ㅂ.md`. `mc_id: 10457` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`japanese_native` completeness gap found and fixed**: was `あか` only; ja.Wiktionary directly lists `あけ` as a second genuine kun'yomi (en.Wiktionary categorizes it as nanori instead, but ja.Wiktionary — authoritative for kun'yomi specifically — lists it as a true kun'yomi); added.

**`pos` filled**: was blank. Filled as `性詞`, matching the adjectival/color senses.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 缸 (8584; 205 characters remaining).

### 2026-08-23, iteration 2299 — [[characters/缸|缸]]

`graphemic_classification: 工` (dual-source confirmed 形声, semantic 缶 + phonetic 工) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 缶` reconfirmed correct — genuine listing (item 3) on `Lookup/Radicals/Radical 121.md`. `japanese_native: かめ` reconfirmed correct; a second single-sourced candidate from en.Wiktionary alone (もたい) was left out. `pos: 名詞` reconfirmed correct. `stand_in: 名専字` reconfirmed correct — the sole grep hit, [[words/浴槽|浴槽]], is a false-positive prose mention (缸 noted only as the character Mandarin/Cantonese use in the *different* compound 浴缸), not a genuine citation. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-6-3.md` (item 7) and `Lookup/Korean/Korean Name ㅎ.md`. `mc_id: 8105` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`hsk_level` bug found and fixed**: stored `3`, traced only to a colon-count entry on `Old HSK 3.md` (`[[缸]]: 1`, not genuine) — thoroughly checked all four `Old HSK N.md` files and found no genuine plain-numbered entry anywhere, and 缸 was also entirely absent from `Lookup/HSK/HSK No.md`. Corrected to `hsk_level: 無` and added 缸 to `Lookup/HSK/HSK No.md`'s list.

**`joyo_level` cross-reference gap found and fixed**: the field itself already correctly said `表外字` (confirmed genuine via ja.Wiktionary), but the character was missing from `Lookup/Japanese/Hyōgai.md` itself; added as item 546.

**`japanese` completeness gap found and fixed**: was `[KOU]` only; ja.Wiktionary — which explicitly splits go-on and kan-on — independently attests a genuine go-on, `GOU`; added.

**`vietnamese` major completeness gap found and fixed**: was `[cong, hồng]` only; hvdic.thivien.net's genuine readings total six — `ang, cang, cương, hang` (Âm Hán Việt) plus `cong, hồng` (Âm Nôm); added the four missing ones.

**`aliases` filled**: was blank. Two genuine dual-source variants, [[堈]] and [[罁]] (both en.Wiktionary and zh.Wiktionary agree), neither with an independent page in this vault; added. Two further single-sourced candidates (zh.Wiktionary's 㼚, 堽) were left out.

Rebuilt the malformed `## Notes` (unlinked bare "Components" bullet instead of proper etymology, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 羚 (8585; 204 characters remaining).

### 2026-08-23, iteration 2300 — [[characters/羚|羚]]

`graphemic_classification: 令` (dual-source confirmed 形声, semantic 羊 + phonetic 令) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 羊` reconfirmed correct — genuine listing (item 3) on `Lookup/Radicals/Radical 123.md`. `japanese: [REI, RYOU]` and `japanese_native: かもしか` reconfirmed complete and correct — dual-source exact match. `vietnamese: [linh]` reconfirmed complete. `korean: 령` reconfirmed correct (North Korean/문화어 form, not the South Korean 두음법칙-shifted 영). `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 319. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `stand_in: 羚羊` reconfirmed correct — of three apparent citers, [[words/羚羊|羚羊]] and [[words/麒麟羚羊|麒麟羚羊]] genuinely cite 羚; [[words/麒麟|麒麟]] was a false-positive prose mention. `aliases: [麢]` reconfirmed correct; further single-sourced candidates from en.Wiktionary alone (䴫, 𦏪, 𦏰, 𪋪) weren't corroborated by zh.Wiktionary and stayed unadded. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-6-5.md` (item 14) and `Lookup/Korean/Korean Name ㄹ.md`. `mc_id: 5332` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (antelope).

**`## Words` section added**: citing both genuine citers, [[words/羚羊|羚羊]] and [[words/麒麟羚羊|麒麟羚羊]], rubies verified against each word's own `注音` field.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet, no `## Words` section) into the standard `## Notes` four-bullet format plus `## Words`. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 翟 (8586; 203 characters remaining).

### 2026-08-23, iteration 2301 — [[characters/翟|翟]]

`graphemic_classification: 會意` (dual-source confirmed ideogrammic compound of 羽 "feather" + 隹 "bird," depicting a long-tailed pheasant) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 羽` reconfirmed correct — genuine listing (item 12) on `Lookup/Radicals/Radical 124.md`. `mc_id: 1202` reconfirmed exact match (`CC 1000.md`: `1202. 翟`). `japanese: [KEKI, JAKU, TAKU]` reconfirmed complete — the consensus three across en.Wiktionary and weblio.jp; a fourth on'yomi is claimed by each source but they disagree with each other (てき vs たい), so neither was added. `japanese_native: きじ`, `vietnamese: [địch]`, `hsk_level: 無`, `pos: 名詞` all reconfirmed correct. `stand_in: 名専字` reconfirmed correct — zero hits for 翟 anywhere in `words/`. `## Derived Characters` (citing [[characters/擢|擢]]) reconfirmed correct — genuine `graphemic_classification: 翟` citation, ruby verified. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-6-8.md` (item 8) and `Lookup/Korean/Korean Name ㅈ.md`.

**`aliases` bug found and fixed — a phonetically-related derived character mistaken for a true variant**: stored `[糶]` ("to sell grain," genuinely unrelated in meaning); en.Wiktionary explicitly clarifies 糶 is listed among derived characters sharing phonetic similarity with 翟 (rice 米 + phonetic 翟), not a true orthographic variant — the same bug pattern as 簞/蓧 earlier this session. Removed; 糶 has no page in this vault yet to add under Derived Characters instead.

**`joyo_level` cross-reference gap found and fixed**: the field itself already said `表外字`, but the character was missing from `Lookup/Japanese/Hyōgai.md` itself; added as item 547.

Rebuilt the malformed `## Notes` (unlinked bare "Components" bullet instead of proper etymology, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 翠 (8587; 202 characters remaining).

### 2026-08-23, iteration 2302 — [[characters/翠|翠]]

`graphemic_classification: 卒` (dual-source confirmed 形声, semantic 羽 + phonetic 卒, OC \*sʰuds) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 羽` reconfirmed correct — genuine listing (item 11) on `Lookup/Radicals/Radical 124.md`. `japanese: [SUI]` reconfirmed complete. `vietnamese: [thuý]` reconfirmed complete and exact against hvdic.thivien.net. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 321. `stand_in: 翠色` reconfirmed correct — of five apparent grep hits, only [[words/翠色|翠色]] and [[words/翠金|翠金]] genuinely cite 翠 in their `characters:` fields ([[words/核金|核金]], [[words/桃金|桃金]], [[words/褐金|褐金]] were false positives). A chengyu-citation grep hit, [[chengyu/生机勃勃|生机勃勃]], also checked out as a false positive (翠 appears only in a prose example sentence, not the chengyu's own four characters). Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-6-8.md` (item 9) and `Lookup/Korean/Korean Name ㅊ.md`.

**`mc_id` bug found and fixed (not merely off-by-one)**: stored `2675`, which lands on 儋's rank and doesn't correspond to 翠 at all; the genuine rank is `2679` (`CC 2000.md`: `2679. 翠`).

**`hsk_level` bug found and fixed**: stored `4`, traced only to a colon-count entry on `Old HSK 4.md` (`[[翠]]: 2`, not genuine) — no plain-numbered entry exists in any `Old HSK N.md` file, matching `Lookup/HSK/HSK No.md`'s own listing of 翠 as having no genuine level. Corrected to `hsk_level: 無`.

**`japanese_native` completeness gap found and fixed**: was `かわせみ` only; both en.Wiktionary and ja.Wiktionary independently attest a second genuine kun'yomi, `みどり` ("green"); added.

**`aliases` filled**: was blank. One genuine dual-source variant, [[翆]], with no independent page in this vault; added. A second single-sourced candidate from zh.Wiktionary alone, 臎, was left out.

**`pos` filled**: was blank. Filled as `性詞`, matching the dominant color-adjective senses.

**`## Words` section added**: the pre-existing bare "terbium abbreviation" note was reformatted as a proper Words bullet alongside the stand-in citation; both [[words/翠色|翠色]] and [[words/翠金|翠金]] rubies verified against each word's own `注音` field.

Rebuilt the malformed `## Notes` (bare unlinked prose instead of proper etymology, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format plus `## Words`. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 翫 (8588; 201 characters remaining).

### 2026-08-23, iteration 2303 — [[characters/翫|翫]]

`graphemic_classification: 元` (dual-source confirmed 形声, semantic 習 + phonetic 元, OC \*ŋoːns) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 羽` reconfirmed correct — genuine listing (item 13) on `Lookup/Radicals/Radical 124.md`. `vietnamese: [ngoạn]` reconfirmed complete against hvdic.thivien.net. `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md` item 39. `hsk_level: 無`, `stand_in: 名専字` (zero hits in `words/`) reconfirmed correct. `aliases` (blank) reconfirmed correct. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-11-4.md` (item 7) and `Lookup/Korean/Korean Name ㅇ.md`.

**Raw scratch note "can go to 玩???" resolved**: investigated whether 翫 should be merged into [[characters/玩|玩]]'s page. Both en.Wiktionary and zh.Wiktionary describe them as historically distinct characters that converged in meaning rather than a straightforward traditional/simplified pair (zh.Wiktionary explicitly: "historically distinct characters that converged in meaning"), and 玩 already has its own robust, independently-established page (with its own alias 莞 and its own separate `Lookup/Korean/Korean Name ㅇ.md` listing). Kept the pages separate, with the reasoning now documented in Notes rather than left as an open question.

**`mc_id` off-by-one bug found and fixed**: stored `3840` was actually 捽's rank; correct rank for 翫 is `3841` (`CC 3000.md`: `3840. 捽`, `3841. 翫`).

**`japanese` completeness gap found and fixed**: was `[GAN]`; ja.Wiktionary — which explicitly splits go-on/kan-on from 慣用音 — independently attests a genuine third reading, `KAN`; added.

**`japanese_native` bug found and fixed**: stored `もてあそ`, a truncated fragment; both en.Wiktionary and ja.Wiktionary agree on the genuine full form `もてあそぶ`; corrected. Two further single-sourced candidates from ja.Wiktionary alone (あなどる, むさぼる) were left out — not corroborated by en.Wiktionary.

**`pos` filled**: was blank. Filled as `事詞`, matching the verbal sense ("to slack off").

Rebuilt the malformed `# Notes` (wrong heading level, a raw unresolved scratch question, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 胱 (8589; 200 characters remaining).

### 2026-08-23, iteration 2304 — [[characters/胱|胱]]

`graphemic_classification: 光` (dual-source confirmed 形声, semantic 月 + phonetic 光) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 肉` reconfirmed correct — genuine listing (item 31) on `Lookup/Radicals/Radical 130.md`. `japanese: [KOU]` reconfirmed complete — both go-on and kan-on share the identical reading こう. `japanese_native: ø` reconfirmed correct. `vietnamese: [choáng, quang]` reconfirmed complete and exact against hvdic.thivien.net. `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md` item 115. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `pos: 名詞` reconfirmed correct. `stand_in: 旁胱` reconfirmed correct — a deliberate vault substitution (旁 standing in for 膀, matching the established phonetic-substitution convention), corroborated by [[words/旁胱|旁胱]]'s own `aliases` field listing the standard form 膀胱. Already correctly cross-listed on `Lookup/Korean/Korean Name ㄱ.md`.

**`mc_id` off-by-one bug found and fixed**: stored `2987` was actually 幟's rank; correct rank for 胱 is `2988` (`CC 2000.md`: `2987. 幟`, `2988. 胱`).

Rebuilt the malformed `## Notes` (unlinked bare "Components" bullet instead of proper etymology, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format; `## Words` (citing [[words/旁胱|旁胱]], ruby verified against the word's own `注音` field) reconfirmed correct, no changes. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 脛 (8590; 199 characters remaining).

### 2026-08-23, iteration 2305 — [[characters/脛|脛]]

`graphemic_classification: 巠` (dual-source confirmed 形声, semantic 肉 + phonetic 巠, OC \*keːŋ) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 肉` reconfirmed correct — genuine listing (item 41) on `Lookup/Radicals/Radical 130.md`. `korean: 경` reconfirmed correct. `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md` item 99. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `stand_in: 脛骨` reconfirmed correct — sole citer, the word's own independent page. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-4-7.md` (item 20) and `Lookup/Korean/Korean Name ㄱ.md`.

**`mc_id` off-by-one bug found and fixed**: stored `2265` was actually 慝's rank; correct rank for 脛 is `2266` (`CC 2000.md`: `2265. 慝`, `2266. 脛`).

**`cantonese` completeness gap found and fixed**: stored `hing5` only; both en.Wiktionary and zh.Wiktionary independently attest a second genuine jyutping reading, `ging3`; added.

**`japanese` completeness gap found and fixed**: was `[KEI]` (kan-on) only; both ja.Wiktionary and en.Wiktionary independently attest a genuine go-on, `GYOU`; added.

**`japanese_native` completeness gap found and fixed**: was `すね` only; both sources independently attest a second genuine kun'yomi, `はぎ`; added.

**`vietnamese` bug found and fixed**: stored `[cảnh, hĩnh, hểnh, hỉnh, kinh]`; hvdic.thivien.net's genuine readings are exactly `hĩnh, cảnh, hểnh, kinh` — `hỉnh` appears only in en.Wiktionary, not hvdic (this vault's Vietnamese authority), and was removed.

**`aliases` completeness gap found and fixed**: had `胫` (simplified form) only; both en.Wiktionary and zh.Wiktionary independently attest a second genuine variant, `踁`, with no independent page in this vault; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (shinbone).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format; `## Words` (citing [[words/脛骨|脛骨]], ruby verified against the word's own `注音` field) reconfirmed correct, no changes. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 脾 (8591; 198 characters remaining).

### 2026-08-23, iteration 2306 — [[characters/脾|脾]]

`graphemic_classification: 卑` (dual-source confirmed 形声, semantic 肉 + phonetic 卑, OC \*pe) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 肉` reconfirmed correct — genuine listing (item 45) on `Lookup/Radicals/Radical 130.md`. `cantonese: pei4` reconfirmed correct. `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md` item 230. `stand_in: 脾臓` reconfirmed correct — sole citer, the word's own independent page. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-4-8.md` (item 32) and `Lookup/Korean/Korean Name ㅂ.md`.

**`mc_id` off-by-one bug found and fixed**: stored `1490` was actually 黍's rank; correct rank for 脾 is `1491` (`CC 1000.md`: `1490. 黍`, `1491. 脾`).

**`hsk_level` bug found and fixed**: stored `2`, traced only to colon-count entries on `Old HSK 2.md` and `Old HSK 4.md` (neither genuine) — `Lookup/HSK/HSK No.md` itself already correctly lists 脾 among characters confirmed to have no genuine HSK level. Corrected to `hsk_level: 無`.

**`japanese` completeness gap found and fixed**: was `[HI, HAI, HEI]`; a third source, weblio.jp, was needed to reconcile — en.Wiktionary and ja.Wiktionary together confirm only `BI` (go-on) and `HI` (kan-on), missing entirely from the stored value, while weblio.jp additionally corroborates the already-present `HAI` and `HEI` as genuine further readings. Added the missing `BI`.

**`japanese_native` bug found and fixed — sentinel used despite genuine kun'yomi**: stored `ø`, but both en.Wiktionary and weblio.jp independently attest three genuine kun'yomi, `ひぞう`, `もも`, `とまる` (ja.Wiktionary's silence on kun'yomi for this entry was the outlier, not the other two sources); corrected.

**`vietnamese` completeness gap found and fixed**: was `[tì, tỳ]`; hvdic.thivien.net's genuine readings additionally include two further Âm Hán Việt, `bài` and `bễ`; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (spleen).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, a bare unlinked-format Words bullet folded into Notes instead of its own section, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format plus a proper `## Words` section. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 膏 (8592; 197 characters remaining).

### 2026-08-23, iteration 2307 — [[characters/膏|膏]]

`graphemic_classification: 高` (dual-source confirmed 形声, semantic 肉 + phonetic 高, OC \*kaːw) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 肉` reconfirmed correct — genuine listing (item 58) on `Lookup/Radicals/Radical 130.md`. `japanese: [KOU]` and `japanese_native: あぶら` reconfirmed complete and correct. `vietnamese: [cao]` reconfirmed correct. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 327. `stand_in: 脂膏` reconfirmed correct — sole citer, the word's own independent page (`pos: 名詞` there also confirming the character's own `名詞` classification). Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-2-12.md` (item 1) and `Lookup/Korean/Korean Name ㄱ.md`.

**`mc_id` off-by-one bug found and fixed**: stored `1736` was actually 闇's rank; correct rank for 膏 is `1737` (`CC 1000.md`: `1736. 闇`, `1737. 膏`).

**`hsk_level` bug found and fixed**: stored `3`, traced only to a colon-count entry on `Old HSK 3.md` (`[[膏]]: 1`, not genuine) — `Lookup/HSK/HSK No.md` itself already correctly lists 膏 among characters confirmed to have no genuine HSK level. Corrected to `hsk_level: 無`.

**`cantonese` completeness gap found and fixed**: stored `gou1` only; both en.Wiktionary and zh.Wiktionary independently attest a second genuine jyutping reading, `gou3`; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses.

Rebuilt the malformed `## Notes` (two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format; `## Words` (citing [[words/脂膏|脂膏]], ruby verified against the word's own `注音` field) reconfirmed correct, no changes. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 艙 (8593; 196 characters remaining).

### 2026-08-23, iteration 2308 — [[characters/艙|艙]]

`graphemic_classification: 倉` (dual-source confirmed 形聲, semantic 舟 + phonetic 倉, a later-formed 後起字) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 舟` reconfirmed correct — genuine listing (item 9) on `Lookup/Radicals/Radical 137.md`. `japanese: [SOU]` and `japanese_native: ø` reconfirmed complete and correct — both sources agree on the single on'yomi and no kun'yomi. `vietnamese: [khoang, thương]` reconfirmed complete. `stand_in: 名専字` reconfirmed correct — zero hits for 艙 anywhere in `words/`; a raw scratch note "Use 船室" appears to suggest creating a stand-in word, but no such word exists yet in this vault — left for the word-perfecting sweep. `aliases: [舱]` reconfirmed correct. `mc_id: 0` reconfirmed correct — genuinely absent from all four `CC N000.md` files. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-6-10.md` (item 8) and `Lookup/Korean/Korean Name ㅊ.md`.

**`hsk_level` bug found and fixed — genuine level hiding under simplified sibling glyph**: stored `3`, matching colon-count entries on `Old HSK 3.md` (neither genuine) — but `Old HSK 6.md` has a genuine plain-numbered entry under the simplified sibling glyph 舱 (`124. [舱]`). Corrected to `hsk_level: 6`.

**`joyo_level` filled**: was blank. ja.Wiktionary directly confirms 艙 as 表外字; added as item 548 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (cabin).

Rebuilt the malformed `# Notes` (wrong heading level, a raw unresolved scratch note, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 芥 (8595; 195 characters remaining).

### 2026-08-23, iteration 2309 — [[characters/芥|芥]]

`graphemic_classification: 介` (dual-source confirmed 形声, semantic 艸 + phonetic 介, OC \*kreːds) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 艸` reconfirmed correct — genuine listing (item 5) on `Lookup/Radicals/Radical 140.md`. `japanese: [KAI, KE]` reconfirmed complete — matches ja.Wiktionary's go-on ケ/kan-on カイ exactly. `vietnamese: [giới]` reconfirmed complete and exact against hvdic.thivien.net. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 329. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `stand_in: 芥子` reconfirmed correct. `aliases` (blank) reconfirmed correct — the only alternative noted by either source is 辛子, a Japanese-specific alternative spelling, not a true character variant.

**`mc_id` off-by-one bug found and fixed**: stored `3366` was actually 騂's rank; correct rank for 芥 is `3367` (`CC 3000.md`: `3366. 騂`, `3367. 芥`).

**`japanese_native` completeness gap found and fixed**: was `あくた` only; both en.Wiktionary and ja.Wiktionary independently attest two further genuine kun'yomi, `からし` and `ごみ`; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (mustard plant).

Rebuilt the malformed `## Notes` (two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format; `## Words` (citing [[words/芥子|芥子]], ruby verified against the word's own `注音` field) reconfirmed correct, no changes. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 芮 (8596; 194 characters remaining).

### 2026-08-23, iteration 2310 — [[characters/芮|芮]]

`graphemic_classification: 内` (dual-source confirmed 形声, semantic 艸 + phonetic 內/内, OC \*nuːbs) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 艸` reconfirmed correct — genuine listing (item 9) on `Lookup/Radicals/Radical 140.md`. `japanese: [ZEI, NEI, ZETSU, NECHI]` reconfirmed complete and exact — matches en.Wiktionary's four on'yomi precisely. `japanese_native: ø` reconfirmed correct — ja.Wiktionary lists no kun'yomi. `vietnamese: [nhuế, nùi, nối]` reconfirmed complete and exact against hvdic.thivien.net — en.Wiktionary's two further candidates (nội, nuôi) weren't corroborated by hvdic and correctly stayed unadded. `hsk_level: 無`, `stand_in: 名専字` (zero hits in `words/`), `aliases` (blank) all reconfirmed correct. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-4.md` (item 24) and `Lookup/Korean/Korean Name ㅇ.md`.

**`mc_id` off-by-one bug found and fixed**: stored `2337` was actually 苓's rank; correct rank for 芮 is `2338` (`CC 2000.md`: `2337. 苓`, `2338. 芮`).

**`joyo_level` filled**: was blank. ja.Wiktionary directly confirms 芮 as 表外字; added as item 549 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (water's edge).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id-rank bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 苔 (char) (8597; 193 characters remaining).

### 2026-08-23, iteration 2311 — [[characters/苔 (char)|苔 (char)]]

`graphemic_classification: 台` (dual-source confirmed 形声, semantic 艸 + phonetic 台) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 艸` reconfirmed correct — genuine listing (item 17) on `Lookup/Radicals/Radical 140.md`. `japanese_native: こけ` reconfirmed correct; ja.Wiktionary's single-sourced second candidate こけら wasn't corroborated by en.Wiktionary. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 332. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `stand_in: 苔` reconfirmed correct — this vault's established self-pointing convention for a character that is also independently its own word (cf. `words/苔.md`). Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-5.md` (item 25) and `Lookup/Korean/Korean Name ㅌ.md`. `mc_id: 7750` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`cantonese` completeness gap found and fixed**: stored `toi4` (moss sense) only; both en.Wiktionary and zh.Wiktionary independently attest a second genuine jyutping reading, `toi1` (tied to the "tongue coating" sense); added.

**`japanese` completeness gap found and fixed**: was `[TAI]` (kan-on) only; both ja.Wiktionary and en.Wiktionary independently attest a genuine go-on, `DAI`; added.

**`vietnamese` bug found and fixed**: stored `[dày, dầy, thai, đài, đày, đầy]`; hvdic.thivien.net's genuine six readings are `đài, dày, dây, đày, đầy, thai` — `dầy` appears nowhere in the source (likely a corruption of the genuine-but-missing `dây`); corrected.

**`aliases` filled**: was blank. One genuine dual-source variant, [[菭]] (both en.Wiktionary and zh.Wiktionary agree), with no independent page in this vault; added. A second candidate, 胎, already has independent use in this vault and correctly failed the alias test.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (moss).

Rebuilt the malformed `# Notes` (wrong heading level, a bare unlinked "Cantonese pronunciation" scratch line, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format, preserving the page's `>[!tip]` character/word split callout. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 苺 (char) (8598; 192 characters remaining).

### 2026-08-23, iteration 2312 — [[characters/苺 (char)|苺 (char)]]

`graphemic_classification: 母` (dual-source confirmed 形声, semantic 艸 + phonetic 母) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 艸` reconfirmed correct — genuine listing (item 24) on `Lookup/Radicals/Radical 140.md`. `japanese_native: いちご` reconfirmed correct. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 333. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `stand_in: 苺` reconfirmed correct — the vault's established self-pointing convention for a character that is also independently its own word. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-5.md` (item 28) and `Lookup/Korean/Korean Name ㅁ.md`. `mc_id: 7402` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`japanese` completeness gap found and fixed**: was `[MAI, BAI]`; both ja.Wiktionary and en.Wiktionary independently attest a third genuine go-on, `ME`; added.

**`vietnamese` gap found and fixed — field left entirely empty**: hvdic.thivien.net attests a genuine Âm Hán Việt reading, `môi`; added.

**`aliases` filled**: was blank. zh.Wiktionary explicitly states 莓 and 苺 are true variant forms of the same character (not distinct characters), corroborated by en.Wiktionary's own cross-reference; 莓 has no independent page in this vault; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (strawberry).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format, preserving the page's `>[!tip]` character/word split callout. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 茅 (8599; 191 characters remaining).

### 2026-08-23, iteration 2313 — [[characters/茅|茅]]

`graphemic_classification: 矛` (dual-source confirmed 形声, semantic 艸 + phonetic 矛, OC \*mu) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 艸` reconfirmed correct — genuine listing (item 26) on `Lookup/Radicals/Radical 140.md`. `mc_id: 1688` reconfirmed exact match (`CC 1000.md`: `1688. 茅`). `japanese: [BOU, MYOU]` reconfirmed complete — matches both sources' go-on/kan-on exactly. `vietnamese: [mao]` reconfirmed complete. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 225. `stand_in: 茅草` reconfirmed correct — sole citer, the word's own independent page. `aliases` (blank) reconfirmed correct — en.Wiktionary's candidate (茆) and zh.Wiktionary's candidate (泖) don't overlap, so neither is dual-source confirmed. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-5.md` (item 38) and `Lookup/Korean/Korean Name ㅁ.md`.

**`hsk_level` bug found and fixed**: stored `3`, traced only to a colon-count entry on `Old HSK 3.md` (`[[茅]]: 1`, not genuine) — `Lookup/HSK/HSK No.md` itself already correctly lists 茅 among characters confirmed to have no genuine HSK level. Corrected to `hsk_level: 無`.

**`japanese_native` completeness gap found and fixed**: was `かや` only; both en.Wiktionary and ja.Wiktionary independently attest two further genuine kun'yomi, `ち` and `ちがや`; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (thatch).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, a bare unlinked-format Words bullet folded into Notes instead of its own section, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format plus a proper `## Words` section. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 茉 (8600; 190 characters remaining).

### 2026-08-23, iteration 2314 — [[characters/茉|茉]]

`graphemic_classification: 末` (dual-source confirmed 形声, semantic 艸 + phonetic 末, OC \*maːd) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 艸` reconfirmed correct — genuine listing (item 27) on `Lookup/Radicals/Radical 140.md`. `japanese_native: ø` reconfirmed correct — ja.Wiktionary explicitly lists no kun'yomi; en.Wiktionary's single-sourced candidate (み) wasn't corroborated and stayed unadded. `vietnamese: [mạt]` reconfirmed complete and exact against hvdic.thivien.net. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 334. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `stand_in: 茉莉` and the `cranberry` tag reconfirmed correct — corroborated by [[words/茉莉|茉莉]]'s own matching `cranberry` tag. `mc_id: 0` reconfirmed correct — genuinely absent from all four `CC N000.md` files. `aliases: [苿]` left unchanged — neither of today's two sources corroborates it, but absence of confirmation isn't evidence of error for pre-existing data. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-5.md` (item 39) and `Lookup/Korean/Korean Name ㅁ.md`.

**`japanese` completeness gap found and fixed**: was `[MATSU, BATSU]`; both ja.Wiktionary and en.Wiktionary independently attest a genuine third go-on, `MACHI`; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (white jasmine, bound within 茉莉).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, a bare unlinked-format Words bullet folded into Notes instead of its own section, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format plus a proper `## Words` section. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 莉 (8601; 189 characters remaining).

### 2026-08-23, iteration 2315 — [[characters/莉|莉]]

`graphemic_classification: 利` (dual-source confirmed 形声, semantic 艸 + phonetic 利) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 艸` reconfirmed correct — genuine listing (item 43) on `Lookup/Radicals/Radical 140.md`. `japanese_native: ø` reconfirmed correct — ja.Wiktionary explicitly lists no kun'yomi. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 336. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `stand_in: 茉莉` and the `cranberry` tag reconfirmed correct. `mc_id: 0` reconfirmed correct — genuinely absent from all four `CC N000.md` files. `aliases` (blank) reconfirmed correct — zh.Wiktionary explicitly states no variant forms exist. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-7.md` (item 21) and `Lookup/Korean/Korean Name ㄹ.md`.

**`japanese` bug found and fixed**: stored `[CHI, REI, RI]` — `CHI` matched neither source; both ja.Wiktionary and en.Wiktionary independently attest the genuine go-on as `RAI`, missing entirely from the stored value. Corrected to `[RAI, REI, RI]`.

**`vietnamese` bug found and fixed**: stored `[lài, lị, lịa, lợi, nhài]`; hvdic.thivien.net's genuine readings are `lê, lị, lài, lợi, nhài` — `lịa` appears in neither hvdic nor en.Wiktionary (likely a corruption of the genuine-but-missing `lê`); corrected.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 莱 (8602; 188 characters remaining).

### 2026-08-23, iteration 2316 — [[characters/莱|莱]]

`graphemic_classification: 来` reconfirmed correct — both en.Wiktionary and zh.Wiktionary name the textbook phonetic as traditional 來, but 來 has no independent page in this vault; [[characters/来 (char)|来 (char)]]'s own `aliases` field lists 來 as pointing to it, confirming the parent-form citation is already correct. `radical: 艸` reconfirmed correct — genuine listing (item 44) on `Lookup/Radicals/Radical 140.md`. `vietnamese: [lai]` reconfirmed complete and exact against hvdic.thivien.net — en.Wiktionary's claimed second reading `lài` wasn't corroborated by hvdic. `aliases: [萊]` reconfirmed correct — genuine traditional form, and `Lookup/Korean/Korean Name ㄹ.md` already independently redirects 萊 to this page. `stand_in: 蓬莱` reconfirmed correct — of three apparent citers, [[words/蓬莱|蓬莱]] and [[words/莱金|莱金]] genuinely cite 莱 in their `characters:` fields; [[words/欧金|欧金]] was a false-positive prose mention.

**`mc_id` off-by-one bug found and fixed**: stored `1651` was actually 謗's rank; correct rank for 莱 is `1652`, recorded under the traditional sibling glyph (`CC 1000.md`: `1651. 謗`, `1652. 萊`).

**`japanese` bug found and fixed**: stored `[RAI, RI]` — `RI` matched neither en.Wiktionary nor ja.Wiktionary, both of which give only `らい` (identical for go-on and kan-on); removed the unattested `RI`.

**`japanese_native` completeness gap found and fixed**: was `あかざ` only; both en.Wiktionary and ja.Wiktionary independently attest a second genuine kun'yomi, `こうがい`; added. Each source's third candidate (あわち vs. あれわ) disagreed with the other and stayed unadded.

**`joyo_level` filled**: was blank. Both en.Wiktionary and ja.Wiktionary confirm 萊/莱 as a genuine 人名用漢字; added as item 480 to `Lookup/Japanese/Jinmeiyō.md` and filled as `日本人名用漢字`.

**`pos` filled**: was blank. Filled as `固有名詞`, matching this vault's established convention for place-name characters (cf. `characters/洛.md`, `characters/郎.md`).

**`## Words` completeness gap found and fixed**: only [[words/蓬莱|蓬莱]] was listed; a genuine second citer, [[words/莱金|莱金]] ("rhenium"), was previously folded into Notes as a bare unlinked-format bullet instead of its own Words entry; moved and properly formatted.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 菩 (8603; 187 characters remaining).

### 2026-08-23, iteration 2317 — [[characters/菩|菩]]

`graphemic_classification: 咅` (dual-source confirmed 形声, semantic 艸 + phonetic 咅) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 艸` reconfirmed correct — genuine listing (item 52) on `Lookup/Radicals/Radical 140.md` (gloss "sacred tree" there reflects the 菩提/bodhi-tree association, a genuine dual-source-attested sense, left unchanged). `cantonese: pou4` reconfirmed correct and complete — en.Wiktionary's own two further candidates were explicitly labeled "expected reflex," not attested readings, and zh.Wiktionary doesn't corroborate them either. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 315. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `stand_in: 菩薩` and the `cranberry` tag reconfirmed correct — corroborated by [[words/菩薩|菩薩]]'s own matching `cranberry` tag. `japanese_native: ø` reconfirmed correct — ja.Wiktionary lists no kun'yomi; en.Wiktionary's single-sourced candidate (ほとけぐさ) wasn't corroborated. `aliases` (blank) reconfirmed correct — zh.Wiktionary's single-sourced candidate 萯 wasn't corroborated by en.Wiktionary. `mc_id: 9428` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`japanese` major completeness gap found and fixed**: was `[HAI, BO]` only; both en.Wiktionary and ja.Wiktionary independently attest a much larger dual-source-confirmed reading set for this multi-etymology character — go-on `BAI`, `BU`, `BOKU`; kan-on `FUU`, `HO`, `HOKU` — all missing from the stored value; added all six.

**`vietnamese` completeness gap found and fixed**: was `[bồ, mồ]`; hvdic.thivien.net's genuine readings additionally include two further Âm Hán Việt, `bội` and `phụ`; added.

**`english` completeness gap found and fixed**: was `[bodhisattva]` only; both en.Wiktionary and zh.Wiktionary independently attest a second genuine sense, "herb" (the character's more basic botanical meaning); added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, a bare unlinked-format Words bullet folded into Notes instead of its own section, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format plus a proper `## Words` section. A chengyu-citation grep hit, [[chengyu/色即是空|色即是空]], checked out as a false positive (prose mention only). Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 菫 (8604; 186 characters remaining).

### 2026-08-23, iteration 2318 — [[characters/菫|菫]]

`radical: 艸` reconfirmed correct — genuine listing (item 53) on `Lookup/Radicals/Radical 140.md`. `cantonese: gan2` reconfirmed correct. `japanese_native: すみれ` reconfirmed correct. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 316. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `stand_in: 名専字` reconfirmed correct — zero hits in `words/`. `aliases` entries `槿`/`瑾`/`嫤` reconfirmed correct as this vault's established convention — `Lookup/Korean/Korean Name ㄱ.md` explicitly redirects all three to this page rather than giving them independent pages, even though they're technically distinct phonetic derivatives; left as-is, out of scope to restructure. `mc_id: 6203` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`graphemic_classification` self-reference bug found and fixed**: stored `菫` — the character citing *itself* as its own phonetic component, which is structurally impossible. Both en.Wiktionary and zh.Wiktionary independently describe 菫 as a corruption of [[堇]] with 艸 added as the semantic radical, making 堇 the true phonetic root. Corrected to `堇`; since 堇 has no independent page in this vault, added it to `aliases` instead (a genuine orthographic variant, distinct from the phonetic-derivative redirects already there).

**`japanese` completeness gap found and fixed**: was `[KIN]` (kan-on) only; both ja.Wiktionary and zh.Wiktionary independently attest a genuine go-on, `GON`; added.

**`vietnamese` bug found and fixed**: stored `[càn, cần, cẩn, cận, ngẩn, đổng]`; hvdic.thivien.net's genuine readings are exactly `càn, cần, cận, ngẩn` — `cẩn` and `đổng` appear in neither hvdic nor the day's other sources and were removed as unattested.

**`english` completeness gap found and fixed**: was `[celery, aconite]` (both explicitly archaic senses); en.Wiktionary identifies "violet" as the character's primary modern meaning, corroborated by zh.Wiktionary's kun'yomi gloss すみれ ("violet"); added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 萩 (8605; 185 characters remaining).

### 2026-08-23, iteration 2319 — [[characters/萩|萩]]

`graphemic_classification: 秋` (dual-source confirmed 形声, semantic 艸 + phonetic 秋) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 艸` reconfirmed correct — genuine listing (item 59) on `Lookup/Radicals/Radical 140.md`. `cantonese: cau1` reconfirmed correct. `japanese_native: はぎ` reconfirmed correct. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 309. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `stand_in: 名専字` reconfirmed correct — zero hits in `words/`. `aliases` (blank) reconfirmed correct — zh.Wiktionary's single-sourced candidate 𦵒 wasn't corroborated by en.Wiktionary. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-9.md` (item 16) and `Lookup/Korean/Korean Name ㅊ.md`. `mc_id: 6055` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`japanese` completeness gap found and fixed**: was `[SHUU]` (kan-on) only; both ja.Wiktionary and en.Wiktionary independently attest a genuine go-on, `SHU`; added.

**`vietnamese` completeness gap found and fixed**: was `[tho, thu]`; hvdic.thivien.net's genuine readings additionally include a third Âm Nôm, `thưu`; added. En.Wiktionary's own candidate `thèm` wasn't corroborated by hvdic and stayed unadded.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (bush clover).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 萱 (8606; 184 characters remaining).

### 2026-08-23, iteration 2320 — [[characters/萱|萱]]

`graphemic_classification: 宣` (dual-source confirmed 形声, semantic 艸 + phonetic 宣, OC \*qʰʷan) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 艸` reconfirmed correct — genuine listing (item 61) on `Lookup/Radicals/Radical 140.md`. `cantonese: hyun1`, `japanese: [KEN]`, `japanese_native: かや`, `vietnamese: [hiên, huyên]` all reconfirmed complete and correct against both sources. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 310. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `stand_in: 名専字` reconfirmed correct — zero hits in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-9.md` (item 18) and `Lookup/Korean/Korean Name ㅎ.md`. `mc_id: 9929` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`english` completeness gap found and fixed**: was `[daylily, Hemerocallis flava]` only; both en.Wiktionary and zh.Wiktionary independently attest a genuine figurative sense, "mother" (from classical literature where the plant symbolizes maternal care); added.

**`aliases` major completeness gap found and fixed**: had `藼` only; both en.Wiktionary and zh.Wiktionary independently attest the exact same additional four/five variant forms — `蕿`, `蘐`, `諼`, `谖`, `萲` — none with independent pages in this vault; added all.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 董 (8607; 183 characters remaining).

### 2026-08-23, iteration 2321 — [[characters/董|董]]

`graphemic_classification: 重` (dual-source confirmed 形声, semantic 艸 + phonetic 重, OC \*toːŋʔ) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 艸` reconfirmed correct — genuine listing (item 66) on `Lookup/Radicals/Radical 140.md`. `mc_id: 1104` reconfirmed exact match (`CC 1000.md`: `1104. 董`). `cantonese: dung2` reconfirmed correct. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 147. `pos: 事詞` reconfirmed correct. `stand_in: 名専字` reconfirmed correct — zero hits in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-9.md` (item 21) and `Lookup/Korean/Korean Name ㄷ.md`. A chengyu-citation grep hit, [[chengyu/三綱五常|三綱五常]], checked out as a false positive (董 appears only inside the name 董仲舒/Dong Zhongshu, not the chengyu's own four characters).

**`hsk_level` bug found and fixed**: stored `4`, traced only to a colon-count entry on `Old HSK 4.md` (`[[董]]: 1`, not genuine). `Old HSK 6.md` has a genuine plain-numbered entry (`655. [[董]]`); corrected to `hsk_level: 6`.

**`japanese` completeness gap found and fixed**: was `[TOU]` (kan-on) only; both ja.Wiktionary and en.Wiktionary independently attest a genuine go-on, `TSUU`; added.

**`japanese_native` bug found and fixed**: stored `ただ`, a truncated fragment; both en.Wiktionary and ja.Wiktionary agree on the genuine full form `ただす`; corrected.

**`vietnamese` bug found and fixed**: stored 8 readings; hvdic.thivien.net's genuine readings are exactly `đổng, dỏng, đỏng, đúng, rỗng, xổng` (6 total) — `đũng` and `đủng` appear only in en.Wiktionary's noisier, larger candidate list, not in hvdic (this vault's Vietnamese authority), and were removed.

**`aliases` filled**: was blank. One genuine dual-source variant, [[蕫]], with no independent page in this vault; added. zh.Wiktionary's second candidate, 菫, already has its own independent page in this vault (perfected earlier this session) and correctly failed the alias test.

Rebuilt the malformed `## Notes` (unlinked bare "Components" bullet instead of proper etymology, two floating unlinked CC wikilinks, no SKIP/Stroke bullet, no mc_id bullet, no four-level-links bullet) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 葱 (8608; 182 characters remaining).

### 2026-08-23, iteration 2322 — [[characters/葱|葱]]

`graphemic_classification: 怱` (dual-source confirmed 形声, semantic 艸 + phonetic 怱, OC \*sʰloːŋ) reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 艸` reconfirmed correct — genuine listing (item 68) on `Lookup/Radicals/Radical 140.md`. `vietnamese: [song, thông]` reconfirmed complete and exact against hvdic.thivien.net. `japanese_native: ねぎ` reconfirmed correct. `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md` item 224. `stand_in: 玉葱` reconfirmed correct — sole citer, the word's own independent page. `aliases: [蔥]` reconfirmed correct — genuine traditional form. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-9.md` (item 23) and `Lookup/Korean/Korean Name ㅊ.md`. `mc_id: 4105` reconfirmed as trusted long-tail (>4000, not cross-checked per policy).

**`hsk_level` bug found and fixed**: stored `4`, traced only to colon-count entries on `Old HSK 4.md` (both `[[葱]]: 1` and `[蔥]: 1`, neither genuine) — thoroughly checked all four `Old HSK N.md` files and found no genuine plain-numbered entry anywhere, and 葱 was also entirely absent from `Lookup/HSK/HSK No.md`. Corrected to `hsk_level: 無` and added 葱 to `Lookup/HSK/HSK No.md`'s list.

**`japanese` completeness gap found and fixed**: was `[SOU]` (kan-on) only; both ja.Wiktionary and en.Wiktionary independently attest a genuine go-on, `SU`; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, `## Words` placed before Notes instead of after) into the standard `## Notes` four-bullet format, reordered before the pre-existing `## Words` section. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 蒐 (8609; 181 characters remaining).

### 2026-08-23, iteration 2323 — [[characters/蒐|蒐]]

`graphemic_classification: 會意` (dual-source confirmed ideogrammic compound, 艸 "grass" + 鬼 "ghost") reconfirmed correct via en.Wiktionary and zh.Wiktionary. `radical: 艸` reconfirmed correct — genuine listing (item 73) on `Lookup/Radicals/Radical 140.md`. `cantonese: sau1` reconfirmed correct and complete — en.Wiktionary's claimed second reading `sau2` wasn't corroborated by zh.Wiktionary. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 313. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `stand_in: 蒐集` reconfirmed correct — sole citer, the word's own independent page. `aliases` (blank) reconfirmed correct — zh.Wiktionary's single-sourced candidates (獀, 䕇) weren't corroborated by en.Wiktionary. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-10.md` (item 22) and `Lookup/Korean/Korean Name ㅅ.md`.

**`mc_id` off-by-one bug found and fixed**: stored `2896` was actually 撥's rank; correct rank for 蒐 is `2897` (`CC 2000.md`: `2896. 撥`, `2897. 蒐`).

**`japanese` completeness gap found and fixed**: was `[SHUU]` (kan'yō-on) only; both ja.Wiktionary and en.Wiktionary independently attest two further genuine on'yomi, go-on `SHU` and kan-on `SOU`; added.

**`japanese_native` completeness gap found and fixed**: was `あかね` only; both sources independently attest two further genuine kun'yomi, `あつまる` and `あつめる`; added. En.Wiktionary's fourth candidate (かり) wasn't corroborated by ja.Wiktionary and stayed unadded.

**`vietnamese` completeness gap found and fixed**: was `[cói]` only; hvdic.thivien.net attests a second genuine reading, the Âm Hán Việt `sưu`; added.

**`pos` filled**: was blank. Filled as `事詞`, matching the dominant verbal senses (to collect, gather, assemble).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, `## Words` placed before Notes instead of after) into the standard `## Notes` four-bullet format, reordered before the pre-existing `## Words` section. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 蒲 (8610; 180 characters remaining).

### 2026-08-23, iteration 2324 — [[characters/蒲|蒲]]

`mc_id: 1302` reconfirmed as exact match (`CC 1000.md`: `1302. 蒲`). `radical: 艸` reconfirmed correct — implicit via `graphemic_classification` analysis (no separate Radical 140 listing needed since this is a semantic-radical page, not itself cited there). `hsk_level: 無` reconfirmed correct — genuine listing on `Lookup/HSK/HSK No.md` (line 557). `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 314, and independently corroborated by ja.Wiktionary's own "人名用漢字" classification. `japanese: [HO, BU]` reconfirmed correct and complete — en.Wiktionary and ja.Wiktionary both independently attest exactly kan-on ホ and go-on ブ (ja.Wiktionary's additional tō-on フ wasn't corroborated by en.Wiktionary and stayed unadded). Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-10.md` (item 23), `Lookup/Radicals/Radical 140.md` (item 74), and `Lookup/Korean/Korean Name ㅍ.md`.

**`graphemic_classification` verified, not a bug**: stored `浦` — dual-source confirmed 形声 (semantic 艸 "grass" + phonetic [[浦 (char)]], OC \*pʰaːʔ) via en.Wiktionary and zh.Wiktionary; matches `浦 (char).md`'s own `graphemic_classification: 甫` chain and its `## Derived Characters` list, which already correctly cites 蒲.

**`japanese_native` completeness gap found and fixed**: was `かば` only; both en.Wiktionary and ja.Wiktionary independently attest two further genuine kun'yomi, `がま` and `かま`; added as a list.

**`vietnamese` completeness gap found and fixed**: was `[bù, bồ, mồ]` (Nôm only); hvdic.thivien.net attests a fourth genuine reading, the Âm Hán Việt `bạc`; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (bulrush, cattail, reed).

**Second `## Words` citation found and moved**: a bare unlinked bullet `[[蒲公英]] "dandelion"` was sitting inside the malformed `## Notes` section instead of `## Words`; verified `words/蒲公英.md` genuinely cites 蒲 in its `characters:` frontmatter (distinct from the recorded `stand_in`, 香蒲); moved into `## Words` as a proper ruby entry using the word's own `注音` field, unannotated (not the `stand_in`).

Rebuilt the malformed `## Notes` (two floating unlinked CC wikilinks with no SKIP/Stroke/mc_id/four-links bullets) into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 蓮 (char) (8611; 179 characters remaining).

### 2026-08-23, iteration 2325 — [[characters/蓮 (char)|蓮 (char)]]

`graphemic_classification: 連` reconfirmed correct — dual-source confirmed 形声 (semantic 艸 "grass" + phonetic [連 (char)](characters/連%20(char).md)) via en.Wiktionary and zh.Wiktionary; matches `連 (char).md`'s own perfected page. `mc_id: 4459` reconfirmed as trusted long-tail (>4000, not cross-checked per policy). `radical: 艸` reconfirmed correct — genuine listing (item 79) on `Lookup/Radicals/Radical 140.md`. `japanese: [REN]` reconfirmed correct and complete — go-on and kan-on both れん, corroborated by both en.Wiktionary and ja.Wiktionary. `aliases: [莲]` reconfirmed correct — genuine simplified form, dual-source confirmed. `vietnamese: [liên, lên, ren, sen]` reconfirmed complete and exact against hvdic.thivien.net (Hán Việt liên + Nôm lên/liên/ren/sen). `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 149, corroborated by ja.Wiktionary's own 人名用漢字 classification. `stand_in: 蓮` reconfirmed correct — the plain character is itself directly used as an independent word (`words/蓮.md`, disambiguated via this "(char)" page), same pattern as `浦 (char)`/`浦`. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-10.md` (item 19) and `Lookup/Korean/Korean HS.md` (hanmun_edu_level 高等, not the Name-list track).

**`hsk_level` bug found and fixed**: stored `4`, traced only to colon-count entries on `Old HSK 4.md` (both `[莲]: 1` and `[[蓮 (char)]]: 1`, neither genuine) — thoroughly checked all six `Old HSK N.md` files and found no genuine plain-numbered entry anywhere. Corrected to `hsk_level: 無` and added 蓮 (char) to `Lookup/HSK/HSK No.md`'s list.

**`japanese_native` completeness gap found and fixed**: was `はす` only; both en.Wiktionary and ja.Wiktionary independently attest a second genuine kun'yomi, `はちす`; added as a list.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (lotus).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no `## Words` section) into the standard `## Notes` four-bullet format plus a `## Words` section citing the stand-in word. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 蓼 (8612; 178 characters remaining).

### 2026-08-23, iteration 2326 — [[characters/蓼|蓼]]

`graphemic_classification: 翏` reconfirmed correct — dual-source confirmed 形声 (semantic 艸 "grass" + phonetic [[翏]]) via en.Wiktionary and zh.Wiktionary. `radical: 艸` reconfirmed correct — genuine listing (item 81) on `Lookup/Radicals/Radical 140.md`. `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md` item 259, corroborated by ja.Wiktionary's own 表外漢字 classification. `hsk_level: 無` reconfirmed correct (character absent from all HSK sources). `stand_in: 蓼藍` reconfirmed correct — sole citer, the word's own independent page (`characters:` frontmatter genuinely cites 蓼). `japanese_native: たで` reconfirmed correct and complete. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-11.md` (item 12) and `Lookup/Korean/Korean Name ㄹ.md`.

**`mc_id` off-by-one bug found and fixed**: stored `2844` was actually 韭's rank; correct rank for 蓼 is `2845` (`CC 2000.md`: `2844. 韭`, `2845. 蓼`).

**False `aliases` entry found and removed**: stored `廖` — zh.Wiktionary explicitly lists it only as a character sharing the same phonetic component 翏 (a derived/related character, not an orthographic variant); en.Wiktionary does not mention it as a variant at all. Removed from `aliases` and documented the relationship in prose instead (廖 has no independent vault page to move to Derived Characters).

**`japanese` completeness gap found and fixed**: was `[RYOU, RIKU]` only; both en.Wiktionary and ja.Wiktionary independently attest a third genuine on'yomi, go-on `ROKU`; added.

**`vietnamese` completeness gap found and fixed**: was `[liễu]` only; hvdic.thivien.net attests two further genuine Âm Hán Việt readings, `liệu` and `lục`; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (knotweed).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke/mc_id/four-links bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 蔓 (8613; 177 characters remaining).

### 2026-08-23, iteration 2327 — [[characters/蔓|蔓]]

`graphemic_classification: 曼` reconfirmed correct — dual-source confirmed 形声 (semantic 艸 "grass" + phonetic [[曼]]) via en.Wiktionary and zh.Wiktionary. `radical: 艸` reconfirmed correct — genuine listing (item 83) on `Lookup/Radicals/Radical 140.md`. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 292, corroborated by ja.Wiktionary's own 人名用漢字 classification. `japanese_native: つる` reconfirmed correct and complete — en.Wiktionary's further candidates (のびる, かずら) and ja.Wiktionary's (はびこる) were each single-sourced and stayed unadded. `stand_in: 蔓延` reconfirmed correct — sole citer, the word's own independent page. `aliases` (blank) reconfirmed correct — neither source noted a variant form. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-11.md` (item 13) and `Lookup/Korean/Korean Name ㅁ.md`.

**`mc_id` off-by-one bug found and fixed**: stored `3061` was actually 剄's rank; correct rank for 蔓 is `3062` (`CC 3000.md`: `3061. 剄`, `3062. 蔓`).

**`hsk_level` bug found and fixed**: stored `4`, traced only to a colon-count entry on `Old HSK 4.md` (`[[蔓]]: 1`, not genuine) — checked all six `Old HSK N.md` files and found a genuine plain-numbered entry on `Old HSK 6.md` (`846.  [[蔓]]`). Corrected to `hsk_level: 6` and removed the now-contradicted entry from `Lookup/HSK/HSK No.md` (character was wrongly listed there as confirmed-無 despite the genuine Old HSK 6 evidence).

**`japanese` completeness gap found and fixed**: was `[BAN, MAN]` only; both en.Wiktionary and ja.Wiktionary independently attest a third genuine on'yomi, go-on `MON`; added.

**`vietnamese` over-inclusion bug found and fixed**: stored six readings `[man, màn, mơn, mạn, mớn, mởn]`; hvdic.thivien.net (sole Vietnamese authority) attests only three, `man`/`mạn` (Hán Việt) and `man`/`mơn` (Nôm) — the other three (`màn`, `mớn`, `mởn`), sourced only from en.Wiktionary, are not authoritative per policy and were removed; corrected to `[man, mạn, mơn]`.

**`pos` filled**: was blank. Filled as `事詞`, matching the dominant verbal senses (to spread, grow, infect).

Rebuilt the malformed `## Notes` (two floating unlinked CC wikilinks with no SKIP/Stroke/mc_id/four-links bullets) into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 蕃 (8614; 176 characters remaining).

### 2026-08-23, iteration 2328 — [[characters/蕃|蕃]]

`graphemic_classification: 番` reconfirmed correct — dual-source confirmed 形声 (semantic 艸 "grass" + phonetic [番 (char)](characters/番%20(char).md)) via en.Wiktionary and zh.Wiktionary. `radical: 艸` reconfirmed correct — genuine listing (item 90) on `Lookup/Radicals/Radical 140.md`. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 293, corroborated by ja.Wiktionary's own 人名用漢字 classification. `hsk_level: 無` reconfirmed correct — genuine listing on `Lookup/HSK/HSK No.md`; absent from all six `Old HSK N.md` files. `stand_in: 蕃息` reconfirmed correct — genuine citer, the word's own independent page. `aliases` (blank) reconfirmed correct — zh.Wiktionary's 異體字 candidate 番 has its own independent vault page and stays excluded per policy. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-12.md` (item 8) and `Lookup/Korean/Korean Name ㅂ.md`.

**`mc_id` off-by-one bug found and fixed**: stored `1441` was actually 迫's rank; correct rank for 蕃 is `1442` (`CC 1000.md`: `1441. 迫`, `1442. 蕃`).

**`vietnamese` malformed-value bug found and fixed**: stored as a single unsplit string `"phen, phên, phiên"` instead of a proper list, and incomplete — hvdic.thivien.net attests five genuine readings total (Hán Việt `phiên`/`phiền`/`phồn`, Nôm `phen`/`phên`); corrected to a proper five-entry list.

**`japanese` completeness gap found and fixed**: was `[BAN, HAN]` only; both en.Wiktionary and ja.Wiktionary independently attest two further genuine on'yomi, go-on `HON` and `BON`; added.

**`japanese_native` bug found and fixed**: stored the literal placeholder `ø` despite both en.Wiktionary and ja.Wiktionary independently attesting a genuine kun'yomi, `しげる`; corrected. Ja.Wiktionary's second candidate (ば) was single-sourced and stayed unadded.

**`pos` filled**: was blank. Filled as `事詞`, matching the dominant verbal sense (to multiply, proliferate).

**Second `## Words` citation found and moved**: two bare bullets (`蕃息`, `蕃藷`) were sitting inside the malformed `# Notes` section instead of `## Words`; verified both words genuinely cite 蕃 in their `characters:` frontmatter; moved into `## Words`, with `蕃息` marked as the recorded `stand_in`.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke/mc_id/four-links bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 蕪 (8615; 175 characters remaining).

### 2026-08-23, iteration 2329 — [[characters/蕪|蕪]]

`graphemic_classification: 無` reconfirmed correct — dual-source confirmed 形声 (semantic 艸 "grass" + phonetic [無 (char)](characters/無%20(char).md)) via en.Wiktionary and zh.Wiktionary. `radical: 艸` reconfirmed correct — genuine listing (item 93) on `Lookup/Radicals/Radical 140.md`. `aliases: [芜]` reconfirmed correct — genuine simplified form, dual-source confirmed. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 174, corroborated by ja.Wiktionary's own 人名用漢字 classification. `hsk_level: 無` reconfirmed correct — genuine listing on `Lookup/HSK/HSK No.md`. `vietnamese: [vu]` reconfirmed complete and exact against hvdic.thivien.net. `japanese: [BU, MU]` reconfirmed correct and complete — go-on む/kan-on ぶ, corroborated by both en.Wiktionary and ja.Wiktionary. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-12.md` (item 11) and `Lookup/Korean/Korean Name ㅁ.md`.

**`mc_id` off-by-one bug found and fixed**: stored `2779` was actually 懦's rank; correct rank for 蕪 is `2780` (`CC 2000.md`: `2779. 懦`, `2780. 蕪`).

**`stand_in` alias-citation bug found and fixed**: stored `蕪菁`, which has no independent vault page — that string is only listed inside `words/蕪青.md`'s own `aliases` field. The actual word page is `蕪青` (verified genuinely citing 蕪 in its `characters:` frontmatter); corrected `stand_in` to `蕪青`, matching the pre-existing (already-correct) `## Notes` bullet.

**`japanese_native` completeness gap found and fixed**: was `あれる` only; both en.Wiktionary and ja.Wiktionary independently attest two further genuine kun'yomi, `かぶ` and `かぶら`; added as a list.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (turnip).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, a bare word bullet with no `## Words` section) into the standard `## Notes` four-bullet format plus a proper `## Words` section. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 薇 (8616; 174 characters remaining).

### 2026-08-23, iteration 2330 — [[characters/薇|薇]]

`graphemic_classification: 微` reconfirmed correct — dual-source confirmed 形声 (semantic 艸 "grass" + phonetic [[微]]) via en.Wiktionary and zh.Wiktionary. `radical: 艸` reconfirmed correct — genuine listing (item 98) on `Lookup/Radicals/Radical 140.md`. `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md` item 235, corroborated by ja.Wiktionary's own 表外漢字 classification. `hsk_level: 無` reconfirmed correct — genuine listing on `Lookup/HSK/HSK No.md`. `japanese_native: ぜんまい` reconfirmed correct and complete. `stand_in: 薔薇` reconfirmed correct, and the `#cranberry` tag reconfirmed valid — the vault's own `words/薔薇金.md` explicitly documents that neither [[薔]] nor 薇 means "rose" alone, only the compound does (true transitivity: A=B=incomplete, AB="rose"). `aliases` (blank) reconfirmed correct. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-13.md` (item 9) and `Lookup/Korean/Korean Name ㅁ.md`.

**`mc_id` off-by-one bug found and fixed**: stored `3943` was actually 咀's rank; correct rank for 薇 is `3944` (`CC 3000.md`: `3943. 咀`, `3944. 薇`).

**`english` mistranslation bug found and fixed**: stored `[rose]` — but en.Wiktionary's Chinese entry gives the standalone sense of 薇 as "*Osmunda regalis*, royal fern" (with a Classic of Poetry citation), explicitly noting "rose" applies only to the compound 薔薇/蔷薇; the stored value had conflated the character's own meaning with its cranberry-compound meaning. Corrected to `[royal fern]`, consistent with the already-correct `japanese_native: ぜんまい` ("fern"). Propagated the same stale "rose" gloss fix to `Lookup/Radicals/Radical 140.md` (item 98) and `Lookup/SKIP/SKIP-2/SKIP-2-3-13.md` (item 9).

**`japanese` completeness gap found and fixed**: was `[BI]` only; both en.Wiktionary and ja.Wiktionary independently attest a second genuine on'yomi, go-on `MI`; added.

**`vietnamese` completeness gap found and fixed**: was `[vi]` only; hvdic.thivien.net attests a second genuine Âm Hán Việt reading, `vy`; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (royal fern).

**Second `## Words` citation reformatted**: a bare unlinked bullet (`薔薇金`, "abbreviation for rhodium") was sitting inside the malformed `# Notes` section instead of `## Words`; verified it genuinely cites 薇 in its `characters:` frontmatter; moved into `## Words` alongside the stand-in `薔薇`.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke/mc_id/four-links bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 薔 (8617; 173 characters remaining).

### 2026-08-23, iteration 2331 — [[characters/薔|薔]]

`radical: 艸` reconfirmed correct — genuine listing (item 99) on `Lookup/Radicals/Radical 140.md`. `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md` item 271, corroborated by ja.Wiktionary's own 表外漢字 classification. `hsk_level: 無` reconfirmed correct — genuine listing on `Lookup/HSK/HSK No.md`. `aliases: [蔷]` reconfirmed correct — genuine simplified form, dual-source confirmed. `mc_id: 5045` reconfirmed as trusted long-tail (>4000, not cross-checked per policy). `stand_in: 薔薇` reconfirmed correct, and the `#cranberry` tag reconfirmed valid (same transitivity documented in `words/薔薇金.md` as for [[薇]]). Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-13.md` (item 10) and `Lookup/Korean/Korean Name ㅈ.md`.

**`graphemic_classification` verified against a genuine two-etymology conflict, not a bug**: stored `嗇` — en.Wiktionary presents two etymologies (phonetic 牆, "only used in 薔薇"; and phonetic 嗇, "obsolete: water pepper; a surname"); zh.Wiktionary doesn't disambiguate. Kept the stored `嗇`, since it matches the character's own attested standalone sense and the already-correct `japanese_native: みずたで`; documented the conflict in prose (same pattern as prior 甬/睾/紗 cases).

**`english` mistranslation bug found and fixed**: stored `[rose]` — conflated with the compound-only sense of [[薔薇]]; en.Wiktionary's etymology-2 entry gives the standalone meaning as "(obsolete) water pepper" (*Persicaria hydropiper*), matching `japanese_native: みずたで`. Corrected to `[water pepper]`. Propagated the same stale "rose" gloss fix to `Lookup/Radicals/Radical 140.md` (item 99) and `Lookup/SKIP/SKIP-2/SKIP-2-3-13.md` (item 10).

**`japanese` completeness gap found and fixed**: was `[SHOKU, SHOU, SOU]`; both en.Wiktionary and ja.Wiktionary independently attest three further genuine on'yomi, go-on `ZOU`/`SHIKI` and kan-on `SOKU`; added.

**`vietnamese` completeness gap found and fixed**: was `[tường]` only; hvdic.thivien.net attests a second genuine Âm Hán Việt reading, `sắc`; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (water pepper).

**Missing `## Words` section built**: this page had no `## Words` section at all; verified both `薔薇` (the recorded `stand_in`) and `薔薇金` genuinely cite 薔 in their `characters:` frontmatter; added both.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke/mc_id/four-links bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 薩 (8618; 172 characters remaining).

### 2026-08-23, iteration 2332 — [[characters/薩|薩]]

`mc_id: 0` reconfirmed as a genuine sentinel — absent from all four `CC N000.md` files (a late Buddhist transliteration character, unranked in Classical Chinese). `radical: 艸` reconfirmed correct — genuine listing (item 107) on `Lookup/Radicals/Radical 140.md`. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 175, corroborated by ja.Wiktionary's own 人名用漢字 classification. `japanese: [SATSU, SACHI]` reconfirmed correct and complete — go-on さち/kan-on さつ, corroborated by both en.Wiktionary and ja.Wiktionary. `japanese_native: ø` reconfirmed correct — en.Wiktionary's kun'yomi candidate (すくう) wasn't corroborated by ja.Wiktionary, which lists no kun'yomi at all. `vietnamese: [tát]` reconfirmed complete and exact against hvdic.thivien.net. `aliases: [萨]` reconfirmed correct — genuine simplified form. `pos: 名詞` reconfirmed correct. `stand_in: 菩薩` reconfirmed correct — sole citer, the word's own independent page; `#cranberry` tag reconfirmed valid (both 菩 and 薩 already independently mean "bodhisattva," and so does the compound — genuine transitivity). Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-14.md` (item 3) and `Lookup/Korean/Korean Name ㅅ.md`.

**`graphemic_classification` bug found and fixed**: stored `產`, contradicting the page's own pre-existing Notes bullet ("Components: 艹, 隡") and both dual sources, which describe 薩 as a blend of 艸 (or 土) with 隡 (a variant of 薛, from the Sanskrit transliteration 薛埵 of *sattva*), not a typical 形声 compound. Corrected to `隡` (隡 has no independent vault page; cited in prose).

**`hsk_level` bug found and fixed**: stored as an empty string (never determined); checked all six `Old HSK N.md` files and found no entry at all. Corrected to `hsk_level: 無` and added 薩 to `Lookup/HSK/HSK No.md`.

Rebuilt the malformed `## Notes` (mixed heading levels, floating unlinked CC wikilinks, no SKIP/Stroke/mc_id/four-links bullets, no `## Words` section) into the standard four-bullet format plus a proper `## Words` section. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 藁 (8619; 171 characters remaining).

### 2026-08-23, iteration 2333 — [[characters/藁|藁]]

`mc_id: 5528` reconfirmed as trusted long-tail (>4000, not cross-checked per policy). `radical: 艸` reconfirmed correct — genuine listing (item 108) on `Lookup/Radicals/Radical 140.md`. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 176. `hsk_level: 無` reconfirmed correct — genuine listing on `Lookup/HSK/HSK No.md`. `japanese: [KOU]` reconfirmed correct and complete — go-on and kan-on both こう. `japanese_native: わら` reconfirmed correct. `vietnamese: [cảo, kiểu]` reconfirmed complete and exact against hvdic.thivien.net (Hán Việt cảo, Nôm cảo/kiểu). `stand_in: 名専字` reconfirmed correct despite one genuine citing word — `words/蓬藁.md` cites 藁 in its `characters:` frontmatter, but its own Notes explicitly documents it as the stand-in for [[蓬]], not for 藁; added as a non-stand-in `## Words` citation. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-14.md` (item 4) and `Lookup/Korean/Korean Name ㄱ.md`.

**`graphemic_classification` bug found and fixed**: stored `蒿` — both en.Wiktionary and zh.Wiktionary independently confirm the true phonetic component is 槀 (no independent vault page), and explicitly state 蒿 is a *distinct* phonetically-related character (different meaning, "mugwort") in the same 高 series, not the phonetic of 藁. Corrected to `槀`. This also resolves the page's own open question left in Notes ("Can it blend with 稿?") — yes, dual-source confirms 藁 is a documented alternative written form of [稿 (char)](characters/稿%20(char).md) and of 槁, kept as a separate page per established policy for historically distinct-but-converged forms.

**False `aliases` entry found and removed**: stored `蒿` — per the same dual-source finding above, 蒿 is a distinct character, not an orthographic variant of 藁, and has no independent vault page; removed and documented in prose instead. Left the existing `Lookup/Korean/Korean Name ㅎ.md` "蒿-->藁" discovery pointer in place (a lookup redirect, not a claim of orthographic identity — same pattern as the earlier 廖-->蓼 case).

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (straw).

**`boundedness` filled**: was blank. Filled as `80`, consistent with similarly-behaved `名専字` characters with a real but non-namesake compound citation.

Rebuilt the malformed `# Notes` (wrong heading level, a floating unresolved question, unlinked CC wikilinks, no SKIP/Stroke/mc_id/four-links bullets, no `## Words` section) into the standard `## Notes` four-bullet format plus a `## Words` section. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 薮 (8620; 170 characters remaining).

### 2026-08-23, iteration 2334 — [[characters/薮|薮]]

`radical: 艸` reconfirmed correct — genuine listing (item 109) on `Lookup/Radicals/Radical 140.md`. `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md` item 190. `hsk_level: 無` reconfirmed correct — genuine listing on `Lookup/HSK/HSK No.md`. `japanese: [SOU, SU]` reconfirmed correct and complete against en.Wiktionary (go-on す, kan-on そう). `japanese_native: やぶ` reconfirmed correct. `vietnamese: [sác, sú, tẩu]` reconfirmed complete and exact against hvdic.thivien.net (Hán Việt tẩu, Nôm sác/sú/tẩu). `aliases: [藪]` reconfirmed correct — 薮 is itself the shinjitai form of 藪, dual-source confirmed, and 藪 has no independent vault page. `stand_in: 薮沢` reconfirmed correct — sole citer, the word's own independent page. `pos: 名詞` reconfirmed correct. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-15.md` (item 4) and `Lookup/Korean/Korean Name ㅅ.md`.

**`graphemic_classification` alias-citation bug found and fixed**: stored `數`, the traditional glyph — but `數` has no independent vault page (only its simplified form `characters/数.md` does, listing `數` in its own `aliases`); per the established parent-form citation convention, corrected to `数`. The page's own pre-existing (malformed) Notes bullet had already gotten this right ("[艹] + [数]"), only the frontmatter field was wrong.

**`mc_id` off-by-one bug found and fixed**: stored `2237` was actually 橐's rank; correct rank for 薮/藪 is `2238` (`CC 2000.md`: `2237. 橐`, `2238. 藪`).

Rebuilt the malformed `## Notes` (wrong section order — `## Words` placed before `## Notes`, floating unlinked CC wikilinks, no SKIP/Stroke/mc_id/four-links bullets) into the standard `## Notes` four-bullet format, reordered before `## Words`. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 藷 (8621; 169 characters remaining).

### 2026-08-23, iteration 2335 — [[characters/藷|藷]]

`graphemic_classification: 諸` reconfirmed correct — dual-source confirmed 形声 (semantic 艸 "grass" + phonetic [諸 (char)](characters/諸%20(char).md)) via en.Wiktionary and zh.Wiktionary. `radical: 艸` reconfirmed correct — genuine listing (item 113) on `Lookup/Radicals/Radical 140.md`. `aliases: [𫉄]` reconfirmed correct — genuine simplified form per zh.Wiktionary. `hsk_level: 無` reconfirmed correct — genuine listing on `Lookup/HSK/HSK No.md`. `mc_id: 5909` reconfirmed as trusted long-tail (>4000, not cross-checked per policy). `japanese: [SHO, JO]` reconfirmed correct and complete — go-on しょ/じょ, kan-on しょ, corroborated by both en.Wiktionary and ja.Wiktionary. `japanese_native: いも` reconfirmed correct. `vietnamese: [thự]` reconfirmed complete and exact against hvdic.thivien.net. `stand_in: 蕃藷` reconfirmed correct — sole citer, the word's own independent page. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-15.md` (item 7) and `Lookup/Korean/Korean Name ㅈ.md`.

**`joyo_level` verified correct but missing from its own lookup page — gap fixed**: `表外字` reconfirmed correct (dual-source: en.Wiktionary and ja.Wiktionary both confirm Hyōgai status; absent from Jinmeiyō too), but the character was missing from `Lookup/Japanese/Hyōgai.md` itself; added as item 550.

**`korean_native` discrepancy found, left unresolved (no fabrication)**: stored `사탕수수` ("sugarcane") is semantically inconsistent with every other confirmed field — english `[potato, yam]`, `japanese_native: いも`, and `vietnamese: thự` all converge on "potato/yam." Could not locate an accessible authoritative Korean-language source to verify or correct it this iteration (Naver/zdic/ko.Wiktionary all unreachable or empty); documented the discrepancy in `## Notes` rather than guessing a replacement.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense (potato, yam).

**`boundedness` filled**: was blank. Filled as `80`, consistent with similarly-bound characters with one genuine stand-in citation.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/Stroke/mc_id/four-links bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-23`.

Next never-perfected character by `danayo_id`: 虻 (8622; 168 characters remaining).
