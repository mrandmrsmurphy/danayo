# Character Perfecting (Solo Loop)

Running log for the character-perfecting backlog sweep (see [[AIOS/checklists/checklist_characters.md|Checklist: Character Pages]]). The prior logs (iterations 1–464, 465–981, and 982–1543) grew large and were archived to `Character Perfecting (Solo Loop).md.zip`, `Character Perfecting (Solo Loop) 2.md.zip`, and `Character Perfecting (Solo Loop) 3.md.zip` respectively; this file continues from there. Iteration numbering continues unbroken from the archived logs.

**Process**: one character per iteration. Find the next never-perfected character via `danayo_id` ascending (`grep -L "^date-last-perfect" characters/*.md`, sorted by each file's own `danayo_id` frontmatter value — not alphabetical, unlike the word sweep). Verify/fill all required frontmatter (`graphemic_classification`, `stand_in`, `mc_id`, `danayo_id`, `pos`, level fields), write or correct the four fixed `## Notes` bullets (graphemic → SKIP/Stroke → MC rank+phonology → levels), cross-check `## Words` against every real word citing this character as a constituent, add `## Chengyu`/`## Derived Characters` when real hits exist, then stamp `date-last-perfect`.

Next never-perfected character by `danayo_id`: 稍 (char) (7276; 961 characters remaining).

### 2026-08-14, iteration 1544 — [[characters/稍 (char)|稍]]

`mc_id: 1228` confirmed correct (matches `CC 1000.md` line 241, no off-by-one). **`graphemic_classification: 肖` confirmed correct** (形聲, semantic 禾 + phonetic 肖), via en.Wiktionary. `korean_native: 점점`, `pos: 副詞` (an established convention value in this vault, used on several other character pages though not a leaf name in the formal grammar taxonomy), and `middle_chinese_initial/final: ʃ`/`ɣau` all reconfirmed correct against `聲 生`/`韻 肴` (both lookup pages, plus `SKIP-1-5-7`/`Stroke 12`/`Hyōgai`/`Old HSK 2`/`Korean Name ㅊ`/`Radical 115`, already cited 稍 correctly).

**`vietnamese` contamination fixed**: hvdic explicitly labels the stored `rảo` and `xao` as Nôm-only, not Hán Việt — removed both; added the missing genuine Hán Việt `sao` alongside the already-correct `sảo`. **`japanese_native` bug fixed**: added missing `ようやく` ("finally, at last"), confirmed via ja.Wiktionary and Jisho alongside the already-stored `やや`. `japanese: SOU/SHOU` confirmed correct (both sources agree, kan-on/go-on).

Rebuilt malformed `## Notes` (informal "Components:" line, no `## Words` section) to the standard format. No Derived Characters; no Chengyu hits (one grep hit, [[弱不禁風]], confirmed a false positive — 稍 not in its `characters:` field). Only the existing self stand-in cites 稍.

**Citing word page [[稍]] (self stand-in) had corrupted data fixed**: `vietnamese: null` (literal placeholder) → `sảo`; blank `pos` → `副詞`.

Stamped `date-last-perfect: 2026-08-14`.

(Session note: mid-cycle, filesystem access to the vault was briefly and completely lost — even re-reading a file already read moments earlier failed with "Operation not permitted" — then spontaneously restored a few tool calls later. No data was lost; this is logged here only as an environment anomaly, not a vault bug.)

Next never-perfected character by `danayo_id`: 喊 (7277; 960 characters remaining).

### 2026-08-14, iteration 1545 — [[characters/喊|喊]]

`mc_id: 9201` confirmed as legitimate long-tail data (喊 not found anywhere in `CC 0000`–`CC 3000`). **`graphemic_classification: 咸` confirmed correct** (形聲, semantic 口 + phonetic 咸), via en.Wiktionary. **New variant alias added**: 㘕 — cross-referenced between en.Wiktionary's and zh.Wiktionary's independent (and largely non-overlapping) variant lists, keeping only the one candidate appearing in both, same cross-referencing method used on [[璽]] a few iterations ago. `vietnamese: hảm` confirmed correct (one of three documented MC readings for this character, matching the stored `middle_chinese_initial/final: x`/`ɑm` against `聲 曉`/`韻 談` — both lookup pages, plus `SKIP-1-3-9`/`Stroke 12`/`Hyōgai`/`Old HSK 3`/`Korean Name ㅎ`/`Radical 030`, already cited 喊 correctly).

**`japanese_native` bug fixed**: corrected bare `さけ` to properly hyphenated `さけ-ぶ`, confirmed via ja.Wiktionary and Jisho; a jisho-only second on'yomi candidate ヤク wasn't corroborated by ja.Wiktionary and was left out. `japanese: KAN` confirmed correct (both sources agree, go-on/kan-on identical). **`joyo_level` bug fixed**: blank → `表外字` (real on'yomi/kun'yomi usage with no jōyō/jinmeiyō classification). **Missing-entry bug fixed accordingly**: added 喊 to `lookup/Japanese/Hyōgai.md`. Blank `pos` filled: `事詞`.

Rebuilt malformed `## Notes` (two bare unlinked CC-lookup wikilinks with no other bullets, missing stand-in annotation in `## Words`) to the standard format. No Derived Characters; no Chengyu hits; only the existing stand-in [[喊声]] cites 喊.

**Citing word page [[喊声]] (already perfected) had one bug fixed**: a redundant duplicate `品詞` field (identical value to `pos`), the same recurring pattern seen repeatedly this session.

(Session note: several `grep -rl` sweeps across the `words/` directory timed out mid-cycle and had to be retried as background tasks or replaced with narrower direct checks — likely transient filesystem slowness following the earlier access outage, not a vault issue. All checks completed successfully once retried.)

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 屁 (char) (7278; 959 characters remaining).

### 2026-08-14, iteration 1546 — [[characters/屁 (char)|屁]]

`mc_id: 0` confirmed as a legitimate sentinel (屁 not found anywhere in `CC 0000`–`CC 3000`, plausible for a colloquial term absent from classical rime dictionaries). **`graphemic_classification: 比` confirmed correct** (形聲, semantic 尸 + phonetic 比), via en.Wiktionary. **New variant alias added**: 䊧, cross-referenced between en.Wiktionary's and zh.Wiktionary's independent variant lists (the only one appearing in both, out of five en.Wiktionary candidates). `korean_native: 방귀`, `vietnamese: thí`, and `middle_chinese_initial/final: pʰ`/`iɪ` all reconfirmed correct against `聲 滂`/`韻 脂A三開` (both lookup pages, plus `SKIP-3-3-4`/`Stroke 07`/`Hyōgai`/`Old HSK 3`, already cited 屁 correctly).

**Major, wide-reaching `english` bug fixed**: the stored gloss `far` was a bald typo/euphemism for the character's actual meaning ("fart, flatulence" — matching `korean_native: 방귀` exactly) — the pre-existing Notes fragment "too rude" suggests a prior editor deliberately avoided writing the real word rather than fixing the data. Propagated to **three further locations**, all corrected: `lookup/SKIP/SKIP-3/SKIP-3-3-4.md`, `lookup/Radicals/Radical 044.md`, and `syllables/ㄆㄧㄜ.md` (both frontmatter and prose). **`japanese_native` bug fixed**: stored `おなら` is a different native Japanese word for "fart" (written in kana, not tied to this kanji's own reading) — both ja.Wiktionary and Jisho confirm the actual kun-yomi of 屁 is `へ`; corrected. `japanese: HI` confirmed correct (both sources agree, go-on/kan-on identical).

