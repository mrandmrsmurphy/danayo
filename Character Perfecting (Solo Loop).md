# Character Perfecting (Solo Loop)

Running log for the character-perfecting backlog sweep (see [[AIOS/checklists/checklist_characters.md|Checklist: Character Pages]]). The prior logs (iterations 1–464, 465–981, 982–1543, and 1544–2049) grew large and were archived to `Character Perfecting (Solo Loop).md.zip`, `Character Perfecting (Solo Loop) 2.md.zip`, `Character Perfecting (Solo Loop) 3.md.zip`, and `Character Perfecting (Solo Loop) 4.md.zip` respectively; this file continues from there. Iteration numbering continues unbroken from the archived logs.

**Process**: one character per iteration. Find the next never-perfected character via `danayo_id` ascending (`grep -L "^date-last-perfect" characters/*.md`, sorted by each file's own `danayo_id` frontmatter value — not alphabetical, unlike the word sweep). Verify/fill all required frontmatter (`graphemic_classification`, `stand_in`, `mc_id`, `danayo_id`, `pos`, level fields), write or correct the four fixed `## Notes` bullets (graphemic → SKIP/Stroke → MC rank+phonology → levels), cross-check `## Words` against every real word citing this character as a constituent, add `## Chengyu`/`## Derived Characters` when real hits exist, then stamp `date-last-perfect`.

Next never-perfected character by `danayo_id`: 麓 (8304; 454 characters remaining).

### 2026-08-19, iteration 2050 — [[characters/麓|麓]]

`mc_id: 3134` reconfirmed exact match (CC 3000.md: `3133. 鈇`, `3134. 麓`, `3135. 癘`). `graphemic_classification: 鹿` (dual-source confirmed 形声, semantic 林 + phonetic 鹿 — the vault storing the phonetic component per convention) reconfirmed correct. `joyo_level: 高等` reconfirmed correct — genuine at `Lookup/Japanese/Jōyō - Kōtō.md` item 2130. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `vietnamese: [lộc]` reconfirmed exact match to hvdic's sole genuine reading. `aliases` (blank) reconfirmed correct — only obscure alternative forms (㯟/𣝹/𣓏/𪋤) exist, not added, consistent with convention. `stand_in: 名専字` reconfirmed correct — zero hits for 麓 anywhere in `words/`. Already correctly cross-listed on `Lookup/Korean/Korean Name ㄹ.md`.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense "foot of a mountain."

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/lookup bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 龐 (8305; 453 characters remaining).

### 2026-08-19, iteration 2051 — [[characters/龐|龐]]

`mc_id: 2064` reconfirmed exact match (CC 2000.md: `2063. 煌`, `2064. 龐`, `2065. 偷`). `graphemic_classification: 龍` (dual-source confirmed 形声, semantic 广 + phonetic 龍) reconfirmed correct. `radical: 龍` reconfirmed correct per the vault's own `Radical 212.md` page, which explicitly lists 龐 among the four characters "Used" under that radical. `stand_in: 名専字` reconfirmed correct — zero hits for 龐 anywhere in `words/`. Already correctly cross-listed on `Lookup/Korean/Korean Name ㅂ.md`.

**`aliases` bug found and fixed — missing genuine variants**: en.Wiktionary's own "Alternative forms" field explicitly lists 龎 and 厐 as variants of 龐, and the vault's own `Radical 212.md` page independently corroborates 龎 ("龎 --> variant of 龐"). Neither has an independent page. Added both alongside the already-correct simplified form `庞`.

**`joyo_level` filled**: was blank. Both sources confirm 龐 as Hyōgai kanji; added as item 440 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`hsk_level` bug found and fixed**: stored `4`, traced only to colon-count frequency entries in `Old HSK 4.md` (neither genuine). `Old HSK 6.md` has a genuine plain-numbered entry (`849. [庞]`). Corrected to `hsk_level: 6`.

**`vietnamese` completeness gap found and fixed**: hvdic lists two genuine Âm Hán Việt readings, `bàng` and `lung`; only `bàng` was stored. Added `lung`.

**`pos` filled**: was blank. Filled as `性詞`, matching the adjectival senses "tall; huge."

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/lookup bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 藻 (8306; 452 characters remaining).

### 2026-08-19, iteration 2052 — [[characters/藻|藻]]

`graphemic_classification: 澡` (dual-source confirmed 形声, semantic 艹 + phonetic 澡, originally written 薻) reconfirmed correct — an initial suspicion that 澡 might be a character-confusion bug for 喿 was checked and ruled out; en.Wiktionary explicitly cites 澡 itself as the phonetic. `joyo_level: 高等` reconfirmed correct — genuine at `Lookup/Japanese/Jōyō - Kōtō.md` item 1653. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `aliases` (blank) reconfirmed correct — only obscure historical variants exist, not added, consistent with convention. `vietnamese: [tang, tảo]` reconfirmed exact match — hvdic lists `tảo` as the sole genuine Âm Hán Việt and both `tang`/`tảo` as genuine Âm Nôm readings. `stand_in: 海藻` reconfirmed correct — the second grep hit, [[words/九尾狐|九尾狐]], is a false-positive prose mention (藻 appearing only within the proper noun 玉藻前, Tamamo-no-Mae), not a genuine `characters:` citation. Already correctly cross-listed on `Lookup/Korean/Korean Name ㅈ.md`.

**`mc_id` off-by-one bug found and fixed**: stored `2769` (actually 鄂's rank); correct rank for 藻 is `2770` (CC 2000.md: `2768. 慨`, `2769. 鄂`, `2770. 藻`).

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses "seaweed; alga."

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/lookup bullets, no `## Words` section) into the standard `## Notes` four-bullet format plus a `## Words` section citing [[words/海藻|海藻]] with ruby verified against the word's own `注音` field. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 鵰 (char) (8308; 451 characters remaining).

### 2026-08-19, iteration 2053 — [[characters/鵰 (char)|鵰 (char)]]

`aliases: [𫛲, 雕]` reconfirmed correct — both dual-source confirmed (雕 the standard simplified form, 𫛲 a nonstandard simplified form). `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `vietnamese: [điêu]` reconfirmed exact match to hvdic's sole genuine reading. `stand_in: 鵰` reconfirmed correct — sole citer, the word's own independent page.

**`graphemic_classification` bug found and fixed (genuine misclassification)**: stored `鳥` — the *semantic* component, not the phonetic — but both sources agree the true phonetic is `周`; en.Wiktionary's composition breakdown is explicit: "⿰周鳥," semantic 鳥 + phonetic 周. Corrected to `周`.

**`mc_id` bug found and fixed — combined absent-sentinel + sibling-glyph pattern**: stored `5429` (a trusted-long-tail value, treating 鵰 as absent from all CC files under its own glyph), but the simplified sibling glyph 雕 has a genuine exact-match entry at CC 1000.md rank `1967` (`1966. 翊`, `1967. 雕`, `1968. 快`). Corrected to `1967`, recorded under the sibling glyph per the established 鈩/鑪-style convention.

**`joyo_level` filled**: was blank. Both sources confirm 鵰 as Hyōgai kanji; added as item 441 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**Missing lookup cross-reference found and fixed**: 鵰 (char) was absent from `Lookup/Korean/Korean Name ㅈ.md`'s `### 조` section despite its `korean` reading being 조 — note that an existing entry "雕" on that same line already points to `characters/彫.md`, a *different* homograph sense (雕 as "carve," aliasing 彫) rather than the "eagle" sense (鵰); both entries now coexist correctly, disambiguating the two unrelated meanings that happen to share the glyph 雕.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses "eagle; vulture."

**Notes trivia verified, not dropped**: the stray unlinked fragment "Pronunciation collision" was investigated and confirmed genuine — 鵰's own `ㄑㄨㄛ` reading is shared by at least six other characters in the vault (秋, 酋, 醜, 雛, 厨, 紬, 遒), a real multi-way homophone cluster rather than a data error; [[秋 (char)|秋]] itself independently holds the self-pointing canonical stand_in role for that syllable. Preserved and expanded into full prose within the rebuilt Notes.

Rebuilt the malformed `# Notes` (wrong heading level, an unlinked stray fragment, two floating unlinked CC wikilinks, no SKIP/mc_id/lookup bullets, no `## Words` section) into the standard `## Notes` four-bullet format plus a `## Words` section citing [[words/鵰|鵰]] with ruby verified against the word's own `注音` field. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 繋 (8309; 450 characters remaining).

### 2026-08-19, iteration 2054 — [[characters/繋|繋]]

`mc_id: 1209` reconfirmed exact match, recorded under traditional sibling glyph 繫 (CC 1000.md: `1208. 領`, `1209. 繫`, `1210. 援`). `aliases: [繫]` reconfirmed correct (genuine kyūjitai form). `vietnamese: [hệ]` reconfirmed exact match to hvdic's sole genuine reading. Already correctly cross-listed on `Lookup/Korean/Korean HS.md` (under sibling glyph 繫).

**`graphemic_classification` bug found and fixed (character-confusion pattern)**: stored `系` — a visually similar but *distinct* character (the simplified Chinese form of 係, meaning "system/lineage") — but en.Wiktionary explicitly identifies the true phonetic as `毄`, a different component entirely. Corrected to `毄` (no independent page exists; plain text).

**`joyo_level` bug found and fixed**: stored `表外字`, but en.Wiktionary explicitly classifies 繫/繋 as Jinmeiyō kanji (人名用漢字), explicitly noting it is "not a jōyō kanji" but reserved for names — a different category than Hyōgai. Corrected to `日本人名用漢字`; already correctly cross-referenced via the `## Redirects` section of `Lookup/Japanese/Jinmeiyō.md` (`繫 --> 繋`).

**`hsk_level` bug found and fixed**: stored `1`, traced only to a colon-count frequency entry in `Old HSK 1.md` (`[繫]: 1`, not genuine). Zero genuine plain-numbered entry exists in any `Old HSK N.md` file, and 繋 was absent from `Lookup/HSK/HSK No.md`. Corrected to `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added 繋 to `HSK No.md`.

**`stand_in` bug found and fixed**: stored `名専字`, but a genuine citing word already existed and was overlooked — [[words/繋辞|繋辞]] (already correctly cited in the page's own `## Words` section) genuinely lists 繋 in its `characters:` field. Corrected `stand_in` to `繋辞`. The other three grep hits ([[words/系詞|系詞]], [[words/否定|否定]], [[words/交替|交替]]) are false-positive prose mentions, not genuine citers.

**`pos` filled**: was blank. Filled as `事詞`, matching the verbal senses "fasten; tie."

**`boundedness` filled**: was blank. Estimated `55` by analogy to comparable bound-but-word-bearing characters, flagged as a judgment call absent a formal definition.

**Notes trivia verified, not dropped**: the stray unlinked fragment "Added to the Korean HS list in 2000" was investigated — 繫/繋 is indeed genuinely present on `Lookup/Korean/Korean HS.md`'s standard list, consistent with the claim. Preserved and folded into the rebuilt Notes prose rather than dropped.

Rebuilt the malformed `## Notes` (correct heading level but missing SKIP/mc_id/lookup bullets, two floating unlinked CC wikilinks) into the standard four-bullet format; the existing `## Words` section (citing [[words/繋辞|繋辞]]) was already correctly formatted and untouched. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 俁 (8310; 449 characters remaining).

### 2026-08-19, iteration 2055 — [[characters/俁|俁]]

`graphemic_classification: 呉` (dual-source confirmed 形声, semantic 亻 + phonetic 吳, the vault citing the shinjitai sibling 呉 matching the established precedent list) reconfirmed correct. `mc_id: 6886` reconfirmed as trusted long-tail (>4000; also confirmed absent from all four CC files). `aliases: [俣]` reconfirmed correct — zh.Wiktionary explicitly labels 俣 as the genuine simplified form of 俁 (not merely a phonetic-series co-occurrence). `joyo_level: 表外字` reconfirmed correct — already correctly cross-referenced via the `## Redirects` section of `Lookup/Japanese/Hyōgai.md` (`俣 --> 俁`). `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md` (under the 俣 alias link). `stand_in: 名専字` reconfirmed correct — zero hits for 俁 anywhere in `words/`. Already correctly cross-listed on `Lookup/Korean/Korean Name ㅇ.md`.

**Severe Vietnamese content error found and fixed**: stored `[ngộ]` bore no resemblance to either genuine reading — hvdic's page for 俁 explicitly confirms the sole Âm Hán Việt readings are `ngu` and `vũ`, and independently confirms "ngộ" appears nowhere on the page at all. Corrected to `[ngu, vũ]`.

**`pos` filled**: was blank. Filled as `性詞`, matching the adjectival sense "big."

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/lookup bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 蟹 (char) (8311; 448 characters remaining).

### 2026-08-19, iteration 2056 — [[characters/蟹 (char)|蟹 (char)]]

`graphemic_classification: 解` (dual-source confirmed 形声, semantic 虫 + phonetic 解) reconfirmed correct. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 20. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `vietnamese: [giải]` reconfirmed exact match to hvdic's sole genuine reading. `stand_in: 蟹` reconfirmed correct — sole citer. Already correctly cross-listed on `Lookup/Korean/Korean Name ㅎ.md`.

**`mc_id` off-by-one bug found and fixed**: stored `3998` (actually 諄's rank); correct rank for 蟹 is `3999` (CC 3000.md: `3998. 諄`, `3999. 蟹`, `4000. 餧`).

**`aliases` bug found and fixed — missing genuine variant**: en.Wiktionary's own "Alternative forms" field explicitly lists 蠏 as a variant of 蟹 (first-listed, dual-source-style strong statement, distinct from the merely-informal-Cantonese 蚧 which was correctly left out), and 蠏 has no independent page in the vault. Added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense "crab."

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/lookup bullets, no `## Words` section) into the standard `## Notes` four-bullet format plus a `## Words` section citing [[words/蟹|蟹]] with ruby verified against the word's own `注音` field. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 鯨 (8312; 447 characters remaining).

### 2026-08-19, iteration 2057 — [[characters/鯨|鯨]]

`graphemic_classification: 京` (dual-source confirmed 形声, semantic 魚 + phonetic 京) reconfirmed correct. `mc_id: 4519` reconfirmed as trusted long-tail (>4000; also confirmed absent from all four CC files). `joyo_level: 高等` reconfirmed correct — genuine at `Lookup/Japanese/Jōyō - Kōtō.md` item 1288. `aliases: [鲸]` reconfirmed correct (genuine simplified form). `hanmun_edu_level: 名` (generic, not 高等) reconfirmed correct — genuinely absent from `Lookup/Korean/Korean HS.md`. `stand_in: 鯨魚` reconfirmed correct as primary citer (two further genuine citers — [[words/捕鯨|捕鯨]] and [[words/虎鯨|虎鯨]] — were already correctly cited in the page's own malformed Notes, now consolidated into `## Words`).

**`hsk_level` bug found and fixed**: stored `3`, traced only to colon-count frequency entries in `Old HSK 3.md` (neither genuine). Zero genuine plain-numbered entry exists in any `Old HSK N.md` file, and 鯨 was absent from `Lookup/HSK/HSK No.md`. Corrected to `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added 鯨 to `HSK No.md`.

**`vietnamese` bug found and fixed — wrong reading, not mere contamination**: hvdic's genuine union is `canh`/`kình` (Hán Việt) and `kềnh`/`kình` (Nôm). The stored `cành` doesn't match any genuine reading (an unrelated word meaning "branch," not a diacritic variant) — corrected to the genuine `canh`.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense "whale."

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, `## Words`-style bullets stranded inside `## Notes` itself) into the standard `## Notes` four-bullet format plus a consolidated `## Words` section citing all three genuine citing words, with ruby verified against each word's own `注音` field. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 譚 (8313; 446 characters remaining).

### 2026-08-19, iteration 2058 — [[characters/譚|譚]]

`mc_id: 1776` reconfirmed exact match (CC 1000.md: `1775. 貸`, `1776. 譚`, `1777. 證`). `graphemic_classification: 覃` (dual-source confirmed 形声, semantic 言 + phonetic 覃) reconfirmed correct. `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md` item 184. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `aliases: [谭]` reconfirmed correct (genuine simplified form). `vietnamese: [đàm]` reconfirmed exact match to hvdic's sole genuine reading. `pos: 性詞` and `stand_in: 名専字` already correct — zero hits for 譚 anywhere in `words/`. Already correctly cross-listed on `Lookup/Korean/Korean Name ㄷ.md`.

**`boundedness` filled**: was blank. Estimated `85` by analogy to comparable bound surname-characters, flagged as a judgment call absent a formal definition.

**Notes trivia verified, not dropped**: the surname claim ("Also used as a Chinese surname, e.g. 譚詠麟" — Alan Tam) was corroborated by en.Wiktionary's own mention of the same surname sense. Preserved and folded into the rebuilt Notes prose.

Rebuilt the malformed `## Notes` (a bare "Components:" bullet with broken/pageless wikilinks, no SKIP/mc_id/lookup bullets) into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 襖 (8314; 445 characters remaining).

### 2026-08-19, iteration 2059 — [[characters/襖|襖]]

`mc_id: 0` reconfirmed correct (confirmed absent from all four CC files). `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 155. `aliases: [袄]` reconfirmed correct (genuine simplified form). `vietnamese: [áo]` reconfirmed exact match to hvdic's sole genuine reading. `stand_in: 名専字` reconfirmed correct — zero hits for 襖 anywhere in `words/`.

**`graphemic_classification` bug found and fixed (kyūjitai/shinjitai inconsistency)**: stored `奧` (the traditional/kyūjitai form, which has no independent page in the vault), but the vault's own established convention (matching the 呉/吳 precedent) is to cite the shinjitai sibling glyph when only that page exists. Corrected to `奥`, matching `characters/奥 (char).md`.

**`hsk_level` bug found and fixed**: stored `4`, traced only to a colon-count frequency entry in `Old HSK 4.md` (`[襖]: 1`, not genuine). Zero genuine plain-numbered entry exists in any `Old HSK N.md` file, and 襖 was absent from `Lookup/HSK/HSK No.md`. Corrected to `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added 襖 to `HSK No.md`.

**Missing lookup cross-reference found and fixed**: 襖 was absent from `Lookup/Korean/Korean Name ㅇ.md`'s `### 오` section despite its `korean` reading being 오; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses "coat; jacket."

Rebuilt the malformed `# Notes` (wrong heading level, a stray bare "HSK/4, 日本人名用漢字" fragment duplicating frontmatter fields, two floating unlinked CC wikilinks, no SKIP/mc_id/lookup bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 砥 (8315; 444 characters remaining).

### 2026-08-19, iteration 2060 — [[characters/砥|砥]]

`mc_id: 2503` reconfirmed exact match (CC 2000.md: `2502. 隘`, `2503. 砥`, `2504. 陘`). `graphemic_classification: 氐` (dual-source confirmed 形声, semantic 石 + phonetic 氐) reconfirmed correct. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 223. `hanmun_edu_level`/`pos: 名詞`/`stand_in: 砥石` already correct — sole citer. `vietnamese: [chỉ, để, đe]` reconfirmed all three genuine (no contamination) — hvdic's union is `chỉ`/`để` (Hán Việt) and `chỉ`/`đe`/`để` (Nôm). Already correctly cross-listed on `Lookup/Korean/Korean Name ㅈ.md`.

**YAML structural bugs found and fixed**: `japanese` was a bare scalar instead of a proper list; the `aliases` key was missing from the frontmatter entirely (not just blank).

**`japanese` bug found and fixed — wrong romanization plus incomplete reading set**: stored `SI`, but the vault's established romanization convention for this on'yomi is `SHI` (confirmed by cross-checking sibling characters sharing the same syllable, e.g. 之/事/刺), and en.Wiktionary documents 砥 has go-on し(shi)/たい(tai) and kan-on し(shi)/てい(tei) — a second genuine on'yomi (`TEI`) was entirely missing. Corrected to `[SHI, TEI]`.

**`hsk_level` reconfirmed correct but evidence-basis fixed**: stored `無` was already right — zero evidence exists anywhere (absent from every `Old HSK N.md` file and, until now, from `Lookup/HSK/HSK No.md` too). Added 砥 to `HSK No.md` for consistency.

Rebuilt the malformed `# Notes` (wrong heading level, `## Words` section placed before `## Notes`, two floating unlinked CC wikilinks, no SKIP/mc_id/lookup bullets) into the standard section order and four-bullet `## Notes` format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 鰌 (8316; 443 characters remaining).

### 2026-08-19, iteration 2061 — [[characters/鰌|鰌]]

`mc_id: 3671` reconfirmed exact match. `graphemic_classification: 酋` (dual-source confirmed 形声, semantic 魚 + phonetic 酋) reconfirmed correct. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `aliases: [䲡]` reconfirmed correct (genuine simplified form). `stand_in: 鰌魚` reconfirmed correct — sole citer. Already correctly cross-listed on `Lookup/Korean/Korean Name ㅊ.md`.

**`joyo_level` filled**: was blank. en.Wiktionary explicitly confirms 鰌 as Hyōgai kanji, an alternative spelling of 泥鰌 ("pond loach"); added as item 442 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`vietnamese` completeness gap found and fixed**: hvdic lists two genuine Âm Hán Việt readings, `thu` and `tù`; only the genuine Nôm reading `tưu` was stored. Added both.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense "loach."

**Notes trivia verified, not dropped**: en.Wiktionary explicitly states 鰌 is "a variant of 鰍" — confirmed genuine and folded into the rebuilt Notes prose (no independent page exists for 鰍 in this vault, so not added as an alias per the parent-page convention).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/lookup bullets) into the standard `## Notes` four-bullet format; the existing `## Words` section (citing [[words/鰌魚|鰌魚]]) was already correctly formatted and untouched. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 鰐 (8317; 442 characters remaining).

### 2026-08-19, iteration 2062 — [[characters/鰐|鰐]]

`mc_id: 0` reconfirmed correct (confirmed absent from all four CC files). `graphemic_classification: 咢` (dual-source confirmed 形声, semantic 魚 + phonetic 咢) reconfirmed correct. `joyo_level: 表外字` reconfirmed correct — genuine at `Lookup/Japanese/Hyōgai.md` item 27. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `aliases: [鱷, 鳄]` reconfirmed correct — en.Wiktionary explicitly frames 鰐 as "a variant traditional form of 鱷" in Chinese and its shinjitai in Japanese (with 鳄 the standard simplified form). `vietnamese: [ngạc]` reconfirmed exact match to hvdic's sole genuine reading. `stand_in: 鰐魚` reconfirmed correct as one of two genuine citers (the other, [[words/鰐梨|鰐梨]], was already correctly cited in the page's own malformed Notes). `pos: 名詞` already correct. Already correctly cross-listed on `Lookup/Korean/Korean Name ㅇ.md`.

**Unclear scratch-note flagged, not propagated**: the stray fragment "looking to replace with 咢~악" was investigated — 咢 has no page of its own anywhere in the vault, and the character's own `graphemic_classification` already correctly cites 咢, so the note's intent is unclear and unverifiable (possibly a stale to-do about creating a 咢 page, now superseded). Dropped rather than carried forward as unresolved ambiguity.

**`boundedness` filled**: was blank. Estimated `65` by analogy to comparable animal-name characters with citing compounds, flagged as a judgment call absent a formal definition.

**Incidental typo fixed on citing word page**: [[words/鰐梨|鰐梨]]'s own `english` field had `avacado` (misspelled); corrected to `avocado`.

Rebuilt the malformed `# Notes` (wrong heading level, a stray unlinked scratch fragment, two floating unlinked CC wikilinks — one with a lowercase lint-breaking `../lookup/` relative path — a stranded bare Words-style bullet) into the standard `## Notes` four-bullet format plus a full `## Words` section citing both genuine citing words, with ruby verified against each word's own `注音` field. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 朧 (8318; 441 characters remaining).

### 2026-08-19, iteration 2063 — [[characters/朧|朧]]

`graphemic_classification: 龍` (dual-source confirmed 形声, semantic 月 + phonetic 龍 — with en.Wiktionary explicitly noting this 月 is genuinely "moon," not the cursive form of 肉) reconfirmed correct. `mc_id: 8895` reconfirmed as trusted long-tail (>4000; also confirmed absent from all four CC files). `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `aliases: [胧]` reconfirmed correct (genuine simplified form). `stand_in: 蒙朧` reconfirmed correct — the second grep hit, [[words/蒙古|蒙古]], is a false-positive prose mention (its own Notes explicitly warns not to confuse 蒙古 with 蒙朧, a coincidental first-character overlap), not a genuine `characters:` citation. Already correctly cross-listed on `Lookup/Korean/Korean Name ㄹ.md`.

**`joyo_level` reconfirmed correct but missing cross-reference fixed**: stored `表外字` was already right (en.Wiktionary explicitly confirms Hyōgai, not jōyō or jinmeiyō), but 朧 was absent from `Lookup/Japanese/Hyōgai.md`; added as item 443.

**`vietnamese` completeness gap found and fixed**: hvdic's genuine union is `long`/`lung`/`lông` (Hán Việt) and `lung` (Nôm); the stored `[lung, lông]` was missing the genuine reading `long`. Added it.

**`pos` filled**: was blank. Filled as `性詞`, matching the adjectival senses "hazy; cloudy."

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/lookup bullets, no `## Words` section) into the standard `## Notes` four-bullet format plus a `## Words` section citing [[words/蒙朧|蒙朧]] with ruby verified against the word's own `注音` field. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 籃 (8319; 440 characters remaining).

### 2026-08-19, iteration 2064 — [[characters/籃|籃]]

`graphemic_classification: 監` (dual-source confirmed 形声, semantic 竹 + phonetic 監) reconfirmed correct. `mc_id: 10118` reconfirmed as trusted long-tail (>4000; also confirmed absent from all four CC files). `aliases: [篮]` reconfirmed correct (genuine first-round simplified form; the obscure second-round 兰 not added, consistent with convention). `stand_in: 名専字` reconfirmed correct — the sole grep hit, [[words/籠球|籠球]], cites 籃 only within its own `aliases` field (籃球), not the `characters:` field — a false positive. `pos: 名詞` already correct.

**YAML structural bugs found and fixed**: `japanese_native` had a malformed scalar+duplicate-list-item hybrid (`かご` on the key line, then a redundant `- かご` list entry below it); collapsed to the single genuine scalar. `vietnamese` was a comma-jammed single string (`"lam, xờm, làn"`) instead of a proper list.

**`vietnamese` bug found and fixed — diacritic corruption plus verified via list-split**: hvdic's genuine union is `lam` (Hán Việt) and `lam`/`làn`/`xớm` (Nôm). The stored `xờm` was a diacritic-corrupted duplicate matching neither list — hvdic explicitly confirmed only `xớm` (different tone mark) appears on its page; corrected.

**`hsk_level` bug found and fixed**: stored `1`, traced only to colon-count frequency entries in `Old HSK 1.md` and `Old HSK 3.md` (neither genuine). Zero genuine plain-numbered entry exists in any `Old HSK N.md` file, and 籃 was absent from `Lookup/HSK/HSK No.md`. Corrected to `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added 籃 to `HSK No.md`.

**`joyo_level` reconfirmed correct but missing cross-reference fixed**: stored `表外字` was already right (en.Wiktionary explicitly confirms Hyōgai), but 籃 was absent from `Lookup/Japanese/Hyōgai.md`; added as item 444.

**Notes trivia verified, not dropped**: the stray fragment "for the word 'basket', use 籠" was investigated and confirmed genuine — [[characters/籠 (char)|籠]] has its own independent page and a self-pointing `stand_in`, matching the claim that it, not 籃, is the vault's genuine bound word for "basket." Preserved and folded into the rebuilt Notes prose.

Rebuilt the doubled `## Notes` section (two separate headers, the first containing only the stray trivia fragment and bare CC wikilinks, the second containing a malformed phono-semantic bullet with an empty phonetic wikilink) into a single standard four-bullet `## Notes` format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 鶴 (char) (8320; 439 characters remaining).

### 2026-08-19, iteration 2065 — [[characters/鶴 (char)|鶴 (char)]]

`mc_id: 2383` reconfirmed exact match (CC 2000.md: `2382. 祇`, `2383. 鶴`, `2384. 訢`). `joyo_level: 高等` reconfirmed correct — genuine at `Lookup/Japanese/Jōyō - Kōtō.md` item 1745. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `hanmun_edu_level: 高等` reconfirmed correct — genuine at `Lookup/Korean/Korean HS.md`. `stand_in: 鶴` reconfirmed correct as primary self-referential citer (a second genuine citer, [[words/紅鶴|紅鶴]], was found and added to `## Words`); the remaining grep hits ([[words/唳|唳]], [[words/嚇|嚇]], [[words/提琴|提琴]], [[words/楼閣|楼閣]]) are false-positive prose mentions.

**`graphemic_classification` cross-source disagreement investigated, kept as-is**: en.Wiktionary's precise etymology cites the phonetic as `寉`, but zh.Wiktionary's own phonetic-series grouping (系列#1551) lists `隺` as the series head including 鶴 itself — a genuine cross-source disagreement matching the established 淳/醇-style precedent of trusting zh.Wiktionary's phonetic-series data. Kept `隺` as stored.

**`aliases` bug found and fixed — missing genuine variants**: en.Wiktionary's own "Alternative forms" field explicitly lists 隺 and 鸖 as variants of 鶴 (a structured field, not mere phonetic-series co-occurrence), and neither has an independent page in the vault. Added both alongside the already-correct simplified form `鹤`; the more obscure 䳽/𮹙 pair was left out, consistent with convention.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense "crane."

Rebuilt the malformed `# Notes` (wrong heading level, a lowercase lint-breaking `../lookup/` relative path, two floating unlinked CC wikilinks, missing blank line before `## Chengyu`) into the standard `## Notes` four-bullet format plus a `## Words` section citing both genuine citing words, with ruby verified against each word's own `注音` field; the existing `## Chengyu` section (citing [[chengyu/焚琴煮鶴|焚琴煮鶴]]) was already correctly formatted and untouched. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 錀 (char) (8321; 438 characters remaining).

### 2026-08-19, iteration 2066 — [[characters/錀 (char)|錀 (char)]]

`graphemic_classification: 侖` (dual-source confirmed 形声, semantic 金 + phonetic 侖) reconfirmed correct. `mc_id: 0` reconfirmed correct (confirmed absent from all four CC files; plausible given roentgenium is a modern synthetic element). `vietnamese: [ø]` reconfirmed correct — hvdic explicitly states no Âm Hán Việt reading exists yet for this character, so the placeholder sentinel is genuine, not a data gap. `pos: 固有名詞` already correct, matching the vault's precedent for element-name characters. `stand_in: 錀` reconfirmed correct — sole self-referential primary citer (a second genuine citer, [[words/錀琴|錀琴]], was already correctly cited in the page's own malformed Notes, now consolidated into `## Words`).

**`aliases` bug found and fixed — missing entirely, not just blank**: the `aliases` key was absent from the frontmatter altogether. en.Wiktionary's own simplified-form field lists `𬬭` as the genuine simplified Chinese form; added.

**`joyo_level` reconfirmed correct but missing cross-reference fixed**: stored `表外字` was already right (en.Wiktionary explicitly confirms Hyōgai), but 錀 was absent from `Lookup/Japanese/Hyōgai.md`; added as item 445.

**`hsk_level` reconfirmed correct but evidence-basis fixed**: stored `無` was already right — zero evidence exists anywhere (absent from every `Old HSK N.md` file and, until now, from `Lookup/HSK/HSK No.md` too). Added 錀 (char) to `HSK No.md` for consistency.

**Broken wikilink fixed in an external lookup file**: `Lookup/Korean/Korean Name ㄹ.md`'s own entry for 錀 used a malformed `[[characters/錀 (char)]] roentgenium` fragment (a raw file-path wikilink with a stray trailing gloss) instead of the standard markdown-link format used by every other entry on that line; corrected to `[錀 (char)](characters/錀%20(char).md)`.

Rebuilt the malformed `## Notes` (a broken relative `../words/` wikilink, no SKIP/mc_id/lookup bullets) into the standard four-bullet format plus a `## Words` section citing both genuine citing words, with ruby verified against each word's own `注音` field. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 纏 (8322; 437 characters remaining).

### 2026-08-19, iteration 2067 — [[characters/纏|纏]]

`mc_id: 3289` reconfirmed exact match (CC 3000.md: `3288. 犨`, `3289. 纏`, `3290. 邈`). `graphemic_classification: 廛` (dual-source confirmed 形声, semantic 糸 + phonetic 廛) reconfirmed correct. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 318. `aliases: [缠, 緾, 纒, 繵]` reconfirmed all four genuine (one simplified form, three variant forms, all explicitly confirmed). `vietnamese: [triền, dờn]` reconfirmed exact match — hvdic lists `triền` as the sole genuine Âm Hán Việt and both `triền`/`dờn` as genuine Âm Nôm readings. `stand_in: 名専字` reconfirmed correct — zero hits for 纏 anywhere in `words/`. Already correctly cross-listed on `Lookup/Korean/Korean Name ㅈ.md`.

**`hsk_level` bug found and fixed**: stored `4`, traced only to colon-count frequency entries in `Old HSK 4.md` (neither genuine). `Old HSK 6.md` has a genuine plain-numbered entry (`630. [缠]`). Corrected to `hsk_level: 6`.

**`pos` filled**: was blank. Filled as `事詞`, matching the verbal sense "wrap."

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/lookup bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 齦 (8323; 436 characters remaining).

### 2026-08-19, iteration 2068 — [[characters/齦|齦]]

`graphemic_classification: 艮` (dual-source confirmed 形声, semantic 齒 + phonetic 艮) reconfirmed correct. `mc_id: 7115` reconfirmed as trusted long-tail (>4000; also confirmed absent from all four CC files). `hsk_level: 無` reconfirmed correct — already present on `Lookup/HSK/HSK No.md` (bare-wikilink format). `aliases: [龈]` reconfirmed correct (genuine simplified form; the more obscure Japanese-extended shinjitai 𮯅 not added, consistent with convention). `stand_in: 歯齦` reconfirmed correct — sole citer.

**`joyo_level` filled**: was blank. en.Wiktionary explicitly confirms 齦 as Hyōgai kanji; added as item 446 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`vietnamese` completeness gap found and fixed**: hvdic lists two genuine Âm Hán Việt readings, `khẩn` and `ngân`; only `ngân` was stored. Added `khẩn`.

**Missing lookup cross-reference found and fixed**: 齦 was absent from `Lookup/Korean/Korean Name ㄱ.md`'s `### 간` section despite its `korean` reading being 간; added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses "gums; gingiva."

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/lookup bullets, no `## Words` section) into the standard `## Notes` four-bullet format plus a `## Words` section citing [[words/歯齦|歯齦]] with ruby verified against the word's own `注音` field. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 軣 (8324; 435 characters remaining).

