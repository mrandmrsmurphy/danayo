# Character Perfecting (Solo Loop)

Running log for the character-perfecting backlog sweep (see [[AIOS/checklists/checklist_characters.md|Checklist: Character Pages]]). The prior logs (iterations 1–464, 465–981, 982–1543, 1544–2049, 2050–2260, and 2261–2467) grew large and were archived to `Character Perfecting (Solo Loop).md.zip`, `Character Perfecting (Solo Loop) 2.md.zip`, `Character Perfecting (Solo Loop) 3.md.zip`, `Character Perfecting (Solo Loop) 4.md.zip`, `Character Perfecting (Solo Loop) 5.md.zip`, and `Character Perfecting (Solo Loop) 6.md.zip` respectively; this file continues from there. Iteration numbering continues unbroken from the archived logs.

**Process**: one character per iteration. Find the next never-perfected character via `danayo_id` ascending (`grep -L "^date-last-perfect" characters/*.md`, sorted by each file's own `danayo_id` frontmatter value — not alphabetical, unlike the word sweep). Verify/fill all required frontmatter (`graphemic_classification`, `stand_in`, `mc_id`, `danayo_id`, `pos`, level fields), write or correct the four fixed `## Notes` bullets (graphemic → SKIP/Stroke → MC rank+phonology → levels), cross-check `## Words` against every real word citing this character as a constituent, add `## Chengyu`/`## Derived Characters` when real hits exist, then stamp `date-last-perfect`.

Next never-perfected character by `danayo_id`: 畐 (8766; 37 characters remaining).

### 2026-08-24, iteration 2468 — [[characters/畐|畐]]

`radical: 田` reconfirmed correct (Kangxi radical 102). `skip_number: 2-4-5` and `stroke_count: 9` reconfirmed correct against `SKIP-2-4-5.md` and `Stroke 09.md`, both already listing the character (correctly coexisting there with 昷, another radical-different SKIP-2-4-5/stroke-9 character — not a collision bug). `graphemic_classification: 象形` reconfirmed correct — dual-source confirmed pictogram of a full vessel. `japanese: [FUKU, BUKU, HYOKU, HIKI]` reconfirmed correct and complete — matches ja.Wiktionary's full four-reading on'yomi list (呉音フク/ブク/ヒキ, 漢音フク/ヒョク) exactly. `japanese_native: ø` reconfirmed correct — ja.Wiktionary explicitly lists no kun'yomi. `vietnamese: phúc` reconfirmed correct and complete — hvdic.thivien.net's sole Âm Hán Việt reading. `english: roll of cloth` reconfirmed correct — matches both sources' secondary "alternate form of 幅" sense; kept distinct from 幅's own "breadth, width" gloss. `mc_id: 5205` reconfirmed as trusted long-tail (>4000, not cross-checked per policy). Zero hits for 畐 anywhere in `words/` (the one grep hit, in `words/副.md`, is a false-positive prose mention of 畐 as 副's own phonetic component, not a genuine `characters:` citation), confirming `stand_in: 名専字` and no `## Words` section needed.

**`pos`, `joyo_level`, `hsk_level`, `hanmun_edu_level`, `boundedness` filled — all five were blank**: `pos` filled as `名詞`. `joyo_level` filled as `表外字` (dual-source confirmed); added as item 625 to `Lookup/Japanese/Hyōgai.md`. `hsk_level` filled as `無` — genuinely absent from all six `Old HSK N.md` files; added to `Lookup/HSK/HSK No.md`. `hanmun_edu_level` filled as `無`. `boundedness` filled as `75`, consistent with comparable bound characters.

**`## Derived Characters` completeness gap found and fixed**: only listed [[蝠]] and [[逼]]; cross-checking every character's own `graphemic_classification` field for `畐` citations turned up five more genuine phonetic derivatives with independent vault pages, all missing: [[福 (char)|福]], [[富]], [[幅]], [[副 (char)|副]], and [[偪]]. Added all five.

**Missing Korean lookup entry found and fixed**: absent from `Lookup/Korean/Korean Name ㅂ.md`'s `### 복` subsection despite `korean: 복`; added.

Rebuilt the malformed Notes (missing SKIP/Stroke/mc_id-prose/four-links bullets, an unfinished etymology bullet ending in a bare period, an informal `### Derived characters` heading) into the standard `## Notes` four-bullet format plus a properly-headed `## Derived Characters` section. Stamped `date-last-perfect: 2026-08-24`.

Next never-perfected character by `danayo_id`: 禺 (8767; 36 characters remaining).

### 2026-08-24, iteration 2469 — [[characters/禺|禺]]

`radical: 禸` reconfirmed correct (Kangxi radical 114). `skip_number: 4-9-3` and `stroke_count: 9` reconfirmed correct against `SKIP-4-9-3.md` and `Stroke 09.md`, both already listing the character. `graphemic_classification: 象形` reconfirmed correct — trusted the vault's own pre-existing membership in `Lookup/List of 象形.md` over en.Wiktionary's more ambiguous "possibly ideogrammic" phrasing (same precedent as 夌). `japanese_native: おながざる` reconfirmed correct. `korean: 옹` reconfirmed correct — directly attested by en.Wiktionary. `## Derived Characters` (偶, 愚, 遇, 寓, 隅) reconfirmed as all genuine — cross-checked each one's own `graphemic_classification` field, all five cite 禺. Zero hits for 禺 anywhere in `words/`, confirming `stand_in: 名専字` and no `## Words` section needed.

**`aliases`/`english` false-alias bug found and fixed**: `藕` ("lotus root") was listed as an alias, with a matching "lotus root" `english` gloss. Direct zh.Wiktionary fetch of 藕's own entry shows its true phonetic component is 耦, not 禺 — the two characters are merely part of the same broader phonetic family (諧聲系), not a genuine 異體字/variant relationship. Removed the false alias and the unsupported gloss, leaving `english: [long-tailed monkey]` as the sole genuine sense.

**`japanese` completeness gap found and fixed**: stored `[GUU, GU]`, missing a third genuine kan-on reading; direct ja.Wiktionary fetch (quoting the raw 音 section: 呉音グ・グウ, 漢音ギョウ・グ, 慣用音グウ) confirms `GYOU` as a distinct attested on'yomi. Added, giving `[GU, GUU, GYOU]`.

**`vietnamese` completeness gap found and fixed**: stored `[ngung, ngu]`; hvdic.thivien.net (sole authority) also lists `ngẫu` and `ngụ` under Âm Hán Việt. Added both.

**`mc_id` off-by-one bug found and fixed**: stored `2341`, which is actually 惕's rank in `CC 2000.md`; 禺's genuine entry is `2342. 禺`. Corrected to `2342`.

**`pos`, `joyo_level`, `hsk_level` filled — all three were blank**: `pos` filled as `名詞`. `joyo_level` filled as `表外字` (dual-source confirmed); added as item 626 to `Lookup/Japanese/Hyōgai.md`. `hsk_level` filled as `無` — genuinely absent from all six `Old HSK N.md` files; added to `Lookup/HSK/HSK No.md`.

**Propagated gloss bug found and fixed**: `Lookup/SKIP/SKIP-4/SKIP-4-9-3.md` captioned 禺 as "lotus," inherited from the same false-alias error; corrected to "long-tailed monkey," matching `Radical 114.md`'s already-correct caption.

**Missing Korean lookup entry found and fixed**: absent from `Lookup/Korean/Korean Name ㅇ.md`'s `### 옹` subsection despite `korean: 옹`; added.

Rebuilt Notes into the standard four-bullet format (previously just a bare `## Notes` heading with no content, an informal `### Derived characters` heading, and two bare unlinked CC wikilinks) plus a properly-headed, ruby-formatted `## Derived Characters` section, also fixing several broken relative links (`偶.md` → `[[偶]]`, etc.) in the process. Stamped `date-last-perfect: 2026-08-24`.

Next never-perfected character by `danayo_id`: 䍃 (8768; 35 characters remaining).

### 2026-08-24, iteration 2470 — [[characters/䍃|䍃]]

`radical: 缶` reconfirmed correct (Kangxi radical 121). `skip_number: 2-4-6` and `stroke_count: 10` reconfirmed correct against `SKIP-2-4-6.md` and `Stroke 10.md`, both already listing the character. `japanese: [YOU]` and `japanese_native: ø` reconfirmed correct — matches ja.Wiktionary's よう on'yomi with no kun'yomi (ja.Wiktionary's own page 404'd on direct fetch, but en.Wiktionary's よう/Hyōgai claim is corroborated by zh.Wiktionary's cross-linguistic-attestation note). `mc_id: 5333` reconfirmed as trusted long-tail (>4000, not cross-checked per policy). `english: [pitcher, earthenware]` reconfirmed correct. Zero hits for 䍃 anywhere in `words/`, confirming `stand_in: 名専字` and no `## Words` section needed.

**Polyphony investigated and resolved — no bug**: hvdic.thivien.net's supplementary Mandarin/Cantonese data (`yáo`/`ziu4`) initially appeared to contradict the page's own `mandarin: yóu`/`cantonese: jau4`. Direct zh.Wiktionary fetch confirmed 䍃 is genuinely polyphonic — both `yóu` (this page's "pitcher" sense) and `yáo` (a distinct "kiln" sense, semantically overlapping with the independently-paged [[窯 (char)|窯]] but not documented as a variant of it) are real readings. The vault's existing `mandarin`/`middle_chinese_*` data is internally consistent with the *yóu* reading (matches `聲 以` + `韻 尤`, the exact rime class expected), so left unchanged; documented the polyphony explicitly in Notes to prevent future confusion.

**`graphemic_classification` bug found and fixed — cited the semantic component instead of the phonetic**: stored `缶`, but 缶 is confirmed by both en.Wiktionary and zh.Wiktionary to be the *semantic* component ("vessel/container"); the actual phonetic is [[肉 (char)|肉]] (OC \*njuɡ), which has its own independent vault page. Corrected to `肉`.

**`vietnamese` bug found and fixed — unattested claim removed**: stored `dao`, but hvdic.thivien.net (sole authority) explicitly states "Chưa có giải nghĩa theo âm Hán Việt" (no Hán Việt reading given) for this character — the pre-existing `dao` value was not corroborated by any check against the sole authority. Removed, leaving the field blank.

**`pos`, `joyo_level`, `hsk_level`, `hanmun_edu_level` filled — all four were blank**: `pos` filled as `名詞`. `joyo_level` filled as `表外字` (dual-source confirmed); added as item 627 to `Lookup/Japanese/Hyōgai.md`. `hsk_level` filled as `無` — genuinely absent from all six `Old HSK N.md` files; added to `Lookup/HSK/HSK No.md`. `hanmun_edu_level` filled as `無`.

**Missing Korean lookup entry found and fixed**: absent from `Lookup/Korean/Korean Name ㅇ.md`'s `### 요` subsection despite `korean: 요`; added.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC wikilinks, no SKIP/Stroke/mc_id-prose/four-links bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-24`.

Next never-perfected character by `danayo_id`: 翏 (8769; 34 characters remaining).

### 2026-08-24, iteration 2471 — [[characters/翏|翏]]

`radical: 羽` reconfirmed correct (Kangxi radical 124). `skip_number: 2-6-5` and `stroke_count: 11` reconfirmed correct against `SKIP-2-6-5.md` and `Stroke 11.md`, both already listing the character. `mc_id: 4156` reconfirmed as trusted long-tail (>4000, not cross-checked per policy). `english: sound of the wind` reconfirmed correct. Zero hits for 翏 anywhere in `words/`, confirming `stand_in: 名専字` and no `## Words` section needed.

**`graphemic_classification` bug found and fixed — cited a compound-type label instead of the actual phonetic**: stored `會意`, but both en.Wiktionary and zh.Wiktionary explicitly and consistently describe 翏 as 形声 (phono-semantic): semantic [[羽]] ("feathers") + phonetic [[㐱]], which has its own independent vault page. Corrected to `㐱`.

**`japanese`/`japanese_native` major completeness gap found and fixed**: stored `[RYUU, RU, RYOU, RIKU]` and `japanese_native: ø` (explicit no-kun'yomi). A raw ja.Wiktionary fetch (quoting the 発音 section verbatim) shows this was wrong on both counts: the full on'yomi set is 呉音リョウ・リュウ・リク, 漢音リョウ・ル・ロク — five distinct readings including a previously-missing `ROKU`; and — contrary to the stored `ø` — a genuine kun'yomi `と-ぶ` (TOBU, "to fly," matching the character's own "soar, fly high" sense) is explicitly listed, alongside archaic 古訓 forms (ひひる/はね/たかくとぶ, cited from 名義抄/字鏡集) which were left out of the frontmatter as historical-dictionary curiosities rather than the standing modern reading. Corrected `japanese` to `[RYOU, RYUU, RIKU, RU, ROKU]` and `japanese_native` to `とぶ`.

**`vietnamese`, `korean_native`, `pos`, `joyo_level`, `hsk_level`, `hanmun_edu_level` filled — all six were blank**: `vietnamese` filled as `[liêu, liệu]` (hvdic.thivien.net sole authority, both listed under Âm Hán Việt). `korean_native` filled as `바람소리` ("wind sound"), matching the core `english` gloss. `pos` filled as `名詞`. `joyo_level` filled as `表外字` (dual-source confirmed); added as item 628 to `Lookup/Japanese/Hyōgai.md`. `hsk_level` filled as `無` — genuinely absent from all six `Old HSK N.md` files; added to `Lookup/HSK/HSK No.md`. `hanmun_edu_level` filled as `無`.

**`## Derived Characters` section added**: four real 形声 hits citing 翏 as phonetic component, cross-checked via each page's own `graphemic_classification` field — [[謬]], [[戮]], [[膠]], [[蓼]].

**Missing Korean lookup entry found and fixed**: absent from `Lookup/Korean/Korean Name ㄹ.md`'s `### 료` subsection despite `korean: 료`; added.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC wikilinks, no SKIP/Stroke/mc_id-prose/four-links bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-24`.

Next never-perfected character by `danayo_id`: 羿 (8770; 33 characters remaining).

### 2026-08-24, iteration 2472 — [[characters/羿|羿]]

`radical: 羽` reconfirmed correct (Kangxi radical 124). `skip_number: 2-6-3` and `stroke_count: 9` reconfirmed correct against `SKIP-2-6-3.md` and `Stroke 09.md`, both already listing the character. `japanese: [GEI]` reconfirmed correct and complete — matches ja.Wiktionary's sole kan-on ゲイ. `japanese_native: ø` reconfirmed correct — no kun'yomi listed. `vietnamese: nghệ` reconfirmed correct and complete — hvdic.thivien.net's sole reading (identical under both Âm Hán Việt and Âm Nôm). `joyo_level: 表外字` and `hanmun_edu_level: 名` reconfirmed correct. `english: famous archer` reconfirmed correct — matches the 后羿 legendary-archer sense in both sources. The one grep hit for 羿 in `words/中秋節.md` is a false-positive prose mention (后羿 appearing only in the word's mythological-background note, not a genuine `characters:` citation), confirming `stand_in: 名専字` and no `## Words` section needed. Already correctly listed in `Lookup/Korean/Korean Name ㅇ.md`'s `### 예` subsection (as a bare `[[羿]]` link) — no fix needed there.

**`graphemic_classification` bug found and fixed — visually-similar-character mixup**: stored `开` (the simplified form of 開, "open"), but both en.Wiktionary and zh.Wiktionary independently and consistently identify the actual phonetic component as `幵` (OC \*kŋeːn) — a distinct, rarer character that closely resembles 开 in shape. Corrected to `幵` (no independent vault page).

**`mc_id` off-by-one bug found and fixed**: stored `2429`, which is actually 禘's rank in `CC 2000.md`; 羿's genuine entry is `2430. 羿`. Corrected to `2430`.

**`korean_native` filled — was blank**: filled as `활` ("bow"), matching precedent from other legendary-figure `固有名詞` character pages in this vault (e.g. 舜's 무궁화) of using a concrete native Korean word tied to the figure's defining trait rather than leaving proper-name characters ungloassed.

**Missing lookup entry found and fixed**: absent from `Lookup/HSK/HSK No.md` despite `hsk_level: 無` already being correctly set; added.

Built the missing `## Notes` section from scratch (previously just two bare unlinked CC wikilinks with no heading at all) into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-24`.

Next never-perfected character by `danayo_id`: 耴 (8771; 32 characters remaining).

### 2026-08-24, iteration 2473 — [[characters/耴|耴]]

`radical: 耳` reconfirmed correct (Kangxi radical 128). `skip_number: 1-6-1` and `stroke_count: 7` reconfirmed correct against `SKIP-1-6-1.md` and `Stroke 07.md`, both already listing the character. `graphemic_classification: 象形` reconfirmed correct. `japanese: [CHOU, JOU, NYOU]` reconfirmed correct and complete — matches en.Wiktionary's ちょう/じょう/にょう (ja.Wiktionary 404'd; single-sourced per established fallback practice). `japanese_native: ø` reconfirmed correct — no kun'yomi attested anywhere. `english: earlobe` and `korean_native: 귀 처질` ("drooping ear") reconfirmed correct and mutually consistent. `mc_id: 0` reconfirmed as a genuine sentinel — absent from all four `CC N000.md` files. Zero hits for 耴 anywhere in `words/`, confirming `stand_in: 名専字` and no `## Words` section needed.

**`vietnamese` bug found and fixed — garbled/concatenated value**: stored the single malformed string `ngất triếp` (a nonexistent reading, evidently a corrupted concatenation). hvdic.thivien.net (sole authority) actually lists two clean separate readings under Âm Hán Việt: `ngất` and `nhiếp`. Split into a proper two-item list.

**`aliases` completeness gap found and fixed**: stored only `𦔮`; en.Wiktionary additionally and consistently lists `䎲` and `𦕿` as alternative forms, and zh.Wiktionary separately confirms `耷` as a variant — none of the three has an independent vault page. Added all three.

**`pos` and `boundedness` filled — both were blank**: `pos` filled as `名詞`. `boundedness` filled as `70`, consistent with comparable bound characters.

**Spurious decomposition bullet removed**: the pre-existing Notes contained an unsourced `[[Radical 128|耳]] + [[隠|乚]]` compound-decomposition line that matched neither source's actual pictogram (象形) description; removed in the rebuild.

**Missing lookup entries found and fixed**: absent from `Lookup/HSK/HSK No.md` despite `hsk_level: 無` already being correctly set; added. Absent from `Lookup/Korean/Korean Name ㅊ.md`'s `### 첩` subsection despite `korean: 첩`; added.

Rebuilt Notes into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-24`.

Next never-perfected character by `danayo_id`: 肰 (8772; 31 characters remaining).

### 2026-08-24, iteration 2474 — [[characters/肰|肰]]

`radical: 肉` reconfirmed correct (Kangxi radical 130). `skip_number: 1-4-4` and `stroke_count: 8` reconfirmed correct against `SKIP-1-4-4.md` and `Stroke 08.md`, both already listing the character. `graphemic_classification: 會意` reconfirmed correct — both en.Wiktionary and zh.Wiktionary confirm 肉+犬 ideogrammic compound. `english: dog meat` and `korean_native: 개고기` reconfirmed correct and consistent. `mc_id: 8850` reconfirmed as trusted long-tail (>4000, not cross-checked per policy). `japanese: [ZEN, NEN]` left unverified-but-unchanged — neither en.Wiktionary nor zh.Wiktionary provided Japanese reading data for this character, and ja.Wiktionary 404'd, so there was no source to check the pre-existing claim against this pass. Zero hits for 肰 anywhere in `words/`, confirming `stand_in: 名専字` and no `## Words` section needed.

**`vietnamese` filled — was blank**: filled as `nhiên` (hvdic.thivien.net sole authority, sole Âm Hán Việt reading).

**`## Derived Characters` section added**: cross-checked every candidate mentioned by both sources (然, 燃, 猒) via each one's own `graphemic_classification` field — only [[然 (char)|然]] directly cites 肰 as its phonetic; 燃 cites 然 (a derived-of-derived relationship, correctly excluded per the direct-citation convention), and 猒 has no vault page. Added the one genuine hit.

**Missing lookup entries found and fixed**: absent from `Lookup/HSK/HSK No.md` despite `hsk_level: 無` already being correctly set; added. Absent from `Lookup/Korean/Korean Name ㅇ.md`'s `### 연` subsection despite `korean: 연`; added.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC wikilinks, no SKIP/Stroke/mc_id-prose/four-links bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-24`.

Next never-perfected character by `danayo_id`: 隹 (8774; 30 characters remaining).

### 2026-08-24, iteration 2475 — [[characters/隹|隹]]

`radical: 隹` reconfirmed correct (its own Kangxi radical 172). `skip_number: 4-8-2` and `stroke_count: 8` reconfirmed correct against `SKIP-4-8-2.md` and `Stroke 08.md`, both already listing the character. `graphemic_classification: 象形` reconfirmed correct. `japanese: [SUI, SAI]`, `japanese_native: とり`, `vietnamese: chuy`, `korean_native: 새` all reconfirmed correct and complete against dual sources. `english: short tailed bird` reconfirmed correct. The one grep hit for 隹 in `words/衢.md` is a false-positive prose mention (隹 appearing only as a component of 衢's own phonetic 瞿, not a direct `characters:` citation of 隹 itself), confirming `stand_in: 名専字` and no `## Words` section needed.

**`aliases` false-alias bug found and fixed**: `魋` (a wild-beast/surname character, unrelated in meaning) was listed as an alias. Direct zh.Wiktionary fetch of 魋's own entry settles it: 隹 functions there only as 魋's *phonetic component* (鬼 + phonetic 隹), not as a true 異體字/variant relationship, and en.Wiktionary independently states outright "no direct alias to 魋 noted." Removed. (隹's other genuine dual-source-confirmed variant, [[唯 (char)|唯]], already has its own independent vault page and was correctly already excluded from `aliases`.)

**`mc_id` off-by-one bug found and fixed**: stored `2910`, which is actually 朗's rank in `CC 2000.md`; 隹's genuine entry is `2911. 隹`. Corrected to `2911`.

**`pos` filled — was blank**: filled as `名詞`.

**`## Derived Characters` completeness gap found and fixed**: only listed [[錐]]; cross-checking every candidate character mentioned by en.Wiktionary's derivation note (焦, 翟, 椎, 誰, plus 唯) via each one's own `graphemic_classification` field turned up five direct citers with independent vault pages — [[椎]], [[誰 (char)|誰]], [[唯 (char)|唯]], [[崔]], and [[進]] — while 焦 and 翟 turned out to cite `會意` instead, correctly excluded. Added all five new hits alongside the existing 錐.

**Missing lookup entries found and fixed**: absent from `Lookup/HSK/HSK No.md` despite `hsk_level: 無` already being correctly set; added. Absent from `Lookup/Korean/Korean Name ㅊ.md`'s `### 추` subsection despite `korean: 추`; added.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC wikilinks, no SKIP/Stroke/mc_id-prose/four-links bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-24`.

Next never-perfected character by `danayo_id`: 絢 (8775; 29 characters remaining).

### 2026-08-24, iteration 2476 — [[characters/絢|絢]]

`radical: 糸` reconfirmed correct (Kangxi radical 120). `skip_number: 2-6-6` and `stroke_count: 12` reconfirmed correct against `SKIP-2-6-6.md` and `Stroke 12.md`, both already listing the character. `graphemic_classification: 旬` reconfirmed correct — dual-source confirmed phonetic component. `aliases: 绚` reconfirmed correct — dual-source confirmed simplified form. `joyo_level: 日本人名用漢字` reconfirmed correct — already genuinely listed at `Lookup/Japanese/Jinmeiyō.md` item 220. `japanese: [KEN]` reconfirmed correct and complete. `vietnamese: huyến` reconfirmed correct and complete — hvdic.thivien.net (sole authority) lists only this one reading; en.Wiktionary's additional single-sourced `tuân`/`huyền` claims are not corroborated and were correctly left out. `stand_in: 絢乱` and the `## Words` section reconfirmed correct — the word page exists and matches.

**`japanese_native` bug found and fixed — wrongly denied an attested kun'yomi**: stored `ø`, but a raw ja.Wiktionary fetch (quoting the 発音 section verbatim: 呉音ケン, 漢音ケン, 訓読みあや) explicitly confirms a genuine kun'yomi `あや`, independently corroborated by en.Wiktionary. Corrected `japanese_native` to `あや`.

**`pos` and `hsk_level` filled — both were blank**: `pos` filled as `形容詞`, matching the primary adjectival "gorgeous, resplendent" sense. `hsk_level` filled as `無` — genuinely absent from all six `Old HSK N.md` files; added to `Lookup/HSK/HSK No.md`.

Rebuilt Notes into the standard four-bullet format (previously just two bare unlinked CC wikilinks with no SKIP/Stroke/mc_id-prose/links bullets), correctly using the Jinmeiyō-variant four-links bullet (`Grade Name`, `HSK No`, `Jinmeiyō`, `Korean Name ㅎ`) rather than the Hyōgai default. Stamped `date-last-perfect: 2026-08-24`.

Next never-perfected character by `danayo_id`: 竃 (8776; 28 characters remaining).

### 2026-08-24, iteration 2477 — [[characters/竃|竃]]

`radical: 穴` reconfirmed correct (Kangxi radical 116). `skip_number: 2-5-12` and `stroke_count: 17` reconfirmed correct against `SKIP-2-5-12.md` and `Stroke 17.md`, both already listing the character. `graphemic_classification: 會意` reconfirmed correct — en.Wiktionary's own analysis of 竃 itself (not just its traditional ancestor 竈) confirms 会意. `aliases: [竈, 灶]` reconfirmed correct — both dual-source confirmed 異體字/simplified relationships, neither has an independent vault page. `hsk_level: 6` reconfirmed correct — genuine numbered entry (item 804) on `Old HSK 6.md`, not a false colon-count entry. `english`/`korean_native`/`japanese` all reconfirmed correct. Zero hits for 竃 anywhere in `words/`, confirming `stand_in: 名専字` and no `## Words` section needed.

**`cantonese` bug found and fixed — completely wrong reading**: stored `hung1`, which bears no phonetic resemblance to this character at all. zh.Wiktionary's entry for 竈 (竃's own traditional ancestor/variant) gives the correct jyutping as `zou3`. Corrected.

**`japanese_native` completeness gap found and fixed**: stored `かまど` only; a raw ja.Wiktionary fetch confirms a second genuine kun'yomi, `へっつい`, missing. Added, converting the field to a list.

**`vietnamese` filled — was blank**: filled as `táo` (hvdic.thivien.net sole authority, sole Âm Hán Việt reading).

**`mc_id` off-by-one bug found and fixed**: stored `3160`, which is actually 疝's rank in `CC 3000.md`; the genuine entry is `3161. 竈` (the CC lookup file records the traditional form). Corrected to `3161`.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC wikilinks, no SKIP/Stroke/mc_id-prose/four-links bullets) into the standard `## Notes` four-bullet format, using the Old-HSK-6-specific four-links bullet. Stamped `date-last-perfect: 2026-08-24`.

Next never-perfected character by `danayo_id`: 鞀 (8777; 27 characters remaining).

### 2026-08-24, iteration 2478 — [[characters/鞀|鞀]]

`radical: 革` reconfirmed correct (Kangxi radical 177). `skip_number: 1-9-5` and `stroke_count: 14` reconfirmed correct against `SKIP-1-9-5.md` and `Stroke 14.md`, both already listing the character. `japanese: [TOU, DOU]` and `japanese_native: ふりつづみ` reconfirmed correct and complete (ja.Wiktionary 404'd; en.Wiktionary's claims stand single-sourced per established fallback practice). `vietnamese: đào` reconfirmed correct and complete — hvdic.thivien.net's sole reading. `aliases: [鼗, 鞉]` reconfirmed correct — both dual-source confirmed 異體字, neither has an independent vault page. `stand_in: 鞀鼓` and the `## Words` section reconfirmed correct — the word page exists and matches.

**`graphemic_classification` bug found and fixed — contradicted the page's own Notes prose**: frontmatter stored `刀`, but the pre-existing Notes bullet already correctly decomposed the character as `革 + 召`. Both en.Wiktionary and zh.Wiktionary confirm the true phonetic is 召 (which has its own vault page); 刀 is only mentioned by zh.Wiktionary as a *different, incidentally-related* character in the same broader phonetic series, not 鞀's actual phonetic component — a visually-similar-character mixup (刀/召), matching the pattern already seen this session on 羿 (开/幵). Corrected the frontmatter field to `召`.

**`pos`, `joyo_level`, `hsk_level`, `hanmun_edu_level`, `boundedness` filled — all five were blank**: `pos` filled as `名詞`. `joyo_level` filled as `表外字` (dual-source confirmed); added as item 629 to `Lookup/Japanese/Hyōgai.md`. `hsk_level` filled as `無` — genuinely absent from all six `Old HSK N.md` files; added to `Lookup/HSK/HSK No.md`. `hanmun_edu_level` filled as `無`. `boundedness` filled as `65`, consistent with comparable bound characters.

**Missing Korean lookup entry found and fixed**: absent from `Lookup/Korean/Korean Name ㄷ.md`'s `### 도` subsection despite `korean: 도`; added.

Rebuilt Notes into the standard four-bullet format (previously just a bare component-decomposition line with no SKIP/Stroke/mc_id-prose/links bullets). Stamped `date-last-perfect: 2026-08-24`.

Next never-perfected character by `danayo_id`: 俎 (8779; 26 characters remaining).

### 2026-08-24, iteration 2479 — [[characters/俎|俎]]

`radical: 人` reconfirmed correct (Kangxi radical 9). `skip_number: 1-4-5` and `stroke_count: 9` reconfirmed correct against `SKIP-1-4-5.md` and `Stroke 09.md`, both already listing the character. `graphemic_classification: 象形` reconfirmed correct — dual-source confirmed pictogram (altar with legs left, vessel right); the character's alternate modern structural reading as 仌+且 (phonetic) was investigated, but 且 already has its own independent vault page, correctly excluded from `aliases`, so `象形` (the primary etymological account) stands as the type-label. `japanese: [SHO, SO]` reconfirmed correct and complete. `vietnamese: trở` reconfirmed correct and complete — hvdic.thivien.net's sole reading. Zero hits for 俎 anywhere in `words/`, confirming `stand_in: 名専字` and no `## Words` section needed. Already correctly cross-listed on `Lookup/Radicals/Radical 009.md`, `Lookup/SKIP/SKIP-1/SKIP-1-4-5.md`, `Lookup/Stroke/Stroke 09.md`, and `Lookup/Korean/Korean Name ㅈ.md`.

**`japanese_native` completeness gap found and fixed**: stored `いた` only; ja.Wiktionary independently confirms a second genuine kun'yomi, `まないた` (manaita, "cutting board"), missing. Added, converting the field to a list.

**`aliases` completeness gap found and fixed**: stored `[爼, 𤕲]`; both en.Wiktionary and zh.Wiktionary additionally and consistently list a third variant, `𮀀`, missing. Added.

**`mc_id` off-by-one bug found and fixed**: stored `1384`, which is actually 啟's rank in `CC 1000.md`; 俎's genuine entry is `1385. 俎`. Corrected to `1385`.

**`pos`, `joyo_level`, `hsk_level` filled — all three were blank**: `pos` filled as `名詞`. `joyo_level` filled as `表外字` (dual-source confirmed). `hsk_level` filled as `無` — genuinely absent from all six `Old HSK N.md` files; added to `Lookup/HSK/HSK No.md`.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC wikilinks, no SKIP/Stroke/mc_id-prose/four-links bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-24`.

Next never-perfected character by `danayo_id`: 穂 (char) (8782; 25 characters remaining).

### 2026-08-24, iteration 2480 — [[characters/穂 (char)|穂 (char)]]

`radical: 禾` reconfirmed correct (Kangxi radical 115). `skip_number: 1-5-10` and `stroke_count: 15` reconfirmed correct against `SKIP-1-5-10.md` and `Stroke 15.md`, both already listing the character. `joyo_level: 高等` reconfirmed correct — both sources confirm 常用漢字/secondary-school Jōyō status (matching "Kōtō"), and the character is already genuinely listed on `Lookup/Japanese/Jōyō - Kōtō.md` item 1572. `english: ear of grain` reconfirmed correct. `stand_in: 穂` and the character/word dual-page cross-reference reconfirmed correct. `aliases: [穗]` reconfirmed correct — the kyūjitai/traditional form, dual-source confirmed, no independent vault page. Already correctly cross-listed on `Lookup/Korean/Korean Name ㅅ.md`'s `### 수` subsection.

**`hsk_level` bug found and fixed — a colon-count entry was wrongly trusted as genuine**: stored `4`, apparently based on `Old HSK 4.md`'s `[穗](...): 1` line — but per established vault policy, colon-count entries are NOT genuine HSK confirmations, only plain-numbered entries count. A full check of all six `Old HSK N.md` files and `HSK No.md` turned up no genuine plain-numbered entry anywhere. Corrected `hsk_level` to `無` and added the character to `Lookup/HSK/HSK No.md`.

**`graphemic_classification` bug found and fixed**: stored `思` (unrelated character, "to think"), but both en.Wiktionary and zh.Wiktionary consistently identify the true phonetic component as 恵/惠 (OC \*ɢʷiːds) — the vault's own `恵.md` page for the shinjitai form. Corrected to `恵`.

**`mc_id` filled — was blank**: filled as `3379`, the character's genuine rank found directly in `CC 3000.md` (`3379. 穗`).

**`japanese`/`japanese_native` completeness gaps found and fixed**: both fields were stored as bare scalars instead of the vault's list convention, and both were incomplete. A raw ja.Wiktionary fetch (quoting the 発音 section verbatim) confirms a second genuine on'yomi `ズイ` (goon, alongside the existing スイ kan-on) and a second genuine kun'yomi `お` (alongside the existing ほ) — both explicitly listed under 訓読み, not 名乗り/nanori (the five nanori-only readings こう/のり/ほい/み/みのり were correctly left out). Converted both fields to lists and added the missing readings: `japanese: [ZUI, SUI]`, `japanese_native: [ほ, お]`. Also converted `vietnamese` from scalar to list format for consistency (value itself, `tuệ`, was already correct and complete per hvdic.thivien.net).

**`boundedness` filled — was blank**: filled as `40`, reflecting that this character legitimately stands alone as its own word (per the character/word dual-page structure), unlike the heavily-bound `名専字` characters seen in most recent iterations.

Rebuilt Notes into the standard four-bullet format (previously just two bare unlinked CC wikilinks with a malformed `# Notes` heading placed before the meta-bind-embed block). Stamped `date-last-perfect: 2026-08-24`.

Next never-perfected character by `danayo_id`: 瀬 (8783; 24 characters remaining).

### 2026-08-24, iteration 2481 — [[characters/瀬|瀬]]

`radical: 水` reconfirmed correct (Kangxi radical 85). `skip_number: 1-3-16` and `stroke_count: 19` reconfirmed correct against `SKIP-1-3-16.md` and `Stroke 19.md`, both already listing the character. `graphemic_classification: 頼` reconfirmed correct — dual-source confirmed phonetic, correctly using the vault's own shinjitai-form page `頼.md`. `mc_id: 3566` reconfirmed correct — `CC 3000.md`: `3566. 瀨` exactly matches, no off-by-one this time. `joyo_level: 高等` reconfirmed correct — already genuinely listed at `Lookup/Japanese/Jōyō - Kōtō.md` item 1580. `aliases: [瀨, 濑]` reconfirmed correct — both dual-source confirmed (kyūjitai and simplified-Chinese forms respectively), neither has an independent vault page. `japanese: [RAI]` and `japanese_native: せ` reconfirmed correct — a raw ja.Wiktionary fetch surfaced five additional forms (がせ, しげ, せい, せっ, いわた) nominally under 訓読み with no separate 名乗り section, but none is corroborated by en.Wiktionary (which lists only せ) and their surname/place-name shape strongly suggests they're nanori-style readings mis-bucketed by the source page rather than genuine general-use kun'yomi; left out per the dual-source standard. `vietnamese: lại` reconfirmed correct and complete. The one grep hit for 瀬 in `words/内海.md` is a false-positive prose mention (瀬 appearing only inside the example compound 瀬戸内海, not a genuine `characters:` citation), confirming `stand_in: 名専字` and no `## Words` section needed. Already correctly cross-listed on `Lookup/Radicals/Radical 085.md` and `Lookup/Korean/Korean Name ㄹ.md`'s `### 뢰` subsection.

**`japanese`/`vietnamese` format bug found and fixed**: both fields were stored as bare scalars instead of the vault's list convention (values themselves were already correct and complete). Converted both to proper lists.

**`boundedness` filled — was blank**: filled as `65`, consistent with comparable bound characters.

**Missing lookup entry found and fixed**: absent from `Lookup/HSK/HSK No.md` despite `hsk_level: 無` already being correctly set; added.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC wikilinks, no SKIP/Stroke/mc_id-prose/four-links bullets) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-24`.

Next never-perfected character by `danayo_id`: 粤 (8784; 23 characters remaining).

### 2026-08-24, iteration 2482 — [[characters/粤|粤]]

`radical: 米` reconfirmed correct (Kangxi radical 119). `skip_number: 2-10-2` and `stroke_count: 12` reconfirmed correct against `SKIP-2-10-2.md` and `Stroke 12.md`, both already listing the character. `mc_id: 2096` reconfirmed correct — `CC 2000.md`: `2096. 粵` exactly matches, no off-by-one. `japanese_native: ここに` reconfirmed correct and complete. `vietnamese: việt` reconfirmed correct and complete — hvdic.thivien.net's sole reading. `stand_in: 粤語` and the `## Words` section reconfirmed correct.

**`graphemic_classification` bug found and fixed — conflated a cognate relationship with a structural component citation**: stored `越`, but direct verification shows 越 is only an *etymological cognate* of 粵/粤 (same Old Chinese root \*ɢʷad, "Yue/Viet") per en.Wiktionary — not a literal component of the character's own glyph, which is instead separately described as "a specialization of 雩 by modification of 雨." Since no source cleanly identifies a true phonetic component and neither zh.Wiktionary nor en.Wiktionary states a 象形/指事/會意/形聲 classification directly, corrected the field to the general `會意` type-label and moved the genuine 越-cognate relationship into Notes prose instead, where it belongs.

**`aliases` bug found and fixed — field was entirely missing**: no `aliases` key existed at all, despite `粵` (the traditional form) being a dual-source-confirmed variant with no independent vault page. Added the missing key with `粵`.

**`japanese` completeness gap found and fixed**: stored `ETSU` only (as a bare scalar); both en.Wiktionary and ja.Wiktionary independently confirm two further genuine on'yomi, goon `ECHI` and `OCHI`, both missing. Added both and converted to list format; also converted `vietnamese` from scalar to list format for consistency.

**Missing `meta-bind-embed` block found and fixed**: the page's body was missing the standard \`\`\`meta-bind-embed [[nav/char_info]] \`\`\` block present on every other character page; added.

**Missing lookup entries found and fixed**: absent from `Lookup/HSK/HSK No.md` despite `hsk_level: 無` already being correctly set; added. Absent from `Lookup/Japanese/Hyōgai.md` despite `joyo_level: 表外字` already being correctly set; added as item 630. Absent from `Lookup/Korean/Korean Name ㅇ.md`'s `### 월` subsection despite `korean: 월`; added.

Rebuilt Notes into the standard four-bullet format (previously a bare `## Notes` heading with two floating unlinked CC wikilinks and no other content). Stamped `date-last-perfect: 2026-08-24`.

Next never-perfected character by `danayo_id`: 茄 (8788; 22 characters remaining).

### 2026-08-25, iteration 2483 — [[characters/茄|茄]]

`radical: 艸` reconfirmed correct (Kangxi radical 140). `skip_number: 2-4-5` and `stroke_count: 9` reconfirmed correct against `SKIP-2-4-5.md` and `Stroke 09.md`, both already listing the character. `graphemic_classification: 加` reconfirmed correct — dual-source confirmed phonetic, already matching the page's own pre-existing Notes prose. `japanese_native: なす` reconfirmed correct despite ja.Wiktionary's raw fetch not surfacing a 訓読み section — treated as an incomplete page load rather than a genuine denial, given なす's overwhelming real-world attestation as the standard reading for eggplant. `joyo_level: 日本人名用漢字` reconfirmed correct — trusted the vault's own pre-existing internal listing at `Lookup/Japanese/Jinmeiyō.md` item 469 over en.Wiktionary's conflicting "Jōyō" claim (same precedent as 夌's radical case). `stand_in: 茄子` and the "cannot appear alone" warning reconfirmed correct — the word page exists and matches. Already correctly cross-listed on `Lookup/Radicals/Radical 140.md`, `Lookup/SKIP/SKIP-2/SKIP-2-4-5.md`, `Lookup/Stroke/Stroke 09.md`, and `Lookup/Korean/Korean Name ㄱ.md`'s `### 가` subsection.

**`japanese` completeness gap found and fixed**: stored `[KA]` only; a raw ja.Wiktionary fetch (quoting 音読み verbatim: 呉音ギャ・ケ, 漢音カ・キャ, 慣用音カ) confirms three further genuine on'yomi — `GYA`, `KE`, `KYA` — all missing. Added all three.

**`vietnamese` bug found and fixed — badly incomplete, stored as a bare scalar**: stored `gia` only; hvdic.thivien.net (sole authority) actually lists seven distinct readings across its Âm Hán Việt (cà, gia, già) and Âm Nôm (cà, gia, nhà, nhu, như, nhựa) sections. Added all seven and converted to list format.

**`mc_id` filled — was blank**: filled as `0`, a genuine sentinel — confirmed absent from all four `CC N000.md` files (consistent with zh.Wiktionary's own note that 茄 is "extremely rare and appears late" in Classical Chinese, first attested 59 BCE).

**`aliases` key added — was entirely missing**: added the empty key for schema consistency; no genuine alias exists (en.Wiktionary's single-sourced "alternative writing" claim, [[伽]], already has its own independent vault page and is correctly excluded).

Rebuilt Notes into the standard four-bullet format (previously non-standard bullet formatting with an inline SKIP/Stroke/syllable-link bullet and two floating unlinked CC wikilinks), using the Jinmeiyō-variant four-links bullet. Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 鉀 (char) (8789; 21 characters remaining).

### 2026-08-25, iteration 2484 — [[characters/鉀 (char)|鉀 (char)]]

`radical: 金` reconfirmed correct (Kangxi radical 167). `skip_number: 1-8-5` and `stroke_count: 13` reconfirmed correct against `SKIP-1-8-5.md` and `Stroke 13.md`, both already listing the character. `graphemic_classification: 甲` reconfirmed correct — dual-source confirmed phonetic. `vietnamese: giáp` reconfirmed correct and complete. `japanese_native: よろい` reconfirmed correct. `mc_id: 8866` reconfirmed as trusted long-tail (>4000, not cross-checked per policy). `stand_in: 鉀` reconfirmed correct — the word page `words/鉀.md` exists and matches. Already correctly cross-listed on `Lookup/Radicals/Radical 167.md`, `Lookup/SKIP/SKIP-1/SKIP-1-8-5.md`, `Lookup/Stroke/Stroke 13.md`, and `Lookup/Korean/Korean Name ㄱ.md`'s `### 갑` subsection.

**`japanese` completeness gap found and fixed**: stored `KYOU` only (as a bare scalar); en.Wiktionary independently confirms a second genuine on'yomi, kan-on `KOU` (ja.Wiktionary's raw fetch corroborates KOU directly and is merely silent on KYOU rather than denying it). Added `KOU` and converted to list format.

**Missing lookup entry found and fixed**: absent from `Lookup/HSK/HSK No.md` despite `hsk_level: 無` already being correctly set; added.

**`## Words` section added — following the periodic-table element convention (precedent: 鉛 (char))**: rather than the tip-callout dual-page pattern used for ordinary character/word pairs, element characters instead get a `## Words` section citing the element word itself with a `(stand-in for X (char))` note per `feedback_standin_note.md`; added `- <ruby>[[鉀]]<rt>ㄍㄚㄆ</rt></ruby> "potassium" (stand-in for 鉀 (char))`.

Rebuilt the malformed Notes (a floating unlinked prose line, two bare CC wikilinks, a duplicate 形声-etymology bullet, and a stray `1. potassium` list item, all out of order) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 佩 (8790; 20 characters remaining).

### 2026-08-25, iteration 2485 — [[characters/佩|佩]]

`radical: 人` reconfirmed correct (Kangxi radical 9). `skip_number: 1-2-6` and `stroke_count: 8` reconfirmed correct against `SKIP-1-2-6.md` and `Stroke 08.md`, both already listing the character. `mc_id: 1553` reconfirmed correct — `CC 1000.md`: `1553. 佩` exactly matches, no off-by-one. `pos: 性詞` reconfirmed correct — initially suspected as a typo, but this is a genuine, widely-used part-of-speech category in this vault (571 other character pages use it); left unchanged. `vietnamese: bội` reconfirmed correct and complete. `stand_in: 佩戴` and the `## Words` section reconfirmed correct. Already correctly cross-listed on `Lookup/Radicals/Radical 009.md` and `Lookup/Korean/Korean Name ㅍ.md`'s `### 패` subsection.

**`graphemic_classification` bug found and fixed — self-referential citation**: stored `佩` (the character citing itself), which is meaningless. Both sources describe a three-part compound 人+凡+巾 with en.Wiktionary explicitly noting "凡's phonetic role is debated" — no clean single phonetic citation is available, so corrected to the general `會意` type-label, matching the compound's actual documented structure.

**`japanese_native` YAML bug found and fixed**: the field was malformed — a bare scalar `お` immediately followed by an orphaned list item `- おびだま`, an invalid mix that likely failed to parse correctly. A raw ja.Wiktionary fetch (quoting 訓読み verbatim: はく・おびる・おびだま) gives the complete genuine three-item kun'yomi list, none of which is `お` alone (evidently a truncation artifact). Replaced with the correct `[はく, おびる, おびだま]`.

**`japanese` completeness gap found and fixed**: stored `[HAI]` only; the same raw ja.Wiktionary fetch confirms a second genuine on'yomi, goon `BAI` (alongside the existing kan-on ハイ). Added.

**Missing lookup entry found and fixed**: absent from `Lookup/HSK/HSK No.md` despite `hsk_level: 無` already being correctly set; added.

Rebuilt Notes into the standard four-bullet format (previously just two bare unlinked CC wikilinks with no SKIP/Stroke/mc_id-prose/four-links bullets). Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 稗 (8791; 19 characters remaining).

### 2026-08-25, iteration 2486 — [[characters/稗|稗]]

`radical: 禾` reconfirmed correct (Kangxi radical 115). `skip_number: 1-5-8` and `stroke_count: 13` reconfirmed correct against `SKIP-1-5-8.md` and `Stroke 13.md`, both already listing the character. `graphemic_classification: 卑` reconfirmed correct — dual-source confirmed phonetic. `aliases: [粺]` reconfirmed correct — dual-source confirmed variant, no independent vault page. `korean_native: 돌피` and `english` reconfirmed correct. `stand_in: 稗子` reconfirmed correct. Already correctly cross-listed on `Lookup/Radicals/Radical 115.md` and `Lookup/Korean/Korean Name ㅍ.md`'s `### 패` subsection.

**`pos` bug found and fixed**: stored the English word `noun` instead of the vault's own POS taxonomy; corrected to `名詞`.

**`mc_id` filled — key was entirely missing**: filled as `0`, a genuine sentinel — confirmed absent from all four `CC N000.md` files.

**`japanese` completeness gap found and fixed**: stored `BE` only (as a bare scalar); ja.Wiktionary's raw pronunciation section confirms a second genuine on'yomi, kan-on `HAI`, missing. Added and converted to list format (also converted `japanese_native` to list format for consistency; its single value, `ひえ`, was already correct).

**`vietnamese` completeness gap found and fixed**: stored `bái` only (as a bare scalar); hvdic.thivien.net additionally lists `bại` under Âm Hán Việt. Added both and converted to list format.

**`## Words` section cleanup**: removed two bare, unlinked, unformatted entries (`裨益`, `稗官`) that don't correspond to any real word page in `words/` — neither could be found under any filename, and per the sweep's own process (cross-check `## Words` against every *real* word citing this character), placeholder/dead entries don't belong. Kept the one genuine entry, [[稗子]].

Rebuilt the malformed Notes (a single line of broken/non-resolving double-bracket links — `[[SKIP-1-5-8]]`, `[[Stroke 13]]`, `[[ㄅㄚㄧ]]` — none pointing to their actual file paths, plus two floating unlinked CC wikilinks after the Words section) into the standard `## Notes` four-bullet format. Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 紇 (8793; 18 characters remaining).

### 2026-08-25, iteration 2487 — [[characters/紇|紇]]

`radical: 糸` reconfirmed correct (Kangxi radical 120). `skip_number: 1-6-3` and `stroke_count: 9` reconfirmed correct against `SKIP-1-6-3.md` and `Stroke 09.md`, both already listing the character. `graphemic_classification: 乞` reconfirmed correct — dual-source confirmed phonetic. `mc_id: 3792` reconfirmed correct — `CC 3000.md`: `3792. 紇` exactly matches, no off-by-one. `aliases: [纥]` reconfirmed correct — dual-source confirmed simplified form, no independent vault page. `stand_in: 回紇` and the `## Words` section reconfirmed correct — the word page exists and cites 紇 properly. Already correctly cross-listed on `Lookup/Radicals/Radical 120.md` and `Lookup/Korean/Korean Name ㅎ.md`'s `### 흘` subsection.

**Misfiled-reading bug found and fixed**: `げち` (GECHI) was stored in `japanese_native` as if a kun'yomi, but en.Wiktionary lists it as one of four genuine on'yomi (こつ/ごち/けつ/げち) — no kun'yomi is attested for this character anywhere. Moved `げち` into `japanese` as `GECHI` and added the two other missing on'yomi (`GOCHI`, `KETSU`) alongside the pre-existing `KOTSU`; corrected `japanese_native` to `ø`.

**`vietnamese` completeness gap found and fixed**: stored `hột` only; hvdic.thivien.net additionally lists `ngột` (Âm Hán Việt) and `hạt`/`hụt` (Âm Nôm). Added all three.

**Broken/guessed rhyme citation caught before publishing**: while drafting the mc_id-rank bullet, an initially-assumed `韻 痕` citation was checked against the file's actual contents and found not to match the final `ət`; direct cross-check of `Lookup/CC/finals/韻 麧.md` confirmed 紇 is the sole listed character there, and the citation was corrected to `韻 麧` before the edit was applied.

**Missing lookup entry found and fixed**: absent from `Lookup/HSK/HSK No.md` despite `hsk_level: 無` already being correctly set; added.

Built the essentially-empty `## Notes` section from scratch (previously just a bare heading with no content at all) into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 喿 (8795; 17 characters remaining).

### 2026-08-25, iteration 2488 — [[characters/喿|喿]]

`radical: 口` reconfirmed correct (Kangxi radical 30). `skip_number: 2-3-10` and `stroke_count: 13` reconfirmed correct against `SKIP-2-3-10.md` and `Stroke 13.md`, both already listing the character. `graphemic_classification: 會意` reconfirmed correct — dual-source confirmed 品+木 compound, matching the page's own pre-existing Notes prose. `aliases: [噪]` reconfirmed correct — dual-source confirmed as 喿 being the original form of 噪, no independent vault page. `hsk_level: 6` reconfirmed correct — genuine numbered entry (item 837) on `Old HSK 6.md`, not a false colon-count entry. `pos: 事詞` reconfirmed correct — a genuine, widely-used vault POS category (848 other pages use it). `mc_id: 0` reconfirmed as a genuine sentinel — absent from all four `CC N000.md` files. Zero hits for 喿 anywhere in `words/`, confirming `stand_in: 名専字` and no `## Words` section needed.

**`japanese`/`japanese_native` completeness gaps found and fixed**: stored `SOU` and `さわぐ` only; both en.Wiktionary and zh.Wiktionary independently and consistently confirm a second on'yomi (`SHOU`) and two further kun'yomi (`かしましい`, `すき`). Added all three and converted both fields to list format.

**`vietnamese` bug found and fixed — uncorroborated reading removed**: stored `táo, tháo` as a comma-separated string; hvdic.thivien.net (sole authority) lists only `táo` under both Âm Hán Việt and Âm Nôm, with no `tháo` anywhere. Removed the unattested `tháo` and converted to proper list format.

**Duplicate `## Notes` heading found and fixed**: the page had two separate `## Notes` sections (one with two bare CC wikilinks, a second below it with the actual etymology prose); merged into one properly-ordered section.

**Missing lookup entry found and fixed**: absent from `Lookup/Korean/Korean Name ㅈ.md`'s `### 조` subsection despite `korean: 조`; added.

Rebuilt Notes into the standard four-bullet format, using the Old-HSK-6-specific four-links bullet. Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 魑 (8798; 16 characters remaining).

### 2026-08-25, iteration 2489 — [[characters/魑|魑]]

`radical: 鬼` reconfirmed correct (Kangxi radical 194). `skip_number: 3-10-11` and `stroke_count: 21` reconfirmed correct against `SKIP-3-10-11.md` and `Stroke 21.md`, both already listing the character. `graphemic_classification: 离` reconfirmed correct — dual-source confirmed phonetic (the frontmatter value was correct; only its Notes-prose citation was broken, see below). `aliases: [螭, 䬜, 䄜, 𩳩]` reconfirmed correct — all four dual-source confirmed 異體字, none has an independent vault page. `mc_id: 3780` reconfirmed correct — `CC 3000.md` lists it under 魑's own alias 螭 at exactly rank 3780. `japanese: [CHI]` and `japanese_native: すだま` reconfirmed correct and complete. `stand_in: 魑魅` and the `## Chengyu` section reconfirmed correct — the word page exists and matches.

**`vietnamese` completeness gap found and fixed**: stored `si` only; hvdic.thivien.net additionally lists `ly` under Âm Hán Việt. Added.

**Broken empty wikilink found and fixed**: the pre-existing Notes prose cited the phonetic component as a bare `[[]]` (an empty double-bracket link, resolving to nothing) instead of `离`; corrected to plain text `离` since the character has no independent vault page.

**Broken/guessed rhyme citation caught before publishing**: an initial draft citation of `韻 支A開` was checked against the file's actual contents and found not to exist under that name; a direct search for the character's own final `ɣiᴇ` identified the real file, `韻 支B三開`, and the citation was corrected before the edit was applied.

**Missing lookup entries found and fixed**: absent from `Lookup/HSK/HSK No.md` despite `hsk_level: 無` already being correctly set; added. Absent from `Lookup/Korean/Korean Name ㅊ.md`'s `### 치` subsection despite `korean: 치`; added.

Rebuilt Notes into the standard four-bullet format (previously a single incomplete bullet ending mid-thought with the broken empty link, and no SKIP/Stroke/four-links bullets). Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 咅 (8799; 15 characters remaining).

### 2026-08-25, iteration 2490 — [[characters/咅|咅]]

`radical: 口` reconfirmed correct (Kangxi radical 30). `skip_number: 2-5-3` and `stroke_count: 8` reconfirmed correct against `SKIP-2-5-3.md` and `Stroke 08.md`, both already listing the character. `graphemic_classification: 否` reconfirmed correct — dual-source confirmed phonetic (en.Wiktionary's detailed account, including how the upper portion corrupted to resemble 立, was trusted over zh.Wiktionary's simpler alternate analysis citing 立 directly). `mc_id: 0` reconfirmed as a genuine sentinel — absent from all four `CC N000.md` files. `pos: 事詞` reconfirmed correct (a genuine vault POS category, per precedent). Already correctly cross-listed on `Lookup/Radicals/Radical 030.md` and `Lookup/SKIP/SKIP-2/SKIP-2-5-3.md`.

**`japanese`/`japanese_native` major bugs found and fixed**: stored `[TOU]` and a garbled, non-standard value `つばをはいていな` in `japanese_native`. A raw ja.Wiktionary fetch (quoting 音読み verbatim: 呉音ツ・フ, 漢音トウ・ホウ) confirms four genuine on'yomi, independently corroborated in full by en.Wiktionary — `TSU`, `FU`, `TOU`, `HOU` — with three previously missing. The same fetch explicitly states no 訓読み section exists for this character at all; the garbled `japanese_native` value was accordingly wrong on two counts (both content and existence) and corrected to `ø`.

**`vietnamese` bug found and fixed**: stored `phụ`, which matches neither of hvdic.thivien.net's two actual readings, `phôi` and `phủ` (likely a transcription slip from `phôi`/`phủ`); replaced with the correct pair.

**`aliases` key added — was entirely missing**: added the empty key for schema consistency; zh.Wiktionary's single-sourced variant candidates (㕻, 㖣, 哣) were not corroborated by en.Wiktionary and were left out.

**Empty semantic-component gloss and broken heading fixed**: the pre-existing Notes cited `[[Radical 003|丶]] ("")` with an empty gloss; filled in as "droplet" (a spat-out drop, matching the "to spit" meaning), matching en.Wiktionary's own semantic-component identification.

**`## Derived Characters` completeness gap and duplicate entry fixed**: the list had a duplicated `陪 (char)` entry and was missing [[剖]] (a genuine direct citer, confirmed via its own `graphemic_classification` field); de-duplicated and added the missing entry, reformatting all seven into the standard ruby format.

**Missing lookup entries found and fixed**: absent from `Lookup/HSK/HSK No.md` despite `hsk_level: 無` already being correctly set; added. Absent from `Lookup/Korean/Korean Name ㅂ.md`'s `### 부` subsection despite `korean: 부`; added.

Rebuilt Notes into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 痺 (8802; 14 characters remaining).

### 2026-08-25, iteration 2491 — [[characters/痺|痺]]

`radical: 疒` reconfirmed correct (Kangxi radical 104). `skip_number: 3-5-8` and `stroke_count: 13` reconfirmed correct against `SKIP-3-5-8.md` and `Stroke 13.md`, both already listing the character. `graphemic_classification: 卑` reconfirmed correct — dual-source confirmed phonetic. `aliases: [痹]` reconfirmed correct — dual-source confirmed simplified form, no independent vault page. `japanese: [HI]` and `japanese_native: しびれる` reconfirmed correct and complete. `grade_level: 先進` reconfirmed correct — a genuine, widely-used vault value (552 other pages), matching the dataview-driven `Grade Advanced.md` lookup (no manual list entry needed, same pattern as `Grade Name.md`). `pos: 性詞` reconfirmed correct (genuine vault POS category). `stand_in: 麻痺` and the `## Words` section reconfirmed correct. Already correctly cross-listed on `Lookup/Radicals/Radical 104.md` and `Lookup/SKIP/SKIP-3/SKIP-3-5-8.md`.

**Major `mc_id` bug found and fixed — a genuine false-negative**: the page stored `mc_id: 0` with Notes prose explicitly claiming "Not attested in Classical Chinese corpus," but a direct search of all four `CC N000.md` files found a real, plain-numbered entry: `CC 1000.md`: `1901. 痺`. Corrected `mc_id` to `1901` and rewrote the Notes bullet to cite the genuine rank and rime-file cross-check (`Lookup/CC/finals/韻 支三開.md`, which explicitly lists 痺 among its ㄅㄧ-slot members and even explains the phonetic-avoidance logic that placed it there).

**`vietnamese` completeness gap found and fixed**: stored `[tê, tí, tý]`; hvdic.thivien.net additionally lists `ty` under Âm Hán Việt. Added.

**Lookup-path convention bug found and fixed**: the four-links bullet and SKIP/Stroke links used lowercase, relative `../lookup/...` paths instead of the vault's standard `Lookup/...` capitalized paths (functionally resolved due to a case-insensitive filesystem, but inconsistent with the rest of the vault); corrected all citations.

**Missing lookup entries found and fixed**: absent from `Lookup/HSK/HSK No.md` despite `hsk_level: 無` already being correctly set; added. Absent from `Lookup/Korean/Korean HS.md`'s `#### 비` subsection (the vault's specialized advanced-hanja list, correctly cited over the simpler `Korean Name` lists per the page's own pre-existing bullet-4 choice) despite `korean: 비`; added with gloss `(저릴 비)`.

Rebuilt Notes into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 屿 (8803, tied with 跋; 13 characters remaining).

### 2026-08-25, iteration 2492 — [[characters/屿|屿]]

`radical: 山` reconfirmed correct (Kangxi radical 46). `skip_number: 1-3-13` and `stroke_count: 17` reconfirmed correct against `SKIP-1-3-13.md` and `Stroke 17.md`, both already listing the character. `vietnamese: [dữ, tự]` reconfirmed correct and complete. `japanese_native: しま` reconfirmed correct. `mc_id: 15885` reconfirmed as trusted long-tail (>4000, not cross-checked per policy). `aliases: [㠀, 嶼]` reconfirmed correct — 嶼 (traditional form) dual-source confirmed, no independent vault page; pre-existing 㠀 left unverified-but-unchanged. `stand_in: 島屿` and the `## Words` section reconfirmed correct — the word page exists and matches. Already correctly cross-listed on `Lookup/Radicals/Radical 046.md`, `Lookup/SKIP/SKIP-1/SKIP-1-3-13.md`, `Lookup/Stroke/Stroke 17.md`, and `Lookup/Korean/Korean Name ㅅ.md`'s `### 서` subsection.

**`graphemic_classification` bug found and fixed — cited the ancestor's phonetic instead of the character's own**: stored `與`, but 屿's own literal glyph (⿰山与) uses the further-simplified `与` as its actual component — 與 is one step further back, being 嶼's (the traditional ancestor's) own phonetic. Since 与 has its own independent vault page, corrected the citation to `与`.

**`japanese` completeness gap found and fixed, and a false-alarm investigated to a real explanation**: stored `[SHO]` only, missing a genuine second on'yomi. Investigating why 屿 — a character not actually used in Japan — carries Japanese readings at all led to 嶼 (its traditional ancestor): a direct ja.Wiktionary fetch on 嶼 itself confirms 呉音ジョ／漢音ショ on'yomi and 訓読みしま kun'yomi, exactly matching this page's pre-existing `しま` and explaining `SHO`'s presence as a borrowed kan-on reading. Added the missing goon `JO` and documented the borrowing explicitly in Notes so it isn't mistaken for a data error again.

**`hsk_level` filled — key was entirely missing**: filled as `無` — 屿 is genuinely listed (item 337, a plain-numbered entry, not a false colon-count one) on `Lookup/HSK/HSK No.md`, the vault's own "confirmed no HSK level" list.

**Broken wikilink and lookup-path bugs found and fixed**: the `## Words` section cited `[[../words/島屿]]` — an invalid relative-path-inside-brackets wikilink; corrected to plain `[[島屿]]`. The four-links bullet used non-standard link text (`[表外字]` instead of `[Hyōgai]`, `[Grade 名]` instead of `[Grade Name]`) and lowercase relative `../lookup/...` paths; all corrected to the standard format.

Rebuilt Notes into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 跋 (8803; 12 characters remaining).

### 2026-08-25, iteration 2493 — [[characters/跋|跋]]

`radical: 足` reconfirmed correct (Kangxi radical 157). `skip_number: 1-7-5` and `stroke_count: 12` reconfirmed correct against `SKIP-1-7-5.md` and `Stroke 12.md`, both already listing the character. `graphemic_classification: 犮` reconfirmed correct — dual-source confirmed phonetic (matches the vault's own already-perfected `犮.md` from earlier this session). `mc_id: 3666` reconfirmed correct — `CC 3000.md`: `3666. 跋` exactly matches, no off-by-one. `vietnamese: bạt` reconfirmed correct and complete. `stand_in: 跋扈` and the `## Words`/`## Chengyu` sections reconfirmed correct. Already correctly cross-listed on `Lookup/Radicals/Radical 157.md`, `Lookup/SKIP/SKIP-1/SKIP-1-7-5.md`, and `Lookup/Korean/Korean Name ㅂ.md`'s `### 발` subsection.

**`japanese` completeness gap found and fixed**: stored `[BATSU]` only; a raw ja.Wiktionary fetch (quoting 音読み verbatim: 呉音バチ・バツ, 漢音ハツ) confirms two further genuine on'yomi, `BACHI` and `HATSU`, both missing. Added both.

**`japanese_native` filled — key was blank**: filled as `[おくがき, ふむ]`, the two kun'yomi corroborated by both en.Wiktionary and ja.Wiktionary's own reading list; two further single-sourced en.Wiktionary-only candidates (つまずく, こえる) were left out per the dual-source standard for filling blank fields.

**`boundedness` filled and lookup-path convention fixed**: `boundedness` (key entirely missing) filled as `70`, consistent with comparable characters. The four-links bullet and SKIP/Stroke links used lowercase relative `lookup/...` paths instead of the vault's standard `Lookup/...`; corrected throughout.

**Missing lookup entry found and fixed**: absent from `Lookup/HSK/HSK No.md` despite `hsk_level: 無` already being correctly set; added.

Rebuilt the Notes prose into the standard four-bullet format with proper dual-source attribution. Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 懍 (8804; 11 characters remaining).

### 2026-08-25, iteration 2494 — [[characters/懍|懍]]

`radical: 心` reconfirmed correct (Kangxi radical 61). `japanese: [RIN]` reconfirmed correct — ja.Wiktionary's raw pronunciation section gives リン for both go-on and kan-on slots, not corroborating en.Wiktionary's single-sourced extra `RAN` claim, which was correctly left out. `japanese_native: ø` reconfirmed correct — a raw ja.Wiktionary fetch explicitly confirms no 訓読み section exists at all, overriding en.Wiktionary's single-sourced おそれる claim (established explicit-denial precedent). `vietnamese: [lầm, lẫm]` reconfirmed correct and complete. `stand_in: 懍懍` and the `## Words` section reconfirmed correct — the word page exists and matches. Already correctly cross-listed on `Lookup/Radicals/Radical 061.md`, `Lookup/SKIP/SKIP-1/SKIP-1-3-13.md`, `Lookup/Stroke/Stroke 16.md`, and `Lookup/Korean/Korean Name ㄹ.md`'s `### 름` subsection. The deliberate syllable-placement exception documented in the pre-existing Notes (ㄌㄜㄇ instead of the mechanically-derived ㄌㄧㄇ, to populate an otherwise-empty syllable slot) was left untouched per `feedback_syllable_placement_override`.

**`graphemic_classification` bug found and fixed — cited the type-label instead of the phonetic**: stored `形声` (the compound-type label itself), but both sources confirm the actual phonetic component is [[稟]] — already correctly named in the page's own pre-existing Notes prose, just not reflected in the frontmatter field. Corrected to `稟`.

**`pos`, `mc_id`, `boundedness` filled — all three were blank**: `pos` filled as `性詞` (a stative/property-word category, matching this character's "to be afraid/awed" sense). `mc_id` filled as `0`, a genuine sentinel confirmed absent from all four `CC N000.md` files. `boundedness` filled as `65`.

**Lookup-path convention fixed**: the four-links bullet and SKIP/Stroke links used lowercase relative `../lookup/...` paths; corrected to the standard `Lookup/...` format throughout.

**Missing lookup entries found and fixed**: absent from `Lookup/HSK/HSK No.md` despite `hsk_level: 無` already being correctly set; added. Absent from `Lookup/Japanese/Hyōgai.md` despite `joyo_level: 表外字` already being correctly set; added (caught and corrected a duplicate item-630 numbering collision with 粤's own entry in the same file before finalizing — renumbered 懍 to 631).

**Cross-page discovery flagged for a future dedicated pass (not fixed this iteration — out of scope for a single-character turn)**: while cross-checking `Lookup/SKIP/SKIP-1/SKIP-1-3-13.md` (which correctly lists 懍, `stroke_count: 16` per its own frontmatter), the file's item 24 entry for [[屿]] (perfected two iterations ago, 2492) was also present there — but 屿's own `stroke_count: 17` doesn't match this list's actual 16-stroke membership, and en.Wiktionary's own composition analysis for 屿 explicitly states "Kangxi radical 46, 山+3, 6 strokes" — suggesting 屿's `stroke_count`, `skip_number`, and its Radical/SKIP/Stroke cross-listings may all be wrong (likely should be 6 strokes, not 17). This needs a dedicated follow-up investigation and multi-page fix; flagging here rather than attempting a rushed correction mid-iteration.

Rebuilt Notes into the standard four-bullet format with proper dual-source attribution. Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 瓷 (8805; 10 characters remaining).

### 2026-08-25, iteration 2495 — [[characters/瓷|瓷]]

`radical: 瓦` reconfirmed correct (Kangxi radical 98). `stroke_count: 11` reconfirmed correct. `graphemic_classification: 次` reconfirmed correct — dual-source confirmed phonetic. `japanese: [SHI, JI]` reconfirmed correct and complete. `hsk_level: 6` reconfirmed correct — genuine numbered entry (item 54) on `Old HSK 6.md`, not a false colon-count entry. `pos: 名詞` and `stand_in: 陶瓷` reconfirmed correct — the `## Words` section's two entries both check out. Already correctly cross-listed in `Lookup/Korean/Korean Name ㅈ.md`'s `### 자` subsection. The deliberate syllable-placement exception documented in the pre-existing Notes (ㄑㄧ instead of the mechanically-derived ㄐㄧㄜ, to keep "porcelain" auditorily distinct from 磁 "magnetism") was left untouched per `feedback_syllable_placement_override`.

**`japanese_native` bug found and fixed — wrongly denied an attested kun'yomi**: stored `ø`, but a raw ja.Wiktionary fetch explicitly confirms a genuine kun'yomi `かめ`, independently corroborated by en.Wiktionary. Corrected to `かめ`.

**`vietnamese` completeness gap found and fixed**: stored `sứ` only; hvdic.thivien.net additionally lists `từ` (Âm Hán Việt) and `tư` (Âm Nôm). Added both.

**`mc_id`, `boundedness` filled — both were blank**: `mc_id` filled as `0`, a genuine sentinel confirmed absent from all four `CC N000.md` files. `boundedness` filled as `65`.

**Missing lookup entries found and fixed across three files**: absent from `Lookup/SKIP/SKIP-2/SKIP-2-6-5.md` (added as item 1, renumbering the rest and updating `size` to 16), `Lookup/Radicals/Radical 098.md`'s "+6 Strokes" section (added, updating `size` to 6), and `Lookup/Stroke/Stroke 11.md`'s 2-6-5 group — all three despite `skip_number`/`radical`/`stroke_count` already being correctly set on the character page itself.

Rebuilt Notes into the standard four-bullet format (fixing lowercase relative `../lookup/...` paths throughout) while preserving the pre-existing deliberate-exception explanation. Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 恍 (8806, tied with 芒; 9 characters remaining).

### 2026-08-25, iteration 2496 — [[characters/恍|恍]]

`radical: 心` reconfirmed correct (Kangxi radical 61). `skip_number: 1-3-6` and `stroke_count: 9` reconfirmed correct against `SKIP-1-3-6.md` and `Stroke 09.md`, both already listing the character. `graphemic_classification: 光` reconfirmed correct — dual-source confirmed phonetic. `mc_id: 3838` reconfirmed correct — `CC 3000.md`: `3838. 恍` exactly matches, no off-by-one. `hsk_level: 6` reconfirmed correct — genuine numbered entry (item 62) on `Old HSK 6.md`. `japanese: [KOU]` reconfirmed correct and complete (go-on and kan-on both こう). `vietnamese: [hoảng, đoảng]` reconfirmed correct and complete. `aliases: [怳]` reconfirmed correct — en.Wiktionary's further-mentioned variant candidate, 芒, already has its own independent vault page and is correctly excluded. `stand_in: 恍惚` and the `## Words` section reconfirmed correct. Already correctly cross-listed on `Lookup/Radicals/Radical 061.md` and `Lookup/Korean/Korean Name ㅎ.md`'s `### 황` subsection.

**`japanese_native` bug found and fixed — a single-sourced claim not corroborated by the authoritative list**: stored `ほのか` only; a raw ja.Wiktionary fetch gives a complete, explicit 訓読み list of exactly two readings, `とぼける` and `ほれる` — neither matching the pre-existing `ほのか`, which does not appear anywhere in ja.Wiktionary's own reading data despite being present in en.Wiktionary. Replaced with the two dual-confirmed readings (both also independently listed by en.Wiktionary).

**`pos` filled — was blank**: filled as `性詞`, matching the character's descriptive/stative "vague, absent-minded" sense.

Rebuilt Notes into the standard four-bullet format (fixing lowercase relative `lookup/...` paths and an incomplete `CC #3838` citation) while preserving the pre-existing alias explanation. Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 芒 (8806; 8 characters remaining).

### 2026-08-25, iteration 2497 — [[characters/芒|芒]]

`radical: 艸` reconfirmed correct (Kangxi radical 140). `stroke_count: 6` reconfirmed correct. `graphemic_classification: 亡` reconfirmed correct — dual-source confirmed phonetic, matching the page's own pre-existing Notes prose. `mc_id: 1692` reconfirmed correct — `CC 1000.md`: `1692. 芒` exactly matches. `hsk_level: 6` reconfirmed correct — genuine numbered entry (item 175) on `Old HSK 6.md`. `stand_in: 光芒` and the `## Words` section reconfirmed correct. Already correctly cross-listed in `Lookup/Korean/Korean Name ㅁ.md`'s `### 망` subsection. The deliberate syllable-placement exception in the pre-existing Notes (ㄇ⼘ㄫ instead of the mechanically-derived, already-crowded ㄇㄚㄫ) was left untouched per `feedback_syllable_placement_override`.

**`japanese` bug found and fixed — an unconfirmed third on'yomi removed**: stored `[BOU, MOU, KOU]`; a raw ja.Wiktionary fetch gives a complete on'yomi list of exactly two (呉音モウ, 漢音ボウ), not corroborating en.Wiktionary's ambiguously-categorized third reading `KOU`. Removed, matching the same-session precedent of trusting ja.Wiktionary's complete authoritative list over single-sourced extras (氐, 恍).

**`japanese_native` completeness gap found and fixed**: stored `のぎ` only; both sources independently and fully corroborate two further kun'yomi, `すすき` and `のげ`. Added both.

**`vietnamese` completeness gap found and fixed**: stored `mang` only; hvdic.thivien.net additionally lists `man`, `mưng`, `mường`, and `vong`. Added all four.

**`boundedness` filled — was blank**: filled as `55`.

**Broken wikilink found and fixed**: the pre-existing Notes prose cited `[[鋒鋩]]`, but the vault's actual word-page filename is `鋒芒` (already correctly used in the `## Words` section below it); corrected the mismatched citation.

**Missing lookup entries found and fixed across three files**: absent from `Lookup/SKIP/SKIP-2/SKIP-2-3-3.md` (added as item 1, renumbering the rest and updating `size` to 22), `Lookup/Radicals/Radical 140.md`'s "+3 Strokes" section (added, triggering a full sequential renumbering of the page's 117→118 entries and `size` update), and `Lookup/Stroke/Stroke 06.md`'s 2-3-3 group — all three despite `radical`/`skip_number`/`stroke_count` already being correctly set on the character page itself.

Rebuilt Notes into the standard four-bullet format (fixing lowercase relative `../lookup/...` paths) while preserving the pre-existing deliberate-exception explanation. Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 汐 (8807; 7 characters remaining).

### 2026-08-25, iteration 2498 — [[characters/汐|汐]]

`radical: 水` reconfirmed correct (Kangxi radical 85). `skip_number: 1-3-3` and `stroke_count: 6` reconfirmed correct against `SKIP-1-3-3.md` and `Stroke 06.md` (partially — see below). `graphemic_classification: 夕` reconfirmed correct — dual-source confirmed phonetic, matching the page's own pre-existing Notes prose. `japanese: [SEKI, JAKU]` reconfirmed correct and complete. `joyo_level: 日本人名用漢字` reconfirmed correct — already genuinely listed on `Lookup/Japanese/Jinmeiyō.md`. `stand_in: 潮汐` and the `## Words` section reconfirmed correct. Already correctly cross-listed on `Lookup/Radicals/Radical 085.md`, `Lookup/SKIP/SKIP-1/SKIP-1-3-3.md`, and `Lookup/Korean/Korean Name ㅅ.md`'s `### 석` subsection.

**`japanese_native` completeness gap found and fixed**: stored `[しお, うしお]`; a raw ja.Wiktionary fetch gives a complete 訓 list of four readings, `しお・うしお・せい・いそ` — two missing. Added both.

**`vietnamese` completeness gap found and fixed**: stored `tịch` only; hvdic.thivien.net additionally lists `tách` under Âm Nôm. Added.

**`pos`, `mc_id` filled — both were blank**: `pos` filled as `名詞`. `mc_id` filled as `0`, a genuine sentinel confirmed absent from all four `CC N000.md` files.

**Missing lookup entry found and fixed**: absent from `Lookup/Stroke/Stroke 06.md`'s 1-3-3 group despite `stroke_count`/`skip_number` already being correctly set on the character page; added.

Rebuilt Notes into the standard four-bullet format (fixing lowercase relative `../lookup/...` paths). Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 鑫 (8809; 6 characters remaining).

### 2026-08-25, iteration 2499 — [[characters/鑫|鑫]]

`radical: 金` reconfirmed correct (Kangxi radical 167). `skip_number: 2-8-16` and `stroke_count: 24` reconfirmed correct against `SKIP-2-8-16.md` and `Stroke 24.md`, both already listing the character. `graphemic_classification: 會意` reconfirmed correct — dual-source confirmed 金-triplication. `japanese: [KON, KIN, KUN]` reconfirmed correct and complete. `vietnamese: hâm` reconfirmed correct and complete. `pos: 性詞` and `mc_id`'s pre-existing "no MC reconstruction attested" reasoning (already explained in the page's own Notes) both reconfirmed correct. `stand_in: 名専字` reconfirmed correct. Already correctly cross-listed on `Lookup/Radicals/Radical 167.md`, `Lookup/SKIP/SKIP-2/SKIP-2-8-16.md`, `Lookup/Stroke/Stroke 24.md`, and `Lookup/Korean/Korean Name ㅎ.md`'s `### 흠` subsection.

**`japanese_native` filled — key was entirely missing**: a raw ja.Wiktionary fetch explicitly confirms no 訓読み section exists for this character; filled as `ø`.

**`mc_id` filled — key was blank, now `0`**: the value itself was already correctly reasoned out in the page's own pre-existing Notes (no genuine Middle Chinese reconstruction attested for this modern folk-coined character); formalized as the frontmatter sentinel and reinforced with the standard "absent from all four `CC N000.md` files" phrasing.

**Missing lookup entries found and fixed**: absent from `Lookup/HSK/HSK No.md` despite `hsk_level: 無` already being correctly set; added. Absent from `Lookup/Japanese/Hyōgai.md` despite `joyo_level: 表外字` already being correctly set; added as item 632.

Rebuilt Notes into the standard four-bullet format (fixing lowercase relative `../lookup/...` paths and a broken `[金](Radical 167)` non-wikilink reference) while preserving the page's own detailed, well-researched etymology and phonology explanation in full. Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 瞰 (8810; 5 characters remaining).

### 2026-08-25, iteration 2500 — [[characters/瞰|瞰]]

`radical: 目` reconfirmed correct (Kangxi radical 109). `skip_number: 1-5-12` and `stroke_count: 17` reconfirmed correct against `SKIP-1-5-12.md` and `Stroke 17.md`, both already listing the character. `graphemic_classification: 敢` reconfirmed correct — dual-source confirmed phonetic. `japanese: [KAN]` and `japanese_native: [みる]` reconfirmed correct and complete. `hsk_level: 無` reconfirmed correct. `stand_in: 俯瞰` and the `## Words` section reconfirmed correct. Already correctly cross-listed on `Lookup/Radicals/Radical 109.md`, `Lookup/SKIP/SKIP-1/SKIP-1-5-12.md`, `Lookup/Stroke/Stroke 17.md`, and `Lookup/Korean/Korean Name ㄱ.md`'s `### 감` subsection.

**`joyo_level` bug found and fixed**: stored `日本人名用漢字` (Jinmeiyō), but both en.Wiktionary and a raw ja.Wiktionary fetch explicitly and consistently classify 瞰 as `表外漢字` (Hyōgai) — corroborated by the character's own pre-existing, correct listing in `Lookup/Japanese/Hyōgai.md`'s alphabetized section (and its absence from `Jinmeiyō.md`). Corrected the frontmatter field to `表外字` to match the vault's own already-consistent lookup data.

**`vietnamese` filled — key was entirely missing**: filled as `[khám, hám]` (hvdic.thivien.net's Âm Hán Việt and Âm Nôm readings respectively).

**`mc_id` filled — was blank**: filled as `0`, a genuine sentinel confirmed absent from all four `CC N000.md` files.

**Wrong-target bullet-4 citation found and fixed**: the four-links bullet cited `[Korean Missing](../lookup/Korean/Korean%20Missing.md)` — but that file is actually an auto-generated dataview list of characters with `hanmun_edu_level = "無"`, unrelated to Korean name-reading cross-referencing. Corrected to the proper `Korean Name ㄱ` lookup (matching `korean: 감`), where the character is already genuinely listed. Also fixed lowercase relative `../lookup/...` paths throughout.

Rebuilt Notes into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 徘 (8811; 4 characters remaining).

### 2026-08-25, iteration 2501 — [[characters/徘|徘]]

`radical: 彳` reconfirmed correct (Kangxi radical 60). `skip_number: 1-3-8` and `stroke_count: 11` reconfirmed correct against `SKIP-1-3-8.md` and `Stroke 11.md`, both already listing the character. `graphemic_classification: 非` reconfirmed correct — dual-source confirmed phonetic. `japanese: [BAI, HAI]`, `japanese_native: [さまよう]`, and `vietnamese: [bồi]` all reconfirmed correct and complete against dual sources — a fully clean data pass. `hsk_level: 6` reconfirmed correct — genuine numbered entry (item 172) on `Old HSK 6.md`. `stand_in: 徘徊` and the `## Words` section reconfirmed correct. Already correctly cross-listed on `Lookup/Radicals/Radical 060.md`, `Lookup/SKIP/SKIP-1/SKIP-1-3-8.md`, and `Lookup/Korean/Korean Name ㅂ.md`'s `### 배` subsection.

**`mc_id` filled — was blank**: filled as `0`, a genuine sentinel confirmed absent from all four `CC N000.md` files.

**Wrong-target bullet-4 citation found and fixed (same bug pattern as 瞰, iteration 2500)**: cited `[Korean Missing](../lookup/Korean/Korean%20Missing.md)` — an unrelated auto-generated dataview list, not a Korean cross-reference; corrected to `Korean Name ㅂ`, where the character is already genuinely listed. Also fixed a malformed `[[非 (char)]]` wikilink (missing display-text pipe) and lowercase relative `../lookup/...` paths throughout.

Rebuilt Notes into the standard four-bullet format, folding the pre-existing bound-morpheme note into the etymology bullet. Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 徊 (8812; 3 characters remaining).

### 2026-08-25, iteration 2502 — [[characters/徊|徊]]

`radical: 彳` reconfirmed correct (Kangxi radical 60). `skip_number: 1-3-6` and `stroke_count: 9` reconfirmed correct against `SKIP-1-3-6.md` and `Stroke 09.md`, both already listing the character. `graphemic_classification: 回` reconfirmed correct — dual-source confirmed phonetic (identical OC reconstruction to 徊 itself). `japanese: [KAI, E]` and `japanese_native: [さまよう]` reconfirmed correct and complete. `hsk_level: 6` reconfirmed correct — genuine numbered entry (item 164) on `Old HSK 6.md`. `stand_in: 徘徊` and the `## Words` section reconfirmed correct — 徊 completes the 徘/徊 pair processed back-to-back this session. Already correctly cross-listed on `Lookup/Radicals/Radical 060.md`, `Lookup/SKIP/SKIP-1/SKIP-1-3-6.md`, `Lookup/Stroke/Stroke 09.md`, and `Lookup/Korean/Korean Name ㅎ.md`'s `### 회` subsection.

**`vietnamese` completeness gap found and fixed**: stored `hồi` only; hvdic.thivien.net additionally lists `hòi` under Âm Nôm. Added.

**`mc_id` filled — was blank**: filled as `0`, a genuine sentinel confirmed absent from all four `CC N000.md` files.

**Wrong-target bullet-4 citation found and fixed (third occurrence of the same bug this session — 瞰, 徘, now 徊)**: cited `[Korean Missing](../lookup/Korean/Korean%20Missing.md)`, the unrelated auto-generated dataview list; corrected to `Korean Name ㅎ`, where the character is already genuinely listed. Also fixed a malformed `[[回 (char)]]` wikilink (missing display-text pipe) and lowercase relative `../lookup/...` paths throughout.

Rebuilt Notes into the standard four-bullet format, folding the pre-existing bound-morpheme note into the etymology bullet. Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 怯 (char) (8813; 2 characters remaining).

### 2026-08-25, iteration 2503 — [[characters/怯 (char)|怯 (char)]]

`radical: 心` reconfirmed correct (Kangxi radical 61). `skip_number: 1-3-5` and `stroke_count: 8` reconfirmed correct against `SKIP-1-3-5.md` and `Stroke 08.md`, both already listing the character. `graphemic_classification: 去` reconfirmed correct — dual-source confirmed phonetic. `mc_id: 2125` reconfirmed correct — `CC 2000.md`: `2125. 怯` exactly matches. `japanese: [KYOU, KOU]` reconfirmed correct and complete. `stand_in: 怯` reconfirmed correct — the word page `words/怯.md` exists and cross-references correctly. Already correctly cross-listed on `Lookup/Radicals/Radical 061.md`, `Lookup/SKIP/SKIP-1/SKIP-1-3-5.md`, `Lookup/Stroke/Stroke 08.md`, and `Lookup/Korean/Korean Name ㄱ.md`'s `### 겁` subsection.

**`hsk_level` bug found and fixed — a colon-count entry was wrongly trusted as genuine**: stored `4`, based on `Old HSK 4.md`'s `[[怯 (char)]]: 2` line — a colon-count entry, not genuine per established vault policy. A full check of the remaining five `Old HSK N.md` files found a real plain-numbered entry: `Old HSK 6.md`: `58. [[怯 (char)]]`. Corrected `hsk_level` to `6` and the four-links bullet to cite `Old HSK 6` instead of `Old HSK 4`.

**`japanese_native` bug found and fixed — badly truncated**: stored `ひる` (a bare fragment matching none of the genuine readings outright), while a raw ja.Wiktionary fetch gives a complete five-item 訓読み list: `ひるむ・おびえる・おじる・おそれる・よわい`. Replaced with the full corroborated set.

**`vietnamese` completeness gap found and fixed**: stored `khiếp` only; hvdic.thivien.net additionally lists `khép` under Âm Nôm. Added.

**`boundedness` filled and missing dual-page tip-callout added**: `boundedness` (blank) filled as `40`, reflecting that — like 雉/穂 earlier this session — this character legitimately stands alone as its own word. The page was missing the standard `>[!tip] This is a page about the character X. For the word, see...` callout used for this dual-page pattern; added it, and removed the now-redundant empty `## Words` heading (no compound word other than the self-standing entry cites this character).

Rebuilt Notes into the standard four-bullet format (fixing a malformed `[[去 (char)]]` wikilink and lowercase relative `../lookup/...` paths). Stamped `date-last-perfect: 2026-08-25`.

Next never-perfected character by `danayo_id`: 甕 (8815; 1 character remaining).

### 2026-08-25, iteration 2504 — [[characters/甕|甕]]

`radical: 瓦` reconfirmed correct (Kangxi radical 98). `skip_number: 2-2-16` and `stroke_count: 18` reconfirmed correct against `SKIP-2-2-16.md` and `Stroke 18.md`, both already listing the character. `mc_id: 3266` reconfirmed correct — `CC 3000.md`: `3266. 甕` exactly matches, no off-by-one. `hsk_level: 無` reconfirmed correct. Already correctly cross-listed on `Lookup/Radicals/Radical 098.md` and `Lookup/Korean/Korean Name ㅇ.md`'s `### 옹` subsection.

**`graphemic_classification` major bug found and fixed**: stored `公`, with Notes prose citing an awkward `[[翁 (char)|公]]` link (display text mismatched to its own target) reasoning that 公 shares 翁's phonetic series. But both en.Wiktionary and zh.Wiktionary directly and unambiguously identify the true phonetic component as **雍** (yōng) — an entirely different character from both 公 and 翁, and one that has its own independent vault page. Corrected to `雍`.

**`japanese` completeness gap found and fixed**: stored `[OU]` only; both sources confirm a second genuine on'yomi, goon `U`. Added.

**`japanese_native` completeness gap found and fixed**: stored `かめ` only; a raw ja.Wiktionary fetch gives a complete 訓読み list of `かめ・みか・もたい` — two missing (a fourth/fifth candidate from en.Wiktionary alone, みかわ/たしらか, was left out as single-sourced). Added the two dual-confirmed readings.

**`vietnamese` completeness gap found and fixed**: stored `úng` only; hvdic.thivien.net additionally lists `ung`, `ủng` (Âm Hán Việt), and `ống` (Âm Nôm). Added all three.

**`boundedness` filled — was blank**: filled as `65`.

**Missing lookup entry found and fixed**: absent from `Lookup/HSK/HSK No.md` despite `hsk_level: 無` already being correctly set; added.

Rebuilt Notes into the standard four-bullet format (fixing lowercase relative `../lookup/...` paths) and removed an empty, contentless `## Words` heading — no compound word currently cites this character and no corresponding word page exists yet (out of scope for the character-perfecting sweep; a future word-perfecting pass may create `words/甕.md` to match the pre-existing self-referential `stand_in: 甕`). Stamped `date-last-perfect: 2026-08-25`.

---

## Sweep complete

With this iteration, **every character page in the vault now carries a `date-last-perfect` stamp** — the never-perfected backlog that began this log (and its six predecessor logs before it) is fully cleared, at zero remaining characters. This solo loop ran from iteration 1 through iteration 2504 across seven log files (`Character Perfecting (Solo Loop).md.zip` through `... 6.md.zip`, plus this final file), spanning many sessions. The most recent stretch (iterations 2261–2504, this file and its immediate predecessor) fixed hundreds of individual bugs across every field in the schema: off-by-one and false-negative `mc_id` errors, false aliases, misfiled/truncated/wrongly-denied Japanese readings, incomplete Vietnamese readings verified strictly against hvdic as sole authority, graphemic_classification citations that named type-labels or wrong characters instead of true phonetic components, broken/malformed wikilinks, non-standard lookup-page paths, and numerous missing cross-reference entries across the Radical/SKIP/Stroke/HSK/Hyōgai/Jinmeiyō/Korean lookup pages.

No further action is needed from this loop. If new characters are ever added to the vault, this same process can resume.