**Missing-entry bug fixed**: added 屁 to the `### 비` subsection of `lookup/Korean/Korean Name ㅂ.md`, absent despite `korean: 비` and being otherwise fully cited everywhere else. Blank `pos` filled: `名詞`.

Rebuilt malformed `# Notes` (wrong heading level, stray "too rude" fragment, two bare unlinked CC-lookup wikilinks, no `## Words` section) to the standard format. No Derived Characters; no Chengyu hits; only the existing self stand-in cites 屁.

**Citing word page [[屁]] (self stand-in) had multiple bugs fixed**: `english: far` corrected to `fart, flatulence` (same cascade as above); `vietnamese: null` (literal placeholder) → `thí`; blank `pos` → `名詞`; the stray "too rude" fragment removed and `# Notes` corrected to standard `## Notes` heading level.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 牢 (7279; 958 characters remaining).

### 2026-08-14, iteration 1547 — [[characters/牢|牢]]

`mc_id: 1290` confirmed correct (matches `CC 1000.md` line 303, no off-by-one). `graphemic_classification: 會意` confirmed correct (宀 "pen" + 牛 "cow"), via en.Wiktionary. `korean_native: 우리` and `middle_chinese_initial/final: l`/`ɑu` reconfirmed correct against `聲 來`/`韻 豪` (both lookup pages, plus `SKIP-2-3-4`/`Stroke 07`/`Hyōgai`/`Old HSK 3`/`Korean Name ㄹ`/`Radical 093`, already cited 牢 correctly).

