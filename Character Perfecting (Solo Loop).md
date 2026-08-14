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

### 2026-08-14, iteration 1557 — [[characters/糞 (char)|糞]]

**`mc_id` off-by-one bug fixed** (2555 → 2556; confirmed against `CC 2000.md` line 581). **`graphemic_classification` bug fixed** (`會意` → `象形`): en.Wiktionary's summary was self-contradictory (labeled it 象形 but described a 米+異 compound sounding like 會意), while zh.Wiktionary explicitly and unambiguously classifies 糞 as 象形 with detailed oracle-bone/seal-script justification — two hands (廾) sweeping away scattered filth-dots, originally meaning "to sweep," with the modern form's dots reinterpreted as 米-like grains as the meaning narrowed to excrement/dung. Added to `lookup/List of 象形.md`'s manual character list (grouped by radical, inserted alongside the other 米-radical entries), since it wasn't there under the old wrong classification. Existing alias 𥻔 and simplified 粪 both reconfirmed correct via zh.Wiktionary's own (much longer) variant list.

`vietnamese: phẩn/phân` and existing alias 粪 confirmed correct via en.Wiktionary. `japanese: FUN` and `japanese_native: くそ` both confirmed correct via ja.Wiktionary. `korean_native: 똥` and `middle_chinese_initial/final: f`/`ɨun` reconfirmed correct against `聲 非`/`韻 文` (both lookup pages — the former's own page independently documents 糞's deliberate coda-shift homophony dodge away from a crowded ㄈㄨㄋ cluster shared with 奮/芬/粉/雰, folded directly into the rebuilt phonology bullet alongside the pre-existing "-m so there's no homophony" trivia note — plus `SKIP-2-6-11`/`Stroke 17`/`Hyōgai`/`Old HSK 3`/`Korean Name ㅂ`, already cited 糞 correctly). Blank `pos` filled: `名詞`.

Rebuilt malformed `## Notes` (missing SKIP/Stroke, MC-phonology, and levels bullets entirely — only the stray homophony-avoidance trivia line was present) to the standard format, adding the missing `## Words` section. No Derived Characters. Existing `## Chengyu` entry [[朽木糞牆]] reconfirmed a genuine hit (糞 present in its `characters:` field).

**Citing word page [[糞]] (self stand-in) had multiple bugs fixed**: `vietnamese: null` (literal placeholder) → `phân`; `注音`/`羅馬字`/`諺文` (`ㄆㄨㄋ`/`pun`/`푼`) were all stale pre-correction values, out of sync with the character page's own already-fixed syllable (`ㄈㄨㄇ`/`fum`/`뿜`) — brought into alignment; blank `pos` → `名詞`.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 紮 (char) (7292; 947 characters remaining).

### 2026-08-14, iteration 1558 — [[characters/紮 (char)|紮]]

`mc_id: 6215` confirmed as legitimate long-tail data (紮 not found anywhere in `CC 0000`–`CC 3000`, but this range is normal — 481 characters vault-wide carry mc_id values above 3999, evidently real MC dictionary ranks simply not covered by a dedicated per-rank lookup page). **`graphemic_classification: 札` confirmed correct** (形聲, semantic 糸 + phonetic 札), via en.Wiktionary. **New variant alias added**: 紥, confirmed via both en.Wiktionary and zh.Wiktionary; existing alias 扎 (simplified) reconfirmed correct.

`vietnamese: trát`, `japanese: SATSU`, and `japanese_native: からげる` all reconfirmed correct via both ja.Wiktionary and Jisho (en.Wiktionary's extra go-on セチ and kun たばねる candidates weren't corroborated by Jisho and were left out). `korean_native: 감을` and `middle_chinese_initial/final: t͡ʃ`/`ɣɛt` reconfirmed correct against `聲 莊`/`韻 鎋開` (both lookup pages, plus `SKIP-2-5-6`/`Stroke 11`/`Hyōgai`/`Korean Name ㅊ`/`Radical 120`, already cited 紮 correctly). **Blank `hsk_level` bug fixed**: `Old HSK 2.md` already cites 紮 (via its simplified alias 扎) but the character's own frontmatter field was left blank — filled `2`. Blank `pos` filled: `動詞`.

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets, no `## Words` section) to the standard format. No Derived Characters; no Chengyu hits. Two grep hits on other word pages ([[束]], [[某処]]) confirmed false positives — both merely mention 紮 in prose (a Cantonese classifier example; a "駐紮" example), not in their `characters:` field. Only the existing self stand-in cites 紮.

**Citing word page [[紮]] (self stand-in) had two gaps fixed**: `vietnamese: null` (literal placeholder) → `trát`; blank `pos` → `動詞`.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 繃 (7294; 946 characters remaining).

### 2026-08-14, iteration 1559 — [[characters/繃|繃]]

`mc_id: 10446` confirmed as legitimate long-tail data. **`graphemic_classification: 崩` confirmed correct** (形聲, semantic 糸 + phonetic 崩), via en.Wiktionary. **Self-reference alias bug fixed**: the stored `aliases` list included 繃 itself (the character's own form) instead of a genuine variant — replaced with 綳, confirmed as the true 異體字 via both en.Wiktionary ("Traditional: 繃, 綳") and zh.Wiktionary (explicitly flagged as the primary variant); existing simplified alias 绷 reconfirmed correct.

**Major `english` bug fixed and its cascade traced**: the stored gloss `bandage` is actually the meaning of the two-character stand-in compound 繃帯, not of 繃 itself — the character's own core meaning across all three Mandarin tone-readings (bēng/běng/bèng) is "to bind, wrap, stretch taut" (per en.Wiktionary), independently corroborated by `korean_native: 묶을` ("to tie") and the kun-yomi meanings "to bundle" / "to wrap." Corrected to `[bind, wrap, stretch tight]`; the identical "bandage" mis-gloss had also propagated to `lookup/Radicals/Radical 120.md`, fixed to match — the vault's own `syllables/ㄅㄚㄫ.md` page already independently had the correct "bind, wrap" gloss, serving as corroboration. Blank `pos` filled: `動詞`.

**`japanese_native` bug fixed**: stored bare `たば` was a truncated/wrong form — corrected to properly hyphenated `たば-ねる` ("to bundle"), and added missing second kun-yomi `まく` ("to wrap"), both confirmed via ja.Wiktionary and Jisho. `japanese: HOU/HYOU` confirmed correct (both sources agree, kan-on/go-on). **Two blank level fields fixed**: `joyo_level` → `表外字` (real on'yomi/kun'yomi usage with no jōyō/jinmeiyō classification) — **missing-entry bug fixed accordingly**, adding 繃 to `lookup/Japanese/Hyōgai.md` (absent despite having real readings, unlike every other level list which already cited it correctly).

**`vietnamese` gap filled**: hvdic's Hán Việt list has three readings (`banh`, `băng`, `bắng`) but only two were stored — added the missing `banh`. `korean_native: 묶을` and `middle_chinese_initial/final: p`/`ɣɛŋ` reconfirmed correct against `聲 幫`/`韻 耕開` (both lookup pages, plus `SKIP-1-6-11`/`Stroke 17`/`Korean Name ㅂ`/`Old HSK 4`, already cited 繃 correctly).

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets, missing stand-in annotation in `## Words`) to the standard format. No Derived Characters; no Chengyu hits; only the existing stand-in [[繃帯]] (already perfected, its own "bandage" gloss correctly describes the compound, not the character alone — left untouched) cites 繃.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 繞 (char) (7295; 945 characters remaining).

### 2026-08-14, iteration 1560 — [[characters/繞 (char)|繞]]

**`mc_id` off-by-one bug fixed** (2690 → 2691; confirmed against `CC 2000.md` line 719-720, where "2690. 驟" precedes "2691. 繞" — the same one-line-off transcription pattern seen repeatedly). **`graphemic_classification: 堯` confirmed correct** (形聲, semantic 糸 + phonetic 堯, OC \*ŋeːw), via en.Wiktionary and independently corroborated by zh.Wiktionary's own 堯-phonetic 系列#2193 family listing. **Broken phonetic link bug fixed**: the graphemic bullet's `[[]]` (empty wikilink) was repaired to `[[堯]]`, and the OC reconstruction for the whole character (\*ŋjewʔ, \*ŋjaws, Zhengzhang) was kept and independently reconfirmed against en.Wiktionary's own Zhengzhang-system entries. **New variant alias added**: 遶, confirmed genuine via both en.Wiktionary ("alternative form") and zh.Wiktionary's dedicated 異體字 box; zh.Wiktionary's box also listed 撓, but that was excluded as a distinct independent character (扌-radical, unrelated core meaning "to scratch/disturb/yield") not corroborated by en.Wiktionary — the same reasoning used to exclude 胡 from [[characters/糊|糊]]'s alias list two iterations ago. Existing simplified alias 绕 reconfirmed correct.

**Major `vietnamese` contamination bug fixed**: the stored 11-entry list (diễu, díu, nhiễu, nhão, nhảu, nhẹo, nhẻo, nhẽo, nhếu, nhểu, thêu) was almost entirely spurious — hvdic's actual entry for 繞 lists exactly **one** genuine Hán Việt reading, `nhiễu`, with diễu/díu/nhão/nhẽo/thêu explicitly filed under a separate "Âm Nôm" (Nôm-only) section, and nhảu/nhẹo/nhẻo/nhếu/nhểu not attested anywhere on the page at all (evidently fabricated near-duplicates of the genuine Nôm forms). Trimmed to `nhiễu` alone, the vault's most severe case yet of this session's recurring Hán-Việt/Nôm contamination pattern.

`japanese: JOU/NYOU` confirmed correct (both ja.Wiktionary's go-on にょう/kan-on じょう and Jisho's ニョウ/ジョウ agree). **`japanese_native` bug fixed**: bare unhyphenated `まとう` was expanded and corrected to the four verb readings corroborated by both ja.Wiktionary and Jisho — `まと-う`, `まわ-る`, `めぐ-る`, `もとう-る` — with proper okurigana hyphenation applied throughout; ja.Wiktionary's extra からむ/まつわる weren't corroborated by Jisho and were left out. `korean_native: 두를` and `middle_chinese_initial/final: ȵ`/`iᴇu` reconfirmed correct against `聲 日`/`韻 宵A` (both lookup pages already cited 繞 correctly — the latter's own page independently notes 繞 and 擾 share the identical ȵ initial yet land on opposite sides of its ⼄ㄨ/ㄛㄨ split, one of its documented "same initial, arbitrary outcome" cases). `korean: 요` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㅇ.md`'s `### 요` subsection already lists 繞 correctly. **Blank `joyo_level` filled**: `表外字` (real on'yomi/kun'yomi usage, Jisho explicitly confirms no jōyō/jinmeiyō status) — **missing-entry bug fixed accordingly**, adding 繞 to `lookup/Japanese/Hyōgai.md` (absent despite having real readings). Blank `pos` filled: `事詞` (a transitive verb per 文法 - 97品詞's Eventive definition — "to surround/entwine [something]").

Rebuilt malformed `## Notes` (missing MC-rank/phonology and levels bullets entirely, two bare unlinked CC-lookup wikilinks floating at the bottom) to the standard format, adding the missing `## Words` section. No Derived Characters (no other character names 繞 as its `graphemic_classification`); no Chengyu hits. Only the existing self stand-in cites 繞.

**Citing word page [[繞]] (self stand-in) had two gaps fixed**: `vietnamese: null` (literal placeholder) → `nhiễu`; blank `pos` → `事詞`. Its `注音`/`羅馬字`/`諺文` (`ㄋㄛㄨ`/`nou`/`놋`) were already in sync with the character page.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 纂 (7296; 944 characters remaining).

### 2026-08-14, iteration 1561 — [[characters/纂|纂]]

**`mc_id` off-by-one bug fixed** (3391 → 3392; confirmed against `CC 3000.md` line 405-409, where "3391. 刊" precedes "3392. 纂" — the same one-line-off transcription pattern seen repeatedly this session). **`graphemic_classification: 算` confirmed correct** (形聲, semantic 糸 + phonetic 算), via en.Wiktionary and independently corroborated by zh.Wiktionary (⿱𮅕糸 composition, phonetic series including 算). Both sources' Zhengzhang reconstruction for the whole character agree exactly (\*ʔsloːnʔ), embedded in the rebuilt graphemic bullet alongside 算's own OC \*sloːnʔ.

**Major `vietnamese` bug fixed**: the stored `soạn` is exactly the Nôm-only trap the checklist warned about — hvdic's actual entry for 纂 lists "Âm Hán Việt: toản" as the sole genuine Sino-Vietnamese reading and explicitly files `soạn` under "Âm Nôm" (Nôm-only), confirming it belongs to an unrelated 撰-family word, not 纂 itself. Corrected to `toản`.

`japanese: SAN` confirmed correct (both ja.Wiktionary's go-on/kan-on さん and Jisho's サン agree). **`japanese_native` bug fixed**: bare unhyphenated `あつ` was a truncated form — corrected to properly hyphenated `あつ-める` ("to gather/compile"), confirmed via both ja.Wiktionary and Jisho, and matching the character's own English gloss. `korean_native: 모을` and `middle_chinese_initial/final: t͡s`/`uɑn` reconfirmed correct against `聲 精`/`韻 桓` (both lookup pages already cited 纂 correctly — the former's own page independently documents 纂 as one of 97 regular ㄐ-palatalization outcomes in the 精組 series, plus `SKIP-2-6-14`/`Stroke 20`, already cited 纂 correctly). `korean: 찬` reconfirmed correct (no 두음법칙 concern); `Lookup/Korean/Korean Name ㅊ.md`'s `### 찬` subsection already lists 纂 correctly. `joyo_level: 日本人名用漢字` confirmed a legitimate convention value; `lookup/Japanese/Jinmeiyō.md` already cites 纂 (#253) correctly. Blank `pos` filled: `事詞` (a transitive verb per 文法 - 97品詞's Eventive definition — "to compile/edit [something]"), matching the citing word page's own already-correct `動詞`-family classification in spirit.