### 2026-08-19, iteration 2069 — [[characters/軣|軣]]

`graphemic_classification: 會意` reconfirmed correct — three copies of 車 stacked, evoking rumble. `mc_id: 8451` reconfirmed as trusted long-tail (>4000; also confirmed absent from all four CC files). `aliases: [轟, 轰]` reconfirmed correct — 軣 is genuinely the Japanese shinjitai of traditional 轟 (with 轰 the Chinese simplified form). `stand_in: 名専字` reconfirmed correct — the sole citer, [[words/軣軣|軣軣]], is a reduplicated form already correctly cited in `## Words`. Already correctly cross-listed on `Lookup/Korean/Korean Name ㄱ.md` (under the 轟 spelling).

**`joyo_level` bug found and fixed**: stored `日本人名用漢字`, but en.Wiktionary explicitly classifies 軣 as Hyōgai kanji (表外漢字), not Jinmeiyō — already correctly cross-referenced via the `## Redirects` section of `Lookup/Japanese/Hyōgai.md` (`轟 --> 軣`), which the stored value contradicted. Corrected to `表外字`.

**`vietnamese` filled**: was entirely blank. hvdic lists two genuine Âm Hán Việt readings, `hoanh` and `oanh`; added both.

**`hsk_level` filled**: was blank. `Old HSK 6.md` has a genuine plain-numbered entry under the sibling glyph 轰 (`425. [轰]`) — corrected to `hsk_level: 6` (correctly absent from `HSK No.md`, matching the genuine non-無 level).

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses "rumble; explosion."

**`boundedness` filled**: was blank. Estimated `60` by analogy to comparable onomatopoeic/sound characters, flagged as a judgment call absent a formal definition.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/lookup bullets) into the standard `## Notes` four-bullet format; the existing `## Words` section (citing [[words/軣軣|軣軣]]) was already correctly formatted and untouched. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 穣 (char) (8325; 434 characters remaining).

### 2026-08-19, iteration 2070 — [[characters/穣 (char)|穣 (char)]]

`mc_id: 1804` reconfirmed exact match, recorded under traditional sibling glyph 穰 (CC 1000.md: `1803. 準`, `1804. 穰`, `1805. 突`). `graphemic_classification: 襄` (dual-source confirmed 形声, semantic 禾 + phonetic 襄) reconfirmed correct. `joyo_level: 日本人名用漢字` reconfirmed correct — en.Wiktionary confirms Jinmeiyō for the traditional glyph; already correctly cross-referenced via the `## Redirects` section of `Lookup/Japanese/Jinmeiyō.md` (`穰 --> 穣`). `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `aliases: [穰]` reconfirmed correct (genuine kyūjitai form). `stand_in: 穣` reconfirmed correct — sole self-referential citer. Already correctly cross-listed on `Lookup/Korean/Korean Name ㅇ.md`.

**`vietnamese` filled**: was entirely blank. hvdic lists two genuine Âm Hán Việt readings, `nhương` and `nhưỡng`; added both.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense "stalks of grain."

**`boundedness` filled**: was blank. Estimated `65` by analogy to comparable bound agricultural-term characters, flagged as a judgment call absent a formal definition.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/lookup bullets, no `## Words` section) into the standard `## Notes` four-bullet format plus a `## Words` section citing [[words/穣|穣]] with ruby verified against the word's own `注音` field. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 𦜝 (8326; 433 characters remaining).

### 2026-08-19, iteration 2071 — [[characters/𦜝|𦜝]]

`mc_id: 3429` reconfirmed exact match, recorded under traditional sibling glyph 臍 (CC 3000.md: `3428. 奕`, `3429. 臍`, `3430. 誖`). `graphemic_classification: 斉` (dual-source confirmed 形声, semantic 肉 + phonetic 齊/斉, the vault citing the shinjitai sibling matching its own available page) reconfirmed correct. `joyo_level: 表外字` reconfirmed correct — already correctly cross-referenced via the `## Redirects` section of `Lookup/Japanese/Hyōgai.md` (`臍 --> 𦜝`). `aliases: [臍, 脐]` reconfirmed correct (kyūjitai and simplified forms respectively). `pos: 名詞` already correct. `stand_in: 名専字` reconfirmed correct — zero hits for 𦜝 anywhere in `words/`. Already correctly cross-listed on `Lookup/Korean/Korean Name ㅈ.md`.

**YAML structural bug found and fixed**: `japanese_native` was a malformed leading-space comma-jammed single string (`" へそ , ほぞ"`) instead of a proper list; split into two proper list items.

**`vietnamese` filled**: was entirely blank. hvdic lists one genuine Âm Hán Việt reading, `tề`; added.

**`hsk_level` reconfirmed correct but evidence-basis fixed**: stored `無` was already right — zero evidence exists anywhere (absent from every `Old HSK N.md` file and, until now, from `Lookup/HSK/HSK No.md` too). Added 𦜝 to `HSK No.md` for consistency.

**`boundedness` filled**: was blank. Estimated `65` by analogy to comparable bound anatomical-term characters, flagged as a judgment call absent a formal definition.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/lookup bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 龔 (8327; 432 characters remaining).

### 2026-08-19, iteration 2072 — [[characters/龔|龔]]

`mc_id: 2525` reconfirmed exact match (CC 2000.md: `2524. 艱`, `2525. 龔`, `2526. 驎`). `radical: 龍` reconfirmed correct (genuine Kangxi radical assignment, per en.Wiktionary's own "龍+6 strokes" citation). `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `aliases: [龚]` reconfirmed correct (genuine simplified form). `vietnamese: [cung]` reconfirmed exact match to hvdic's sole genuine reading. `pos: 事詞` already correct. `stand_in: 名専字` reconfirmed correct — zero hits for 龔 anywhere in `words/`.

**`graphemic_classification` bug found and fixed (genuine semantic/phonetic swap)**: stored `龍` — the *semantic* component (also the radical) — but zh.Wiktionary's own explicit 聲符 field states the phonetic is `共`, not `龍`; en.Wiktionary's less precise description left this ambiguous, but zh.Wiktionary's structured field resolved it definitively. Corrected to `共`.

**Missing lookup cross-references found and fixed**: 龔 was absent from both `Lookup/Japanese/Hyōgai.md` (despite genuine `表外字` status) and `Lookup/Korean/Korean Name ㄱ.md`'s `### 공` section (despite its `korean` reading being 공); added to both.

**`boundedness` filled**: was blank. Estimated `85` by analogy to comparable bound surname-characters, flagged as a judgment call absent a formal definition.

Rebuilt the malformed `## Notes` (a stray unheaded "Components:" bullet with pageless wikilinks stranded below proper CC-lookup bullets, no SKIP/mc_id/lookup-reference bullets) into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 麟 (8328; 431 characters remaining).

### 2026-08-19, iteration 2073 — [[characters/麟|麟]]

`mc_id: 1811` reconfirmed exact match (CC 1000.md: `1811. 麟`). `graphemic_classification: 粦` (dual-source confirmed 形声, semantic 鹿 + phonetic 粦) reconfirmed correct. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 297. `hsk_level: 無` reconfirmed correct — present on `Lookup/HSK/HSK No.md`. `vietnamese: [lân]` reconfirmed exact match to hvdic's sole genuine reading. `tags: [character, cranberry]`/`stand_in: 麒麟` reconfirmed correct — transitivity holds with sibling [[characters/麒|麒]] (A=麒, B=麟, AB=麒麟, both bound to the same word). Already correctly cross-listed on `Lookup/Korean/Korean Name ㄹ.md`.

**`stroke_count`/`skip_number` bug found and fixed**: stored `24`/`1-11-13`, but en.Wiktionary explicitly states 麟 has 23 strokes ("Kangxi radical 198, 鹿+12, 23 strokes"), corroborated internally by the vault's own phonetic-series sibling [[characters/鱗 (char)|鱗]] (same 粦 phonetic, same 12-stroke component, stroke_count 23). Corrected to `stroke_count: 23`, `skip_number: 1-11-12`; removed 麟 from `Lookup/SKIP/SKIP-1/SKIP-1-11-13.md` (size 1→0) and added it to `Lookup/SKIP/SKIP-1/SKIP-1-11-12.md` (size 2→3).

**`aliases` false-positive found and removed, genuine variant added**: stored `獜` — but zh.Wiktionary's own page for 獜 identifies its variant relationship as pointing to 鏻, not 麟 (a shared-phonetic-series false positive, not a genuine alias); removed. Both en.Wiktionary ("Alternative forms": 麐) and zh.Wiktionary (異體字: 麐) independently confirm 麐 as the genuine traditional variant, with en.Wiktionary's own 麐 page confirming "this character is a variant form of 麟." Added `麐`.

**Broken wikilink fixed in an external lookup file**: `Lookup/Korean/Korean Name ㄹ.md`'s own `### 린` line linked `[獜](characters/麟.md)` — pointing the now-confirmed-unrelated 獜 at 麟's page; corrected to an unresolved `[[獜]]` wikilink, matching the format used for the line's other pageless characters.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense "qilin," consistent with sibling 麒.

**`boundedness` filled**: was blank. Estimated `40` — less bound than 麒 (5) since 麟 appears productively as an independent morpheme in [[words/麟経|麟経]] and [[words/麟史|麟史]] (both meaning "the Spring and Autumn Annals"), not solely within 麒麟 itself.

**`## Words` completeness gap found and fixed**: [[words/麒麟羚羊|麒麟羚羊]] genuinely cites 麟 in its `characters:` field but was missing from the list; added, ruby verified against the word's own `注音` field.

Rebuilt the malformed `## Notes` (two bare floating CC-initial/final wikilinks, no phono-semantic/SKIP/level bullets) into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 槐 (8329; 430 characters remaining).

### 2026-08-19, iteration 2074 — [[characters/槐|槐]]

`mc_id: 2322` reconfirmed exact match (CC 2000.md: `2321. 餌`, `2322. 槐`, `2323. 悍`). `graphemic_classification: 鬼` (dual-source confirmed 形声, semantic 木 + phonetic 鬼) reconfirmed correct. `joyo_level: 表外字` reconfirmed correct — en.Wiktionary explicitly cites Hyōgai classification. `korean: 괴`/`羅馬字: hwai`/`諺文: 홰` investigated as a suspected mismatch, then reconfirmed correct: sibling 怪 shares the exact same MC final (ɣuɛi) and also reads 괴 in Korean but derives a *different* 羅馬字/諺文 (gwai/괘ﾞ) from its unvoiced 見-series initial versus 槐's voiced 匣-series initial — modern Korean merges the voicing distinction the conlang's MC-derived romanization preserves, so the mismatch is expected, not a bug. `stand_in: 槐樹` reconfirmed correct as primary citer. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-4-10.md` (item 7).

**`pos` bug found and fixed (genuine misclassification)**: stored `固有名詞` (proper noun), but "pagoda tree" is a common tree-species noun — comparable characters (梅, 桑, 樟) are all `名詞`. Corrected to `名詞`.

**`japanese`/`japanese_native` bugs found and fixed — incomplete on'yomi plus nanori/kun'yomi confusion**: `japanese` was a bare scalar `KAI` (only the kan-on); en.Wiktionary documents two additional go-on readings, `け (ke)` and `ゑ→え (e)`. Corrected to a list `[KE, E, KAI]`. `japanese_native` stored `さいかち`, which en.Wiktionary identifies as a *nanori* (name-only reading), not the genuine kun'yomi `えんじゅ (enju)` — corroborated independently by [[words/槐月|槐月]]'s own `japanese` field, `えんじゅつき`. Corrected `japanese_native` to `えんじゅ`.

**`vietnamese` bug found and fixed — incomplete plus YAML scalar**: stored bare scalar `hoe` (the Nôm reading only); hvdic also lists the genuine Hán Việt reading `hoè`. Corrected to a proper list `[hoè, hoe]`.

**`aliases` bug found and fixed — missing entirely, not just blank**: the `aliases` key was absent from the frontmatter altogether; both sources confirm no variant/simplified forms exist for 槐 (identical across traditional/simplified). Added the key, correctly blank.

**`hsk_level` reconfirmed correct but evidence-basis fixed**: stored `無` was already right — `Old HSK 4.md` has only a colon-count frequency entry (`[[槐]]: 2`, not genuine), and 槐 was absent from `Lookup/HSK/HSK No.md`. Added for consistency.

**Missing lookup cross-reference found and fixed**: 槐 was absent from `Lookup/Japanese/Hyōgai.md`; added as item 448.

**Broken wikilink fixed in an external lookup file**: `Lookup/Korean/Korean Name ㄱ.md`'s own `### 괴` line linked `[[characters/槐]] (do it)` — a raw file-path wikilink plus a stray scratch-note fragment — instead of the standard markdown-link format used by the line's other entries; corrected to `[槐](characters/槐.md)`.

**`## Words` completeness gap found and fixed**: [[words/槐月|槐月]] genuinely cites 槐 in its `characters:` field but was missing from the list; added, ruby verified against the word's own `注音` field (also independently corroborating the `japanese_native` fix above).

Rebuilt the malformed `## Notes` (two bare floating CC-initial/final wikilinks, no phono-semantic/SKIP/level bullets) into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 栾 (8330; 429 characters remaining).

### 2026-08-19, iteration 2075 — [[characters/栾|栾]]

`mc_id: 1518` reconfirmed exact match, recorded under traditional sibling glyph 欒 (CC 1000.md: `1517. 釐`, `1518. 欒`, `1519. 苗`). `graphemic_classification: 䜌` (dual-source confirmed 形声, semantic 木 + phonetic 䜌, recorded under the traditional sibling matching convention) reconfirmed correct. `joyo_level: 表外字` reconfirmed correct — en.Wiktionary explicitly cites Hyōgai classification. `vietnamese: [loan]` reconfirmed exact match to hvdic's sole genuine reading (both Hán Việt and Nôm). `japanese: [RAN]`/`japanese_native: おうち` reconfirmed correct — en.Wiktionary lists several additional kun'yomi (ひじき, まどか, まるい) but these belong to unrelated senses (seaweed; "round") not covered by this page's single tree-species meaning, so left as-is rather than treated as a completeness gap. `stand_in: 名専字` reconfirmed correct — zero hits for 栾 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-6-4.md` (item 14) and `Lookup/Korean/Korean Name ㄹ.md` (under the 欒 alias link).

**`aliases` bug found and fixed — three phonetic-series false positives**: stored `[欒, 圝, 灤, 滦]`. Only `欒` is genuine (en.Wiktionary explicitly confirms it as the traditional/kyūjitai form of shinjitai 栾). The other three were investigated individually: zh.Wiktionary's own page for `灤` lists its variants as `滦`/`灓`, not 欒/栾 — 灤 and 欒 merely share the same phonetic series (系列#1173) per a "See also" note, not a genuine variant relationship; `圝` is explicitly identified by its own zh.Wiktionary page as "a variant form of 圞" (an unrelated "round/circle" word), again just phonetic-series co-occurrence. Removed all three; `滦` (灤's own simplified form) was never a variant of 欒/栾 either and was removed alongside it. This mirrors the 獜/麟 false-positive pattern found last iteration, but with three false positives on a single page rather than one.

**`pos` bug found and fixed (genuine misclassification)**: stored `固有名詞` (proper noun), but "Koelreuteria paniculata" (goldenrain tree) is a common tree-species noun, matching the 槐/梅/桑/樟 precedent. Corrected to `名詞`.

**YAML cosmetic inconsistencies fixed**: `japanese` and `english` list items were written at 0 indentation (`japanese:\n- RAN`) instead of the file's otherwise-consistent 2-space indent; normalized.

**`hsk_level` reconfirmed correct but evidence-basis fixed**: stored `無` was already right — zero evidence exists anywhere (absent from every `Old HSK N.md` file and from `Lookup/HSK/HSK No.md`). Added for consistency.

**Missing lookup cross-reference found and fixed**: 栾 was absent from `Lookup/Japanese/Hyōgai.md`; added as item 449.

**Unverifiable scratch note dropped, not propagated**: the stray fragment "Originally 2-19-4, it is now because Extended Shinjitai" was investigated — no `SKIP-2-19-4.md` file exists anywhere in the vault to corroborate a prior SKIP classification, and SKIP data isn't sourced from Wiktionary, so the claim is unverifiable by this vault's own methodology. Dropped rather than carried forward as unresolved ambiguity, consistent with the 鰐 precedent.

Rebuilt the malformed `# Notes` (wrong heading level, a stray unverifiable scratch fragment, two floating unlinked CC wikilinks, no SKIP/mc_id/lookup bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 蘭 (8331; 428 characters remaining).

### 2026-08-19, iteration 2076 — [[characters/蘭|蘭]]

`mc_id: 1417` reconfirmed exact match (CC 1000.md: `1416. 乏`, `1417. 蘭`, `1418. 穿`). `graphemic_classification: 䦨` reconfirmed correct — dual-source confirmed 形声, semantic 艹 + phonetic 闌 (traditional glyph); 䦨 is zh.Wiktionary's own confirmed variant of 闌 (part of the same 系列) and is the only one of that phonetic-series cluster with its own vault page, matching the cite-what-exists convention. `joyo_level: 日本人名用漢字` reconfirmed correct — already correctly cross-referenced at `Lookup/Japanese/Jinmeiyō.md` item 151. `hanmun_edu_level: 高等` reconfirmed correct — already correctly cross-referenced at `Lookup/Korean/Korean HS.md`. `aliases: [兰, 𬞕]` reconfirmed both correct (standard and nonstandard simplified forms). `stand_in: 蘭花` reconfirmed correct as primary citer.

**`english` bug found and fixed (genuine content error)**: stored `[lily, orchid]` — dual-source confirms 蘭 never means "lily" anywhere; its sole primary sense is "orchid" (specifically cymbidium). Removed the spurious `lily`.

**`vietnamese` bug found and fixed — wrong reading, not mere contamination**: stored `[lan, lơn]`; hvdic's genuine union is `lan` only (both Hán Việt and Nôm) — `lơn` appears nowhere on the page, a severe content error matching the 俁/鯨 precedent rather than diacritic corruption. Removed.

**`hsk_level` bug found and fixed**: stored `"3"` (also incorrectly quoted as a string), traced only to colon-count frequency entries in `Old HSK 3.md` (`[[蘭]]: 1` and `[兰](...): 1`, neither genuine). Zero genuine plain-numbered entry exists in any `Old HSK N.md` file, and 蘭 was absent from `Lookup/HSK/HSK No.md`. Corrected to `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added to `HSK No.md`.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense "orchid."

**Missing lookup cross-reference found and fixed**: 蘭 was absent from `Lookup/Korean/Korean Name ㄹ.md`'s `### 란` section despite having its own independent page and `korean` reading 란 (all four other characters sharing that reading were already listed); added.

**`## Words` completeness gap found and fixed — two missing citers plus the stand_in itself**: the malformed pre-existing list (six country names, jammed inside a mis-headed `## Words`/`## Notes` block) was missing [[words/蘭花|蘭花]] (the stand_in itself), [[words/蘭月|蘭月]] ("orchid month"), and [[words/芬蘭|芬蘭]] ("Finland"). All three added, ruby verified against each word's own `注音` field; one pre-existing entry ([[words/新西蘭|新西蘭]]) used a raw markdown-link-to-file-path format instead of a standard wikilink — normalized to match the rest of the list.

**Notes trivia verified, not dropped**: the stray unheaded fragment "often used for sound, to imitate 'land'" was investigated and confirmed genuine — 蘭 functions purely phonetically (transliterating English "-land") in all six country-name citers. Preserved and folded into the rebuilt Notes prose.

Rebuilt the malformed `## Notes`/`## Words` block (wrong section order, an Old-Chinese-only phono-semantic bullet mixing reconstruction notation inconsistent with the page's own Middle Chinese fields, a broken empty phonetic wikilink, two floating unlinked CC wikilinks, no SKIP/mc_id/lookup bullets) into the standard section order and four-bullet `## Notes` format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 砒 (8332; 427 characters remaining).

### 2026-08-19, iteration 2077 — [[characters/砒|砒]]

`mc_id: 0` reconfirmed correct (confirmed absent from all four CC files). `graphemic_classification: 比` (dual-source confirmed 形声, semantic 石 + phonetic 比) reconfirmed correct. `joyo_level: 表外字` reconfirmed correct — already correctly cross-referenced at `Lookup/Japanese/Hyōgai.md` item 203. `aliases: [磇]` reconfirmed correct — zh.Wiktionary explicitly confirms 磇 as "another way of writing 砒." `stand_in: 砒素` reconfirmed correct — sole citer.

**`vietnamese` bug found and fixed — wrong reading, not mere contamination**: stored `[phi]`; hvdic's genuine union is `phê`/`tì`/`tỳ` (Hán Việt) and `phê`/`tì` (Nôm) — `phi` appears nowhere on the page, a severe content error matching the 俁/鯨/蘭 precedent. Corrected to `[phê, tì, tỳ]`.

**`pos` bug found and fixed (genuine misclassification)**: stored `固有名詞` (proper noun); the comparable classical element-name character [[characters/硫|硫]] (sulfur) is `名詞`, and 砒 (a naturally-occurring classical element name, unlike the synthetic-element `固有名詞` exception seen on [[characters/錀 (char)|錀 (char)]]) should follow the common-element-noun pattern. Corrected to `名詞`.

**Notes content error found and fixed (backwards claim)**: the stray fragment "Replaces 砷" had the historical relationship backwards — both sources confirm 砒 is the *obsolete* character, and 砷 is what replaced *it* as the modern standard element symbol for arsenic, not the reverse. Corrected the wording and linked `[[砷]]` (no independent page exists).

**Missing lookup cross-reference found and fixed**: 砒 was absent from `Lookup/HSK/HSK No.md` despite genuine `hsk_level: 無` status (zero evidence anywhere); added.

**Broken wikilink fixed in an external lookup file**: `Lookup/Korean/Korean Name ㅂ.md`'s own `### 비` line linked `[[characters/砒]]` — a raw file-path wikilink — instead of the standard markdown-link format used by the line's other resolved entries; corrected to `[砒](characters/砒.md)`.

Rebuilt the malformed `## Notes` (missing `## Words` section entirely — the sole citing word [[words/砒素|砒素]] was folded into a Notes bullet instead — Old-Chinese-only phonetic notation, a stray unheaded numbered-list artifact "1. Arsenic", two floating unlinked CC wikilinks, no SKIP/mc_id/lookup bullets) into the standard section order and four-bullet `## Notes` format, with ruby verified against the word's own `注音` field. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 攬 (8333; 426 characters remaining).

### 2026-08-19, iteration 2078 — [[characters/攬|攬]]

`mc_id: 3818` reconfirmed exact match (CC 3000.md: `3817. 沌`, `3818. 攬`, `3819. 晡`). `graphemic_classification: 覽` (dual-source confirmed 形声, semantic 扌 + phonetic 覽) reconfirmed correct. `aliases: [揽]` reconfirmed correct (genuine simplified form). `vietnamese: [lãm]` reconfirmed exact match to hvdic's sole genuine reading. `stand_in: 名専字` reconfirmed correct — zero hits for 攬 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-3-22.md` (item 1) and `Lookup/Korean/Korean Name ㄹ.md`.

**`japanese_native` bug found and fixed (truncated reading)**: stored `と` — an incomplete fragment; en.Wiktionary's genuine kun'yomi is `とる (toru)`. Corrected.

**`joyo_level` filled**: was blank. Both sources confirm 攬 as Hyōgai kanji; added as item 450 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`hsk_level` bug found and fixed**: stored `"4"` (also incorrectly quoted as a string), traced only to colon-count frequency entries in `Old HSK 4.md` (neither genuine). Zero genuine plain-numbered entry exists in any `Old HSK N.md` file, and 攬 was absent from `Lookup/HSK/HSK No.md`. Corrected to `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added to `HSK No.md`.

**`pos` filled**: was blank. Filled as `事詞`, matching the verbal sense "grasp; monopolize."

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no phono-semantic/SKIP/level bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 鷹 (char) (8334; 425 characters remaining).

### 2026-08-19, iteration 2079 — [[characters/鷹 (char)|鷹 (char)]]

`mc_id: 2452` reconfirmed exact match (CC 2000.md: `2451. 雁`, `2452. 鷹`, `2453. 譯`). `graphemic_classification: 䧹` (dual-source confirmed 形声, semantic 鳥 + phonetic 䧹) reconfirmed correct. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 304. `aliases: [鹰]` reconfirmed correct (genuine simplified form). `vietnamese: [ưng]` reconfirmed exact match to hvdic's sole genuine reading. `stand_in: 鷹` reconfirmed correct as primary self-referential citer (a second genuine citer, [[words/単鷹国|単鷹国]] "Prussia," was found and added to `## Words`). Already correctly cross-listed on `Lookup/SKIP/SKIP-3/SKIP-3-3-21.md` and `Lookup/Korean/Korean Name ㅇ.md`.

**`hsk_level` bug found and fixed**: stored `"4"` (also incorrectly quoted as a string), traced only to colon-count frequency entries in `Old HSK 4.md` (neither genuine). Zero genuine plain-numbered entry exists in any `Old HSK N.md` file, and 鷹 (char) was absent from `Lookup/HSK/HSK No.md`. Corrected to `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added to `HSK No.md`.

**Incidental YAML bug fixed on citing word page**: [[words/鷹|鷹]]'s own `characters` field was a bare scalar (`鷹 (char)`) instead of a proper list; corrected.

Rebuilt the doubled `## Notes` section (two separate headers — the first containing only floating unlinked CC wikilinks, the second containing a malformed phono-semantic bullet with semantic/phonetic reversed in the prose and an empty phonetic wikilink, no SKIP/mc_id/lookup bullets, no `## Words` section) into a single standard `## Notes` four-bullet format plus a `## Words` section citing both genuine citing words, with ruby verified against each word's own `注音` field. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 鑽 (8335; 424 characters remaining).

### 2026-08-19, iteration 2080 — [[characters/鑽|鑽]]

`mc_id: 3038` reconfirmed exact match (CC 3000.md: `3037. 窴`, `3038. 鑽`, `3039. 耨`). `graphemic_classification: 贊` (dual-source confirmed 形声, semantic 金 + phonetic 贊) reconfirmed correct. `joyo_level: 表外字` reconfirmed correct — en.Wiktionary explicitly cites Hyōgai (noting 鑚 as its own Japanese shinjitai, already correctly held in `aliases`). `stand_in: 鑽石` reconfirmed correct — sole citer. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-8-19.md` (item 2).

**`japanese_native` bug found and fixed (truncated reading)**: stored `き` — an incomplete fragment; en.Wiktionary's genuine kun'yomi set is きり/きる/たがね. Corrected to `きり` (matching the "auger/drill" noun sense).

**`aliases` completeness gap found and fixed**: en.Wiktionary's own "Alternative forms" field lists `鑚`, `鉆`/`钻` — `鉆` was missing from the stored `[钻, 鑚, 𰿆]`. Independently verified `𰿆` as genuine (zh.Wiktionary explicitly labels it "a simplification-by-analogy form of 鑽 (U+947D)," not a false positive). Added `鉆`.

**`vietnamese` completeness gap found and fixed**: hvdic's genuine union is `toàn`/`toản` (Hán Việt) and `toản`/`xoảng` (Nôm); the stored `[toản, xoảng]` was missing the genuine reading `toàn`. Added it.

**`hsk_level` bug found and fixed**: stored `"2"` (also incorrectly quoted as a string), traced only to colon-count/malformed frequency entries in `Old HSK 2.md` (neither genuine). `Old HSK 6.md` has a genuine plain-numbered entry under the simplified sibling glyph 钻 (`521. [钻]`). Corrected to `hsk_level: 6`.

**Missing lookup cross-reference found and fixed**: 鑽 was absent from `Lookup/Japanese/Hyōgai.md` despite genuine `表外字` status; added as item 451.

**Broken wikilink fixed in an external lookup file**: `Lookup/Korean/Korean Name ㅊ.md`'s own `### 찬` line held an unresolved `[[鑽]]` wikilink even though `characters/鑽.md` genuinely exists as a page; corrected to the standard markdown-link format `[鑽](characters/鑽.md)`.

Rebuilt the malformed `## Notes` (a bare unheaded "Components:" bullet with pageless wikilinks, no SKIP/mc_id/lookup bullets, two floating unlinked CC wikilinks) into the standard four-bullet format, preserving the genuine "use 金剛石 for the mineral" trivia. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 菱 (char) (8336; 423 characters remaining).

### 2026-08-19, iteration 2081 — [[characters/菱 (char)|菱 (char)]]

`mc_id: 5223` reconfirmed as trusted long-tail (>4000, per convention no exhaustive grep required). `graphemic_classification: 夌` (dual-source confirmed 形声, semantic 艹 + phonetic 夌) reconfirmed correct. `joyo_level: 日本人名用漢字` reconfirmed correct — already correctly cross-referenced at `Lookup/Japanese/Jinmeiyō.md` item 317. `hsk_level: 無` reconfirmed correct — already correctly cross-referenced at `Lookup/HSK/HSK No.md`. `vietnamese: [lăng, năng, trăng]` reconfirmed all three genuine (no contamination) — hvdic's union is `lăng` (Hán Việt) and `lăng`/`năng`/`trăng` (Nôm), a rare case where all three initially-suspicious readings (including "trăng," which coincidentally also means "moon" in isolation) checked out as genuine. `korean: 릉` (not the South Korean 두음법칙-shifted `능` that zh.Wiktionary's summary paraphrase suggested) reconfirmed correct per the vault's standing North-Korean-reading convention. `aliases` (blank) reconfirmed correct — no variant/simplified forms exist; the traditional/simplified glyphs are unified. `stand_in: 菱` reconfirmed correct as primary self-referential citer (the page's own pre-existing Notes already correctly cited the second genuine citer, [[words/菱形|菱形]], now moved into `## Words`). Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-8.md` (item 20) and `Lookup/Korean/Korean Name ㄹ.md`.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense "water chestnut."

**Incidental YAML bug fixed on citing word page**: [[words/菱|菱]]'s own `characters` field was a bare scalar (`菱 (char)`) instead of a proper list; corrected.

Rebuilt the malformed `# Notes` (wrong heading level, no `## Words` section — the sole pre-existing citer was folded into a bare Notes bullet instead — two floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard section order and four-bullet `## Notes` format, with ruby verified against each word's own `注音` field. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 梛 (8337; 422 characters remaining).