**`vietnamese` contamination fixed**: hvdic gives a completely different Hán Việt set (`lao`, `lâu`, `lạo`) than what was stored (`lao`, `lào`, `sao`, `sau`) — hvdic explicitly labels `sao`/`sau` as Nôm-only and doesn't attest `lào` at all; replaced accordingly, keeping the one already-correct reading (`lao`). **`japanese_native` bug fixed**: corrected bare `かた` to properly hyphenated `かた-い`, and added missing `ひとや` ("prison"), both confirmed via ja.Wiktionary and Jisho. `japanese: ROU` confirmed correct (both sources agree, go-on/kan-on identical). Blank `pos` filled: `名詞`.

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, a stray `## Words`-style bullet floating inside `## Notes` instead of its own section) to the standard format, adding the missing stand-in annotation. No Derived Characters; no Chengyu hits (one grep hit, [[臨渇掘井]], confirmed a false positive). Only the existing stand-in [[牢獄]] cites 牢.

**Citing word page [[牢獄]] had a genuine gap filled**: blank `vietnamese` → `lao ngục`, confirmed as a directly-attested Sino-Vietnamese compound via hvdic (found during this cycle's own research).

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 牽 (7280; 957 characters remaining).

### 2026-08-14, iteration 1548 — [[characters/牽|牽]]

**`mc_id` off-by-one bug fixed** (1587 → 1588; confirmed against `CC 1000.md` line 612). **`graphemic_classification: 玄` confirmed correct** as the phonetic component, but the existing Notes prose had the semantic/phonetic roles swapped — it called 玄 "semantic" and glossed it as "cow, ox" (actually 牛's meaning), and called 牛 "phonetic." Corrected the prose to match the field: semantic 牛 + phonetic 玄, with the character's own additional 冖 element left noted as etymologically uncertain (per en.Wiktionary's own "etymology incomplete" flag, preserved rather than invented). **New variant alias added**: 𪺮, cross-referenced between en.Wiktionary's single "alternative form" and zh.Wiktionary's much longer variant list (the only candidate appearing in both); existing alias 牵 (simplified) reconfirmed correct.

`vietnamese: khin/khiên` confirmed correct via en.Wiktionary. `japanese: KEN` confirmed correct (both sources agree, go-on/kan-on identical). **`japanese_native` bug fixed**: corrected bare `ひ` to properly hyphenated `ひ-く`, confirmed via ja.Wiktionary and Jisho. `korean_native: 끌` and `middle_chinese_initial/final: kʰ`/`en` reconfirmed correct against `聲 溪`/`韻 先開` (both lookup pages, plus `SKIP-2-2-9`/`Stroke 11`/`Jinmeiyō`/`Old HSK 2`, already cited 牽 correctly). **Missing-entry bug fixed**: added 牽 to the `### 견` subsection of `lookup/Korean/Korean Name ㄱ.md`, absent despite `korean: 견`. Blank `pos` filled: `動詞` (an established convention value in this vault, alongside `副詞`, used on other character pages though not itself a leaf name in the formal grammar taxonomy).

Rebuilt malformed `## Notes` (a stray "Added to the Korean HS list in 2000" trivia line folded back into the levels bullet per the established [[蛮]]-style precedent) to the standard format, adding the stand-in annotation to `## Words`. No Derived Characters; no Chengyu hits; only the existing stand-in [[牽引]] cites 牽.

**Citing word page [[牽引]] had two things fixed**: a redundant duplicate `品詞` field (identical value to `pos`, the same recurring pattern seen repeatedly this session); and a genuine gap filled — missing `vietnamese` → `khiên dẫn`, confirmed as a directly-attested Sino-Vietnamese compound via hvdic (found during this cycle's own research).

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 瘋 (7281; 956 characters remaining).

### 2026-08-14, iteration 1549 — [[characters/瘋|瘋]]

`mc_id: 0` confirmed as a legitimate sentinel (瘋 not found anywhere in `CC 0000`–`CC 3000`). **`graphemic_classification: 風` confirmed correct** (形聲, semantic 疒 + phonetic 風), via en.Wiktionary — `韻 東三`'s own final page carries an unusually detailed note explaining 瘋's own syllable outcome (ㄈㄜㄫ) as a deliberate homophony-avoidance shift away from the regular ㄈㄨㄫ, already doubly occupied by 風/楓; folded this directly into the rebuilt phonology bullet. Existing alias 疯 (simplified) reconfirmed correct.

**`vietnamese` contamination fixed**: hvdic explicitly labels the stored `phung` as Nôm-only, not Hán Việt — removed, keeping only the genuine Hán Việt `phong`. `japanese: FUU` and `japanese_native: ø` (no kun-yomi) both confirmed correct — ja.Wiktionary's extra candidates (kan-on ホウ, kun-yomi ずつう) weren't corroborated by Jisho and were left out. **Two blank level fields fixed**: `joyo_level` → `表外字`; `hanmun_edu_level` → `無`. **Missing-entry bugs fixed accordingly**: added 瘋 to `lookup/Japanese/Hyōgai.md` and to the `### 풍` subsection of `lookup/Korean/Korean Name ㅍ.md` (absent despite `korean: 풍`).

**Data-error bug fixed on a shared lookup page**: `lookup/SKIP/SKIP-3/SKIP-3-5-9.md` cited 瘋 with a garbled ruby `ㄆㄨㄫ` — wrong on both initial and final, contradicting every other lookup page (initials, finals, syllable, radical), which all consistently show the correct `ㄈㄜㄫ` — corrected.

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, a `## Words`-style bullet misplaced inside `## Notes` instead of its own section) to the standard format. No Derived Characters; no Chengyu hits; only the existing stand-in [[瘋顚]] (already perfected, no bugs) cites 瘋.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 碩 (7282; 955 characters remaining).

### 2026-08-14, iteration 1550 — [[characters/碩|碩]]

**`mc_id` off-by-one bug fixed** (2510 → 2511; confirmed against `CC 2000.md` line 535). **`graphemic_classification: 石` confirmed correct** — the true semantic component is 頁 ("head"), and 石 is the phonetic; this coincides with the character's own Kangxi radical (also 石) purely by indexing accident, not a duplication error. `vietnamese: thượt/thạc` and existing alias 硕 (simplified) both confirmed correct via en.Wiktionary. `japanese: SEKI` confirmed correct (Jisho corroborates; ja.Wiktionary's extra go-on ジャク wasn't corroborated and was left out). `korean_native: 클` and `middle_chinese_initial/final: d͡ʑ`/`iᴇk` reconfirmed correct against `聲 禪`/`韻 昔開` (both lookup pages, plus `SKIP-1-5-9`/`Stroke 14`/`Jinmeiyō`/`Korean Name ㅅ`/`Radical 112`, already cited 碩 correctly).

**`japanese_native` bug fixed**: corrected bare `おお` to properly hyphenated `おお-きい`, confirmed via ja.Wiktionary and Jisho. Blank `pos` filled: `性詞`.

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets) to the standard format, adding the missing stand-in annotation to `## Words`. No Derived Characters; no Chengyu hits; only the existing stand-in [[碩大]] (already perfected, no bugs — its own rich prose already independently explains the 石-as-phonetic relationship) cites 碩.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 磚 (7283; 954 characters remaining).

### 2026-08-14, iteration 1551 — [[characters/磚|磚]]

`mc_id: 9149` confirmed as legitimate long-tail data (磚 not found anywhere in `CC 0000`–`CC 3000`). **`graphemic_classification: 專` confirmed correct** (形聲, semantic 石 + phonetic 專), via en.Wiktionary. **Three new variant aliases added**: 塼, 甎, 磗, all confirmed genuine via both en.Wiktionary and zh.Wiktionary (a fourth en.Wiktionary-only candidate, 㼷, wasn't corroborated by zh.Wiktionary and was excluded); existing alias 砖 (simplified) reconfirmed correct.

**`vietnamese` contamination fixed**: hvdic explicitly labels the stored `gạch` (the everyday native Vietnamese word for "brick") as Nôm-only, not Hán Việt — removed, keeping only the genuine Hán Việt `chuyên`. `japanese: SEN` and `japanese_native: かわら` both confirmed correct via both ja.Wiktionary and Jisho. **Two blank level fields fixed**: `joyo_level` → `表外字`; `hanmun_edu_level` → `無`. **Two missing-entry bugs fixed accordingly**: added 磚 to `lookup/Japanese/Hyōgai.md`, and to the `### 전` subsection of `lookup/Korean/Korean Name ㅈ.md` — which already had a bare, pageless `[[塼]]` mention but no link for 磚 itself; added both a proper link for the new alias 塼 (pointing to 磚's page, matching the established practice for phonetic-family members without their own page) and a direct entry for 磚. Blank `pos` filled: `名詞`. `korean_native: 벽돌` and `middle_chinese_initial/final: t͡ɕ`/`iuᴇn` reconfirmed correct against `聲 章`/`韻 仙A三合` (both lookup pages, plus `SKIP-1-5-11`/`Stroke 16`/`Old HSK 3`/`Radical 112`, already cited 磚 correctly).

Rebuilt malformed body (`## Words` section misplaced before `# Notes`, wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard format. No Derived Characters; no Chengyu hits; only the existing stand-in [[磚石]] (already perfected) cites 磚.

**Citing word page [[磚石]] left untouched**: missing `japanese`/`vietnamese` fields are genuine never-perfected gaps — a direct hvdic lookup for 磚石 returned no attested compound, so there was no directly-evidenced answer in hand; left for the word-sweep.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 稟 (7284; 953 characters remaining).

### 2026-08-14, iteration 1552 — [[characters/稟|稟]]

**`mc_id` bug fixed** (1700 → 1701): the stored rank actually belonged to a different character, 盾 — 稟's true rank found immediately adjacent on the next line of `CC 1000.md`. `graphemic_classification: 㐭` confirmed correct (會意, 㐭 "granary" + 禾 "grain"), via en.Wiktionary — `韻 侵A`'s own final page independently notes 稟's unconditioned landing alongside 凜, corroborating the phonetic-family relationship documented below.

**Major `vietnamese` bug fixed**: the stored seven-entry list mixed one genuine Hán Việt reading (`bẩm`) with six Nôm-only or entirely unattested forms — hvdic gives a completely different, much shorter genuine set: `bẩm` and `lẫm`. Replaced accordingly. `japanese: RIN/HIN` and `japanese_native: こめぐら` both confirmed correct (Jisho corroborates both; ja.Wiktionary's several extra kun-yomi candidates weren't corroborated and were left out). `korean_native: 여쭐` and `middle_chinese_initial/final: p`/`iɪm` reconfirmed correct against `聲 幫`/`韻 侵A` (both lookup pages, plus `SKIP-2-2-11`/`Stroke 13`/`Jinmeiyō`/`Korean Name ㅍ`/`Radical 115`, already cited 稟 correctly). Blank `pos` filled: `動詞`.

Merged two duplicate `## Notes` sections and rebuilt to the standard format (a stray `## Words`-style bullet was misplaced inside the first `## Notes` block). **Found and added a new `## Derived Characters` section**: [[凜 (char)|凜]], confirmed via its own `graphemic_classification: 稟`. No Chengyu hits; only the existing stand-in [[稟告]] cites 稟.

**Citing word page [[稟告]] left untouched**: missing `vietnamese` is a genuine never-perfected gap — a direct hvdic lookup for 稟告 returned no attested compound, so there was no directly-evidenced answer in hand; left for the word-sweep.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 竄 (7285; 952 characters remaining).

### 2026-08-14, iteration 1553 — [[characters/竄|竄]]

**`mc_id` off-by-one bug fixed** (2700 → 2701; confirmed against `CC 2000.md` line 729). **`graphemic_classification: 會意` confirmed correct** (鼠 "mouse" + 穴 "hole"), via en.Wiktionary. **Three new variant aliases added**: 䞼, 窾, 躥, all confirmed genuine via zh.Wiktionary (none hold their own vault page); existing alias 窜 (simplified) reconfirmed correct.

**Major `english` bug fixed and its cascade traced**: the stored gloss `revise, edit` covered only a minor, compound-only sense — the character's true primary and etymological meaning is "to flee, hide, go into exile" (literally "to hide in a hole"), with "falsify, tamper with" as the specific sense activated in its stand-in compound. Corrected to `[flee, hide, falsify, tamper with]`; the identical narrow "revise" gloss had also propagated to `syllables/ㄑㄚㄋ.md`, `lookup/SKIP/SKIP-2/SKIP-2-3-15.md`, and `lookup/Radicals/Radical 116.md`, all fixed to match. This correction is independently corroborated by the citing word [[改竄]]'s own pre-existing prose, which already explains "竄's core sense is 'to hide, to conceal, to flee into hiding.'"

`vietnamese: thoán` confirmed correct via en.Wiktionary. `japanese: ZAN/SAN` confirmed correct (both sources agree: SAN is go-on/kan-on, ZAN is kan'yō-on). **`japanese_native` bug fixed**: corrected bare `かく` to properly hyphenated `かく-れる`, and added missing `のが-れる` ("to escape"), both confirmed via ja.Wiktionary and Jisho. `korean_native: 숨을` and `middle_chinese_initial/final: t͡sʰ`/`uɑn` reconfirmed correct against `聲 清`/`韻 桓` (both lookup pages, plus `SKIP-2-3-15`/`Stroke 18`/`Hyōgai`/`Old HSK 3`/`Korean Name ㅊ`, already cited 竄 correctly).

Rebuilt malformed body (`## Words` section misplaced before `# Notes`, wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard format. No Derived Characters; no Chengyu hits; only the existing stand-in [[改竄]] cites 竄.

**Citing word page [[改竄]] had one bug fixed**: a redundant duplicate `品詞` field (identical value to `pos`, the same recurring pattern seen repeatedly this session). Missing `vietnamese` left untouched — a direct hvdic lookup for 改竄 returned no attested compound.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 竦 (char) (7286; 951 characters remaining).

### 2026-08-14, iteration 1554 — [[characters/竦 (char)|竦]]

**`mc_id` off-by-one bug fixed** (2580 → 2581; confirmed against `CC 2000.md` line 605). **`graphemic_classification: 束` confirmed correct** (形聲, semantic 立 + phonetic 束), via en.Wiktionary. **Existing alias 聳 investigated and reconfirmed correct**: zh.Wiktionary's own page for 竦 doesn't mention 聳 at all, but en.Wiktionary's page for 聳 explicitly calls it "an alternative form" of 竦 (same word family via a different phonetic route, 從 vs 束) — treated as one source confirming vs. the other simply not addressing it, not a contradiction; `lookup/Korean/Korean Name ㅅ.md` independently corroborates by already linking 聳 to 竦's own page. **New variant alias added**: 捒, confirmed via zh.Wiktionary.

`vietnamese: tủng` confirmed correct via hvdic. `japanese: SHOU` confirmed correct (Jisho corroborates; ja.Wiktionary's extra go-on シュ wasn't corroborated and was left out). **`japanese_native` bug fixed**: expanded bare `おそ` to the full three-item kun-yomi list confirmed by both sources — `すく-む`, `おそ-れる`, `つつし-む`. `korean_native: 공경할` and `middle_chinese_initial/final: s`/`ɨoŋ` reconfirmed correct against `聲 心`/`韻 鍾` (both lookup pages, plus `SKIP-1-5-7`/`Stroke 12`/`Hyōgai`/`Korean Name ㅅ`/`Radical 117`, already cited 竦 correctly). Blank `pos` filled: `名詞`.

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets, no `## Words` section) to the standard format. No Derived Characters; no Chengyu hits; only the existing self stand-in cites 竦.

**Citing word page [[竦]] (self stand-in) had two gaps filled**: blank `vietnamese` → `tủng`; blank `pos` → `名詞`.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 箔 (7288; 950 characters remaining).

### 2026-08-14, iteration 1555 — [[characters/箔|箔]]

`mc_id: 0` confirmed as a legitimate sentinel (箔 not found anywhere in `CC 0000`–`CC 3000`). **`graphemic_classification: 泊` confirmed correct** (形聲, semantic 竹 + phonetic 泊, itself derived from 薄), via en.Wiktionary — `韻 鈬合`'s own final page independently groups 博/泊/箔/薄 together as evidence for a labial w-glide-ban phonotactic rule, corroborating the phonetic link. `vietnamese: bạc`, `japanese: HAKU` (Jisho corroborates; ja.Wiktionary's extra go-on バク wasn't corroborated and was left out), and `japanese_native: すだれ` all reconfirmed correct. `korean_native: 발` and `middle_chinese_initial/final: b`/`wɑk` reconfirmed correct against `聲 並`/`韻 鈬合` (both lookup pages, plus `SKIP-2-6-8`/`Stroke 14`/`Jinmeiyō`/`Korean Name ㅂ`, already cited 箔 correctly).

**Broken-path bug fixed**: the finals-lookup wikilink used `../lookup/CC/finals/...` (one directory up) instead of the bare `lookup/CC/finals/...` form used everywhere else — the same broken-relative-path pattern seen recurring throughout this project, here in a not-yet-seen variant directory depth. Blank `pos` filled: `名詞`.

Rebuilt malformed `# Notes` (wrong heading level, no `## Words` section) to the standard format. No Derived Characters; no Chengyu hits; only the existing stand-in [[蚕箔]] cites 箔.

**Citing word page [[蚕箔]] had a genuine gap filled**: blank `vietnamese` → `tàm bạc`, confirmed as a directly-attested Sino-Vietnamese compound via hvdic (found during this cycle's own research); its other blank fields (`pos`, `japanese`, `korean`) are genuine never-perfected gaps left for the word-sweep, since no directly-evidenced answers were in hand for those.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 糊 (7289; 949 characters remaining).

### 2026-08-14, iteration 1556 — [[characters/糊|糊]]

`mc_id: 9479` confirmed as legitimate long-tail data (糊 not found anywhere in `CC 0000`–`CC 3000`). **`graphemic_classification: 胡` confirmed correct** (形聲, semantic 米 + phonetic 胡), via en.Wiktionary. **Five new variant aliases added**: 䊀, 餬, 䭌, 䭅, 𬲾, all confirmed genuine via both en.Wiktionary and zh.Wiktionary; excluded the second-round-simplified 胡, since it's a full independent character with its own distinct meaning.

**`english` bug fixed**: the stored `[muddled, confused]` covered only the character's figurative sense, while `korean_native: 죽` ("porridge") and `japanese_native: のり` ("paste") already correctly reflected its more fundamental meanings — added `paste` and `porridge` ahead of the existing entries rather than replacing them, since "muddled" remains accurate for the figurative sense used in the stand-in compound; left the identical "muddled" short-glosses on shared lookup pages (SKIP, syllable, radical) unchanged, since those aren't factually wrong, just abbreviated to one sense.

`vietnamese: hồ` and `japanese: KO/GO` (both go-on/kan-on) both confirmed correct via ja.Wiktionary. `korean_native: 죽` and `middle_chinese_initial/final: ɣ`/`uo` reconfirmed correct against `聲 匣`/`韻 模` (both lookup pages — the latter's own page documents 糊 as part of a 5-member overflow group escaping Cantonese's single most crowded ㄏㄛ slot — plus `SKIP-1-6-9`/`Stroke 15`/`Jinmeiyō`/`Korean Name ㅎ`/`Old HSK 2`/`Radical 119`, already cited 糊 correctly). Blank `pos` filled: `性詞`.

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets, no `## Words` section) to the standard format. No Derived Characters; no Chengyu hits (one grep hit, [[汗食帰泥]], confirmed a false positive). Only the existing stand-in [[糊塗]] cites 糊.

**Citing word page [[糊塗]] had a genuine gap filled**: blank `vietnamese` → `hồ đồ`, confirmed as a directly-attested Sino-Vietnamese compound via hvdic (found during this cycle's own research).

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 糞 (char) (7290; 948 characters remaining).