**No alias added**: en.Wiktionary's "alternative forms" list (篹, 纘/缵, 繤, 䰖/𱆈) was not corroborated by zh.Wiktionary, which instead labels a different, unrelated set (攥, 𣠹, 𨰭) as 衍生字 (characters derived *from* 纂, not variants *of* it) — since the two sources disagree rather than agree, no alias was added, left as a genuine gap per the "only add if both sources agree" policy. Both sources agree 纂 has no separate simplified form (identical in both scripts).

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks floating with no bullet structure) to the standard format. **No Derived Characters needed on 纂's own page** (nothing names 纂 as its own phonetic component), but confirmed 纂's phonetic parent [[characters/算 (char)|算]] already correctly lists 纂 in its own `## Derived Characters` section — no fix needed there. No Chengyu hits: the one grep match ([[焚琴煮鶴]]) only mentions 纂 in its `origin` citation (a book title, 《雜纂·殺風景》), not in its `characters:` field — false positive. Only the existing stand-in [[編纂]] cites 纂 as a constituent.

**Citing word page [[編纂]] (stand-in) reviewed, no bugs found**: `vietnamese: biên soạn` is a genuine, independently attested Vietnamese compound term for "to compile" (not a literal concatenation of the two characters' individual readings, so 纂's own corrected `toản` does not propagate here) — left untouched; `pos: 動詞` already filled with no duplicate `品詞` field; `注音`/`羅馬字`/`諺文` (`ㄅ⼶ㄋㄐ⺢ㄋ`/`byenjwan`/`변좐`) already in sync with the character page's own corrected syllable.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 罹 (7297; 943 characters remaining).

### 2026-08-14, iteration 1562 — [[characters/罹|罹]]

**`mc_id` off-by-one bug fixed** (3197 → 3198; confirmed against `CC 3000.md` line 206-207, where "3197. 胙" precedes "3198. 罹" — the same one-line-off transcription pattern seen repeatedly this session). **`graphemic_classification: 會意` confirmed correct**: en.Wiktionary analyzes 罹 as an ideogrammic compound of 网 ("net") + 忄 ("heart") + 隹 ("bird") — a bird caught in a net, its capture felt as anxiety of heart. zh.Wiktionary's own quoted Shuowen Jiezi entry ("心憂也。从网。未詳。古多通用離。") does not contradict this — Xu Shen himself calls the phonetic derivation "unclear" (未詳) rather than asserting a 形聲 reading, so there was no competing claim to weigh against en.Wiktionary's compound analysis. Linked all three components to their Radical lookup pages ([[Radical 122|网]], [[Radical 061|忄]], [[Radical 172|隹]]), since all three are themselves Kangxi radicals, per the checklist's radical-linking rule.

**Major `vietnamese` gap filled**: hvdic's entry for 罹 lists three genuine Âm Hán Việt readings — `duy, li, ly` — but only `li` was stored; added the missing `duy` and `ly` (hvdic separately flags `li` as also usable as an Âm Nôm reading, which doesn't disqualify it since it's independently attested as Hán Việt too).