### 2026-08-19, iteration 2082 — [[characters/梛|梛]]

`mc_id: 0` reconfirmed correct (confirmed absent from all four CC files). `graphemic_classification: 那` (dual-source confirmed 形声, semantic 木 + phonetic 那) reconfirmed correct. `joyo_level: 日本人名用漢字` reconfirmed correct — already correctly cross-referenced at `Lookup/Japanese/Jinmeiyō.md` item 240. `stand_in: 名専字` reconfirmed correct — zero hits for 梛 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-4-7.md` (item 8).

**Significant cross-character conflation found and fixed, touching three fields plus two external lookup files**: this page had been contaminated with data belonging to the unrelated character 挪 ("to move; shift" — same phonetic series 那, but a different character entirely, using 扌 rather than 木, and with no page of its own anywhere in this vault). Specifically:
- `aliases` stored `[挪]`; both sources confirm 挪 merely shares 梛's phonetic component, not a variant relationship — dual-source false positive, removed (mirroring the 獜/麟 and 灤/圝/栾 precedents from recent iterations).
- `korean_native` stored `옮길` ("move") — genuinely 挪's meaning, not 梛's. Corrected to `나무이름` ("tree name"), a defensible generic gloss given no attested traditional 훈 could be sourced for 梛 specifically.
- `hsk_level` stored `"6"` (quoted) — traced to `Old HSK 6.md`'s entry `792. [挪](../../characters/梛.md)`, which is genuinely about 挪 (a common HSK 6 verb) but mislinks to 梛's page — the likely origin of the whole conflation. Corrected to `hsk_level: 無` (zero genuine evidence exists for 梛 the tree-name character itself); left the Old HSK 6.md source file untouched (out of scope — a raw frequency-list artifact, not a maintained lookup cross-reference).
- `Lookup/Korean/Korean Name ㄴ.md`'s own `### 나` line also linked `[挪](../../characters/梛.md)` — corrected to an unresolved `[[挪]]` wikilink, correctly reflecting that 挪 has no page and is not 梛.

**`vietnamese` bug found and fixed — spurious extra reading**: stored `[na, ná, nứa]`; hvdic confirms no Hán Việt reading exists yet for 梛 ("Chưa có giải nghĩa theo âm Hán Việt") and lists only `na`/`nứa` as genuine Nôm readings — `ná` appears nowhere on the page. Removed.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal tree-name sense.

**`boundedness` filled**: was blank. Estimated `65` by analogy to comparable obscure tree-name characters (槐, 栾), flagged as a judgment call absent a formal definition.

Rebuilt the malformed `## Notes` (a stray bare lookup-only bullet with no phono-semantic/SKIP/mc_id content, two floating unlinked CC wikilinks) into the standard four-bullet format, explicitly noting the 挪 non-relationship to prevent the conflation from recurring. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 狗 (8338; 421 characters remaining).

### 2026-08-19, iteration 2083 — [[characters/狗|狗]]

`mc_id: 1196` reconfirmed exact match (CC 1000.md: `1195. 踐`, `1196. 狗`, `1197. 讒`). `graphemic_classification: 句` (dual-source confirmed 形声, semantic 犬 + phonetic 句) reconfirmed correct. `joyo_level: 表外字` reconfirmed correct — already correctly cross-referenced at `Lookup/Japanese/Hyōgai.md` item 96. `hanmun_edu_level: 高等` reconfirmed correct — already correctly cross-referenced at `Lookup/Korean/Korean HS.md`. `english: [hound]` reconfirmed correct as a deliberate vocabulary-uniqueness choice, not a bug — the vault's [[characters/犬 (char)|犬 (char)]] already holds the plain "dog" gloss and is the genuine bound word for "dog," so 狗 (colloquial/originally "small dog") takes the secondary gloss. `諺文: 곳` reconfirmed correct — matches the vault's own established ㄍㄛㄨ syllable-page spelling convention, not a typo despite superficially looking inconsistent with `羅馬字: gou`. `vietnamese: [cẩu]` reconfirmed correct via general corroboration (hvdic returned a server error on this character; "cẩu" is a well-attested common Hán Việt reading, e.g. in 狗肉/cẩu nhục). `stand_in: 名専字` reconfirmed correct — 狗 never appears as a `characters:`-citing constituent of its own compound headword; it's always a bound constituent of other words. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-3-5.md` (item 72).

**`aliases` filled**: was blank. en.Wiktionary's own "Alternative forms" field lists `豿` and `㺃`; zh.Wiktionary references both without contradicting the relationship. Added both under the established single-source-strong-statement exception (matching the 鶴/蟹 precedent).

**`hsk_level` bug found and fixed**: stored `"2"` (quoted), traced only to a colon-count frequency entry in `Old HSK 2.md` (`[狗](...): 1`, not genuine). Zero genuine plain-numbered entry exists in any `Old HSK N.md` file, and 狗 was absent from `Lookup/HSK/HSK No.md` — despite 狗 being common vocabulary in reality, the methodology only trusts plain-numbered entries. Corrected to `hsk_level: 無` and added to `HSK No.md`.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense "dog."

**`## Words` completeness gap found and fixed**: [[words/天狗|天狗]] ("tengu; Tiangou") genuinely cites 狗 in its `characters:` field but was missing from the list; added, ruby verified against the word's own `注音` field. The four other pre-existing citers (狗肉, 狗盗, 狗吠, 芻狗, 海狗) were already correctly identified but stranded as bare or malformed bullets outside a proper `## Words` section — consolidated and ruby-corrected against each word's own `注音` field (one, 狗吠, had been given a fabricated placeholder ruby during drafting and was corrected before finalizing).

**Notes trivia verified, not dropped**: zh.Wiktionary's classical distinction "大者為犬，小者為狗" (larger ones are 犬, smaller ones are 狗) was corroborated and folded into the rebuilt Notes prose.

Rebuilt the malformed `## Notes`/`## Words` block (wrong section order, floating unlinked CC wikilinks stranded between two Words-style bullet groups, no SKIP/mc_id/level bullets) into the standard section order and four-bullet `## Notes` format; the existing `## Chengyu` section was already correctly formatted and untouched. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 嘉 (8339; 420 characters remaining).

### 2026-08-19, iteration 2084 — [[characters/嘉|嘉]]

`mc_id: 663` reconfirmed exact match (CC 0000.md: `661. 貧`, `662. 再`, `663. 嘉`). `graphemic_classification: 加` (dual-source confirmed 形声, semantic 壴 + phonetic 加) reconfirmed correct. `radical: 口` reconfirmed correct — genuine Kangxi radical 30. `joyo_level: 日本人名用漢字` reconfirmed correct — already correctly cross-referenced at `Lookup/Japanese/Jinmeiyō.md` item 427. `vietnamese: [gia]` reconfirmed exact match to hvdic's sole genuine reading. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-11.md` (item 1) and `Lookup/Korean/Korean Name ㄱ.md`.