**`japanese` bug fixed**: dropped uncorroborated `RA` — en.Wiktionary lists only go-on/kan-on り (RI) with no Tō-on or other category, while Jisho alone adds ラ (RA); since only RI is corroborated by both sources, RA was excluded, matching this session's established cross-reference policy (e.g. 繃's excluded セチ/たばねる). **`japanese_native` bug fixed**: bare unhyphenated `かか` corrected to properly hyphenated `かか-る` ("to be afflicted with, incur"), confirmed via both ja.Wiktionary and Jisho, matching the English gloss. `korean_native: 걸릴` and `middle_chinese_initial/final: l`/`iᴇ` reconfirmed correct against `聲 來`/`韻 支三開` (both lookup pages already cited 罹 correctly — the latter's own page independently lists 罹 among 10 members of its documented ㄧ overflow group, escaping a maximally crowded ㄙㄝ slot). `korean: 리` reconfirmed correct (genuine North Korean/문화어 form, no 두음법칙 concern); `Lookup/Korean/Korean Name ㄹ.md`'s `### 리` subsection already lists 罹 correctly, and `kwin: true` is consistent (諺文 리 matches korean 리 exactly). `joyo_level: 表外字` confirmed correct; `lookup/Japanese/Hyōgai.md` already cites 罹 (#254). Blank `pos` filled: `事詞` (a transitive verb per 文法 - 97品詞's Eventive definition — "to incur/suffer from [something]"), matching the pattern used on similar-meaning characters this session (繞→事詞, 纂→事詞).

**No alias added**: en.Wiktionary's formal "Alternative forms" box lists 離/离, but 離 is itself a full independent character already in the vault with its own distinct primary meaning ("leave, separate") — its appearance here traces to Shuowen's note that the two were "anciently often used interchangeably" (古多通用離), a historical loan-usage note, not a graphemic variant claim. zh.Wiktionary's own 異體字 box instead lists an unrelated pair, 𦌐 and 𮊔, not corroborated by en.Wiktionary. Since the two sources disagree entirely, no alias was added — left as a genuine gap, same reasoning as 纂's excluded candidates two iterations ago.

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks floating with no bullet structure at all — no SKIP/Stroke bullet, no MC-rank bullet, no levels bullet) to the standard format, adding the missing `## Words` section. No Derived Characters (nothing names 罹 as its own `graphemic_classification`); no Chengyu hits (no `chengyu/*.md` cites 罹 in its `characters:` field). Only the existing stand-in [[罹患]] cites 罹 as a constituent.

**Citing word page [[罹患]] (stand-in) had a stale-syllable bug fixed**: its `注音`/`羅馬字`/`諺文` for the 患 half (`ㄏ⼘ㄋ`/`hwan`/`환`) were out of sync with [[characters/患 (char)|患]]'s own already-perfected syllable (`ㄏ⺢ㄇ`/`hwam`/`홤`) — corrected to `ㄌㄧㄏ⺢ㄇ`/`lihwam`/`리홤` throughout, and propagated the same fix to `syllables/ㄌㄧ.md`'s own citation of the same compound reading. `pos: 事詞` was already filled with no duplicate `品詞` field. `vietnamese` left blank as a genuine gap — hvdic has no dedicated entry for the compound 罹患 itself, only for the individual characters, so no directly-evidenced compound reading was in hand.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 羸 (7298; 942 characters remaining).

### 2026-08-14, iteration 1563 — [[characters/羸|羸]]

**`mc_id` off-by-one bug fixed** (2050 → 2051; confirmed against `CC 2000.md` line 55-56, where "2050. 俯" precedes "2051. 羸" — the same one-line-off transcription pattern seen repeatedly this session). **`graphemic_classification: 象形` bug fixed → `蠃`**: en.Wiktionary's Glyph origin section for 羸 shows a phonetic-series table naming 蠃 as the phonetic component (OC \*roːl, shared with 驘/鸁/臝, all \*roːl-family), with 羊 as the semantic determiner (OC whole-character \*rol, Zhengzhang) — 象形 was simply wrong for a 19-stroke compound like this, exactly the kind of error the checklist flagged as plausible going in. zh.Wiktionary's own "系列#2307" derived-character family listing independently corroborates the same phonetic cluster (𦝠/𣎆/𦟀/嬴/赢/贏/蠃/羸/臝/驘/鸁). Linked the semantic component to its Radical page (`[[Radical 123|羊]]`), since 羊 is itself a Kangxi radical, and the phonetic `[[蠃]]` as a bare link (no vault page exists yet for 蠃, same red-link convention already established for 繞's phonetic 堯).

**No alias added**: zh.Wiktionary's 異體字 box lists 贏, but en.Wiktionary treats 贏 as an entirely distinct character (its own phono-semantic compound, semantic 貝ではなく羊, meaning "to win/profit," Proto-Lolo-Burmese cognate, no cross-reference to 羸 at all) — since the two sources disagree rather than agree, no alias was added, matching the same reasoning used to exclude 離 from [[characters/罹|罹]]'s alias list and 撓 from [[characters/繞 (char)|繞]]'s alias list two and three iterations ago.

**`vietnamese` gap filled**: hvdic's entry for 羸 explicitly lists two genuine Âm Hán Việt readings — `luy, nuy` — with no Nôm-only flag on either; only `luy` was stored, added the missing `nuy`.

`japanese: RUI` confirmed correct as the sole corroborated on-yomi (ja.Wiktionary's extra ren/レン go-on/kan-on reading wasn't corroborated by Jisho, excluded per this session's established cross-reference policy, e.g. 罹's excluded RA). **`japanese_native` bug fixed**: bare unhyphenated `つか` was a truncated fragment — corrected to the two kun-yomi corroborated by both ja.Wiktionary and Jisho, properly hyphenated: `つか-れる` ("to become exhausted") and `よわ-い` ("weak"); ja.Wiktionary's extra みつる/やせる/よわる weren't corroborated by Jisho and were left out. `korean_native: 파리할` and `middle_chinese_initial/final: l`/`iuᴇ` reconfirmed correct against `聲 來`/`韻 支三合` (both lookup pages already cited 羸 correctly — the latter's own page independently lists 羸 among 12 of 13 members landing on the regular ㄨㄧ outcome, with only 瑞 escaping to a homophony-driven ⼔). `korean: 리` reconfirmed correct (genuine North Korean/문화어 form, no 두음법칙 concern); `Lookup/Korean/Korean Name ㄹ.md`'s `### 리` subsection already lists 羸 correctly, and `kwin: false` is consistent (諺文 뤼 differs from korean 리). **Blank `joyo_level` filled**: `表外字` (real on'yomi/kun'yomi usage, both ja.Wiktionary and Jisho confirm no jōyō/jinmeiyō status) — **missing-entry bug fixed accordingly**, adding 羸 to `lookup/Japanese/Hyōgai.md` as entry #307 (absent despite having real readings). Blank `pos` filled: `性詞` (a stative per 文法 - 97品詞's definition — "weakness, frailty" is a quality/state, not an action), matching the citing word page's own already-correct `性詞` classification.

Rebuilt malformed `## Notes` (two bare unlinked CC-lookup wikilinks floating with no bullet structure at all — no graphemic bullet, no SKIP/Stroke bullet, no MC-rank bullet, no levels bullet) to the standard format. Radical 123 (羊)'s own lookup page, `SKIP-2-2-17`, `Stroke 19`, `Korean Name ㄹ` all already cited 羸 correctly before this iteration. No Derived Characters (nothing names 羸 as its own `graphemic_classification`); no Chengyu hits (no `chengyu/*.md` cites 羸 in its `characters:` field). Only the existing stand-in [[羸弱]] cites 羸 as a constituent.

**Citing word page [[羸弱]] (stand-in) reviewed, no bugs found**: its `羅馬字`/`諺文`/`注音` (`luinyag`/`뤼냑`/`ㄌㄨㄧㄋ⼘ㄎ`) are already in sync with both constituent characters' own syllables ([[characters/羸|羸]]'s `lui`/`뤼`/`ㄌㄨㄧ` and [[characters/弱 (char)|弱]]'s already-perfected `nyag`/`냑`/`ㄋ⼘ㄎ`); `pos: 性詞` already filled with no duplicate `品詞` field; blank `vietnamese` is correctly *omitted* per the word checklist's own rule (optional fields are omitted, not left empty, when blank) rather than a bug — hvdic has no dedicated entry for the compound 羸弱 itself, only for the individual characters, so this is a genuine gap, not a placeholder to fix, same as [[characters/罹|罹]]'s citing word page one iteration ago.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 翔 (7299; 941 characters remaining).

### 2026-08-14, iteration 1564 — [[characters/翔|翔]]

**`mc_id: 1841` confirmed correct** — first clean rank verified against `CC 1000.md` in a while, with no off-by-one this time: line 877-878 reads "1840. 嗚" directly preceding "1841. 翔." **`graphemic_classification: 羊` confirmed correct** (形聲, semantic 羽 + phonetic 羊), via en.Wiktionary, which gives the Zhengzhang OC reconstruction for the whole character as \*ljaŋ and for 羊 alone as \*laŋ; zh.Wiktionary's Baxter-Sagart entry (\*s-ɢaŋ) doesn't contradict this, being a different reconstruction system built on the same 羊 phonetic root.

`vietnamese: tường` confirmed correct and genuine Hán Việt via hvdic — notably hvdic lists it under *both* its Hán Việt and its "Âm đọc khác" Nôm sections rather than flagging a separate contaminating Nôm form, so no correction was needed (unlike the severe contamination found on 繞/纂/羸 in prior iterations). `japanese: SHOU` confirmed correct as the sole corroborated reading — en.Wiktionary and ja.Wiktionary both additionally list a go-on ゾウ, but Jisho shows only ショウ, so ゾウ was excluded per this session's established both-sources policy (matching 罹's excluded RA, 羸's excluded REN). **`japanese_native` bug fixed**: bare unhyphenated `かけ` was a truncated single reading — corrected to a properly hyphenated two-item list, `かけ-る` ("to soar/glide") and `と-ぶ` ("to fly"), both corroborated by both ja.Wiktionary and Jisho.

`korean_native: 날` (consistent with the "fly" gloss), `middle_chinese_initial/final: z`/`ɨɐŋ` reconfirmed correct against `聲 邪`/`韻 陽開` (both lookup pages already cited 翔 correctly — the former's page independently documents 翔 among 46 of 49 regular ㄙ outcomes in the 邪 series, the latter among the 45-member ⼘ㄫ y-glide majority of its five-way split), plus `SKIP-1-6-6`/`Stroke 12`, already cited 翔 correctly. `korean: 상` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㅅ.md`'s `### 상` subsection already lists 翔 correctly. `joyo_level: 日本人名用漢字` confirmed a legitimate convention value (Jisho explicitly labels 翔 "Jinmeiyō kanji, used in names"); `lookup/Japanese/Jinmeiyō.md` already cites 翔 (#320) correctly. `Lookup/Radicals/Radical 124.md` (羽) already lists 翔 correctly at +6 strokes. Blank `pos` filled: `事詞` (an intransitive Eventive per 文法 - 97品詞's definition — "to soar/fly" is an action without an object), matching [[characters/飛 (char)|飛]]'s own identical `事詞` classification for the closely related "fly" sense.

**No alias added**: en.Wiktionary mentions derived-series characters 𦤥/𰝲 (not explicitly framed as alternative forms), while zh.Wiktionary's own 異體字 box instead lists a different unrelated pair, 羏 and 鴹 — since the two sources disagree rather than agree, no alias was added, matching the same reasoning used to exclude candidates on 罹/纂/羸's alias lists in prior iterations.

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks floating with no bullet structure at all — no graphemic bullet, no SKIP/Stroke bullet, no MC-rank bullet, no levels bullet) to the standard format. No Derived Characters (nothing names 翔 as its own `graphemic_classification`); no Chengyu hits. Grepped all `words/*.md` citing 翔 in prose ([[飛]], [[飛行]]) — both confirmed false positives, neither lists 翔 in its own `characters:` field. Only the existing stand-in [[飛翔]] cites 翔 as a constituent.

**Citing word page [[飛翔]] (stand-in) reviewed, no bugs found**: `pos: 動詞` already filled with no duplicate `品詞` field; its `羅馬字`/`諺文`/`注音` (`feisyang`/`뻬샹`/`ㄈㄝㄧㄙ⼘ㄫ`) are already in sync with both constituent characters' own syllables ([[characters/飛 (char)|飛]]'s already-perfected `fei`/`뻬`/`ㄈㄝㄧ` and 翔's own `syang`/`샹`/`ㄙ⼘ㄫ`); blank `vietnamese` is a genuine gap, correctly omitted rather than a `null` placeholder — hvdic has no dedicated entry for the compound 飛翔 itself, only for the individual characters, same reasoning as [[characters/羸|羸]]'s and [[characters/罹|罹]]'s citing word pages in prior iterations.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 聘 (char) (7300; 940 characters remaining).

### 2026-08-14, iteration 1565 — [[characters/聘 (char)|聘]]

**`mc_id: 1171` confirmed correct** — clean rank, no off-by-one this time: `CC 1000.md` line 179-181 reads "1170. 否" / "1171. 聘" / "1172. 竭" in direct sequence. **`graphemic_classification: 甹` confirmed correct** (形声, semantic 耳 + phonetic 甹): en.Wiktionary's glyph origin gives 聘 as ⿰耳甹, and zh.Wiktionary independently corroborates via its quoted Shuowen entry ("訪也。从耳甹聲"). Both sources' Zhengzhang reconstruction for the whole character agree exactly (\*pʰleŋs), and both give 甹's own OC as \*pʰleːŋ — embedded in the rebuilt graphemic bullet along with a semantic-motivation note (訪 "to inquire/visit" conducted by ear).

**Major `vietnamese` bug fixed**: hvdic's actual entry for 聘 lists "Âm Hán Việt: sính" as the sole genuine Sino-Vietnamese reading, and separately files `sánh` under "Âm Nôm" (Nôm-only, an unrelated word meaning "to compare") — the stored `sánh` was exactly the Nôm-only contamination trap the checklist warned about, matching the pattern found on 稍/牢/瘋/糊/繞/纂/罹/羸. Trimmed `vietnamese` down to `sính` only.

`japanese: HEI` confirmed correct as the sole corroborated on-yomi (en.Wiktionary additionally lists a go-on ひょう, but Jisho shows only ヘイ, so ひょう was excluded per this session's established both-sources policy, matching 罹's excluded RA, 羸's excluded REN). **`japanese_native` bug fixed**: the stored bare unhyphenated `と` was both truncated and in the wrong frontmatter shape (a single string rather than a list) — corrected to a proper two-item list, `と-う` ("to ask, inquire, invite") and `め-す` ("to summon"), both corroborated by both en.Wiktionary and Jisho; a third candidate, へい.する (an on-yomi-plus-suru form rather than a true native kun), was excluded from both sources' listings as not a genuine kun-yomi.

`korean_native: 부를` and `middle_chinese_initial/final: pʰ`/`iᴇŋ` reconfirmed correct against `聲 滂`/`韻 清開` (both lookup pages already cited 聘 correctly — the former's own page independently documents 聘 among 49 of 50 regular ㄆ outcomes in the 滂 series, escaping the single ㄈ exception 頗; the latter among the 35-member ㄧㄫ majority of its three-way split). `korean: 빙` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `lookup/Korean/Korean HS.md`'s line 321 already lists 聘 correctly ("찾아갈 빙"). **Blank `joyo_level` filled**: `表外字` (real corroborated on'yomi/kun'yomi per both sources, with no jōyō or jinmeiyō status found on Jisho or in web search) — **missing-entry bug fixed accordingly**, adding 聘 to `lookup/Japanese/Hyōgai.md` as entry #308 (absent despite having real readings). Blank `pos` filled: `事詞` (a transitive Eventive per 文法 - 97品詞's definition — "to engage/betroth" takes an object), matching the pattern used on similar action-meaning characters this session (繞/纂/罹/翔 → 事詞). `Lookup/Radicals/Radical 128.md` (耳), `SKIP-1-6-7`, `Stroke 13`, and `syllables/ㄆㄧㄫ.md` all already cited 聘 correctly before this iteration.

**`aliases: 娉` confirmed correct after careful cross-check**: en.Wiktionary explicitly lists 娉 as an "alternate form" of 聘, and zh.Wiktionary's own entry for 聘 independently corroborates the same equivalence for the specific betrothal sense ("女子訂婚或出嫁。同娉"). Unlike the disagreement pattern that excluded candidates on 罹/纂/羸's alias lists, both sources here agree a genuine variant relationship exists — so the alias was kept, despite 娉 also carrying its own unrelated primary meaning ("graceful, beautiful," as in 娉婷) under a different reading (pīng) per en.Wiktionary, which doesn't disqualify its secondary use as 聘's variant. No character page for 娉 exists in the vault, so no conflict with an independent entry.

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks floating with no bullet structure at all — no graphemic bullet, no SKIP/Stroke bullet, no MC-rank bullet, no levels bullet) to the standard format, adding the missing `## Words` section. No Derived Characters (nothing names 聘 as its own `graphemic_classification`); no Chengyu hits. Only `words/聘.md` (the character's own self stand-in) cites 聘 as a constituent.

**Citing word page [[聘]] (self stand-in) had two gaps fixed**: literal `vietnamese: null` placeholder → `sính` (matching the character's own corrected reading); missing `pos` field entirely → added `事詞`. Its `注音`/`羅馬字`/`諺文` (`ㄆㄧㄫ`/`ping`/`핑`) were already in sync with the character page's own syllable.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 聾 (7301; 939 characters remaining).

### 2026-08-14, iteration 1566 — [[characters/聾|聾]]

**`mc_id: 2086` confirmed correct** — clean rank, no off-by-one this time: `CC 2000.md` line 91 reads "2086. 聾" directly, with "2085. 羈" and "2087. 齋" immediately adjacent. **`graphemic_classification: 龍` confirmed correct** (形聲, semantic 耳 + phonetic 龍): en.Wiktionary gives 聾 as ⿰耳龍, and zh.Wiktionary independently corroborates ("聲符 龍 + 意符 耳"). Both sources' Zhengzhang reconstruction for the whole character agree (\*roːŋ), and both give 龍's own OC as \*b·roŋ/\*mroːŋ — embedded in the rebuilt graphemic bullet alongside a semantic-motivation note (deafness as a condition of the ear).

**Major `vietnamese` bug fixed**: hvdic's actual entry for 聾 lists "Âm Hán Việt: lung" as the sole genuine Sino-Vietnamese reading, and separately files `tủng` under "Âm Nôm" (Nôm-only) — the stored `tủng` was exactly the contamination trap flagged going in, the same reading that had turned up as a genuine Hán Việt hit on the unrelated [[characters/竦 (char)|竦]] a few iterations ago; here on 聾 it's a copy-paste artifact, not this character's own reading. Corrected `vietnamese` to `lung`.

`japanese: ROU` confirmed correct as the sole corroborated on-yomi (en.Wiktionary and ja.Wiktionary both additionally list a go-on る/ル, but Jisho shows only ロウ, so る was excluded per this session's established both-sources policy, matching 聘's excluded ひょう). **`japanese_native` gap filled**: bare unhyphenated single-string `つんぼ` was missing a second corroborated kun-yomi and stored in the wrong frontmatter shape — corrected to a proper two-item list, `つんぼ` ("deaf person/deafness") and `みみしい` ("hard of hearing"), both confirmed via both en.Wiktionary and ja.Wiktionary; neither carries okurigana hyphenation in either source (unlike verb-form kun'yomi seen on prior iterations), confirmed rather than assumed, since both are nominal/adjectival glosses rather than inflecting verb stems.

`korean_native: 귀먹을` reconfirmed correct (also documented as 귀머거리 롱 in Korean sources, but 귀먹을 is an equally genuine, attested 훈) and `middle_chinese_initial/final: l`/`uŋ` reconfirmed correct against `聲 來`/`韻 東一` (both lookup pages already cited 聾 correctly — the former's own page independently documents 聾 among all 214 characters landing on the single regular ㄌ outcome, the latter among the 45-member ㄛㄫ majority of its two-way split, the lone exception being the unrelated cranberry override 檬). `korean: 롱` reconfirmed correct (genuine North Korean/문화어 form — South Korean 두음법칙 would shift a word-initial ㄹ to 농, so 롱 here confirms the North Korean convention, matching the pattern documented for [[characters/竦 (char)|竦]]'s `kwin` memory note); `Lookup/Korean/Korean Name ㄹ.md`'s `### 롱` subsection already lists 聾 correctly, and `kwin: true` is consistent (諺文 롱 matches korean 롱 exactly). `joyo_level: 表外字` confirmed correct; `lookup/Japanese/Hyōgai.md` already cites 聾 (#221). `pos: 性詞` confirmed appropriate (a stative quality — "deaf" — per 文法 - 97品詞, matching the pattern used on similarly stative characters like 羸→性詞).

**Two new variant aliases added**: 䏊 and 𰭹, cross-referenced between en.Wiktionary's and zh.Wiktionary's independent variant-form lists — both sources agree on exactly these two candidates, and neither holds its own vault page, so no conflict with an independent entry; existing alias 聋 (simplified) reconfirmed correct via both sources.

Rebuilt malformed `## Notes` (two bare unlinked CC-lookup wikilinks floating with no bullet structure at all — no graphemic bullet, no SKIP/Stroke bullet, no MC-rank bullet, no levels bullet) to the standard format. No Derived Characters (nothing names 聾 as its own `graphemic_classification`); no Chengyu hits (no `chengyu/*.md` cites 聾 in its `characters:` field). Only the existing stand-in [[耳聾]] cites 聾 as a constituent.

**Citing word page [[耳聾]] (stand-in) reviewed, no bugs found**: `pos: 性詞` already filled with no duplicate `品詞` field; blank `vietnamese` is correctly *omitted* rather than a bug — a direct hvdic lookup for 耳聾 returned no attested compound, so this is a genuine gap, not a placeholder to fix, same reasoning as [[characters/羸|羸]]'s and [[characters/飛翔|飛翔]]'s citing word pages in prior iterations. Its `注音`/`羅馬字`/`諺文` (`ㄋㄧㄌㄛㄫ`/`nilong`/`니롱`) are already in sync with both constituent characters' own syllables ([[characters/耳 (char)|耳]]'s already-perfected `ni`/`니`/`ㄋㄧ` and 聾's own unchanged `long`/`롱`/`ㄌㄛㄫ`).

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 肴 (char) (7302; 938 characters remaining).

### 2026-08-14, iteration 1567 — [[characters/肴 (char)|肴]]

**`mc_id` off-by-one bug fixed** (3244 → 3245; confirmed against `CC 3000.md` line 257-258, where "3244. 熬" precedes "3245. 肴" — the same one-line-off transcription pattern seen repeatedly this session). **`graphemic_classification: 爻` confirmed correct** (形聲, semantic 肉 + phonetic 爻): en.Wiktionary gives 肴 as ⺼(肉)+爻, and its own phonetic-series listing for 爻 independently corroborates (肴, 教/敎, 淆 all sharing the series). Notably both the whole character and its phonetic component 爻 land on the *identical* Zhengzhang OC reconstruction (\*ɢraːw) — an unusually clean, undisturbed phonetic borrowing, folded into the rebuilt graphemic bullet alongside both systems' values (Zhengzhang \*ɢraːw for both; Baxter–Sagart \*[ɡ]ˤraw for 肴, \*N-kˤraw for 爻).

`vietnamese: hào` confirmed correct via hvdic — notably hvdic lists `hào` under *both* its Âm Hán Việt and Âm Nôm sections rather than flagging a separate contaminating Nôm form, so no correction was needed (same as 翔's `tường` a few iterations ago, unlike the severe contamination found on 繞/纂/羸/聾). `japanese: KOU` confirmed correct as the sole corroborated on-yomi (en.Wiktionary additionally lists a go-on ぎょう, but Jisho shows only コウ, so ぎょう was excluded per this session's established both-sources policy, matching 聾's excluded る). `japanese_native: さかな` confirmed correct (both sources agree; en.Wiktionary's extra な wasn't corroborated by Jisho and was left out) — confirmed as a nominal gloss requiring no okurigana hyphenation, rather than assumed.

**`korean_native` gap filled**: blank → `안주` ("side dish/accompaniment for alcohol"), the standard 訓 given for 肴 across Korean hanja dictionaries (wordrow.kr, hanja.nameunse.com, zetawiki: "안주 효"), matching the vault's established bare-noun convention for nominal concepts (e.g. 飯→밥, 額→이마). `middle_chinese_initial/final: ɣ`/`ɣau` reconfirmed correct against `聲 匣`/`韻 肴` (both lookup pages already cited 肴 correctly), plus `SKIP-2-2-6`/`Stroke 08`, already cited 肴 correctly. `korean: 효` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㅎ.md`'s `### 효` subsection already lists 肴 correctly. `joyo_level: 日本人名用漢字` confirmed a legitimate convention value; `lookup/Japanese/Jinmeiyō.md` already cites 肴 (#324). Blank `pos` filled: `名詞` (a concrete nominal concept — "cooked meat, meat dish").

**No alias added**: en.Wiktionary and zh.Wiktionary both agree the sole variant is the already-stored `餚` (en.Wiktionary calls 肴 "the simplified and variant traditional form of 餚"; zh.Wiktionary explicitly lists 餚 as 肴's 傳統字/異體字); zh.Wiktionary's separate phonetic-series listing (倄/崤/淆/誵/郩/殽) represents derived characters sharing the 爻 phonetic, not variants of 肴 itself, and none of them names 肴 as its own `graphemic_classification` in the vault (confirmed via grep), so no `## Derived Characters` section applies.

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks floating with no bullet structure at all — no graphemic bullet, no SKIP/Stroke bullet, no MC-rank bullet, no levels bullet), adding the missing `## Words` section for the self stand-in. No Chengyu hits; two `words/*.md` grep hits ([[孝]], [[小学校]]) both confirmed false positives — 孝's mention is its own homophone callout, and 小学校's is a `韻 肴` phonology citation in prose, neither citing 肴 in a `characters:` field. Only the existing self stand-in cites 肴.

**Citing word page [[肴]] (self stand-in) had one gap fixed**: missing `pos` field entirely → added `名詞`. `vietnamese: hào` (not a `null` placeholder) and `注音`/`羅馬字`/`諺文` (`ㄏ⼘ㄨ`/`hyau`/`햣`) were already correct and in sync with the character page's own syllable, which was unchanged by this iteration's `mc_id` fix.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 膠 (7303; 937 characters remaining).

### 2026-08-14, iteration 1568 — [[characters/膠|膠]]

**`mc_id: 1370` confirmed correct** — clean rank, no off-by-one this time: `CC 1000.md` line 1370 reads "1370. 膠" directly, flanked by "1369. 筋" and "1371. 豆." **`graphemic_classification: 翏` confirmed correct** (形声, semantic 肉/⺼ + phonetic 翏), agreed by both en.Wiktionary and zh.Wiktionary, with en.Wiktionary's own 翏-phonetic series listing independently corroborating (膠 alongside 謬/戮/廖/繆). Unlike [[characters/肴 (char)|肴]]/爻's identical OC match last iteration, 膠's whole-character reconstruction (\*krɯːw, Zhengzhang; \*[k]ˤriw, Baxter–Sagart) diverges from 翏 alone (\*ɡ·rɯːw, Zhengzhang; \*[r]iw-s, Baxter–Sagart) in initial voicing — a less clean phonetic borrowing, noted in the rebuilt graphemic bullet.

**Major `vietnamese` bug fixed**: hvdic's actual entry for 膠 lists "Âm Hán Việt: giao" as the sole genuine Sino-Vietnamese reading, and separately files `keo` under "Âm Nôm" (Nôm-only, the everyday native word for "glue") — the stored `keo` was exactly the contamination trap the checklist warned about going in, the same pattern found repeatedly this session (聘/繞/纂/罹/羸/聾). Trimmed `vietnamese` down to `giao` only.

**`japanese` gap filled**: both ja.Wiktionary and Jisho agree on two on-yomi, コウ (kan-on) and キョウ (go-on) — the stored `[KOU]` was missing the corroborated `KYOU`, added. **`japanese_native` gap filled**: both sources also agree on two kun-yomi, にかわ ("animal glue") and にべ ("fish glue") — the stored bare `にかわ` was missing the corroborated `にべ`; converted to a proper list. Neither needs okurigana hyphenation, both being bare nominal glosses rather than verb stems.

**`korean_native` bug fixed**: stored `아교` is a genuine Sino-Korean loanword (阿膠-derived) but only the *secondary* listed 훈음 for 膠 — Korean hanja dictionaries (wordrow.kr) give 膠's full 훈음 set as "갖풀 교, 화할 교, 아교 교, 어긋날 호," with 갖풀 (a native 순우리말 word for hide/animal glue) as the primary traditional gloss, matching the vault's established native-gloss convention better than the Sino-Korean secondary reading. Corrected to `갖풀`. `middle_chinese_initial/final: k`/`ɣau` reconfirmed correct against `聲 見`/`韻 肴` (both lookup pages already cited 膠 correctly — the former's own page independently documents 膠 among 284 of 301 regular ㄍ outcomes in the 見 series' most lopsided split yet, the latter among the 10-member ⼄ㄨ plain-k subgroup of its own initial-conditioned split), plus `SKIP-1-4-11`/`Stroke 15`, already cited 膠 correctly. `korean: 교` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㄱ.md`'s `### 교` subsection already lists 膠 correctly. `joyo_level: 表外字` confirmed correct; `lookup/Japanese/Hyōgai.md` already cites 膠 (#120). Blank `pos` filled: `名詞` (a concrete nominal concept — "glue"), matching [[characters/肴 (char)|肴]]'s own identical `名詞` classification for the same 肉-radical "concrete substance" pattern.

**No alias added**: both en.Wiktionary and zh.Wiktionary agree the only variant form is the already-stored simplified 胶 — no other candidates on either side.

Rebuilt malformed `## Notes` (two bare unlinked CC-lookup wikilinks floating with no bullet structure at all — no graphemic bullet, no SKIP/Stroke bullet, no MC-rank bullet, no levels bullet) to the standard format. No Derived Characters (nothing names 膠 as its own `graphemic_classification`); no Chengyu hits (no `chengyu/*.md` cites 膠 in its `characters:` field). **`## Words` gap filled**: grepped all `words/*.md` citing 膠 in their `characters:` field and found [[塑膠]] ("plastic," already independently perfected 2026-08-04) missing from the list alongside the existing stand-in [[膠水]] — added.

**Citing word page [[膠水]] (stand-in) reviewed, no bugs found**: `pos: 名詞` already filled with no duplicate `品詞` field; its `注音`/`羅馬字`/`諺文` (`ㄍ⼄ㄨㄙㄨ`/`gyousu`/`굣수`) already in sync with the character page's own unchanged syllable; blank `vietnamese` (field entirely absent, not a `null` placeholder) is a genuine gap, correctly omitted per the established pattern (no dedicated hvdic entry for the compound 膠水 itself).

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 舵 (char) (7304; 936 characters remaining).

### 2026-08-14, iteration 1569 — [[characters/舵 (char)|舵]]

**`mc_id: 0` confirmed plausible**: grepped `CC 0000.md` through `CC 3000.md` in full and found no occurrence of 舵 anywhere — genuinely absent from the Classical Chinese usage ranking, consistent with a technical/nautical term staying rare in classical prose. Left as-is, phrased per the checklist's `mc_id: 0` convention, matching [[characters/砧|砧]]'s established wording pattern from an earlier iteration.

**Major `graphemic_classification` bug fixed** (`蛇` → `它`): both en.Wiktionary and zh.Wiktionary independently and explicitly analyze 舵 as 形声 semantic [[Radical 137|舟]] ("boat") + phonetic **它**, not 蛇 — zh.Wiktionary places 舵 in its own 它-phonetic "谐声系列" (#1806) alongside 陀/駝/駄, all of which already read ㄉㄚ on their own character pages, exactly mirroring 舵's own ㄉㄚ; 蛇 itself is merely a *sibling* in that same 它-phonetic family, not 舵's own directly-cited component — a textbook case of the checklist's "component of a component" trap. Corrected the field and rebuilt the graphemic bullet with both sources' Zhengzhang OC values (whole character \*l'aːlʔ, phonetic 它 alone \*l̥ʰaːl), noting the guessability chain against 陀/駝/駄.

`vietnamese: đà` confirmed correct and genuine Hán Việt via hvdic — notably hvdic lists `đà` under *both* its Âm Hán Việt and Âm Nôm sections rather than flagging a separate contaminating Nôm form, so no correction was needed (same pattern as 翔/肴's `tường`/`hào`, unlike the severe contamination found on 繞/纂/羸/聾/膠). `japanese: [TA, DA]` and `japanese_native: かじ` both fully corroborated by cross-referencing ja.Wiktionary (呉音 ダ, 漢音 タ, kun かじ) against Jisho (ダ/タ on'yomi, かじ kun'yomi) — no uncorroborated extras found on either side this time, and かじ correctly left as a bare nominal gloss with no okurigana hyphenation needed, matching [[characters/肴 (char)|肴]]'s さかな pattern.

`korean_native: 키` reconfirmed correct (the everyday native Korean word for "rudder," matching the word page's own note that Korean keeps a native term for this concept) and `middle_chinese_initial: d`/`middle_chinese_final: a` reconfirmed correct in substance against `聲 定`/`韻 歌` — but **a formatting bug was found and fixed on `middle_chinese_final`**: stored as bare Latin `a` rather than the vault's actual IPA convention `ɑ` (open-back unrounded) used consistently by every sibling on the same 它-phonetic family — [[characters/陀|陀]], [[characters/駝|駝]], [[characters/駄 (char)|駄]], and [[characters/可 (char)|可]] all store `"ɑ"`. Corrected to match. `聲 定.md` already cited 舵 correctly among its ㄉ-outcome majority. **`韻 歌.md` missing-entry bug fixed**: 舵 was entirely absent from the page's ㄚ-outcome list despite belonging there (`size: 37` → `38`, prose count updated 30/37 → 31/38, 舵 added to the ㄚ bullet). `korean: 타` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㅌ.md`'s `### 타` subsection already lists 舵 correctly. `joyo_level: 日本人名用漢字` confirmed a legitimate convention value; `lookup/Japanese/Jinmeiyō.md` already cites 舵 (#328). `pos: 名詞` confirmed appropriate (a concrete nominal concept, "rudder, helm").

**Two new variant aliases added, one existing alias reconfirmed**: en.Wiktionary's alternative-forms list (柁, 柂, 杝, 舦, 艜, 𰰏) and zh.Wiktionary's 異體字 box (柁, 柂, 䑨, 杕) overlap exactly on **柁** and **柂** — added both, neither holding an independent vault character page. The existing `杕` alias was carefully re-verified rather than assumed: both sources give 杕 *two* separate etymologies — an independent meaning ("a tree standing alone," per both en. and zh.Wiktionary) *and* a second, explicitly labeled variant-of-舵 etymology ("此字是「舵」的異體字") — so the alias is genuine for that second sense despite 杕 also being an unrelated independent character under its first sense, the same dual-meaning-alias pattern established on [[characters/聘 (char)|聘]]'s 娉.

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks floating with no bullet structure at all — no graphemic bullet, no SKIP/Stroke bullet, no MC-rank bullet, no levels bullet), adding the missing `## Words` section for the self stand-in (`stand_in: 舵`). No Derived Characters (nothing names 舵 as its own `graphemic_classification`); no Chengyu hits. Grepped all `words/*.md` citing 舵 in their `characters:` field and found only the existing self stand-in [[舵]] itself; a homophone mention of 舵 in [[駄]]'s prose (its own `## Notes` homophone callout) was confirmed a false positive, not a `characters:` citation.

**Citing word page [[舵]] (self stand-in) reviewed, no bugs found**: `pos: 名詞` already filled with no duplicate `品詞` field; `vietnamese: lái` is a real value, not a `null` placeholder; `注音`/`羅馬字`/`諺文` (`ㄉㄚ`/`da`/`다`) already in sync with the character page's own unchanged syllable (the `mc_final` IPA-formatting fix above did not change the syllable itself).

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 葺 (char) (7305; 935 characters remaining).

### 2026-08-14, iteration 1570 — [[characters/葺 (char)|葺]]

`mc_id: 5288` confirmed as legitimate long-tail data (葺 not found anywhere in `CC 0000`–`CC 3000.md`, consistent with the checklist's policy of trusting an existing above-4000 rank verbatim rather than blanking it). **`graphemic_classification: 咠` confirmed correct** (形聲, semantic [[Radical 140|艸]] + phonetic 咠), via en.Wiktionary (Zhengzhang OC whole character \*ʔsib/\*sʰib/\*zib, phonetic 咠 alone \*ʔsib/\*sʰib) and independently corroborated by zh.Wiktionary's own 系列#1452（咠）phonetic-family grouping.

**Major `korean_native` bug fixed**: the stored `기울` is an unrelated Korean word ("bran"), with no connection to 葺's actual meaning — a Korean-language web search confirms the character's real 訓 (gloss) is "지붕 이을" ("to roof/thatch"), i.e. the attributive form of 이다/잇다 ("to thatch a roof") — corrected to `이을`, matching this vault's established convention of storing a bare attributive verb stem (e.g. [[characters/竄|竄]]'s `숨을`, [[characters/稟|稟]]'s `여쭐`).

**`japanese_native` gap filled**: the stored `あし` was genuine but incomplete — both ja.Wiktionary and Jisho independently corroborate two further kun'yomi, `ふ-く` (verb, "to thatch," properly hyphenated) and `ふき` (its noun form) — added both alongside the existing `あし`, converting the field to a proper list. `japanese: SHUU` confirmed correct (both sources agree, go-on/kan-on identical, シフ historical spelling aside). `vietnamese: tập` confirmed correct via hvdic — notably listed under *both* Âm Hán Việt and Âm Nôm categories rather than flagging a contaminating separate Nôm form, the same "no correction needed" pattern seen on [[characters/舵 (char)|舵]]/[[characters/翔|翔]]/[[characters/肴 (char)|肴]]'s own readings, unlike the severe contamination found on [[characters/繞 (char)|繞]]/[[characters/羸|羸]].

`korean: 즙` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㅈ.md`'s `### 즙` subsection already lists 葺 correctly. `middle_chinese_initial/final: t͡sʰ`/`iɪp` reconfirmed correct against `聲 清`/`韻 緝A三` (both lookup pages, plus `SKIP-2-3-9`/`Stroke 12`/`Jinmeiyō`/`Radical 140`, already cited 葺 correctly). **Blank `hsk_level` bug fixed**: no `lookup/HSK/*.md` file cites 葺 anywhere — filled `無`. Blank `pos` filled: `事詞` (a transitive verb — "to roof/thatch [something]" — per 文法 - 97品詞's Eventive definition), matching the pattern used on similar action-meaning characters this session.

**No alias added**: en.Wiktionary's alternative-forms list (𦱫, 𦲭) was not corroborated by zh.Wiktionary, which lists no 異體字 for 葺 at all — left as a genuine gap per the "only add if both sources agree" policy, same reasoning as [[characters/羸|羸]]'s and [[characters/纂|纂]]'s excluded candidates.

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks floating with no bullet structure at all — no graphemic bullet, no SKIP/Stroke bullet, no MC-rank bullet, no levels bullet) to the standard format, adding the missing `## Words` section for the self stand-in (`stand_in: 葺`). No Derived Characters (nothing names 葺 as its own `graphemic_classification`); no Chengyu hits. Only the existing self stand-in [[葺]] cites 葺 as a constituent.

**Citing word page [[葺]] (self stand-in) had two gaps fixed**: literal `vietnamese: null` placeholder → `tập`; `pos` field was missing entirely (not just blank) → added `事詞`.

Stamped `date-last-perfect: 2026-08-14`.

(Session note: this iteration was done directly in the main conversation at the user's request, rather than delegated to a background subagent — the previous iteration's background agent had hit a session-limit error mid-run and was stopped; a fresh async agent launched for this character was then also stopped mid-flight so the work could be done visibly instead.)

Next never-perfected character by `danayo_id`: 蠢 (7306; 934 characters remaining).

### 2026-08-14, iteration 1571 — [[characters/蠢|蠢]]

**`mc_id` off-by-one bug fixed** (3413 → 3414; confirmed against `CC 3000.md` line 435, where "3413. 惇" precedes "3414. 蠢"). **`graphemic_classification: 春` confirmed correct** (形声, semantic 䖵 "insects" + phonetic 春), via en.Wiktionary (whole-character Zhengzhang OC \*tʰjunʔ), independently corroborated by zh.Wiktionary's own 系列#0260（春）phonetic-family grouping. **New variant alias added**: 惷, confirmed genuine via both en.Wiktionary's alternative-forms list and zh.Wiktionary's explicit 異體字 box.

**Major `vietnamese` contamination fixed**: the stored three-entry list (xoáy, xoẳn, xuẩn) was mostly spurious — hvdic's actual entry for 蠢 lists exactly one genuine Âm Hán Việt reading, `xuẩn`, with `xoáy` and `xoẳn` filed only under the separate Âm Nôm (Nôm-only) section; trimmed to `xuẩn` alone, independently corroborated by the citing word [[蠢動]]'s own already-correct `vietnamese: xuẩn động`.

**`japanese_native` bug fixed**: the stored bare `うご` was a truncated, non-existent reading (not うごく "to move," a different kanji's word, and not a complete word on its own) — both ja.Wiktionary and Jisho independently confirm the actual sole kun-yomi is `うご-めく` ("to squirm/wriggle"), properly hyphenated; corrected. `japanese: SHUN` confirmed correct (both sources agree, go-on/kan-on identical). **Blank `joyo_level` filled**: `表外字` (real on'yomi/kun'yomi usage, confirmed absent from every Japanese level list in the vault) — **missing-entry bug fixed accordingly**, adding 蠢 to `lookup/Japanese/Hyōgai.md` as entry #309.

`korean_native: 꿈틀거릴` ("to squirm/wriggle") reconfirmed correct as a good semantic match; `korean: 준` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㅈ.md`'s `### 준` subsection already lists 蠢 correctly. `middle_chinese_initial/final: t͡ɕʰ`/`iuɪn` reconfirmed correct against `聲 昌`/`韻 諄` (both lookup pages, plus `SKIP-2-9-12`/`Stroke 21`/`Old HSK 3`, already cited 蠢 correctly); `syllables/ㄑㄨㄋ.md` also already correctly listed 蠢 among its three characters. Blank `pos` filled: `事詞` (a transitive/intransitive Eventive verb — "to squirm, wiggle"), matching the citing word page's own already-correct `事詞` classification.

Rebuilt the malformed body (`## Words` section misplaced before `# Notes`; wrong heading level; two bare unlinked CC-lookup wikilinks with no other bullets) to the standard format. No Derived Characters (nothing names 蠢 as its own `graphemic_classification`); no Chengyu hits. Only the existing stand-in [[蠢動]] cites 蠢 as a constituent.

**Citing word page [[蠢動]] (stand-in) had one bug fixed**: a redundant duplicate `品詞` field (identical value to `pos`), the same recurring pattern seen repeatedly this session.

Stamped `date-last-perfect: 2026-08-14`.

(Session note: this iteration was again done directly in the main conversation, per the user's standing request to see every step live rather than delegate to a background subagent.)

Next never-perfected character by `danayo_id`: 袂 (char) (7307; 933 characters remaining).

### 2026-08-14, iteration 1572 — [[characters/袂 (char)|袂]]

**`mc_id` off-by-one bug fixed** (3066 → 3067; confirmed against `CC 3000.md` line 71-72, where "3066. 絺" precedes "3067. 袂"). **`graphemic_classification: 夬` confirmed correct** (形聲, semantic 衤/衣 + phonetic 夬), via en.Wiktionary (whole-character Zhengzhang OC \*mɡʷeds, phonetic 夬 alone \*kʷraːds), independently corroborated by zh.Wiktionary's own composition breakdown (⿰衤夬).

**Alias bug fixed**: the stored `𣍐` is not a genuine variant of 袂-the-sleeve at all — both en.Wiktionary and zh.Wiktionary explicitly tie 𣍐 (and its sibling 𫧃) to a completely unrelated *second etymology*, a Hokkien (泉漳話) grammatical negation particle that merely happens to share the character form; zh.Wiktionary's own entry explicitly separates this from the standard "sleeve" sense, with no variant listed for the sleeve meaning itself. Removed, left as a genuine gap.

**Major `vietnamese` contamination fixed**: the stored `[khuyết, quyết]` were both filed by hvdic exclusively under Âm Nôm (Nôm-only) — hvdic's actual Âm Hán Việt entry for 袂 gives a completely different pair, `duệ` and `mệ` (the latter phonologically regular, matching the character's own m- Middle Chinese initial and the m-initial forms seen across Mandarin/Cantonese/Korean). Replaced accordingly.

**`japanese` field investigated and reconfirmed correct despite source disagreement**: ja.Wiktionary and Jisho disagreed sharply (ja.Wiktionary: go-on マイ/kan-on ベイ/kan'yō-on ヘイ, no ケツ; Jisho: ベイ・ケツ only, no マイ/ヘイ) — rather than trimming to the single overlapping reading per the usual "corroborated by both" rule, a third tiebreaker source (Kanjipedia, via web search) confirmed **all four** readings are genuinely attested (マイ・ベイ・ヘイ・ケツ), so the existing stored `[BEI, KETSU]` was left unchanged as a valid (if partial) subset rather than incorrectly trimmed. **`japanese_native` gap filled**: both ja.Wiktionary and Jisho agree on two kun-yomi, `たまと` and `たもと` — the stored bare `たまと` was genuine but incomplete; added `たもと`, converting the field to a proper list.

`korean_native: 소매` ("sleeve") and `korean: 몌` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㅁ.md`'s `### 몌` subsection already lists 袂 correctly. `middle_chinese_initial/final: m`/`iᴇi` reconfirmed correct against `聲 明`/`韻 祭A三開` (both lookup pages, plus `SKIP-1-5-4`/`Stroke 09`/`Hyōgai`/`HSK No`, already cited 袂 correctly — also surfacing and fixing the wrong Kangxi radical number baked into the pre-existing corrupted Notes prose, which had linked 衤 to `Radical 120` (actually 糸) instead of the correct `Radical 145` (衣), cross-checked against [[characters/被 (char)|被]]'s own already-correct citation). Blank `pos` filled: `名詞` (a concrete noun — "sleeve").

Rebuilt severely malformed `## Notes` (an unclosed wikilink `[[夬`, a bare fragment `- Korean Name ㅋ, ` with no link and the wrong Hangul consonant entirely, wrong Radical number, two bare unlinked CC-lookup wikilinks with no other bullets, no `## Words` section) to the standard format, adding the missing self stand-in citation (`stand_in: 袂`). No Derived Characters (nothing names 袂 as its own `graphemic_classification`); no Chengyu hits. Only the existing self stand-in [[袂]] cites 袂.

**Citing word page [[袂]] (self stand-in) had two gaps fixed**: literal `vietnamese: null` placeholder → `duệ` (the first-listed/primary Hán Việt reading, matching the established convention of picking one value for the word page from a multi-entry character field); missing `pos` field entirely → added `名詞`.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 袴 (char) (7308; 932 characters remaining).

### 2026-08-14, iteration 1573 — [[characters/袴 (char)|袴]]

`mc_id: 4149` confirmed as legitimate long-tail data (袴 not found anywhere in `CC 0000`–`CC 3000.md`, consistent with the checklist's policy of trusting an existing above-4000 rank verbatim). **`graphemic_classification: 夸` confirmed correct**: en.Wiktionary directly analyzes 袴 as 形聲 (semantic 衤 + phonetic 夸, Zhengzhang OC \*kʰʷaːs for the whole character), while zh.Wiktionary instead frames 袴 as a variant of a separate but closely related character, [[絝]] (itself 形聲 semantic 糸 + phonetic 夸) — the two framings don't actually conflict on the essential point, since both agree the phonetic component is 夸 either way; folded the zh.Wiktionary framing into the graphemic bullet as a cross-reference. **New variant alias added**: 褲 (the modern traditional-Chinese standard form for "pants"), confirmed genuine via both en.Wiktionary's alternative-forms note and zh.Wiktionary's explicit 異體字 box.

`vietnamese: khố` confirmed correct via hvdic (listed under both Âm Hán Việt and Âm Nôm, the same "no correction needed" pattern seen on [[characters/舵 (char)|舵]]/[[characters/袂 (char)|袂]]'s own readings). **`japanese` and `japanese_native` gaps filled**: both ja.Wiktionary and Jisho fully agree on two on-yomi (コ go-on, ク kan-on) and two kun-yomi (ずぼん, はかま) — the stored fields had only `[KO]` and bare `ずぼん`, missing the corroborated `KU` and `はかま`; both expanded to complete lists.

`korean_native: 바지` ("pants") and `korean: 고` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㄱ.md`'s `### 고` subsection already lists 袴 correctly. `middle_chinese_initial/final: kʰ`/`uo` reconfirmed correct against `聲 溪`/`韻 模` (both lookup pages, plus `SKIP-1-5-6`/`Stroke 11`/`Jinmeiyō`, already cited 袴 correctly). **Blank `hsk_level` bug fixed**: no `lookup/HSK/*.md` file cites 袴 anywhere — filled `無`. Blank `pos` filled: `名詞` (a concrete noun — "pants, trousers").

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets, no `## Words` section) to the standard format, adding the missing self stand-in citation (`stand_in: 袴`). No Derived Characters (nothing names 袴 as its own `graphemic_classification`); no Chengyu hits. Only the existing self stand-in [[袴]] cites 袴.

**Citing word page [[袴]] (self stand-in) had two gaps fixed**: literal `vietnamese: null` placeholder → `khố`; missing `pos` field entirely → added `名詞`.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 訣 (7309; 931 characters remaining).

### 2026-08-14, iteration 1574 — [[characters/訣|訣]]

**`mc_id` off-by-one bug fixed** (3938 → 3939; confirmed against `CC 3000.md` line 979-980, where "3938. 燃" precedes "3939. 訣"). **Major `graphemic_classification` bug fixed** (`叏` → `夬`): both en.Wiktionary and zh.Wiktionary confirm 訣 is 形聲 with semantic 言 + phonetic **夬** (Zhengzhang OC whole-character \*kʷeːd, phonetic 夬 alone \*kʷraːds) — the stored `叏` is a distinct, unrelated character (U+53CF, visually similar to 夬 but not it), evidently a transcription slip somewhere upstream, corrected. **Alias judgment call, no change made**: zh.Wiktionary's own 異體字 box lists 決/决 alongside the existing 诀, but 決 is already a full, independent, high-frequency vault character with its own well-established distinct meaning ("to decide; to breach [a dam]") — the same reasoning that excluded 離 from [[characters/罹|罹]]'s alias list despite a historical-interchange note applies here; left unadded rather than risk corrupting 決's independent status.

`vietnamese: quyết` confirmed correct via hvdic (listed under both Âm Hán Việt and Âm Nôm). **`japanese` bug fixed**: the stored `KEI` was uncorroborated by either ja.Wiktionary (go-on ケチ/kan-on ケツ, no ケイ) or Jisho (ケツ only) — removed, leaving the confirmed `KETSU` alone. **`japanese_native` bug fixed**: bare unhyphenated `わかれ` corrected to properly hyphenated `わか-れる` ("to part ways"), the verb form corroborated by both sources; ja.Wiktionary's extra わけ/わ-ける weren't corroborated by Jisho and were left out.

`korean_native: 이별할` ("to part/separate") and `korean: 결` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㄱ.md`'s `### 결` subsection already lists 訣 correctly. `middle_chinese_initial/final: k`/`wet` reconfirmed correct against `聲 見`/`韻 屑合` (both lookup pages — the latter's own page independently documents 屑合 as a fully uniform 4-member group with no exceptions, 訣 among them — plus `SKIP-1-7-4`/`Stroke 11`/`Jinmeiyō`, already cited 訣 correctly). Blank `pos` filled: `名詞`, matching both citing stand-in compounds' own already-correct `名詞` classification.

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets) to the standard format. No Derived Characters (nothing names 訣 as its own `graphemic_classification`); no Chengyu hits. **`## Words` gap filled**: grepped all `words/*.md` citing 訣 in their `characters:` field and found a second stand-in, [[口訣]] ("mnemonic formula"), missing from the list alongside the existing [[秘訣]] — added.

**Both citing word pages reviewed, no bugs found**: [[秘訣]] (already perfected) and [[口訣]] (never perfected, but out of scope for this character sweep beyond the standard consequence-bug check) both already have real `vietnamese` values (not `null` placeholders), filled `pos: 名詞` fields, and no duplicate `品詞` fields — left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 訥 (char) (7310; 930 characters remaining).

### 2026-08-14, iteration 1575 — [[characters/訥 (char)|訥]]

**`mc_id` off-by-one bug fixed** (3923 → 3924; confirmed against `CC 3000.md` line 964-965, where "3923. 盼" precedes "3924. 訥"). **`graphemic_classification` bug fixed** (`會意` → `内`): en.Wiktionary classifies 訥 as 會意兼形聲 — semantic 言 + phonetic 內 (OC \*nuːbs, "inside," Zhengzhang whole-character \*nuːd) — a case where the phonetic component is directly identifiable, so per the checklist's "store the phonetic component, not the bare type string" convention this vault's field should name the phonetic component (matching the vault's existing page for 內/内, which already lists 內 as its own alias) rather than the coarser `會意` label; corrected. **Two new variant aliases added**: 吶 and 㕯, both confirmed genuine via cross-reference between en.Wiktionary's and zh.Wiktionary's independent variant lists (both agreeing on this exact pair, with 呐 noted as 吶's own simplified spelling rather than a separate third form); existing simplified alias 讷 reconfirmed correct.

**Major `vietnamese` contamination fixed**: the stored six-entry list (dốt, nhốt, nuốt, nói, nốt, nột) was almost entirely spurious — hvdic's actual entry for 訥 lists exactly **one** genuine Âm Hán Việt reading, `nột`, with dốt/nói/nốt/nuốt explicitly filed under Âm Nôm and `nhốt` not attested anywhere on the page at all (evidently a fabricated near-duplicate, the same pattern seen on [[characters/繞 (char)|繞]]'s own severe case). Trimmed to `nột` alone.

**`japanese` bug fixed**: the stored `DOTSU` was corroborated only by ja.Wiktionary (kan-on ドツ) and not by Jisho (トツ only) — removed per this session's established "corroborated by both" policy, the same reasoning applied to [[characters/訣|訣]]'s excluded `KEI` one iteration ago; `TOTSU` retained (both sources agree). **`japanese_native` bug fixed**: bare unhyphenated `ども` was a truncated fragment of the verb `どもる` — corrected to properly hyphenated `ども-る` ("to stammer"), confirmed via both sources.

**Blank `korean_native` bug fixed**: a Korean-language web search confirms 訥's real 훈(訓) gloss is "말더듬을" ("to stammer/stutter") — filled, matching this vault's established convention of storing a bare attributive verb stem (e.g. [[characters/葺 (char)|葺]]'s `이을`). `korean: 눌` reconfirmed correct (no 두음법칙 concern — the rule only affects ㄹ/ㄴ before ㅣ or a y-glide, and 눌's own vowel ㅜ isn't one of those); `Lookup/Korean/Korean Name ㄴ.md`'s `### 눌` subsection already lists 訥 correctly. `middle_chinese_initial/final: n`/`uət` reconfirmed correct against `聲 泥`/`韻 沒` (both lookup pages — the latter's own page independently documents 訥 and 肭 as the only two n-initial characters on this final, with 肭 alone dodging via a vowel shift — plus `SKIP-1-7-4`/`Stroke 11`, already cited 訥 correctly). **Blank `joyo_level` filled**: `表外字` (real on'yomi usage, no jōyō/jinmeiyō status) — **missing-entry bug fixed accordingly**, adding 訥 to `lookup/Japanese/Hyōgai.md` as entry #310. Blank `pos` filled: `事詞` (a transitive/intransitive verb — "to mumble, stammer").

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets, no `## Words` section) to the standard format, adding the missing self stand-in citation (`stand_in: 訥`). No Derived Characters (nothing names 訥 as its own `graphemic_classification`); no Chengyu hits (one grep hit, [[言行一致]], confirmed a false positive — 訥 not in its `characters:` field). One grep hit on another word page ([[巧言]]) confirmed a false positive — 訥 not in its `characters:` field either; only the existing self stand-in [[訥]] cites 訥 as a constituent.

**Citing word page [[訥]] (self stand-in) had two gaps fixed**: literal `vietnamese: null` placeholder → `nột`; missing `pos` field entirely → added `事詞`.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 諜 (7314; 929 characters remaining).

### 2026-08-14, iteration 1576 — [[characters/諜|諜]]

**`mc_id` off-by-one bug fixed** (3561 → 3562; confirmed against `CC 3000.md` line 586-587, where "3561. 柚" precedes "3562. 諜"). **`graphemic_classification: 枼` confirmed correct** (形聲, semantic 言 + phonetic 枼, part of the 世 phonetic series, Zhengzhang whole-character OC \*l'eːb), via en.Wiktionary; no new aliases beyond the existing simplified 谍, which en.Wiktionary also independently confirms.

`vietnamese: điệp` confirmed correct via hvdic (listed under both Âm Hán Việt and Âm Nôm, the same "no correction needed" pattern seen repeatedly this session). `japanese: CHOU` confirmed correct as the sole corroborated on-yomi (ja.Wiktionary's extra go-on ジョウ wasn't corroborated by Jisho and was excluded, matching this session's established cross-reference policy). **`japanese_native` gap filled**: the stored bare `うかが` was a truncated fragment of `うかが-う` ("to spy on, watch furtively") — both ja.Wiktionary and Jisho also independently agree on a second kun-yomi, `しめ-す` ("to show"); expanded to a proper hyphenated list.

`korean_native: 염탐할` ("to spy, reconnoiter") and `korean: 첩` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㅊ.md`'s `### 첩` subsection already lists 諜 correctly. `middle_chinese_initial/final: d`/`ep` reconfirmed correct against `聲 定`/`韻 帖` (both lookup pages — the latter's own page independently documents 諜 as one of a 6-member d/tʰ cluster escaping the main 帖-final group via a shared vowel-shift — plus `SKIP-1-7-9`/`Stroke 16`/`Hyōgai`, already cited 諜 correctly). Blank `pos` filled: `名詞`, matching the citing stand-in compound [[間諜]]'s own already-correct `名詞` classification ("spy, secret agent" as a person/noun).

Rebuilt the malformed `## Notes` (correct heading level already present, but only two bare unlinked CC-lookup wikilinks with no bullet structure at all) to the standard four-bullet format. No Derived Characters (nothing names 諜 as its own `graphemic_classification`); no Chengyu hits. Two grep hits on other word pages ([[喋]], [[情報]]) confirmed false positives — neither cites 諜 in its own `characters:` field; only the existing stand-in [[間諜]] cites 諜.

**Citing word page [[間諜]] reviewed, no bugs found**: already perfected (2026-06-03), `pos: 名詞` filled with no duplicate `品詞` field, `vietnamese: gián điệp` a genuine attested compound, not a `null` placeholder — left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 謎 (char) (7315; 928 characters remaining).

### 2026-08-14, iteration 1577 — [[characters/謎 (char)|謎]]

`mc_id: 0` confirmed plausible (謎 not found anywhere in `CC 0000`–`CC 3000.md`, consistent with it being a common but relatively late-attested word not core to classical prose). **`graphemic_classification: 迷` confirmed correct** (形聲, semantic 言 + phonetic 迷, "to be lost, bewildered"), via en.Wiktionary (whole-character Zhengzhang OC \*miː/\*miːs), independently corroborated by zh.Wiktionary's own 系列#1257（迷）phonetic-family grouping alongside 谜/瞇/醚/蒾. **New variant alias added**: 詸, confirmed genuine via both en.Wiktionary's and zh.Wiktionary's independent variant lists (the only candidate appearing in both; en.Wiktionary's extra 䛧 wasn't corroborated by zh.Wiktionary and was excluded); existing simplified alias 谜 reconfirmed correct.

`vietnamese: mê` confirmed correct via hvdic (listed under both Âm Hán Việt and Âm Nôm, the same "no correction needed" pattern seen repeatedly this session). **`japanese` gap filled**: ja.Wiktionary and Jisho both independently agree on two on-yomi, メイ (kan'yō-on) and ベイ (kan-on) — the stored `[MEI]` was missing the corroborated `BEI`; ja.Wiktionary's extra go-on マイ wasn't corroborated by Jisho and was excluded. `japanese_native: なぞ` confirmed correct (both sources agree; a bare nominal gloss needing no okurigana hyphenation).

`korean_native: 수수께끼` ("riddle") and `korean: 미` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㅁ.md`'s `### 미` subsection already lists 謎 correctly. `middle_chinese_initial/final: m`/`ei` reconfirmed correct against `聲 明`/`韻 齊開` (both lookup pages, plus `SKIP-1-7-10`/`Stroke 17`/`Jōyō - Kōtō`/`Old HSK 3`, already cited 謎 correctly). Blank `pos` filled: `名詞`.

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets, no `## Words` section) to the standard format, adding the missing self stand-in citation (`stand_in: 謎`). No Derived Characters (nothing names 謎 as its own `graphemic_classification`); no Chengyu hits. Two grep hits on other word pages ([[米]], [[迷]]) confirmed false positives — both are homophone-callout mentions in 謎's own citing word page, not citations of 謎 itself in their own `characters:` fields. Only the existing self stand-in [[謎]] cites 謎.

**Citing word page [[謎]] (self stand-in) had two gaps fixed**: literal `vietnamese: null` placeholder → `mê`; missing `pos` field entirely → added `名詞`.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 贋 (char) (7317; 927 characters remaining).

### 2026-08-14, iteration 1578 — [[characters/贋 (char)|贋]]

`mc_id: 0` confirmed plausible (贋 not found anywhere in `CC 0000`–`CC 3000.md`). **`graphemic_classification: 雁` confirmed correct** (形聲, semantic 貝 "money" + phonetic 雁, OC \*ŋraːns), via en.Wiktionary. **Malformed `aliases` field fixed**: the stored value was a single un-split string `贗赝` instead of a proper two-item YAML list — split into `贗`/`赝` (matching the already-correct list format on the citing word page [[贋]]); both confirmed genuine via en.Wiktionary (which frames 贋 itself as "a variant traditional form of 贗," with 赝 cross-referenced as the simplified form) and independently corroborated by zh.Wiktionary's own 異體字 box. zh.Wiktionary's box also listed 雁/鴈 and a further candidate 偐 — 雁 is already the character's own cited phonetic component and a full independent vault character (excluded per the established "don't alias an independent character" policy, e.g. [[characters/訥 (char)|訥]]'s excluded 決 two iterations ago); 偐 wasn't corroborated by en.Wiktionary and was excluded too.

`vietnamese: nhạn` confirmed correct via hvdic (listed under both Âm Hán Việt and Âm Nôm). `japanese: GAN` and `japanese_native: にせ` both confirmed correct via ja.Wiktionary (go-on ゲン wasn't corroborated elsewhere and was left out, matching this session's cross-reference policy). **Blank `korean_native` bug fixed**: cross-referenced Korean-language sources gave two different candidate glosses (ko.Wiktionary's "옳지 않다" vs. a hanja-meaning summary's "가짜") — chose `가짜` ("fake"), since it directly matches the character's own core meaning and English gloss, unlike the more oblique "not correct" phrasing.

`korean: 안` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `kwin: true` consistent (諺文 안 matches korean 안 exactly). `middle_chinese_initial/final: ŋ`/`ɣan` reconfirmed correct against `聲 疑`/`韻 刪開` (both lookup pages — the latter's own page independently documents 贋 as one of three null-initial members escaping a crowded ㄚㄋ collision, dodging without a leading letter, alongside 雁/顔 — plus `SKIP-3-2-17`/`Stroke 19`, already cited 贋 correctly). **Missing-entry bug fixed**: added 贋 to `lookup/Japanese/Jinmeiyō.md` as entry #477 (absent despite `joyo_level: 日本人名用漢字`); `hanmun_edu_level: 無` needed no manual list edit — `lookup/Korean/Korean Missing.md` is a pure dataview query auto-populated from the frontmatter field itself, not a manual list. Blank `pos` filled: `性詞`, matching the citing word page's own already-correct `性詞` classification ("fake" as an attributive/stative quality).

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets) to the standard format; `## Words` section was already present and correct. No Derived Characters (nothing names 贋 as its own `graphemic_classification`); no Chengyu hits. Two grep hits on other word pages ([[岸]], [[雁]]) confirmed false positives — both are the citing word page [[贋]]'s own homophone-callout mentions, not citations in either word's own `characters:` field.

**Citing word page [[贋]] reviewed, no bugs found**: already perfected (2026-05-15), `pos: 性詞` filled, `aliases` already a proper list, `vietnamese: nhạn` a genuine value — left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 贖 (7318; 926 characters remaining).

### 2026-08-14, iteration 1579 — [[characters/贖|贖]]

`mc_id: 1655` confirmed correct (matches `CC 1000.md` line 684, no off-by-one this time — a rare clean check, the same as [[characters/翔|翔]]'s a few iterations back). **`graphemic_classification: 𧶠` confirmed correct** (形聲, semantic 貝 "money" + phonetic 𧶠, OC \*ɦljoɡ), via en.Wiktionary — its own etymology note explains the phonetic element was originally 𧷏 but was later graphically reshaped into the unrelated-looking 賣, independently corroborated by zh.Wiktionary's identical account. **New variant alias added**: 𧹎, confirmed genuine via both en.Wiktionary's and zh.Wiktionary's independent variant lists (the only candidate appearing in both); existing simplified alias 赎 reconfirmed correct.

**Major `vietnamese` contamination fixed**: the stored `[chuộc, thục]` mixed one genuine Hán Việt reading (`thục`) with a Nôm-only form — hvdic's actual entry for 贖 lists exactly one Âm Hán Việt reading, `thục`, filing `chuộc` under Âm Nôm — trimmed accordingly (the citing word page [[贖罪]]'s own detailed prose already independently explains this exact distinction, calling `chuộc` "a genuine older, vernacular doublet ... not itself Hán Việt," corroborating the fix even though it's a much richer word than the fabricated Nôm entries seen on other characters this session). **`japanese` field investigated, no change**: ja.Wiktionary lists an extra go-on ゾク not corroborated by Jisho (which shows only ショク) — excluded per this session's established cross-reference policy, leaving `SHOKU` alone. **`japanese_native` bug fixed**: bare unhyphenated `あがな` corrected to properly hyphenated `あがな-う` ("to atone, redeem"), confirmed via both sources.

`korean_native: 속바칠` ("to pay as ransom/tribute") and `korean: 속` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㅅ.md`'s `### 속` subsection already lists 贖 correctly. `middle_chinese_initial/final: ʑ`/`ɨok` reconfirmed correct against `聲 船`/`韻 燭` (both lookup pages, plus `SKIP-1-7-15`/`Stroke 22`, already cited 贖 correctly). **Missing-entry bug fixed**: `joyo_level: 表外字` was already correctly set, but 贖 was entirely absent from `lookup/Japanese/Hyōgai.md` — added as entry #311. Blank `pos` filled: `事詞` (a transitive verb — "to ransom, redeem").

**Major `## Words` gap filled**: the character's own `stand_in: 贖罪` names 贖罪 as the required stand-in compound, but the pre-existing `## Words` section only listed the secondary citing word [[救贖]] and omitted the stand-in itself entirely — added [[贖罪]] first, ahead of 救贖, per the checklist's "most common/central word first" ordering (the stand-in compound takes precedence). Grepped all `words/*.md` and confirmed no other word cites 贖 as a constituent; two further word-page hits ([[償還]], [[祭物]]) and four chengyu hits ([[世間罪盛]], [[創反救成]], [[破頭傷足]], [[血誓盟約]]) were all confirmed false positives — none cite 贖 in their own `characters:` field.

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets, missing blank line before `## Words`) to the standard format. No Derived Characters (nothing names 贖 as its own `graphemic_classification`); no Chengyu hits.

**Both citing word pages reviewed, no bugs found**: [[救贖]] and [[贖罪]] are both already perfected, with `pos` filled, no duplicate `品詞` fields, and genuine (non-`null`) `vietnamese` values — left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 迂 (7320; 925 characters remaining).

### 2026-08-14, iteration 1580 — [[characters/迂|迂]]

**`mc_id` off-by-one bug fixed** (2989 → 2990; confirmed against `CC 2000.md` line 1030, where "2989. 觚" precedes "2990. 迂"). **`graphemic_classification: 于` confirmed correct** (形聲, semantic 辵/辶 "movement, path" + phonetic 于), via en.Wiktionary (Zhengzhang whole-character OC \*qʷa/\*qʷaʔ/\*ɢʷa). **New variant alias added**: 迃, confirmed genuine via both en.Wiktionary's and zh.Wiktionary's independent variant lists (the only candidate appearing in both); en.Wiktionary's extra "ancient form" 込 wasn't corroborated by zh.Wiktionary and was excluded.

`vietnamese: vu` confirmed correct via hvdic (explicitly the sole genuine Âm Hán Việt reading, no Nôm contamination this time). `japanese: U` and `japanese_native: ø` (no kun-yomi) both confirmed correct via ja.Wiktionary (go-on and kan-on both ウ; the entry has no kun'yomi section at all).

`korean_native: 에돌` ("to go around") and `korean: 우` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `kwin: true` consistent (諺文 우 matches korean 우 exactly). `Lookup/Korean/Korean Name ㅇ.md`'s `### 우` subsection already lists 迂 correctly. `middle_chinese_initial/final: ʔ`/`ɨo` reconfirmed correct against `聲 影`/`韻 虞` (both lookup pages, plus `SKIP-3-3-3`/`Stroke 06`/`Jinmeiyō`, already cited 迂 correctly — the latter's own page has a pre-existing broken relative-path link on an unrelated entry, [[衢]], left untouched as out of scope for this iteration). Blank `pos` filled: `性詞` (a stative/adjectival quality — "roundabout, circuitous").

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets, no `## Words` section) to the standard format, adding the missing stand-in citation (`stand_in: 迂回`). No Derived Characters (nothing names 迂 as its own `graphemic_classification`); no Chengyu hits. One grep hit on another word page ([[重畳]]) confirmed a false positive — doesn't cite 迂 in its own `characters:` field; only the existing stand-in [[迂回]] cites 迂.

**Citing word page [[迂回]] left untouched**: blank `vietnamese` is a genuine never-perfected gap — a quick hvdic lookup for the compound 迂回 returned no direct hit, so there was no directly-evidenced answer in hand; left for the word-sweep, matching the established "genuine gap" pattern from prior iterations.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 逞 (char) (7321; 924 characters remaining).

### 2026-08-14, iteration 1581 — [[characters/逞 (char)|逞]]

**`mc_id` off-by-one bug fixed** (2761 → 2762; confirmed against `CC 2000.md` line 794-795, where "2761. 准" precedes "2762. 逞"). **`graphemic_classification: 呈` confirmed correct** (形聲, semantic 辵/辶 + phonetic 呈, Zhengzhang whole-character OC \*l̥ʰeŋʔ), via en.Wiktionary, independently corroborated by zh.Wiktionary's own 系列#0208（呈）phonetic-family grouping. **New variant alias added**: 徎, confirmed genuine via both en.Wiktionary's and zh.Wiktionary's independent variant lists (en.Wiktionary's other candidate, 呈, was excluded as merely a repeat citation of the phonetic component itself, not a true variant, per zh.Wiktionary's own explicit clarification).

**Interesting near-miss investigated, no contamination found**: the stored `vietnamese: [sánh, sính]` is the exact same two-reading pair seen on [[characters/聘 (char)|聘]] a few iterations ago (where `sánh` was trimmed as Nôm-only contamination) — raising suspicion of a copy-paste error between the two characters. However, hvdic's own entry for 逞 independently confirms the identical split holds true here too: `sính` is genuine Âm Hán Việt, `sánh` is Nôm-only — so the fix (trimming to `sính` alone) is correct, but the coincidence is just that, a coincidence, not evidence of a shared bug; verified rather than assumed.

**`japanese` field investigated, no change**: ja.Wiktionary lists an extra go-on チョウ not corroborated by Jisho (which shows only テイ) — excluded, leaving `TEI` alone, matching this session's cross-reference policy. **`japanese_native` bug fixed**: bare unhyphenated `たくま` corrected to properly hyphenated `たくま-しい` ("burly, strong, sturdy" — the extended/figurative sense beyond "indulge, brag"), confirmed via both sources.

`korean_native: 쾌할` ("pleasant, brisk") and `korean: 령` reconfirmed correct (no 두음법칙 concern — the rule affects word-initial position, and 령 isn't being spelled as 영 here, consistent with this vault's convention); `Lookup/Korean/Korean Name ㄹ.md`'s `### 령` subsection already lists 逞 correctly. `middle_chinese_initial/final: ʈʰ`/`iᴇŋ` reconfirmed correct against `聲 徹`/`韻 清開` (both lookup pages, plus `SKIP-3-4-7`/`Stroke 11`/`Jinmeiyō`, already cited 逞 correctly). Blank `pos` filled: `事詞` (a transitive/intransitive verb — "to indulge, give free rein to, brag").

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets, no `## Words` section) to the standard format, adding the missing self stand-in citation (`stand_in: 逞`). No Derived Characters (nothing names 逞 as its own `graphemic_classification`); no Chengyu hits. Only the existing self stand-in [[逞]] cites 逞.

**Citing word page [[逞]] (self stand-in) had two gaps fixed**: literal `vietnamese: null` placeholder → `sính`; missing `pos` field entirely → added `事詞`.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 遽 (7322; 923 characters remaining).

### 2026-08-14, iteration 1582 — [[characters/遽|遽]]

**`mc_id` off-by-one bug fixed** (1989 → 1990; confirmed against `CC 1000.md` line 1030-1031, where "1989. 淑" precedes "1990. 遽"). **`graphemic_classification: 豦` confirmed correct** (形聲, semantic 辵/辶 + phonetic 豦, Zhengzhang whole-character OC \*ɡas), via en.Wiktionary. **Existing alias 蘧 reconfirmed correct**: both en.Wiktionary (explicitly calling 遽 "a variant form of 蘧") and zh.Wiktionary's own 異體字 box agree, despite 蘧's own primary meaning ("fringed pink," a plant name) being unrelated — the variant relationship holds specifically for this shared graphemic form, the same kind of dual-meaning-alias case as [[characters/聘 (char)|聘]]'s 娉 and [[characters/舵 (char)|舵]]'s 杕 in prior iterations. No further variant candidates on either source.

`vietnamese: cự` confirmed correct via hvdic (listed under both Âm Hán Việt and Âm Nôm, no contamination). `japanese: KYO` confirmed correct as the sole corroborated on-yomi (ja.Wiktionary's extra go-on ゴ wasn't corroborated by Jisho and was excluded). **`japanese_native` gap filled**: the stored bare `あわ` was a truncated fragment — both ja.Wiktionary and Jisho independently agree on a full set of four kun-yomi, `あわ-てる` ("to be flustered"), `あわただ-しい` ("hectic, hasty"), `すみやか` ("swift"), and `にわか` ("sudden"); expanded to the complete hyphenated list.

`korean_native: 급히` ("hastily") and `korean: 거` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㄱ.md`'s `### 거` subsection already lists 遽 correctly. `middle_chinese_initial/final: ɡ`/`ɨʌ` reconfirmed correct against `聲 群`/`韻 魚` (both lookup pages, plus `SKIP-3-4-13`/`Stroke 17`/`Hyōgai`, already cited 遽 correctly). Blank `pos` filled: `性詞` (a stative/adjectival quality — "in a hurry, hasty").

Rebuilt malformed `## Notes` (correct heading level already present, but only two bare unlinked CC-lookup wikilinks with no bullet structure at all) to the standard four-bullet format; `## Words` section was already present and correct. No Derived Characters (nothing names 遽 as its own `graphemic_classification`); no Chengyu hits. Only the existing stand-in [[急遽]] cites 遽.

**Citing word page [[急遽]] left untouched**: blank `vietnamese` (field entirely absent, not a `null` placeholder) is a genuine never-perfected gap, left for the word-sweep; `pos: 副詞` already filled with no duplicate `品詞` field.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 釉 (7323; 922 characters remaining).

### 2026-08-14, iteration 1583 — [[characters/釉|釉]]

`mc_id: 0` confirmed plausible (釉 not found anywhere in `CC 0000`–`CC 3000.md`). **`graphemic_classification: 由` confirmed correct** (形聲, semantic 采 "color" + phonetic 由, OC \*lɯwɢs), via en.Wiktionary, independently corroborated by zh.Wiktionary's identical account (explicitly noting the character can also be written with the visually similar 釆 in place of 采, matching this vault's own `radical: 釆` field, which indexes 釉 under Kangxi radical 165 for lookup purposes even though the semantic component itself is technically the distinct-but-near-identical 采 — left as bare text rather than radical-linked, since 采 itself isn't literally the Kangxi radical). **No alias added**: zh.Wiktionary's sole variant candidate, 𥑤, wasn't corroborated by en.Wiktionary, and was excluded per the established "both sources must agree" policy.

`vietnamese: dứu` and `japanese: YUU` (Jisho's sole listed on-yomi; ja.Wiktionary's extra go-on ユ wasn't corroborated and was excluded) both confirmed correct, no changes. `japanese_native: うわぐすり` also confirmed correct via both sources.

`korean_native: 광택` ("gloss, luster") and `korean: 유` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㅇ.md`'s `### 유` subsection already lists 釉 correctly. `middle_chinese_initial/final: j`/`ɨu` reconfirmed correct against `聲 以`/`韻 尤` (both lookup pages, plus `SKIP-1-7-5`/`Stroke 12`/`Jinmeiyō`, already cited 釉 correctly). Blank `pos` filled: `名詞` (a concrete noun — "glaze, enamel").

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets, no `## Words` section at all) to the standard format, adding the missing stand-in citation (`stand_in: 釉薬`). No Derived Characters (nothing names 釉 as its own `graphemic_classification`); no Chengyu hits. Only the existing stand-in [[釉薬]] cites 釉.

**Citing word page [[釉薬]] reviewed, no bugs found**: `pos: 名詞` already filled with no duplicate `品詞` field; `vietnamese: dứu` a genuine value, not a `null` placeholder; empty `aliases: []` is a valid empty list, not a bug — left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 鉗 (char) (7324; 921 characters remaining).

### 2026-08-14, iteration 1584 — [[characters/鉗 (char)|鉗]]

**`mc_id` off-by-one bug fixed** (2701 → 2702; confirmed against `CC 2000.md` line 734-735, where "2701. 竄" precedes "2702. 鉗"). **`graphemic_classification: 甘` confirmed correct** (形聲, semantic 金 "metal" + phonetic 甘, Zhengzhang whole-character OC \*ɡram), via en.Wiktionary, independently corroborated by zh.Wiktionary's own 系列#0506（甘）phonetic-family grouping. **New variant alias added**: 箝, confirmed genuine via both en.Wiktionary's and zh.Wiktionary's independent variant lists; zh.Wiktionary's further candidates 䈤/鉆 weren't corroborated by en.Wiktionary and were excluded; existing simplified alias 钳 reconfirmed correct.

**Severe `vietnamese` contamination fixed**: the stored seven-entry list (cùm, cườm, ghìm, kiềm, kèm, kìm, kềm) was almost entirely spurious — hvdic's actual entry for 鉗 lists exactly **one** genuine Âm Hán Việt reading, `kiềm`, filing all six other entries under Âm Nôm — trimmed to `kiềm` alone, one of the largest contamination cases found this session (matching [[characters/繞 (char)|繞]]'s own 11-entry case in scale).

**`korean_native: 칼` investigated and reconfirmed correct**: at first glance this looks like a mismatch (칼 usually means "knife"), but Korean-language sources confirm 칼 also independently denotes a historical wooden/metal neck-restraint device (a cangue), a documented second meaning distinct from the "knife" sense — this exactly matches 鉗's own attested historical meaning (a metal device binding the neck or legs of a prisoner, per Former Han-era usage) and is directly corroborated by the character's own Japanese kun-yomi `くびかせ` ("neck restraint, cangue"). No change needed; folded the historical meaning into the rebuilt graphemic bullet's dash-note. **`japanese: [KAN, KEN]` confirmed correct** (Jisho corroborates both; ja.Wiktionary's extra go-on ゲン wasn't corroborated and was excluded). **`japanese_native` gap filled**: the stored `くびかせ` was genuine but incomplete — both ja.Wiktionary and Jisho independently agree on a second kun-yomi, `つぐ-む` ("to shut one's mouth, keep silent"); added, properly hyphenated, converting the field to a proper list.

`korean: 겸` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㄱ.md`'s `### 겸` subsection already lists 鉗 correctly. `middle_chinese_initial/final: ɡ`/`ɣiᴇm` reconfirmed correct against `聲 群`/`韻 鹽B三` (both lookup pages — the latter's own page independently documents 鉗 among a crowded 4-member g/k-initial slot that a fifth character, 芡, dodges via vowel-shift — plus `SKIP-1-8-5`/`Stroke 13`/`Hyōgai`/`Old HSK 4`, already cited 鉗 correctly). Blank `pos` filled: `名詞` (a concrete noun — "vice, pliers, forceps").

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets, no `## Words` section) to the standard format, adding the missing self stand-in citation (`stand_in: 鉗`). No Derived Characters (nothing names 鉗 as its own `graphemic_classification`); no Chengyu hits. One grep hit on another word page ([[兼]]) confirmed a false positive — a homophone (`gem`/`검`) mention, not a `characters:` citation; only the existing self stand-in [[鉗]] cites 鉗.

**Citing word page [[鉗]] (self stand-in) had two gaps fixed**: literal `vietnamese: null` placeholder → `kiềm`; missing `pos` field entirely → added `名詞`.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 塚 (char) (7325; 920 characters remaining).

### 2026-08-14, iteration 1585 — [[characters/塚 (char)|塚]]

**`mc_id` off-by-one bug fixed** (3978 → 3979; confirmed against `CC 3000.md` line 1019-1020, where "3978. 澍" precedes "3979. 塚"). **`graphemic_classification: 冢` confirmed correct** (形聲, semantic 土 "earth" + phonetic 冢, OC \*toŋʔ), via en.Wiktionary — an unusual case where 塚 is itself essentially a variant elaboration of its own phonetic component 冢 (both meaning "earthen mound/grave"), with 土 added seemingly to reinforce rather than newly specify the sense; folded this into the graphemic bullet's dash-note. **New alias added**: 冢, confirmed as a genuine variant via both en.Wiktionary and zh.Wiktionary's independent 異體字 boxes; no independent vault character page exists for 冢, so no conflict.

**`vietnamese` gap filled**: hvdic's entry for 塚 lists two genuine Âm Hán Việt readings, `trũng` and `trủng`, but only `trủng` was stored — added the missing `trũng`. **Major `japanese_native` bug fixed**: the stored `ø` (asserting no kun-yomi at all) was simply wrong — both ja.Wiktionary and Jisho independently and clearly attest a real, standard kun-yomi, `つか` ("mound, tomb"); corrected from the false-negative sentinel to the genuine reading. `japanese: CHOU` confirmed correct (Jisho's sole listed on-yomi; ja.Wiktionary's extra go-on チュウ wasn't corroborated and was excluded).

`korean_native: 무덤` ("grave") and `korean: 총` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `kwin: true` consistent (諺文 총 matches korean 총 exactly). `middle_chinese_initial/final: ʈ`/`ɨoŋ` reconfirmed correct against `聲 知`/`韻 鍾` (both lookup pages — the former's own page independently documents 塚 as one of the small ㄑ-aspirated pocket in 知's messiest four-way split, its aspiration predicted by matching Cantonese/Korean aspiration rather than Mandarin — plus `SKIP-1-3-9`/`Stroke 12`/`Jōyō - Kōtō`, already cited 塚 correctly). **Missing-entry bug fixed**: `hanmun_edu_level: 高等` requires a citation on `lookup/Korean/Korean HS.md`, but 塚 was absent from its `#### 총` subsection despite three sibling characters (銃/總/聰) already being listed there — added, `(무덤 총)`.

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets) to the standard format, re-adding the pre-existing `## Words` self-citation that was accidentally dropped mid-edit and immediately restored. No Derived Characters (nothing names 塚 as its own `graphemic_classification`); no Chengyu hits. Three grep hits on other word pages ([[衝]], [[重]], [[軽歌劇]]) confirmed false positives — all homophone/compound-component mentions in prose, none citing 塚 in a `characters:` field; only the existing self stand-in [[塚]] cites 塚.

**Citing word page [[塚]] left untouched**: already fully perfected (2026-07-11) with rich comparative prose across all five languages, `vietnamese: trủng` (one of the two now-confirmed genuine readings, a valid representative choice), `pos: 名詞` filled — no bugs found.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 蟄 (char) (7326; 919 characters remaining).

### 2026-08-14, iteration 1586 — [[characters/蟄 (char)|蟄]]

**`mc_id` off-by-one bug fixed** (2302 → 2303; confirmed against `CC 2000.md` line 319-320, where "2302. 銘" precedes "2303. 蟄"). **`graphemic_classification: 執` confirmed correct** (形聲, semantic 虫 "insect" + phonetic 執, Zhengzhang whole-character OC \*dib), via en.Wiktionary. **No alias added**: en.Wiktionary's extra variant candidate, 𧒦, wasn't corroborated by zh.Wiktionary (which lists only the already-stored simplified 蛰) — excluded per the established "both sources must agree" policy.

**Major `vietnamese` contamination fixed**: the stored four-entry list (chẫu, chập, chặp, trập) mixed two genuine Hán Việt readings with two Nôm-only forms — hvdic's actual entry for 蟄 lists exactly `chập` and `trập` under Âm Hán Việt, filing `chẫu` and `chặp` under Âm Nôm only — trimmed to the two genuine readings. **`japanese` field reconfirmed correct**: both `CHITSU` (kan'yō-on) and `CHUU` (kan-on) are corroborated by both ja.Wiktionary and Jisho; ja.Wiktionary's extra go-on ジュウ wasn't corroborated and was excluded. **`japanese_native` bug fixed**: the stored bare `かく` was a truncated fragment — both sources agree on two kun-yomi, `かく-れる` ("to hide/conceal") and `ちっ-する` (a suru-verb form); corrected and expanded, properly hyphenated. **Blank `joyo_level` filled**: `表外字` — cross-verified via multiple sources that despite carrying real, standard on'yomi and kun'yomi, 蟄 carries no jōyō or jinmeiyō classification (a Kanken 1級 character, the highest/most obscure proficiency tier, well above the jōyō-covering tiers; an AI-search-engine summary claiming 常用漢字 status was checked against Jisho and Kanjipedia directly and found unsupported — neither shows any formal grade/classification for this kanji) — **missing-entry bug fixed accordingly**, adding 蟄 to `lookup/Japanese/Hyōgai.md` as entry #312.

`korean_native: 동면할` ("to hibernate") and `korean: 칩` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `kwin: true` consistent (諺文 칩 matches korean 칩 exactly); `Lookup/Korean/Korean Name ㅊ.md`'s `### 칩` subsection already lists 蟄 correctly. `middle_chinese_initial/final: ɖ`/`ɣiɪp` reconfirmed correct against `聲 澄`/`韻 緝B三` (both lookup pages, plus `SKIP-2-11-6`/`Stroke 17`/`HSK No`, already cited 蟄 correctly). Blank `pos` filled: `事詞` (an intransitive verb — "to hibernate").

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets, no `## Words` section) to the standard format, adding the missing self stand-in citation (`stand_in: 蟄`). No Derived Characters (nothing names 蟄 as its own `graphemic_classification`); no Chengyu hits. Only the existing self stand-in [[蟄]] cites 蟄.

**Citing word page [[蟄]] (self stand-in) had two gaps fixed**: literal `vietnamese: null` placeholder → `trập`; missing `pos` field entirely → added `事詞`.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 銹 (char) (7327; 918 characters remaining).

### 2026-08-14, iteration 1587 — [[characters/銹 (char)|銹]]

`mc_id: 8367` confirmed as legitimate long-tail data (銹 not found anywhere in `CC 0000`–`CC 3000.md`, consistent with the checklist's policy of trusting an existing above-4000 rank verbatim). **`graphemic_classification: 秀` confirmed correct** (形聲, semantic 金 "metal" + phonetic 秀, OC \*slus), via en.Wiktionary, independently corroborated by zh.Wiktionary's identical account (explicitly framing 銹 as "another way of writing 鏽/锈"). Existing aliases 鏽 (traditional) and 锈 (simplified) both reconfirmed correct via both sources; no further candidates.

`vietnamese: tú` confirmed correct via hvdic, no contamination. **`japanese` gap filled**: both ja.Wiktionary and Jisho independently agree on two on-yomi, シュウ (kan-on) and シュ (go-on) — the stored `[SHUU]` was missing the corroborated `SHU`, added. `japanese_native: さび` confirmed correct (a bare nominal gloss, no hyphenation needed); ja.Wiktionary's extra verb form さ-びる wasn't corroborated by Jisho and was excluded.

`korean_native: 녹슬` ("to rust") and `korean: 수` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㅅ.md`'s `### 수` subsection already lists 銹 correctly. `middle_chinese_initial/final: s`/`ɨu` reconfirmed correct against `聲 心`/`韻 尤` (both lookup pages, plus `SKIP-1-8-7`/`Stroke 15`/`Old HSK 3`, already cited 銹 correctly). **Missing-entry bug fixed**: `joyo_level: 表外字` was already correctly set, but 銹 was entirely absent from `lookup/Japanese/Hyōgai.md` — added as entry #313. Blank `pos` filled: `名詞` (a concrete noun — "rust").

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets) to the standard format; `## Words` section was already present and correct (self stand-in `stand_in: 銹`). No Derived Characters (nothing names 銹 as its own `graphemic_classification`); no Chengyu hits. Two grep hits on other word pages ([[手]], [[痩]]) confirmed false positives — both are the citing word page [[銹]]'s own homophone-callout mentions, not `characters:` citations. Only the existing self stand-in [[銹]] cites 銹.

**Citing word page [[銹]] (self stand-in) had two gaps fixed**: literal `vietnamese: null` placeholder → `tú`; missing `pos` field entirely → added `名詞`.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 鍍 (7328; 917 characters remaining).

### 2026-08-14, iteration 1588 — [[characters/鍍|鍍]]

`mc_id: 0` confirmed plausible (鍍 not found anywhere in `CC 0000`–`CC 3000.md`, consistent with a technical/craft term absent from classical prose). **`graphemic_classification: 度` confirmed correct** (形聲, semantic 金 "metal" + phonetic 度, Zhengzhang whole-character OC \*daː/\*daːɡs), via en.Wiktionary; existing simplified alias 镀 reconfirmed correct. **No alias added**: zh.Wiktionary's extra variant candidate, 塗, wasn't corroborated by en.Wiktionary, and 塗 is itself a full independent vault character with its own distinct meaning ("to spread, paint over") — excluded per the established "don't alias an independent character absent source agreement" policy.

`vietnamese: độ` confirmed correct via hvdic, no contamination. `japanese: TO` confirmed correct as the sole corroborated on-yomi (ja.Wiktionary's extra go-on ド wasn't corroborated by Jisho and was excluded). `japanese_native: めっき` confirmed correct via both sources (a bare nominal gloss, no hyphenation needed).

`korean_native: 도금할` ("to plate/gild") and `korean: 도` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `kwin: true` consistent (諺文 도 matches korean 도 exactly); `Lookup/Korean/Korean Name ㄷ.md`'s `### 도` subsection already lists 鍍 correctly. `middle_chinese_initial/final: d`/`uo` reconfirmed correct against `聲 定`/`韻 模` (both lookup pages, plus `SKIP-1-8-9`/`Stroke 17`/`Old HSK 4`, already cited 鍍 correctly). **Blank `joyo_level` filled**: `表外字` — cross-verified via a Japanese-language source (kanji.jitenon.jp) explicitly classifying 鍍 as 表外漢字 with a real reading (ト) and no jōyō/jinmeiyō status — **missing-entry bug fixed accordingly**, adding 鍍 to `lookup/Japanese/Hyōgai.md` as entry #314. Blank `pos` filled: `事詞` (a transitive verb — "to coat, gild, plate").

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets) to the standard format; `## Words` section was already present and correct. No Derived Characters (nothing names 鍍 as its own `graphemic_classification`); no Chengyu hits. One grep hit on another word page ([[杜金]]) confirmed a false positive — cites 杜, not 鍍, in its own `characters:` field; only the existing stand-in [[鍍金]] cites 鍍.

**Citing word page [[鍍金]] reviewed, no bugs found**: already perfected (2026-05-15), `pos: 名詞` filled, `vietnamese: độ kim` a genuine attested compound, no duplicate `品詞` field — left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 闊 (char) (7329; 916 characters remaining).