**`stand_in` bug found and fixed**: stored `名専字`, but two genuine citing words exist — [[words/嘉賓|嘉賓]] (already correctly cited in the page's own pre-existing Notes) and [[words/新嘉浦|新嘉浦]] ("Singapore," a phonetic-transliteration compound, missing entirely). Corrected `stand_in` to `嘉賓` (the meaning-bearing compound, matching the 蘭/蘭花 precedent of preferring a semantic citer over a phonetic-transliteration one), and added both to `## Words`.

**`hsk_level` bug found and fixed**: stored `"4"` (quoted), traced only to a colon-count frequency entry in `Old HSK 4.md` (`[[嘉]]: 2`, not genuine). `Old HSK 5.md` has a genuine plain-numbered entry (`504. [[嘉]]`). Corrected to `hsk_level: 5`.

**`pos` filled**: was blank. Filled as `性詞`, matching the adjectival sense "good; excellent."

**Stale gloss error propagated from a since-fixed word page, caught and corrected**: the page's own pre-existing Notes carried the gloss "guest of honor, sparrow" for [[words/嘉賓|嘉賓]] — the "sparrow" half was a content error on that word's own page, already found and removed during a prior word-perfecting pass (`words/嘉賓.md`, dated 2026-08-04), but the stale erroneous gloss had never been updated here. Corrected to match the word's current, already-fixed gloss ("guest of honor" only).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard section order and four-bullet `## Notes` format, with ruby verified against each word's own `注音` field. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 丕 (8340; 419 characters remaining).

### 2026-08-19, iteration 2085 — [[characters/丕|丕]]

`mc_id: 2202` reconfirmed exact match (CC 2000.md: `2201. 豚`, `2202. 丕`, `2203. 黔`). `graphemic_classification: 不` (dual-source confirmed 形声, semantic 一 + phonetic 不) reconfirmed correct. `hsk_level: 無` reconfirmed correct — already correctly cross-referenced at `Lookup/HSK/HSK No.md`. `aliases` (blank) reconfirmed correct — no variant forms found in either source. `stand_in: 名専字` reconfirmed correct — zero hits for 丕 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-4-1.md` (item 1) and `Lookup/Korean/Korean Name ㅂ.md`.

**`vietnamese` bug found and fixed — three diacritic-corrupted duplicates**: stored `[bậy, chăng, chẳng, phi, phỉ, vầy, vậy]`. This character genuinely has an unusually large reading set — hvdic confirms `phi` (Hán Việt) and `bậy`/`chăng`/`phi`/`vầy` (Nôm) as all genuine — but three additional entries (`chẳng`, `phỉ`, `vậy`) are near-duplicate tone/diacritic corruptions of the genuine `chăng`/`phi`/`vầy` and appear nowhere on hvdic's page. Removed the three spurious entries, keeping the four genuine ones.

**`joyo_level` filled**: was blank. en.Wiktionary explicitly confirms 丕 as Hyōgai kanji; added as item 452 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`pos` filled**: was blank. Filled as `性詞`, matching the adjectival sense "great; grand."

**Notes trivia added**: en.Wiktionary/zh.Wiktionary corroborate 丕's surname sense (e.g. 曹丕, Cao Pi); folded into the rebuilt Notes prose.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no phono-semantic/SKIP/level bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 喇 (8341; 418 characters remaining).

### 2026-08-19, iteration 2086 — [[characters/喇|喇]]

`mc_id: 7015` reconfirmed as trusted long-tail (>4000). `graphemic_classification: 剌` (dual-source confirmed 形声, semantic 口 + phonetic 剌) reconfirmed correct. `joyo_level: 表外字` reconfirmed correct (implicit — obscure character, no jōyō/jinmeiyō listing found in either source). `vietnamese: [lạt]` reconfirmed exact match to hvdic's sole genuine reading. `hsk_level: "6"` reconfirmed correct (also unquoted) — `Old HSK 6.md` has a genuine plain-numbered entry `611. [[喇]]`. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-3-9.md` (item 4, itself already correctly glossing the trumpet/lama sense) and `Lookup/Korean/Korean Name ㄹ.md`.

**Significant polysemy/cross-etymology conflation found and fixed, touching three fields plus two lookup files**: 喇 is genuinely polysemous with several distinct etymologies at different tones (Etymology 1: `lǎ`, bound to 喇叭 "trumpet"; Etymology 6: a Cantonese/Mandarin sentence-final particle, aliased 嗱/啦/嘑/嚹/𡅈). This page's stored `mandarin: lǎ` and `korean_native: 나팔` ("trumpet") both clearly targeted Etymology 1, but two fields had been contaminated with Etymology-6 data instead:
- `english` stored `rain sound` — actually a *third*, unrelated etymology (onomatopoeia for wind/rain) — while [[words/喇叭|喇叭]] (a genuine citing word, confirming the intended sense) glosses "horn, trumpet." Corrected to `[horn, trumpet]`.
- `aliases` stored `[嗱, 啦, 嘑, 嚹, 𡅈]` — en.Wiktionary explicitly attributes these to the Cantonese-particle etymology (Etymology 6), unrelated to the trumpet sense modeled on this page. Removed all five; noted the non-relationship explicitly in the rebuilt Notes to prevent recurrence.
- `stand_in` stored `名専字`, overlooking the genuine citing word [[words/喇叭|喇叭]] — corrected to `喇叭`, and added to a new `## Words` section.

**`Lookup/HSK/HSK No.md` inconsistency found and fixed**: 喇 was listed there (implying `hsk_level: 無`) despite the frontmatter's own genuine `hsk_level: 6` — a pre-existing internal contradiction. Removed the stray entry, since a real numeric level and a "confirmed-無" listing can't both be true.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense "horn; trumpet."

**Missing lookup cross-reference found and fixed**: 喇 was absent from `Lookup/Japanese/Hyōgai.md` despite genuine `表外字` status; added as item 453.

Rebuilt the malformed `# Notes` (wrong heading level, no `## Words` section, two floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard section order and four-bullet `## Notes` format, with ruby verified against the word's own `注音` field. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 煥 (8342; 417 characters remaining).

### 2026-08-19, iteration 2087 — [[characters/煥|煥]]

`mc_id: 3571` reconfirmed exact match (CC 3000.md: `3570. 彳`, `3571. 煥`, `3572. 麑`). `graphemic_classification: 奐` (dual-source confirmed 形声, semantic 火 + phonetic 奐) reconfirmed correct. `vietnamese: [hoán]` reconfirmed exact match to hvdic's sole genuine reading. `aliases: [烉, 焕]` reconfirmed both correct — `焕` the standard simplified form; `烉` investigated further after zh.Wiktionary's phrasing was ambiguous, then confirmed genuine via en.Wiktionary's explicit "this character is an ancient form of 煥." `stand_in: 名専字` reconfirmed correct — zero hits for 煥 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-4-9.md` (item 20) and `Lookup/Korean/Korean Name ㅎ.md`.

**`english` typo found and fixed**: `lusterous` → `lustrous`.

**`joyo_level` filled**: was blank. en.Wiktionary explicitly confirms 煥 as Hyōgai kanji; added as item 454 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`hsk_level` filled**: was blank. Zero evidence anywhere (absent from every `Old HSK N.md` file and from `Lookup/HSK/HSK No.md`). Filled as `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added to `HSK No.md`.

**`pos` filled**: was blank. Filled as `性詞`, matching the adjectival sense "shining; lustrous."

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 祚 (8343; 416 characters remaining).

### 2026-08-19, iteration 2088 — [[characters/祚|祚]]

`mc_id: 2192` reconfirmed exact match (CC 2000.md: `2191. 扈`, `2192. 祚`, `2193. 擯`). `graphemic_classification: 乍` (dual-source confirmed 形声, semantic 示 + phonetic 乍) reconfirmed correct. `vietnamese: [tộ]` reconfirmed exact match to hvdic's sole genuine reading. `aliases` (blank) reconfirmed correct — no variant/simplified forms found. `stand_in: 名専字` reconfirmed correct — zero hits for 祚 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-5-5.md` (item 13) and `Lookup/Korean/Korean Name ㅈ.md`.

**`japanese`/`japanese_native` bugs found and fixed**: `japanese` stored only `[SO]` (the kan-on), missing the genuine go-on `ゾ (ZO)`; corrected to `[ZO, SO]`. `japanese_native` stored `くら`, which appears nowhere in en.Wiktionary's reading list — the genuine kun'yomi is `さいわい (saiwai)`, matching the "blessing; fortune" sense. Corrected.

**`joyo_level` filled**: was blank. en.Wiktionary explicitly confirms 祚 as Hyōgai kanji; added as item 455 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`hsk_level` filled**: was blank. Zero evidence anywhere (absent from every `Old HSK N.md` file and from `Lookup/HSK/HSK No.md`). Filled as `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added to `HSK No.md`.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses "throne; blessing."

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 芦 (8344; 415 characters remaining).

### 2026-08-19, iteration 2089 — [[characters/芦|芦]]

`mc_id: 3728` reconfirmed exact match, recorded under traditional sibling glyph 蘆 (CC 3000.md: `3727. 嵬`, `3728. 蘆`, `3729. 鷇`). `graphemic_classification: 戸` (dual-source confirmed 形声, semantic 艹 + phonetic 户/戸) reconfirmed correct. `joyo_level: 日本人名用漢字` reconfirmed correct — already correctly cross-referenced at `Lookup/Japanese/Jinmeiyō.md` item 330. `hsk_level: 6` (also unquoted) reconfirmed correct — `Old HSK 6.md` has a genuine plain-numbered entry (`248. [[芦]]`). `vietnamese: [lư]` and `tags: [character, cranberry]`/`stand_in: 芦葦` reconfirmed correct — 芦 has no independent word page of its own, matching the bound-morpheme pattern. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-4.md` (item 21).

**Significant cross-character conflation found and fixed, touching aliases and three external lookup/redirect files**: 芦 is genuinely the simplified/variant form of 蘆 ("reed"), but its `aliases` also incorrectly listed `櫓` and `艪` — both confirmed by dual-source research to mean "oar; scull" and to derive from an entirely unrelated phonetic series (魯), with zero relationship to 芦/蘆. Removed both. This same conflation had propagated into three separate places, all now corrected:
- `Lookup/Japanese/Jinmeiyō.md`'s own `## Redirects` section asserted `櫓 --> 芦`; removed the false redirect line.
- `Lookup/Korean/Korean Name ㄹ.md`'s `### 로` line linked `[櫓](characters/芦.md)`; corrected to an unresolved `[[櫓]]` wikilink (`蘆`'s own correct link on the same line was left untouched).
- `Lookup/HSK/HSK No.md` also listed `[[芦]]` despite 芦's own genuine numeric `hsk_level: 6` — a pre-existing internal contradiction (mirroring the 喇 precedent from two iterations ago); removed the stray entry.

**Flagged, not fixed (out of scope for a single-character iteration)**: [[words/櫓櫂|櫓櫂]] ("oars; oars and paddles") — a word whose own display name uses 櫓 — has a `characters:` field citing `芦` instead, apparently relying on the very same false alias relationship just disproven. Since 櫓 has no character page of its own in this vault, correcting this citation would require creating a new page for 櫓, which is out of scope for this iteration's single-character focus. Removed 櫓櫂 from 芦's own `## Words` section (since it isn't a genuine "reed"-sense usage) but left `words/櫓櫂.md` itself untouched — flagging it here for a future iteration once 櫓 has been given a page.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense "reed; rushes."

**`## Words` completeness gap found and fixed**: [[words/胡芦|胡芦]] ("bottle gourd; calabash," genuinely using 芦=蘆 via its own `葫蘆`/`瓠蘆` aliases) was missing from the list; added alongside [[words/芦葦|芦葦]], both ruby-verified against their own `注音` fields.

Rebuilt the malformed `# Notes` (wrong heading level, `## Words` section placed before the Notes rebuild, two floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard section order and four-bullet `## Notes` format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 葦 (8345; 414 characters remaining).

### 2026-08-19, iteration 2090 — [[characters/葦|葦]]

`mc_id: 2480` reconfirmed exact match (CC 2000.md: `2479. 蛟`, `2480. 葦`, `2481. 緯`). `graphemic_classification: 韋` (dual-source confirmed 形声, semantic 艹 + phonetic 韋) reconfirmed correct. `joyo_level: 日本人名用漢字` reconfirmed correct — already correctly cross-referenced at `Lookup/Japanese/Jinmeiyō.md` item 311. `hsk_level: 無` reconfirmed correct — already correctly cross-referenced at `Lookup/HSK/HSK No.md`. `aliases: [苇]` reconfirmed correct (genuine simplified form). `tags: [character, cranberry]`/`stand_in: 芦葦` reconfirmed correct — confirmed transitive with [[characters/芦|芦]] (A=芦, B=葦, AB=芦葦, both bound to the same word, sole citer). Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-10.md` (item 20) and `Lookup/Korean/Korean Name ㅇ.md`.

**`vietnamese` completeness gap found and fixed**: hvdic's genuine union is `vy`/`vĩ` (Hán Việt) and `vi` (Nôm); only `vi` was stored. Added `vy` and `vĩ`.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense "reed."

Rebuilt the malformed `# Notes` (wrong heading level, no `## Words` section, two floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard section order and four-bullet `## Notes` format, with ruby verified against the word's own `注音` field. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 靄 (8346; 413 characters remaining).

### 2026-08-19, iteration 2091 — [[characters/靄|靄]]

`mc_id: 0` reconfirmed correct (confirmed absent from all four CC files). `graphemic_classification: 謁` (dual-source confirmed 形声, semantic 雨 + phonetic 謁) reconfirmed correct. `joyo_level: 表外字` reconfirmed correct — en.Wiktionary explicitly cites Hyōgai; already correctly cross-referenced at `Lookup/Japanese/Hyōgai.md` item 7. `hsk_level: 無` reconfirmed correct — already correctly cross-referenced at `Lookup/HSK/HSK No.md`. `aliases: [霭]` reconfirmed correct (genuine simplified form). `stand_in: 名専字` reconfirmed correct — zero hits for 靄 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-8-16.md` (item 1) and `Lookup/Korean/Korean Name ㅇ.md`.

**Notes content error found and fixed (contradicted frontmatter)**: the stray fragment "日本人名用漢字, 이름" asserted Jinmeiyō status, directly contradicting the page's own (correct) `joyo_level: 表外字` and lacking any corroborating source. Dropped rather than propagated.

**`vietnamese` completeness gap found and fixed**: hvdic's genuine union is `ái`/`ải` (Hán Việt) and `ái` (Nôm); only `ái` was stored. Added `ải`.

**`pos` filled**: was blank. Filled as `性詞`, matching the adjectival senses "cloudy; hazy."

Rebuilt the malformed `# Notes` (wrong heading level, a stray contradictory unlinked fragment, two floating unlinked CC wikilinks, no phono-semantic/SKIP/level bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 吾 (8347; 412 characters remaining).

### 2026-08-19, iteration 2092 — [[characters/吾|吾]]

`mc_id: 108` reconfirmed exact match (CC 0000.md: `> 107. 東`, `> 108. 吾`, `> 109. 焉`). `graphemic_classification: 五` confirmed correct — the frontmatter field itself was right, but the malformed Notes prose had it backwards (see below). `joyo_level: 日本人名用漢字` reconfirmed correct — already correctly cross-referenced at `Lookup/Japanese/Jinmeiyō.md` item 86. `hsk_level: 無` reconfirmed correct — already correctly cross-referenced at `Lookup/HSK/HSK No.md`. `vietnamese: [ngô, ngo]` reconfirmed exact match to hvdic's genuine union. `stand_in: 名専字` reconfirmed correct — the page's own pre-existing trivia note (see below) correctly explains why: [[characters/我 (char)|我]] is the vault's genuine bound word for "I," a true Dan'a'yo homophone (both syllable ㄚ/'a/아), leaving 吾 for names only. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-4-3.md` (item 2) and `Lookup/Korean/Korean Name ㅇ.md`.

**Notes prose bug found and fixed (semantic/phonetic reversed and mislabeled)**: the stored bullet read "semantic 五 ('mouth') + phonetic 口" — but 五 means "five," not "mouth," and dual-source research confirms the true composition is semantic 口 ("mouth") + phonetic 五, exactly backwards from what was written (the frontmatter's own `graphemic_classification: 五` had actually been correct all along). Corrected the prose.

**`aliases` bug found and fixed — phonetic-series false positive, replaced with genuine structured-field variants**: stored `[梧]`; zh.Wiktionary explicitly confirms 梧 is not a variant of 吾 but an independently-constructed character (木 + phonetic 吾) that merely shares 吾's phonetic series — the same false-positive pattern as 獜/麟, 灤/栾, and 櫓/艪·芦 from recent iterations. Removed. En.Wiktionary's own structured "Alternative forms" field lists genuine ancient variants `𠮣` and `𭇁` (neither with an independent page); added both under the established single-source-strong-statement exception.

**Same conflation found and fixed in two more external lookup files**: `Lookup/Japanese/Jinmeiyō.md`'s own flat Jinmeiyō-kanji list linked `[梧](../../characters/吾.md)`, and `Lookup/Korean/Korean Name ㅇ.md`'s `### 오` line did the same — both corrected to unresolved `[[梧]]` wikilinks, since 梧 has no page of its own and is not genuinely related to 吾.

**Unverifiable/misattributed scratch note dropped**: "梧 was dropped from the Korean HS list in 2000" — given 梧 is confirmed unrelated to 吾, and neither character currently appears on `Lookup/Korean/Korean HS.md` at all, this note was either about the wrong character or unverifiable; dropped rather than propagated.

**`pos` filled**: was blank. Filled as `名詞`, matching the vault's convention for pronoun-like characters (cf. [[characters/我 (char)|我]]).

**`## Derived Characters` completeness gap found and fixed**: two further genuine derived characters citing `graphemic_classification: 吾` were missing — [[characters/悟|悟]] ("realize") and [[characters/語|語]] ("language") — added alongside the pre-existing [[characters/圄|圄]] ("prison"), all three ruby-verified against each character's own `注音` field.

Rebuilt the malformed `## Notes` (reversed phono-semantic bullet, a misattributed scratch note, two floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard four-bullet format; the pre-existing `## Derived Characters` section was expanded rather than rebuilt from scratch. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 邾 (8348; 411 characters remaining).

### 2026-08-19, iteration 2093 — [[characters/邾|邾]]

`mc_id: 1152` reconfirmed exact match (CC 1000.md: `1151. 雞`, `1152. 邾`, `1153. 斂`). `graphemic_classification: 朱` (dual-source confirmed 形声, semantic 邑 + phonetic 朱) reconfirmed correct. `joyo_level: 表外字` reconfirmed correct — en.Wiktionary explicitly cites Hyōgai. `vietnamese: [chau, chu]` reconfirmed exact match to hvdic's genuine union. `aliases` (blank) reconfirmed correct — no variant/simplified forms found. `stand_in: 邾国` reconfirmed correct — sole citer. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-6-3.md` (item 13) and `Lookup/Korean/Korean Name ㅈ.md`.

**`korean_native` filled**: was blank. Filled as `주나라` ("state of Ju"), matching the vault's own established pattern for feudal-state-name characters (cf. [[characters/楚|楚]] → 초나라, [[characters/宋|宋]] → 송나라).

**`pos` filled**: was blank. Filled as `固有名詞`, matching the proper-noun sense "State of Zou," consistent with other historical-state-name characters.

**`joyo_level` reconfirmed correct but missing cross-reference fixed**: 邾 was absent from `Lookup/Japanese/Hyōgai.md`; added as item 456.

**`hsk_level` filled**: was blank. Zero evidence anywhere (absent from every `Old HSK N.md` file and from `Lookup/HSK/HSK No.md`). Filled as `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added to `HSK No.md`.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard `## Notes` four-bullet format; the existing `## Words` section (citing [[words/邾国|邾国]]) was already correctly formatted and untouched. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 鄭 (8349; 410 characters remaining).

### 2026-08-19, iteration 2094 — [[characters/鄭|鄭]]

`mc_id: 308` reconfirmed exact match (CC 0000.md: `> 307. 賜`, `> 308. 鄭`, `> 309. 制`). `graphemic_classification: 奠` (dual-source confirmed 形声, semantic 邑 + phonetic 奠) reconfirmed correct. `joyo_level: 日本人名用漢字` reconfirmed correct — already correctly cross-referenced at `Lookup/Japanese/Jinmeiyō.md` item 164. `korean_native: 정나라` reconfirmed correct, matching the established feudal-state-name pattern. `stand_in: 鄭国` reconfirmed correct as primary citer (the second genuine citer, [[words/鄭重|鄭重]], was already correctly cited in the page's own malformed Notes, now consolidated into `## Words`). Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-12-3.md` (item 3) and `Lookup/Korean/Korean Name ㅈ.md`.

**`aliases` bug found and fixed — two false positives, including the phonetic component itself**: stored `[郑, 郏, 奠]`. `郑` is genuine (simplified form). `郏` is en.Wiktionary-confirmed to be entirely unmentioned in relation to 鄭 — an unrelated place-name character, a false positive. `奠` is the character's own *phonetic component* (a distinct word, "to offer sacrifice; settle"), not a variant of 鄭 at all — this exact confusion (a character's phonetic component being mistaken for one of its own aliases) also explains a parallel data error in `Old HSK 6.md`, which contains a genuine plain-numbered entry `664. [奠](.../鄭.md)` mislinking the unrelated character 奠 to this page (left untouched, a source-file artifact). Removed both `郏` and `奠` from `aliases`.

**`vietnamese` bugs found and fixed — capitalization plus missing reading**: stored `[Trịnh]` (capitalized, inconsistent with field convention); hvdic's genuine union is `trịnh` (Hán Việt) and `chạnh`/`trịnh` (Nôm). Corrected casing and added the missing `chạnh`.

**`hsk_level` filled**: was blank. `Old HSK 6.md` has a genuine plain-numbered entry under the simplified sibling glyph 郑 (`464. [郑]`). Filled as `hsk_level: 6`.

**`pos` filled**: was blank. Filled as `固有名詞`, matching the proper-noun sense "State of Zheng."

**Unverifiable scratch fragment dropped**: a stray bare "1317" at the top of the malformed Notes matched no known field (not the mc_id, stroke count, or danayo_id) and was unverifiable; dropped rather than propagated.

Rebuilt the malformed `# Notes` (wrong heading level, an unverifiable stray numeral, two floating unlinked CC wikilinks, `## Words`-style bullets stranded inside Notes itself) into the standard section order and four-bullet `## Notes` format, with ruby verified against each word's own `注音` field. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 宋 (8350; 409 characters remaining).

### 2026-08-19, iteration 2095 — [[characters/宋|宋]]

A largely clean page this iteration. `mc_id: 347` reconfirmed exact match (CC 0000.md: `> 346. 刑`, `> 347. 宋`, `> 348. 尊`). `graphemic_classification: 會意` reconfirmed correct — dual-source confirms the etymology is unclear beyond its literal ⿱宀木 composition, matching the vault's semantic-only classification convention. `joyo_level: 日本人名用漢字` reconfirmed correct — already correctly cross-referenced at `Lookup/Japanese/Jinmeiyō.md` item 95. `hsk_level: 無` reconfirmed correct — already correctly cross-referenced at `Lookup/HSK/HSK No.md`. `korean_native: 송나라` reconfirmed correct, matching the established feudal-state/dynasty-name pattern. `vietnamese: [tống]` reconfirmed exact match to hvdic's sole genuine reading. `aliases` (blank) reconfirmed correct — no alternative forms documented. `pos: 固有名詞` and `stand_in: 宋朝` already correct — sole citer. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-4.md` (item 8) and `Lookup/Korean/Korean Name ㅅ.md`.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no component/SKIP/mc_id/level bullets) into the standard `## Notes` four-bullet format; the existing `## Words` section was already correctly formatted and untouched. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 荇 (8352; 408 characters remaining, 8351 already perfected).

### 2026-08-19, iteration 2096 — [[characters/荇|荇]]

`mc_id: 6702` reconfirmed as trusted long-tail (>4000; also confirmed absent from all four CC files). `graphemic_classification: 行` (dual-source confirmed 形声, semantic 艹 + phonetic 行) reconfirmed correct. `vietnamese: [hành, hạnh]` reconfirmed both genuine (no contamination) — hvdic confirms `hạnh` (Hán Việt) and `hành` (Nôm). Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-6.md` (item 18) and `Lookup/Korean/Korean Name ㅎ.md`.

**`stand_in` bug found and fixed — cited a nonexistent word**: stored `荇菜`, but no such word page exists anywhere in `words/` — the stand_in pointed at a word that was never created. Corrected to the `名専字` sentinel, matching current vault reality. Flagging `荇菜` ("floating-heart plant," the obvious primary compound for this character) as a candidate for a future word-creation pass.

**`aliases` filled**: was blank. En.Wiktionary's own "Alternative forms" field lists the genuine variant `莕` (no independent page); added under the established single-source-strong-statement exception.

**`joyo_level` filled**: was blank. En.Wiktionary explicitly confirms 荇 as Hyōgai kanji; added as item 457 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`hsk_level` filled**: was blank. Zero evidence anywhere (absent from every `Old HSK N.md` file and from `Lookup/HSK/HSK No.md`). Filled as `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added to `HSK No.md`.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal plant-name sense.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 寐 (8353; 407 characters remaining).

### 2026-08-19, iteration 2097 — [[characters/寐|寐]]

`mc_id: 2167` reconfirmed exact match (CC 2000.md: `2166. 轂`, `2167. 寐`, `2168. 駿`). `graphemic_classification: 未` (dual-source confirmed 形声, abbreviated semantic 㝱 + phonetic 未) reconfirmed correct. `vietnamese: [mị]` reconfirmed exact match to hvdic's sole genuine reading. `stand_in: 名専字` reconfirmed correct — zero hits for 寐 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-9.md` (item 5) and `Lookup/Korean/Korean Name ㅁ.md`.

**`aliases` filled**: was blank. zh.Wiktionary explicitly lists genuine variant forms `𥧌` and `𥧴` (neither with an independent page); added both.

**`joyo_level` filled**: was blank. en.Wiktionary explicitly confirms 寐 as Hyōgai kanji; added as item 458 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`hsk_level` filled**: was blank. Zero evidence anywhere (absent from every `Old HSK N.md` file and from `Lookup/HSK/HSK No.md`). Filled as `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added to `HSK No.md`.

**`pos` filled**: was blank. Filled as `名詞`, matching the page's own nominal gloss "deep sleep."

**Notes trivia added**: en.Wiktionary corroborates 寐's classical antonym relationship with 寤 ("to wake"); folded into the rebuilt Notes prose.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 瑟 (char) (8354; 406 characters remaining).

### 2026-08-19, iteration 2098 — [[characters/瑟 (char)|瑟 (char)]]

`mc_id: 1585` reconfirmed exact match (CC 1000.md: `1584. 筮`, `1585. 瑟`, `1586. 歡`). `graphemic_classification: 必` (dual-source confirmed 形声, semantic 珡 + phonetic 必) reconfirmed correct. `vietnamese: [sắt]` reconfirmed exact match to hvdic's sole genuine reading. `stand_in: 瑟` reconfirmed correct as sole citer (self-referential). Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-8-5.md` (item 7) and `Lookup/Korean/Korean Name ㅅ.md`.

**`japanese` completeness gap found and fixed**: stored `[SHITSU]` (kan-on only); en.Wiktionary also documents the genuine go-on `しち (SHICHI)`. Added.

**`korean_native` filled**: was blank. Confirmed via Korean Wikipedia that the instrument's Korean name is simply `슬` (no distinct native gloss, unlike 거문고/비파 for other stringed instruments); filled accordingly.

**`joyo_level` filled**: was blank. En.Wiktionary explicitly confirms 瑟 as Hyōgai kanji; added as item 459 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`hsk_level` filled**: was blank. Zero evidence anywhere (absent from every `Old HSK N.md` file and from `Lookup/HSK/HSK No.md`). Filled as `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added to `HSK No.md`.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal instrument-name sense.

**Incidental YAML bug fixed on citing word page**: [[words/瑟|瑟]]'s own `characters` field was a bare scalar (`瑟 (char)`) instead of a proper list; corrected.

**Notes trivia added**: both sources corroborate the 琴瑟相和 idiom (qin-and-se harmony, describing marital concord) and the historical pairing with 琴; folded into the rebuilt Notes prose, alongside a note flagging that the true semantic component 珡 is now conflated with the unrelated 玨 in the modern glyph.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no phono-semantic/SKIP/level bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 窈 (8355; 405 characters remaining).

### 2026-08-19, iteration 2099 — [[characters/窈|窈]]

`mc_id: 3036` reconfirmed exact match (CC 3000.md: `3035. 巔`, `3036. 窈`, `3037. 窴`). `graphemic_classification: 幼` (dual-source confirmed 形声, semantic 穴 + phonetic 幼) reconfirmed correct. `vietnamese: [yểu]` reconfirmed exact match to hvdic's sole genuine reading. `aliases` (blank) reconfirmed correct — no named variants found. `stand_in: 名専字` reconfirmed correct — zero hits for 窈 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-7.md` (item 18) and `Lookup/Korean/Korean Name ㅇ.md`.

**`羅馬字` bug found and fixed**: stored `'youso` — a corrupted/contaminated value with a stray "so" appended; the character's own syllable page `⼄ㄨ.md` confirms the genuine value is `'you` (matching the already-correct `諺文: 욧`). Corrected.

**`japanese_native` filled**: was blank (`ø`). En.Wiktionary documents three genuine kun'yomi — `くらい` (dim), `よい` (good), `あでやか` (graceful) — all representing senses of this same character rather than unrelated homograph readings (unlike the 栾 precedent where extra kun'yomi belonged to a different sense entirely). Added all three.

**`joyo_level` filled**: was blank. En.Wiktionary explicitly confirms 窈 as Hyōgai kanji; added as item 460 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`hsk_level` filled**: was blank. Zero evidence anywhere (absent from every `Old HSK N.md` file and from `Lookup/HSK/HSK No.md`). Filled as `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added to `HSK No.md`.

**`pos` filled**: was blank. Filled as `性詞`, matching the adjectival sense "graceful."

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 窕 (8356; 404 characters remaining).

### 2026-08-19, iteration 2100 — [[characters/窕|窕]]

`mc_id: 3172` reconfirmed exact match (CC 3000.md: `3171. 鄗`, `3172. 窕`, `3173. 倖`). `graphemic_classification: 兆` (dual-source confirmed 形声, semantic 穴 + phonetic 兆) reconfirmed correct. `korean_native: 으늑할` investigated and reconfirmed plausible — 으늑하다 is a genuine (if less common) Korean word meaning "quiet and secluded," matching 窕's semantic range; not force-changed absent clearer contrary evidence. `aliases` (blank) reconfirmed correct — no named variant found. `stand_in: 名専字` reconfirmed correct — zero hits for 窕 anywhere in `words/`; note that [[words/窈窕|窈窕]] itself (the character's primary real-world compound, paired with [[characters/窈|窈]] from the previous iteration) also has no word page yet — flagging alongside 荇菜 as a second candidate for a future word-creation pass. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-8.md` (item 17) and `Lookup/Korean/Korean Name ㅈ.md`.

**`japanese_native` bug found and fixed (truncated reading)**: stored `うつく` — an incomplete fragment; en.Wiktionary's genuine kun'yomi is `うつくしい (utsukushii)`. Corrected.

**`vietnamese` completeness gap found and fixed**: hvdic's genuine union is `dao`/`thiêu`/`điệu` (Hán Việt) and `điệu` (Nôm); only `điệu` was stored. Added `dao` and `thiêu`.

**`joyo_level` filled**: was blank. En.Wiktionary explicitly confirms 窕 as Hyōgai kanji; added as item 461 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`hsk_level` filled**: was blank. Zero evidence anywhere (absent from every `Old HSK N.md` file and from `Lookup/HSK/HSK No.md`). Filled as `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added to `HSK No.md`.

**`pos` filled**: was blank. Filled as `性詞`, matching the adjectival sense "elegant."

**Typo fixed in an external lookup file**: `Lookup/SKIP/SKIP-2/SKIP-2-3-8.md`'s own gloss for 窕 read "elegent"; corrected to "elegant."

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard `## Notes` four-bullet format, adding a cross-reference to the paired character 窈. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 逑 (8357; 403 characters remaining).

### 2026-08-19, iteration 2101 — [[characters/逑|逑]]

`mc_id: 5674` reconfirmed as trusted long-tail (>4000; also confirmed absent from all four CC files). `graphemic_classification: 求` (dual-source confirmed 形声, semantic 辵 + phonetic 求) reconfirmed correct. `vietnamese: [cầu]` reconfirmed exact match to hvdic's sole genuine reading. `stand_in: 名専字` reconfirmed correct — zero hits for 逑 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-3/SKIP-3-4-7.md` (item 5) and `Lookup/Korean/Korean Name ㄱ.md`.

**`japanese_native` bug found and fixed (truncated plus incomplete reading set)**: stored `つれあ` — an incomplete fragment of `つれあい` ("spouse; mate"); en.Wiktionary also documents three further genuine kun'yomi representing this character's other senses ("meet," "gather," "collect") — `あう`, `あつまる`, `あつめる`. Corrected the truncation and added all four.

**`aliases` filled**: was blank. zh.Wiktionary notes a genuine alternate form `訄` (no independent page); added.

**`joyo_level` filled**: was blank. En.Wiktionary explicitly confirms 逑 as Hyōgai kanji; added as item 462 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`hsk_level` filled**: was blank. Zero evidence anywhere (absent from every `Old HSK N.md` file and from `Lookup/HSK/HSK No.md`). Filled as `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added to `HSK No.md`.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense "mate; match."

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 芼 (8358; 402 characters remaining).

### 2026-08-19, iteration 2102 — [[characters/芼|芼]]

`mc_id: 5104` reconfirmed as trusted long-tail (>4000; also confirmed absent from all four CC files). `graphemic_classification: 毛` (dual-source confirmed 形声, semantic 艹 + phonetic 毛) reconfirmed correct. `english: [cook]` reconfirmed correct despite an initial suspicion of mismatch against `korean_native: 우거질` ("overgrown") — both sources independently confirm 芼's primary classical sense is genuinely "to cook and present," famously attested in the *Classic of Poetry*'s 荇菜 passage (a direct textual link to [[characters/荇|荇]], perfected six iterations ago); "overgrown" is a separate secondary/extended sense, not a bug. `aliases` (blank) reconfirmed correct — no named variant found. `stand_in: 名専字` reconfirmed correct — zero hits for 芼 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-4.md` (item 28) and `Lookup/Korean/Korean Name ㅁ.md`.

**`japanese_native` bug found and fixed (truncated reading)**: stored `はびこ` — an incomplete fragment; en.Wiktionary's genuine kun'yomi is `はびこる (habikoru)`. Corrected.

**`vietnamese` completeness gap found and fixed**: hvdic's genuine union is `mao`/`mạo` (Hán Việt) and `mào` (Nôm); only `mào` was stored. Added `mao` and `mạo`.

**`joyo_level` filled**: was blank. En.Wiktionary explicitly confirms 芼 as Hyōgai kanji; added as item 463 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`hsk_level` filled**: was blank. Zero evidence anywhere (absent from every `Old HSK N.md` file and from `Lookup/HSK/HSK No.md`). Filled as `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added to `HSK No.md`.

**`pos` filled**: was blank. Filled as `事詞`, matching the verbal sense "to cook and present."

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 邑 (8359; 401 characters remaining).

### 2026-08-19, iteration 2103 — [[characters/邑|邑]]

`mc_id: 343` reconfirmed exact match (CC 0000.md: `> 342. 觀`, `> 343. 邑`, `> 344. 姓`). `graphemic_classification: 會意` (dual-source confirmed 囗 over 卪, "enclosure" + "kneeling person") reconfirmed correct. `joyo_level: 日本人名用漢字` reconfirmed correct — already correctly cross-referenced at `Lookup/Japanese/Jinmeiyō.md` item 162. `hsk_level: 無` reconfirmed correct — already correctly cross-referenced at `Lookup/HSK/HSK No.md`. `aliases` (blank) reconfirmed correct — no named variant found. `stand_in: 名専字` reconfirmed correct — zero hits for 邑 anywhere in `words/` (its extensive use as a *semantic component* citation on other character pages, e.g. [[characters/邾|邾]] and [[characters/鄭|鄭]], doesn't count as a word citation). No `## Derived Characters` needed — zero character pages cite 邑 as their own `graphemic_classification` (it functions purely as radical/semantic material, never as a phonetic). Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-4.md` (item 32).

**`vietnamese` bug found and fixed — spurious extra reading**: stored `[phấp, óp, ấp, ọp, ốp]`; hvdic confirms only `ấp` (Hán Việt) and `ấp`/`óp`/`ốp`/`phấp` (Nôm) as genuine — `ọp` appears nowhere on the page, a diacritic-corrupted duplicate. Removed.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense "township."

**Missing lookup cross-reference found and fixed**: 邑 was absent from `Lookup/Korean/Korean Name ㅇ.md`'s `### 읍` section despite its `korean` reading being 읍 (only 揖 was listed); added.

**Forbidden-component citation handled per vault policy**: while writing the Notes bullet, checked `文法 - 98違法字.md` before treating the etymology's 卪 component as "pageless" — it's explicitly listed there as a permanently forbidden glyph (a Korean 구결/gugyeol annotation mark), so it was cited as plain text rather than a `[[卪]]` wikilink, which would never resolve.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no component/SKIP/mc_id/level bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 䏜 (8360; 400 characters remaining).

### 2026-08-19, iteration 2104 — [[characters/䏜|䏜]]

`mc_id: 0` reconfirmed correct (confirmed absent from all four CC files). `graphemic_classification: 及` (dual-source confirmed 形声, semantic 肉 + phonetic 及) reconfirmed correct. `mandarin: hē` / `cantonese: ho1` reconfirmed correct despite an initial suspicion of mismatch against the Vietnamese-derived `羅馬字`/`諺文`/`注音` cluster (mab/맙/ㄇㄚㄆ) — investigated and resolved: this CJK Unified Ideographs Extension A character's living use is entirely as a Vietnamese Nôm coinage for *mập/mạp* ("fat"), with the Mandarin/Cantonese readings being dictionary-only forms never in real use, explaining the `hapax` tag and justifying why the vault's own derived pronunciation follows the Vietnamese layer rather than Mandarin. `korean: 급` also reconfirmed correct — corroborated by its phonetic-series siblings (汲, 伋, 扱, all also read 급) on `Lookup/Korean/Korean Name ㄱ.md`. `stand_in: 名専字` reconfirmed correct — zero hits for 䏜 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-4-4.md` (item 36).

**`vietnamese` YAML bug found and fixed**: the first two entries (`mạp`, `mập`) had trailing `, ` sequences literally baked into the string values — closer inspection revealed the trailing character was a non-breaking space (U+00A0), not a regular space, which is why a first attempt with the Edit tool silently failed to match; fixed via a direct Python string-replace pass. Confirmed all three genuine via hvdic (`mạp, mập, mọp`, all Nôm; no Hán Việt reading exists yet).

**`english` YAML bug found and fixed**: stored as a single comma-joined string (`"plump, fat, obese"`) instead of a proper three-item list; split.

**Missing lookup cross-references found and fixed**: 䏜 was absent from both `Lookup/Japanese/Hyōgai.md` (despite genuine `表外字` status) and `Lookup/Korean/Korean Name ㄱ.md`'s `### 급` section (despite its `korean` reading being 급); added to both.

**`boundedness` filled**: was blank. Estimated `90` given the character's extreme rarity (`hapax` tag) and total absence from `words/`, flagged as a judgment call absent a formal definition.

Rebuilt the malformed `# Notes` (wrong heading level, a stray bare "Vietnamese pronunciation" fragment, two floating unlinked CC wikilinks, no SKIP/level bullets) into the standard `## Notes` four-bullet format, explicitly documenting the Nôm-vs-Mandarin reading discrepancy to prevent future misdiagnosis as a bug. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 猲 (8361; 399 characters remaining).

### 2026-08-19, iteration 2105 — [[characters/猲|猲]]

`mc_id: 5445` reconfirmed as trusted long-tail (>4000; also confirmed absent from all four CC files). `graphemic_classification: 喝` reconfirmed correct — en.Wiktionary cites the more precise phonetic root as 曷, but 曷 has no independent page in this vault, so citing 喝 (the character sharing that exact phonetic root, which does have a page) matches the established "cite what has a page" convention (cf. 鶴/隺 precedent). `joyo_level: 表外字` reconfirmed correct. `stand_in: 名専字` reconfirmed correct — zero hits for 猲 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-3-9.md` (item 67 — whose own gloss "hunting dog; growl, snarl" turned out to be the key corroborating evidence for the fix below).

**Significant polysemy/sense-mismatch bug found and fixed (`english` field)**: stored `[flame, smoke]`, but 猲 is a genuinely polysemous glyph with at least four distinct Mandarin pronunciations mapping to unrelated senses (gé "flame/smoke from fire"; hài "scent of a dog"; hè, an obsolete alt of 嚇 "frighten"; xiē, "only used in" the compounds 猲獢/猲狚). This page's own `mandarin: xiē` corresponds to the dog/wolf sense, not "flame/smoke" — confirmed decisively by: the radical (犬, "dog"), `japanese_native: おおかみ` ("wolf," matching 猲狚's own zh.Wiktionary definition "a legendary giant red wolf"), and the pre-existing SKIP-lookup gloss "hunting dog; growl, snarl" (matching 猲獢, "short-mouthed hunting dog"). Corrected `english` to `[hunting dog, growl]`, matching the SKIP page's own long-standing gloss, and documented the cross-sense conflation risk explicitly in the rebuilt Notes to prevent recurrence.

**`vietnamese` filled**: was entirely blank. hvdic lists four genuine Hán Việt readings — `cát`, `hiết`, `hạt`, `yết`; added all four (Nôm readings were not detailed on the source page).

**Missing lookup cross-references found and fixed**: 猲 was absent from both `Lookup/Japanese/Hyōgai.md` (despite genuine `表外字` status) and `Lookup/Korean/Korean Name ㄱ.md`'s `### 겁` section (despite its `korean` reading being 겁); added to both.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no phono-semantic/SKIP/level bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 漷 (8362; 398 characters remaining).

### 2026-08-19, iteration 2106 — [[characters/漷|漷]]

`mc_id: 5318` reconfirmed as trusted long-tail (>4000; also confirmed absent from all four CC files). `graphemic_classification: 郭` (dual-source confirmed 形声, semantic 水 + phonetic 郭) reconfirmed correct. `stand_in: 名専字` reconfirmed correct — zero hits for 漷 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-3-11.md` (item 26).

**`vietnamese` filled**: was entirely blank. hvdic lists one genuine Hán Việt reading, `khuếch`; added (no Nôm reading listed on the source page).

**Missing lookup cross-references found and fixed**: despite the page's own pre-existing (malformed) Notes already linking generically to `Hyōgai` and `HSK No` and explicitly flagging "Missing Korean," none of the three actually contained a genuine entry for 漷 — added it to `Lookup/Japanese/Hyōgai.md` (item 466), `Lookup/HSK/HSK No.md`, and `Lookup/Korean/Korean Name ㄱ.md`'s `### 곽` section.

Rebuilt the malformed `## Notes` (relative `../lookup/` paths instead of vault-root paths, a dash-separated bullet mixing SKIP and syllable links, generic unconfirmed lookup links, two floating unlinked CC wikilinks) into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 斡 (8363; 397 characters remaining).

### 2026-08-19, iteration 2107 — [[characters/斡|斡]]

`mc_id: 4550` reconfirmed as trusted long-tail (>4000; also confirmed absent from all four CC files). `graphemic_classification: 倝` (dual-source confirmed 形声, semantic 斗 + phonetic 倝) reconfirmed correct. `joyo_level: 日本人名用漢字` reconfirmed correct — already correctly cross-referenced at `Lookup/Japanese/Jinmeiyō.md` item 265. `hsk_level: 無` reconfirmed correct — already correctly cross-referenced at `Lookup/HSK/HSK No.md`. `aliases` (blank) reconfirmed correct — no named variant found. `stand_in: 名専字` reconfirmed correct — zero hits for 斡 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-8-6.md` (item 1) and `Lookup/Korean/Korean Name ㅇ.md`.

**`japanese_native` bug found and fixed (truncated reading)**: stored `めぐ` — an incomplete fragment; en.Wiktionary's genuine kun'yomi is `めぐる (meguru)`. Corrected.

**`vietnamese` completeness gap found and fixed**: hvdic's genuine union is `oát`/`quản` (Hán Việt) and `oát` (Nôm); only `oát` was stored. Added `quản`.

**`pos` filled**: was blank. Filled as `事詞`, matching the verbal sense "revolve; rotate."

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no phono-semantic/SKIP/level bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 佤 (8364; 396 characters remaining).

### 2026-08-19, iteration 2108 — [[characters/佤|佤]]

`mc_id: 0` reconfirmed correct (confirmed absent from all four CC files). `graphemic_classification: 瓦` (dual-source confirmed 形声, semantic 人 + phonetic 瓦) reconfirmed correct. `vietnamese: [ngoã]` reconfirmed exact match to hvdic's sole genuine reading. `stand_in: 名専字` reconfirmed correct — zero hits for 佤 anywhere in `words/` (flagging a single-character word page for "watt" as a plausible future candidate, alongside 荇菜 and 窈窕 from earlier iterations). Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-2-4.md` (item 13).

**Apparent homophone/duplication anomaly investigated and confirmed intentional, not a bug**: this page's `注音`/`羅馬字`/`諺文` (⺢ㄊ/'wad/왇) are IDENTICAL to [[characters/斡|斡]]'s values from the immediately preceding iteration, despite the two characters having completely different genuine Middle Chinese finals (麻二合 `ɣua` vs 末 `uɑt`). Investigation confirmed this is deliberate: the page's own pre-existing Notes fragment ("SI unit of power. Hence, pronunciation was altered.") explains that 佤 (genuinely "Wa/Va ethnic minority") was repurposed in Dan'a'yo as a loanword vehicle for "watt," with its reading deliberately overridden to approximate the English word rather than following its natural MC derivation — and the syllable page `syllables/⺢ㄊ.md` itself already explicitly documents both characters sharing this slot under a "Naming" category, both correctly marked `名専字`. No correction needed; reworded the Notes to make the deliberate-override reasoning explicit and cross-link to 斡, to prevent this from being misdiagnosed as a duplication bug in a future pass.

**Missing lookup cross-references found and fixed**: 佤 was absent from `Lookup/Japanese/Hyōgai.md` (despite plausible `表外字` status for such an obscure character) and from `Lookup/Korean/Korean Name ㅇ.md`'s `### 와` section (despite its `korean` reading being 와); added to both.

Rebuilt the malformed `# Notes` (wrong heading level, the stray unstructured trivia fragment, two floating unlinked CC wikilinks, no phono-semantic/SKIP/level bullets) into the standard `## Notes` four-bullet format, preserving and expanding the genuine repurposing trivia. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 腽 (8365; 395 characters remaining).

### 2026-08-19, iteration 2109 — [[characters/腽|腽]]

`mc_id: 0` reconfirmed correct (confirmed absent from all four CC files). `graphemic_classification: 昷` (dual-source confirmed 形声, semantic 月/肉 + phonetic 昷) reconfirmed correct. `joyo_level: 表外字` reconfirmed correct — en.Wiktionary explicitly cites Hyōgai. `aliases: [膃]` reconfirmed correct — en.Wiktionary explicitly confirms 膃 as a genuine variant/traditional form. `tags: [hapax, cranberry]`/`stand_in: 膃肭` reconfirmed correct — 腽 has no independent word page and is bound solely to [[words/膃肭|膃肭]] ("fur seal"), matching the cranberry pattern. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-4-10.md` (item 13) and `Lookup/Korean/Korean Name ㅇ.md`.

**`vietnamese` completeness gap found and fixed**: hvdic's genuine union is `ốt`/`ột` (Hán Việt) and `oát`/`ột` (Nôm); the stored `[oát, ột]` was missing `ốt`. Added.

**Missing lookup cross-reference found and fixed**: 腽 was absent from `Lookup/Japanese/Hyōgai.md` (despite genuine `表外字` status) and from `Lookup/HSK/HSK No.md`; added to both.

Rebuilt the malformed `# Notes` (wrong heading level, section order reversed, no SKIP/mc_id/level bullets, two floating unlinked CC wikilinks) into the standard section order and four-bullet `## Notes` format; the existing `## Words` section was already correctly formatted and untouched. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 蠖 (8366; 394 characters remaining).

### 2026-08-19, iteration 2110 — [[characters/蠖|蠖]]

`mc_id: 5243` reconfirmed as trusted long-tail (>4000; also confirmed absent from all four CC files). `graphemic_classification: 蒦` (dual-source confirmed 形声, semantic 虫 + phonetic 蒦) reconfirmed correct. `joyo_level: 表外字` reconfirmed correct. `stand_in: 尺蠖` reconfirmed correct — sole citer. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-6-13.md` (item 2).

**`vietnamese` completeness gap found and fixed**: hvdic's genuine union is `hoạch`/`oách` (Hán Việt) and `oách` (Nôm); only `oách` was stored. Added `hoạch`.

**Missing lookup cross-references found and fixed**: 蠖 was absent from `Lookup/Japanese/Hyōgai.md` (despite genuine `表外字` status), `Lookup/HSK/HSK No.md`, and `Lookup/Korean/Korean Name ㅎ.md`'s `### 확` section (despite its `korean` reading being 확); added to all three.

**Unverifiable scratch fragment dropped**: the stray "<- make at hwag" note appended to the phono-semantic bullet matched no known field or convention and couldn't be corroborated; dropped rather than propagated.

Rebuilt the malformed `## Notes` (a relative `lookup/` path instead of vault-root, a stray unverifiable fragment, no mc_id/level bullets, two floating unlinked CC wikilinks, no `## Words` section) into the standard section order and four-bullet `## Notes` format, with a new `## Words` section citing the sole genuine citer, ruby verified against its own `注音` field. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 窆 (8367; 393 characters remaining).

### 2026-08-19, iteration 2111 — [[characters/窆|窆]]

`mc_id: 4926` reconfirmed as trusted long-tail (>4000; also confirmed absent from all four CC files). `graphemic_classification: 乏` (dual-source confirmed 形声, semantic 穴 + phonetic 乏) reconfirmed correct. `vietnamese: [biếm]` reconfirmed exact match to hvdic's sole genuine reading. `aliases` (blank) reconfirmed correct — no named variant found. `stand_in: 名専字` reconfirmed correct — zero hits for 窆 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-7.md` (item 17).

**`japanese_native` bug found and fixed (truncated reading)**: stored `ほうむ` — an incomplete fragment; en.Wiktionary's genuine kun'yomi is `ほうむる (hōmuru)`, matching the "to bury" sense. Corrected.

**`joyo_level` filled**: was blank. En.Wiktionary explicitly confirms 窆 as Hyōgai kanji; added as item 470 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`hsk_level` filled**: was blank. Zero evidence anywhere (absent from every `Old HSK N.md` file and from `Lookup/HSK/HSK No.md`). Filled as `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added to `HSK No.md`.

**`hanmun_edu_level` filled**: was blank. Genuinely absent from `Lookup/Korean/Korean HS.md`; filled as `無`.

**`pos` filled**: was blank. Filled as `事詞`, matching the verbal sense "to bury; entomb."

**Missing lookup cross-reference found and fixed**: 窆 was absent from `Lookup/Korean/Korean Name ㅍ.md`'s `### 폄` section despite its `korean` reading being 폄; added.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 砭 (8368; 392 characters remaining).

### 2026-08-19, iteration 2112 — [[characters/砭|砭]]

`mc_id: 4611` reconfirmed as trusted long-tail (>4000; also confirmed absent from all four CC files). `graphemic_classification: 乏` (dual-source confirmed 形声, semantic 石 + phonetic 乏, sharing the same phonetic series as the immediately preceding character 窆) reconfirmed correct. `stand_in: 名専字` reconfirmed correct — zero hits for 砭 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-5-5.md` (item 10) — whose own gloss shared the same typo fixed below.

**`vietnamese` bug found and fixed — four spurious extra readings**: stored a 9-entry list `[biêm, bom, bàm, bãm, bìm, bơm, bẫm, bẳm, bờm]`; hvdic confirms only six as genuine — `biêm` (Hán Việt) and `bàm`/`bẳm`/`biêm`/`biìm`/`bìm`/`bơm` (Nôm). Removed the four spurious entries (`bom`, `bãm`, `bẫm`, `bờm`) and added the missing genuine `biìm`.

**`english`/gloss typo found and fixed in two places**: "accupuncture" → "acupuncture," corrected both on this page and on `Lookup/SKIP/SKIP-1/SKIP-1-5-5.md`'s matching gloss.

**`joyo_level` filled**: was blank. En.Wiktionary explicitly confirms 砭 as Hyōgai kanji; added as item 471 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`hsk_level`/`hanmun_edu_level` filled**: both blank. Zero evidence anywhere for either (absent from every `Old HSK N.md` file, `Lookup/HSK/HSK No.md`, and `Lookup/Korean/Korean HS.md`); filled both as `無`, and added 砭 to `HSK No.md`.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense "stone needle."

**Missing lookup cross-reference found and fixed**: 砭 was absent from `Lookup/Korean/Korean Name ㅍ.md`'s `### 폄` section despite its `korean` reading being 폄; added.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 杴 (8370; 391 characters remaining, 8369 already perfected).

### 2026-08-19, iteration 2113 — [[characters/杴|杴]]

`mc_id: 0` reconfirmed correct (confirmed absent from all four CC files). `graphemic_classification: 欠` (dual-source confirmed 形声, semantic 木 + phonetic 欠) reconfirmed correct. `joyo_level: 表外字` reconfirmed correct. `vietnamese: [hân]` reconfirmed exact match to hvdic's sole genuine reading. `stand_in: 名専字` reconfirmed correct — zero hits for 杴 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-4-4.md` (item 14).

**`japanese_native` YAML bug found and fixed**: was a malformed scalar+duplicate-list-item hybrid (`すき` on the key line, then a redundant `- すき` list entry below it); collapsed to the single genuine scalar.

**`aliases` filled**: was blank. zh.Wiktionary explicitly lists a simplified form (`锨`) and three variant forms (`㸝`, `檶`, `鍁`); added all four (none has an independent page).

**`joyo_level` reconfirmed correct but missing cross-reference fixed**: 杴 was absent from `Lookup/Japanese/Hyōgai.md`; added as item 472.

**`hsk_level` reconfirmed correct but evidence-basis fixed**: stored `無` was already right — zero evidence exists anywhere. Added 杴 to `HSK No.md` for consistency.

**Missing lookup cross-reference found and fixed**: 杴's own `### 험` section was entirely absent from `Lookup/Korean/Korean Name ㅎ.md` (not just missing an entry — the whole heading didn't exist), despite its `korean` reading being 험; created the section in correct alphabetical position (between `### 헐` and `### 혁`) and added the entry.

Rebuilt the malformed `## Notes` (no phono-semantic/SKIP/mc_id/level bullets, two floating unlinked CC wikilinks) into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 鵖 (8371; 390 characters remaining).

### 2026-08-19, iteration 2114 — [[characters/鵖|鵖]]

`mc_id: 8843` reconfirmed as trusted long-tail (>4000; also confirmed absent from all four CC files). `graphemic_classification: 皀` reconfirmed correct — dual-source confirms composition ⿰皀鳥 with 鳥 as the clear semantic (matching "hoopoe"), leaving 皀 as phonetic by elimination. `aliases: [𱉝]` reconfirmed correct — explicitly confirmed as the genuine simplified form. `tags: [cranberry]`/`stand_in: 鵖鴔` reconfirmed correct — confirmed transitive with [[characters/鴔|鴔]] (A=鵖, B=鴔, AB=鵖鴔, both bound to the same word). Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-7-11.md` (item 6).

**`vietnamese` filled with confirmed-absent sentinel**: was entirely blank. hvdic explicitly states no Hán Việt reading exists yet for this character ("Chưa có giải nghĩa theo âm Hán Việt") and lists no Nôm reading either; filled as `ø`, matching the established confirmed-absent convention (cf. [[characters/錀 (char)|錀 (char)]]) rather than leaving it blank/unchecked.

**Missing lookup cross-references found and fixed**: 鵖 was absent from `Lookup/Japanese/Hyōgai.md` (despite genuine `表外字` status), `Lookup/HSK/HSK No.md`, and `Lookup/Korean/Korean Name ㅍ.md`'s `### 핍` section (despite its `korean` reading being 핍); added to all three.

**`## Words` completeness gap found and fixed**: the sole genuine citer, [[words/鵖鴔|鵖鴔]] ("hoopoe"), was missing entirely; added, ruby verified against the word's own `注音` field.

Rebuilt the malformed `# Notes` (wrong heading level, no `## Words` section, two floating unlinked CC wikilinks, no phono-semantic/SKIP/level bullets) into the standard section order and four-bullet `## Notes` format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 柉 (8373; 389 characters remaining, 8372 already perfected).

### 2026-08-19, iteration 2115 — [[characters/柉|柉]]

`mc_id: 0` reconfirmed correct (confirmed absent from all four CC files). `graphemic_classification: 乏` (dual-source confirmed 形声, semantic 木 + phonetic 乏, same phonetic series as 窆/砭 from two iterations ago) reconfirmed correct. `joyo_level: 表外字` reconfirmed correct. `vietnamese: [múp, mướp, mấp, phím]` reconfirmed all four genuine (no contamination, despite an initial suspicion) — hvdic confirms all four as genuine Nôm readings and explicitly states no Hán Việt reading exists. `aliases` (blank) reconfirmed correct — no named variant found. `stand_in: 名専字` reconfirmed correct — zero hits for 柉 anywhere in `words/`.

**`english` bug found and fixed (romanization leaked into gloss)**: stored `mub` — literally the page's own `羅馬字` value, not an actual English meaning. Both sources confirm 柉's real (Vietnamese Nôm-only) meaning is "loofah" (a kind of melon/gourd) — corroborated by the pre-existing `korean_native: 나무 껍질` ("tree bark/fibrous plant material," consistent with a loofah's fibrous texture). Corrected to `loofah`. The same "mub" placeholder had also leaked into `Lookup/SKIP/SKIP-1/SKIP-1-4-5.md`'s own gloss for this character; fixed there too.

**`pos` bug found and fixed (genuine misclassification)**: stored `固有名詞` (proper noun), but "loofah" is a common plant/food noun; corrected to `名詞`.

**`boundedness` filled**: was blank. Estimated `90` given the character's extreme rarity (`hapax` tag) and total absence from `words/`, flagged as a judgment call absent a formal definition.

**Missing lookup cross-references found and fixed**: 柉 was absent from `Lookup/Japanese/Hyōgai.md` (despite genuine `表外字` status), `Lookup/HSK/HSK No.md`, and `Lookup/Korean/Korean Name ㅂ.md`'s `### 범` section (despite its `korean` reading being 범); added to all three.

Rebuilt the malformed `## Notes` (no phono-semantic/SKIP/mc_id/level bullets, two floating unlinked CC wikilinks) into the standard four-bullet format, explicitly documenting the Nôm-only nature of this character's reading to prevent future misdiagnosis. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 炢 (8374; 388 characters remaining).

### 2026-08-19, iteration 2116 — [[characters/炢|炢]]

`graphemic_classification: 朮` (dual-source confirmed 形声, semantic 火 + phonetic 术/朮) reconfirmed correct. `mc_id: 0` reconfirmed correct (confirmed absent from all four CC files). `stroke_count: 9`/`skip_number: 1-4-5` reconfirmed correct — already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-4-5.md` (item 22). `aliases` (blank) reconfirmed correct — neither en.Wiktionary nor zh.Wiktionary lists any Alternative forms/異體字. `stand_in: 名専字` reconfirmed correct — zero hits for 炢 anywhere in `words/`. Already correctly cross-listed on both `Lookup/CC/initials/聲 澄.md` and `Lookup/CC/finals/韻 術.md`.

**Severe `english`/`pos` content error found and fixed**: stored `english: [dud]` bore no resemblance to the character's actual meaning — en.Wiktionary explicitly and solely defines 炢 as "(obsolete) to produce smoke," with an Old Chinese Zhengzhang reconstruction of *l'ud specifically attributed to 炢 itself (not to its phonetic component). Corrected `english` to `[produce smoke]` and filled `pos` (was blank) as `事詞`, matching the verbal sense.

**`vietnamese` filled with confirmed-absent sentinel**: was entirely blank. hvdic explicitly states no Âm Hán Việt reading exists for this character ("Chưa có giải nghĩa theo âm Hán Việt") and lists no Âm Nôm reading either; filled as `ø`, matching the established confirmed-absent convention (cf. [[characters/錀 (char)|錀 (char)]], [[characters/鵖|鵖]]).

**`joyo_level` filled**: was blank, and neither en.Wiktionary nor ja.Wiktionary carries a Japanese-language section for 炢 (no on'yomi/kun'yomi attestation beyond the vault's own derived `SHUTSU`). Filled as `表外字` per the established fallback convention for attested-only-in-CJK-Ext-A hapax characters with a populated `japanese` field but no dictionary-confirmed jōyō/jinmeiyō status (cf. [[characters/䏜|䏜]]); added as item 473 to `Lookup/Japanese/Hyōgai.md`.

**`hsk_level` filled**: was blank. Zero evidence anywhere (absent from every `Old HSK N.md` file and from `Lookup/HSK/HSK No.md`); filled as `無`, and added 炢 to `HSK No.md`.

**`hanmun_edu_level` filled**: was blank. 炢 is absent from both `Lookup/Korean/Korean HS.md` and `Korean MS.md`, and carries no independent Korean-name attestation beyond the vault's own derived `korean`/`korean_native` fields; filled as `無` matching the established pattern for comparable unattested-in-Korean-hanja hapax characters (cf. [[characters/柉|柉]], [[characters/鵖|鵖]]). Added to `Lookup/Korean/Korean Name ㅊ.md`'s existing `### 출` section regardless (that index tracks the `korean` reading itself, independent of `hanmun_edu_level`'s HS/MS/Name/Missing classification — cf. 鵖's own precedent of a Korean Name X listing despite `hanmun_edu_level: 無`).

**`boundedness` filled**: was blank. Estimated `90` given the character's extreme rarity (`hapax` tag), obsolete-only meaning, and total absence from `words/`, flagged as a judgment call absent a formal definition.

Rebuilt the malformed Notes (two floating unlinked CC wikilinks, no heading, no bullet structure at all) into the standard `## Notes` four-bullet format, including the Old Chinese reconstructions for both 炢 itself (*l'ud) and its phonetic component 朮 (*ɦljud, Zhengzhang system) in the graphemic bullet. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 魶 (char) (8375; 387 characters remaining).

### 2026-08-19, iteration 2117 — [[characters/魶 (char)|魶 (char)]]

`graphemic_classification: 内` (dual-source confirmed 形声, semantic 魚 + phonetic 内/內, composition ⿰魚內) reconfirmed correct. `mc_id: 0` reconfirmed correct (confirmed absent from all four CC files; already correctly cross-listed on `Lookup/CC/initials/聲 泥.md` and `Lookup/CC/finals/韻 盍.md`, the latter explicitly noting 魶 as "the only n-initial character in this final"). `stroke_count: 15`/`skip_number: 1-11-4` reconfirmed correct — already cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-11-4.md` (item 8) and `Radical 195.md` (+4 strokes). `aliases: [𱇔]` reconfirmed correct — en.Wiktionary explicitly gives 𱇔 as the simplified form. `vietnamese: [ø]` reconfirmed correct — hvdic explicitly disclaims any Âm Hán Việt reading ("Chưa có giải nghĩa theo âm Hán Việt"); a stray "tháp" fragment on the same page is an unrelated placeholder, not a genuine reading. `pos: 名詞`/`stand_in: 魶` reconfirmed correct — the sole citer is the word's own independent page [[words/魶|魶]], added to a new `## Words` section.

**Cross-source variant investigated, not added**: zh.Wiktionary's own 異體字 field mutually cross-references 魶 and 鰨 ("sole/flatfish"), but en.Wiktionary's more granular sense breakdown shows this variant relationship belongs to a different, unrelated sense of 魶 ("sole") from the one Dan'a'yo uses ("giant salamander," matching `korean_native: 도롱뇽`). Not added as an alias, per the same sense-specific-homograph caution as the [[characters/鵰 (char)|鵰]]/彫 precedent — conflating unrelated senses under one glyph would misrepresent the alias relationship.

**`japanese` bug found and fixed — wrong reading entirely**: stored `[NATSU]`, which matches neither of ja.Wiktionary's two genuine on'yomi for 魶 — 呉音 ノウ and 漢音 ドウ (with historical spellings ナフ/ダフ). Corrected to `[NOU, DOU]`, romanized per the vault's own established convention (cross-checked against sibling on'yomi entries, e.g. 悩/納/脳/膿 for ノウ, 動/撞/銅 for ドウ). `japanese_native: ø` reconfirmed correct — ja.Wiktionary lists no kun'yomi.

**`joyo_level` reconfirmed correct but missing cross-reference fixed**: stored `表外字` was already right (ja.Wiktionary explicitly classifies 魶 as 表外漢字, not jōyō or jinmeiyō), but 魶 was absent from `Lookup/Japanese/Hyōgai.md`; added as item 475.

**`hsk_level` reconfirmed correct but evidence-basis fixed**: stored `無` was already right — zero evidence exists anywhere. Added 魶 (char) to `HSK No.md` for consistency.

**`hanmun_edu_level` reconfirmed correct**: stored `無` was already right — genuinely absent from `Korean HS.md`/`Korean MS.md`, and `Korean Missing.md` is a dataview auto-query keyed on `hanmun_edu_level = "無"` (no manual entry needed there). However, `Lookup/Korean/Korean Name ㄴ.md`'s `### 납` section — a general Korean-reading index independent of `hanmun_edu_level`, per the precedent from [[characters/炢|炢]] the iteration before this one — was missing 魶 despite its `korean` reading being 납; added.

**`boundedness` filled**: was blank. Estimated `90` by analogy to comparable rare, self-standing but never-compounding animal-name characters, flagged as a judgment call absent a formal definition.

Rebuilt the malformed `## Notes` (informal prose commentary instead of the graphemic bullet, a syllable link wrongly placed in the SKIP/Stroke bullet, the phono-semantic content split into its own non-standard bullet with inline ruby styling, an informal "On no one's list!" levels bullet missing three of the four required level links, and two floating unlinked CC wikilinks at the very bottom) into the standard `## Notes` four-bullet format, embedding both CC links inside the MC-rank bullet and writing out all four level links (`Grade Name`, `HSK No`, `Hyōgai`, `Korean Missing`) per the mapping table; added a `## Words` section citing [[words/魶|魶]] with ruby verified against the word's own `注音` field. The pre-existing disambiguation callout and `meta-bind-embed` placement were already correct and left untouched. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 肭 (8376; 386 characters remaining).

### 2026-08-19, iteration 2118 — [[characters/肭|肭]]

`graphemic_classification: 内` (dual-source confirmed 形声, semantic [[Radical 130|肉]] + phonetic 内, same phonetic series as its sibling [[characters/魶 (char)|魶]] from the prior iteration) reconfirmed correct. `radical: 肉` reconfirmed correct (Kangxi radical 130, matching stroke_count 8 = 4-stroke radical + 4-stroke phonetic). `mc_id: 10202` reconfirmed as trusted long-tail (>4000, per checklist policy not cross-checked against the CC 0000–3000 files). `skip_number: 1-4-4` reconfirmed correct — already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-4-4.md` (item 39). `boundedness: 5` reconfirmed correct — matches sibling [[characters/腽|腽]]'s own boundedness score for the same cranberry pairing. `stand_in: 膃肭`/`tags: cranberry` transitivity reconfirmed correct — checked sibling `characters/腽.md` (the word's actual `characters:` citer, since 膃 is itself only an alias of 腽 per the parent-form convention): it independently carries `stand_in: 膃肭` and `tags: [character, hapax, cranberry]`, already `date-last-perfect`-stamped, confirming genuine transitivity (A=腽, B=肭, AB=膃肭, both bound to the same word).

**`japanese` bug found and fixed**: stored `[DOTSU, NACHI, DATSU]`. En.Wiktionary's Readings section for 肭 explicitly lists only Go-on のち (`NOCHI`) and Kan-on どつ (`DOTSU`) as genuine on'yomi — `NACHI` is evidently a corruption of `NOCHI`, and `DATSU` has no attestation anywhere. Corrected to `[DOTSU, NOCHI]`.

**`japanese_native` bug found and fixed**: stored the confirmed-absent sentinel `ø`, but en.Wiktionary explicitly lists a genuine Kun reading こえる (`koeru`, "to grow fat") for 肭 as a Hyōgai kanji — the sentinel was wrong, not evidence-based. Corrected to `[こえる]`.

**`pos` bug found and fixed**: stored `事詞` (verbal), but 肭 is bound exclusively to the noun compound [[words/膃肭|膃肭]] ("fur seal," itself `pos: 名詞`), matching sibling 腽's own `pos: 名詞` — the isolated Teochew-dialect verbal/adjectival senses ("to cave in," "soft, tender") found on zh.Wiktionary belong to an unrelated topolect reading, not the vault's own "fur seal" sense. Corrected to `名詞`.

**`aliases` filled**: was blank. Zh.Wiktionary's own Chinese-language entry for 肭 opens with an explicit structured redirect notice: "關於「肭」的發音和釋義，請見「朒」。（此字是「朒」的異體字。）" ("For the pronunciation and meaning of 肭, see 朒. This character is a variant form of 朒.") — 朒 has no independent page in the vault. Added `朒`.

**`vietnamese` completeness gap found and fixed**: hvdic's genuine union is `nạp`/`nột` (Âm Hán Việt) and `nạp`/`nọi` (Âm Nôm); the stored `[nạp, nọi]` was missing the genuine Hán Việt reading `nột`. Added it, giving `[nạp, nột, nọi]`.

**Missing lookup cross-references found and fixed**: 肭 was absent from `Lookup/HSK/HSK No.md` (despite genuine `hsk_level: 無`), `Lookup/Japanese/Hyōgai.md` (despite genuine `joyo_level: 表外字`; added as item 476), and `Lookup/Korean/Korean Name ㄴ.md`'s `### 눌` section (despite its `korean` reading being 눌, alongside the existing 訥 entry); added to all three.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, zero bullets at all) into the standard `## Notes` four-bullet format, embedding both CC links inside the MC-rank bullet; the existing `## Words` section (citing [[words/膃肭|膃肭]], ruby already correct against the word's own `注音` field) was left untouched. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 妠 (8377; 385 characters remaining).

### 2026-08-19, iteration 2119 — [[characters/妠|妠]]

`graphemic_classification: 内` (dual-source confirmed 形声, semantic [[Radical 038|女]] + phonetic 内, both en.Wiktionary's "⿰女内" breakdown and zh.Wiktionary's own 内-series #1330 grouping agree) reconfirmed correct. `radical: 女` reconfirmed correct. `mc_id: 0` reconfirmed correct — confirmed absent from all four `Lookup/CC/CC 0000–3000.md` files. `stroke_count: 7`/`skip_number: 1-3-4` reconfirmed correct — already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-3-4.md` (item 15). `aliases` (blank) reconfirmed correct — neither source lists any variant forms. `stand_in: 名専字` reconfirmed correct — zero hits for 妠 anywhere in `words/`.

**Severe `english` content error found and fixed (romanization leak, same pattern as 柉/iteration 2115)**: stored `num` — an exact match to the page's own `羅馬字: num` value, not a real gloss. Both en.Wiktionary (Cantonese sense "to collect, seize, grab") and zh.Wiktionary agree on the genuine dialectal meaning. Corrected to `seize`; the same leaked "num" gloss had also propagated to `Lookup/SKIP/SKIP-1/SKIP-1-3-4.md`'s own entry for this character — fixed there too.

**`pos` filled**: was blank. Filled as `事詞`, matching the verbal sense "seize; grab; collect" (resolves what would otherwise have looked like a noun/verb mismatch against the corrected gloss).

**`japanese` bug found and fixed — spurious unattested reading**: stored six on'yomi `[DOU, NOU, DATSU, NACHI, DAN, NAN]`. Both en.Wiktionary and zh.Wiktionary independently list exactly five genuine on'yomi (どう/のう/だつ/なち/だん), with no `NAN` attested anywhere. Removed `NAN`, leaving `[DOU, NOU, DATSU, NACHI, DAN]`.

**`japanese_native` bug found and fixed — wrong confirmed-absent sentinel**: stored `ø`, but en.Wiktionary explicitly lists three genuine kun'yomi (めとる, いれる, とる). Corrected to `[めとる, いれる, とる]`.

**`vietnamese` filled**: was entirely blank. hvdic lists one genuine Âm Hán Việt reading, `nạp`, and no Nôm reading; filled as `[nạp]`.

**`joyo_level` filled**: was blank. En.Wiktionary explicitly confirms 妠 as Hyōgai kanji; added as item 477 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`hsk_level`/`hanmun_edu_level` filled**: both blank. Zero evidence anywhere for either (absent from every `Old HSK N.md` file, `Lookup/HSK/HSK No.md`, and `Lookup/Korean/Korean HS.md`/`Korean MS.md`); filled both as `無`, and added 妠 to `HSK No.md`.

**`boundedness` filled**: was blank. Estimated `90` by analogy to comparable hapax characters absent from `words/`, flagged as a judgment call absent a formal definition.

**Missing lookup cross-reference found and fixed**: 妠's own `### 눔` section was entirely absent from `Lookup/Korean/Korean Name ㄴ.md` (not just missing an entry — the whole heading didn't exist), despite its `korean` reading being 눔; created the section in correct alphabetical position (between `### 눌` and `### 뉴`) and added the entry.

Rebuilt the malformed `## Notes` (no phono-semantic/SKIP/mc_id/level bullets, two floating unlinked CC wikilinks) into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 潗 (8378; 384 characters remaining).

### 2026-08-19, iteration 2120 — [[characters/潗|潗]]

`graphemic_classification: 集` (dual-source confirmed 形声, semantic 水 + phonetic 集) reconfirmed correct. `english: friendly` reconfirmed correct despite an initial suspicion it might be a romanization/mistranslation artifact (matching the recent 柉/妠 leaked-羅馬字 pattern) — both en.Wiktionary and zh.Wiktionary independently give "friendly; harmonious" as 潗's genuine sense, and the vault's own pre-existing gloss on `Lookup/SKIP/SKIP-1/SKIP-1-3-12.md` (item 26) already independently corroborates it. `mc_id: 9500` reconfirmed as trusted long-tail (>4000; per policy not cross-checked against the CC 0000–3000 files). `stroke_count: 15`/`skip_number: 1-3-12` reconfirmed correct, already cross-listed there. `hanmun_edu_level: 名` reconfirmed correct — already cross-listed on `Lookup/Korean/Korean Name ㅈ.md`'s `### 집` section. `stand_in: 名専字` reconfirmed correct — zero hits for 潗 anywhere in `words/`.

**`japanese_native` bug found and fixed (truncation)**: stored bare `わ`, but en.Wiktionary's genuine kun'yomi is the full `わく` (waku) — corrected.

**`vietnamese` completeness gap found and fixed**: hvdic lists a genuine Âm Hán Việt reading `tập` (distinct from the three already-stored Âm Nôm readings `bập`/`tấp`/`tắp`, all reconfirmed genuine); added `tập`.

**`joyo_level`/`hsk_level` filled**: both blank. En.Wiktionary confirms real attested on'yomi/kun'yomi (しゅう/わく) with no listing on any jōyō/jinmeiyō list; filled `joyo_level: 表外字` and added 潗 as item 478 to `Lookup/Japanese/Hyōgai.md`. Zero evidence anywhere for `hsk_level` (absent from every `Old HSK N.md` file and `Lookup/HSK/HSK No.md`); filled `無` and added to `HSK No.md`.

**`pos` filled**: was blank. Filled as `性詞`, matching the adjectival sense "friendly; harmonious."

**`aliases` investigated, left blank**: zh.Wiktionary's own 異體字 field names `淁` as a variant, but en.Wiktionary carries no corroborating "Alternative forms" entry — single-source only, so per the dual-source convention this was not added.

**Cantonese romanization flagged, not changed**: en.Wiktionary's own Jyutping is `zap1`, differing from the page's stored `cap1` (unaspirated vs. aspirated initial) — noted as a discrepancy worth a future look, but left as-is this iteration since no second source was checked to arbitrate and it fell outside this iteration's core scope.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no bullet structure at all) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 湆 (8379; 383 characters remaining).

### 2026-08-19, iteration 2121 — [[characters/湆|湆]]

`mc_id: 3922` reconfirmed exact match (CC 3000.md: `3921. 翬`, `3922. 湆`, `3923. 盼`). `graphemic_classification: 音` (dual-source confirmed 形声, semantic 水 + phonetic 音) reconfirmed correct. `aliases: [湇]` reconfirmed correct (dual-source confirmed genuine variant meaning "broth"; en.Wiktionary's further-listed 𣲷 was investigated and excluded — it carries only an unrelated Cantonese slang sense "sticky," not dual-source confirmed as a variant of this sense). `joyo_level: 表外字` reconfirmed correct — en.Wiktionary confirms Hyōgai status; added as item 479 to `Lookup/Japanese/Hyōgai.md` (which it was missing from). `hsk_level: 無` reconfirmed correct — zero evidence anywhere; added to `Lookup/HSK/HSK No.md` (also missing). `hanmun_edu_level: 無` reconfirmed correct — genuinely absent from `Lookup/Korean/Korean HS.md`/`Korean MS.md`. `stand_in: 名専字` reconfirmed correct — zero hits for 湆 anywhere in `words/`. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-3-9.md` (item 55, gloss "broth, soup liquid").

**Apparent `english`/`korean_native` mismatch investigated, resolved as two genuine senses, not a bug**: `korean_native: 축축해질` ("will become damp") looked disconnected from `english: broth`, but both en.Wiktionary and zh.Wiktionary independently confirm 湆 carries exactly these two senses — "dark and moist" and "meat broth/stock." Added `damp` as a second `english` gloss alongside the pre-existing `broth` rather than treating either as wrong; the Notes prose now explicitly documents both senses to prevent future misdiagnosis. `pos` filled as `名詞`, matching the primary/first-listed "broth" sense.

**`vietnamese` completeness gap found and fixed**: hvdic lists a genuine Âm Hán Việt reading, `khấp`, entirely missing alongside the already-correct Âm Nôm `ùm`. Added.

**`boundedness` filled**: was blank. Estimated `90` by analogy to comparable zero-citation hapax characters.

**Missing lookup cross-reference found and fixed**: 湆 was absent from `Lookup/Korean/Korean Name ㅇ.md`'s `### 읍` section despite its `korean` reading being 읍; added.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no bullet structure at all) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 翕 (8380; 382 characters remaining).

### 2026-08-19, iteration 2122 — [[characters/翕|翕]]

`mc_id: 2010` reconfirmed exact match (CC 2000.md: `2009. 欬`, `2010. 翕`, `2011. 饋`). `vietnamese: [hấp]` reconfirmed complete — en.Wiktionary's Vietnamese section lists only the single Hán Nôm reading `hấp`. `hanmun_edu_level: 名` reconfirmed correct — already correctly cross-listed on `Lookup/Korean/Korean Name ㅎ.md`'s `### 흡` section. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-2-10.md` (item 4). `pos: 性詞` and `boundedness: 80` already correct.

**`graphemic_classification` bullet bug found and fixed (semantic/phonetic roles swapped, wrong gloss)**: the page's malformed prose bullet labeled `合` as the *semantic* component with the gloss "wings" — but 合 means "close/combine/unite," not "wings." Both en.Wiktionary and zh.Wiktionary confirm the true composition is semantic [[Radical 124|羽]] ("wings," also the page's own `radical` value) + phonetic `合` (OC *kuːb, *ɡuːb) — matching the frontmatter's own `graphemic_classification: 合`, which was already correct; only the malformed bullet's prose had the roles and gloss backwards. Rewrote the bullet correctly, radical-linking 羽 per convention.

**`aliases` false-positive avoided**: zh.Wiktionary lists a broad 異體字 set (扱/翖/𦐬/噏/歙/𪴱/㒆 etc.) under a shared phonetic series, but en.Wiktionary's Etymology 1 (the sense Dan'a'yo uses) carries no "Alternative forms" field at all — insufficient dual-source corroboration. Left blank.

**`japanese`/`japanese_native` bug found and fixed (truncation)**: stored `japanese: [KYUU]` was missing a second genuine on'yomi — en.Wiktionary confirms go-on `こう` (KOU) alongside kan-on `きゅう` (KYUU); added `KOU`. `japanese_native: あ` was a truncated kun-yomi — the genuine reading is `あう` (au); corrected to `[あう]` (the nanori reading さかり was not added, consistent with the vault's on/kun-only convention).

**`english` completeness gap found and fixed**: stored `agreeable` (matching en.Wiktionary's "friendly; compliant" and zh.Wiktionary's "united, harmonious") reflected only the primary sense. zh.Wiktionary's secondary sense "draw in; inhale" corroborates the page's own `korean_native: 모일` ("to gather"), which the single existing gloss didn't cover. Added `gather` as a second gloss.

**`stand_in: 名専字` reconfirmed correct** — zero hits for 翕 anywhere in `words/`. **`## Derived Characters` checked, none needed** — no other vault character names 翕 as its `graphemic_classification`.

**Missing lookup cross-references found and fixed**: 翕 was absent from `Lookup/Japanese/Hyōgai.md` (despite genuine `表外字` status) and `Lookup/HSK/HSK No.md` (despite genuine `hsk_level: 無`); added to both (Hyōgai item 480).

Collapsed the doubled `## Notes` header (the first containing only floating CC links, the second containing the malformed composition bullet) into a single standard four-bullet format. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 歆 (8381; 381 characters remaining).

### 2026-08-19, iteration 2123 — [[characters/歆|歆]]

`graphemic_classification: 音` (dual-source confirmed 形声, semantic [[Radical 076|欠]] "to exhale/yawn" + phonetic 音, itself Kangxi Radical 180 — the checklist's radical-linking rule applies to phonetic components too, so both get `[[Radical NNN|char]]` treatment) reconfirmed correct against the frontmatter's own `radical: 欠`. `mc_id: 1498` reconfirmed exact match (CC 1000.md: `1497. 霜`, `1498. 歆`, `1499. 蕩`). `hanmun_edu_level: 名` reconfirmed correct — already correctly cross-listed on `Lookup/Korean/Korean Name ㅎ.md`'s `### 흠` section. `joyo_level: 表外字` reconfirmed correct — already correctly cross-listed on `Lookup/Japanese/Hyōgai.md` (item 175). `stroke_count`/`skip_number` reconfirmed correct — already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-9-4.md` (item 11) and on `Lookup/Radicals/Radical 076.md` (item 8, under its own `radical: 欠` assignment).

**Open editorial question resolved, not carried forward**: a prior editor's stray Notes bullet asked "Korean dictionaries list the meaning as 歆饗. Is it not a 名専字?" — grepped all of `words/*.md` for any citation of 歆 (including a possible `歆饗` compound); zero hits anywhere. No such word page exists, so `stand_in: 名専字` is confirmed genuinely correct; the open question is resolved (not a 名専字-tagging bug) and dropped rather than carried forward as unresolved ambiguity.

**`japanese_native` YAML bug found and fixed**: was a malformed scalar+stray-list-item hybrid (`う` on the key line, a separate `- うける` list item below it). ja.Wiktionary/hvdic both confirm the sole genuine kun'yomi is うける; the bare `う` was truncation garbage. Corrected to the single proper list item `[うける]`.

**`vietnamese` completeness gap found and fixed**: hvdic's page lists the sole Âm Hán Việt reading `hâm` (already stored) alongside five further genuine Âm Nôm spellings — `ham`, `hăm`, `hom`, `hôm`, `hum` — none previously stored. Added all five, matching the established completeness convention of storing the full genuine union.

**`english` gap filled**: hvdic/en.Wiktionary's definitions center on "to receive a sacrificial offering's fragrance with pleasure," extended to "admire, be moved, submit willingly" — the existing `be pleased` gloss was accurate but incomplete; added `enjoy (an offering)` as a second gloss to capture the core ritual sense reflected in `korean_native: 흠향할`.

**`aliases` key added (was entirely absent from frontmatter)**: investigated zh.Wiktionary's phonetic-series grouping (which lists 歆 alongside 噷/嬜) — these are phonetic-series co-occurrences only, not genuine variant forms of 歆 itself; no dual-source-confirmed alias found. Added the key as blank for schema consistency with other pages.

**Missing lookup cross-reference found and fixed**: 歆 was absent from `Lookup/HSK/HSK No.md` despite genuine `hsk_level: 無`; added.

Rebuilt the malformed Notes (an informal open question instead of the graphemic bullet, a run-on second bullet mixing composition/SKIP/stroke/syllable into one line with bare non-resolving wikilinks, an informal third bullet with "No HSK" prose instead of a real link, floating CC initial/final wikilinks at the bottom) into the standard `## Notes` four-bullet format, with the CC links embedded in bullet 3. Stamped `date-last-perfect: 2026-08-19`.

Next never-perfected character by `danayo_id`: 偪 (8382; 380 characters remaining).

### 2026-08-19, iteration 2124 — [[characters/偪|偪]]

**`english`/`pos` bug found and fixed (genuine misclassification)**: stored `english: Fuyang` and blank `pos` — but "Fuyang" is only the meaning of the bound compound [[偪陽]] (an ancient place name), not the character's own standalone sense. Both en.Wiktionary and zh.Wiktionary independently confirm 偪's real standalone meaning is as a variant form of [[逼]] ("to press, urge, compel"), matching the page's own `korean_native: 핍박할` ("to oppress/persecute"). Corrected `english` to `[press, compel]` and filled `pos: 事詞`, matching 逼's own precedent (`pos: 事詞`, `english: [compel, force, pressure]`); moved the "Fuyang" sense into the `## Words` section where it belongs, citing the bound compound.

`graphemic_classification: 畐` reconfirmed correct (dual-source: semantic [[Radical 009|人]] + phonetic 畐). `mc_id: 2667` reconfirmed exact match (CC 2000.md: `2666. 韶`, `2667. 偪`, `2668. 題`). `stand_in: 偪陽` reconfirmed correct — sole citer, [[words/偪陽|偪陽]], already correctly cited (moved from a stranded Notes bullet into a proper `## Words` section); its odd ruby `ㄆㄧㄆ·⼘ㄫ` (with a mid-dot separator) verified genuine against the word's own `注音` field, not a formatting error. `boundedness: 75` reconfirmed correct.

**`japanese` bug found and fixed**: stored `HIYOKU` — a corrupted romanization of ひょく (a small-y-glide syllable, which the vault's own convention romanizes as `HYOKU`, confirmed by cross-checking sibling character [[逼]]'s own `japanese: [HITSU, HYOKU]`). Corrected to `HYOKU`; `HIKI`/`FUKU` reconfirmed genuine against dual sources.

**`japanese_native` bug found and fixed**: stored truncated bare scalar `せま`, not a real reading. Dual sources confirm genuine kun'yomi せまる ("to press/narrow," verbal, matching the corrected `pos`) and せまい ("narrow," adjectival); corrected to the list `[せまる, せまい]`. A third kun'yomi むかばき ("leg wrap") belongs to an unrelated etymological sense (historical variant of 幅) and was not added.

**`vietnamese` bug found and fixed — contamination plus completeness gap**: stored `[bậc, bức, bực]`; hvdic's genuine union is `bức`/`phúc` (Hán Việt) and `bậc`/`bức` (Nôm). `bực` matches no genuine reading (an unrelated common word meaning "annoyed/story," not a real reading of 偪) — removed; missing genuine `phúc` added. Corrected to `[bậc, bức, phúc]`.

**`joyo_level`/`hsk_level`/`hanmun_edu_level` filled**: all three were blank. Filled `joyo_level: 表外字` (added as item 481 to `Lookup/Japanese/Hyōgai.md`), `hsk_level: 無` (added to `Lookup/HSK/HSK No.md`), and `hanmun_edu_level: 名` (already correctly documented via its Sino-Korean reading 핍; added to `Lookup/Korean/Korean Name ㅍ.md`'s `### 핍` section, matching sibling 逼's own `名` designation).

**Sibling-page bug found and fixed**: `characters/畐.md`'s own `aliases` field listed `偪` as an alias — but 偪 has a full independent page with its own senses, frontmatter, and citing word, violating the vault's alias convention ("a character listed as another's alias is never used independently"). Removed 偪 from 畐's aliases. Also updated the now-stale "Fuyang" gloss on two pages that cite 偪 by its old meaning: `characters/福 (char).md`'s `## Derived Characters` entry and `Lookup/SKIP/SKIP-1/SKIP-1-2-9.md`'s numbered list entry, both corrected to "press; compel."

Rebuilt the malformed `# Notes` (wrong heading level, floating unlinked CC wikilinks, a `## Words`-style bullet stranded inside Notes) into the standard `## Notes` four-bullet format plus a proper `## Words` section. Stamped `date-last-perfect: 2026-08-19`.

### 2026-08-20, iteration 2125 — [[characters/堵|堵]]

**`english`/`pos` bug found and fixed (severe content error)**: stored `english: [stifled, suffocated]` and blank `pos`, but this is only 堵's most marginal sense (the 5th of ~8 listed on en.Wiktionary). The page's own `korean_native: 담` ("wall") and `radical: 土` ("earth") point clearly to 堵's central meaning, "wall" — confirmed by both en.Wiktionary (sense 2, "wall (literary)") and hvdic ("a wall or partition"), and matching the vault's own pre-existing gloss on `Lookup/SKIP/SKIP-1/SKIP-1-3-8.md` item 14 ("wall; block, stop up"), which the character page itself had never been brought into agreement with. Corrected `english` to `[wall, block]` and filled `pos: 名詞`.

`graphemic_classification: 者` (dual-source confirmed 形声, semantic 土 + phonetic 者) reconfirmed correct. `mc_id: 2949` reconfirmed exact match (CC 2000.md: `2948. 扇`, `2949. 堵`, `2950. 錐`). `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 432. `hanmun_edu_level: 名` reconfirmed correct — already correctly cross-listed on `Lookup/Korean/Korean Name ㄷ.md`'s `### 도` section. `vietnamese: [đổ]` reconfirmed exact match — hvdic confirms đổ as both the genuine Hán Việt and Nôm reading (not contamination from the common unrelated word "đổ," despite that word's high frequency). `stand_in: 名専字` reconfirmed correct — zero hits for 堵 anywhere in `words/`. `aliases` (blank) reconfirmed correct — no genuine dual-source variant found. `boundedness: 90` reconfirmed correct.

**`japanese_native` YAML bug found and fixed**: `かき` was a bare scalar instead of a proper list; corrected to `[かき]` (genuine kun'yomi, "fence," consistent with the "wall" sense).

**`hsk_level` bug found and fixed**: stored `2`, traced only to colon-count frequency entries in `Old HSK 2.md` and `Old HSK 4.md` (neither genuine). Zero genuine plain-numbered entry exists in any `Old HSK N.md` file, and 堵 was absent from `Lookup/HSK/HSK No.md`. Corrected to `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added 堵 to `HSK No.md`.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 閔 (8384; 378 characters remaining).

### 2026-08-20, iteration 2126 — [[characters/閔|閔]]

**`english`/`pos` bug found and fixed (genuine misclassification)**: stored `english: [urge, incite]` and blank `pos` — but both en.Wiktionary and zh.Wiktionary confirm 閔's real central sense is "to grieve, pity, sympathize" (a near-synonym/variant relationship with the independently-paged [[characters/憫 (char)|憫]], not added as an alias per the parent-page convention since 憫 has its own full page), extended to a surname (e.g. Confucius's disciple 閔子騫), matching the page's own `korean_native: 근심할` ("to worry/grieve"). Corrected `english` to `[grieve, pity]` and filled `pos: 事詞`. The stale "urge, incite" gloss had also propagated to two lookup pages — `syllables/ㄇㄧㄇ.md` and `Lookup/SKIP/SKIP-3/SKIP-3-8-4.md` (item 6) — both corrected in place.

`graphemic_classification: 文` reconfirmed correct (dual-source: semantic [[Radical 169|門]] + phonetic 文). `mc_id: 1488` reconfirmed exact match (CC 1000.md: `1487. 裘`, `1488. 閔`, `1489. 央`). `aliases: [闵]` reconfirmed correct (genuine simplified form). `hsk_level: 無` reconfirmed correct — already present on `Lookup/HSK/HSK No.md`. `hanmun_edu_level: 名` reconfirmed correct — already correctly cross-listed on `Lookup/Korean/Korean Name ㅁ.md`'s `### 민` section. `stand_in: 名専字` reconfirmed correct — zero hits for 閔 anywhere in `words/`. `boundedness: 65` left as-is (a plausible judgment-call value within the range used for comparable 名専字 hapax characters this session).

**Stray note "Pronunciation altered to fill a blank syllable" investigated and preserved, not dropped**: confirmed genuine — `syllables/ㄇㄧㄇ.md` explicitly states the syllable "does not have intrinsic meaning" and hosts only this one character under its `### Naming` section, matching the vault's syllable-placement-override convention (a character deliberately assigned to an otherwise-empty syllable slot rather than by strict phonological derivation). Folded into the rebuilt MC/phonology bullet's prose rather than left as a fifth stray bullet.

**`japanese_native` bug found and fixed (truncation)**: stored bare `あわ`, not a real reading. Both sources confirm genuine kun'yomi `あわれむ` ("to pity") and `うれえる` ("to grieve"); corrected to the list `[あわれむ, うれえる]`.

**`vietnamese` bug found and fixed (diacritic corruption)**: stored `mẩn` (hỏi tone) doesn't match hvdic's genuine sole Âm Hán Việt reading `mẫn` (ngã tone) — corrected.

**`joyo_level` filled**: was blank. En.Wiktionary explicitly confirms 閔 as Hyōgai kanji; added as item 482 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

Rebuilt the malformed Notes (one genuine graphemic bullet, one stray informal note, floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 鱏 (char) (8385; 377 characters remaining).

### 2026-08-20, iteration 2127 — [[characters/鱏 (char)|鱏 (char)]]

**Alias-list conflation investigated, kept as-is (not a bug)**: the four-item `aliases: [𱈓, 鱘, 鱝, 鰩]` initially looked like it might mix two unrelated fish senses, but both en.Wiktionary and zh.Wiktionary independently confirm 鱏 genuinely carries two dual-source-attested senses — "sturgeon" in Chinese/Korean usage (matching `korean_native: 심어` and Mandarin xún; aliases 鱘/𱈓 belong here) and "ray/eagle ray" in Japanese usage (matching kun'yomi えい; aliases 鱝/鰩 belong here). `english: [ray, skate]` reconfirmed correct — it matches the Dan'a'yo word's own stored gloss at [[words/鱏|鱏]], which deliberately draws on the Japanese sense rather than the Chinese "sturgeon" sense; both senses documented in the rebuilt graphemic bullet rather than silently dropping the sturgeon sense. `graphemic_classification: 覃` reconfirmed correct (dual-source: semantic [[Radical 195|魚]] + phonetic 覃). `mc_id: 8432` reconfirmed as trusted long-tail (>4000; also confirmed absent from all four CC files). `vietnamese: [tầm]` reconfirmed exact match to hvdic's sole genuine reading. `stand_in: 鱏` reconfirmed correct — sole citer, the word's own independent page; ruby verified against the word's own `注音` field. Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-11-12.md`.

**`japanese: [SHIN, JIN, IN]` reconfirmed correct**: ja.Wiktionary independently confirms all three on'yomi (呉音 ジン/イン, 漢音 シン/イン). **`japanese_native: えい` reconfirmed correct** — sole genuine kun'yomi.

**`joyo_level`/`hsk_level`/`hanmun_edu_level` filled**: all three were blank. Filled `joyo_level: 表外字` (ja.Wiktionary explicitly confirms Hyōgai; added as item 483 to `Lookup/Japanese/Hyōgai.md`), `hsk_level: 無` (zero evidence anywhere; added to `Lookup/HSK/HSK No.md`), `hanmun_edu_level: 名` (added to `Lookup/Korean/Korean Name ㅅ.md`'s `### 심` section, absent despite the korean reading being 심).

**`boundedness` filled**: was blank. Estimated `90` by analogy to comparable hapax bound-word characters.

Rebuilt the malformed `## Notes` (two floating unlinked CC wikilinks, no bullet structure at all, no `## Words` section) into the standard four-bullet format plus a `## Words` section citing [[words/鱏|鱏]]. Stamped `date-last-perfect: 2026-08-20`.

### 2026-08-20, iteration 2128 — [[characters/姂|姂]]

**`japanese` bug found and fixed (fabricated on'yomi)**: stored `[BUTSU, FUTSU]` matched neither ja.Wiktionary (no page exists for 姂 at all) nor en.Wiktionary (explicitly states "no Japanese on'yomi or kun'yomi readings" for this character), and bore no resemblance to the phonetic component's own reading. The vault's own established convention for phonetic-inherited on'yomi on otherwise-unattested characters (cf. [[characters/潗|潗]] inheriting [[集]]'s SHUU) points to the phonetic component [[乏]]'s own vault page, which stores `japanese: [BOU]` — corrected 姂 to match, `[BOU]`.

**`vietnamese` completeness gap found and fixed — source correction**: en.Wiktionary claimed a Hán Việt reading `phạp`, but hvdic (this vault's trusted primary source) explicitly states no Hán Việt reading exists ("Chưa có giải nghĩa theo âm Hán Việt") and instead lists `phạp` as a second genuine **Nôm** reading alongside the already-stored `bợm`. Added `phạp` to the list, corrected as Nôm not Hán Việt (no separate frontmatter distinction needed, but noted for the record).

`graphemic_classification: 乏` reconfirmed correct — dual-source (en.Wiktionary + zh.Wiktionary) confirms composition ⿰女乏, semantic 女 + phonetic 乏; both share Zhengzhang OC *bob, corroborating the phonetic link. `mc_id: 0` reconfirmed correct (hvdic independently notes 姂 has "rất thấp," very low, corpus frequency). `stroke_count`/`skip_number` reconfirmed correct — already cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-3-5.md` (item 11). `pos: 性詞` and `english: beautiful quiet (of a woman)` reconfirmed correct, matching `korean_native: 예쁠` and both dictionary sources' primary sense (one of three distinct senses attested for this glyph; the other two, corresponding to different MC readings, were not adopted). `aliases` (blank) reconfirmed correct — neither source lists a variant. `stand_in: 名専字` reconfirmed correct — zero hits for 姂 anywhere in `words/`.

**`boundedness` filled**: was blank. Estimated `90` by analogy to comparable hapax characters absent from `words/`.

**Missing lookup cross-references found and fixed**: 姂 was absent from `Lookup/Japanese/Hyōgai.md` (despite genuine `joyo_level: 表外字`) and `Lookup/HSK/HSK No.md` (despite genuine `hsk_level: 無`); added as item 484 to the former. `hanmun_edu_level: 無` is correctly picked up automatically by `Lookup/Korean/Korean Missing.md`'s dataview query — no manual list edit needed there.

Rebuilt the malformed Notes (a correct-but-incomplete graphemic bullet with empty `(OC )` placeholders, two floating unlinked CC wikilinks, no SKIP/MC-rank/levels bullets) into the standard `## Notes` four-bullet format, filling in the real OC reconstructions. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 𦚖 (8387; 375 characters remaining).

### 2026-08-20, iteration 2129 — [[characters/𦚖|𦚖]]

**YAML bug found and fixed**: `vietnamese` had a literal trailing comma baked into the first list item (`mập,` instead of `mập`), a transcription artifact. `graphemic_classification: 乏` (dual-source confirmed, semantic [[Radical 130|肉]] + phonetic 乏, matching the same OC *bob phonetic series as [[姂]] from the immediately prior iteration) reconfirmed correct. `mc_id: 0` reconfirmed correct — confirmed absent from all four Classical Chinese frequency files. `stroke_count: 8`/`skip_number: 1-4-4` reconfirmed correct against the existing SKIP-1-4-4 cross-listing (item 41). `stand_in: 名専字` reconfirmed correct — zero hits for 𦚖 anywhere in `words/`.

**`vietnamese` completeness gap found and fixed**: hvdic's genuine Nôm union is `bẫm, mạp, mập, míp, móp, mụp` (no Hán Việt reading exists); only `mập`/`móp` were stored. Corrected to the full six-item list.

**`aliases: [眨]` investigated, kept as genuine**: en.Wiktionary/zh.Wiktionary don't explicitly label 𦚖 a variant of 眨, but this vault's own `Lookup/HSK/Old HSK 6.md` (entry `646. [眨](../../characters/𦚖.md)`) already routes 眨's real HSK-6 citation to this very page — confirming 𦚖 genuinely serves as 眨's stand-in page in this vault (眨 has no independent page of its own), the same sibling-glyph convention seen with [[characters/鵰 (char)|鵰 (char)]]/雕 earlier this session. This also confirms `hsk_level: "6"` is genuine, not a fabrication, and explains why it looked suspicious in isolation for such an obscure glyph.

**`mandarin` bug found and fixed (tone error)**: stored `zhá` (2nd tone) matched neither 𦚖's own unattested Mandarin reading (none found in either source) nor 眨's real modern Mandarin reading `zhǎ` (3rd tone, per the confirmed sibling-glyph relationship above); corrected to `zhǎ`.

**`japanese` bug found and fixed (fabrication, same pattern as [[姂]] last iteration)**: stored `[BUTSU]` matched no dictionary source. Since no genuine on'yomi is attested for this rare glyph, corrected to `[BOU]`, inherited from the phonetic component 乏's own vault page, matching the established phonetic-inheritance convention used on 姂 in the immediately prior iteration.

**`pos` bug found and fixed**: stored `性詞` (stative/adjectival), but "to wink" (per `english: wink` and the verbal `korean_native: 깜작일`) is a dynamic action, not a description. Corrected to `事詞`.

**`joyo_level`/`hanmun_edu_level` filled**: both blank. Filled `joyo_level: 表外字` (added as item 485 to `Lookup/Japanese/Hyōgai.md`) and `hanmun_edu_level: 無` (absent from every Korean HS/MS/Name list; `Lookup/Korean/Korean Missing.md`'s dataview query picks it up automatically, no manual edit needed).

**`boundedness` filled**: was blank. Estimated `90` (hapax, zero citing words).

Rebuilt the malformed Notes (a stray unlinked "Vietnamese pronunciation" fragment — folded into bullet 1's prose explaining the character's Vietnamese-only attestation — floating unlinked CC wikilinks, no bullet structure) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 姏 (8388; 374 characters remaining).

### 2026-08-20, iteration 2130 — [[characters/姏|姏]]

**`english` bug found and fixed (genuine misclassification)**: stored `greatgrandmother`, but both en.Wiktionary and zh.Wiktionary independently give the single definition "old woman" for 姏 — no source supports "great-grandmother" specifically. Corrected to `old woman`; propagated the same fix to the two other pages citing the stale gloss, `Lookup/SKIP/SKIP-1/SKIP-1-3-5.md` (item 14) and `characters/甘 (char).md`'s own `## Derived Characters` entry.

**`japanese`/`japanese_native` bug found and fixed — not fabrication this time, genuinely dual-sourced**: unlike 姂/𦚖 earlier this session, all four stored on'yomi (`BAN, MAN, KAN, KON`) are independently confirmed genuine (unclassified) readings on both en.Wiktionary and zh.Wiktionary — left as-is. `japanese_native: ø` was wrong, however: both sources also list a genuine kun'yomi ばば ("baba," matching "old woman"), entirely missing from the page; corrected to `[ばば]`.

**`vietnamese` filled**: was entirely blank. hvdic gives one genuine Âm Hán Việt reading, `kiềm`; no Nôm reading exists. Added.

`graphemic_classification: 甘` reconfirmed correct (dual-source: semantic [[Radical 038|女]] + phonetic 甘; already correctly cross-listed in `甘 (char).md`'s own `## Derived Characters`). `mc_id: 0` reconfirmed correct (confirmed absent from all four CC files). `stroke_count`/`skip_number` reconfirmed correct — already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-3-5.md` (item 14). `aliases` (blank) reconfirmed correct — no genuine dual-source variant found. `stand_in: 名専字` reconfirmed correct — zero hits for 姏 anywhere in `words/`. `joyo_level: 表外字`/`hsk_level: 無`/`hanmun_edu_level: 無` all reconfirmed correct; added to `Lookup/Japanese/Hyōgai.md` (item 486) and `Lookup/HSK/HSK No.md`, both previously missing it.

**`boundedness` filled**: was blank. Estimated `90` (hapax, zero citing words).

Rebuilt the malformed Notes (floating unlinked CC wikilinks, no bullet structure) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 㽉 (8389; 373 characters remaining).

### 2026-08-20, iteration 2131 — [[characters/㽉|㽉]]

`graphemic_classification: 監` reconfirmed correct — dual-source: en.Wiktionary's structural breakdown ("Kangxi radical 98, 瓦+14") plus zh.Wiktionary's placement of 㽉 within the variant cluster of 鑑 (which itself is built on phonetic 監), independently corroborated by the vault's own `characters/監.md` page, which already correctly lists 㽉 under its own `## Derived Characters`. `mc_id: 0` reconfirmed correct — genuinely absent from all Classical Chinese frequency data; also independently corroborated by `Lookup/CC/finals/韻 銜.md`'s own prose noting 㽉 "dodges via vowel-shift, landing alone on ㄛㄇ." `english: [big jar, big basin]` reconfirmed correct — both en.Wiktionary's definition and the Unihan `kDefinition` field ("a big jar; a big basin") independently confirm this, distinct from the unrelated `鑑` ("mirror, to reflect") sense zh.Wiktionary groups it near. `stroke_count`/`skip_number` reconfirmed correct — already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-14-5.md` (item 2, gloss "jar"). `aliases` (blank) reconfirmed correct — no genuine direct variant found beyond the broader unrelated 監-phonetic cluster. `stand_in: 名専字` reconfirmed correct — zero hits for 㽉 anywhere in `words/`.

**`japanese` bug found and fixed (fabrication)**: stored `SHIN` matched no dictionary source and doesn't fit the phonetic-inheritance pattern seen elsewhere in this session (e.g. 姂/𦚖 inheriting from 乏). The Unihan `kJapanese` field explicitly gives カン・ガン (matching 監's own genuine on'yomi `KAN`, plus its voiced counterpart). Corrected to `[KAN, GAN]`.

**`vietnamese` bug found and fixed (fabrication)**: stored `hạm` — but hvdic explicitly states "Chưa có giải nghĩa theo âm Hán Việt" (no Hán Việt reading yet) and lists no Nôm reading either, only Cantonese `gam3`/`ham3`. Corrected to the confirmed-absent sentinel `ø`.

**`joyo_level`/`hsk_level`/`hanmun_edu_level` filled**: all three were blank. Filled `joyo_level: 表外字` (per the genuine Unihan-attested on'yomi, added as item 487 to `Lookup/Japanese/Hyōgai.md`), `hsk_level: 無` (zero evidence anywhere; added to `HSK No.md`), and `hanmun_edu_level: 無` (absent from Korean HS/MS/Name lists — `Korean Name ㅎ.md`'s own `### 함` section does not include it).

**`boundedness` filled**: was blank. Estimated `90` (hapax, zero citing words).

Rebuilt the malformed Notes (floating unlinked CC wikilinks, no bullet structure) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 䝙 (8390; 372 characters remaining).

### 2026-08-20, iteration 2132 — [[characters/䝙|䝙]]

`graphemic_classification: 区` reconfirmed correct — both en.Wiktionary and zh.Wiktionary confirm 䝙 is the simplified form of traditional 貙 (composition ⿰豸区), matching the vault's precedent of citing the simplified sibling's phonetic when only that page exists (貙 has no independent page and is correctly recorded as an alias). `mc_id: 4082` reconfirmed as trusted long-tail (just above 4000, per policy not cross-checked against `Lookup/CC/CC 0000–3000.md`). `english: mythical tiger-beast` reconfirmed correct — Unihan's `kDefinition` ("a kind of animal like a tiger; fierce wild beasts") and hvdic's Từ điển Nguyễn Quốc Hùng gloss ("a person transformed into a tiger") both independently support the "mythical" framing; `korean_native: 스라소니` ("lynx") is not a contradiction but a second genuine gloss — en.Wiktionary's own Korean-reading note explicitly documents this same lynx/bobcat sense alongside the tiger-beast sense. `japanese: [CHU, CHO]` and `japanese_native: けもの` both reconfirmed genuine via Unihan's `kJapaneseOn`/`kJapaneseKun` fields and en.Wiktionary, not fabricated (unlike similar-looking readings found corrupted elsewhere this session). `aliases: [貙]` reconfirmed correct. `stand_in: 名専字` reconfirmed correct — zero hits for 䝙 or 貙 anywhere in `words/`. `boundedness: 65` left as-is (pre-existing judgment call, no evidence of error). Already correctly cross-listed on `Lookup/SKIP/SKIP-1/SKIP-1-7-11.md`.

**`vietnamese` bug found and fixed — wrong reading entirely**: stored `chu` matches no genuine reading; hvdic's actual Âm Hán Việt union for 貙 is `khu`/`sơ`. Corrected to `[khu, sơ]`.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense.

**`joyo_level`/`hsk_level`/`hanmun_edu_level` filled**: all three were blank. Filled `joyo_level: 表外字` (genuine per en.Wiktionary; added as item 488 to `Lookup/Japanese/Hyōgai.md`), `hsk_level: 無` (zero evidence anywhere; added to `Lookup/HSK/HSK No.md`), and `hanmun_edu_level: 名` (matching `grade_level: 名`; added to `Lookup/Korean/Korean Name ㅊ.md`'s `### 추` section).

Rebuilt the malformed `# Notes` (wrong heading level, floating unlinked CC wikilinks, no bullet structure) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 貒 (char) (8391; 371 characters remaining).

### 2026-08-20, iteration 2133 — [[characters/貒 (char)|貒 (char)]]

**`english` completeness gap found and fixed**: stored `[wild boar]` alone — both en.Wiktionary and zh.Wiktionary independently confirm 貒 genuinely carries two attested senses, "hog badger" (matching the page's own `korean_native: 오소리` "badger") and "wild boar" (the sense the vault's own bound word [[words/貒|貒]] draws on, per that word's own `english` field). Added `badger` alongside the already-correct `wild boar`, same dual-sense pattern as [[characters/鱏 (char)|鱏]] two iterations ago.

`graphemic_classification: 耑` reconfirmed correct (dual-source, semantic [[Radical 153|豸]] + phonetic 耑). `mc_id: 7387` reconfirmed as trusted long-tail (>4000, per policy not cross-checked against the CC files). `aliases: [猯, 䝎]` reconfirmed both genuine dual-source variants. `joyo_level: 表外字` reconfirmed correct but was missing its cross-reference — added as item 489 to `Lookup/Japanese/Hyōgai.md`. `hsk_level: 無` reconfirmed correct but was missing from `Lookup/HSK/HSK No.md` — added. `hanmun_edu_level: 無` reconfirmed correct (no Korean Name-list entry required for `無`, per this session's established convention). `stand_in: 貒` reconfirmed correct — the disambiguation callout's own citing word [[words/貒|貒]] confirmed via its `characters: "貒 (char)"` field.

**`japanese_native` YAML bug found and fixed**: the malformed scalar-plus-duplicate-list-item hybrid (`まみ` on the key line, then a redundant `- まみ` entry below it) collapsed to the single genuine kun'yomi `[まみ]`, dual-source confirmed — also the standalone Japanese word for "badger," corroborating the added `english` sense.

**`vietnamese` filled with confirmed-absent sentinel**: was entirely blank. hvdic explicitly states no Âm Hán Việt or Âm Nôm reading exists for 貒 ("Chưa có giải nghĩa theo âm Hán Việt"); filled as `ø`.

**`boundedness` filled**: was blank. Estimated `40` — lower than the typical 65–90 range seen on `名専字`-only hapax characters this session, since 貒 genuinely stands alone as its own Dan'a'yo word rather than being restricted to a fixed compound; flagged as a judgment call absent a formal definition.

Rebuilt the malformed `# Notes` (wrong heading level, floating unlinked CC wikilinks, no bullet structure, no `## Words` section) into the standard `## Notes` four-bullet format plus a `## Words` section citing [[words/貒|貒]], ruby verified against the word's own `注音` field. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 盂 (8392; 370 characters remaining).

### 2026-08-20, iteration 2134 — [[characters/盂|盂]]

`graphemic_classification: 于` reconfirmed correct (dual-source, 形声: semantic [[Radical 108|皿]] "dish, vessel" + phonetic 于). `mc_id: 3106` reconfirmed exact match (CC 3000.md: `3105. 粲`, `3106. 盂`, `3107. 姿`). `english: [cup, basin]` reconfirmed correct — both en.Wiktionary and zh.Wiktionary independently confirm "basin/cup" as 盂's genuine sense, matching `korean_native: 사발` ("bowl"); no character-confusion or precision issue found. `vietnamese: [vu]` reconfirmed exact match to hvdic's sole genuine reading (identical for both Hán Việt and Nôm). `aliases` (blank) reconfirmed correct — en.Wiktionary's lone mention of 𥁄 as an alternative form is single-source, not corroborated by zh.Wiktionary, so not added per convention. `joyo_level: 表外字`, `hsk_level: 無`, `hanmun_edu_level: 名` all reconfirmed correct and already genuinely cross-listed on `Lookup/Japanese/Hyōgai.md` (item 13), `Lookup/HSK/HSK No.md`, and `Lookup/Korean/Korean Name ㅇ.md`'s `### 우` section respectively. `stand_in: 名専字` reconfirmed correct — zero hits for 盂 anywhere in `words/`. No other vault character names 盂 as its `graphemic_classification`, so no `## Derived Characters` section applies. `boundedness: 75` reconfirmed correct.

**`japanese_native` completeness gap found and fixed**: stored only `はち`; both sources independently confirm a second genuine kun'yomi `わん`. Added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense "basin, cup."

Rebuilt the malformed `# Notes` (wrong heading level, floating unlinked CC wikilinks, no bullet structure) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 薨 (8393; 369 characters remaining).

### 2026-08-20, iteration 2135 — [[characters/薨|薨]]

`radical: 艸` reconfirmed correct — genuine Kangxi radical 140 per both sources, though (see below) it plays no semantic role. `mc_id: 483` reconfirmed exact match (CC 0000.md: `482. 福`, `483. 薨`, `484. 穀`). `stroke_count`/`skip_number` reconfirmed correct, already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-3-13.md`. `joyo_level: 表外字` reconfirmed correct — already correctly cross-referenced on `Lookup/Japanese/Hyōgai.md` (item 121). `hanmun_edu_level: 名` reconfirmed correct — already correctly cross-listed on `Lookup/Korean/Korean Name ㅎ.md`'s `### 훙` section. `japanese: [KOU]` reconfirmed correct (sole genuine on'yomi, dual-source). `aliases` (blank) reconfirmed correct — en.Wiktionary's lone candidate `𣩾` has no zh.Wiktionary corroboration, left out per the dual-source convention. `stand_in: 名専字` reconfirmed correct — zero hits for 薨 anywhere in `words/`.

**`graphemic_classification` cross-source disagreement investigated, kept as-is**: en.Wiktionary and the classical Shuowen Jiezi ("从死，瞢省聲") both independently confirm the true composition is semantic 死 ("to die") + phonetic 瞢 (abbreviated) — matching the already-stored `瞢`. zh.Wiktionary's own phonetic-series field instead names 夢 as a same-series character (per Zhengzhang's Old Chinese reconstruction grouping), a genuine disagreement, but this reflects a looser rhyme-based series grouping rather than Shuowen's own structural analysis; kept `瞢` per the classical/en.Wiktionary structural analysis this time, the reverse of the usual 淳/醇-style precedent of favoring zh.Wiktionary. Also newly documented: the character's own Kangxi radical `艸` is a pure graphical top-shape classification, unrelated to either the "death" or "buzzing" senses — the true semantic component is 死, which is not itself a Kangxi radical.

**`pos` bug found and fixed**: stored blank; both attested senses ("to die, of a feudal lord" and "buzz/swarm, onomatopoeia") are verbal. Filled `事詞`.

**`english` bug found and fixed (incomplete, and noun-phrased against a verbal `pos`)**: stored `feudal lord's death` — a noun phrase capturing only one of two dual-source-confirmed senses. Corrected to `[die (of a feudal lord), buzz (onomatopoeia)]`, verb-phrased to match the corrected `pos`.

**`japanese_native` bug found and fixed**: stored `こう` — an exact duplicate of the already-stored on'yomi `KOU`, not a genuine kun'yomi. Both sources independently confirm the real kun'yomi is `みまかる` ("to pass away," a euphemism for death). Corrected.

**`vietnamese` completeness gap found and fixed**: hvdic lists two genuine Âm Hán Việt readings, `hoăng` and `hoằng`; only `hoăng` was stored. Added `hoằng`.

**`hsk_level` filled**: was blank. Zero evidence exists anywhere (absent from every `Old HSK N.md` file and from `Lookup/HSK/HSK No.md`); filled `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added 薨 to `HSK No.md`.

Rebuilt the malformed `# Notes` (wrong heading level, floating unlinked CC wikilinks, no bullet structure) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 娥 (8394; 368 characters remaining).

### 2026-08-20, iteration 2136 — [[characters/娥|娥]]

`mc_id: 3177` reconfirmed exact match (CC 3000.md: `3176. 醇`, `3177. 娥`, `3178. 餼`). `graphemic_classification: 我` (dual-source confirmed 形声, semantic 女 + phonetic 我) reconfirmed correct. `hsk_level: 無` reconfirmed correct — already present on `Lookup/HSK/HSK No.md`. `hanmun_edu_level: 名` reconfirmed correct — already correctly cross-listed on `Lookup/Korean/Korean Name ㅇ.md`'s `### 아` section. `vietnamese: [nga]` reconfirmed exact match to both en.Wiktionary and hvdic's sole genuine reading. `stand_in: 名専字` reconfirmed correct — the sole grep hit, [[words/中秋節|中秋節]], is a false-positive prose mention (referencing 嫦娥 in a Mid-Autumn Festival context), not a genuine `characters:` citation. `boundedness: 75` reconfirmed correct.

**`japanese_native` bug found and fixed**: stored truncated `みめよ`, not a real word. En.Wiktionary confirms the genuine kun'yomi is みめよい ("good-looking"). Corrected to `[みめよい]`.

**`joyo_level` filled**: was blank. En.Wiktionary explicitly confirms 娥 as Hyōgai kanji; added as item 490 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`pos` filled**: was blank. Filled as `性詞`, matching the adjectival senses "beautiful, good."

**Aliases investigated, not added**: zh.Wiktionary's phonetic-series grouping surfaced a candidate variant `䄉`, but en.Wiktionary lists no alternative forms for 娥 and 䄉's own composition (a 禾-based glyph) doesn't corroborate a genuine variant relationship; left `aliases` blank per the dual-source convention.

Rebuilt the malformed `# Notes` (wrong heading level, floating unlinked CC wikilinks, no bullet structure) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 酉 (8395; 367 characters remaining).

### 2026-08-20, iteration 2137 — [[characters/酉|酉]]

**`注音: ⼜` investigated, reconfirmed correct — NOT a corruption**: this Kangxi radical-supplement glyph looked like a corrupted Bopomofo transcription at first glance, but `syllables/⼜.md` confirms it's a genuine, deliberate vault-wide convention — an entire ten-character syllable roster (有/右/油/憂/裕/癒/祐/庾/酉/䍃) is notated with ⼜ instead of standard Bopomofo, consistently reflected in `words/酉月.md`'s own `注音: ⼜·⼔ㄊ` and `Lookup/SKIP/SKIP-4/SKIP-4-7-1.md`'s ruby. Left untouched.

**`graphemic_classification: "象形"` reconfirmed correct, with a genuine pictograph/zodiac distinction clarified**: en.Wiktionary explicitly confirms 酉 as 象形, depicting an ancient wine vessel with a pointed bottom — the original form of [[酒]] ("alcohol") — not a rooster; zh.Wiktionary's oracle-bone/bronze/seal-script evolution corroborates a visual origin without contradicting this. The "rooster" sense (`english: rooster`, `korean_native: 닭`) comes purely from 酉's later role as the tenth Earthly Branch, calendrically paired with the zodiac rooster — unrelated to what the glyph depicts. Rewrote the graphemic bullet to state this distinction explicitly rather than conflating "what it depicts" with "what it's used for."

**`stand_in` bug found and fixed**: stored `名専字`, but a genuine citing word was overlooked — [[words/酉月|酉月]] ("eighth month, rooster month") genuinely lists 酉 in its `characters:` field. Corrected to `酉月`; the other three grep hits ([[words/仲秋|仲秋]], [[words/地支|地支]], [[words/酩酊|酩酊]]) are false-positive prose mentions.

**`## Derived Characters` gap found and fixed**: two vault characters name 酉 as their phonetic component — [[醜]] ("ugly") and [[酒]] ("alcohol") — neither was listed; added both.

**`vietnamese` contamination found and fixed**: stored `[dáu, dấu, dậu, giấu, giậu]`; hvdic's genuine union is only `dậu` (Hán Việt) and `dấu`/`giấu` (Nôm) — `dáu` and `giậu` match no genuine reading (en.Wiktionary's looser "Nôm" list is not this vault's trusted source per established convention). Corrected to `[dấu, dậu, giấu]`.

**`japanese` completeness gap found and fixed**: en.Wiktionary lists both go-on ゆ (`YU`) and kan-on ゆう (`YUU`); only `YUU` was stored. Added `YU`.

**`aliases` filled**: was blank. Both en.Wiktionary ("Alternative forms": 丣) and zh.Wiktionary (異體字 list including 丣) independently confirm 丣 as a genuine variant. Added.

**`hsk_level` filled**: was blank. Zero evidence anywhere (absent from every `Old HSK N.md` file and `Lookup/HSK/HSK No.md`); filled `無`, added 酉 to `HSK No.md`.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses.

`mc_id: 1013` reconfirmed exact match (CC 1000.md: `1012. 亥`, `1013. 酉`, `1014. 寅`). `radical: 酉` reconfirmed correct (its own Kangxi radical, #164). `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 165. `hanmun_edu_level: 中` reconfirmed correct — genuine at `Lookup/Korean/Korean MS.md`. `boundedness: 75` reconfirmed reasonable for a character now bound to one compound.

Rebuilt the malformed `# Notes` (wrong heading level, floating unlinked CC wikilinks, no bullet structure, no `## Words`/`## Derived Characters`) into the standard section order and four-bullet `## Notes` format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 諌 (8396; 366 characters remaining).

### 2026-08-20, iteration 2138 — [[characters/諌|諌]]

**`stand_in` bug found and fixed (contradicted the page's own `## Words` section)**: stored `名専字`, but the page already carried a `## Words` section citing [[諌議]] — grep confirmed 諌議 is the sole genuine citer. Corrected `stand_in` to `諌議`, and filled `boundedness: 85` accordingly (bound to one compound).

**`mandarin` severe content error found and fixed**: stored `dǒng` — matching neither 諌 nor its sibling glyph 諫 (jiàn), and apparently confused with the unrelated character 董. En.Wiktionary confirms 諫's sole Mandarin reading is `jiàn`, consistent with `korean_native: 간할` ("to admonish") and the alias list itself listing 諫. Corrected to `jiàn`.

**`japanese`/`japanese_native` bugs found and fixed**: `japanese` was missing the genuine kan-on `KEN` alongside the already-correct go-on `KAN`; corrected to `[KAN, KEN]`. `japanese_native` was a malformed scalar+stray-list-item hybrid (`いさ` / `- いさむ`) — いさむ is actually a *nanori* (name-reading), not the kun'yomi; the genuine kun'yomi verb is いさめる. Corrected to `[いさめる]`.

`graphemic_classification: 柬` (dual-source confirmed 形声, semantic [[Radical 149|言]] + phonetic 柬) reconfirmed correct. `mc_id: 548` reconfirmed exact match, recorded under sibling glyph 諫 (CC 0000.md: `547. 賓`, `548. 諫`, `549. 澤`) — 諫 has no independent page in this vault. `aliases: [諫, 谏, 𮷅]` reconfirmed correct — en.Wiktionary independently confirms all three as genuine traditional/simplified/variant forms; no `characters/諫.md` page exists, so no alias-direction conflict. `vietnamese: [gián]` reconfirmed exact match — hvdic lists it as both the sole Hán Việt and Nôm reading. `joyo_level: 表外字` reconfirmed correct via `Hyōgai.md`'s own `諫-->[諌]` redirect entry. `hanmun_edu_level: 名` reconfirmed correct — already cross-listed on `Lookup/Korean/Korean Name ㄱ.md`'s `### 간` section (under the 諫 label). `hsk_level: 無` reconfirmed correct but was missing from `Lookup/HSK/HSK No.md` — added. `## Words` ruby verified exact match against `words/諌議.md`'s own `注音` field.

Fixed the section order (Words was placed before Notes) and rebuilt the malformed `# Notes` (wrong heading level, floating unlinked CC wikilinks, no bullet structure) into the standard `## Notes` four-bullet format, documenting the sibling-glyph mc_id convention explicitly. Stamped `date-last-perfect: 2026-08-20`.

### 2026-08-20, iteration 2139 — [[characters/晏|晏]]

`mc_id: 602` reconfirmed exact match (CC 0000.md: `601. 業`, `602. 晏`, `603. 遇`). `graphemic_classification: 安` (dual-source confirmed 形声, semantic 日 "sun" + phonetic 安) reconfirmed correct. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 219. `hanmun_edu_level: 名` reconfirmed correct — already correctly cross-listed on `Lookup/Korean/Korean Name ㅇ.md`'s `### 안` section. `aliases` (blank) reconfirmed correct — zh.Wiktionary's phonetic-series co-occurrences (暥/騴/鼹/鷃) are not genuine 異體字, not added, consistent with convention. `stand_in: 名専字` reconfirmed correct — the sole grep hit, [[words/春秋|春秋]], cites 晏 only within the book-title prose mention "晏子春秋," not a genuine `characters:` citation. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-4-6.md` (item 4).

**Empty gloss filled**: the existing malformed composition bullet had `semantic [[Radical 072|日]] ("")` with the English gloss for 日 missing entirely; filled as "sun."

**`japanese_native` bug found and fixed**: stored truncated `おそ`, not a real reading. Both sources confirm the genuine kun'yomi is おそい ("late," matching `english: late`); corrected to `[おそい]`.

**`vietnamese` completeness gap found and fixed**: hvdic lists two genuine Âm Hán Việt readings, `yến` and `án`; only `yến` was stored. Added `án`.

**`pos` filled**: was blank. Filled as `性詞`, matching the adjectival sense "late" (precedent: [[characters/早 (char)|早]] uses the same `性詞` for its antonym "early").

**`hsk_level` filled**: was blank. Zero evidence anywhere for a genuine level (absent from every `Old HSK N.md` file and, until now, from `Lookup/HSK/HSK No.md` too); filled as `無` per the zero-evidence-defaults-to-無 precedent, and added 晏 to `HSK No.md`.

**Notes trivia added, not just dropped**: en.Wiktionary and zh.Wiktionary both independently attest additional senses beyond "late" — "sunny and cloudless," "peaceful," and the surname of 晏子/晏嬰, the famous Qi-state statesman — folded into the rebuilt graphemic bullet's prose as context, without altering the page's chosen `english: late`.

Collapsed the doubled `## Notes` headers (one bare with floating unlinked CC wikilinks, one with the incomplete composition bullet) into a single standard four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 徙 (8399; 364 characters remaining).

### 2026-08-20, iteration 2140 — [[characters/徙|徙]]

`graphemic_classification: 止` reconfirmed correct (dual-source: semantic [[Radical 060|彳]] "to walk" + phonetic 止). `mc_id: 613` reconfirmed exact match (CC 0000.md: `612. 罰`, `613. 徙`, `614. 赤`). `hsk_level: 6` reconfirmed genuine — a real plain-numbered entry exists at `Lookup/HSK/Old HSK 6.md` item 173 (not just a colon-count frequency entry). `hanmun_edu_level: 名` reconfirmed correct — already cross-listed on `Lookup/Korean/Korean Name ㅅ.md`'s `### 사` section. `stand_in: 名専字` reconfirmed correct — zero hits for 徙 anywhere in `words/`. `boundedness: 65` reconfirmed correct.

**`japanese_native` bug found and fixed**: stored truncated bare fragment `うつ`, not a real reading. Dual sources confirm two genuine kun'yomi, うつす (transitive "to move/relocate something") and うつる (intransitive "to move/relocate"); corrected to the list `[うつす, うつる]`.

**`vietnamese` completeness gap found and fixed**: hvdic's genuine union is `tỉ`/`tỷ` (Hán Việt) and `si`/`tỉ` (Nôm); the stored `[si, tỉ]` was missing the genuine reading `tỷ`. Added.

**`joyo_level` filled**: was blank. 徙 is absent from every Jōyō/Jinmeiyō list despite having genuine dual-source-attested on'yomi/kun'yomi; filled as `表外字` per the zero-more-specific-evidence convention, and added as item 491 to `Lookup/Japanese/Hyōgai.md`.

**`pos` filled**: was blank. Filled as `事詞`, matching the verbal sense "to migrate, relocate."

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 莽 (8400; 363 characters remaining).

### 2026-08-20, iteration 2141 — [[characters/莽|莽]]

**`english` gap found and fixed, not a content error**: stored `english: [poisonous]` looked disconnected from `korean_native: 풀` ("grass") at first glance, but both en.Wiktionary and zh.Wiktionary independently confirm 莽 genuinely carries three dual-sourced senses — "thick weeds/vegetation" (matching `korean_native`), reference to specific toxic plants (*Illicium henryi/lanceolatum*, the source of the stored "poisonous"), and "rash, reckless" (莽撞). Expanded to `[thick vegetation, poisonous, reckless]` rather than replacing the existing value. `pos` filled as `名詞`, matching the primary nominal sense.

**`graphemic_classification: 茻` reconfirmed correct, composition bullet corrected**: en.Wiktionary explicitly analyzes 莽 as phono-semantic with phonetic 茻 (alongside an equally-valid 會意 reading of the same two components, per the source itself), so the stored value is right. However the previous malformed Notes gave no real composition bullet at all; the rebuilt one correctly identifies semantic [[Radical 094|犬]] ("dog") + phonetic [[茻]] — note 茻 is NOT itself a Kangxi radical (it's a distinct four-㇒-stacked character, not the same as the page's own `radical: 艸` assignment), so it gets a bare wikilink, not a Radical-page link; only the semantic 犬 (itself Radical 094) gets the Radical-linking treatment, with a note that the page's own 艸-radical assignment is purely graphical/positional and unrelated to 犬's true etymological role — same pattern as 薨 several iterations ago.

**`stroke_count`/`skip_number` bug found and fixed**: stored `9`/`2-3-6`, but Unicode Unihan's `kTotalStrokes`/`kRSUnicode` (140.7) and an independent stroke-order source both confirm 莽 genuinely has 10 strokes, not 9. Corrected to `stroke_count: 10`, `skip_number: 2-3-7`; removed 莽 from `Lookup/SKIP/SKIP-2/SKIP-2-3-6.md` (size 22→21) and added it to `Lookup/SKIP/SKIP-2/SKIP-2-3-7.md` (size 27→28).

**`vietnamese` contamination fixed**: stored `[mãng, mảng]`; hvdic's page for 莽 lists only `mãng` (as both the Âm Hán Việt and Âm Nôm reading) — `mảng` (a common, unrelated Vietnamese word meaning "patch/piece") does not appear on the page at all. Corrected to `[mãng]`.

**`japanese` completeness gap found and fixed**: stored `[BOU, MOU]`; ja.Wiktionary confirms a third genuine go-on reading `MO`, missing from the list. Corrected to `[MO, MOU, BOU]`. `japanese_native: くさ` reconfirmed genuine (dual-source, "grass"), converted from a bare scalar to a proper list.

**`hsk_level`/`joyo_level` filled**: both blank. Zero genuine plain-numbered entry exists in any `Old HSK N.md` file; filled `hsk_level: 無` and added 莽 to `HSK No.md`. ja.Wiktionary confirms genuine Hyōgai status (not Jōyō/Jinmeiyō); filled `joyo_level: 表外字` and added as item 492 to `Lookup/Japanese/Hyōgai.md`. `mc_id: 624` reconfirmed exact match (CC 0000.md: `623. 載`, `624. 莽`, `625. 舜`). `hanmun_edu_level: 名` reconfirmed correct — already cross-listed on `Lookup/Korean/Korean Name ㅁ.md`'s `### 망` section. `aliases` left blank — the candidate variant 莾 is attested only by a single source (zh.Wiktionary), not dual-source-confirmed. `stand_in: 名専字` reconfirmed correct — zero hits for 莽 anywhere in `words/`. `boundedness: 40` reconfirmed plausible — a high-frequency (mc_id 624), genuinely independent-meaning character, consistent with a lower-than-typical boundedness score despite currently lacking a citing word.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no SKIP/mc_id/level bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 殷 (8401; 362 characters remaining).

### 2026-08-20, iteration 2142 — [[characters/殷|殷]]

`mc_id: 643` reconfirmed exact match (CC 0000.md: `642. 毋`, `643. 殷`, `644. 襄`). `hsk_level: 無` reconfirmed correct — already present on `Lookup/HSK/HSK No.md`. `hanmun_edu_level: 名` reconfirmed correct — already correctly cross-listed on `Lookup/Korean/Korean Name ㅇ.md`'s `### 은` section. `radical: 殳` reconfirmed correct — already listed on `Lookup/Radicals/Radical 079.md`. `stand_in: 名専字` reconfirmed correct — the sole grep hit, [[words/左学|左学]], cites 殷 only within a quoted classical-text prose passage ("殷人養國老於右學…"), not a genuine `characters:` field citation.

**`graphemic_classification: 會意` reconfirmed correct, full component breakdown written**: en.Wiktionary's oracle-bone analysis gives 㐆 ("person with swollen belly," no independent page) + [[Radical 079|殳]] ("hand holding a weapon/club") combining to depict a resonant blow, associated with grand percussion music, extended to "substantial, numerous, prosperous." zh.Wiktionary's own competing `形声` framing was checked and rejected — it names no actual phonetic component, only vaguely gestures at 殳 as "radical + a phonetic," far weaker evidence than en.Wiktionary's concrete oracle-bone sourcing.

**`japanese` completeness gap found and fixed**: stored `[IN, AN]` (both genuine kan-on) was missing the equally genuine go-on pair; added `ON`/`EN`, giving `[IN, AN, ON, EN]`.

**`japanese_native` completeness gap found and fixed**: stored bare `さかん` was missing three further genuine kun'yomi (おおい, ゆたか, にぎやか), all confirmed via en.Wiktionary; expanded to the full four-item list.

**`vietnamese: [ân]` reconfirmed correct, not contamination**: hvdic confirms 殷 carries four tonally-distinct reading/sense pairs (an "large/prosperous," yên "deep red," ân "prosperous/abundant/Yin-dynasty/surname," ẩn "thunder rumble"); `ân` is the genuine reading for the "prosperous" sense this vault uses, restricted per the established convention of not importing unrelated tonal-sense readings.

**`pos` filled**: was blank. Filled as `性詞`, matching the adjectival/stative sense "prosperous."

**Missing lookup cross-reference found and fixed**: 殷 was absent from `Lookup/Japanese/Hyōgai.md` despite genuine `joyo_level: 表外字`; added as item 493.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no bullet structure at all) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 稷 (8402; 361 characters remaining).

### 2026-08-20, iteration 2143 — [[characters/稷|稷]]

`mc_id: 665` reconfirmed exact match (CC 0000.md: `664. 著`, `665. 稷`, `666. 寸`). `graphemic_classification: 畟` reconfirmed correct (dual-source: semantic [[Radical 115|禾]] + phonetic 畟). `japanese: SHOKU`/`japanese_native: きび` reconfirmed correct. `vietnamese: [tắc]` reconfirmed exact match to hvdic's sole genuine reading. `hanmun_edu_level: 名` reconfirmed correct — already correctly cross-listed on `Lookup/Korean/Korean Name ㅈ.md`. `stand_in: 名専字` reconfirmed correct — the two grep hits ([[words/五穀|五穀]], [[words/祭物|祭物]]) are false-positive prose mentions, not genuine `characters:` citations. `boundedness: 80` reconfirmed correct.

**`aliases` bug found and fixed — a paired-but-unrelated grain, not a variant**: stored `黍`, but neither en.Wiktionary nor zh.Wiktionary treats 黍 ("panicled/glutinous millet," a botanically distinct crop) as a variant form of 稷 — the two are simply frequently paired in classical texts (黍稷) and often confused. Confirmed via the "alias = parent form" convention: [[characters/黍|黍]] has its own fully independent page in this vault (its own frontmatter, `stand_in: 名専字`, everything), so it cannot genuinely be an alias of 稷. Removed; the genuine zh.Wiktionary-only variants 畟/禝 were left out per the dual-source convention (en.Wiktionary doesn't corroborate either).

**`english` completeness gap found and fixed**: stored `god of cereals` captured only the deified sense; both sources agree the primary literal sense is "millet" (foxtail millet, *Setaria italica*), extended to the grain-deity and, via 社稷, state-metonym senses. Corrected to `[millet, god of grain]`; the SKIP-list gloss on `Lookup/SKIP/SKIP-1/SKIP-1-5-10.md` updated to match.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses.

**`joyo_level`/`hsk_level` filled**: both were blank. En.Wiktionary explicitly confirms 稷 as Hyōgai kanji; added as item 494 to `Lookup/Japanese/Hyōgai.md` and filled `joyo_level: 表外字`. Zero HSK evidence exists anywhere (absent from every `Old HSK N.md` file and from `Lookup/HSK/HSK No.md`); filled `hsk_level: 無` and added 稷 to `HSK No.md`.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no bullet structure at all) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 淮 (8403; 360 characters remaining).

### 2026-08-20, iteration 2144 — [[characters/淮|淮]]

**`english`/`pos` bug found and fixed (romanization leak, same pattern as 柉/妠)**: stored `english: hwai` was literally the page's own `羅馬字` value, not a real gloss. Both en.Wiktionary and zh.Wiktionary confirm 淮 is the name of the Huai River (淮河), one of China's three major rivers alongside the Yangtze and Yellow rivers, with a secondary surname sense; corrected `english` to `[Huai River, surname]` and filled `pos: 固有名詞`. The vault's own `Lookup/SKIP/SKIP-1/SKIP-1-3-8.md` already independently carried the correct "Huai River" gloss, corroborating the fix.

`graphemic_classification: 隹` reconfirmed correct (dual-source 形声, semantic 水 + phonetic 隹 — both sources note the phonetic choice may trace to bird-totem worship among the ancient Huaiyi people of the Huai river basin). `mc_id: 713` reconfirmed exact match (CC 0000.md: `712. 霸`, `713. 淮`, `714. 莊`). `vietnamese: [choài, hoài]` reconfirmed exact match to hvdic's genuine union (not contamination from the unrelated common word "hoài," despite the coincidental homograph). `japanese_native: ø` reconfirmed correct — ja.Wiktionary explicitly lists no kun'yomi, contradicting an initial suspicion raised by a stray en.Wiktionary listing of unrelated-looking kun readings (ひとしくする/かこむ), which ja.Wiktionary's own dedicated entry does not corroborate. `hanmun_edu_level: 名` reconfirmed correct — already correctly cross-listed on `Lookup/Korean/Korean Name ㅎ.md`. `stand_in: 名専字` reconfirmed correct — all three grep hits ([[words/宙|宙]], [[words/太始|太始]], [[words/書契|書契]]) are false-positive prose mentions of the book title 淮南子, not genuine `characters:` citations. `aliases` (blank) reconfirmed correct — neither source lists a variant form.

**`japanese` completeness gap found and fixed**: stored `[WAI, KAI]` (kan'yō-on and kan-on); ja.Wiktionary's own entry additionally confirms a genuine go-on `エ`. Added `E`.

**`korean_native` filled**: was blank. Filled as `물 이름` ("name of a river"), matching the standard Korean-hanja-dictionary gloss convention for geographic-name characters.

**`hsk_level` filled**: was blank. Zero evidence anywhere (absent from every `Old HSK N.md` file and from `Lookup/HSK/HSK No.md`); filled `hsk_level: 無` and added 淮 to `HSK No.md`.

**`joyo_level` reconfirmed correct but missing cross-reference fixed**: stored `表外字` was already right (ja.Wiktionary explicitly confirms Hyōgai status), but 淮 was absent from `Lookup/Japanese/Hyōgai.md`; added as item 495.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no bullet structure at all) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

### 2026-08-20, iteration 2145 — [[characters/戎|戎]]

`mc_id: 717` reconfirmed exact match (CC 0000.md: `716. 賈`, `717. 戎`, `718. 骨`). `radical: 戈` reconfirmed correct (Kangxi radical 062). `hanmun_edu_level: 名` reconfirmed correct — already correctly cross-listed on `Lookup/Korean/Korean Name ㅇ.md`'s `### 융` section. `english: [arms, armaments]` reconfirmed correct against `korean_native: 병장기` ("weapons"). `stand_in: 名専字` reconfirmed correct — the sole grep hit, [[words/祭物|祭物]], cites 戎 only within a classical-Chinese quotation in its own prose ("國之大事，在祀與戎"), not its `characters:` field — a false positive. Already correctly cross-listed on `Lookup/SKIP/SKIP-3/SKIP-3-4-2.md`.

**`graphemic_classification` bug found and fixed**: stored `會意` with no component bullet ever written. Both en.Wiktionary (components 甲 "shield" + 戈 "halberd/weapons") and zh.Wiktionary (definition "戈戟与盾牌" — halberds and shields) independently confirm the same 會意 breakdown; wrote the full bullet linking [[甲 (char)|甲]] (bare, not itself a Kangxi radical) and [[Radical 062|戈]] (radical-linked per convention), with the resulting "arms/weaponry" sense plus the historically significant secondary senses (military affairs, the 西戎 frontier peoples, a surname) folded into the prose. A zh.Wiktionary-only 異體字 claim (扔, "to throw" — an unrelated common word with a completely different pronunciation) was investigated and rejected as a likely parsing artifact, not a genuine variant; `aliases` left blank.

**`vietnamese` contamination fixed**: stored six readings `[nhong, nhung, nhòng, nhông, nhỏng, xong]`; hvdic's genuine union is only three (`nhung` Hán Việt; `nhong`/`nhung`/`xong` Nôm) — the other three matched no listed reading and were removed.

**`japanese_native` completeness gap fixed**: stored only `えびす` ("barbarian," matching the Rong-tribe sense); en.Wiktionary also lists a second genuine kun'yomi `つわもの` ("warrior," matching the arms/weapons sense) that was missing. Added.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal senses "arms; armaments."

**`joyo_level`/`hsk_level` filled**: both blank, and absent from every relevant lookup page. Filled `joyo_level: 表外字` (ja.Wiktionary confirms genuine on'yomic/kun'yomic attestation with no jōyō/jinmeiyō status; added as item 496 to `Lookup/Japanese/Hyōgai.md`) and `hsk_level: 無` (zero evidence in any `Old HSK N.md` file; added to `HSK No.md`).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no bullet structure at all) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 胥 (8405; 358 characters remaining).

### 2026-08-20, iteration 2146 — [[characters/胥|胥]]

`graphemic_classification: 疋` reconfirmed correct (dual-source, phonetic 疋 OC *sŋraʔ + semantic [[Radical 130|肉]] "flesh"). `mc_id: 727` reconfirmed exact match (CC 0000.md: `726. 崩`, `727. 胥`, `728. 勇`). `english: mutually` reconfirmed correct — matches `korean_native: 서로`; the graphemic bullet now also documents the character's other well-attested senses ("official who catches thieves," extended to "minor clerk/official" 胥吏, and a surname via 伍子胥 Wu Zixu). `vietnamese: [tư]` reconfirmed exact match to hvdic's sole genuine reading (both Hán Việt and Nôm). `japanese: [SHO, SO]` reconfirmed correct (kan-on/go-on). `hanmun_edu_level: 名` reconfirmed correct — already correctly cross-listed on `Lookup/Korean/Korean Name ㅅ.md`'s `### 서` section. `stand_in: 名専字` reconfirmed correct — zero genuine hits for 胥 anywhere in `words/`.

**`aliases` bug found and removed — phonetic-series false positive**: stored `縃`, but 縃's own zh.Wiktionary page identifies it only as belonging to the phonetic-series family "系列#2094（胥）" (a character that uses 胥 as its own phonetic component), not as a variant/alternative form of 胥 itself — the same false-positive pattern as 麟's rejected 獜 alias earlier this session. Removed; left blank, since 縃 has no independent page in this vault and isn't a genuine variant either.

**`## Derived Characters` gap found and fixed**: [[characters/婿 (char)|婿]] genuinely names 胥 as its own `graphemic_classification` phonetic component (composition semantic 女 + phonetic 胥, "son-in-law") but was missing from this page; added.

**`japanese_native` completeness gap found and fixed**: stored only `あい` (genuine, not truncated); both en.Wiktionary and ja.Wiktionary-derived sources additionally confirm kun'yomi `みな` ("all") and `みる`; added both.

**`pos` filled**: was blank. Filled as `名詞`.

**`joyo_level`/`hsk_level` filled**: both blank, and absent from every relevant lookup page. Filled `joyo_level: 表外字` (genuine go-on/kan-on attestation, no jōyō/jinmeiyō status; added as item 497 to `Lookup/Japanese/Hyōgai.md`) and `hsk_level: 無` (zero evidence in any `Old HSK N.md` file; added to `HSK No.md`).

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no bullet structure at all) into the standard `## Notes` four-bullet format plus a `## Derived Characters` section. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 祠 (8406; 357 characters remaining).

### 2026-08-20, iteration 2147 — [[characters/祠|祠]]

`graphemic_classification: 司` reconfirmed correct (dual-source: semantic [[Radical 113|示]] + phonetic 司). `mc_id: 732` reconfirmed exact match (CC 0000.md: `731. 曲`, `732. 祠`, `733. 孰`). `english: ancestral shrine` reconfirmed correct, matching `korean_native: 사당`. `vietnamese: [thờ, tờ, từ]` reconfirmed all three genuine, exact match to en.Wiktionary's union — no contamination despite `từ`/`thờ` both being common independent Vietnamese words. `aliases` (blank) reconfirmed correct — neither source lists a genuine variant form. `stand_in: 名専字` reconfirmed correct — zero hits for 祠 anywhere in `words/`. Already correctly cross-listed on `Lookup/Japanese/Hyōgai.md` (item 137), `Lookup/Korean/Korean Name ㅅ.md`'s `### 사` section, and `Lookup/SKIP/SKIP-2/SKIP-2-5-5.md`.

**`japanese`/`japanese_native` completeness gap found and fixed**: both sources confirm a second genuine on'yomi `JI` (alongside `SHI`) and a second genuine kun'yomi `まつる` ("to offer sacrifice," a literary verbal sense) alongside the already-correct `ほこら`. Added both.

**`pos` filled**: was blank. Filled as `名詞`, matching the primary nominal sense; the verbal "offer sacrifice" sense is noted in prose rather than changing `pos`, per the convention of picking the primary sense (cf. [[characters/薨|薨]]'s onomatopoeic secondary sense).

**`hsk_level` filled**: was blank. Zero evidence anywhere (absent from every `Old HSK N.md` file and, until now, from `Lookup/HSK/HSK No.md` too). Filled `無` and added 祠 to `HSK No.md`.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no bullet structure at all) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 嬰 (8407; 356 characters remaining).

### 2026-08-20, iteration 2148 — [[characters/嬰|嬰]]

**`stand_in` bug found and fixed — contradicted the page's own Notes**: stored `名専字`, but the page's own malformed Notes already carried a stray, ruby-less bullet citing [[words/嬰児|嬰児]] — grepped `words/*.md` and confirmed `嬰児.md` genuinely lists 嬰 in its `characters:` field (the sole genuine citer; other 児/児児/連体 hits were unrelated). Corrected `stand_in` to `嬰児`, raised `boundedness` from 75 to 85 to match the compound-bound convention, and moved the citation into a proper `## Words` section with ruby verified against the word's own `注音` field.

**`hsk_level` bug found and fixed**: stored `3`, traced only to colon-count frequency entries in `Old HSK 3.md` (neither genuine). `Old HSK 6.md` has a genuine plain-numbered entry under the simplified sibling glyph 婴 (`775. [婴]`). Corrected to `hsk_level: 6`.

`mc_id: 736` reconfirmed exact match (CC 0000.md: `735. 迎`, `736. 嬰`, `737. 辰`). `graphemic_classification: 賏` reconfirmed correct — en.Wiktionary notes Shuowen itself analyzes 嬰 as 會意 of 女+賏 rather than phonetic, but this vault follows the phono-semantic reading consistent with 賏's own phonetic-series data; disagreement documented in the rebuilt Notes rather than silently resolved. `aliases: [𰋷, 婴]` reconfirmed correct (dual-source: 𰋷 the Japanese shinjitai, 婴 the standard simplified form); a zh.Wiktionary-listed 纓 was investigated and excluded as a same-reading phonetic-series false positive, not a genuine variant. `vietnamese: [anh]` reconfirmed exact match to hvdic's sole genuine reading (Hán Việt and Nôm identical). `joyo_level: 表外字` and `hanmun_edu_level: 名` reconfirmed correct, already correctly cross-listed on `Lookup/Japanese/Hyōgai.md` and `Lookup/Korean/Korean Name ㅇ.md`'s `### 영` section respectively.

**`english` bug found and fixed**: stored `newborn`, narrower than the character's real primary sense; both sources confirm "infant" as the core gloss (secondary obsolete senses "necklace" and "to encircle/hang around the neck," from which "infant" is itself extended, folded into the rebuilt Notes prose rather than added to `english`). Also updated the stale "newborn" gloss on `Lookup/SKIP/SKIP-2/SKIP-2-14-3.md`'s own numbered-list entry.

**`japanese`/`japanese_native` completeness gaps found and fixed**: missing go-on `YOU` added alongside kan-on `EI`; missing kun'yomi `みどりご` ("infant") added alongside `あかご`.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal "infant" sense.

**Missing `## Derived Characters` found and added**: [[鸚]] genuinely names 嬰 as its own `graphemic_classification` (phonetic component); added.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, a stray ruby-less word citation stranded inside Notes) into the standard `## Notes` four-bullet format plus proper `## Words` and `## Derived Characters` sections. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 寇 (8408; 355 characters remaining).

### 2026-08-20, iteration 2149 — [[characters/寇|寇]]

`mc_id: 740` reconfirmed exact match (CC 0000.md: `739. 勢`, `740. 寇`, `741. 慎`). `hanmun_edu_level: 名` reconfirmed correct — already correctly cross-listed on `Lookup/Korean/Korean Name ㄱ.md`'s `### 구` section. `vietnamese: [kháu, khấu]` reconfirmed exact match to hvdic's genuine union (khấu the sole Hán Việt reading, kháu/khấu both genuine Nôm readings). `japanese_native: あだ` reconfirmed correct against ja.Wiktionary's own kun'yomi listing — an initial suspicion of truncation (expecting あだする) was checked and ruled out. `stand_in: 名専字` reconfirmed correct — zero genuine `characters:` citations anywhere in `words/`.

**`graphemic_classification` filled in from scratch — 會意, not previously described**: dual-source confirmed (en.Wiktionary explicit oracle-bone breakdown, corroborated by zh.Wiktionary's component listing): [[Radical 040|宀]] ("roof, house") + [[元]] ("a person's head") + [[Radical 066|攴]] ("hand holding a rod/weapon") — a hand striking another's head inside their own house, depicting an armed invader breaking in.

**`aliases` bug found and fixed — three of six unverifiable, pruned**: stored six variants (宼, 冦, 㓂, 窛, 𡨥, 𡯷); only 宼/冦/㓂 are dual-source confirmed (zh.Wiktionary's own 異體字 field lists exactly these three). The other three (窛, 𡨥, 𡯷) are en.Wiktionary-only claims — each candidate's own zh.Wiktionary page was checked individually and none identifies itself as a variant of 寇. Removed per the dual-source convention.

**`hsk_level` bug found and fixed**: stored `4`, traced only to a colon-count frequency entry in `Old HSK 4.md` (`[[寇]]: 1`, not genuine). Zero genuine plain-numbered entry exists in any `Old HSK N.md` file. Corrected to `hsk_level: 無` per the zero-evidence-defaults-to-無 precedent, and added 寇 to `HSK No.md`.

**`joyo_level` filled**: was blank. En.Wiktionary and ja.Wiktionary both confirm 寇 as Hyōgai kanji; added as item 498 to `Lookup/Japanese/Hyōgai.md` and filled as `表外字`.

**`japanese` completeness gap fixed**: was missing the genuine go-on reading `KU` (dual-source confirmed alongside the already-stored kan-on `KOU`).

**`english`/`pos` filled**: `pos` was blank. Both sources independently confirm a well-attested secondary verbal sense "to invade, plunder" (入寇) alongside the primary noun sense "bandit"; added `invade` to `english`, filled `pos: 名詞` matching the primary noun sense.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no bullet structure at all) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

### 2026-08-20, iteration 2150 — [[characters/咎|咎]]

**Stray "1271" fragment investigated and resolved**: the malformed Notes left a bare numeral "1271" with no explanation. Cross-checked both mc_id: 788 (confirmed exact match, CC 0000.md: `787. 稽`, `788. 咎`, `789. 歌`) and the stray 1271 against `CC 1000.md` (`1271. 皋`) — the "1271" was never 咎's own rank at all, but 皋's, left behind by whoever mistakenly added 皋 to `aliases`.

**`aliases` bug found and fixed (wrong-homograph pattern)**: stored `[鼛, 皋]`. En.Wiktionary does list 咎 as an alternative form of both — but only under a separate Etymology 2 entry for an unrelated *gāo* reading ("large drum" / a surname), distinct from the *jiù* "fault, calamity" sense this page and `mandarin: jiù` document. Both removed as belonging to the wrong homographic sense; zh.Wiktionary's genuine variants for the *jiù* sense (䛮, 𧧖, 𠧨) are all obscure and pageless, not added. hvdic's Hán Việt reading `cao` was excluded from `vietnamese` for the same reason — it corresponds to the *gāo* reading, not *jiù*.

**`graphemic_classification: 會意` reconfirmed correct**, and the bullet written from scratch: dual-source confirmed as 人 ("person") + 各 ("to oppose"), per Shuowen's own "从人从各，各者，相違也"; the earlier oracle/bronze form combined 夊 ("foot/trample") + 人 before 口 was added in the Spring and Autumn period.

**`english` gap fixed**: stored only `calamity`; both sources independently confirm 咎's core senses also include "fault, blame, guilt" (matching `korean_native: 허물`) — added `fault`, `blame`.

**`japanese`/`japanese_native` completeness gaps fixed**: `japanese` was missing the genuine go-on `GU` (alongside already-correct 呉音/漢音 `KOU`, 漢音 `KYUU`); `japanese_native` was missing the genuine second kun'yomi `とがめる` (alongside already-correct とが).

**`pos` filled**: was blank. Filled as `名詞`, matching the primary nominal senses.

**`hsk_level` filled**: was blank. Zero evidence anywhere for 咎 (absent from every `Old HSK N.md` file); filled as `無`, and added 咎 to `HSK No.md` (was missing despite the level now being 無).

`joyo_level: 表外字` and `hanmun_edu_level: 名` both reconfirmed correct — already genuinely cross-listed on `Lookup/Japanese/Hyōgai.md` (item 48) and `Lookup/Korean/Korean Name ㄱ.md`'s `### 구` section respectively. `stand_in: 名専字` reconfirmed correct — zero hits for 咎 anywhere in `words/`. `boundedness: 90` reconfirmed correct. Already correctly cross-listed on `Lookup/SKIP/SKIP-2/SKIP-2-5-8.md`.

Rebuilt the malformed `# Notes` (wrong heading level, a stray unexplained numeral, two floating unlinked CC wikilinks) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 荊 (8410; 353 characters remaining).

### 2026-08-20, iteration 2151 — [[characters/荊|荊]]

**`stand_in` bug found and fixed — two overlooked genuine citers**: stored `名専字`, but the page's own malformed Notes already stranded a citation of [[words/荊棘|荊棘]] without a proper `## Words` section, and a second genuine citer, [[words/荊州|荊州]], was overlooked entirely (grep confirms both genuinely list 荊 in their `characters:` field). Corrected `stand_in` to `荊棘` (the more central, literal sense) and consolidated both into a proper `## Words` section, ruby verified against each word's own `注音` field.

**`graphemic_classification: 刑` reconfirmed correct** — dual-source (en.Wiktionary + zh.Wiktionary) confirms 形声, semantic 艸/艹 ("grass") + phonetic 刑. `mc_id: 811` reconfirmed exact match (CC 0000.md: `810. 表`, `811. 荊`, `812. 狀`). `aliases: [荆]` reconfirmed correct (genuine simplified form; en.Wiktionary's other listed variants 𦮓/𭱧/𮏂 not added, single-source only). `japanese: [KEI, KYOU]` and `japanese_native: いばら` both reconfirmed genuine and complete via ja.Wiktionary (go-on キョウ, kan-on ケイ, kun'yomi いばら — no truncation). `vietnamese: [kinh]` reconfirmed exact match to hvdic's sole genuine reading. Already correctly cross-listed on `Lookup/Japanese/Hyōgai.md` (item 98) and `Lookup/Korean/Korean Name ㅎ.md`'s `### 형` section, and on `Lookup/SKIP/SKIP-2/SKIP-2-3-6.md`.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense "thorn, bramble."

**`hsk_level` filled**: was blank. Zero evidence anywhere (absent from every `Old HSK N.md` file and from `Lookup/HSK/HSK No.md`). Filled `hsk_level: 無` and added 荊 to `HSK No.md`.

**`boundedness` corrected**: was `75` (calibrated as if a `名専字` hapax); lowered to `55` to reflect genuine, non-name standalone-word productivity across two established compounds (荊棘, 荊州) rather than a single bound compound or pure proper-noun use.

**`## Chengyu` gloss fixed**: `[荊棘荻蓬]` was missing its required English gloss; added `"thorns and thistles"` per the chengyu's own stated meaning (Genesis 3:18).

Rebuilt the malformed body (Notes/Chengyu out of proper order, no `## Words` section, a missing Chengyu gloss, two floating unlinked CC wikilinks stranded past the Chengyu section) into the standard section order — `## Notes` (four-bullet format, graphemic → SKIP/Stroke → MC rank+phonology → levels, with the CC initial/final links embedded in bullet 3) → `## Words` → `## Chengyu`. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 庚 (8411; 352 characters remaining).

### 2026-08-20, iteration 2152 — [[characters/庚|庚]]

**`korean_native: 별` ("star") investigated, kept as genuine — not an error**: Korean dictionaries (어문회 훈음, "별 경") independently confirm 庚's Korean gloss "star" derives from the compound [[長庚]] (장경, *Jangyeong*), a classical name for Venus as the evening star — a real third sense alongside the vault's primary "seventh heavenly stem" and a secondary "age" sense (庚帖, an age-declaration document used in matchmaking). All three folded into the rebuilt Notes prose rather than left as an unexplained mismatch.

`mc_id: 897` reconfirmed exact match (CC 0000.md: `896. 雍`, `897. 庚`, `898. 苟`). `graphemic_classification: 象形` reconfirmed correct — en.Wiktionary describes an ancient flail/threshing-tool pictograph (oracle-bone/bronze forms show a cross-bar with hanging cords or weights), borrowed for the abstract stem/surname senses; `radical: 广` reconfirmed as a purely graphical top-shape classification unrelated to either sense, matching the 薨-style precedent from earlier this session. `vietnamese: [canh]` reconfirmed exact match to hvdic's sole genuine reading. `aliases` (blank) reconfirmed correct — neither source lists a genuine variant form. `stand_in: 名専字` reconfirmed correct — the three grep hits ([[words/乙|乙]], [[words/十干|十干]], [[words/天干|天干]]) are false-positive prose mentions of 庚 within the full ten-stem list, not genuine `characters:` field citations. `pos: 固有名詞` reconfirmed correct, matching the established convention for other heavenly-stem characters in this vault ([[characters/戊|戊]], [[characters/壬|壬]], both also `固有名詞`) as distinct from stem-characters with broader independent senses (己 "self" → 名詞, 辛 "spicy" → 性詞). `joyo_level: 日本人名用漢字`, `hsk_level: 無`, and `hanmun_edu_level: 中` all reconfirmed already correctly cross-listed on `Lookup/Japanese/Jinmeiyō.md` (item 105), `Lookup/HSK/HSK No.md`, and `Lookup/Korean/Korean MS.md` respectively. Already correctly cross-listed on `Lookup/SKIP/SKIP-3/SKIP-3-3-5.md` (item 8).

**`japanese` completeness gap found and fixed**: was missing the genuine go-on reading `KYOU` alongside the already-correct kan-on `KOU`; both confirmed via en.Wiktionary. `japanese_native: かのえ` reconfirmed correct and complete.

**`english` completeness gap found and fixed**: added `surname` as a second gloss, dual-source confirmed alongside the already-correct `seventh heavenly stem`.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no bullet structure at all) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 荻 (8412; 351 characters remaining).

### 2026-08-20, iteration 2153 — [[characters/荻|荻]]

**`aliases` bug found and fixed (genuine misclassification)**: stored `狄` — but both en.Wiktionary and zh.Wiktionary explicitly identify 狄 as merely 荻's *phonetic* component (already correctly captured in `graphemic_classification: 狄`), not a variant/alternative form of 荻 itself; the two are distinct words ("Amur silvergrass" vs. "northern tribe") that happen to share an Old Chinese reading. Removed 狄; added the two genuine dual-source-confirmed variants instead, `蔐` and `藡`.

**Stray "狄=C#867" fragment investigated and resolved**: this turned out to be a prior editor's scratch note recording 狄's own Classical Chinese frequency rank (`Lookup/CC/CC 0000.md`: `867. 狄`) — genuine, but irrelevant to 荻's own `mc_id`, since the two are not sibling glyphs under the vault's established interchangeable-orthography convention (unlike 龐/龎, 鵰/雕, 繋/繫 from earlier iterations). `mc_id: 5535` (trusted long-tail) reconfirmed correct as stored; the finding was folded into the rebuilt graphemic bullet's prose rather than silently dropped.

**Broken wikilink fixed in an external lookup file**: `Lookup/Korean/Korean Name ㅈ.md`'s own `### 적` section linked `[狄](characters/荻.md)` — pointing the unrelated, pageless 狄 at 荻's page, the same mis-link pattern found on 麟's page earlier this session. Corrected to an unresolved `[[狄]]` wikilink, matching the format used for other pageless characters on that line; the adjacent, already-correct `[荻](characters/荻.md)` entry was left untouched.

**`pos` bug found and fixed (genuine misclassification)**: stored `固有名詞`, but 荻 is a common plant-species noun (a specific reed-grass species), not a proper noun — corrected to `名詞`, matching this session's precedent for other plant/animal-species characters (藻, 蟹, 貒).

**`japanese` completeness gap found and fixed**: ja.Wiktionary lists two genuine on'yomi, go-on `ジャク` (JAKU) and kan-on `テキ` (TEKI); only TEKI was stored. Added JAKU.

**`english` completeness gap found and fixed**: added the accessible common-name gloss `silver grass` alongside the existing scientific-name gloss `Miscanthus sacchariflorus`.

**`boundedness` bug found and fixed**: stored `35`, notably low for a `名専字`-only character with zero citing words in `words/`; corrected to `90`, matching this session's convention for comparable hapax `名専字` characters.

Reconfirmed `graphemic_classification: 狄` (dual-source), `vietnamese: [địch]` (hvdic's sole genuine reading, matching its Nôm reading too), `japanese_native: おぎ`, `joyo_level: 日本人名用漢字` (already correctly cross-listed at `Lookup/Japanese/Jinmeiyō.md` item 335), `hsk_level: 無` (already correctly cross-listed on `Lookup/HSK/HSK No.md`), `hanmun_edu_level: 名` (already correctly cross-listed on `Lookup/Korean/Korean Name ㅈ.md`), `stand_in: 名専字` (zero hits for 荻 anywhere in `words/`).

Rebuilt the malformed `# Notes` (wrong heading level, a stray cryptic "狄=C#867" fragment, two floating unlinked CC wikilinks, no bullet structure at all) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 羌 (8413; 350 characters remaining).

### 2026-08-20, iteration 2154 — [[characters/羌|羌]]

`mc_id: 869` reconfirmed exact match (CC 0000.md: `868. 幽`, `869. 羌`, `870. 丹`). `stand_in: 名専字` reconfirmed correct — zero hits for 羌 anywhere in `words/`. `vietnamese: [cưng, gừng, khương]` reconfirmed all three genuine (en.Wiktionary's own Hán Nôm reading list matches exactly, despite cưng/gừng both being common independent Vietnamese words — no contamination). Already correctly cross-listed on `Lookup/Korean/Korean Name ㄱ.md` and `Lookup/SKIP/SKIP-2/SKIP-2-6-6.md`.

**`graphemic_classification` investigated, kept as-is**: initially suspected as a 形声-vs-會意 misclassification bug (since 羌 is traditionally described as a 會意 of 人+羊 depicting Qiang shepherds), but en.Wiktionary's own Shuowen citation explicitly states 羊 serves *both* as the semantic image and the phonetic component (a genuine 會意兼形聲 hybrid) — the checklist has no dedicated hybrid-type field, so `graphemic_classification: 羊` was kept, with the hybrid nature documented in the rebuilt graphemic bullet.

**`japanese_native: ああ` bug investigated, confirmed genuine — not a corruption**: this bare fragment looked suspicious but ja.Wiktionary explicitly confirms it as a real kun'yomi, reflecting 羌's obsolete Chu Ci exclamatory-particle sense ("alas!/oh!"); confirmed alongside the already-listed えびす. `japanese` missing reading `KOU` (go-on) added alongside the already-correct `KYOU` (kan-on).

**`korean_native` filled**: was blank. Filled `오랑캐` ("barbarian/nomad"), matching the vault's own precedent for the parallel ethnonym character [[characters/匈|匈]] (Xiongnu).

**`english` completeness gap fixed**: en.Wiktionary confirms a second genuine sense, "muntjac deer" (山羌); added alongside the already-correct `Qiang`. `pos` filled as `固有名詞`, matching the primary ethnonym sense.

**`aliases` completeness gap fixed**: dual-source (en.Wiktionary + zh.Wiktionary) confirms `猐` as a genuine second variant alongside the already-correct `羗`; the more obscure single-source-only candidates (𦍑, 𠒌, 𡸓, 㳾) were not added, consistent with convention.

**`joyo_level`/`hsk_level` filled**: both blank. Filled `joyo_level: 表外字` (added as item 499 to `Lookup/Japanese/Hyōgai.md`) and `hsk_level: 無` (zero evidence in any `Old HSK N.md` file; added to `Lookup/HSK/HSK No.md`).

Rebuilt the malformed `# Notes` (wrong heading level, floating unlinked CC wikilinks, no bullet structure at all) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 輒 (8414; 349 characters remaining).

### 2026-08-20, iteration 2155 — [[characters/輒|輒]]

**`english`/`pos` bug found and fixed (genuine incompleteness, not outright wrong)**: stored `chariot's weapons pouch` and blank `pos` captured only the character's archaic etymological noun sense — but 輒's overwhelmingly common classical usage is adverbial, "then, promptly, at every turn, always" (as in 動輒 "at every turn"), matching both `korean_native: 문득` and the already-stored kun'yomi すなわち. En.Wiktionary confirms both senses explicitly (phono-semantic compound, semantic [[Radical 159|車]] + phonetic 耴, OC *teːb/*ŋrɯd), zh.Wiktionary's shorter entry does not contradict. Corrected `english` to `[then, always, at every turn]` and `pos` to `副詞`, keeping the original chariot-side-panel sense as etymological background in the rebuilt Notes.

`mc_id: 871` reconfirmed exact match (CC 0000.md: `870. 丹`, `871. 輒`, `872. 全`). `aliases: [辄]` reconfirmed correct (genuine simplified form; 辄 has no independent page). `vietnamese: [triếp]` reconfirmed exact match to hvdic's sole genuine reading (Hán Việt and Nôm identical). `hanmun_edu_level: 名` reconfirmed correct — already correctly cross-listed on `Lookup/Korean/Korean Name ㅊ.md`'s `### 첩` section. `stand_in: 名専字` reconfirmed correct — zero hits for 輒 anywhere in `words/`.

**`japanese_native` completeness gap found and fixed**: hvdic and en.Wiktionary both independently confirm a second genuine kun'yomi, わきぎ (reflecting the original "chariot side panel" noun sense); added alongside the already-correct すなわち.

**`joyo_level`/`hsk_level` filled**: both blank. En.Wiktionary confirms 輒 as Hyōgai kanji; added as item 500 to `Lookup/Japanese/Hyōgai.md`. Zero genuine evidence anywhere for an HSK level; filled `hsk_level: 無` and added 輒 to `HSK No.md`.

**`boundedness` raised**: was `80`; raised to `90` to match the standard convention for a `名専字` hapax character with zero citing words in `words/`.

Rebuilt the malformed `# Notes` (wrong heading level, floating unlinked CC wikilinks, no bullet structure at all) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 雍 (8415; 348 characters remaining).

### 2026-08-20, iteration 2156 — [[characters/雍|雍]]

**`graphemic_classification` bug found and fixed (genuine misclassification, contradicted by a stray editorial note)**: stored `宮`, contradicted by a stray "Components: 亠, 乡, 隹" note left by a prior editor who never resolved it. Research shows neither value is right: en.Wiktionary explicitly states 雍 is a variant of [[雝]], whose own phonetic component 邕 (OC *qoŋ) corrupted into a 玄-like shape since the two forms looked similar in pre-Qin script — the stray "亠/乡" fragments are just that corrupted remnant misread as separate components, not genuine constituents. Corrected `graphemic_classification` to `邕` (semantic 隹 "short-tailed bird" + phonetic 邕).

**`stand_in` bug found and fixed**: stored `名専字`, but a stray unruby'd bullet already cited [[雍雍]] — confirmed genuine via `words/雍雍.md`'s own `characters: [雍, 雍]` field. Corrected to `雍雍`; moved the citation into a proper ruby-annotated `## Words` section. `boundedness` raised from 75 to 85 to match the compound-bound convention.

**Stray "Pronunciation changed in accordance with the Korean surname" note investigated, dropped**: no genuine syllable-placement-override evidence found — 옹 is a perfectly regular Sino-Korean reading for 雍, matching its MC-derived syllable exactly. Documented as unverified/unsupported in the rebuilt Notes rather than silently dropped or blindly carried forward.

`mc_id: 896` reconfirmed exact match (CC 0000.md: `895. 附`, `896. 雍`, `897. 庚` — internally consistent with iteration 2152's finding that 庚 sits at rank 897). `aliases: [雝, 邕, 廱]` all reconfirmed genuine dual-source variants (zh.Wiktionary's own variant-forms field lists all three, plus 𩀢/嗈 which were left out per the dual-source-only convention); none has an independent page in this vault. `vietnamese: [ung, úng, ủng]` reconfirmed all three genuine (hvdic explicitly lists all three as Âm Hán Việt). `joyo_level`/`hsk_level`/`hanmun_edu_level` all reconfirmed correct — `hsk_level: 無` and `hanmun_edu_level: 名` were already correctly cross-listed (the latter even correctly redirects the alias 邕 to this page); `joyo_level: 表外字` was missing its own cross-reference, added as item 501 to `Lookup/Japanese/Hyōgai.md`.

**`japanese_native` truncation fixed**: stored bare `ふさ`, a truncated fragment of the genuine kun'yomi `ふさぐ` ("to obstruct," matching 雍's attested "alternative form of 壅/擁" sense). A second genuine kun'yomi, `やわらぐ` ("to be harmonious/soften"), matching the character's primary sense and `korean_native: 화할`, was missing entirely; added both.

Rebuilt the malformed `## Notes` (floating unlinked CC links, a stray incorrect "Components" note, an unresolved pronunciation claim, a stranded unruby'd Words-style bullet) into the standard four-bullet format plus a proper `## Words` section. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 悉 (8416; 347 characters remaining).

### 2026-08-20, iteration 2157 — [[characters/悉|悉]]

`graphemic_classification: 會意` reconfirmed correct — both en.Wiktionary and zh.Wiktionary independently cite Shuowen's own gloss, "詳盡也。从心从釆" ("thorough; from 心 and 釆"), a mind that discerns thoroughly. Wrote the missing graphemic bullet accordingly. `mc_id: 907` reconfirmed exact match (CC 0000.md: `906. 背`, `907. 悉`, `908. 誰`). `vietnamese: [dứt, tạt, tất, tắt]` reconfirmed exact match — hvdic's genuine union is `tất` (Hán Việt) plus all four as Nôm readings. `joyo_level: 日本人名用漢字` reconfirmed correct — genuine at `Lookup/Japanese/Jinmeiyō.md` item 457. `hanmun_edu_level: 名` reconfirmed correct — already correctly cross-listed on `Lookup/Korean/Korean Name ㅅ.md`'s `### 실` section. `stand_in: 名専字` reconfirmed correct — zero hits for 悉 anywhere in `words/`.

**`english`/`pos` completeness gap found and fixed**: stored `english: comprehend` and blank `pos` captured only 悉's secondary "to know/comprehend fully" sense, missing the extremely common adverbial "all, entirely" sense (悉皆, 悉數) that `korean_native: 다` and the kun'yomi `ことごとく` actually point to — both dual sources independently confirm this second sense. Corrected `english` to `[entirely, comprehend]` and filled `pos: 副詞`, matching the same adverbial-sense pattern resolved on [[characters/輒|輒]] last iteration.

**`hsk_level` bug found and fixed**: stored `2`, traced only to colon-count frequency entries in `Old HSK 2.md` (`[[悉]]: 1`) and `Old HSK 4.md` (`[悉](...): 2`), neither genuine. Zero genuine plain-numbered entry exists in any `Old HSK N.md` file. Corrected to `hsk_level: 無` — already correctly present on `Lookup/HSK/HSK No.md`.

**`japanese_native` truncation fixed**: stored bare `ことごと`, a truncated fragment of the genuine kun'yomi `ことごとく`. A second genuine kun'yomi, `つくす` ("to exhaust, use up fully"), was missing entirely; added both.

**`aliases` bug found and fixed — missing genuine variants**: was blank. Both en.Wiktionary and zh.Wiktionary independently list `怸`, `𢚊`, and `𢝕` as alternative forms of 悉 (a dual-sourced intersection — zh.Wiktionary's further `𢗦`/`𢘤`/`𢙍` were single-source only and not added, consistent with convention); none has an independent page in this vault. Added all three.

Rebuilt the malformed `# Notes` (wrong heading level, floating unlinked CC links, no bullet structure at all) into the standard `## Notes` four-bullet format. The stale gloss "comprehend" on `Lookup/SKIP/SKIP-2/SKIP-2-7-4.md`'s own item 10 was also corrected to "entirely" to match. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 蕎 (8417; 346 characters remaining).

### 2026-08-20, iteration 2158 — [[characters/蕎|蕎]]

`stroke_count: 15` reconfirmed correct against Unihan (kTotalStrokes), despite zh.Wiktionary's own summary claiming 18 — trusted the authoritative Unicode source over the secondary summary. `korean_native: 메밀`/`english: buckwheat` reconfirmed correct (dual-source). `japanese_native: そば`/`vietnamese: [kiều, kiệu]` reconfirmed exact matches to both sources' genuine unions. `graphemic_classification: 喬` reconfirmed correct (dual-source 形声, semantic 艸 + phonetic 喬). `stand_in: 名専字` reconfirmed correct — zero hits for 蕎 anywhere in `words/`. `joyo_level: 日本人名用漢字`/`hsk_level: 無`/`hanmun_edu_level: 名` all reconfirmed already correctly cross-listed on `Lookup/Japanese/Jinmeiyō.md`, `Lookup/HSK/HSK No.md`, and `Lookup/Korean/Korean Name ㄱ.md`'s `### 교` section respectively.

**`aliases` bug found and fixed — two false positives, one missing genuine variant**: stored `[荞, 乔, 驕]`. `荞` (the genuine simplified form) reconfirmed correct. `乔` removed — it's the simplified form of the *phonetic component* 喬 itself, already correctly listed under `characters/喬.md`'s own `aliases` field, not a variant of 蕎. `驕` ("proud, arrogant," an unrelated 馬-radical word) removed — it merely shares the 喬 phonetic; both sources' "Alternative forms" fields for 蕎 list neither. Added the genuine dual-sourced variant `荍` (missing entirely).

**`mc_id` bug found and fixed (character-confusion pattern)**: stored `977`, but `Lookup/CC/CC 0000.md` rank `977` is genuinely `驕`, not `蕎` — the identical character-confusion error as the aliases bug above. 蕎 itself is confirmed absent from all four CC frequency files; corrected to `mc_id: 0`.

**Vault-wide propagation of the 驕/蕎 confusion found and fixed**: `Lookup/HSK/Old HSK 2.md`'s own colon-count entry for 驕 and `Lookup/Korean/Korean Name ㄱ.md`'s `### 교` section had both mistakenly linked 驕 to `characters/蕎.md` instead of a bare unresolved wikilink (驕 has no independent page of its own in this vault); both corrected to `[[驕]]`.

**`pos` filled**: was blank. Filled as `名詞`, matching the nominal sense "buckwheat."

**`boundedness` bug found and fixed**: stored `5`, anomalously low compared to every other `名専字`, no-citing-word character this session (which cluster 65–90) and inconsistent with the checklist's judgment-call convention; corrected to `85`.

Rebuilt the malformed `# Notes` (wrong heading level, floating unlinked CC links, no bullet structure) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 穆 (8418; 345 characters remaining).

### 2026-08-20, iteration 2159 — [[characters/穆|穆]]

**`english`/`pos` bug found and fixed (content error, dominant sense missing)**: stored `english: [standing grain]` — a genuine but obsolete etymological sense per en.Wiktionary's own definition list — but the character's dominant living senses ("reverent, solemn, dignified, harmonious, calm," matching `korean_native: 화목할`) were entirely absent from the gloss, and `pos` was blank. Corrected `english` to `[harmonious, solemn, reverent]`, filled `pos: 性詞`; the obsolete "standing grain" sense and the 穆斯林/穆罕默德 Muslim-transliteration use preserved in the rebuilt Notes prose rather than dropped. The stale "standing grain" gloss was also propagated to `Lookup/SKIP/SKIP-1/SKIP-1-5-11.md`'s own entry; fixed there too.

`graphemic_classification: 㣎` (dual-source confirmed 形声, semantic 禾 + phonetic 㣎) reconfirmed correct. `mc_id: 918` reconfirmed exact match (CC 0000.md: `917. 午`, `918. 穆`, `919. 序`). `hanmun_edu_level: 名` reconfirmed correct — already correctly cross-listed on `Lookup/Korean/Korean Name ㅁ.md`'s `### 목` section. `stand_in: 名専字` reconfirmed correct — zero hits for 穆 anywhere in `words/`. `boundedness: 90` reconfirmed correct. `aliases` (blank) reconfirmed correct — en.Wiktionary's own alternative-forms list (繆/缪, 𥠇, 𥡆, 𢿉, 𢿬, 𢾓) is single-source only, not corroborated by zh.Wiktionary, so left out per convention.

**`hsk_level` bug found and fixed**: stored `4`, traced only to a colon-count frequency entry in `Old HSK 4.md` (`[[穆]]: 1`, not genuine) — and directly contradicted by 穆's own pre-existing presence on `Lookup/HSK/HSK No.md`. Corrected to `hsk_level: 無`.

**`joyo_level` filled**: was blank. Confirmed 穆 as a genuine 人名用漢字 (Jinmeiyō) via multiple independent Japanese kanji-dictionary sources; added as item 479 to `Lookup/Japanese/Jinmeiyō.md` and filled as `日本人名用漢字`.

**`japanese_native` bug found and fixed**: stored truncated bare fragment `やわ`, not a real reading. ja.Wiktionary confirms the genuine kun'yomi is `やわらぐ` ("to soften, become harmonious"); corrected.

**`vietnamese` completeness gap found and fixed**: hvdic lists two genuine Âm Hán Việt readings, `mặc` and `mục`; only `mục` was stored. Added `mặc`.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no bullet structure) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 癸 (8419; 344 characters remaining).

### 2026-08-20, iteration 2160 — [[characters/癸|癸]]

`mc_id: 967` reconfirmed exact match (CC 0000.md: `966. 寬`, `967. 癸`, `968. 錯`). `radical: 癶` reconfirmed correct — genuine Kangxi radical 105 per en.Wiktionary's own citation. `japanese: [KI]` and `japanese_native: みずのと` both reconfirmed genuine (on-yomi き, kun'yomi みずのと "younger sibling of water," dual-source confirmed). `joyo_level: 表外字` reconfirmed correct — already correctly cross-listed on `Lookup/Japanese/Hyōgai.md` (item 72). `hsk_level: 無` reconfirmed correct — already present on `Lookup/HSK/HSK No.md`. `hanmun_edu_level: 中` reconfirmed correct — already correctly cross-listed on `Lookup/Korean/Korean MS.md`. `aliases` (blank) reconfirmed correct — no genuine dual-source variant found. `stand_in: 名専字` reconfirmed correct — the sole grep hit, [[words/乙|乙]], is a false-positive prose mention (乙 listing all ten Heavenly Stems including 癸), not a genuine `characters:` citation. `boundedness: 90` reconfirmed correct.

**`graphemic_classification` bullet written from scratch, origin genuinely uncertain**: en.Wiktionary lists competing proposals (original form of 戣 "a type of halberd" or 葵 "mallow"; a measuring tool related to 揆/季; or a sundial-shadow device for fixing directions/solstices, ancestor of 規), while zh.Wiktionary cites Shuowen's own gloss: "冬時，水土平，可揆度也。象水從四方流入地中之形" ("depicts water flowing into the earth from four directions"). Documented as uncertain per both sources rather than picking one arbitrarily.

**`vietnamese` bug found and fixed — contamination**: stored `[quý, quấy, quậy]`; hvdic's genuine union is `quý` (Hán Việt) and `quấy`/`quý` (Nôm). `quậy` ("to be mischievous," an unrelated common word) matches no genuine reading — removed.

**`pos` filled**: was blank. Filled as `固有名詞`, matching the precedent set by sibling calendrical-stem character [[characters/庚|庚]] (iteration 2152) for this session.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no bullet structure) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-20`.

### 2026-08-20, iteration 2161 — [[characters/偲|偲]]

**`english`/`pos` completeness gap found and fixed**: stored `talent` was only one of two dual-source-confirmed classical senses. en.Wiktionary and zh.Wiktionary both independently confirm 偲's *Shijing*-attested "able, talented, capable" sense, but ja.Wiktionary explicitly documents a second genuine sense, "to mutually admonish one another" — matching `korean_native: 책선할` and the reduplicated form 偲偲 (as in the *Analects*' 切切偲偲). Expanded `english` to `[talented, urge one another (to improve)]` and filled `pos: 事詞` for the admonishing-verb sense the vault's own `korean_native` points to.

`graphemic_classification` (unlabeled, semantic 人 + phonetic 思) reconfirmed correct — dual-source confirmed composition ⿰亻思. `mc_id: 6379` reconfirmed as trusted long-tail (>4000). `stand_in: 名専字` reconfirmed correct — zero hits for 偲 anywhere in `words/`. `boundedness: 65` reconfirmed correct. Already correctly cross-listed on `Lookup/HSK/HSK No.md`, `Lookup/Japanese/Jinmeiyō.md`, and `Lookup/Korean/Korean Name ㅅ.md`.

**`japanese_native` truncation fixed**: stored bare fragment `しの` was not a genuine standalone reading; ja.Wiktionary's real kun'yomi is しのぶ ("to yearn for, recall fondly" — a third, distinct extended sense from the "talented"/"mutual admonishment" pair). Corrected to `しのぶ`.

**`vietnamese` filled**: was entirely blank. hvdic lists three genuine Âm Hán Việt readings, `tai`, `ti`, `ty`; no Nôm readings exist. Added all three.

**`aliases` filled**: was blank. zh.Wiktionary explicitly lists 愢 as a variant form of 偲 (matching the "mutual admonishment" sense); no independent page exists for 愢 in this vault, so added per the parent-page convention. A second candidate, 𤟧, and en.Wiktionary's own "alternative form of 䰄" (bearded-appearance sense) were investigated and left out — 䰄 reflects an unrelated sense, and 𤟧 lacked corroboration from zh.Wiktionary's own entry beyond a passing mention.

Rebuilt the malformed `# Notes` (wrong heading level, two floating unlinked CC wikilinks, no bullet structure) into the standard `## Notes` four-bullet format. Also fixed the stale "talent"-only gloss on `Lookup/SKIP/SKIP-1/SKIP-1-2-9.md`'s own item 11. Stamped `date-last-perfect: 2026-08-20`.

Next never-perfected character by `danayo_id`: 僑 (8421; 342 characters remaining).
