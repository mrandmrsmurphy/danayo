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

### 2026-08-14, iteration 1589 — [[characters/闊 (char)|闊]]

**`mc_id` off-by-one bug fixed** (2924 → 2925; confirmed against `CC 2000.md` line 965-966, where "2924. 瘦" precedes "2925. 闊"). **`graphemic_classification: 活` confirmed correct** (形聲, semantic 門 "gate; door" + phonetic 活, Zhengzhang whole-character OC \*kʰoːd), via en.Wiktionary, corroborated by zh.Wiktionary. **New variant alias added**: 䦢, confirmed genuine via both en.Wiktionary's and zh.Wiktionary's independent variant lists (a further en.Wiktionary-only trio, 𨶖/𨴿, and a zh.Wiktionary-only candidate, 䦚, weren't cross-corroborated and were excluded); existing aliases 阔/濶 reconfirmed correct.

**`vietnamese` contamination fixed**: the stored `[khoát, khoắt]` mixed one genuine Hán Việt reading with a Nôm-only form — hvdic's actual entry lists only `khoát` under Âm Hán Việt, filing `khoắt` under Âm Nôm — trimmed to `khoát` alone. **`japanese_native` bug fixed**: bare unhyphenated `ひろ` corrected to properly hyphenated `ひろ-い` ("wide, broad"), confirmed via both ja.Wiktionary and Jisho; ja.Wiktionary's extra go-on カチ wasn't corroborated by Jisho and the existing `japanese: [KATSU]` was left unchanged.

**Blank `hanmun_edu_level` bug fixed**: filled `名` — `Lookup/Korean/Korean Name ㅎ.md`'s own `### 활` subsection already cited 闊, revealing the frontmatter field itself was simply never filled despite the citation already existing; **a broken link on that same subsection line was fixed as a direct consequence**, since the pre-existing citation pointed to the word page (`words/闊.md`) instead of the character page, inconsistent with every sibling entry on the same line. `korean_native: 넓을` ("wide") and `korean: 활` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial). `middle_chinese_initial/final: kʰ`/`uɑt` reconfirmed correct against `聲 溪`/`韻 末` (both lookup pages, plus `SKIP-3-8-9`/`Stroke 17`/`Hyōgai`/`Old HSK 2`, already cited 闊 correctly). Blank `pos` filled: `性詞` (a stative/adjectival quality — "broad, wide").

**Major `## Words`/`## Chengyu` gaps filled**: `stand_in: 闊` means 闊 is a standalone word, but the pre-existing `## Words` section omitted the self-citation entirely, listing only the two secondary compounds [[久闊]] and [[闊葉]] — added the missing self stand-in first, per ordering convention. [[闊葉]]'s own entry was also missing its ruby annotation entirely (a bare unformatted wikilink); rebuilt to match the standard `<ruby>`+gloss format, pulling the reading from its own stored `注音`. **New `## Chengyu` section added**: grepped all `chengyu/*.md` and found a genuine hit, [[海闊天空]] ("as boundless as the sky and sea," 闊 confirmed present in its own `characters:` field), previously entirely unlisted on the character page; a second grep hit, [[白頭偕老]], confirmed a false positive. Rebuilt malformed `## Notes` (correct heading level already present, but missing three of the four standard bullets — only the graphemic bullet existed, with two bare unlinked CC-lookup wikilinks floating below it) to the full standard format.

No Derived Characters (nothing names 闊 as its own `graphemic_classification`). Four further grep hits on other word pages ([[久]], [[交友]], [[交遊]]) were confirmed false positives — none cite 闊 in their own `characters:` field.

**Citing word page [[闊]] (self stand-in) had two gaps fixed**: literal `vietnamese: null` placeholder → `khoát`; missing `pos` field entirely → added `性詞`. **Citing word page [[久闊]] reviewed, no bugs found** (already perfected). **Citing word page [[闊葉]] left otherwise untouched**: its own blank `vietnamese`/`cantonese` fields are genuine never-perfected gaps, out of scope for this character-level pass — its missing ruby was fixed only on the character page's own citation of it, not on 闊葉's own page.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 鞄 (char) (7330; 915 characters remaining).

### 2026-08-14, iteration 1590 — [[characters/鞄 (char)|鞄]]

`mc_id: 8366` confirmed as legitimate long-tail data (鞄 not found anywhere in `CC 0000`–`CC 3000.md`). **`graphemic_classification: 包` confirmed correct** (形聲, semantic 革 "leather" + phonetic 包, Zhengzhang whole-character OC \*bruː/\*bruːʔ/\*bruːs/\*pʰruːɡ), via en.Wiktionary — the pre-existing OC reconstruction data in the Notes bullet was already accurate, but the phonetic-component link itself was corrupted: a malformed self-referential wikilink, `[[鞄 (char)]]包`, pointing the character back at its own page instead of at 包 — corrected to a proper `[[包 (char)|包]]` link.

**`vietnamese` gap filled**: hvdic's entry for 鞄 lists two genuine Âm Hán Việt readings, `bào` and `bạc`, but only `bạc` was stored — added the missing `bào` (the existing `bạc` also appears under Âm Nôm on the same page, the "listed in both categories, no contamination" pattern seen repeatedly this session, not a bug). **`japanese` bug fixed**: cross-referencing ja.Wiktionary (go-on ビョウ, kan-on ホウ, no ハク at all) against Jisho (all three: ハク/ホウ/ビョウ) — only ホウ and ビョウ are corroborated by both sources; the stored `HAKU` (Jisho-only) was dropped and the missing `BYOU` added, per this session's established cross-reference policy. `japanese_native: かばん` confirmed correct via both sources.

`korean_native: 혁공` ("leathercraft") and `korean: 포` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial). `middle_chinese_initial/final: pʰ`/`ɣʌk` reconfirmed correct against `聲 滂`/`韻 覺` (both lookup pages, plus `SKIP-1-9-5`/`Stroke 14`/`Jinmeiyō`, already cited 鞄 correctly). `hanmun_edu_level: 無` confirmed correct as-is — `lookup/Korean/Korean Missing.md` is a pure dataview auto-query, not a manual list, so no missing-entry fix was needed there. Blank `pos` filled: `名詞` (a concrete noun — "bag, luggage").

Rebuilt malformed `## Notes` (correct heading level already present, but missing all three of the SKIP/Stroke, MC-rank, and levels bullets — only the graphemic bullet existed, with two bare unlinked CC-lookup wikilinks floating below it) to the full standard format, adding the missing `## Words` self-citation (`stand_in: 鞄`). No Derived Characters (nothing names 鞄 as its own `graphemic_classification`); no Chengyu hits. Only the existing self stand-in [[鞄]] cites 鞄.

**Citing word page [[鞄]] (self stand-in) had two gaps fixed**: literal `vietnamese: null` placeholder → `bào`; missing `pos` field entirely → added `名詞`.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 顆 (7331; 914 characters remaining).

### 2026-08-14, iteration 1591 — [[characters/顆|顆]]

**`mc_id` off-by-one bug fixed** (3879 → 3880; confirmed against `CC 3000.md` line 916-917, where "3879. 茸" precedes "3880. 顆"). **`graphemic_classification: 果` confirmed correct** (形聲, semantic 頁 "head" + phonetic 果, Zhengzhang whole-character OC \*kʰloːlʔ), via en.Wiktionary; existing simplified alias 颗 reconfirmed correct. **No alias added**: zh.Wiktionary's extra candidate, 䂺, wasn't corroborated by en.Wiktionary and was excluded.

**`vietnamese` contamination fixed**: the stored `[khoả, loã]` mixed one genuine Hán Việt reading with a Nôm-only form — hvdic's actual entry lists `khoã` and `khoả` under Âm Hán Việt (filing `loã` under Âm Nôm only) — replaced accordingly, keeping `khoả` and adding the previously-missing `khoã`. **`japanese_native` bug fixed**: the stored bare `つ` was a truncated fragment of the real kun-yomi `つぶ` ("grain, granule"), confirmed by both ja.Wiktionary and Jisho; corrected. `japanese: KA` confirmed correct (the sole on-yomi per both sources).

`korean_native: 낱알` ("individual grain") and `korean: 과` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㄱ.md`'s `### 과` subsection already lists 顆 correctly. `middle_chinese_initial/final: kʰ`/`uɑ` reconfirmed correct against `聲 溪`/`韻 戈一合` (both lookup pages — the latter's own page independently notes 顆 as the only other kʰ-initial character on this final besides 課, which dodges via a coda addition — plus `SKIP-1-8-9`/`Stroke 17`/`Hyōgai`/`Old HSK 2`, already cited 顆 correctly). Blank `pos` filled: `名詞` (a concrete noun — "granule, grain").

Rebuilt malformed `## Notes` (correct heading level already present, but only two bare unlinked CC-lookup wikilinks with no bullet structure at all) to the standard four-bullet format; `## Words` section was already present and correct. No Derived Characters (nothing names 顆 as its own `graphemic_classification`); no Chengyu hits. Only the existing stand-in [[顆粒]] cites 顆.

**Citing word page [[顆粒]] had one bug fixed**: a redundant duplicate `品詞` field (identical value to `pos`), the same recurring pattern seen repeatedly this session.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 饗 (7332; 913 characters remaining).

### 2026-08-14, iteration 1592 — [[characters/饗|饗]]

`mc_id: 1250` confirmed correct (matches `CC 1000.md` line 263, no off-by-one). **`graphemic_classification: 郷` confirmed correct** (形聲, semantic 食 "food" + phonetic 郷/鄉/鄕, OC \*qʰaŋʔ), via en.Wiktionary; existing simplified alias 飨 reconfirmed correct.

`vietnamese: hưởng` confirmed correct via hvdic (listed under both Âm Hán Việt and Âm Nôm, no contamination). **`japanese` field investigated, no change**: ja.Wiktionary lists an extra go-on コウ not corroborated by Jisho (which shows only キョウ) — excluded, leaving `KYOU` alone. **`japanese_native` gap filled**: the stored bare `う` was a truncated fragment of `う-ける` ("to receive [a feast]") — both ja.Wiktionary and Jisho independently agree on this plus a second kun-yomi, `もてな-す` ("to entertain, treat"); ja.Wiktionary's extra あえ/あい weren't corroborated by Jisho (which classifies them as name-readings, not standard kun'yomi) and were excluded; expanded to a proper hyphenated list.

`korean_native: 잔치할` ("to hold a feast") and `korean: 향` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `kwin: true` consistent (諺文 향 matches korean 향 exactly); `Lookup/Korean/Korean Name ㅎ.md`'s `### 향` subsection already lists 饗 correctly (an earlier grep with a trailing-space pattern mismatch had briefly suggested it was missing — re-checked and confirmed present). `middle_chinese_initial/final: x`/`ɨɐŋ` reconfirmed correct against `聲 曉`/`韻 陽開` (both lookup pages, plus `SKIP-2-13-9`/`Stroke 22`/`Jinmeiyō`, already cited 饗 correctly). Blank `pos` filled: `事詞` (a transitive verb — "to feast, entertain [guests]").

Rebuilt malformed `## Notes` (correct heading level already present, but only two bare unlinked CC-lookup wikilinks with no bullet structure at all) to the standard four-bullet format; `## Words` section was already present and correct. No Derived Characters (nothing names 饗 as its own `graphemic_classification`); no Chengyu hits. Only the existing stand-in [[饗宴]] cites 饗.

**Citing word page [[饗宴]] had one bug fixed**: a redundant duplicate `品詞` field (identical value to `pos`), the same recurring pattern seen repeatedly this session.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 駁 (7333; 912 characters remaining).

### 2026-08-14, iteration 1593 — [[characters/駁|駁]]

`mc_id: 3968` confirmed correct (matches `CC 3000.md` line 1009, no off-by-one). **`graphemic_classification: 爻` confirmed correct** (形聲, semantic 馬 "horse" + phonetic 爻, Zhengzhang whole-character OC \*praːwɢ), via en.Wiktionary — original meaning "dappled, piebald" (of a horse), metaphorically extended to "mixed, contradictory" and hence "to dispute, refute," folded into the rebuilt graphemic bullet. Existing aliases 驳 (simplified) and 駮 (traditional variant) both reconfirmed correct via both sources. **No further alias added**: en.Wiktionary's extra candidates 剝/剥 weren't corroborated by zh.Wiktionary, and 剝 is itself a full independent vault character with its own distinct meaning — excluded per the established "don't alias an independent character" policy.

`vietnamese: bác` confirmed correct via hvdic (listed under both Âm Hán Việt and Âm Nôm, no contamination). `japanese: [BAKU, HAKU]` confirmed correct — both sources agree on both readings (ja.Wiktionary's extra go-on ホク wasn't corroborated by Jisho and was excluded). **`japanese_native` gap filled**: the stored bare `ぶち` was genuine but incomplete — both ja.Wiktionary and Jisho independently agree on two further kun-yomi, `まだら` ("dappled, mottled") and `まじ-る` ("to be mixed"); ja.Wiktionary's extra まざる/いいかえす weren't corroborated by Jisho and were excluded; expanded to a proper hyphenated list.

`korean_native: 논박할` ("to refute") and `korean: 박` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `kwin: true` consistent (諺文 박 matches korean 박 exactly); `Lookup/Korean/Korean Name ㅂ.md`'s `### 박` subsection already lists 駁 correctly. `middle_chinese_initial/final: p`/`ɣʌk` reconfirmed correct against `聲 幫`/`韻 覺` (both lookup pages — the latter's own page independently notes 駁 as the reason a regularly-expected sibling, 剝, is forced to dodge to a different slot — plus `SKIP-1-10-4`/`Stroke 14`/`Hyōgai`, already cited 駁 correctly). Blank `pos` filled: `事詞` (a transitive verb — "to refute, dispute").

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets, no `## Words` section at all) to the standard format, adding the missing stand-in citation (`stand_in: 反駁`). No Derived Characters (nothing names 駁 as its own `graphemic_classification`); no Chengyu hits. Only the existing stand-in [[反駁]] cites 駁.

**Citing word page [[反駁]] had a genuine gap filled**: blank `pos` (empty field, present but unfilled) → `事詞`.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 𥈞 (7335; 911 characters remaining).

### 2026-08-14, iteration 1594 — [[characters/𥈞|𥈞]]

**Major `radical` bug fixed** (`手` → `目`): en.Wiktionary explicitly gives 𥈞's true Kangxi radical as 109 (目, "eye"), not 手 ("hand") as stored — 𥈞 is an "extended shinjitai" form of [[瞞]], whose own semantic component is unambiguously 目 (confirmed independently on 瞞's own en.Wiktionary entry: 形聲, semantic 目 + phonetic 㒼). **`graphemic_classification: 㒼` confirmed correct** (OC \*moːn for the whole character, phonetic 㒼 glossed "to cover carefully and tightly, without a break" — folded into the rebuilt graphemic bullet). **Two cascading missing-entry bugs fixed as a direct consequence of the radical correction**: 𥈞 was wrongly listed under `Lookup/Radicals/Radical 064.md` (手, entry #109) instead of `Lookup/Radicals/Radical 109.md` (目) — removed from the wrong page (renumbering all 28 subsequent entries down by one via a small script to avoid leaving a numbering gap, `size: 137` → `136`) and added to the correct page's `+9 Strokes` section as entry #21 (`size: 27` → `28`).

`mc_id: 5114` confirmed as legitimate long-tail data (not found in `CC 0000`–`CC 3000.md`, above the checklist's trusted-verbatim threshold). **Major `vietnamese` gap filled**: hvdic's entry for 𥈞 lists two genuine Hán Việt readings, `man` and `môn`, but only `man` was stored — added the missing `môn`. **Malformed `japanese_native` field fixed**: the stored value was a single raw string with a stray leading space and comma-separated entries (`" だます ,あざむく ,かたる"`) instead of a proper YAML list — cross-referencing ja.Wiktionary (だま-す, あざむ-く) against Jisho (だます corroborated via compound, あざむく/かたる not present as kun'yomi at all) left only `だま-す` as doubly-corroborated; corrected to a clean single-item hyphenated value. **`japanese` gap filled**: ja.Wiktionary (Goon マン, Kan-on バン) and Jisho (マン, モン, バン, ボン all listed) both corroborate `BAN` alongside the already-stored `MAN` — added.

`korean_native: 속일` ("to deceive") and `korean: 만` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `kwin: true` consistent (諺文 만 matches korean 만 exactly); `Lookup/Korean/Korean Name ㅁ.md`'s `### 만` subsection already lists 𥈞 correctly (via its own alias 瞞). `middle_chinese_initial/final: m`/`uɑn` reconfirmed correct against `聲 明`/`韻 桓` (both lookup pages — the latter's own page independently documents 𥈞 as one of six m-initial characters dodged by 㒼's own coda shift — plus `SKIP-1-5-9`/`Stroke 14`/`Old HSK 3`, already cited 𥈞 correctly). `joyo_level: 表外字` confirmed correct — `lookup/Japanese/Hyōgai.md` already carries the necessary redirect entry (`瞞 --> 𥈞`), the vault's established convention for shinjitai-variant characters, so no missing-entry fix was needed there. `pos: 事詞` (already filled) confirmed appropriate — no change.

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets) to the standard format; `## Words` section was already present and correct. No Derived Characters (nothing names 𥈞 as its own `graphemic_classification`); no Chengyu hits. Only the existing stand-in [[欺瞞]] (also aliased as 欺𥈞/欺瞒) cites 𥈞.

**Citing word page [[欺瞞]] reviewed, no bugs found**: already perfected (2026-06-13), with a detailed Notes section already explaining the shared-alias mechanism between 𥈞 and 瞞/瞒 in depth — left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 佇 (7337; 910 characters remaining).

### 2026-08-14, iteration 1595 — [[characters/佇|佇]]

`mc_id: 5581` confirmed as legitimate long-tail data (佇 not found anywhere in `CC 0000`–`CC 3000.md`, above the checklist's trusted-verbatim threshold). **`graphemic_classification: 宁` confirmed correct** (形聲, semantic 人 "person" + phonetic 宁, Zhengzhang whole-character OC \*daʔ), via en.Wiktionary. **New variant alias added**: 竚, confirmed genuine via both en.Wiktionary's and zh.Wiktionary's independent variant lists; en.Wiktionary's further candidates 貯/贮/在/置 weren't corroborated by zh.Wiktionary and, more importantly, are all independent characters with their own distinct meanings already in the vault — excluded per the established alias-exclusion policy; existing simplified alias 伫 reconfirmed correct.

**`vietnamese` contamination fixed**: the stored `[giữ, trữ]` mixed one genuine Hán Việt reading with a Nôm-only form — hvdic's actual entry lists only `trữ` under Âm Hán Việt, filing `giữ` under Âm Nôm only — trimmed accordingly. **`japanese` field investigated, no change**: ja.Wiktionary lists an extra go-on ジョ not corroborated by Jisho (which shows only チョ) — excluded, leaving `CHO` alone. **`japanese_native` bug fixed**: bare unhyphenated `たたず` corrected to properly hyphenated `たたず-む` ("to stand still, loiter"), confirmed via both sources.

**Blank `korean_native` bug fixed**: a Korean-language web search confirms 佇's real 훈음 is "우두커니 설" ("to stand blankly/vacantly") — filled, matching the vault's established multi-word gloss format (space-separated, e.g. [[characters/䋇 (char)|䋇]]'s `실 뽑을`). `korean: 저` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㅈ.md`'s `### 저` subsection already lists 佇 correctly. `middle_chinese_initial/final: ɖ`/`ɨʌ` reconfirmed correct against `聲 澄`/`韻 魚` (both lookup pages — the latter's own page independently documents 佇 as sharing a homophony-overflow slot with 儲, one of several ordinary singleton escapes noted on that page — plus `SKIP-1-2-5`/`Stroke 07`/`Hyōgai`, already cited 佇 correctly). Blank `pos` filled: `事詞` (an intransitive verb — "to stand waiting, stand still"), matching the citing word page's own already-correct classification.

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets) to the standard format; `## Words` section was already present and correct. No Derived Characters (nothing names 佇 as its own `graphemic_classification`); no Chengyu hits. Only the existing stand-in [[佇立]] cites 佇.

**Citing word page [[佇立]] reviewed, no bugs found**: already perfected (2026-08-03), with its own detailed prose already explaining a compositional (non-idiomatic) `vietnamese: trữ lập` derivation — left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 侏 (7338; 909 characters remaining).

### 2026-08-14, iteration 1596 — [[characters/侏|侏]]

**`mc_id` off-by-one bug fixed** (3346 → 3347; confirmed against `CC 3000.md` line 363-364, where "3346. 瑣" precedes "3347. 侏"). **`graphemic_classification: 朱` confirmed correct** (形聲, semantic 人 "person" + phonetic 朱, Zhengzhang whole-character OC \*tjo), via en.Wiktionary; no variant forms found on either source.

**`vietnamese` gap filled**: hvdic's entry for 侏 lists two genuine Âm Hán Việt readings, `chu` and `thù`, but only `thù` was stored — added the missing `chu`. **`japanese` bug fixed**: the stored `CHU` was corroborated by neither ja.Wiktionary (which lists only go-on ス/kan-on シュ, no CHU) nor Jisho (シュ only) — dropped as an unsupported reading, leaving `SHU` alone. `japanese_native: ø` (no kun-yomi) confirmed correct on closer inspection: ja.Wiktionary lists two candidate kun-yomi (みじか-い, あざむ-く) but neither is corroborated by Jisho (which shows no kun'yomi at all for this character) — per this session's established cross-reference policy, uncorroborated candidates don't clear the bar, so the existing `ø` sentinel stands as correctly verified rather than a gap.

`korean_native: 난쟁이` ("dwarf") and `korean: 주` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `kwin: true` consistent (諺文 주 matches korean 주 exactly); `Lookup/Korean/Korean Name ㅈ.md`'s `### 주` subsection already lists 侏 correctly. `middle_chinese_initial/final: t͡ɕ`/`ɨo` reconfirmed correct against `聲 章`/`韻 虞` (both lookup pages — the latter's own page independently documents 侏 as one of 11 members in the single most crowded slot found across its entire sweep, ㄐㄨ — plus `SKIP-1-2-6`/`Stroke 08`, already cited 侏 correctly). **Blank `joyo_level` was already correctly `表外字`, but the corresponding missing-entry bug was fixed**: 侏 was entirely absent from `lookup/Japanese/Hyōgai.md` — added as entry #315. Blank `pos` filled: `名詞` (a concrete noun — "dwarf").

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets, no `## Words` section) to the standard format, adding the missing stand-in citation (`stand_in: 侏儒`). No Derived Characters (nothing names 侏 as its own `graphemic_classification`); no Chengyu hits. Only the existing stand-in [[侏儒]] cites 侏.

**Citing word page [[侏儒]] reviewed**: `pos: 名詞` was already correctly filled (not blank, contrary to an initial misreading during this iteration — a stray blank line was briefly introduced by that misreading and immediately corrected); `vietnamese: [chu, nhu]` independently verified against hvdic's own attested compound reading "chu nhu" and confirmed genuine, not a compositional guess — left otherwise untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 倭 (7339; 908 characters remaining).

### 2026-08-14, iteration 1597 — [[characters/倭|倭]]

`mc_id: 4239` confirmed as legitimate long-tail data (倭 not found anywhere in `CC 0000`–`CC 3000.md`, above the checklist's trusted-verbatim threshold). **`graphemic_classification: 委` confirmed correct** (形聲, semantic 人 "person" + phonetic 委, Zhengzhang whole-character OC \*qoːl/\*qrol/\*qoːlʔ), via en.Wiktionary — its extra note about 和 replacing 倭 as Japan's self-designation after ~757 CE is a national-name substitution, not a graphemic variant, and was correctly left unadded as an alias.

**`vietnamese` field investigated at length, ultimately reconfirmed correct**: an initial hvdic query returned an apparently contradictory/garbled summary suggesting all four stored readings (nuỵ, oa, oải, uy) were Nôm-only contamination with zero genuine Hán Việt readings — a claim serious enough to warrant re-verification rather than acting on immediately, especially since it would have been the first character this session with *no* attested Hán Việt reading at all. Three further, progressively more careful re-queries of the same page converged on the opposite, correct picture: 倭 is a genuine polyphonic character with four separate reading-entries on hvdic (not four alternate spellings of one sense), and all four — nuỵ, oa, oải, uy — are independently labeled Âm Hán Việt for their own senses (the first three all covering "dwarf/Japan," the fourth a distinct "distant" sense). No change made; flagging the investigation process itself since it's a useful precedent for treating an unusually clean-looking "zero genuine readings" result with extra scrutiny before trusting it.

**`japanese` field reconfirmed correct**: both `I` and `WA` are corroborated by both ja.Wiktionary and Jisho. **`japanese_native` gap filled**: the stored `やまと` was genuine but incomplete — both sources independently agree on a second kun-yomi, `したが-う` ("to obey, follow"); added, properly hyphenated.

`korean_native: 왜나라` ("the land of Wa/Japan") and `korean: 왜` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㅇ.md`'s `### 왜` subsection already lists 倭 correctly. `middle_chinese_initial/final: ʔ`/`ɣiuᴇ` reconfirmed correct against `聲 影`/`韻 支B三合` (both lookup pages — the latter's own page independently documents 倭 as one of 9 members in the project's single most crowded same-final slot, ⼔ㄧ — plus `SKIP-1-2-8`/`Stroke 10`/`Jinmeiyō`, already cited 倭 correctly). Blank `pos` filled: `名詞` (a concrete/proper noun — historically "Japan/the Japanese," and by extension "dwarf").

Rebuilt malformed `## Notes` (correct heading level already present, but only two bare unlinked CC-lookup wikilinks with no bullet structure at all) to the standard four-bullet format; `## Words` section was already present and correct. No Derived Characters (nothing names 倭 as its own `graphemic_classification`); no Chengyu hits. One grep hit on another word page ([[黒猩]]) confirmed a false positive — cites 黒/猩, not 倭, in its own `characters:` field; the two genuine citing stand-ins [[倭人]] and [[倭猩]] were already both correctly listed.

**Both citing word pages reviewed, no bugs found**: [[倭人]] and [[倭猩]] are both already perfected, with real (non-`null`) values and no duplicate `品詞` fields — left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 僵 (7340; 907 characters remaining).

### 2026-08-14, iteration 1598 — [[characters/僵|僵]]

**`mc_id` off-by-one bug fixed** (2585 → 2586; confirmed against `CC 2000.md` line 610-611, where "2585. 裝" precedes "2586. 僵"). **`graphemic_classification: 畺` confirmed correct** (形聲, semantic 人 "person" + phonetic 畺, Zhengzhang whole-character OC \*kaŋ), via en.Wiktionary, independently corroborated by zh.Wiktionary's own 系列#0833（畺）phonetic-family grouping. **New variant alias added**: 殭, confirmed genuine via both en.Wiktionary's and zh.Wiktionary's independent variant lists.

**Major `english` bug fixed**: the stored gloss `stuff corpse` was a typo for `stiff corpse` — verified via en.Wiktionary, whose full definition confirms the character's true core meaning is "stiff, rigid" (extending metaphorically to "motionless, stupefied"), not any sense involving "stuff." Corrected the `english` field to `[stiff, rigid]` (a clean adjectival gloss for the character itself, distinct from the citing compound's own "corpse, zombie" sense); the identical typo had also propagated into the citing word page [[僵屍]]'s own prose ("stuff corpse, stiffen") and was fixed there too.

**`vietnamese` gap filled**: hvdic's entry for 僵 lists two genuine Âm Hán Việt readings, `cương` and `thương`, but only `cương` was stored — added the missing `thương`. **`japanese` field investigated, no change**: ja.Wiktionary lists an extra go-on コウ not corroborated by Jisho (which shows only キョウ) — excluded, leaving `KYOU` alone. **`japanese_native` bug fixed**: bare unhyphenated `たお` corrected to properly hyphenated `たお-れる` ("to fall over, collapse"), confirmed via both sources.

`korean_native: 넘어질` ("to fall over") and `korean: 강` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial). `middle_chinese_initial/final: k`/`ɨɐŋ` reconfirmed correct against `聲 見`/`韻 陽開` (both lookup pages — the latter's own page independently notes 僵 as one of only two members (alongside 強) in a small crowded ⼘ㄫ slot that two other characters, 疆/姜, are forced to dodge via coda-shift — plus `SKIP-1-2-13`/`Stroke 15`/`Old HSK 3`, already cited 僵 correctly). `hanmun_edu_level: 無` confirmed correct as-is (`lookup/Korean/Korean Missing.md` is a pure dataview auto-query, no manual list to update). **Missing-entry bug fixed**: `joyo_level: 表外字` was already correctly set, but 僵 was entirely absent from `lookup/Japanese/Hyōgai.md` — added as entry #316. Blank `pos` filled: `性詞` (a stative/adjectival quality — "stiff, rigid").

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets) to the standard format; `## Words` section was already present and correct. No Derived Characters (nothing names 僵 as its own `graphemic_classification`); no Chengyu hits. Only the existing stand-in [[僵屍]] cites 僵.

**Citing word page [[僵屍]] had one bug fixed**: the same "stuff corpse" typo propagated from the character page's own English gloss, corrected to "stiff, rigid" in its own Notes prose; other fields (`vietnamese: cương thi`, `pos: 名詞`, no duplicate `品詞`) already correct, left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 僻 (7341; 906 characters remaining).

### 2026-08-14, iteration 1599 — [[characters/僻|僻]]

**`mc_id` off-by-one bug fixed** (2021 → 2022; confirmed against `CC 2000.md` line 26-27, where "2021. 婚" precedes "2022. 僻"). **`graphemic_classification: 辟` confirmed correct** (形聲, semantic 人 "person" + phonetic 辟, Zhengzhang whole-character OC \*pʰeɡ/\*pʰeːɡ), via en.Wiktionary. **No alias added**: en.Wiktionary's extra candidates 𠈳/𠒱 weren't corroborated by zh.Wiktionary (which lists no variants at all), and its third candidate, 辟, is itself already an independent vault character — excluded.

**`vietnamese` gap filled**: hvdic's entry for 僻 lists two genuine Âm Hán Việt readings, `tích` and `tịch`, but only `tịch` was stored — added the missing `tích` (this required careful re-verification: an initial imprecise WebFetch summary falsely claimed `tịch` was Nôm-only, but a follow-up exact-transcription query confirmed both readings genuinely appear under Âm Hán Việt, the same "listed in both categories" pattern seen elsewhere, not contamination — the same caution pattern applied on [[characters/倭|倭]] two iterations ago).

**Major `japanese` and `japanese_native` bugs fixed**: cross-referencing ja.Wiktionary (Goon ヒ/ヒャク, Kan'on ヒ/ヘキ, kun'yomi ひが-む only) against Jisho (on'yomi ヘキ/ヒ/ヘイ, kun'yomi へき-する/ひが-む) — `HEI` was corroborated only by Jisho and was dropped per this session's established policy; the stored `japanese_native: へき` was a genuine bug, not a real reading at all in either source on its own (Jisho's only へき-adjacent form is the suru-verb へき-する, itself uncorroborated by ja.Wiktionary) — corrected to the one kun-yomi both sources agree on, `ひが-む` ("to be biased, warped").

`korean_native: 궁벽할` ("remote, out-of-the-way") and `korean: 벽` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㅂ.md`'s `### 벽` subsection already lists 僻 correctly. `middle_chinese_initial/final: pʰ`/`iᴇk` reconfirmed correct against `聲 滂`/`韻 昔開` (both lookup pages — the latter's own page independently documents 僻's own final as an unusual "double-shift" escape case, borrowing the aspirated ㄆ letter as if from a pʰ-initial despite its true b-initial ancestry — plus `SKIP-1-2-13`/`Stroke 15`/`Hyōgai`/`Old HSK 4`, already cited 僻 correctly). Blank `pos` filled: `性詞` (a stative/adjectival quality — "remote, far away").

Rebuilt malformed `## Notes` (correct heading level already present, but only two bare unlinked CC-lookup wikilinks with no bullet structure at all) to the standard four-bullet format; `## Words` section was already present and correct. No Derived Characters (nothing names 僻 as its own `graphemic_classification`); no Chengyu hits. Only the existing stand-in [[窮僻]] cites 僻.

**Citing word page [[窮僻]] reviewed, no bugs found**: already perfected (2026-06-03), `pos: 性詞` filled with no duplicate `品詞` field — left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 冕 (7342; 905 characters remaining).

### 2026-08-14, iteration 1600 — [[characters/冕|冕]]

**`mc_id` off-by-one bug fixed** (1843 → 1844; confirmed against `CC 1000.md` line 880-881, where "1843. 鴈" precedes "1844. 冕"). **`graphemic_classification: 免` confirmed correct** (形聲, semantic 冂 + phonetic 免, Zhengzhang whole-character OC \*mronʔ), via en.Wiktionary.

**Major `radical` bug fixed** (`冖` → `冂`): en.Wiktionary explicitly gives 冕's true Kangxi radical as 13 (冂, "enclosure/open frontier"), not 14 (冖, "cover") as stored — these are two visually similar but genuinely distinct radicals, and the vault's own `Lookup/Radicals/Radical 013.md` page's own prose independently confirms 冂 covers "characters relating to enclosure... and things bound or wrapped," a better semantic fit for a crown than the "cloth draped over something" gloss on Radical 014's own page. **Three cascading missing/wrong-entry bugs fixed as a direct consequence**: 冕 was wrongly listed under `Lookup/Radicals/Radical 014.md` (冖, entry #8 of 9) — removed and the remaining entries renumbered/shifted (`size: 9` → `8`); added to the correct `Lookup/Radicals/Radical 013.md` page instead (`size: 5` → `6`); and `Lookup/Radicals/Radicals.md`'s own summary line counts for both radicals corrected to match (013: 5→6 characters; 014: 9→8 characters).

**`vietnamese` contamination fixed**: hvdic's actual entry for 冕 lists only `miện` under Âm Hán Việt, filing the stored second entry `mịn` under Âm Nôm only — removed (this required an exact-transcription re-query per the now-established practice of not trusting an imprecise first-pass summary). `japanese: [BEN, MEN]` and `japanese_native: かんむり` both confirmed correct via both sources, no changes. **Blank `joyo_level` filled**: `表外字` — confirmed via a Japanese-language web search explicitly classifying 冕 as 表外漢字 (not 常用 or 人名用) — **missing-entry bug fixed accordingly**, adding 冕 to `lookup/Japanese/Hyōgai.md` as entry #317.

`korean_native: 면류관` ("ceremonial crown") and `korean: 면` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `kwin: true` consistent (諺文 면 matches korean 면 exactly); `Lookup/Korean/Korean Name ㅁ.md`'s `### 면` subsection already lists 冕 correctly. `middle_chinese_initial/final: m`/`ɣiᴇn` reconfirmed correct against `聲 明`/`韻 仙B三開` (both lookup pages, plus `SKIP-2-2-9`/`Stroke 11`/`HSK No`, already cited 冕 correctly). Blank `pos` filled: `名詞` (a concrete noun — "crown").

Rebuilt malformed `## Notes` (correct heading level already present, but only two bare unlinked CC-lookup wikilinks with no bullet structure at all) to the standard four-bullet format; `## Words` section was already present and correct. No Derived Characters (nothing names 冕 as its own `graphemic_classification`); no Chengyu hits. Only the existing stand-in [[冠冕]] cites 冕.

**Citing word page [[冠冕]] reviewed, no bugs found**: already perfected (2026-06-03), `pos: 名詞` filled with no duplicate `品詞` field — left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 剃 (char) (7343; 904 characters remaining).

### 2026-08-14, iteration 1601 — [[characters/剃 (char)|剃]]

`mc_id: 7175` confirmed as legitimate long-tail data (剃 not found anywhere in `CC 0000`–`CC 3000.md`, above the checklist's trusted-verbatim threshold). **`graphemic_classification: 弟` confirmed correct** (形聲, semantic 刀/刂 "knife" + phonetic 弟, OC \*tʰiːls, "possibly a post-Han variant of [[剔]]"), via en.Wiktionary, independently corroborated by the citing word page [[剃]]'s own pre-existing prose ("剃 combines [[刀]] with phonetic [[弟]]").

**Severe cascading `aliases` bug found and fixed, with two further downstream bugs traced and corrected**: the stored alias `涕` is explicitly and unambiguously confirmed by en.Wiktionary as *not* a variant of 剃 at all — it's a phonetic-family sibling (sharing the same phonetic 弟) with its own completely distinct primary meaning, "tears," not corroborated by zh.Wiktionary either. This single wrong alias had visibly contaminated the character's own frontmatter (`korean_native: 눈물` — literally "tears" in Korean, obviously borrowed from 涕's own meaning rather than 剃's "shave") and had propagated into two shared lookup pages: `Lookup/Korean/Korean Name ㅊ.md`'s `### 체` subsection carried a bogus `[涕](...剃 (char).md)` entry (removed), and `lookup/HSK/Old HSK 4.md`'s frequency list carried a duplicate bogus `[涕](...剃 (char).md): 1` line alongside the already-correct direct `[[剃 (char)]]: 1` entry (removed). Replaced the alias field with the two variants both en.Wiktionary and zh.Wiktionary genuinely agree on, `鬀` and `鬄` (en.Wiktionary's further 𩮜/薙 candidates and zh.Wiktionary's own 剔 candidate weren't cross-corroborated — 剔 in particular is itself a wholly separate independent character, mentioned only as an etymological ancestor, not a true variant, and was correctly left unadded).

**Blank `korean_native` bug fixed** (having been overwritten by the 涕 contamination): a Korean-language web search gives 剃's real 훈음 as "머리 깎을 체" ("to shave the head") — filled `머리 깎을`, matching the vault's established multi-word gloss convention. **Major `japanese_native` bug fixed**: the stored `まい` turned out to be a real but singly-corroborated reading (Jisho only, not ja.Wiktionary) — dropped per this session's established cross-reference policy, replaced with the two kun-yomi both sources agree on, `そ-る` ("to shave") and `す-る` (a homograph-adjacent verb form), both properly hyphenated. `japanese: TEI` confirmed correct as the sole doubly-corroborated on-yomi (ja.Wiktionary's extra go-on タイ wasn't corroborated by Jisho and was excluded).

**`vietnamese` contamination fixed**: hvdic's actual entry for 剃 lists only `thế` under Âm Hán Việt, filing the stored second entry `thí` under Âm Nôm only — removed (independently corroborated by the citing word page's own prose, which already only ever discusses `thế`, never `thí`). `korean: 체` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㅊ.md`'s `### 체` subsection (once cleaned of the bogus 涕 entry) still correctly lists 剃 itself. `middle_chinese_initial/final: tʰ`/`ei` reconfirmed correct against `聲 透`/`韻 齊開` (both lookup pages — the latter's own page independently documents 剃 as part of an unusually large 14-member combined dental-stop cohort on this final — plus `SKIP-1-7-2`/`Stroke 09`/`Hyōgai`/`Old HSK 4`, already cited 剃 correctly). **A broken relative link and stray trailing whitespace on `lookup/Japanese/Hyōgai.md`'s pre-existing entry #195 were also fixed** (missing `../../` prefix, the same recurring broken-path pattern seen throughout this project). Blank `pos` filled: `事詞` (a transitive verb — "to shave [something]").

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets, no `## Words` section) to the standard format, adding the missing self stand-in citation (`stand_in: 剃`). No Derived Characters (nothing names 剃 as its own `graphemic_classification`); no Chengyu hits. Only the existing self stand-in [[剃]] cites 剃.

**Citing word page [[剃]] left otherwise untouched**: already independently perfected (2026-07-26) with rich prose explicitly corroborating the graphemic bullet and the genuine `vietnamese: thế` reading, plus its own already-correct `pos: 動詞` (an accepted convention value per the checklist, not a bug) — its existing three-way homophone callout with [[締]] and [[諦]] is intentionally one-directional pending their own future turns in this sweep, per its own stated design.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 喧 (7344; 903 characters remaining).

### 2026-08-14, iteration 1602 — [[characters/喧|喧]]

`mc_id: 4323` confirmed as legitimate long-tail data (喧 not found anywhere in `CC 0000`–`CC 3000.md`, above the checklist's trusted-verbatim threshold). **`graphemic_classification: 宣` confirmed correct** (形聲, semantic 口 "mouth" + phonetic 宣, Zhengzhang whole-character OC \*qʰʷan), via en.Wiktionary. **New variant alias added**: 吅, confirmed genuine via both en.Wiktionary's and zh.Wiktionary's independent variant lists; zh.Wiktionary's further candidates 諠/咺 weren't corroborated by en.Wiktionary and were excluded.

**`stand_in` bug fixed** (`喧喿` → `喧嘩`): the stored compound 喧喿 doesn't exist anywhere in the vault as a word file, and a web search found no evidence it's an attested Chinese word at all (only tangentially-related terms like 喧嘩/喧譁/喧闐 surfaced, all built on different second characters) — meanwhile [[喧嘩]] is a real, well-attested, already-perfected word (2026-08-04) that genuinely cites 喧 as a constituent and was already correctly listed in `## Words`. Corrected the `stand_in` field to point at the real compound rather than an apparently fictitious one.

`vietnamese: huyên` confirmed correct via hvdic, no contamination. `japanese: KEN` confirmed correct as the sole doubly-corroborated on-yomi (ja.Wiktionary's extra go-on コン wasn't corroborated by Jisho and was excluded). **`japanese_native` gap filled**: the stored bare `やかま` was a truncated fragment — both sources independently agree on two full kun-yomi, `やかまし-い` ("noisy") and `かまびすし-い` ("clamorous"); expanded to a proper hyphenated list.

`korean_native: 지껄일` ("to clamor, chatter") and `korean: 훤` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㅎ.md`'s `### 훤` subsection already lists 喧 correctly. `middle_chinese_initial/final: x`/`ʉɐn` reconfirmed correct against `聲 曉`/`韻 元合` (both lookup pages — the latter's own page independently notes 喧 as a lone-member ㄏㄛㄋ slot that a would-be same-final sibling, 亘, is forced to dodge via a w-glide addition — plus `SKIP-1-3-9`/`Stroke 12`/`Jinmeiyō`, already cited 喧 correctly). **Blank `hsk_level` bug fixed**: no `lookup/HSK/*.md` file cites 喧 anywhere — filled `無`. Blank `pos` filled: `性詞` (a stative/adjectival quality — "noisy, clamorous").

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets) to the standard format; `## Words` section was already present and correct (citing the now-corrected stand-in [[喧嘩]]). No Derived Characters (nothing names 喧 as its own `graphemic_classification`); no Chengyu hits.

**Citing word page [[喧嘩]] reviewed, no bugs found**: already perfected (2026-08-04), with rich comparative prose across all five languages already in place — left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 呕 (7345; 902 characters remaining).

### 2026-08-14, iteration 1603 — [[characters/呕|呕]]

**`mc_id` off-by-one bug fixed** (1913 → 1914; confirmed against `CC 1000.md` line 954-955, where "1913. 芳" precedes "1914. 嘔"). **`graphemic_classification: 区` confirmed correct** (形聲, semantic 口 "mouth" + phonetic 區/区, Zhengzhang whole-character OC \*qoːʔ — a distinct etymology from the character's rarer "sing/hum" sense, \*qoː), via en.Wiktionary. Fixed a broken link within the rebuilt graphemic bullet itself (phonetic component page is `characters/区.md`, not `区 (char).md`).

**`aliases` field carefully re-verified, one entry removed**: the stored `歐` is genuinely confirmed by en.Wiktionary as the historical "original form" specifically of 呕/嘔's *vomiting* sense — but investigation revealed this exact character is *already* independently claimed as an alias on a separate, pre-existing vault page, [[𧦅]] (danayo_id 7336, "eulogize, praise"), whose own alias list (謳/赞/讴/歐/欧, set 2026-02-01) represents this vault's own established prior decision about which character owns 歐/欧 — and `Lookup/Korean/Korean Name ㄱ.md`'s own `### 구` subsection already links 歐 to 𧦅's page, not 呕's, consistently with that decision. Rather than re-litigating an existing cross-character assignment as a side effect of this iteration, left 歐 off 呕's own alias list to avoid creating a genuine ownership conflict between two vault pages — flagging this as a real ambiguity worth a dedicated future look, not a settled call. **New alias added**: 㰶, confirmed genuine via both en.Wiktionary and zh.Wiktionary; existing alias 嘔 (already correctly cited elsewhere) and the previously-stored 𠴰 (uncorroborated by zh.Wiktionary, removed) were both re-verified.

**Major `vietnamese` gap filled**: hvdic's entry for 呕/嘔 lists three genuine Âm Hán Việt readings — `hú`, `âu`, `ẩu` — but only `ẩu` was stored; added the two missing readings. **Major `japanese`/`japanese_native` bugs fixed**: cross-referencing ja.Wiktionary (Goon ウ/ク, Kan'on オウ/ク; kun-yomi は-く/むかつ-く/うた-う) against Jisho (on'yomi オウ/ク only, no ウ; same three kun'yomi) — `U` was corroborated only by ja.Wiktionary and was dropped; the missing `KU` (corroborated by both) was added. The stored `japanese_native: うたう` was genuine but severely incomplete and unhyphenated — both sources agree on three kun-yomi covering both of the character's senses, `は-く`/`むかつ-く` (vomit, nausea) and `うた-う` (sing, the character's rarer secondary sense) — expanded to a proper hyphenated list rather than dropping the "sing" reading as an apparent mismatch, since it's genuinely attested for this exact polysemous character.

`korean_native: 게울` ("to vomit/regurgitate") and `korean: 구` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `Lookup/Korean/Korean Name ㄱ.md`'s `### 구` subsection already lists 呕 (via alias 嘔) correctly. `middle_chinese_initial/final: ʔ`/`əu` reconfirmed correct against `聲 影`/`韻 侯` (both lookup pages, plus `SKIP-1-3-11`/`Stroke 14`/`Old HSK 4`, already cited 呕 correctly); `joyo_level: 表外字` also already correctly supported by `lookup/Japanese/Hyōgai.md`'s existing `嘔-->呕` redirect entry. `pos: 性詞` (already filled) confirmed appropriate — no change.

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets) to the standard format; `## Words` section was already present and correct. No Derived Characters (nothing names 呕 as its own `graphemic_classification`); no Chengyu hits. Only the existing stand-in [[呕吐]] cites 呕.

**Citing word page [[呕吐]] reviewed, no bugs found**: already perfected (2026-08-04), with its own detailed prose already documenting a prior content-bug fix on this exact character pair — left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 嘩 (7346; 901 characters remaining).

### 2026-08-14, iteration 1604 — [[characters/嘩|嘩]]

`mc_id: 5368` confirmed as legitimate long-tail data (嘩 not found anywhere in `CC 0000`–`CC 3000.md`, above the checklist's trusted-verbatim threshold). **`graphemic_classification: 華` confirmed correct** (形聲, semantic 口 "mouth" + phonetic 華, Zhengzhang whole-character OC \*ɡʷraː), via en.Wiktionary. **New variant alias added**: 譁, confirmed genuine via both en.Wiktionary and zh.Wiktionary (explicitly given as the primary traditional-form pairing, "正體/繁體: 嘩/譁"); existing simplified alias 哗 reconfirmed correct.

**`stand_in` field investigated and reconfirmed correct, unlike the near-identical case on [[characters/喧|喧]] one iteration ago**: no word file for 嘩然 exists in the vault yet, initially raising the same suspicion as 喧's own bogus 喧喿 stand-in — but a web search this time confirms 嘩然 (huárán) *is* a genuinely attested classical/modern Chinese term ("an uproar; to cause a sensation, widely discussed"), unlike 喧喿, which had no attestation anywhere. Left `stand_in: 嘩然` unchanged as a real but not-yet-created word, a genuine gap for the word-sweep rather than a data bug to fix here — while still adding the character's actual existing citing word, [[喧嘩]] (already perfected, genuinely citing 嘩 as a constituent), to `## Words` per the checklist's completeness requirement.

`vietnamese: hoa` confirmed correct via hvdic, no contamination. **`japanese` field reconfirmed correct**: both `KA` and `KE` are doubly corroborated by ja.Wiktionary and Jisho. **`japanese_native` bug fixed**: bare unhyphenated `かまびす` corrected to properly hyphenated `かまびす-しい` ("clamorous, noisy"), confirmed via both sources.

`korean_native: 떠들썩할` ("noisy, boisterous") and `korean: 화` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `kwin: true` consistent (諺文 화 matches korean 화 exactly). `middle_chinese_initial/final: x`/`ɣua` reconfirmed correct against `聲 曉`/`韻 麻二合` (both lookup pages, plus `SKIP-1-3-12`/`Stroke 15`/`Jinmeiyō`/`Old HSK 3`, already cited 嘩 correctly). **Blank `hanmun_edu_level` bug fixed**: no `Lookup/Korean/*.md` file cites 嘩 anywhere — filled `無` (`lookup/Korean/Korean Missing.md` being a pure dataview auto-query, no manual list entry needed). Blank `pos` filled: `性詞` (a stative/adjectival quality — "clamorous, noisy").

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets, no `## Words` section) to the standard format. No Derived Characters (nothing names 嘩 as its own `graphemic_classification`); no Chengyu hits.

**Citing word page [[喧嘩]] reviewed, no bugs found**: already perfected (2026-08-04) — left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 嚢 (7347; 900 characters remaining).

### 2026-08-14, iteration 1605 — [[characters/嚢|嚢]]

`mc_id: 1833` confirmed correct (matches `CC 1000.md` line 870, no off-by-one). **`graphemic_classification: 襄` confirmed correct** (originally 會意 — a depiction of a tied bag — later reanalyzed as 形聲 with an abbreviated 㯻 "bag" semantic element + abbreviated phonetic 襄, Zhengzhang whole-character OC \*naːŋ), via en.Wiktionary; the graphemic bullet's phonetic-component link was corrected from an earlier draft that conflated the semantic "bag" element with the character's own Kangxi radical (口) — they coincide only by indexing accident, the same pattern flagged on [[characters/碩|碩]] much earlier in this sweep.

**`aliases` bug fixed**: the stored `曩` and `㶞` were both explicitly identified by zh.Wiktionary as *not* genuine variants of 囊/嚢 — 曩 is a distinct character with an unrelated meaning ("formerly, in the past"), only sharing the same 襄 phonetic ancestry, and 㶞 wasn't corroborated by either source at all — both removed, keeping only the existing, doubly-confirmed simplified-form alias 囊.

**`vietnamese` gap filled**: hvdic gives the sole genuine Hán Việt reading `nang` — the field was entirely blank; filled. **`japanese` gap filled**: both ja.Wiktionary and Jisho independently agree on two on-yomi, ノウ and ドウ — the stored `[NOU]` was missing the corroborated `DOU`; added. `japanese_native: ふくろ` confirmed correct via both sources (a bare nominal gloss, no hyphenation needed).

`korean_native: 주머니` ("pocket, pouch") and `korean: 낭` reconfirmed correct (no 두음법칙 concern, not ㄹ/ㄴ-initial); `kwin: true` consistent (諺文 낭 matches korean 낭 exactly); `Lookup/Korean/Korean Name ㄴ.md`'s `### 낭` subsection already lists 嚢 correctly (via alias 囊). `middle_chinese_initial/final: n`/`ɑŋ` reconfirmed correct against `聲 泥`/`韻 唐開` (both lookup pages, plus `SKIP-2-7-11`/`Stroke 18`/`Hyōgai`, already cited 嚢 correctly). `hsk_level: 無` (already filled) reconfirmed correct against `lookup/HSK/HSK No.md`'s own direct citation — a second, seemingly-contradictory appearance on `lookup/HSK/Old HSK 4.md` (with a bare frequency count, `: 2`) was investigated and determined to be that file's own separate "appears N times within HSK4-level compound vocabulary" tracking mechanism, not a competing claim about the standalone character's own level, consistent with the same pattern seen on several other characters' Old-HSK-N citations earlier this session — no fix needed. `pos: 名詞` (already filled) confirmed appropriate — no change.

Rebuilt malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks with no other bullets) to the standard format; `## Words` section was already present and correct. No Derived Characters (nothing names 嚢 as its own `graphemic_classification`); no Chengyu hits. Only the existing stand-in [[胆嚢]] cites 嚢.

**Citing word page [[胆嚢]] left otherwise untouched**: `pos: 名詞` already filled; its blank `vietnamese`/`hsk_level` are genuine never-perfected gaps — a direct hvdic lookup for the compound 胆嚢 returned no attested result, so there was no directly-evidenced answer in hand; left for the word-sweep.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 垢 (7349; 899 characters remaining).

### 2026-08-14, iteration 1606 — [[characters/垢|垢]]

**`mc_id` off-by-one fixed**: stored `2491` (which actually names 蓍 in `CC 2000.md`); the real line for 垢 is `2492`. **`pos` gap filled**: was entirely blank; both English glosses ("dirt", "filth") are concretely nominal, set to `名詞`. **`graphemic_classification: 后` reconfirmed correct** (形聲: semantic [[Radical 032|土]] "earth" + phonetic 后, Zhengzhang OC \*koːʔ from phonetic \*ɡoːʔ/\*ɡoːs) via en.Wiktionary and zh.Wiktionary agreement.

**`aliases` gap filled**: both sources list variant forms for 垢 — en.Wiktionary gives 坸 and 𡊦; zh.Wiktionary gives those same two plus 㘬 and 㻈. Per the dual-corroboration policy only the two forms confirmed by *both* sources were added (坸, 𡊦); 㘬 and 㻈 (zh.Wiktionary-only) were excluded. Confirmed none of the four candidate forms already have independent vault character pages, so no ownership-conflict risk. `vietnamese: [cáu, cấu]` (already filled) reconfirmed correct — en.Wiktionary independently corroborates exactly these two Hán Việt readings.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. The stroke-lookup link in the SKIP bullet had to use the zero-padded `Stroke 09.md` filename (not `Stroke 9.md`, which doesn't exist) — corrected on first pass after checking the actual `lookup/Stroke/` directory listing and cross-checking two other genuine 9-stroke characters' existing Notes for the established format. Confirmed 垢 is already correctly cited on all four closing-bullet lookup pages (`Grade Advanced` is a dynamic Base query needing no manual entry; `HSK No`, `Hyōgai`, `Korean Name ㄱ` all already list it). No Derived Characters citing 垢 as their own phonetic; no Chengyu hits. Only existing stand-in [[污垢]] cites 垢.

Citing word page [[污垢]] checked and found already fully clean — `pos: 名詞` filled, alias 汙垢 correct, no vietnamese/hsk gaps — no edit needed.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 埠 (7350; 898 characters remaining).

### 2026-08-14, iteration 1607 — [[characters/埠|埠]]

**`mc_id: 0` verified as a genuine "confirmed absent" sentinel**, not an unresearched gap: 埠 does not appear anywhere in `CC 0000.md`–`CC 3000.md` — unsurprising, since "wharf, quay" in this specific graphic form is a comparatively late/dialectal coinage rather than a Classical-era word. **`pos` gap filled**: was blank, set to `名詞` ("wharf", "quay" are concretely nominal). **`graphemic_classification: 阜` reconfirmed correct** (形聲: semantic [[Radical 032|土]] "earth" + phonetic 阜, Zhengzhang OC \*baːs from phonetic \*buʔ) via en.Wiktionary and zh.Wiktionary agreement.

**`aliases` gap filled**: both en.Wiktionary and zh.Wiktionary independently list 埗 (Cantonese *bou6*) as the sole variant form of 埠; confirmed 埗 has no independent vault character page, so added with no ownership conflict. `vietnamese: [phụ]` (already filled) double-checked directly against hvdic.thivien.net's exact verbatim transcription — both the "Âm Hán Việt:" and "Âm Nôm:" lines give `phụ` identically, so this is a genuine non-contaminated Hán Việt reading with no divergence to flag.

Rebuilt the malformed `## Notes` (two bare unlinked CC-lookup wikilinks, no other bullets) to the standard 4-bullet format, using the established `mc_id: 0` template precedent (matching e.g. [[characters/呆 (char)|呆 (char)]]'s Notes) for the third bullet. Confirmed citation on `Old HSK 4`, `Korean Name ㅂ`, and `Grade Advanced` (dynamic Base query); **found and fixed a missing `Hyōgai` entry** — added as new sequential item 318 in `lookup/Japanese/Hyōgai.md`. No Derived Characters citing 埠 as their own phonetic; no Chengyu hits. Only existing stand-in [[埠頭]] cites 埠.

Citing word page [[埠頭]] checked: `pos: 名詞` already filled; its blank `vietnamese` field investigated directly via hvdic for the compound 埠頭 — no attested entry found, confirming a genuine gap rather than a bug; left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 墊 (char) (7351; 897 characters remaining).

### 2026-08-14, iteration 1608 — [[characters/墊 (char)|墊 (char)]]

`mc_id: 4368` is above the ~4000-entry ceiling of `CC 0000.md`–`CC 3000.md`, so per policy it's trusted long-tail data and left unverified/unchanged. **`graphemic_classification: 執` reconfirmed correct** (形聲: semantic [[Radical 032|土]] "earth" + phonetic 執, Zhengzhang OC \*diːb from phonetic \*tjib) via en.Wiktionary. Existing alias `垫` (simplified form) reconfirmed correct — both en.Wiktionary and zh.Wiktionary corroborate it as the sole reliably-doubly-attested variant; zh.Wiktionary's own "異體字" list for this page turned out to be a bundle of unrelated near-homophones/synonyms (including 簟, "bamboo mat," a wholly distinct character), so nothing further was added from it per the dual-corroboration policy.

**`vietnamese` gap found and filled**: the stored single reading `điếm` was correct but incomplete — hvdic.thivien.net's exact verbatim "Âm Hán Việt:" line gives *two* readings, `điếm, điệp`; added `điệp` as a second value. (`điếm`'s own homophone-collision caveat vs. the unrelated vulgar word from 店 was already thoroughly documented in the citing word page's own Notes — see below — and needed no further action here.)

Rebuilt the malformed `# Notes` (wrong heading level, stray leftover "needed dib" reminder line, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Checked all four closing-bullet lookup pages: `Grade Advanced` (dynamic Base query, fine) and `Old HSK 3` (already cites 墊, via a pre-existing dual-entry pattern — one via alias 垫, one via direct wikilink — confirmed this dual-listing is a widespread, consistent convention across dozens of other characters in that file, not a page-specific bug, so left untouched) needed no fix; **found and fixed two missing citations**: added as new sequential item 319 in `lookup/Japanese/Hyōgai.md`, and added to the existing `### 점` subsection of `Lookup/Korean/Korean Name ㅈ.md`. No Derived Characters citing 墊 as their own phonetic; no Chengyu hits.

This character's `stand_in` is itself — [[墊]] is a standalone word page, not a bound compound. Checked it and found it **already fully perfected** (stamped `date-last-perfect: 2026-07-27`): its Notes already contain a detailed, correct explanation of why the word's own `vietnamese: đệm` deliberately diverges from the character's formal Hán Việt `điếm` (a documented homophone collision with an unrelated vulgar word tracing to 店) — left entirely untouched, no edit needed.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 寓 (7352; 896 characters remaining).

### 2026-08-14, iteration 1609 — [[characters/寓|寓]]

**`mc_id` off-by-one fixed**: stored `2796` (which actually names 涸 in `CC 2000.md`); the real line for 寓 is `2797`. **`graphemic_classification: 禺` reconfirmed correct** (形聲: semantic [[Radical 040|宀]] "roof, house" + phonetic 禺, Zhengzhang OC \*ŋos from phonetic \*ŋo/\*ŋos) via en.Wiktionary and zh.Wiktionary agreement. Existing alias `庽` reconfirmed correct (doubly corroborated); zh.Wiktionary's additional candidate 䴁 was not corroborated by en.Wiktionary, so excluded per the dual-source policy.

`vietnamese: ngụ` (already filled) double-checked directly against hvdic.thivien.net's exact verbatim transcription — both the "Âm Hán Việt:" and "Âm Nôm:" lines give `ngụ` identically, confirming a genuine non-contaminated reading. `pos: 名詞` (already filled) confirmed appropriate.

Rebuilt the malformed Notes (mixed relative-path lookup links inconsistent with the vault-root-relative convention used elsewhere, a stray missing rank line, and two bare unlinked CC-lookup wikilinks trailing the closing bullet) to the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 3`, `Jinmeiyō`, `Korean Name ㅇ` all already correctly list 寓) — no lookup-page fixes needed this iteration. **Found and fixed a missing `## Words` section entirely**: the page had no Words heading at all despite `stand_in: 寓居` being set and [[寓居]] existing and correctly citing 寓 from its own side; added the section citing it. No Derived Characters citing 寓 as their own phonetic; no Chengyu hits; no other word pages cite 寓 besides its sole stand-in.

Citing word page [[寓居]] checked and found already fully clean — `pos: 名詞` filled, `vietnamese: ngụ cư` filled, all other fields present — no edit needed.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 寞 (7353; 895 characters remaining).

### 2026-08-14, iteration 1610 — [[characters/寞|寞]]

`mc_id: 4548` is above the ~4000-entry ceiling of `CC 0000.md`–`CC 3000.md`, trusted long-tail data, left unchanged. **`graphemic_classification: 莫` reconfirmed correct** (形聲: semantic [[Radical 040|宀]] "roof, house" + phonetic 莫, Zhengzhang OC \*maːɡ) via en.Wiktionary and zh.Wiktionary agreement; neither source lists any variant forms, so the existing blank `aliases` field is a genuine "no variants exist" state, not a gap. `vietnamese: mịch` (already filled) double-checked directly against hvdic.thivien.net's exact verbatim transcription — both "Âm Hán Việt:" and "Âm Nôm:" lines give `mịch` identically, no contamination. `pos: 性詞` (already filled) confirmed appropriate for a stative "lonely, desolate."

Rebuilt the malformed Notes (mixed relative-path lookup links, a raw parenthetical "Phono-semantic :" heading instead of the 形声-with-OC-gloss format, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format; verified the 韻 鈬開.md final page genuinely exists under that name (not a typo, as it first appeared) and correctly maps to `ɑk`. Confirmed citation on `Old HSK 3`, `Korean Name ㅁ`, and `Grade Advanced` (dynamic Base query); **found and fixed a missing `Hyōgai` entry** — added as new sequential item 320. **Found and fixed a missing `## Words` section entirely** (the page had no Words heading despite `stand_in: 寂寞` being set and the citing word already existing) — added, citing [[寂寞]]. Confirmed two other word pages ([[孤独]], [[寂滅]]) mention 寞/寂寞 only in comparative prose discussion, not as an actual citing compound — correctly excluded from Words. No Derived Characters citing 寞 as their own phonetic; no Chengyu hits.

Citing word page [[寂寞]] checked and found already clean on all bug-pattern checks (`pos: 性詞` filled, `vietnamese: tịch mịch` filled, no duplicate 品詞, no stale syllable) — no edit needed (its own missing `date-last-perfect` stamp is out of scope for the character-perfecting sweep).

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 屏 (7354; 894 characters remaining).

### 2026-08-14, iteration 1611 — [[characters/屏|屏]]

**`mc_id` off-by-one fixed**: stored `1689`; the real line for 屏 is `1690`. **`graphemic_classification: 并` reconfirmed correct** (形聲: semantic [[Radical 044|尸]] "corpse/body" + phonetic 并, Zhengzhang OC \*beːŋ/\*peŋ) via en.Wiktionary and zh.Wiktionary agreement.

**`aliases` bug fixed**: the stored `摒` was investigated specifically because it appeared in zh.Wiktionary's "相關派生漢字" (related-derivation) family list alongside 屏's genuine variants, but a direct check of 摒's own zh.Wiktionary page confirmed it explicitly as a *distinct derived character* (扌 "hand" + 屏 as phonetic, meaning "expel, arrange") sharing a common root with 屏, **not** a true variant/alias of it — removed (confirmed no other vault page referenced it, so no cascading fix needed). Cross-checked both sources' actual `異體字`-labeled sections (careful to distinguish the labeled variant section from the unlabeled derivation-family list, since the two are easy to conflate) and found 屛 (already present) and 幈 (missing) doubly confirmed — added 幈.

**`vietnamese: bình` reconfirmed correct and deliberately left as the sole reading**: hvdic.thivien.net's exact verbatim "Âm Hán Việt:" line actually gives three readings (`bình, bính, phanh`), but en.Wiktionary's pronunciation section confirms 屏 is polyphonic — píng "screen" (→ bình) is a wholly separate Mandarin reading/sense from bǐng "abandon, discard, suppress" (→ presumably bính/phanh) — and this character page is specifically the píng/"folding screen" sense (matching its `english`, `mandarin: píng`, and `stand_in: 屏風`). Adding the other two readings would have wrongly conflated a different sense onto this page, so only `bình` was kept — a deliberately different call from the two-reading addition made on [[characters/墊 (char)|墊 (char)]] two iterations ago, where both hvdic readings genuinely belonged to the same sense.

Rebuilt the malformed `## Notes` (two bare unlinked CC-lookup wikilinks, no other bullets) to the standard 4-bullet format. Confirmed citation on `Old HSK 6` and `Grade Advanced` (dynamic Base query); **found and fixed two missing citations**: `Hyōgai` only had the variant-redirect note "屛 --> 屏" but was missing 屏's own numbered entry (added as new sequential item 321, following the same pattern previously caught on [[characters/剃|剃]] earlier this session), and `Korean Name ㅂ`'s `### 병` subsection was missing 屏 entirely (added). No Derived Characters citing 屏 as their own phonetic with an existing vault page (摒 would qualify conceptually but has no page yet); no Chengyu hits. `## Words` already correctly lists the sole stand-in [[屏風]].

Citing word page [[屏風]] checked and found already fully clean (`pos` filled, `vietnamese` filled, no duplicate 品詞, no stale syllable) — no edit needed.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 屑 (char) (7355; 893 characters remaining).

### 2026-08-14, iteration 1612 — [[characters/屑 (char)|屑 (char)]]

**`mc_id` off-by-one fixed**: stored `3098`; the real line for 屑 is `3099`. **`pos` gap filled**: was blank, set to `名詞` ("scraps, waste tidbits" are concretely nominal).

**`graphemic_classification` bug found and fixed — the most structurally significant catch this iteration**: the stored value `八` was flatly wrong. Both en.Wiktionary (explicitly: "⿸尸肖," a phono-semantic compound, "originally written 㞕") and zh.Wiktionary's stroke breakdown (尸 radical + 7 additional strokes, matching 肖's own 7 strokes) independently confirm the true phonetic component is [[肖]], not 八 — corrected. Checked [[characters/八 (char)|八 (char)]] for a stray cross-reference to 屑 from the old wrong value (none found, so no cleanup needed there) and **added the missing entry to [[肖]]'s own `## Derived Characters` section**, which had never listed 屑 as one of its phonetic derivatives.

**`aliases` gap filled**: both sources doubly corroborate 㞕 (the character's own historical/original form) as the sole variant; confirmed it has no independent vault page, added with no conflict. `vietnamese: tiết` (already filled) double-checked against hvdic.thivien.net's exact verbatim transcription — both "Âm Hán Việt:" and "Âm Nôm:" lines give `tiết` identically, no contamination.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 4`, `Jinmeiyō`, `Korean Name ㅅ` all already correct) — no lookup-page fixes needed. **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[屑]] is a standalone word page, not a bound compound — added the section citing it.

Citing/self word page [[屑]] checked and found two of the standard recurring bugs: **`vietnamese: null` literal placeholder** (fixed to `tiết`, matching the character's own confirmed reading) and **blank `pos`** (filled with `名詞`) — both corrected.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 屠 (7356; 892 characters remaining).

### 2026-08-14, iteration 1613 — [[characters/屠|屠]]

`mc_id: 1342` reconfirmed correct against `CC 1000.md` (a rare clean check, no off-by-one). **`pos` gap filled**: was blank, set to `動詞` to match the citing word [[屠殺]]'s own `動詞` and the character's primary "to slaughter" sense. **`graphemic_classification: 者` reconfirmed correct** (形聲: semantic [[Radical 044|尸]] "body" + phonetic 者, Zhengzhang OC \*daː) via en.Wiktionary and zh.Wiktionary agreement — but the Notes wikilink needed correcting to `[[者 (char)|者]]`, since the actual vault page is filed as `者 (char).md`, not `者.md`.

**`vietnamese: đồ` reconfirmed correct and deliberately left as the sole reading**, mirroring the same judgment call made on [[characters/屏|屏]] two iterations ago: hvdic.thivien.net's exact verbatim "Âm Hán Việt:" line gives two readings (`chư, đồ`), but en.Wiktionary confirms 屠 is polyphonic — tú "slaughter" (→ đồ) is the primary reading this page covers, while a separate, rare chú/ceoi4 reading exists but is restricted solely to the place/tribe name 休屠 (Xiūchú) — so `chư` was correctly withheld as belonging to an unrelated sense, not added.

No variant forms found by either source, so the existing blank `aliases` field is a genuine "no variants" state, not a gap. Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 4`, `Hyōgai`, `Korean Name ㄷ` all already correct) and confirmed [[者 (char)|者 (char)]]'s own `## Derived Characters` section already correctly lists 屠 — no further fixes needed. `## Words` section was already present and correct, citing the sole stand-in [[屠殺]].

Citing word page [[屠殺]] checked and found already fully clean (`pos: 動詞` filled, no duplicate 品詞, `vietnamese`/other fields all filled) — no edit needed.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 嵌 (7357; 891 characters remaining).

### 2026-08-14, iteration 1614 — [[characters/嵌|嵌]]

`mc_id: 9661` is well above the ~4000-entry ceiling of `CC 0000.md`–`CC 3000.md`, trusted long-tail data, left unchanged. **`pos` gap filled**: was blank, set to `動詞` to match the citing word [[嵌入]]'s own `動詞`. **`graphemic_classification: 歁` reconfirmed correct** (形聲: semantic [[Radical 046|山]] "mountain" + abbreviated phonetic 歁, OC \*sɡaːmʔ/\*kʰraːm) via en.Wiktionary; zh.Wiktionary's summary claiming a simple 甘 phonetic was judged a shallower/less accurate WebFetch read and not followed.

**`aliases` gap filled**: intersecting both sources' variant-form lists (en.Wiktionary: 篏, 廞/𫷷; zh.Wiktionary's explicitly-labeled 異體字 section: 㘛, 廞, 篏) gives 篏 and 廞 as doubly corroborated; added both (confirmed neither has an independent vault page). 㘛 and 𫷷 were each single-source only, excluded per policy.

**`vietnamese` gap filled with a second reading**: hvdic's exact verbatim "Âm Hán Việt:" line gives `khâm, khảm`; unlike the polyphonic-with-distinct-sense cases on [[characters/屏|屏]] and [[characters/屠|屠]] (where a second hvdic reading was deliberately withheld), en.Wiktionary confirms 嵌's two Mandarin readings (qiàn/qiān) sit under the *same* Etymology 1 entry with no sense differentiation — i.e., these are dialectal/tonal doublets of one meaning, the same situation as [[characters/墊 (char)|墊 (char)]] — so `khâm` was added alongside the existing `khảm`.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format, using the `mc_id`-as-real-rank template (distinct from the `mc_id: 0` "confirmed absent" template used on e.g. [[characters/埠|埠]]). Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 4`, `Hyōgai`, `Korean Name ㄱ` all already correct) — no lookup-page fixes needed. `## Words` section was already present and correct, citing the sole stand-in [[嵌入]].

Citing word page [[嵌入]] checked: `pos: 動詞` already filled, no duplicate 品詞; its missing `vietnamese` field investigated directly via hvdic for the compound 嵌入 — no attested entry found, confirming a genuine gap rather than a bug; left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 彷 (7358; 890 characters remaining).

### 2026-08-14, iteration 1615 — [[characters/彷|彷]]

`mc_id: 4178` is above the ~4000-entry ceiling of `CC 0000.md`–`CC 3000.md`, trusted long-tail data, left unchanged. **`pos` gap filled**: was blank, set to `性詞`, matching the same stative-gloss convention used elsewhere in the vault for a bare "resemble"-type sense. **`graphemic_classification: 方` reconfirmed correct** (形聲: semantic [[Radical 060|彳]] "step, walk" + phonetic 方) via en.Wiktionary and zh.Wiktionary agreement; caught and fixed a wrong wikilink target in the process — the phonetic character's actual vault page is `方.md`, not `方 (char).md`.

**`vietnamese` contamination bug found and fixed — the significant catch this iteration**: the stored field held five readings (bàng, phảng, phẳng, phỏng, vưởng), but hvdic.thivien.net's exact verbatim transcription shows only `bàng, phảng` under the genuine "Âm Hán Việt:" line — the other three (phẳng, phỏng, vưởng) are listed exclusively under "Âm Nôm:", the vernacular-reading line, and do not belong in this field at all. Removed all three Nôm-layer readings, keeping only the two confirmed Hán Việt ones; en.Wiktionary independently corroborates `phảng`.

Checked `aliases` carefully: en.Wiktionary's alternative-form note for this specific fǎng-reading etymology gives 髣, while zh.Wiktionary's explicitly-labeled `異體字` section gives only 妨 — the two sources' lists don't overlap at all, so per the dual-corroboration policy neither was added; existing blank `aliases` field is correctly left blank, not a gap.

Rebuilt the malformed `## Notes` (two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format, adding a clarifying note on the character's two etymologically-separate Mandarin readings (páng "wander" vs. fǎng "resemble," the latter relevant to this page's `stand_in`). Confirmed citation on all four closing-bullet lookup pages and confirmed [[方]]'s own `## Derived Characters` section already correctly lists 彷 — no further fixes needed. `## Words` section was already present and correct, citing the sole stand-in [[彷彿]]. Noted in passing (but did not touch, per one-character-per-iteration scope) that the cranberry co-character [[characters/彿|彿]] shares an identical still-blank `pos` and is not yet perfected — a future iteration's task.

Citing word page [[彷彿]] checked: `pos: 副詞` already filled, no duplicate 品詞; its missing `vietnamese` field investigated directly via hvdic for the compound 彷彿 — no attested entry found, confirming a genuine gap; left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 恰 (char) (7359; 889 characters remaining).

### 2026-08-14, iteration 1616 — [[characters/恰 (char)|恰 (char)]]

`mc_id: 8219` is well above the ~4000-entry ceiling of `CC 0000.md`–`CC 3000.md`, trusted long-tail data, left unchanged. `pos: 性詞` and `graphemic_classification: 合` were both already correct — the latter reconfirmed (形聲: semantic [[Radical 061|忄]] "heart" + phonetic 合, Zhengzhang OC \*kʰruːb from phonetic \*kuːb/\*ɡuːb) via en.Wiktionary and zh.Wiktionary agreement; no doubly-corroborated variant forms found (en.Wiktionary's 太 note was for a separate, unrelated Etymology 2 and unconfirmed by zh.Wiktionary), so the existing blank `aliases` is a genuine "no variants" state.

**`vietnamese: kháp` investigated and deliberately left as the sole reading**: hvdic's exact verbatim "Âm Hán Việt:" line gives two readings, `cáp, kháp`, but unlike the same-sense doublet case on [[characters/嵌|嵌]], neither en.Wiktionary's pronunciation section nor the vault's own stored Cantonese (`hap1`, phonetically matching kháp, not cáp) gave any way to confirm `cáp` belongs to the same qià "exactly, just" sense covered by this page — en.Wiktionary's only other listed Mandarin reading (qiā, dialectal "eat" slang) is clearly unrelated to either Vietnamese form. Absent that confirmation, `cáp` was withheld rather than guessed onto the page.

Rebuilt the malformed `# Notes` (wrong heading level, a raw "= [SKIP...]" concatenation instead of separate bullets, a bare "HSK 3" plain-text mention instead of a proper Old HSK 3 link) to the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 3`, `Jinmeiyō`, `Korean Name ㅎ` all already correct) — no lookup-page fixes needed. **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[恰]] is a standalone word page — added the section citing it.

Self word page [[恰]] checked and found a missing `pos` field entirely (not even present in frontmatter, not just blank) — added `性詞` to match the character page.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 悶 (7360; 888 characters remaining).

### 2026-08-14, iteration 1617 — [[characters/悶|悶]]

`mc_id: 3424` reconfirmed correct against `CC 3000.md` (a rare clean check, no off-by-one). **`pos` gap filled**: was blank, set to `名詞`, matching the citing word [[苦悶]]'s own `名詞`. **`graphemic_classification: 門` reconfirmed correct** (形聲: semantic [[Radical 061|心]] "heart" + phonetic 門, Zhengzhang OC \*mɯːns) via en.Wiktionary and zh.Wiktionary agreement.

**`vietnamese` contamination bug found and fixed — the significant catch this iteration**: the stored field held three readings (muốn, muộn, mụn), but both hvdic.thivien.net's exact verbatim transcription *and* an independent en.Wiktionary check agree precisely: the genuine "Âm Hán Việt:" readings are `muộn, môn`, while `muốn` and `mụn` are Nôm-only vernacular readings that don't belong in this field. Fixed to `[muộn, môn]` — removing two contaminated entries and simultaneously recovering a missing genuine second reading (`môn`) that had never been present at all.

**`aliases` gap filled**: intersecting both sources' variant-form lists (en.Wiktionary: 㥃, 惛; zh.Wiktionary's explicitly-labeled 異體字 section: 㥃, 闷) gives 㥃 as newly doubly corroborated (in addition to the already-present, already-correct simplified alias 闷); added 㥃 (confirmed no independent vault page). 惛 was single-source only (en.Wiktionary), excluded per policy.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 3` — via the same established dual traditional/simplified-form listing pattern seen on other characters this session, not a bug — `Hyōgai`, `Korean Name ㅁ` all already correct) — no lookup-page fixes needed. **Found and fixed an entirely missing `## Words` section**: added, citing the sole stand-in [[苦悶]]. No Derived Characters citing 悶 as their own phonetic; no Chengyu hits; no other word pages cite 悶.

Citing word page [[苦悶]] checked: `pos: 名詞` already filled, no duplicate 品詞; its blank `vietnamese`/`hsk_level` fields investigated directly via hvdic for the compound 苦悶 — no attested entry found, confirming genuine gaps; left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 拱 (char) (7362; 887 characters remaining).

### 2026-08-14, iteration 1618 — [[characters/拱 (char)|拱 (char)]]

**`mc_id` off-by-one fixed**: stored `2449` (which actually names 虵 in `CC 2000.md`); the real line for 拱 is `2450`. **`korean_native` gap filled**: was an empty string, not just unset — verified via ko.Wiktionary's own 훈음 gloss "팔짱낄 공" (to clasp hands/fold arms) and filled with `팔짱낄`, matching the vault convention of storing only the 훈 stem.

**`vietnamese` contamination bug found and fixed — the largest single-field cleanup this session**: the stored field held four readings (cõng, cùng, cũng, củng), but hvdic.thivien.net's exact verbatim transcription gives only `củng` under the genuine "Âm Hán Việt:" line, with `cõng` and `cùng` explicitly under "Âm Nôm:" instead; `cũng` (one of the single most common Vietnamese function words, "also/too," unrelated to this character) wasn't attested by hvdic at all and appears to have been pure contamination. Reduced to the single genuine reading `củng`.

**`graphemic_classification: 共` reconfirmed correct** (形聲/會意 hybrid per en.Wiktionary: semantic [[Radical 064|扌]] "hand" + phonetic 共, OC \*kloŋʔ) — but investigated 共 itself as a possible alias candidate (both en.Wiktionary and zh.Wiktionary's explicitly-labeled 異體字 sections list it) and excluded it, since 共 already has its own independent, actively-used vault page (`共 (char).md`, "with, together") with a wholly different core meaning — the same phonetic-relation-vs-true-alias distinction established on [[characters/屏|屏]] (摒) and [[characters/墊 (char)|墊 (char)]] (簟) earlier this session. 拲/珙 (zh-only) and 廾 (en-only) were likewise single-source and excluded.

**Two broken wikilinks fixed**: the old Notes referenced bare `[[扌]]` (no such page exists — the semantic component is the Radical 064 lookup page, not a standalone character page) and `[[共]]` (the actual vault page is filed as `共 (char).md`). **Found and fixed a stale/broken `## Words` entry**: the page cited `[[拱手]]`, a word page that does not exist in this vault (confirmed via a vault-wide search, and already independently flagged in the vault's own `broken links output.md` audit) — replaced with a correct self-citation of [[拱]], matching this character's own `stand_in: 拱`. **Found and fixed a missing `Hyōgai` citation**: added as new sequential item 322.

Rebuilt the malformed Notes to the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `Old HSK 4`, and `Korean Name ㄱ`. **Found and fixed a missing `## Derived Characters` section entirely on [[characters/共 (char)|共 (char)]]** (a previously-`date-last-perfect`-stamped page from 2026-07-10 that had never had this section at all) — added it, citing 拱.

Self word page [[拱]] checked and fixed two of the standard recurring bugs: **`vietnamese: null` literal placeholder** (fixed to `củng`, matching the character's own corrected reading) and **missing `pos` field** (added `名詞`).

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 捷 (7363; 886 characters remaining).

### 2026-08-14, iteration 1619 — [[characters/捷|捷]]

**`mc_id` off-by-one fixed**: stored `1924`; the real line for 捷 is `1925`. **`pos` gap filled**: was blank, set to `性詞`, matching the citing word [[敏捷]]'s own `性詞`. **`graphemic_classification: 疌` reconfirmed correct** (形聲: semantic [[Radical 064|手]] "hand" + phonetic 疌, Zhengzhang OC \*zeb) via en.Wiktionary and zh.Wiktionary agreement; no doubly-corroborated variant forms found (en.Wiktionary listed none at all; zh.Wiktionary's long 異體字 list was single-source), so the existing blank `aliases` is a genuine "no variants" state.

**`vietnamese` contamination bug found and fixed**: the stored field held `tiệp, tẹp`, but hvdic.thivien.net's exact verbatim transcription shows the genuine "Âm Hán Việt:" line as `thiệp, tiệp` and the "Âm Nôm:" line as `tẹp, tiệp` — `tẹp` is Nôm-only and doesn't belong here, while the genuine second Hán Việt reading `thiệp` had never been present at all. Fixed to `[tiệp, thiệp]`.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Initially searched for a citation on `Korean Name ㅈ` and found none — then caught the mistake: 捷's Korean reading is 첩, which belongs under `ㅊ` not `ㅈ`, and confirmed it was already correctly cited on `Korean Name ㅊ`'s own `### 첩` subsection all along. Confirmed citation on `Grade Advanced`, `Old HSK 3`, and `Jinmeiyō` too — no lookup-page fixes needed this iteration.

**Fixed a duplicate-`品詞` bug on both citing word pages**: [[敏捷]] carried both `pos: 性詞` and a redundant `品詞: 形容動詞` (a second part-of-speech tagging system duplicating the same information — the classic recurring pattern, this time with non-identical surface text but the same redundant purpose); [[門捷金]] carried `pos: 固有名詞` and an exactly-identical `品詞: 固有名詞`. Removed the redundant `品詞` field from both, keeping only the canonical `pos`.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 掏 (7364; 885 characters remaining).

### 2026-08-14, iteration 1620 — [[characters/掏|掏]]

`mc_id: 6567` is well above the ~4000-entry ceiling of `CC 0000.md`–`CC 3000.md`, trusted long-tail data, left unchanged. **`pos` gap filled**: was blank, set to `動詞`, matching the citing word [[掏摸]]'s own `動詞`.

**`graphemic_classification: 陶` investigated for a possible bug and deliberately kept**: en.Wiktionary claims the phonetic is 匋 (陶's own pageless original form/alias), while zh.Wiktionary explicitly says the phonetic is 陶 itself. Checked [[characters/陶|陶]]'s own Notes, which already document that 匋 is treated as its true phonetic root (pageless, cited by name with an explanatory note) — but since this is a single-source (en.Wiktionary) claim about 掏 specifically, unconfirmed by zh.Wiktionary, and citing 陶 directly is a fully corroborated, vault-consistent choice already backed by an existing page, kept `陶` rather than introducing 匋 as a second pageless-phonetic citation pattern. **Found and fixed a missing `## Derived Characters` section entirely on [[characters/陶|陶]]** (already `date-last-perfect`-stamped 2026-08-10, but with no such section at all) — added it, citing 掏.

**`vietnamese` contamination bug found and fixed**: the stored field held `thao, đào`, but hvdic.thivien.net's exact verbatim transcription gives only `đào` under the genuine "Âm Hán Việt:" line, with `thao` appearing exclusively under "Âm Nôm:" — removed the Nôm-only reading, keeping just `đào` (also the sole reading en.Wiktionary corroborates).

Investigated the existing alias `搯`: en.Wiktionary and zh.Wiktionary's variant-form lists for 掏 don't overlap at all (en: 𢲛 only; zh's explicitly-labeled 異體字: 搯 only) — but since `搯` has no independent vault page and zh.Wiktionary's account is from a properly-labeled variant section (not a derivation-family list, the distinguishing test established earlier this session), it was kept rather than removed; `𢲛` was not added, being single-source.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. **Found and fixed two missing citations**: `Hyōgai` (added as new sequential item 323) and `Korean Name ㄷ`'s `### 도` subsection (added). Confirmed citation on `Grade Advanced` and `Old HSK 2`. `## Words` section was already present and correct, citing the sole stand-in [[掏摸]].

Citing word page [[掏摸]] checked: `pos: 動詞` already filled, no duplicate 品詞 — no edit needed.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 揶 (7365; 884 characters remaining).

### 2026-08-14, iteration 1621 — [[characters/揶|揶]]

`mc_id: 0` verified as a genuine "confirmed absent" sentinel: 揶 does not appear anywhere in `CC 0000.md`–`CC 3000.md`. **`pos` gap filled**: was blank, set to `動詞` (a transitive "to ridicule/mock," consistent with the same choice made on [[characters/屠|屠]] and [[characters/掏|掏]] earlier this session) — deliberately not matched to the citing word [[揶揄]]'s own stored `実詞`, since checking `grammar/文法 - 97品詞.md` confirmed 実詞 (Content Words) is a non-leaf parent category in the formal taxonomy, not a valid leaf `pos` value; that word page's own value looks like a separate, out-of-scope bug for the word-sweep to fix later. **`graphemic_classification: 耶` reconfirmed correct** (形聲: semantic [[Radical 064|手]] "hand" + phonetic 耶, Zhengzhang OC \*laː) via en.Wiktionary — the Notes wikilink needed correcting to `[[耶 (char)|耶]]`, since the actual vault page is filed as `耶 (char).md`.

**`vietnamese` gap filled — an unusual case with no Nôm contamination**: the field was entirely blank; hvdic.thivien.net's exact verbatim "Âm Hán Việt:" line gives two readings, `da, gia`, with no "Âm Nôm:" line present at all. Cross-checked against the compound 揶揄 itself, which hvdic shows read both "da du" and "gia du" — confirming both are genuine alternate Hán Việt readings of the same sense, not a contamination or polyphony split. Filled with both.

**`aliases` gap filled**: intersecting both sources' variant-form lists (en.Wiktionary: 擨, 捓; zh.Wiktionary's explicitly-labeled 異體字: 捓 only) gives 捓 as doubly corroborated; added (confirmed no independent vault page). 擨 was single-source, excluded.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard `mc_id: 0` template. Confirmed citation on `Grade Advanced` and `Hyōgai`; **found and fixed a broken citation on `Korean Name ㅇ`**: its `### 야` subsection already had an entry, but as a bare `[[捓]]` wikilink to 揶's own alias, which has no page of its own (a red link) — replaced with a proper link to 揶's actual page. Confirmed [[characters/耶 (char)|耶 (char)]]'s own `Derived Characters` section already correctly lists 揶 — no further fix needed there.

Citing word page [[揶揄]] checked: its blank `vietnamese` field investigated directly via hvdic for the compound 揶揄 — no formally-labeled "Âm Hán Việt:" line found for the compound itself (only informal component-reading transcriptions), confirming a genuine gap; left untouched. Its `pos: 実詞` non-leaf-taxonomy issue was noted but not touched, being out of scope for this character-only iteration.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 擱 (7366; 883 characters remaining).

### 2026-08-14, iteration 1622 — [[characters/擱|擱]]

`mc_id: 0` verified as a genuine "confirmed absent" sentinel. **Two malformed-YAML frontmatter bugs fixed**: `japanese_native` held an invalid mix of a bare scalar (`お`) followed by an orphan list item (`- おく`) under the same key — verified via both ja.Wiktionary and Jisho that this character has exactly one kun-yomi, お-く (oku), and fixed the field to that single hyphenated value. `vietnamese` held a single string `"gác, các"` with an embedded comma instead of a proper YAML list — split apart during the same edit that fixed its contents (see below).

**`vietnamese` contamination bug found and fixed**: hvdic.thivien.net's exact verbatim transcription shows the genuine "Âm Hán Việt:" line as `các` only, with `gác` appearing exclusively under "Âm Nôm:" — reduced to just `các`. **`pos` inconsistency fixed**: was `性詞`, but the citing word [[擱筆]]'s own `pos: 動詞` and the plainly transitive/action sense ("to lay down the pen, stop writing") both point to `動詞`; corrected to match. **`graphemic_classification: 閣` reconfirmed correct** (形聲: semantic [[Radical 064|手]] "hand" + phonetic 閣, Zhengzhang OC \*klaːɡ) via en.Wiktionary and zh.Wiktionary agreement; zh.Wiktionary's labeled 異體字 section also listed 閣 itself as a "variant," but since 閣 has its own independent, actively-used vault page ("chamber, pavilion, cabinet") — the same phonetic-relation-vs-true-alias pattern as [[characters/屏|屏]] (摒) and [[characters/墊 (char)|墊 (char)]] (簟) — it was not added as an alias; the existing `搁` (simplified form, doubly corroborated) was left as the sole alias.

**Found and fixed the identical Vietnamese contamination bug on [[characters/閣|閣]] itself** while researching 擱's phonetic component: 閣's own stored `vietnamese: [các, gác]` had the exact same Nôm-layer `gác` contaminating the field (confirmed directly via hvdic for 閣) — fixed to `[các]` despite that page already being `date-last-perfect`-stamped from 2026-08-08, evidently predating this session's contamination-checking practice. **Found and fixed a missing `## Derived Characters` section entirely on [[characters/閣|閣]]** — added it, citing 擱.

Rebuilt the malformed `## Notes` (a bare "MC pronunciation assumed to be the same as 閣" placeholder note plus two unlinked CC-lookup wikilinks) to the standard `mc_id: 0` template. **Found and fixed two missing citations**: `Hyōgai` (added as new sequential item 324) and `Korean Name ㄱ`'s `### 각` subsection (added). Confirmed citation on `Grade Advanced` and `Old HSK 2` (the latter via the established dual traditional/simplified dual-listing pattern, not a bug). `## Words` section was already present and correct, citing the sole stand-in [[擱筆]].

Citing word page [[擱筆]] checked: `pos: 動詞` already filled (and now matches the corrected character `pos`), no duplicate 品詞; its missing `vietnamese` field investigated directly via hvdic for the compound 擱筆 — no attested entry found, confirming a genuine gap; left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 攀 (7367; 882 characters remaining).

### 2026-08-14, iteration 1623 — [[characters/攀|攀]]

**`mc_id` off-by-one fixed**: stored `3451`; the real line for 攀 is `3452`. **`pos` gap filled**: was blank, set to `事詞` — matched to the citing word [[攀縁]]'s own `事詞`, the correct formal transitive-verb leaf per `grammar/文法 - 97品詞.md` (unlike the non-leaf `実詞` value flagged as out-of-scope on [[characters/揶|揶]]'s citing word two iterations ago). **`graphemic_classification: 樊` reconfirmed correct** (形聲: semantic [[Radical 064|手]] "hand" + phonetic 樊, Zhengzhang OC \*pʰraːn from phonetic \*ban) via en.Wiktionary and zh.Wiktionary agreement.

**`aliases` gap filled**: both sources' labeled 異體字/alternative-form lists give exactly the same pair, 扳 and 㐴 — fully doubly corroborated; added both (confirmed neither has an independent vault page).

**`vietnamese` gap filled with a second reading**: hvdic's exact verbatim "Âm Hán Việt:" line gives `phan, phàn`; unlike contamination cases, `phan` also appears under "Âm Nôm:" but `phàn` is not disqualified by anything — en.Wiktionary independently lists both as "Vietnamese Han Readings" without restricting either to a separate sense, and the character has only one Mandarin reading/meaning (pān, "climb") — so both were kept, the same same-sense-doublet judgment as [[characters/嵌|嵌]] and [[characters/墊 (char)|墊 (char)]].

Rebuilt the malformed `## Notes` (two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 3`, `Hyōgai`, `Korean Name ㅂ` all already correct) — no lookup-page fixes needed this iteration. `## Words` section was already present and correct, citing the sole stand-in [[攀縁]].

Citing word page [[攀縁]] checked: `pos: 事詞` already filled, no duplicate 品詞; its missing `vietnamese` field investigated directly via hvdic for the compound 攀縁 — no attested entry found, confirming a genuine gap; left untouched.

Stamped `date-last-perfect: 2026-08-14`.

Next never-perfected character by `danayo_id`: 敲 (char) (7368; 881 characters remaining).

### 2026-08-15, iteration 1624 — [[characters/敲 (char)|敲 (char)]]

`mc_id: 6526` is well above the ~4000-entry ceiling of `CC 0000.md`–`CC 3000.md`, trusted long-tail data, left unchanged. **`pos` gap filled**: was blank, set to `事詞` (transitive "to knock/tap something," the correct formal taxonomy leaf). **`graphemic_classification: 高` reconfirmed correct** (形聲: semantic [[Radical 066|攴]] "to strike, tap" + phonetic 高, Zhengzhang OC \*kʰraːw/\*kʰraːws) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/高 (char)|高 (char)]]'s own `Derived Characters` section already correctly lists 敲.

**`vietnamese` contamination bug found and fixed**: the stored field held three readings (sao, xao, xào), but hvdic.thivien.net's exact verbatim transcription gives only `xao` under the genuine "Âm Hán Việt:" line — `sao` is Nôm-only, and `xào` wasn't attested by hvdic at all. Reduced to the single genuine reading `xao`.

**`aliases` gap filled**: intersecting both sources' variant-form lists (en.Wiktionary's Etymology-1 set: 㪣, 毃, 䯨, 摮, 𣫁; zh.Wiktionary's explicitly-labeled 異體字: 㪣, 䯨, 搞, 摮, 毃) gives four doubly-corroborated forms — 㪣, 䯨, 摮, 毃 — added all four (confirmed none has an independent vault page). `搞` (zh-only — also a very common independent character, "to do/make," a likely false-positive of the same phonetic-relation type flagged repeatedly this session) and `𣫁` (en-only) were excluded.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages. **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[敲]] is a standalone word page — added the section citing it.

Self word page [[敲]] checked and fixed two of the standard recurring bugs: **`vietnamese: null` literal placeholder** (fixed to `xao`, matching the character's own corrected reading) and **missing `pos` field** (added `事詞`).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 斟 (7369; 880 characters remaining).

### 2026-08-15, iteration 1625 — [[characters/斟|斟]]

`mc_id: 2898` reconfirmed correct against `CC 2000.md` (a rare clean check, no off-by-one). **`pos` gap filled**: was blank, set to `事詞`, matching the citing word [[斟酌]]'s own `事詞`. **`graphemic_classification: 甚` reconfirmed correct** (形聲: semantic [[Radical 068|斗]] "dipper, cup" + phonetic 甚, Zhengzhang OC \*kljum) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/甚|甚]]'s own `Derived Characters` section already correctly lists 斟.

**`joyo_level` and `hsk_level` both found blank/wrong and fixed**: `joyo_level` was an empty string despite en.Wiktionary explicitly classifying 斟 as hyōgai kanji (non-jōyō, non-jinmeiyō) — filled with `表外字`, and added the correspondingly-missing `Hyōgai` citation (new sequential item 325). `hsk_level` was stored as `"6"`, but the character is also manually listed on `lookup/HSK/HSK No.md` (the vault's curated "no official HSK level" list) — a direct contradiction. Resolved the same way as the [[characters/嚢|嚢]]/[[characters/墊 (char)|墊 (char)]] precedent earlier this session: 斟's own citation on `Old HSK 6.md` almost certainly reflects its appearance *within* the HSK6 vocabulary compound [[斟酌]], not an official standalone designation for the bare character — corrected `hsk_level` to `無`.

**`vietnamese` contamination bug found and fixed**: the stored field held four readings (cham, châm, chơm, chầm), but hvdic.thivien.net's exact verbatim transcription gives only `châm` under the genuine "Âm Hán Việt:" line, with `cham` appearing exclusively under "Âm Nôm:" and `chơm`/`chầm` not attested anywhere at all (likely pure contamination or typos). Reduced to the single genuine reading `châm`.

Checked `aliases`: zh.Wiktionary's explicitly-labeled 異體字 section gives 㪸 and 酙 (酙 — with the 酉 "alcohol" radical — fits the "pour wine" sense particularly well), but en.Wiktionary's only listed alternative forms (漛, 滕) are explicitly scoped to a wholly separate Southern Min Etymology 2, not this character's sense — zero overlap between the two sources, so nothing was added; existing blank `aliases` correctly left as-is.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, a stray bullet holding the Words-section content) to the standard 4-bullet format plus a proper `## Words` section, citing the sole stand-in [[斟酌]]. Confirmed citation on `Grade Advanced` and `Korean Name ㅈ`.

Citing word page [[斟酌]] checked: `pos: 事詞` already filled; its blank `vietnamese` field investigated directly via hvdic for the compound 斟酌 — no attested entry found, confirming a genuine gap; left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 昂 (7370; 879 characters remaining).

### 2026-08-15, iteration 1626 — [[characters/昂|昂]]

`mc_id: 4587` is above the ~4000-entry ceiling of `CC 0000.md`–`CC 3000.md`, trusted long-tail data, left unchanged. **`pos` gap filled**: was blank, set to `性詞` ("proud, bold" — a descriptive/stative sense). **`graphemic_classification: 卬` reconfirmed correct** (形聲: semantic [[Radical 072|日]] "sun" + phonetic 卬, Zhengzhang OC \*ŋaːŋ) via en.Wiktionary and zh.Wiktionary agreement.

**`aliases` gap filled**: intersecting both sources' variant-form lists (en.Wiktionary: 昻, 䀚; zh.Wiktionary's explicitly-labeled 異體字: 卬, 昻, 枊) gives 昻 as the sole doubly-corroborated candidate; added (confirmed no independent vault page). 卬 (the phonetic component itself, already correctly excluded as pageless rather than cited as an alias), 枊, and 䀚 were each single-source, excluded.

**`vietnamese` contamination bug found and fixed**: the stored field held four readings (ngang, ngàng, ngáng, ngãng), but both hvdic.thivien.net's exact verbatim transcription and en.Wiktionary's own explicit Hán Việt/Nôm split agree: the genuine "Âm Hán Việt:" reading is `ngang` alone, with `ngàng, ngáng, ngãng` (plus two further Nôm-only forms neither source flagged as attested) all belonging exclusively to the Nôm layer. Reduced to the single genuine reading `ngang`.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, a stray bullet holding one Words-section entry) to the standard 4-bullet format plus a proper `## Words` section. **Found this character has two genuine citing words, not one**: the existing stray bullet already named [[昂揚]], and adding it alongside the `stand_in` [[昂然]] revealed both had been missing from a real Words section entirely. Confirmed citation on `Grade Advanced`, `Old HSK 6`, `Jinmeiyō`, and `Korean Name ㅇ` — no lookup-page fixes needed.

Both citing word pages checked and fixed the same recurring bug: **missing `pos` field** — [[昂然]] and [[昂揚]] each had a bare `pos:` key with no value; both filled with `性詞` to match the character. Their blank `vietnamese` fields were investigated directly via hvdic for each compound — no formally-labeled "Âm Hán Việt:" line found for either (昂然 turned up an informal "ngang nhiên" gloss elsewhere on the page, but not under that label, so it was treated as a genuine gap per the established exact-citation bar) — left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 暈 (7371; 878 characters remaining).

### 2026-08-15, iteration 1627 — [[characters/暈|暈]]

`mc_id: 4353` is above the ~4000-entry ceiling of `CC 0000.md`–`CC 3000.md`, trusted long-tail data, left unchanged. **`pos`, `joyo_level`, and `korean_native` gaps all filled**: `pos` was blank, set to `性詞` ("dizzy, blurry"); `joyo_level` was blank despite en.Wiktionary explicitly classifying 暈 as hyōgai kanji — filled with `表外字`, with a correspondingly missing `Hyōgai` citation added (new sequential item 326); `korean_native` was an empty string — filled with `무리`, verified via ko.Wiktionary's own 훈음 gloss "무리 운". **`graphemic_classification: 軍` reconfirmed correct** (形聲: semantic [[Radical 072|日]] "sun" + phonetic 軍, Zhengzhang OC \*ɢuns from phonetic \*kun — originally a pictogram of the sun's halo) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/軍|軍]]'s own `Derived Characters` section already correctly lists 暈.

**`vietnamese` contamination bug found and fixed, with a cross-source conflict resolved in hvdic's favor**: the stored field held four readings (quầng, vầng, vừng, vựng); hvdic.thivien.net's exact verbatim transcription splits genuine "Âm Hán Việt:" as `vận, vựng` against "Âm Nôm:" `quầng, vầng, vừng` — but en.Wiktionary's own account classifies `quầng` as Hán Việt too, disagreeing with hvdic. Trusting hvdic as the specialized dedicated Hán-Nôm dictionary (the established practice all session), fixed to `[vận, vựng]` — dropping three Nôm-layer readings and recovering the missing genuine `vận`.

**`aliases` gap filled**: both sources' labeled variant/異體字 sections agree on 煇 (in addition to the already-correct, already-present simplified alias 晕); added (confirmed no independent vault page).

**Found and fixed a vault-wide propagated `羅馬字` bug affecting three sibling characters on the same syllable**: 暈's stored `羅馬字: "'unsu"` didn't match its own single-syllable `諺文`/`注音` (운/ㄨㄋ) — cross-checking the `syllables/ㄨㄋ.md` page itself confirmed the canonical value is `'un`. The exact same wrong `"'unsu"` value turned out to also be stored on two *other*, already-`date-last-perfect`-stamped characters sharing this syllable — [[characters/員|員]] (2026-07-30) and [[characters/運|運]] (2026-07-25) — while a fourth sibling, [[characters/韻|韻]], already had the correct value. Fixed all three to `'un`, consistent with this session's practice of fixing directly-discovered consequence bugs on other pages regardless of their own perfection status.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `Old HSK 3` (via the established dual traditional/simplified listing pattern), and `Korean Name ㅇ`. **Found and fixed an entirely missing `## Words` section**: added, citing the sole stand-in [[玄暈]] (already flagged with the same non-leaf `実詞` taxonomy issue noted on [[characters/揶|揶]]'s citing word — not touched, out of scope).

Citing word page [[玄暈]]'s blank `vietnamese` field investigated directly via hvdic for the compound 玄暈 — no attested entry found, confirming a genuine gap; left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 杜 (7372; 877 characters remaining).

### 2026-08-15, iteration 1628 — [[characters/杜|杜]]

`mc_id: 1019` reconfirmed correct against `CC 1000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `動詞`, matching the citing word [[杜撰]]'s own `動詞`. **`graphemic_classification: 土` reconfirmed correct** (形聲: semantic [[Radical 075|木]] "tree" + phonetic 土, Zhengzhang OC \*l'aːʔ) — the Notes wikilink needed correcting to `[[土 (char)|土]]`, since the actual vault page is filed as `土 (char).md`.

**`vietnamese` contamination bug found and fixed — the largest cleanup this iteration**: the stored field held five readings (đũa, đậu, đỏ, đổ, đỗ), but hvdic.thivien.net's exact verbatim transcription gives only `đỗ` under the genuine "Âm Hán Việt:" line, with all four others appearing exclusively under "Âm Nôm:". (en.Wiktionary's own account muddies this slightly, additionally counting `đổ` as Hán Việt, but hvdic — the specialized dedicated dictionary trusted throughout this session — was followed.) Reduced to the single genuine reading `đỗ` (also notable as the common Vietnamese surname Đỗ). No doubly-corroborated variant forms found, so the existing blank `aliases` is a genuine "no variants" state.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 4`, `Jinmeiyō`, `Korean Name ㄷ` all already correct) — no lookup-page fixes needed. `## Words` section was already present and correct, citing both [[杜撰]] (the `stand_in`) and the neologism [[杜金]] ("dubnium").

**Found and fixed two consequence bugs on [[characters/土 (char)|土 (char)]]** while verifying the phonetic link: a duplicate `品詞: 名詞` field exactly redundant with its own `pos: 名詞` (removed — the same recurring pattern flagged repeatedly on word pages this session, here found on a character page, already `date-last-perfect`-stamped from 2026-02-20), and an entirely missing `## Derived Characters` section (added, citing 杜). **Found and fixed the identical duplicate-`品詞` bug on the citing word page [[杜金]]** (`品詞: 固有名詞` exactly duplicating `pos: 固有名詞`) — removed. [[杜撰]] was already fully clean (`pos: 動詞`, `vietnamese: đỗ soạn` both filled, no duplicate 品詞) — no edit needed.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 柩 (7373; 876 characters remaining).

### 2026-08-15, iteration 1629 — [[characters/柩|柩]]

**`mc_id` off-by-one fixed**: stored `2551`; the real line for 柩 is `2552`. **`pos` gap filled**: was blank, set to `名詞` ("coffin" is concretely nominal). **`japanese_native` typo fixed**: stored `ひちぎ`, which doesn't correspond to any real reading — both en.Wiktionary and the character's own meaning confirm the genuine kun-yomi is `ひつぎ` (hitsugi, "coffin"); corrected the transposed kana. **`graphemic_classification: 匛` reconfirmed correct** per en.Wiktionary (semantic [[Radical 075|木]] "tree, wood" + phonetic 匛, Zhengzhang OC \*ɡʷlɯs); zh.Wiktionary's own account named 臼 as the phonetic instead, but its own explicitly-labeled 異體字 section separately lists 匛 as a variant — read as the same underlying phonetic-series relationship described two different ways rather than a genuine conflict, so the existing, en.Wiktionary-corroborated value was kept.

**`aliases` gap filled**: intersecting both sources' variant-form notes (en.Wiktionary: "see also 柾"; zh.Wiktionary's explicitly-labeled 異體字: 匛, 匶, 柾) gives 柾 as the sole doubly-corroborated candidate; added (confirmed no independent vault page). 匶 was single-source, excluded.

**`vietnamese` contamination bug found and fixed**: the stored field held two readings (cửu, cữu), but hvdic.thivien.net's exact verbatim transcription shows the genuine "Âm Hán Việt:" reading is `cữu` alone, with `cửu` appearing exclusively under "Âm Nôm:". Reduced to the single genuine reading `cữu`.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `HSK No`, `Hyōgai`, `Korean Name ㄱ` all already correct) — no lookup-page fixes needed. `## Words` section was already present and correct, citing the sole stand-in [[霊柩]].

Citing word page [[霊柩]] checked and found already fully clean (`pos: 名詞` filled, `vietnamese: linh cữu` filled, aliases present, no duplicate 品詞) — no edit needed.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 梳 (char) (7374; 875 characters remaining).

### 2026-08-15, iteration 1630 — [[characters/梳 (char)|梳 (char)]]

`mc_id: 6271` is well above the ~4000-entry ceiling of `CC 0000.md`–`CC 3000.md`, trusted long-tail data, left unchanged. **`pos` and `joyo_level` gaps filled**: `pos` was blank, set to `名詞` ("comb," a physical object); `joyo_level` was blank despite en.Wiktionary explicitly classifying 梳 as hyōgai kanji — filled with `表外字`, with a correspondingly missing `Hyōgai` citation added (new sequential item 327). **`graphemic_classification: 疏` reconfirmed correct** (形聲: semantic [[Radical 075|木]] "wood" + abbreviated phonetic 疏, Zhengzhang OC \*sŋra) via en.Wiktionary and zh.Wiktionary agreement; `vietnamese: sơ` (already filled) double-checked against hvdic's exact verbatim transcription — both the "Âm Hán Việt:" and "Âm Nôm:" lines give `sơ` identically, no contamination. No variant forms found by either source, so the existing blank `aliases` is a genuine "no variants" state.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `Old HSK 3`, and `Korean Name ㅅ`. **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[梳]] is a standalone word page — added the section citing it.

Self word page [[梳]] checked and fixed two of the standard recurring bugs: **`vietnamese: null` literal placeholder** (fixed to `sơ`, matching the character's own confirmed reading) and **missing `pos` field** (added `名詞`).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 歇 (7375; 874 characters remaining).

### 2026-08-15, iteration 1631 — [[characters/歇|歇]]

**`mc_id` off-by-one fixed**: stored `2617`; the real line for 歇 is `2618`. **`pos` and `joyo_level` gaps filled**: `pos` was blank, set to `性詞` (matching the citing word [[間歇]]'s own `性詞`); `joyo_level` was blank despite en.Wiktionary explicitly classifying 歇 as hyōgai kanji — filled with `表外字`, with a correspondingly missing `Hyōgai` citation added (new sequential item 328).

**`graphemic_classification` bug found and fixed**: the stored value `喝` was wrong — both en.Wiktionary and zh.Wiktionary independently and explicitly identify the true phonetic component as [[曷]] (OC \*ɡaːd), a pageless character distinct from [[characters/喝 (char)|喝 (char)]] (which itself derives from 曷 with a different semantic radical, "shout, drink," and has its own independent vault page) — corrected to `曷`. Confirmed 喝 (char)'s own page had no stray cross-reference to clean up.

**`vietnamese` contamination bug found and fixed**: the stored field held six readings (hiết, hét, hít, hết, hớt, yết), but hvdic.thivien.net's exact verbatim transcription gives only `hiết, tiết, yết` under the genuine "Âm Hán Việt:" line, with `hét, hít, hết, hớt` all under "Âm Nôm:" — reduced to the three genuine readings, recovering the previously entirely-missing `tiết` (en.Wiktionary corroborates `hiết, yết` but doesn't mention `tiết` either way, so hvdic's dedicated Hán-Nôm split was trusted as the deciding source).

Rebuilt the malformed `## Notes` (two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `Old HSK 2`, and `Korean Name ㅎ`. `## Words` section was already present and correct, citing the sole stand-in [[間歇]].

Citing word page [[間歇]]'s blank `vietnamese` field investigated directly via hvdic for the compound 間歇 — no attested entry found, confirming a genuine gap; left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 沐 (7376; 873 characters remaining).

### 2026-08-15, iteration 1632 — [[characters/沐|沐]]

**`mc_id` off-by-one fixed**: stored `1708`; the real line for 沐 is `1709`. **`pos` and `joyo_level` gaps filled**: `pos` was blank, set to `性詞` (matching the citing word [[沐浴]]'s own `性詞`); `joyo_level` was blank despite en.Wiktionary explicitly classifying 沐 as hyōgai kanji — filled with `表外字`, with a correspondingly missing `Hyōgai` citation added (new sequential item 329). **`korean_native` investigated but left blank**: could not find a corroborated 훈음 gloss on ko.Wiktionary or zh.Wiktionary's Korean section (only the bare sound-reading 목 was available anywhere) — left as a genuine gap rather than guessed. **`graphemic_classification: 木` reconfirmed correct** (形聲: semantic [[Radical 085|氵]] "water" + phonetic 木, Zhengzhang OC \*moːɡ) — the Notes wikilink needed correcting to `[[木 (char)|木]]`, since the actual vault page is filed as `木 (char).md`; confirmed its own `Derived Characters` section already correctly lists 沐.

**`vietnamese` contamination bug found and fixed**: the stored field held four readings (móc, múc, mốc, mộc), but hvdic.thivien.net's exact verbatim transcription (independently corroborated by en.Wiktionary) gives only `mộc` under the genuine "Âm Hán Việt:" line, with the other three exclusively under "Âm Nôm:". Reduced to the single genuine reading `mộc`. No aliases added — en.Wiktionary's only listed alternative form, 沭, is explicitly flagged as "erroneous" rather than a genuine variant.

Rebuilt the malformed Notes (a stray unlinked "Dropped from the Korean HS list in 2000" fact-bullet, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format, folding the Korean-HS-list fact into the closing lookup-page bullet as a parenthetical rather than dropping it. Confirmed citation on `Grade Advanced`, `Old HSK 6`, and `Korean Name ㅁ` (its absence from `Korean HS.md` is consistent with the noted 2000 delisting, not a bug).

Citing word page [[沐浴]] checked and found already clean (`pos: 性詞`, `vietnamese: mộc dục` both filled, no duplicate 品詞) — no edit needed.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 渣 (char) (7377; 872 characters remaining).

### 2026-08-15, iteration 1633 — [[characters/渣 (char)|渣 (char)]]

`mc_id: 0` verified as a genuine "confirmed absent" sentinel: 渣 does not appear anywhere in `CC 0000.md`–`CC 3000.md`. **`pos` and `joyo_level` gaps filled**: `pos` was blank, set to `名詞` ("dregs, lees, sediment" are concretely nominal); `joyo_level` was blank despite en.Wiktionary explicitly classifying 渣 as hyōgai kanji — filled with `表外字`, with a correspondingly missing `Hyōgai` citation added (new sequential item 330). Almost repeated the same ㅈ/ㅅ subsection mixup caught two iterations ago on [[characters/捷|捷]] — 渣's Korean reading 사 belongs under `ㅅ`, not `ㅈ`; checked the correct file first and confirmed it was already cited there.

**`graphemic_classification: 査` reconfirmed correct**: en.Wiktionary names the phonetic as 查, but the vault's own [[characters/査|査]] page already lists 查 as its own doubly-established `aliases` entry — same character, different graphical form — so no discrepancy; confirmed [[characters/査|査]]'s own `Derived Characters` section already correctly lists 渣. `vietnamese: tra` (already filled) double-checked against hvdic's exact verbatim transcription — both "Âm Hán Việt:" and "Âm Nôm:" lines give `tra` identically, no contamination. Checked `aliases`: en.Wiktionary's "second-round simplified form" 泎 and zh.Wiktionary's labeled 異體字 溠 don't overlap at all, so neither was added; existing blank `aliases` correctly left as-is.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard `mc_id: 0` template. Confirmed citation on `Grade Advanced` and `Old HSK 3`. **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[渣]] is a standalone word page — added the section citing it.

Self word page [[渣]] checked and fixed two of the standard recurring bugs: **`vietnamese: null` literal placeholder** (fixed to `tra`, matching the character's own confirmed reading) and **missing `pos` field** (added `名詞`).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 烝 (7379; 871 characters remaining).

### 2026-08-15, iteration 1634 — [[characters/烝|烝]]

**`mc_id` off-by-one fixed**: stored `2123`; the real line for 烝 is `2124`. **`pos`, `joyo_level`, and `korean_native` gaps all filled**: `pos` was blank, set to `名詞` (matching the citing word [[烝民]]'s own `名詞`); `joyo_level` was blank despite en.Wiktionary explicitly classifying 烝 as hyōgai kanji — filled with `表外字`, with a correspondingly missing `Hyōgai` citation added (new sequential item 331); `korean_native` was an empty string — filled with `김 오를` ("for steam to rise"), verified via ko.Wiktionary's own 훈음 gloss, using the same multi-word gloss format already established on [[characters/剃|剃]].

**`graphemic_classification: 丞` reconfirmed correct** (形聲: semantic [[Radical 086|灬]] "fire" + phonetic 丞, Zhengzhang OC \*kljɯŋ/\*kljɯŋs from phonetic \*ɡljɯŋ "to raise") via en.Wiktionary; confirmed the Radical-086-displayed-as-灬 convention matches established precedent (e.g. [[characters/照 (char)|照 (char)]], [[characters/熟|熟]]).

**`aliases` gap filled**: intersecting both sources' variant-form lists (en.Wiktionary: 㷥, 𤇶, 𩟘; zh.Wiktionary's explicitly-labeled 異體字: 㷥, 蒸) gives 㷥 as the sole doubly-corroborated candidate; added (confirmed no independent vault page). 蒸 — despite zh.Wiktionary calling it a variant — was excluded, since it has its own independent, actively-used vault page (the same phonetic-relation-vs-true-alias pattern flagged repeatedly this session).

**`vietnamese` bug found and fixed — a subtler tone-mark error rather than Hán Việt/Nôm contamination**: the stored field held `chưng, chừng`, but hvdic.thivien.net's exact verbatim "Âm Hán Việt:" line gives `chưng, chứng` — the second reading's diacritic was wrong (huyền `chừng` instead of the correct sắc `chứng`); corrected. Both readings are genuinely Hán Việt per hvdic (its own "Âm Nôm:" line lists only `chưng`).

Reordered the malformed page (Words section had been placed before Notes) and rebuilt the malformed Notes (wrong heading level, two bare unlinked CC-lookup wikilinks) into the standard 4-bullet-Notes-then-Words structure. Confirmed citation on `Grade Advanced`, `HSK No`, and `Korean Name ㅈ`.

Citing word page [[烝民]]'s blank `vietnamese` field investigated directly via hvdic for the compound 烝民 — no attested entry found, confirming a genuine gap; left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 焰 (7380; 870 characters remaining).

### 2026-08-15, iteration 1635 — [[characters/焰|焰]]

`mc_id: 5510` is well above the ~4000-entry ceiling of `CC 0000.md`–`CC 3000.md`, trusted long-tail data, left unchanged. **`pos` gap filled**: was blank, set to `名詞`, matching the citing word [[火焰]]'s own `名詞`.

**`graphemic_classification` bug found and fixed**: the stored value `陥` was wrong — both en.Wiktionary and zh.Wiktionary independently identify the true phonetic component as [[臽]] (OC \*kʰloːmʔ, \*ɡroːms), a pageless character distinct from [[characters/陥 (char)|陥 (char)]] (itself a derived character sharing the same phonetic 臽 but with a different semantic radical, "to fall into," and its own independent vault page) — the same sibling-derived-character confusion pattern caught repeatedly this session (屠/者, 掏/陶, 歇/曷). Corrected to `臽`; confirmed 陥 (char)'s own page had no stray cross-reference to clean up.

**`aliases` gap filled**: intersecting both sources' variant-form lists (en.Wiktionary: 焔, 燄, 熖, 爓/𰟘; zh.Wiktionary's explicitly-labeled 異體字 and "其他变体" notes: 㷔, 炎, 燄, 爓, 焔) gives three doubly-corroborated forms — 焔, 燄, 爓 — added all three (confirmed none has an independent vault page). `炎` — despite zh.Wiktionary listing it — was excluded, having its own independent, actively-used vault page (the same phonetic-relation-vs-true-alias pattern flagged repeatedly this session). 㷔 and 熖 were single-source, excluded.

**`vietnamese` contamination bug found and fixed**: the stored field held three readings (dim, diêm, diễm), but hvdic.thivien.net's exact verbatim transcription gives the genuine "Âm Hán Việt:" readings as `diễm, diệm`, with `diêm` and `dim` both under "Âm Nôm:" — reduced to the two genuine readings, recovering the previously entirely-missing `diệm`.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 3`, `Jinmeiyō`, `Korean Name ㅇ` all already correct) — no lookup-page fixes needed this iteration. `## Words` section was already present and correct, citing the sole stand-in [[火焰]].

Citing word page [[火焰]] checked and found already fully clean (`pos: 名詞`, `vietnamese: hỏa diễm` both filled) — no edit needed.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 弒 (7381; 869 characters remaining).

### 2026-08-15, iteration 1636 — [[characters/弒|弒]]

`mc_id: 1050` reconfirmed correct against `CC 1000.md` (no off-by-one). **`pos`, `joyo_level`, and `korean_native` gaps all filled**: `pos` was blank, set to `事詞`, matching the citing word [[弒君]]'s own `事詞`; `joyo_level` was blank despite en.Wiktionary explicitly classifying 弒 as hyōgai kanji — filled with `表外字`, with a correspondingly missing `Hyōgai` citation added (new sequential item 332); `korean_native` was an empty string — filled with `윗사람 죽일` ("to kill one's superior"), verified via ko.Wiktionary's own 훈음 gloss. `hsk_level` was left blank deliberately — not contradicted by any lookup page, and blank is an established alternate convention alongside `無` elsewhere in this vault.

**`graphemic_classification: 式` reconfirmed correct** (形聲: abbreviated semantic [[殺 (char)|殺]] "to kill" + phonetic 式, Zhengzhang OC \*hljɯɡs) via en.Wiktionary; confirmed [[characters/式|式]]'s own `Derived Characters` section already correctly lists 弒. `vietnamese: thí` (already filled) reconfirmed correct — hvdic gives only `thí` with no "Âm Nôm:" line at all, no contamination. Existing alias `弑` (simplified form) reconfirmed correct; zh.Wiktionary's other listed variant, 殺, was excluded as it's a common independent character with its own vault page (the same phonetic/semantic-relation-vs-true-alias pattern flagged repeatedly this session).

**Preserved and properly documented an unusual pre-existing note rather than discarding it as noise**: the malformed Notes held a bare, cryptic fragment "Pronunciation from V" — investigated and confirmed this refers to the character's `hapax` tag and its Dan'a'yo reading (`ti`/ㄊㄧ) having been deliberately taken from the Vietnamese Hán Việt reading `thí` rather than the standard Middle-Chinese-initial-plus-final derivation pipeline (which would give a different syllable from 書+之) — rebuilt into a proper explanatory bullet within the standard format rather than dropped.

Confirmed citation on `Grade Advanced` and `Korean Name ㅅ` (no `HSK` citation expected, matching its blank `hsk_level`). `## Words` section was already present and correct, citing the sole stand-in [[弒君]].

Citing word page [[弒君]]'s blank `vietnamese` field investigated directly via hvdic for the compound 弒君 — no attested entry found, confirming a genuine gap; left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 趨 (char) (7382; 868 characters remaining).

### 2026-08-15, iteration 1637 — [[characters/趨 (char)|趨 (char)]]

`mc_id: 1085` reconfirmed correct against `CC 1000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `動詞`. **`graphemic_classification: 芻` reconfirmed correct** (形聲: semantic [[Radical 156|走]] "run, walk" + phonetic 芻, Zhengzhang OC \*sʰlo) via en.Wiktionary and zh.Wiktionary agreement.

**`aliases` gap filled**: intersecting both sources' variant-form lists (en.Wiktionary: 趍, 騶/驺, 趣, 𧻫, 𧻬, 𨃘, 𧼜, plus simplified 趋; zh.Wiktionary's explicitly-labeled 異體字: 趋, 趍, 趣, 跢) gives 趍 as newly doubly corroborated (in addition to the already-present, already-correct simplified alias 趋); added 趍. `趣` — despite both sources calling it a variant — was excluded, having its own independent, actively-used vault page ("interest, fun," the same phonetic-relation-vs-true-alias pattern flagged repeatedly this session).

**`vietnamese` contamination bug found and fixed**: the stored field held three readings (so, xu, xô), but hvdic.thivien.net's exact verbatim transcription gives only `xu, xúc` under the genuine "Âm Hán Việt:" line, with `so` and `xô` both under "Âm Nôm:" — reduced to the two genuine readings, recovering the previously-missing `xúc`.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 4`, `Hyōgai`, `Korean Name ㅊ` all already correct) — no lookup-page fixes needed. **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[趨]] is a standalone word page — added the section citing it. **Found and fixed a missing `## Derived Characters` section entirely on [[characters/芻|芻]]** (a later, not-yet-perfected character in the sweep, danayo_id 7498) while verifying the phonetic link — added, citing 趨, per this session's practice of fixing directly-discovered consequence bugs on other pages regardless of their own perfection status.

Self word page [[趨]] checked and fixed two of the standard recurring bugs: **`vietnamese: null` literal placeholder** (fixed to `xu`, matching the character's own corrected primary reading) and **missing `pos` field** (added `動詞`).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 讐 (7383; 867 characters remaining).

### 2026-08-15, iteration 1638 — [[characters/讐|讐]]

`mc_id: 1138` reconfirmed correct, with a wrinkle: 讐 itself doesn't appear anywhere in `CC 0000.md`–`CC 3000.md`, but rank 1138 correctly indexes its own alias 讎 instead — both forms represent the same word, so this is a genuine clean match, not a bug. **`pos` gap filled**: was blank, set to `名詞`, matching the citing word [[私讐]]'s own `名詞`.

**`graphemic_classification: 雔` reconfirmed correct** (形聲: semantic [[言 (char)|言]] "speech, words" + phonetic 雔) — an initial en.Wiktionary fetch had reversed which component was semantic vs. phonetic, but re-querying zh.Wiktionary directly confirmed the vault's stored value was right all along and the first fetch was a summarization error, not a genuine discrepancy. Existing alias `讎` reconfirmed correct — zh.Wiktionary explicitly states 讐 is itself a 異體字 of 讎, matching the vault's own alias-direction choice.

**`vietnamese` contamination bug found and fixed**: the stored field held two readings (cừu, thù), but hvdic.thivien.net's exact verbatim transcription gives only `thù` under the genuine "Âm Hán Việt:" line, with `cừu` appearing exclusively under "Âm Nôm:" (en.Wiktionary's own listing doesn't distinguish the two layers, so hvdic's dedicated split was decisive). Reduced to the single genuine reading `thù`.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `Hyōgai`, and `Korean Name ㅅ` (already correctly listed under both alias forms) — no lookup-page fixes needed. `## Words` section was already present and correct, citing the sole stand-in [[私讐]]. Left the blank `boundedness` field untouched — it reflects an internal corpus-frequency metric with no external source to verify or derive it from, unlike the other recurring bug patterns this session.

Citing word page [[私讐]] checked and found already fully clean (`pos: 名詞`, `vietnamese: tư thù` both filled) — no edit needed.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 㪘 (char) (7385; 866 characters remaining).

### 2026-08-15, iteration 1639 — [[characters/㪘 (char)|㪘 (char)]]

`mc_id: 1153` reconfirmed correct, with the same alias-indexing pattern seen on [[characters/讐|讐]] last iteration: 㪘 itself doesn't appear in `CC 0000.md`–`CC 3000.md`, but rank 1153 correctly indexes its traditional form 斂 instead. **`pos` and `joyo_level` gaps filled**: `pos` was blank, set to `動詞`, matching the already-perfected citing word [[㪘]]'s own `動詞`; `joyo_level` was blank despite en.Wiktionary explicitly classifying 㪘 as hyōgai kanji (an "extended shinjitai" form) — filled with `表外字`, with a correspondingly missing `Hyōgai` citation added (new sequential item 333).

**`japanese_native` hyphenation fixed**: stored as the un-hyphenated `おさめる`, corrected to `お-さめる` per the vault's stem-plus-okurigana convention. **`graphemic_classification: 㑒` reconfirmed correct** (形聲: semantic [[Radical 066|攴]] "strike, tap" + phonetic 㑒, itself a shinjitai-simplified stand-in for 僉, the phonetic used in the traditional form 斂) — confirmed 㑒 has its own distinct vault page with the matching reading (qiān), ruling out a bogus phonetic citation.

**`vietnamese` bug found and fixed — both a malformed-YAML issue and contamination**: the stored field held a single string `"kiếm, liễm, liệm"` (a comma-embedded scalar, not a proper list) instead of separate list items; querying hvdic for the traditional form 斂 gives genuine "Âm Hán Việt:" readings `liễm, liệm`, with `kiếm` appearing exclusively under "Âm Nôm:" — fixed to a proper two-item list `[liễm, liệm]`, matching the already-perfected citing word [[㪘]]'s own single `liễm` reading as a subset.

**`aliases` gap filled**: intersecting both sources' variant-form lists (en.Wiktionary: 歛, 㪘 itself, 敛; zh.Wiktionary's explicitly-labeled 異體字: 敛, 歛) gives 歛 as newly doubly corroborated (alongside the already-present, already-correct 斂 and 敛); added 歛 (confirmed no independent vault page).

Reordered the malformed page (Words section had been placed before Notes) and rebuilt the malformed Notes (two bare unlinked CC-lookup wikilinks) into the standard 4-bullet-Notes-then-Words structure. Confirmed citation on `Grade Advanced` and `Korean Name ㄹ`. Left the blank `boundedness` and `hsk_level` fields untouched — neither is contradicted by any lookup page, and both reflect internal metrics with no external source to verify.

Self word page [[㪘]] was already fully perfected (`date-last-perfect: 2026-07-26`) and required no changes.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 仍 (char) (7386; 865 characters remaining).

### 2026-08-15, iteration 1640 — [[characters/仍 (char)|仍 (char)]]

`mc_id: 2122` reconfirmed correct against `CC 2000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `副詞` ("yet, still," a bare adverbial sense). **`graphemic_classification: 乃` reconfirmed correct** (形聲: semantic [[Radical 009|亻]] "person" + phonetic 乃, Zhengzhang OC \*njɯŋ) via en.Wiktionary and zh.Wiktionary agreement — the Notes wikilink needed correcting to `[[乃 (char)|乃]]`, since the actual vault page is filed as `乃 (char).md`.

**`vietnamese` contamination bug found and fixed — the most extreme case this session**: the stored field held eleven readings (dưng, dừng, nhang, nhùng, nhăng, nhưng, nhẳng, nhẵng, nhừng, nhửng, những), but hvdic.thivien.net's exact verbatim transcription gives only `nhưng` under the genuine "Âm Hán Việt:" line — every other stored value, including the very common function word `những` ("several/many," wholly unrelated), was Nôm-layer or unattested noise. Reduced to the single genuine reading `nhưng`.

**Found and fixed the identical severe contamination bug on [[characters/乃 (char)|乃 (char)]] itself** while verifying the phonetic link: its own stored `vietnamese` held eight readings (bèn, náy, nãi, nãy, nải, nảy, nấy, nới), but hvdic's exact verbatim transcription gives the genuine Hán Việt readings as `nãi, ái` — only `nãi` was among the stored values, `ái` was entirely missing, and `bèn` wasn't attested at all. Fixed to `[nãi, ái]`, despite that page already being `date-last-perfect`-stamped from 2026-07-02, evidently predating this session's contamination-checking practice (matching the same pattern found on [[characters/員|員]]/[[characters/運|運]] and [[characters/閣|閣]] earlier). **Also found and fixed a missing `## Derived Characters` section entirely on 乃 (char)** — added, citing 仍.

Rebuilt a heavily malformed page: the Notes section held only two bare unlinked CC-lookup wikilinks, and after a correct `## Words` bullet for the `stand_in` [[仍]], the page continued with several un-headered/loosely-headered prose paragraphs and two ad hoc "## Semantic contrast" / "## Style contrast" sections comparing 仍 to [[仍旧]] — a second, genuine citing word that was never actually added to the Words list itself. Rebuilt the standard 4-bullet Notes, added [[仍旧]] as a second `## Words` entry with a condensed version of the comparison note, and removed the redundant duplicate prose (the same comparison content already lives properly in [[仍旧]]'s own Notes). Confirmed citation on `Grade Advanced`, `Old HSK 2`, and `Korean Name ㅇ`; **found and fixed a missing `Hyōgai` citation** — added as new sequential item 334.

Self word page [[仍]] was already fully perfected (`pos: 副詞` filled, stamped 2026-07-01) but was missing a `vietnamese` field entirely — added `nhưng`, matching the character's own corrected reading, as a direct consequence fix.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 嬌 (7387; 864 characters remaining).

### 2026-08-15, iteration 1641 — [[characters/嬌|嬌]]

`mc_id: 5259` is well above the ~4000-entry ceiling of `CC 0000.md`–`CC 3000.md`, trusted long-tail data, left unchanged. **`pos` gap filled**: was blank, set to `性詞`, matching the citing word [[嬌媚]]'s own `性詞`. **`graphemic_classification: 喬` reconfirmed correct** (形聲: semantic [[Radical 038|女]] "woman" + phonetic 喬, Zhengzhang OC \*krew/\*krewʔ/\*ɡrew) via en.Wiktionary and zh.Wiktionary agreement; `vietnamese: kiều` (already filled) double-checked against hvdic's exact verbatim transcription — both "Âm Hán Việt:" and "Âm Nôm:" lines give `kiều` identically, no contamination. zh.Wiktionary's labeled 異體字 list added two further candidates (姣, 驕) beyond the already-present, doubly-confirmed 娇, but neither was corroborated by en.Wiktionary, so nothing further was added.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 4`, `Hyōgai`, `Korean Name ㄱ` all already correct) — no lookup-page fixes needed. **Found and fixed a missing `## Derived Characters` section on [[characters/喬|喬]]** (a later, not-yet-perfected character in the sweep, danayo_id 8179) while verifying the phonetic link — added, citing 嬌, without otherwise touching 喬's own still-pending perfection.

Citing word page [[嬌媚]] had a blank `vietnamese` field despite its own Notes explicitly documenting the intended mechanical derivation (嬌's own `kiều` + 媚's own `mị`) — no formally-labeled hvdic entry exists for the compound itself, but since the page's own stated logic made the intended value unambiguous, filled it as `kiều mị` rather than leaving a pure gap.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 墟 (7388; 863 characters remaining).

### 2026-08-15, iteration 1642 — [[characters/墟|墟]]

`mc_id: 2512` reconfirmed correct against `CC 2000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `名詞`, matching the citing word [[廃墟]]'s own `名詞`. **`graphemic_classification: 虚` reconfirmed correct** (形聲: semantic [[Radical 032|土]] "earth" + phonetic 虚/虛, Zhengzhang OC \*kʰa) — the actual vault page is `虚 (char).md`, with 虛 already correctly stored as its own alias (the same 査/查-style dual-form pattern seen on [[characters/掏|掏]] earlier this session); confirmed [[characters/虚 (char)|虚 (char)]]'s own `Derived Characters` section already correctly lists 墟.

**`vietnamese: [hư, khư]` reconfirmed correct and left unchanged**: unlike most contamination cases this session, hvdic's exact verbatim transcription shows both readings under *both* the "Âm Hán Việt:" and "Âm Nôm:" lines — a genuine dual Hán-Việt/Nôm classification for both forms, not contamination.

**`aliases` gap filled**: both en.Wiktionary and zh.Wiktionary's explicitly-labeled 異體字 sections agree on 圩 as a genuine variant; added (confirmed no independent vault page).

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 3`, `Hyōgai`, `Korean Name ㅎ` all already correct) — no lookup-page fixes needed. **Found and fixed an entirely missing `## Words` section**: added, citing the sole stand-in [[廃墟]].

Citing word page [[廃墟]]'s blank `vietnamese` field investigated directly via hvdic for the compound 廃墟/廢墟 — no attested entry found, confirming a genuine gap; left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 肋 (7389; 862 characters remaining).

### 2026-08-15, iteration 1643 — [[characters/肋|肋]]

`mc_id: 4864` is well above the ~4000-entry ceiling of `CC 0000.md`–`CC 3000.md`, trusted long-tail data, left unchanged. **`pos` gap filled**: was blank, set to `名詞`, matching the citing word [[肋骨]]'s own `名詞`. **`graphemic_classification: 力` reconfirmed correct** (形聲: semantic [[Radical 130|肉]] "meat, body" + phonetic 力, Zhengzhang OC \*rɯːɡ) via en.Wiktionary; `vietnamese: lặc` (already filled) double-checked against hvdic's exact verbatim transcription — both "Âm Hán Việt:" and "Âm Nôm:" lines give `lặc` identically, no contamination. No corroborated variant forms found by either source (only an unrelated CJK compatibility ideograph), so the existing blank `aliases` is a genuine "no variants" state.

**Found and fixed the identical contamination bug pattern on [[characters/力 (char)|力 (char)]] itself** while verifying the phonetic link: its own stored `vietnamese` held four readings (lực, sức, sực, sựt), but hvdic's exact verbatim transcription gives the genuine Hán Việt reading as `lực` alone, with `sức` and `sựt` under "Âm Nôm:" and `sực` not attested by hvdic at all. Fixed to `[lực]`, despite that page already being `date-last-perfect`-stamped from 2026-04-30, one of the earliest-perfected pages in the vault and evidently long predating this session's contamination-checking practice. **Also found and fixed a missing `## Derived Characters` section entirely on 力 (char)** — added, citing 肋.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `HSK No`, `Jinmeiyō`, and `Korean Name ㄹ`. **Found and fixed an entirely missing `## Words` section**: added, citing the sole stand-in [[肋骨]].

Citing word page [[肋骨]]'s blank `vietnamese` field investigated directly via hvdic for the compound 肋骨 — no attested entry found, confirming a genuine gap; left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 堰 (7390; 861 characters remaining).

### 2026-08-15, iteration 1644 — [[characters/堰|堰]]

`mc_id: 1132` reconfirmed correct, with the same alias-indexing pattern seen repeatedly this session: 堰 itself doesn't appear in `CC 0000.md`–`CC 3000.md`, but rank 1132 correctly indexes its alias 偃 instead. **`pos` gap filled**: was blank, set to `名詞`, matching the already-perfected citing word [[井堰]]'s own `名詞`.

**`graphemic_classification: 妟` investigated carefully and kept**: en.Wiktionary names 匽 as the phonetic, zh.Wiktionary names 偃 — neither matching the vault's stored 妟 at first glance. A direct check of 妟's own en.Wiktionary entry resolved this: 妟 is confirmed as the deepest root of a documented four-character phonetic series (妟→匽→偃→堰, all sharing OC \*qanʔ/\*qans), with 匽 and 偃 being intermediate derived siblings rather than competing "true" phonetics — consistent with the "cite the pageless root, not a derived sibling with its own page" precedent established on [[characters/歇|歇]] (曷) and [[characters/焰|焰]] (臽) earlier this session. `vietnamese: yển` (already filled) reconfirmed correct via hvdic — both lines match identically, no contamination.

Checked `aliases`: existing `偃` reconfirmed correct (matches both the mc_id-indexing and zh.Wiktionary's own named phonetic); zh.Wiktionary's two further candidates (墕, 隁) were single-source, not added.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `Jinmeiyō`, and `Korean Name ㅇ` (no `HSK` citation expected, matching its blank `hsk_level`). **Found and fixed an entirely missing `## Words` section**: added, citing the sole stand-in [[井堰]], which was already fully perfected and required no further changes.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 厩 (7393; 860 characters remaining).

### 2026-08-15, iteration 1645 — [[characters/厩|厩]]

`mc_id: 2186` reconfirmed correct, indexed under its alias 廄 (the same pattern seen repeatedly this session). `pos: 名詞` (already filled) confirmed appropriate; `hanmun_edu_level` left blank as a genuine alternate convention, not contradicted by any lookup page.

**`graphemic_classification: 㲃` investigated carefully and confirmed correct** — a genuinely confusing case: en.Wiktionary's page for the simplified 厩 itself gives phonetic 既, while the further variant 廏 gives phonetic 𣪘, neither matching the vault's stored 㲃. Checking the canonical traditional form 廄 directly (the form the vault's own `mc_id` indexes 厩 under) resolved it: 廄's own etymology explicitly gives phonetic 㲃, exactly matching the vault's stored value — the three orthographic variants (厩/廄/廏) simply redraw or abbreviate the phonetic differently while representing the same word, and the vault's citation is anchored correctly to the indexed canonical form.

**`aliases` gap filled**: en.Wiktionary's full variant list for 廄 (厩, 廐, 廏, 𢋁, 𠤙) and zh.Wiktionary's explicitly-labeled 異體字 for 廄 (厩, 廏, 廐) both include 廏, not previously stored alongside the existing 廄/廐; added (confirmed no independent vault page). `vietnamese: cứu` (already filled) reconfirmed correct via hvdic on the alias form — no contamination.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on `Grade Advanced` and `Jinmeiyō`; **found and fixed two broken redlink citations on `Korean Name ㄱ`**: its listing already included `[[廏]]` and `[[廐]]` as bare wikilinks with no target pages of their own — replaced both with proper links to 厩's actual page. **Found and fixed an entirely missing `## Words` section**: added, citing the sole stand-in [[馬厩]].

Citing word page [[馬厩]] checked: `pos: 名詞` already filled; **fixed a malformed `japanese` field** that held the same reading tripled (`うまや,うまや,うまや`) instead of once; its missing `vietnamese` field investigated directly via hvdic for the compound 馬厩/馬廄 — no attested entry found, confirming a genuine gap; left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 叩 (7394; 859 characters remaining).

### 2026-08-15, iteration 1646 — [[characters/叩|叩]]

**`mc_id` off-by-one fixed**: stored `2030`; the real line for 叩 is `2031`. **`pos` gap filled**: was blank, set to `性詞`, matching the citing word [[叩頭]]'s own `性詞`. **`graphemic_classification: 口` investigated and confirmed correct** — an unusual case where the semantic/phonetic roles are reversed from the visually-obvious guess: en.Wiktionary confirms 口 ("mouth") actually functions as the *phonetic* here, while 卩 ("kneeling person," pageless) is the semantic component — the vault's stored value was right all along.

**`vietnamese` contamination bug found and fixed**: the stored field held two readings (khạo, khấu), but hvdic's exact verbatim transcription gives the genuine "Âm Hán Việt:" reading as `khấu` alone, with `khạo` appearing exclusively under "Âm Nôm:". Reduced to the single genuine reading `khấu`.

**`aliases` gap filled**: intersecting both sources' variant-form lists (en.Wiktionary: 敂, 扣; zh.Wiktionary's explicitly-labeled 異體字: 口 already-cited-as-phonetic, 扣) gives 扣 as doubly corroborated; added (confirmed no independent vault page). 敂 was single-source, excluded.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `HSK No`, and `Hyōgai`. **Found and fixed an entirely missing `## Words` section**: added, citing the sole stand-in [[叩頭]]. **Found and fixed a missing `## Derived Characters` section entirely on [[characters/口 (char)|口 (char)]]** (already `date-last-perfect`-stamped from 2026-07-16) while verifying the phonetic link — added, citing 叩.

Citing word page [[叩頭]] was already fully clean (`pos: 性詞`, `vietnamese: khấu đầu`, `korean: 고두` all filled per its own detailed Notes) — no edit needed.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 剪 (char) (7395; 858 characters remaining).

### 2026-08-15, iteration 1647 — [[characters/剪 (char)|剪 (char)]]

`mc_id: 4439` is well above the ~4000-entry ceiling of `CC 0000.md`–`CC 3000.md`, trusted long-tail data, left unchanged. **`pos` and `joyo_level` gaps filled**: `pos` was blank, set to `名詞` ("scissors"); `joyo_level` was blank despite en.Wiktionary explicitly classifying 剪 as hyōgai kanji — filled with `表外字`, with a correspondingly missing `Hyōgai` citation added (new sequential item 335). **`graphemic_classification: 前` reconfirmed correct** (形聲: semantic [[刀]] "knife" + phonetic 前, Zhengzhang OC \*ʔslenʔ from phonetic \*zleːn — originally 𣦃, later stylized as 前, with the 刀 later reassigned to form this separate character) via en.Wiktionary; both wikilinks needed correcting to their actual filed page names (`刀.md` has no suffix, `前 (char).md` does — opposite of what a naive guess would produce); confirmed [[characters/前 (char)|前 (char)]]'s own Notes and `Derived Characters` section already document this exact split correctly.

**`japanese_native` bug found and fixed**: the stored value was a bare, un-hyphenated `き` — not even a complete reading. Both ja.Wiktionary and Jisho independently confirm two genuine kun-yomi, `き-る` (kiru, "to cut") and `つ-む` (tsumu, "to pick/trim"); replaced the single truncated fragment with the correct two-item hyphenated list.

**`vietnamese` contamination bug found and fixed**: the stored field held `tiễn, tiện`, but hvdic's exact verbatim transcription gives only `tiễn` under both the "Âm Hán Việt:" and "Âm Nôm:" lines — `tiện` isn't attested by hvdic at all. Reduced to `tiễn`; independently corroborated by the already-perfected self word page [[剪]], whose own Notes explicitly document having investigated and rejected `tiện` as likely contamination from the unrelated character 便.

**`aliases` gap filled**: both en.Wiktionary and zh.Wiktionary's explicitly-labeled 異體字 sections agree on 翦 as a genuine variant (beyond the already-excluded 前, which is the phonetic itself with its own distinct vault page); added 翦 (confirmed no independent vault page).

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `Old HSK 2`, and `Korean Name ㅈ`. **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[剪]] is a standalone word page, already fully perfected — added the section citing it.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 儡 (7396; 857 characters remaining).

### 2026-08-15, iteration 1648 — [[characters/儡|儡]]

`mc_id: 7077` is well above the ~4000-entry ceiling of `CC 0000.md`–`CC 3000.md`, trusted long-tail data, left unchanged. **`pos` gap filled**: was blank, set to `名詞`, matching the citing word [[傀儡]]'s own `名詞`. `vietnamese: lỗi` (already filled) reconfirmed correct via hvdic — no contamination.

**`graphemic_classification` bug found and fixed**: the stored value `雷` was wrong — en.Wiktionary and zh.Wiktionary both identify the true phonetic component as [[畾]] (pageless), and checking [[characters/雷 (char)|雷]]'s own already-perfected page confirmed it explicitly treats 畾 (not itself) as the shared phonetic root in its own Notes, with a `Derived Characters` entry for 儡 already correctly present there. Corrected to `畾` — the same sibling-derived-character pattern caught repeatedly this session (屠/者, 掏/陶, 歇/曷, 焰/臽, 堰/妟).

**Found and fixed the identical Vietnamese contamination bug on [[characters/雷 (char)|雷]] itself** while verifying the phonetic link: its own stored `vietnamese` held four readings (loay, loi, lôi, rôi), but hvdic's exact verbatim transcription gives the genuine Hán Việt readings as `lôi, lỗi` — only `lôi` (well, its near-homograph `loi`, without the correct diacritic) was among the stored values, `lỗi` was entirely missing, and `loay`/`rôi` were unattested. Fixed to `[lôi, lỗi]`, despite that page already being `date-last-perfect`-stamped from 2026-08-07 (earlier this same session, showing the contamination check wasn't yet being applied that early on).

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `HSK No`, and `Korean Name ㄹ`; **found and fixed a missing `Hyōgai` citation** — added as new sequential item 336. **Found and fixed an entirely missing `## Words` section**: added, citing the sole stand-in [[傀儡]].

Citing word page [[傀儡]] checked and found already fully clean (`pos: 名詞`, `vietnamese: quỷ lỗi` both filled) — no edit needed.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 誅 (7399; 856 characters remaining).

### 2026-08-15, iteration 1649 — [[characters/誅|誅]]

`mc_id: 304` reconfirmed correct against `CC 0000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `動詞`, matching the citing word [[誅殺]]'s own `動詞`. **`graphemic_classification: 朱` reconfirmed correct** (形聲: semantic [[言 (char)|言]] "speech" + phonetic 朱, Zhengzhang OC \*to from phonetic \*tjo) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/朱|朱]]'s own `Derived Characters` section already lists 誅.

**`vietnamese` contamination bug found and fixed**: the stored field held two readings (tru, trô), but hvdic's exact verbatim transcription gives the genuine "Âm Hán Việt:" reading as `tru` alone, with `trô` appearing exclusively under "Âm Nôm:". Reduced to the single genuine reading `tru`. No new aliases: zh.Wiktionary's only additional candidate beyond the already-present 诛 was single-source (㦵), not added.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on `Hyōgai` and `Korean Name ㅈ`; `Grade Advanced` is dynamic and its blank `hsk_level` isn't contradicted by any lookup page (a genuine alternate-convention gap, not a bug). `## Words` section was already present and correct, citing the sole stand-in [[誅殺]].

Citing word page [[誅殺]]'s blank `vietnamese` field investigated directly via hvdic for the compound 誅殺 — no formally-labeled entry found (only an informal "tru sát" gloss elsewhere on the page), confirming a genuine gap per the established exact-citation bar; left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 擢 (7400; 855 characters remaining).

### 2026-08-15, iteration 1650 — [[characters/擢|擢]]

**`mc_id` off-by-one fixed**: stored `1820`; the real line for 擢 is `1821`. **`pos` gap filled**: was blank, set to `事詞`, matching the citing word [[抜擢]]'s own `事詞`. **`graphemic_classification: 翟` reconfirmed correct** (形聲: semantic [[Radical 064|手]] "hand" + phonetic 翟, Zhengzhang OC \*r'eːwɢ from phonetic \*r'aːwɢ/\*l'eːwɢ) via en.Wiktionary and zh.Wiktionary agreement.

**`vietnamese` contamination bug found and fixed**: the stored field held two readings (dập, trạc), but hvdic's exact verbatim transcription gives only `trạc` under both the "Âm Hán Việt:" and "Âm Nôm:" lines — `dập` wasn't attested by either source at all. Reduced to the single genuine reading `trạc`. No aliases added: zh.Wiktionary's sole candidate (戳) was single-source.

Rebuilt the malformed `## Notes` (two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format, moving it after the pre-existing `## Words` section into the correct order. Confirmed citation on `Grade Advanced`, `Jinmeiyō`, and `Korean Name ㅌ`. **Found and fixed a missing `## Derived Characters` section entirely on [[characters/翟|翟]]** (a later, not-yet-perfected character in the sweep, danayo_id 8586) while verifying the phonetic link — added, citing 擢.

Citing word page [[抜擢]] was already fully clean (`pos: 事詞`, `vietnamese: bạt trạc` both filled) — no edit needed.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 撇 (char) (7401; 854 characters remaining).

### 2026-08-15, iteration 1651 — [[characters/撇 (char)|撇 (char)]]

`mc_id: 9478` is well above the ~4000-entry ceiling of `CC 0000.md`–`CC 3000.md`, trusted long-tail data, left unchanged. `pos: 事詞` (already filled) confirmed appropriate. **`graphemic_classification: 敝` reconfirmed correct** (形聲: semantic [[Radical 064|手]] "hand" + phonetic 敝, Zhengzhang OC \*pʰeːd) via en.Wiktionary and zh.Wiktionary agreement.

**`aliases` bug found and fixed**: the stored `襒` was investigated specifically because it wasn't corroborated by either general variant-form fetch — a direct check of 襒's own zh.Wiktionary page confirmed it as a distinct sibling character sharing the same 敝 phonetic-series root but with its own reading (bié, vs. 撇's piē) and its own semantic radical (衣 "clothing," not 手), **not** a true variant/alias — removed. Intersecting both sources' actual labeled variant sections instead surfaced 撆 (confirmed by both en.Wiktionary and zh.Wiktionary), which was added in its place.

**`japanese_native` bug found and fixed**: stored as the truncated, un-hyphenated `ぬぐ` — both Jisho and general knowledge confirm the genuine kun-yomi is `ぬぐ.う` (nuguu, "to wipe"); corrected to the properly hyphenated `ぬぐ-う`.

**`vietnamese` contamination bug found and fixed**: the stored field held four readings (phiết, phét, phết, phệt), but hvdic's exact verbatim transcription gives only `phiết` under the genuine "Âm Hán Việt:" line — `phét`/`phết` are Nôm-only and `phệt` isn't attested by hvdic at all. Reduced to the single genuine reading `phiết`.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on `Grade Advanced` and `Old HSK 4`; **found and fixed two missing citations**: `Hyōgai` (added as new sequential item 337) and `Korean Name ㅂ`'s `### 별` subsection, which oddly already carried an entry for 襒 pointing at 撇's own page (left untouched, pre-existing and out of scope) but was missing 撇 itself — added. **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[撇]] is a standalone word page — added the section citing it.

Self word page [[撇]] checked and fixed three bugs: **`vietnamese: null` literal placeholder** (fixed to `phiết`), **`korean: "null"` literal string placeholder** — a variant of the same bug pattern, this time appearing in the Korean field instead (fixed to `별`, matching the character), and **missing `pos` field** (added `事詞`).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 柬 (char) (7403; 853 characters remaining).

### 2026-08-15, iteration 1652 — [[characters/柬 (char)|柬 (char)]]

`mc_id: 5112` is well above the ~4000-entry ceiling of `CC 0000.md`–`CC 3000.md`, trusted long-tail data, left unchanged. `pos: 名詞` (already filled) confirmed appropriate; `hanmun_edu_level` left blank as a genuine alternate convention.

**`graphemic_classification` bug found and fixed**: the stored value `指事` (indicative) contradicted the page's own pre-existing Notes bullet, "Components: 束, 八" — a textbook 會意 (ideogrammic compound) structure. En.Wiktionary explicitly confirms 柬 as 會意: 束 ("tie") + 八 ("division, individually"), matching the page's own Notes exactly; corrected the frontmatter field to `會意` to match what the page already documented elsewhere. `vietnamese: giản` (already filled) reconfirmed correct via hvdic — no contamination. No aliases added: zh.Wiktionary's variant candidates (㪝, 揀, 簡) weren't corroborated by en.Wiktionary, and 揀/簡 are independently common characters likely to have their own vault pages regardless.

Rebuilt the malformed `## Notes` (a stray unlinked "Components" bullet mixed with two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format, properly linking [[束 (char)|束]] and [[八 (char)|八]] to their actual vault pages. Confirmed citation on `Grade Advanced` and `Old HSK 4`; **found and fixed a broken citation on `Korean Name ㄱ`**: its existing entry pointed to `words/柬.md` instead of the character page (inconsistent with every neighboring entry on the same line, all linking to `characters/`) — corrected the target. **Found and fixed a missing `Hyōgai` citation** — added as new sequential item 338. **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[柬]] is a standalone word page — added the section citing it. Checked [[characters/束 (char)|束 (char)]]'s own `Derived Characters` section (which tracks phonetic derivatives like 竦, 速) and confirmed 柬 correctly doesn't belong there, since it uses 束 as a semantic component in a 會意 compound, not as a phonetic.

Self word page [[柬]] checked and fixed two of the standard recurring bugs: **`vietnamese: null` literal placeholder** (fixed to `giản`) and **missing `pos` field** (added `名詞`).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 櫛 (char) (7404; 852 characters remaining).

### 2026-08-15, iteration 1653 — [[characters/櫛 (char)|櫛 (char)]]

**`mc_id` off-by-one fixed**: stored `3239`; the real line for 櫛 is `3240`. `pos: 名詞` (already filled) confirmed appropriate. **`graphemic_classification: 節` reconfirmed correct** (形聲: semantic [[木 (char)|木]] "wood" + phonetic 節, Zhengzhang OC \*ʔsriɡ from phonetic \*ʔsiːɡ) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/節 (char)|節 (char)]]'s own `Derived Characters` section already correctly lists 櫛. `vietnamese: trất` (already filled) reconfirmed correct via hvdic — no contamination. No further aliases found beyond the already-present, already-correct simplified 栉.

Rebuilt the malformed `## Notes` (a stray unlinked "Components" bullet mixed with two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `HSK No`, `Jinmeiyō`, `Korean Name ㅈ` all already correct) — no lookup-page fixes needed this iteration. **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[櫛]] is a standalone word page — added the section citing it.

Self word page [[櫛]] checked and fixed two of the standard recurring bugs: **blank `vietnamese`** (filled with `trất`, matching the character) and **missing `pos` field** (added `名詞`).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 槌 (char) (7405; 851 characters remaining).

### 2026-08-15, iteration 1654 — [[characters/槌 (char)|槌 (char)]]

`mc_id: 5656` is well above the ~4000-entry ceiling of `CC 0000.md`–`CC 3000.md`, trusted long-tail data, left unchanged. **`pos` gap filled**: was blank, set to `名詞` ("hammer"). **`korean_native` investigated but left blank**: no corroborated 훈 gloss found on either ko.Wiktionary (404) or zh.Wiktionary's Korean section (bare sound-reading only) — left as a genuine gap rather than guessed. **`graphemic_classification: 追` reconfirmed correct** (形聲: semantic [[木 (char)|木]] "wood" + phonetic 追) via en.Wiktionary and zh.Wiktionary agreement — the Notes wikilink needed correcting to `[[追 (char)|追]]`, since the actual vault page is filed as `追 (char).md`; confirmed its own `Derived Characters` section already correctly lists 槌.

**`vietnamese` contamination bug found and fixed**: the stored field held `chuỳ, dùi`, but hvdic's exact verbatim transcription gives the genuine "Âm Hán Việt:" readings as `chuỳ, truỳ, đôi` — `dùi` is Nôm-only, and the two other genuine readings (`truỳ`, `đôi`) had never been present. Fixed to `[chuỳ, truỳ, đôi]`.

**`aliases` gap filled**: en.Wiktionary's hedge-worded mention of 鎚/椎 as "alternative spellings... etymological relationships unclear" was cross-checked against zh.Wiktionary's explicitly-labeled 異體字 section, which independently confirms 鎚 (but not 椎) — added 鎚 as the doubly-corroborated candidate (confirmed no independent vault page).

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `HSK No`, `Jinmeiyō`, and `Korean Name ㅌ`. **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[槌]] is a standalone word page — added the section citing it.

Self word page [[槌]] checked and fixed two of the standard recurring bugs: **`vietnamese: null` literal placeholder** (fixed to `chuỳ`, the character's primary reading) and **missing `pos` field** (added `名詞`).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 欣 (7406; 850 characters remaining).

### 2026-08-15, iteration 1655 — [[characters/欣|欣]]

**`mc_id` off-by-one fixed**: stored `1917`; the real line for 欣 is `1918`. **`pos` gap filled**: was blank, set to `性詞`, matching the citing word [[欣喜]]'s own `性詞`. **`graphemic_classification: 斤` reconfirmed correct** (形聲: semantic [[Radical 076|欠]] "to lack, yawn" + phonetic 斤, Zhengzhang OC \*qʰɯn from phonetic \*kɯn/\*kɯns) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/斤|斤]]'s own `Derived Characters` section already correctly lists 欣.

**`aliases` gap filled — a three-way intersection**: en.Wiktionary's variant list (訢, 䜣, 忻, 惞) and zh.Wiktionary's explicitly-labeled 異體字 section (俽, 惞, 訢, plus a separately-mentioned 忻) overlap on three forms — 訢, 惞, 忻 — all added (confirmed none has an independent vault page); 俽 and 䜣 were each single-source, excluded. **Found and fixed a broken citation on `Korean Name ㅎ`**: its listing already had a bare `[[忻]]` redlink (now confirmed a genuine alias) — replaced with a proper link to 欣's page.

**`vietnamese` contamination bug found and fixed**: the stored field held four readings (hoen, hân, hơn, hớn), but hvdic's exact verbatim transcription gives only `hân` under the genuine "Âm Hán Việt:" line, with all three others under "Âm Nôm:". Reduced to the single genuine reading `hân`.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, a stray bullet holding the sole Words-section entry) to the standard 4-bullet format plus a proper `## Words` section. Confirmed citation on `Grade Advanced`, `Old HSK 3`, and `Jinmeiyō`.

Citing word page [[欣喜]]'s blank `vietnamese` field investigated directly via hvdic for the compound 欣喜 — no attested entry found, confirming a genuine gap; left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 帚 (7407; 849 characters remaining).

### 2026-08-15, iteration 1656 — [[characters/帚|帚]]

**`mc_id` off-by-one fixed**: stored `3891`; the real line for 帚 is `3892`. **`pos` gap filled**: was blank, set to `名詞`, matching the citing word [[掃帚]]'s own `名詞`. `graphemic_classification: 象形` (already correct — a genuine pictogram, not a phonetic-component name) reconfirmed via en.Wiktionary and zh.Wiktionary, both describing it as a depiction of a broom.

**`aliases` gap filled**: both sources' labeled 異體字/variant lists agree on 箒 and 菷 (en.Wiktionary additionally listed 𦲅, single-source, excluded); added both doubly-corroborated forms (confirmed neither has an independent vault page).

**`vietnamese` contamination bug found and fixed**: the stored field held `chổi, trửu`, but hvdic's exact verbatim transcription gives the genuine "Âm Hán Việt:" readings as `chửu, trửu` — `chổi` is Nôm-only, and the genuine `chửu` had never been present. Fixed to `[chửu, trửu]`.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `HSK No`, and `Hyōgai`; **found and fixed a missing `Korean Name ㅊ` citation** — 帚's Korean reading 추 belongs under `ㅊ`, not `ㅎ`/elsewhere, and its `### 추` subsection had no entry at all; added. While there, **also fixed a stray broken redlink for `[[鎚]]`** in the same subsection — 鎚 was confirmed as [[characters/槌 (char)|槌]]'s alias just one iteration ago, so retargeted it to 槌's actual page instead of leaving it dangling.

Citing word page [[掃帚]]'s missing `vietnamese` field investigated directly via hvdic for the compound 掃帚 — no attested entry found, confirming a genuine gap; left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 巴 (char) (7409; 848 characters remaining).

### 2026-08-15, iteration 1657 — [[characters/巴 (char)|巴 (char)]]

`mc_id: 1565` reconfirmed correct against `CC 1000.md` (no off-by-one). **`radical` bug found and fixed**: stored `已` — a visually near-identical but distinct glyph from the actual Kangxi radical 49, `己` (confirmed against the vault's own `Radical 049.md`, which stores `己`, and against en.Wiktionary's explicit "Kangxi radical 49" citation). **`pos` gap filled**: was blank, set to `名詞`.

**`english` gloss bug found and fixed**: the stored list held `song, tomoe`, but neither en.Wiktionary's 23-sense Chinese definition list nor its Japanese kanji section mention any "song" sense for 巴 at all. Circumstantial confirmation came from [[words/唄|唄]]'s own Notes, which document an almost identical prior contamination incident on a different but similarly-read character in this vault (a stray "song"/"ugh" sense bleeding in from an unrelated word) — strongly suggesting the same kind of copy-paste bleed here. Removed `song`, keeping the well-attested Japanese-specific `tomoe` sense (already used consistently across this page and its citing words).

**`aliases` bug found and fixed**: the stored `吧` was investigated and confirmed via zh.Wiktionary as a *distinct* 形聲 character (口 semantic + 巴 phonetic) with its own independent etymology (a particle contracted from 罷/夫, or a loanword for "bar") — **not** a variant/alias of 巴, the same sibling-vs-alias distinction flagged repeatedly this session. Removed; the existing `笆` (confirmed by zh.Wiktionary's explicitly-labeled 異體字 section) was kept.

**`vietnamese` contamination bug found and fixed**: the stored field held five readings (ba, bơ, bư, bưa, va), but hvdic's exact verbatim transcription gives only `ba` under the genuine "Âm Hán Việt:" line, with `bơ`/`va` under "Âm Nôm:" and `bư`/`bưa` unattested anywhere. Reduced to the single genuine reading `ba`.

Rebuilt the malformed `## Notes` (a bare "Descendants: [[把]]" bullet mixed with two bare unlinked CC-lookup wikilinks) into the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `HSK Beginner`, `Jinmeiyō`, and `Korean Name ㅍ`. **Found and fixed a missing `## Derived Characters` section entirely**: verified [[characters/把|把]], [[characters/芭|芭]], and [[characters/琶|琶]] each genuinely cite 巴 as their own `graphemic_classification` before listing them (replacing the ad hoc "Descendants" bullet, which had only named 把). **Found and fixed a missing self-citation in `## Words`**: this character's `stand_in` is itself — [[巴]] is a standalone word page — added it alongside the pre-existing [[巴基斯坦]] entry.

Self word page [[巴]] checked and fixed the identical bugs found on the character page: the same `song` contamination in its own `english` list (removed), **`vietnamese: null` literal placeholder** (fixed to `ba`), and **missing `pos` field** (added `名詞`).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 鼎 (char) (7410; 847 characters remaining).

### 2026-08-15, iteration 1658 — [[characters/鼎 (char)|鼎 (char)]]

`mc_id: 836` reconfirmed correct against `CC 0000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `名詞`, matching the already-perfected self word page [[鼎]]'s own `名詞`. `graphemic_classification: 象形` (already correct, a genuine pictogram depicting an ancient tripod cauldron) reconfirmed via en.Wiktionary and zh.Wiktionary agreement.

**`vietnamese` contamination bug found and fixed, independently pre-corroborated**: the stored field held four readings (đềnh, đểnh, đễnh, đỉnh), but hvdic's exact verbatim transcription gives only `đỉnh` under the genuine "Âm Hán Việt:" line, with `đềnh` under "Âm Nôm:" and `đểnh`/`đễnh` unattested anywhere. Reduced to `đỉnh` — this exact conclusion was already independently reached and documented in [[words/鼎|鼎]]'s own Notes, which explicitly called out the character page's "noisier 4-item stored set" and picked `đỉnh` as the genuine reading; today's fix simply applies that already-correct reasoning to the character page itself. No aliases added: en.Wiktionary's and zh.Wiktionary's variant lists (𣇓 vs. 𪔂/㫀/鼑/鐤) don't overlap at all.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format, preserving the pre-existing `## Chengyu` section. Confirmed citation on `Grade Advanced`, `HSK No`, `Jinmeiyō`, and `Korean Name ㅈ`. **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[鼎]] is a standalone word page, already fully perfected and explicitly anticipating this exact fix (its own Notes flagged 鼎 (char) as "a tenth character page found in this state this sweep") — added the section citing it.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 杪 (7412; 846 characters remaining).

### 2026-08-15, iteration 1659 — [[characters/杪|杪]]

`mc_id: 4806` is well above the ~4000-entry ceiling of `CC 0000.md`–`CC 3000.md`, trusted long-tail data, left unchanged. **`pos` and `joyo_level` gaps filled**: `pos` was blank, set to `名詞` ("treetop, extremity" — deliberately not matched to the citing word [[杪小]]'s own `性詞`, since that compound uses 杪 in an extended figurative-adjectival sense while the character's own primary gloss is nominal); `joyo_level` was blank despite en.Wiktionary explicitly classifying 杪 as hyōgai kanji — filled with `表外字`, with a correspondingly missing `Hyōgai` citation added (new sequential item 339). `hsk_level`/`hanmun_edu_level` left blank as genuine alternate-convention gaps, not contradicted by any lookup page. **`graphemic_classification: 少` reconfirmed correct** (形聲: semantic [[木 (char)|木]] "wood" + phonetic 少, per the character's own 說文解字 gloss "the utmost end of a tree") via en.Wiktionary and zh.Wiktionary agreement.

**`vietnamese` bug found and fixed — a tone-mark/contamination hybrid**: the stored field held `diễu, miểu`, but hvdic's exact verbatim transcription reveals the genuine "Âm Hán Việt:" reading is actually `diểu` (hỏi tone), not the stored `diễu` (ngã tone) — which turns out to be the *Nôm* form instead. Corrected to `[diểu, miểu]`, both genuinely Hán Việt per hvdic. No aliases found by either source.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, a stray bullet holding the sole Words-section entry) to the standard 4-bullet format plus a proper `## Words` section. Confirmed citation on `Grade Advanced`; **found and fixed a missing `Korean Name ㅊ` citation** — its `### 초` subsection had no entry at all; added.

Citing word page [[杪小]]'s missing `vietnamese` field investigated directly via hvdic for the compound 杪小 — no attested entry found, confirming a genuine gap; left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 黼 (7413; 845 characters remaining).

### 2026-08-15, iteration 1660 — [[characters/黼|黼]]

`mc_id: 2697` reconfirmed correct against `CC 2000.md` (no off-by-one). **`pos` and `joyo_level` gaps filled**: `pos` was blank, set to `名詞`; `joyo_level` was blank despite en.Wiktionary explicitly classifying 黼 as hyōgai kanji — filled with `表外字`, with correspondingly missing `Hyōgai` and `Korean Name ㅂ` citations both added. `graphemic_classification: 甫` (already correct) and `vietnamese: phủ` (already filled, no Nôm line at all per hvdic — genuinely clean) both reconfirmed via en.Wiktionary and zh.Wiktionary.

**`english` gloss bug found and fixed — a striking content error**: the stored gloss was `fufu` (an unrelated African food dish), while both en.Wiktionary and zh.Wiktionary agree 黼 denotes a black-and-white axe-shaped embroidery pattern on ceremonial robes, one of the Twelve Ornaments. Corrected to `axe-pattern embroidery`. **The identical `fufu` contamination was found on two more pages while investigating**: the citing word [[黼黻]] (both its `english` field and its own Etymology bullet glossed both component characters as "fufu") and [[characters/黻|黻]] itself (the very next character in this sweep, danayo_id 7414) — fixed the `english` field on both as a direct, minimal consequence fix, leaving 黻's full perfection pass for its own upcoming iteration.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on `Grade Advanced` and `HSK No`. **Found and fixed an entirely missing `## Words` section**: added, citing the sole stand-in [[黼黻]].

Citing word page [[黼黻]]'s blank `vietnamese` field investigated directly via hvdic for the compound 黼黻 — no attested entry found, confirming a genuine gap; left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 黻 (7414; 844 characters remaining).

### 2026-08-15, iteration 1661 — [[characters/黻|黻]]

`mc_id: 3082` reconfirmed correct against `CC 3000.md` (no off-by-one). **`pos` and `joyo_level` gaps filled**: `pos` was blank, set to `名詞`; `joyo_level` was blank despite en.Wiktionary explicitly classifying 黻 as hyōgai kanji — filled with `表外字`, with correspondingly missing `Hyōgai` and `Korean Name ㅂ` citations both added. `graphemic_classification: 犮` reconfirmed correct (形聲: semantic [[Radical 204|黹]] "embroidery" + phonetic 犮, Zhengzhang OC \*pud). `vietnamese: phất` (already filled) reconfirmed correct — hvdic gives only `phất` as Hán Việt with no Nôm line at all, genuinely clean.

Independently corroborated the `english` fix applied to this character one iteration ago (on [[characters/黼|黼]]'s turn, as a direct consequence fix replacing a stray "fufu" placeholder): en.Wiktionary's own definition for 黻 — "an embroidered figure in black and blue resembling 亞 ... one of the Twelve Ornaments" — matches the corrected `亞-pattern embroidery` gloss exactly. No aliases added: en.Wiktionary's sole variant candidate (𦓗) wasn't corroborated by zh.Wiktionary, which has no labeled 異體字 section at all for this character.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on `Grade Advanced` and `HSK No`. **Found and fixed an entirely missing `## Words` section**: added, citing the sole stand-in [[黼黻]]. **Found and fixed a missing `## Derived Characters` section entirely on [[characters/犮|犮]]** (a much later, not-yet-perfected character in the sweep, danayo_id 8765) while verifying the phonetic link — added, citing 黻.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 鹸 (char) (7415; 843 characters remaining).

### 2026-08-15, iteration 1662 — [[characters/鹸 (char)|鹸 (char)]]

`mc_id: 0` verified as a genuine "confirmed absent" sentinel: 鹸/鹼/碱 don't appear anywhere in `CC 0000.md`–`CC 3000.md`. `pos: 性詞` (already filled) confirmed appropriate. **`graphemic_classification: 㑒` reconfirmed correct** (形聲: semantic [[Radical 197|鹵]] "salt" + phonetic 㑒, a shinjitai simplification of traditional 鹼) via en.Wiktionary and zh.Wiktionary agreement.

**`japanese_native` malformed-YAML bug fixed**: the stored value mixed a bare scalar (`あ`) with an orphan list item (`- あく`) under the same key — both Jisho and general confirmation agree on a single genuine kun-yomi, あ.く (aku); fixed to the properly hyphenated `あ-く`.

**`vietnamese` gap filled — an unusual case, adding rather than removing readings**: the stored field held only `kiềm`, but hvdic's exact verbatim "Âm Hán Việt:" line gives three genuine readings — `dảm, kiềm, thiêm` — with no "Âm Nôm:" line at all to suggest contamination. Added the two missing genuine readings.

**`hsk_level` bug found and fixed**: stored as `無`, but a stray unformatted Notes fragment ("HSK/3, 이름") turned out to be a leftover, never-applied edit note — cross-checked against `lookup/HSK/Old HSK 3.md`, which does list 鹸 (via its aliases 碱/鹼) — corrected `hsk_level` to `"3"` to match, treating this as an incomplete-edit bug rather than the separate-tracking-mechanism pattern seen elsewhere this session, since the stray note itself signals original intent.

Rebuilt the malformed `## Notes` (the stray HSK/이름 fragment, a bare numbered list instead of proper bullets, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on `Grade Advanced`. **Found and fixed three missing citations**: `Old HSK 3` bullet added now that `hsk_level` is corrected; `Hyōgai`, which already had a variant-redirect note ("鹼 --> 鹸") but no numbered entry for 鹸 itself — added as new sequential item 342 (the same pattern caught on [[characters/屏|屏]] earlier this session); and `Korean Name ㅊ`'s `### 첨` subsection, which was missing 鹸 entirely. **Found and fixed an entirely missing `## Words` section**: added, citing both the `stand_in` self-word [[鹸]] and the existing, already-perfected [[鹸素]] (sodium). **Found and fixed a missing `### Descendants` entry on [[characters/㑒|㑒]]** (a later, not-yet-perfected character, danayo_id 8735) — added 鹸 alongside its existing 検 entry, matching that page's own established subsection heading style rather than introducing a different one.

Self word page [[鹸]] checked and fixed two bugs: a duplicate `品詞: 性詞` field exactly redundant with `pos: 性詞` (removed), and an "akali"/"akalai" typo for "alkali" in both `english` and the prose Notes (corrected both instances). [[鹸素]] was already fully perfected and required no changes.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 鬣 (char) (7416; 842 characters remaining).

### 2026-08-15, iteration 1663 — [[characters/鬣 (char)|鬣 (char)]]

`mc_id: 3632` reconfirmed correct against `CC 3000.md` (no off-by-one). **`pos` and `joyo_level` gaps filled**: `pos` was blank, set to `名詞` ("mane, whiskers"); `joyo_level` was blank despite en.Wiktionary explicitly classifying 鬣 as hyōgai kanji — filled with `表外字`, with correspondingly missing `Hyōgai` and `Korean Name ㄹ` citations both added (the latter required creating an entirely new `### 렵` subsection, alphabetically slotted between the existing `### 렴` and `### 령`). **`graphemic_classification: 巤` reconfirmed correct** (形聲: semantic [[Radical 190|髟]] "hair" + phonetic 巤, Zhengzhang OC \*rab) via en.Wiktionary and zh.Wiktionary agreement; zh.Wiktionary's only 異體字 candidate was 巤 itself (the pageless phonetic already correctly cited, not a separate alias), so no new aliases were added.

**`vietnamese` contamination bug found and fixed**: the stored field held `liệp, lạp`, but hvdic's exact verbatim transcription gives only `liệp` under the genuine "Âm Hán Việt:" line, with `lạp` appearing exclusively under "Âm Nôm:". Reduced to the single genuine reading `liệp`.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. Confirmed citation on `Grade Advanced` and `HSK No`. **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[鬣]] is a standalone word page — added the section citing it.

Self word page [[鬣]] checked and fixed three bugs: a blank `品詞:` field (an empty duplicate of the equally-blank `pos:` — removed entirely rather than filling both, since only one canonical field is needed), **missing `pos` value** (filled `名詞`), and **blank `vietnamese`** (filled `liệp`, matching the character's own corrected reading).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 鬚 (7417; 841 characters remaining).

### 2026-08-15, iteration 1664 — [[characters/鬚|鬚]]

`mc_id: 3261` reconfirmed correct against `CC 3000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `名詞`, matching the citing word [[鬚髯]]'s own `名詞`. **`graphemic_classification: 須` reconfirmed correct** (形聲: semantic [[Radical 190|髟]] "hair" + phonetic 須, Zhengzhang OC \*so) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/須|須]]'s own Notes and `Derived Characters` section already document this exact split (鬚 is the original archaic form, later disambiguated from 須's borrowed "must, essential" sense) and already list 鬚 correctly.

**`aliases` gap filled**: intersecting both sources' variant-form/異體字 lists (both include 䰅, 䰑, 須, and 须) gives 䰅 and 䰑 as newly doubly corroborated (alongside the already-present, already-correct simplified alias 须); added both. `須` — despite being confirmed by both sources — was excluded, having its own independent, actively-used vault page tracking a distinct modern sense ("must, essential"), the same phonetic-relation-vs-true-alias pattern flagged repeatedly this session.

**`vietnamese` contamination bug found and fixed**: the stored field held three readings (râu, tu, tua), but hvdic's exact verbatim transcription gives only `tu` under the genuine "Âm Hán Việt:" line, with `râu` and `tua` both under "Âm Nôm:". Reduced to the single genuine reading `tu`.

Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `HSK No`, `Hyōgai`, `Korean Name ㅅ` all already correct) — no lookup-page fixes needed this iteration. Rebuilt the malformed `## Notes` (two bare unlinked CC-lookup wikilinks) to the standard 4-bullet format. `## Words` section was already present and correct, citing the sole stand-in [[鬚髯]].

Citing word page [[鬚髯]]'s blank `vietnamese` field investigated directly via hvdic for the compound 鬚髯 — no attested entry found, confirming a genuine gap; left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 騙 (char) (7418; 840 characters remaining).

### 2026-08-15, iteration 1665 — [[characters/騙 (char)|騙 (char)]]

`mc_id: 0` verified as a genuine "confirmed absent" sentinel: 騙 doesn't appear anywhere in `CC 0000.md`–`CC 3000.md`. **`pos` gap filled**: was blank, set to `事詞` (a transitive "to deceive someone"). **`graphemic_classification: 扁` reconfirmed correct** (形聲: semantic [[馬 (char)|馬]] "horse" + phonetic 扁, Zhengzhang OC \*pʰens) via en.Wiktionary and zh.Wiktionary agreement — the Notes wikilink needed correcting to `[[扁]]`, since the actual vault page is filed as `扁.md`, not `扁 (char).md`; confirmed 扁's own `Derived Characters` section already correctly lists 騙. No new aliases: both sources agree only on the already-present 騗/骗.

**`vietnamese` contamination bug found and fixed**: the stored field held three readings (biền, biển, thiến), but hvdic's exact verbatim transcription gives the genuine "Âm Hán Việt:" readings as `biển, phiến` — `biền` is Nôm-only, and `thiến` isn't attested by either source at all. Fixed to `[biển, phiến]`, recovering the previously-missing genuine `phiến`.

Rebuilt the malformed `# Notes` (a stray unlinked "sound" fragment, two bare unlinked CC-lookup wikilinks) to the standard `mc_id: 0` template. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 2`, `Hyōgai`, `Korean Name ㅍ` all already correct) — no lookup-page fixes needed. **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[騙]] is a standalone word page — added the section citing it.

Self word page [[騙]] checked and fixed four bugs: a blank `品詞:` field (empty duplicate of the equally-blank `pos:` — removed), **missing `pos` value** (filled `事詞`), **blank `vietnamese`** (filled `phiến`, matching the character's own corrected primary reading), and an **"defraid" typo** for "defraud" in the `english` list.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 駝 (7419; 839 characters remaining).

### 2026-08-15, iteration 1666 — [[characters/駝|駝]]

`mc_id: 3992` reconfirmed correct against `CC 3000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `性詞`, matching the citing word [[駝背]]'s own `性詞` for the "hunchbacked" sense. **`graphemic_classification` bug found and fixed — the session's major recurring bug category, this time cascading across four characters**: stored as `蛇`, but both en.Wiktionary and zh.Wiktionary agree the true phonetic root is **它** (OC \*l̥ʰaːl), the original pictogram of a snake, with 蛇 itself being 它's own derivative (semantic [[Radical 142|虫]] + phonetic 它) — confirmed decisively by [[characters/蛇 (char)|蛇 (char)]]'s own existing Notes, which already states this explicitly. Corrected to `它`.

**Cascading consequence check across the whole 它/蛇 phonetic family**: since 蛇 (char)'s own Notes prove 它 (not 蛇) is the shared root, every character citing 蛇 as its `graphemic_classification` was actually citing a sibling rather than the true root. Checked all four characters listed in 蛇 (char)'s `## Derived Characters` section — [[characters/舵 (char)|舵]] (already correctly `它` from an earlier iteration this session), [[characters/拖|拖]] and [[characters/陀|陀]] (both still wrongly stored `蛇`, both fixed to `它` as minimal consequence edits; neither is otherwise perfected yet), and 駝 itself. **Removed the entire `## Derived Characters` section from [[characters/蛇 (char)|蛇 (char)]]**, since none of the four are actually descendants of 蛇 — they're phonetic siblings via 它, one generation further back.

**`vietnamese` gap filled — adding rather than removing**: the stored field held only `đà`, but hvdic's exact verbatim "Âm Hán Việt:" line gives two genuine readings, `trì, đà` (with `đà` also appearing under "Âm Nôm:", making it dual-classified rather than contaminated). Added the missing genuine `trì`.

**`aliases` gap filled**: both en.Wiktionary and zh.Wiktionary agree on variant forms 駞, 𫘞, and 𩣾 alongside the already-present simplified 驼; confirmed none of the three have their own vault pages, so all three added.

Rebuilt the malformed `# Notes` (wrong heading level, a stray ruby-formatted word citation standing in for a proper `## Words` section, two bare unlinked CC-lookup wikilinks) into the standard 4-bullet format, cross-referencing the shared 它 series via [[舵 (char)|舵]] and [[陀]] the same way [[舵 (char)|舵]]'s own Notes already do. Added the missing `## Words` section citing [[駝背]]. **Found and fixed a missing `Hyōgai` citation**: `joyo_level: 表外字` had no corresponding numbered entry in `Lookup/Japanese/Hyōgai.md` — added as new sequential item 344. `Korean Name ㅌ`'s `### 타` subsection already correctly cited 駝; no fix needed there.

Citing word page [[駝背]] was already fully perfected (checked, no bugs found).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 饅 (7421; 838 characters remaining).

### 2026-08-15, iteration 1667 — [[characters/饅|饅]]

`mc_id: 0` verified as a genuine "confirmed absent" sentinel: 饅/馒 don't appear anywhere in `CC 0000.md`–`CC 3000.md`. **`graphemic_classification: 曼` reconfirmed correct** (形声: semantic [[Radical 184|食]] "food" + phonetic 曼, OC \*moːn) via en.Wiktionary and zh.Wiktionary agreement — unlike the sibling/root confusion found on several other characters this session, [[characters/曼|曼]] is itself the genuine root (`graphemic_classification: 會意`, an independent ideogrammic compound, not a phonetic derivative of anything else), so no misattribution here. **`aliases` reconfirmed complete**: both sources agree on exactly 馒 and 䊡 (already present); en.Wiktionary's third candidate 𪍩 was explicitly checked against zh.Wiktionary's 異體字 list and found absent there, so correctly excluded per the dual-source policy. `vietnamese: man` reconfirmed correct — hvdic's exact verbatim transcription shows `man` under both "Âm Hán Việt:" and "Âm Nôm:" simultaneously, a genuine dual-classification (the same non-contamination pattern seen on [[characters/墟|墟]] earlier this session), not a bug.

Normalized four `../lookup/...`-prefixed relative links in the Notes bullets to the vault's dominant bare `Lookup/...` convention (1900 files use the bare form vs. 662 using the `../` form vault-wide; fixed only this character's own page, out of scope to sweep the rest). Added the missing `mc_id: 0` sentinel sentence to the MC bullet (present on other perfected pages, was missing here). **Found and fixed an entirely missing `## Words` section**: added, citing the `stand_in` [[饅頭]]. **Found and fixed a missing `## Derived Characters` entry on [[characters/曼|曼]]** (a later, not-yet-perfected character, danayo_id 8150) — the section didn't exist at all yet; created it and added 饅, per the checklist's explicit instruction not to assume the section doesn't apply just because a page never had one before.

Citing word page [[饅頭]] checked and fixed one bug: `english: wonton` was a content error (饅頭 is "steamed bun," not "wonton," which is 餛飩/雲吞) — corrected to `steamed bun`.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 颯 (char) (7422; 837 characters remaining).

### 2026-08-15, iteration 1668 — [[characters/颯 (char)|颯 (char)]]

`mc_id: 3883` reconfirmed correct against `CC 3000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `名詞` ("gale," matching the self-word). **`graphemic_classification: 立` reconfirmed correct** (形声: semantic 風 "wind" + phonetic 立) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/立 (char)|立]]'s own `## Derived Characters` section already correctly lists 颯. **`aliases` gap filled**: both sources agree on 飒 (already present) and 䬃 (newly added, confirmed no vault page of its own).

**`vietnamese` contamination bug found and fixed**: the stored field held `bùng, táp`, but hvdic's exact verbatim transcription gives only `táp` under the genuine "Âm Hán Việt:" line; `bùng` appears exclusively under "Âm Nôm:". Reduced to the single genuine reading `táp`.

**Significant discovery, deferred**: verifying the semantic-component radical citation surfaced that [[Lookup/Radicals/Radical 182]] — which both the vault's master `Radicals.md` index and [[characters/風 (char)|風 (char)]]'s own already-perfected page agree should be 風 — currently contains content describing 飛 instead, and the mislabeling cascades onward (`Radical 183.md` holds 首's content instead of 飛's; `Radical 185.md` and `Radical 189.md` both currently hold 高's content). This is a real, bounded-but-nontrivial content bug in the Radical lookup pages around 182–190, independent of any single character's perfection. Not fixed this iteration — flagged here for a dedicated future pass, since untangling the full chain (which file's content belongs where) needs more investigation than a single-character consequence fix warrants. My own Notes bullet on 颯 links to `Radical 182` regardless, matching the vault's established/intended numbering (per the master index and 風 (char)'s precedent), not the page's current (wrong) content.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, no SKIP/MC/levels bullets at all) into the standard 4-bullet format, cross-referencing the 立-phonetic family via [[拉 (char)|拉]] and [[粒]]. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `HSK No`, `Jinmeiyō`, `Korean Name ㅅ` all already correct). **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[颯]] is a standalone word page — added the section citing it.

Self word page [[颯]] checked and fixed two bugs: `vietnamese: null` literal placeholder (fixed to `táp`, matching the character's own corrected reading), and a missing `pos` field entirely (filled `名詞`).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 鞭 (7423; 836 characters remaining).

### 2026-08-15, iteration 1669 — [[characters/鞭|鞭]]

**`mc_id` off-by-one bug found and fixed**: stored as `2253`, but 鞭 actually appears as the 2254th entry in `CC 2000.md` (`2254. 鞭`) — corrected to `2254`. **`middle_chinese_final` typo found and fixed**: stored as `"iᴇn "` with a trailing space (cross-checked against several other characters sharing the same 仙A三開 rime — none carry a trailing space); trimmed to `"iᴇn"`. **`pos` gap filled**: was blank, set to `動詞`, matching the citing word [[鞭打]]'s own `動詞`. **`graphemic_classification: 便` reconfirmed correct** (形声: semantic [[Radical 177|革]] "leather" + phonetic 便, OC \*ben/\*bens) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/便 (char)|便 (char)]]'s own `## Derived Characters` section already correctly lists 鞭.

**`aliases` gap filled**: both sources agree on four variant forms — 鞕, 𠓥, 𠓠, 𩌻 — all newly added (aliases field was previously empty); confirmed none have their own vault pages. Excluded 卞 (en.Wiktionary's odd "second-round simplified form" claim, not corroborated by zh.Wiktionary, and 卞 is itself an independent vault character with a distinct meaning) and 𩋸 (zh.Wiktionary-only, not corroborated by en.Wiktionary).

**`vietnamese` contamination bug found and fixed — a more severe case than usual**: the stored field held `roi, tiệm`, but hvdic's exact verbatim transcription gives the genuine "Âm Hán Việt:" reading as `tiên` alone — a reading that was entirely missing from storage. `tiệm` is Nôm-only per hvdic's own "Âm Nôm:" line; `roi` turned out not to be a reading at all, but the plain Vietnamese gloss ("cái roi," "a whip") that had been mistakenly stored as if it were a pronunciation. Replaced both with the single genuine reading `tiên`.

Reordered the `## Words` section (which had incorrectly preceded `## Notes`) and rebuilt the malformed Notes into the standard 4-bullet format (was missing the SKIP/stroke, MC-ranking, and levels bullets entirely; fixed the bare `[[便 (char)]]` link to properly display as `便`). Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 4`, `Jinmeiyō`, `Korean Name ㅍ`'s `### 편` subsection all already correct).

Citing word page [[鞭打]] checked and fixed one bug: an entirely missing `vietnamese` field — hvdic has a direct compound entry for 鞭打 giving `tiên đả`; added.

**Significant discovery from the previous iteration remains open**: the Radical 182–190 mislabeling (flagged perfecting [[characters/颯 (char)|颯]]) is still unaddressed — noting again here since it affects [[Radical 177|177]]'s neighbors, though 177 (革) itself, cited in this iteration's own graphemic bullet, was independently verified correct and is not part of that cascade.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 鞘 (7424; 835 characters remaining).

### 2026-08-15, iteration 1670 — [[characters/鞘|鞘]]

`mc_id: 9772` confirmed to be a genuine trusted long-tail value (beyond the vault's tracked `CC 0000`–`CC 3000` range, not independently verifiable). **`pos` gap filled**: was blank, set to `名詞`, matching both citing words [[刀鞘]] and [[翅鞘]]'s own `名詞`. **`graphemic_classification: 肖` reconfirmed correct** (形声: semantic [[Radical 177|革]] "leather" + phonetic 肖) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/肖|肖]]'s own `## Derived Characters` section already correctly lists 鞘.

**`aliases` gap filled, with a source-conflict resolution**: zh.Wiktionary's 異體字 list (削, 箾, 鞩, 韒) conflicted with en.Wiktionary, which explicitly denied any of those being variants except 鞩 — a follow-up fetch clarified that 削/箾/韒 are merely *other characters sharing the same 肖 phonetic series*, not true variants of 鞘 itself (and 削 is independently confirmed to have its own distinct vault page, the same false-positive pattern flagged repeatedly this session). Added only the one genuinely dual-corroborated candidate, 鞩 (no vault page of its own).

**`vietnamese` gap filled — adding rather than removing**: the stored field held only `sao`, but hvdic's exact verbatim "Âm Hán Việt:" line gives two genuine readings, `sao, tiếu` (with `sao` also appearing under "Âm Nôm:", making it dual-classified rather than contaminated, the same pattern as [[characters/墟|墟]] and [[characters/饅|饅]] earlier this session). Added the missing genuine `tiếu`.

Rebuilt the malformed `## Notes` (a redundant duplicate bullet restating the same graphemic info already in bullet 1, no SKIP/MC/levels bullets at all, and a stray empty English gloss `("")` in the graphemic bullet) into the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `HSK No`, and `Jinmeiyō`. **Found and fixed a missing `Korean Name ㅊ` citation**: the `### 초` subsection existed but had no entry for 鞘 at all (its `korean: 초` field pointed to the ㅊ-consonant subsection, not the danayo-syllable-derived ㅅ subsection its `諺文: 소` might suggest at a glance) — added.

Citing word pages [[刀鞘]] (already fully perfected) and [[翅鞘]] (missing only `date-last-perfect`, itself a separate word-perfecting concern outside this loop's scope) checked; [[翅鞘]]'s blank `vietnamese` field investigated directly via hvdic — no compound entry exists, confirming a genuine gap, left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 靖 (7425; 834 characters remaining).

### 2026-08-15, iteration 1671 — [[characters/靖|靖]]

`mc_id: 1664` reconfirmed correct against `CC 1000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `名詞`, matching the citing word [[綏靖]]'s own `名詞`. **`graphemic_classification: 青` reconfirmed correct** (形声: semantic [[立 (char)|立]] "stand" + phonetic 青) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/青 (char)|青 (char)]]'s own `## Derived Characters` section already correctly lists 靖. [[characters/立 (char)|立]]'s own `Derived Characters` list was checked too but correctly does NOT include 靖, since that section tracks phonetic citations (matching each listed character's own `graphemic_classification`) and 立 here is only 靖's semantic component, not its phonetic one — consistent with the section's existing entries, all of which use 立 phonetically.

**`aliases` — a source-conflict correctly resolved to "add nothing"**: zh.Wiktionary's 異體字 list (靜/静, 竫, 竧, 𩇕, 㣏, 𫕼, 靚) was NOT corroborated by en.Wiktionary, which has no dedicated "Alternative forms" section for 靖 at all — it only notes 靖 is "Same word as 靜" in a glyph-origin/phonetic-series context, a looser etymological-doublet relationship, not a formal variant citation. 靜/静 is also independently confirmed to be an existing, distinctly-meaningful vault character ([[characters/静|静]], "quiet, calm"), the same false-positive exclusion pattern flagged repeatedly this session. Left `aliases` empty rather than trusting the single-source list.

**`vietnamese` gap filled — adding rather than removing**: the stored field held only `tịnh`, but hvdic's exact verbatim "Âm Hán Việt:" line gives two genuine readings, `tĩnh, tịnh` (with `tịnh` also appearing under "Âm Nôm:", the same dual-classification pattern seen repeatedly this session). Added the missing genuine `tĩnh`.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, no other bullets at all) into the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `HSK No`, `Jinmeiyō`, `Korean Name ㅈ`'s `### 정` subsection all already correct). **Found and fixed an entirely missing `## Words` section**: added, citing the `stand_in` [[綏靖]].

Citing word page [[綏靖]] was already fully perfected (checked, no bugs found).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 鑼 (7426; 833 characters remaining).

### 2026-08-15, iteration 1672 — [[characters/鑼|鑼]]

`mc_id: 0` verified as a genuine "confirmed absent" sentinel: 鑼/锣 don't appear anywhere in `CC 0000.md`–`CC 3000.md`. **`pos` gap filled**: was blank, set to `名詞`, matching the citing word [[銅鑼]]'s own `名詞`. **`graphemic_classification: 羅` reconfirmed correct** (形声: semantic [[Radical 167|金]] "metal" + phonetic 羅) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/羅|羅]]'s own `## Derived Characters` section already correctly lists 鑼. `aliases: 锣` reconfirmed complete — en.Wiktionary's only other candidate, 𬫤, is explicitly noted on its own page as nonexistent ("page does not exist") and isn't corroborated by zh.Wiktionary at all. `vietnamese: la` reconfirmed correct — hvdic shows `la` as both genuine Hán Việt and Nôm simultaneously (dual-classified, not contaminated). `joyo_level` confirmed genuinely blank (no fix needed): searched all Japanese classification lookup files (Jōyō grades, Jinmeiyō, Hyōgai) and 鑼 appears in none of them, consistent with the empty field.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, no other bullets at all) into the standard 4-bullet format. Confirmed citation on `Grade Advanced` and `Old HSK 3`. **Found and fixed a missing `Korean Name ㄹ` citation**: the `### 라` subsection existed but had no entry for 鑼 — added. **Found and fixed an entirely missing `## Words` section**: added, citing the `stand_in` [[銅鑼]].

Citing word page [[銅鑼]] checked and fixed two bugs: a duplicate `品詞: 名詞` field exactly redundant with `pos: 名詞` (removed), and an entirely missing `korean` field (filled `동라`, compositional from [[銅 (char)|銅]]'s own `동` + 鑼's own `라`, matching the already-correct stored `諺文: 동라`). Its blank `vietnamese` field was investigated directly via hvdic for the compound 銅鑼 — no attested entry found, confirming a genuine gap; left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 鋏 (char) (7427; 832 characters remaining).

### 2026-08-15, iteration 1673 — [[characters/鋏 (char)|鋏 (char)]]

`mc_id: 5392` confirmed to be a genuine trusted long-tail value (beyond the vault's tracked `CC 0000`–`CC 3000` range). **`graphemic_classification: 夹` reconfirmed correct, with a notable vault quirk observed**: both en.Wiktionary and zh.Wiktionary agree the phonetic is 夾/夹, and this vault's own page for that component is unusually filed under the *simplified* glyph [[characters/夹|夹]] (with traditional 夾 stored only as an alias) — the reverse of the vault's normal traditional-primary convention, but confirmed correct and consistent since 夹.md's own `aliases` field lists 夾. Fixed 鋏's own Notes bullet, which had linked to the non-existent `[[夾]]`, to correctly link `[[夹]]` instead.

**`vietnamese` bug found and fixed — a mixed case, both adding and removing**: the stored field held `kiệp, kẹp`, but hvdic's exact verbatim transcription gives the genuine "Âm Hán Việt:" readings as `giáp, khiếp, kiệp` (with `kiệp` also appearing under "Âm Nôm:," making it dual-classified) and `kẹp` appearing exclusively under "Âm Nôm:." Removed the Nôm-only `kẹp` and added the two previously-missing genuine readings `giáp` and `khiếp`.

**`aliases` gap filled**: both sources agree on the already-present simplified 铗 and a second candidate, 𨦇 (a Japanese shinjitai-style simplification also independently corroborated by both), newly added; excluded 矢床 (a multi-character Japanese compound word for a specific "yattoko" sense, not a single-character variant, so out of scope for this field).

Rebuilt the malformed `## Notes` (CC-lookup bullets preceding the graphemic/component bullets, wrong order, no SKIP/stroke or levels bullets at all) into the standard 4-bullet format, preserving the existing cross-reference to the near-synonym [[鉗]]. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `HSK No`, `Hyōgai`, `Korean Name ㅎ`'s `### 협` subsection all already correct). **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[鋏]] is a standalone word page — added the section citing it.

Self word page [[鋏]] checked and fixed one bug: `vietnamese: null` literal placeholder (fixed to `kiệp`, the dual Hán-Việt/Nôm reading judged the best fit for the concrete "tongs" sense, matching the character's own corrected reading set).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 鉦 (7428; 831 characters remaining).

### 2026-08-15, iteration 1674 — [[characters/鉦|鉦]]

`mc_id: 4544` confirmed to be a genuine trusted long-tail value (beyond the vault's tracked `CC 0000`–`CC 3000` range). **`pos` gap filled**: was blank, set to `名詞`, matching the citing word [[鉦鼓]]'s own `名詞`. **`graphemic_classification: 正` reconfirmed correct** (形声: semantic [[Radical 167|金]] "metal" + phonetic 正) via en.Wiktionary and zh.Wiktionary agreement. `aliases: 钲` reconfirmed complete — en.Wiktionary's only other candidate, 錚/铮 ("bell"), wasn't corroborated by zh.Wiktionary and is itself a distinct character (excluded, consistent with the established false-positive pattern).

**`vietnamese` contamination bug found and fixed**: the stored field held `chinh, chiêng`, but hvdic's exact verbatim transcription gives the genuine "Âm Hán Việt:" reading as `chinh` alone (also dual-classified, appearing under "Âm Nôm:" too); `chiêng` is Nôm-only. Reduced to the single genuine reading `chinh`.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, no other bullets at all) into the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `HSK No`, `Hyōgai`, `Korean Name ㅈ`'s `### 정` subsection all already correct). **Found and fixed an entirely missing `## Words` section**: added, citing the `stand_in` [[鉦鼓]]. **Found and fixed a missing `## Derived Characters` entry on [[characters/正 (char)|正 (char)]]** (already perfected earlier this session, danayo_id much lower at an earlier point in the sweep) — its existing list (定, 征, 症) was missing 鉦; added.

Citing word page [[鉦鼓]] was already fully perfected (checked, no bugs found).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 跆 (7429; 830 characters remaining).

### 2026-08-15, iteration 1675 — [[characters/跆|跆]]

`mc_id: 0` verified as a genuine "confirmed absent" sentinel: 跆 doesn't appear anywhere in `CC 0000.md`–`CC 3000.md`. `joyo_level` confirmed genuinely blank: searched all Japanese classification lookup files and 跆 appears in none, consistent with the empty field. **`pos` gap filled**: was blank; the citing word [[跆籍]]'s own `名詞` reflects a drifted, extended nominal sense ("Taekwondo registration record"), distinct from 跆's own core verbal meaning ("trample, kick") — set to `事詞` for the character's own transitive-action sense instead, the same drifted-sense exception pattern seen on [[characters/杪|杪]] earlier this session. **`graphemic_classification: 台` reconfirmed correct** (形声: semantic [[Radical 157|足]] "foot" + phonetic 台) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/台 (char)|台 (char)]]'s own `## Derived Characters` section already correctly lists 跆. No aliases found by either source; left empty.

**`vietnamese` gap filled — an entirely empty field**: hvdic's exact verbatim transcription gives the genuine "Âm Hán Việt:" reading `đài`, with no "Âm Nôm:" line at all. Filled the previously-empty field with this single genuine reading.

Rebuilt the malformed `## Notes` (only two bare unlinked CC-lookup wikilinks, no other bullets at all) into the standard 4-bullet format, cross-referencing the 台-phonetic family via [[苔 (char)|苔]], [[殆]], and [[鮐]]. Confirmed citation on `Grade Advanced`, `HSK No`, and `Korean Name ㅌ`.

Citing word page [[跆籍]] checked and fixed one bug: an entirely missing `vietnamese` field — hvdic has a direct compound entry for 跆籍 (a coincidental classical-usage attestation, "chà đạp, dẫm đạp, tàn phá," distinct from but compatible with the vault's Taekwondo-registration neologism sense) giving `đài tạ`; added.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 赳 (7430; 829 characters remaining).

### 2026-08-15, iteration 1676 — [[characters/赳|赳]]

`mc_id: 4137` confirmed to be a genuine trusted long-tail value (beyond the vault's tracked `CC 0000`–`CC 3000` range). **`pos` gap filled**: was blank, set to `性詞`, matching the citing word [[赳赳]]'s own `性詞`. **`graphemic_classification: 丩` reconfirmed correct** (形声: semantic [[Radical 156|走]] "run" + phonetic 丩, a pageless root cited directly, same as several other pageless phonetics found this session) via en.Wiktionary and zh.Wiktionary agreement. `vietnamese: củ` reconfirmed correct — hvdic shows `củ` as both genuine Hán Việt and Nôm simultaneously (dual-classified). No aliases added: en.Wiktionary's two candidates (𠡟, 𧺇) weren't corroborated by zh.Wiktionary, so left empty per the dual-source policy.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, no other bullets at all) into the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `HSK No`, `Jinmeiyō`, `Korean Name ㄱ` all already correct). `## Words` section was already present and correct, citing the sole stand-in [[赳赳]].

Citing word page [[赳赳]] was already fully perfected; its blank `vietnamese` field was investigated directly via hvdic for the reduplicated compound — no attested entry found, confirming a genuine gap, left untouched. Left the blank `boundedness` field on 赳 itself untouched, consistent with this session's practice of not addressing that field (a large fraction of never-perfected characters share the same blank value, suggesting a separate systematic pass rather than a per-character bug).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 謗 (7431; 828 characters remaining).

### 2026-08-15, iteration 1677 — [[characters/謗|謗]]

`mc_id: 1651` reconfirmed correct against `CC 1000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `事詞`, matching the citing word [[誹謗]]'s own `事詞`. **`graphemic_classification: 旁` reconfirmed correct** (形声: semantic [[言 (char)|言]] "speech" + phonetic 旁) via en.Wiktionary and zh.Wiktionary agreement; a link in the Notes bullet needed correcting to `[[旁]]`, since the actual vault page is filed as `旁.md`, not `旁 (char).md`.

**`aliases` bug found and fixed — a synonym mistakenly stored as a variant**: the stored field held `譖, 谤`; only `谤` (the simplified form) is corroborated by either source. `譖` (zèn) was independently verified to be a completely different, unrelated character — different phonetic component (朁, not 旁), different Old Chinese pronunciation, its own distinct meaning ("to slander by false accusation") and its own alternative forms (譛, 谮) — a plausible-but-wrong synonym conflated with a true graphemic variant. Removed.

**`vietnamese` contamination bug found and fixed**: the stored field held `báng, bướng`, but hvdic's exact verbatim transcription gives the genuine "Âm Hán Việt:" reading as `báng` alone; `bướng` appears exclusively under "Âm Nôm:" (alongside a third form, `bang`, not previously stored and not added, since it wasn't part of the existing data and isn't itself Hán Việt). Reduced to the single genuine reading `báng`.

Rebuilt the malformed `# Notes` (wrong heading level, a bare stand-in wikilink with no gloss instead of a proper `## Words` entry, two bare unlinked CC-lookup wikilinks) into the standard 4-bullet format plus a corrected `## Words` section. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 4`, `Hyōgai`, `Korean Name ㅂ` all already correct). **Found and fixed a missing `## Derived Characters` section on [[characters/旁|旁]]** (a later, not-yet-perfected character) — the section didn't exist at all; created it and added 謗.

**`#cranberry` tag reconfirmed valid**: checked [[characters/誹|誹]]'s own `stand_in` field — also `誹謗` — confirming transitivity (誹 = 謗 = 誹謗 as the shared stand-in), the condition required for the tag per this vault's own convention.

Citing word page [[誹謗]] was already fully perfected; its own Notes already documents a corrected 注音 (`ㄈㄧㄆㄚㄫ`, not `ㄆㄧㄆㄚㄫ`) — used the correct, corrected form when citing it in 謗's own `## Words` entry rather than a naive guess from 謗's own reading alone.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 蕩 (7432; 827 characters remaining).

### 2026-08-15, iteration 1678 — [[characters/蕩|蕩]]

**`mc_id` off-by-one bug found and fixed**: stored as `1498` (which actually belongs to a different character, 歆), but 蕩 is the 1499th entry in `CC 1000.md` — corrected to `1499`. **`pos` gap filled**: was blank, set to `性詞`, matching the citing word [[放蕩]]'s own `性詞`. **`graphemic_classification: 湯` reconfirmed correct** (形声: semantic [[Radical 140|艸]] "grass" + phonetic 湯) via en.Wiktionary and zh.Wiktionary agreement; fixed the Notes bullet's link, which needed to point to `[[湯 (char)|湯]]` since the actual vault page carries the `(char)` disambiguator; confirmed [[characters/湯 (char)|湯 (char)]]'s own `## Derived Characters` section already correctly lists 蕩.

**`aliases` gap filled — with conservative resolution of a noisy source**: both sources agree on the already-present simplified 荡, plus 蘯 (added). A second candidate, 盪 — not explicitly in zh.Wiktionary's own 異體字 list on a first pass, but independently corroborated by this **vault's own existing HSK lookup data**, which already treats 盪 as pointing to 蕩's page — was added on that internal-precedent basis. Three further zh-only candidates (偒, 簜, 潒, plus a likely rendering artifact 荄) were NOT added: single-source, unconfirmed by en.Wiktionary, and not worth the risk of compounding a possible OCR/extraction error from the fetch.

**`vietnamese` bug found and fixed — the session's most heavily contaminated case yet**: the stored field held six readings (dãng, thững, vảng, đãng, đẵng, đững), but hvdic's exact verbatim transcription gives only two genuine "Âm Hán Việt:" readings, `đãng, đảng` — `đãng` also dual-classified under "Âm Nôm:," while `dãng, thững, vảng, đẵng` are Nôm-only, and `đững` doesn't appear in hvdic's entry at all (an apparent invented/erroneous form). Replaced the entire contaminated list with the two genuine readings, `đãng` and the previously entirely-missing `đảng`.

Rebuilt the malformed `## Notes` (only two bare unlinked CC-lookup wikilinks, no other bullets at all) into the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 4`, `Hyōgai`, `Korean Name ㅌ` all already correct). `## Words` section was already present and correct, citing the sole stand-in [[放蕩]].

Citing word page [[放蕩]] checked and fixed one bug: an entirely missing `vietnamese` field — hvdic has a direct compound entry for 放蕩 giving `phóng đãng`; added.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 芬 (7433; 826 characters remaining).

### 2026-08-15, iteration 1679 — [[characters/芬|芬]]

**`mc_id` off-by-one bug found and fixed**: stored as `2995` (which actually belongs to a different character, 彥), but 芬 is the 2996th entry in `CC 2000.md` — corrected to `2996`. **`graphemic_classification: 分` reconfirmed correct** (形声: semantic [[Radical 140|艸]] "grass" + phonetic 分) via en.Wiktionary and zh.Wiktionary agreement; a stray content error in the existing Notes ("bamboo" for 艸, which actually means "grass" — bamboo is 竹) was fixed in the rebuild. Confirmed [[characters/分 (char)|分 (char)]]'s own `## Derived Characters` section already lists 芬 (that page's overall formatting is rougher — bare unruby'd links throughout — but out of scope for this iteration). No aliases added: zh.Wiktionary's sole candidate, 㞣, wasn't corroborated by en.Wiktionary, which explicitly states there are no variant forms.

**`vietnamese` gap filled — adding rather than removing**: the stored field held only `phân`, but hvdic's exact verbatim "Âm Hán Việt:" line gives two genuine readings, `phân, phần` (with `phân` also dual-classified under "Âm Nôm:"). Added the missing genuine `phần`.

**Two missing lookup citations found and fixed**: despite `joyo_level: 表外字` and `hsk_level: 無`, 芬 was absent from both `Hyōgai` (added as new sequential item 345) and `HSK No` (a manually-maintained list, not a dynamic Base like `Grade Advanced` — added to its `## List`). `Korean Name ㅂ`'s `### 분` subsection already correctly cited 芬.

Rebuilt the malformed `# Notes` (wrong heading level, the "bamboo" content error, a stray `### Words` subheading nested one level too deep, one entry — [[芬蘭]] — with no ruby annotation or gloss) into the standard 4-bullet format plus a properly formatted `## Words` section. Verified [[芬蘭]]'s own 注音 directly rather than assuming — its stored reading (`ㄆㄨㄋㄌㄚㄋ`, P-initial) differs from 芬's own regular reading (`ㄈㄨㄋ`, F-initial); left as-is since it's an internally consistent proper-noun transliteration on a separate, not-yet-perfected word page, not something to silently override from this character's own citation.

Citing word page [[芬芳]] checked and fixed one bug: an entirely missing `vietnamese` field — hvdic has a direct compound entry for 芬芳 giving `phân phương`; added.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 艱 (7434; 825 characters remaining).

### 2026-08-15, iteration 1680 — [[characters/艱|艱]]

**`mc_id` off-by-one bug found and fixed**: stored as `2523` (which actually belongs to a different character, 衢), but 艱 is the 2524th entry in `CC 2000.md` — corrected to `2524`. **`pos` gap filled**: was blank, set to `性詞`, matching the citing word [[艱難]]'s own `性詞`. **`graphemic_classification: 艮` reconfirmed correct** (形声: semantic 𦰩 "meat/flesh" + phonetic 艮) via en.Wiktionary and zh.Wiktionary agreement; fixed the Notes bullet's link, which needed to point to the actual vault filename `[[艮]]` rather than a `(char)`-suffixed variant; confirmed [[characters/艮|艮]]'s own `## Derived Characters` section already correctly lists 艱. `vietnamese: gian` reconfirmed correct — hvdic shows `gian` as both genuine Hán Việt and Nôm simultaneously (dual-classified). `joyo_level` confirmed genuinely blank: searched all Japanese classification lookup files and 艱 appears in none.

**`aliases` gap filled**: both sources independently agree on the exact same five variant forms — 𦫒, 囏, 𡆒, 𮎚, 𡿤 — all newly added alongside the already-present simplified 艰; confirmed none have their own vault pages.

Rebuilt the malformed `## Notes` (only two bare unlinked CC-lookup wikilinks, no other bullets at all) into the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `Old HSK 2`, and `Korean Name ㄱ`'s `### 간` subsection (all already correct). `## Words` section was already present and correct, citing the sole stand-in [[艱難]].

Citing word page [[艱難]] was already fully perfected (checked, no bugs found).

Stamped `date-last-perfect: 2026-08-15`.

**Note on this iteration's verification query**: the usual shell scan for the next never-perfected character repeatedly timed out (the per-file loop over 3350 files hung past the 3-minute bash timeout, root cause not diagnosed — possibly transient system load or a slow grep backend). Worked around it with a faster `rg --files-without-match` count (confirmed 824 remaining) plus direct spot-checks on the two lowest-`danayo_id` candidates already visible from this iteration's pre-completion listing (肇 at 7436, 耽 (char) at 7437 — both confirmed still never-perfected, with 7435 evidently belonging to an already-perfected file not in the unperfected set) to identify the true next character without a full re-scan.

Next never-perfected character by `danayo_id`: 肇 (7436; 824 characters remaining).

### 2026-08-15, iteration 1681 — [[characters/肇|肇]]

`mc_id: 3201` reconfirmed correct against `CC 3000.md` (no off-by-one). **`graphemic_classification` bug found and fixed**: stored as `聿`, but the character's own pre-existing Notes already stated the true phonetic is **肁** (itself composed of 戶+聿, sharing the identical OC \*dawʔ) — 聿 is a phonetic one level further back, not 肇's own direct component. En.Wiktionary decisively confirms 肁 as the phonetic (with semantic 攴/攵 "hand action"), matching the vault's own existing text exactly. Corrected `graphemic_classification` to `肁`, and correspondingly **removed 肁 from `aliases`**, since it was being double-counted as both a "variant form" and (correctly, per the vault's own Notes) the phonetic component — it's a pageless direct phonetic root, not an interchangeable variant graph, the same distinction drawn for other pageless roots this session (它, 妟, 臽, 曷, 巤). `aliases: 肈` (the sole genuine variant, confirmed by both sources) was kept. Note: the character's own `radical: 聿` field is unaffected by this fix — that's the separate Kangxi dictionary-indexing radical, not the etymological phonetic, and 肇 is conventionally filed there regardless of its true graphemic composition.

**`pos` gap filled**: was blank; matched to the citing word [[肇造]]'s own `動詞` (an accepted vault-wide convention, not the disqualifying non-leaf 実詞). `vietnamese: triệu` reconfirmed correct — hvdic shows `triệu` as both genuine Hán Việt and Nôm simultaneously (dual-classified).

Rebuilt the malformed `## Notes` (missing SKIP/stroke and levels bullets, a raw non-wikilinked `Radical%20066` URL fragment instead of a proper radical link) into the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `HSK No`, `Jinmeiyō`, `Korean Name ㅈ`'s `### 조` subsection all already correct). `## Words` section was already present and correct, citing the sole stand-in [[肇造]].

Citing word page [[肇造]]'s blank `vietnamese` field was investigated directly via hvdic for the compound — no attested entry found, confirming a genuine gap; left untouched, along with its missing `kwin`/`date-last-perfect` fields (out of scope — word-level perfection tracked separately from this character loop).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 耽 (char) (7437; 823 characters remaining).

### 2026-08-15, iteration 1682 — [[characters/耽 (char)|耽 (char)]]

**`mc_id` off-by-one bug found and fixed**: stored as `3011` (which actually belongs to a different character, 腴), but 耽 is the 3012th entry in `CC 3000.md` — corrected to `3012`. **`pos` gap filled**: was blank, set to `事詞` ("indulge in," transitive). **`graphemic_classification: 冘` reconfirmed correct** (形声: semantic [[Radical 128|耳]] "ear" + phonetic 冘) via en.Wiktionary and zh.Wiktionary agreement; a stray empty English gloss `("")` on the radical bullet was fixed to `("ear")`.

**`aliases` bug found and fixed**: stored as `㽎`, a completely unrelated character (independently verified: different Mandarin readings *tán*/*xīn*, different meanings entirely — "the profundity of the harem," unrelated to 耽 in any way) — a clear data error, not a plausible-but-wrong synonym or sibling this time, just a mismatched glyph. Replaced with `躭`, confirmed by both en.Wiktionary and zh.Wiktionary as the genuine variant form; excluded zh-only candidate 聃 (also independently a distinct character with its own name/earlobe senses).

**`vietnamese` contamination bug found and fixed**: the stored field held three readings (xẩm, đam, đắm), but hvdic's exact verbatim transcription gives only `đam` under the genuine "Âm Hán Việt:" line, with `đắm` and `xẩm` both appearing exclusively under "Âm Nôm:" (alongside `đam` itself, dual-classified). Reduced to the single genuine reading `đam`.

Rebuilt the malformed `## Notes` (missing SKIP/stroke and levels bullets entirely) into the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `HSK No`, `Jinmeiyō`, `Korean Name ㅌ`'s `### 탐` subsection all already correct). **Found and fixed an entirely missing `## Words` entry**: this character's `stand_in` is itself — [[耽]] is a standalone word page, previously missing from the section entirely alongside the existing [[耽耽]] entry (which itself was missing its gloss quotation marks, now fixed) — added, and reformatted the `## Chengyu` section onto its own proper heading rather than running together with Words. **Found and fixed a missing `## Derived Characters` section on [[characters/冘|冘]]** (a later, not-yet-perfected character) — didn't exist at all; created it and added 耽.

Self word page [[耽]] checked and fixed two bugs: `vietnamese: null` literal placeholder (fixed to `đam`, matching the character's own corrected reading) and a missing `pos` value entirely (filled `事詞`). Citing word page [[耽耽]] was already fully perfected; its blank `vietnamese` field was investigated directly via hvdic for the reduplicated compound — no attested entry found, confirming a genuine gap, left untouched; its `pos: 擬詞` (ideophone) was left as-is, a plausible dedicated category for onomatopoeic/mimetic words rather than a bug, consistent with the word's own Notes explicitly flagging it "(ideophonic)."

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 翅 (7438; 822 characters remaining).

### 2026-08-15, iteration 1683 — [[characters/翅|翅]]

**`mc_id` off-by-one bug found and fixed**: stored as `3601` (which actually belongs to a different character, 壙), but 翅 is the 3602nd entry in `CC 3000.md` — corrected to `3602`. **`graphemic_classification: 支` reconfirmed correct, but the existing Notes had it completely backwards**: the stored prose read "semantic 支 ('feathers') + phonetic 羽 (OC \*kje)" — both the semantic/phonetic role assignment AND the gloss were wrong (支 means "branch, support," not "feathers"; 羽, not 支, is the true semantic "feathers" component; the OC \*kje value belongs to phonetic 支, not 羽). Both en.Wiktionary and zh.Wiktionary independently confirm the correct assignment: semantic [[Radical 124|羽]] + phonetic [[支]]. Rewrote the bullet accordingly. Confirmed [[characters/支|支]]'s own `## Derived Characters` section already correctly lists 翅.

**`aliases` gap filled, conservatively**: en.Wiktionary lists 翄, 𦐊; zh.Wiktionary lists 翄, 翤, 翨, 趐, 鳷 — only 翄 is corroborated by both, so only 翄 was added (no vault page of its own); the four zh-only and one en-only candidates were excluded per the dual-source policy. `vietnamese: sí` reconfirmed correct — hvdic shows `sí` as both genuine Hán Việt and Nôm simultaneously (dual-classified).

**`japanese_native` malformed-YAML bug fixed**: a bare scalar (`つばさ`) was immediately followed by an orphaned duplicate list item under the same key — collapsed to the single correct scalar.

Rebuilt the malformed Notes into the standard 4-bullet format (fixing a broken lowercase `lookup/SKIP/...` path along the way) and confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 2`, `Hyōgai`, `Korean Name ㅅ`'s `### 시` subsection all already correct). **Found and fixed a missing `## Words` entry**: the section already listed [[翅鞘]] and [[展翅]] but was missing the character's own primary `stand_in`, [[魚翅]] — added it first.

Citing word page [[魚翅]] checked and fixed one bug: a duplicate `品詞: 名詞` field exactly redundant with `pos: 名詞` (removed); its blank `vietnamese` field investigated via hvdic — no attested entry, genuine gap, left untouched. Citing word page [[展翅]]'s blank `vietnamese` field similarly investigated via hvdic — no attested entry either, left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 繕 (7439; 821 characters remaining).

### 2026-08-15, iteration 1684 — [[characters/繕|繕]]

**`mc_id` off-by-one bug found and fixed**: stored as `2288` (which actually belongs to a different character, 軸), but 繕 is the 2289th entry in `CC 2000.md` — corrected to `2289`. **`pos` gap filled**: was blank, set to `事詞`, matching the citing word [[修繕]]'s own `事詞`. **`graphemic_classification: 善` reconfirmed correct** (形声: semantic [[Radical 120|糸]] "thread" + phonetic 善 "good") via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/善 (char)|善 (char)]]'s own `## Derived Characters` section already correctly lists 繕. No aliases added: zh.Wiktionary's sole extra candidate, 㪨, wasn't corroborated by en.Wiktionary, so left at the already-present, dual-confirmed 缮. `vietnamese: thiện` reconfirmed correct — hvdic shows `thiện` as both genuine Hán Việt and Nôm simultaneously (dual-classified).

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, no other bullets at all) into the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `HSK No`, `Jōyō - Kōtō`, `Korean Name ㅅ`'s `### 선` subsection all already correct). **Found and fixed an entirely missing `## Words` section**: added, citing the `stand_in` [[修繕]].

Citing word page [[修繕]] was already fully perfected (checked, no bugs found) — its own Notes already documents a deliberate disambiguation between this 繕 ("mend," 纟-radical) and the unrelated homophone-adjacent 善-series "thiện" senses.

Stamped `date-last-perfect: 2026-08-15`.

**Note on this iteration's verification query**: the shell scan for the next never-perfected character timed out again (same intermittent hang as the previous iteration, cause still undiagnosed). Worked around it by directly spot-checking the two lowest-`danayo_id` candidates already visible from the prior iteration's pre-completion listing (縞 at 7440, 絆 at 7441 — both confirmed still never-perfected), identifying 縞 as the true next character without a full re-scan; the remaining-count figure below is deduced (821 − 1) rather than independently re-verified.

Next never-perfected character by `danayo_id`: 縞 (7440; 820 characters remaining).

### 2026-08-15, iteration 1685 — [[characters/縞|縞]]

**`mc_id` off-by-one bug found and fixed**: stored as `2564` (which actually belongs to a different character, 叢), but 縞 is the 2565th entry in `CC 2000.md` — corrected to `2565`. **`pos` gap filled**: was blank, set to `名詞`, matching the citing word [[縦縞]]'s own `名詞`. **`graphemic_classification: 高` reconfirmed correct** (形声: semantic [[Radical 120|糸]] "silk" + phonetic 高) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/高 (char)|高 (char)]]'s own `## Derived Characters` section already correctly lists 縞. `vietnamese: cảo` reconfirmed correct — hvdic gives it as the sole genuine Hán Việt reading with no Nôm line at all, no contamination. `aliases: 缟` reconfirmed complete — both sources agree on only this one simplified variant.

Rebuilt the malformed `## Notes` (missing SKIP/stroke and levels bullets entirely) into the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `HSK No`, `Jinmeiyō`, `Korean Name ㅎ`'s `### 호` subsection all already correct). `## Words` section was already present and correct, citing the sole stand-in [[縦縞]].

Citing word page [[縦縞]]'s blank `vietnamese` field was investigated directly via hvdic for the compound (both traditional 縦縞 and its alias 縱縞) — no attested entry found, consistent with its own Notes explicitly flagging the word as primarily a Japanism with no standard Chinese/Vietnamese currency; left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 絆 (7441; 819 characters remaining).

### 2026-08-15, iteration 1686 — [[characters/絆|絆]]

`mc_id: 5068` confirmed to be a genuine trusted long-tail value (beyond the vault's tracked `CC 0000`–`CC 3000` range). **`graphemic_classification: 半` reconfirmed correct** (形声: semantic [[Radical 120|糸]] "silk" + phonetic 半) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/半|半]]'s own `## Derived Characters` section already correctly lists 絆. No aliases added: zh.Wiktionary's extra candidate, 靽, wasn't corroborated by en.Wiktionary.

**`vietnamese` bug found and fixed — a mixed case, both adding and removing**: the stored field held four readings (bạn, bấn, bận, bện), but hvdic's exact verbatim transcription gives the genuine "Âm Hán Việt:" readings as `bán, bạn` (with `bạn` also dual-classified under "Âm Nôm:") and Nôm-only readings `bấn, bện`; `bận` doesn't appear in hvdic's entry at all. Replaced the contaminated list with the two genuine readings, keeping `bạn` and adding the previously-missing `bán`.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, no other bullets at all) into the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `HSK No`, `Jinmeiyō`, `Korean Name ㅂ`'s `### 반` subsection all already correct). `## Words` section was already present and correct, citing the sole stand-in [[絆倒]].

Citing word page [[絆倒]] checked and fixed one bug — an unusual case since the word was already stamped `date-last-perfect`: a blank `pos:` field despite otherwise being fully filled out (filled `事詞`, matching 絆's own corrected pos and the compound's "to trip, cause to stumble" sense) — a reminder that a `date-last-perfect` stamp doesn't guarantee every field was checked at the time.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 筈 (char) (7442; 818 characters remaining).

### 2026-08-15, iteration 1687 — [[characters/筈 (char)|筈 (char)]]

`mc_id: 8377` confirmed to be a genuine trusted long-tail value (beyond the vault's tracked `CC 0000`–`CC 3000` range). **`pos` gap filled**: was blank, set to `名詞` ("nock," a concrete noun for the arrow's notched end). **`graphemic_classification: 舌` reconfirmed correct** (形声: semantic [[Radical 118|竹]] "bamboo" + phonetic 舌) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/舌 (char)|舌 (char)]]'s own `## Derived Characters` section already correctly lists 筈.

**`aliases` gap filled**: both sources agree on 栝, added (no vault page of its own); en.Wiktionary's other candidate, 弭, was explicitly labeled a Japanese-specific alternative kun'yomi spelling rather than a Chinese variant character, so excluded as a different category, not a true graphemic alias.

**`vietnamese` gap filled — an entirely empty field**: hvdic's exact verbatim transcription gives the genuine "Âm Hán Việt:" reading `quát`, with no "Âm Nôm:" line at all. Filled the previously-empty field with this single genuine reading.

**Found and fixed a missing `Korean Name ㄱ` citation**: the `### 괄` subsection existed but had no entry for 筈 at all — added.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, no other bullets at all) into the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `HSK No`, and `Jinmeiyō`. **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[筈]] is a standalone word page — added the section citing it.

Self word page [[筈]] checked and fixed one bug: `vietnamese: null` literal placeholder (fixed to `quát`, matching the character's own newly-filled reading).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 笠 (7443; 817 characters remaining).

### 2026-08-15, iteration 1688 — [[characters/笠|笠]]

`mc_id: 4128` confirmed to be a genuine trusted long-tail value (beyond the vault's tracked `CC 0000`–`CC 3000` range). **`pos` gap filled**: was blank, set to `名詞`, matching the citing word [[笠帽]]'s own `名詞`. **`graphemic_classification: 立` reconfirmed correct** (形声: semantic [[Radical 118|竹]] "bamboo" + phonetic 立) via en.Wiktionary and zh.Wiktionary agreement. **Found and fixed a missing `## Derived Characters` entry on [[characters/立 (char)|立 (char)]]** (already perfected earlier this session) — its list (拉, 颯, 粒, 雴, 泣) was missing 笠; added.

**`vietnamese` bug found and fixed — the most severe contamination case this session**: the stored field held **fourteen** readings (liếp, lép, lạp, lẹp, lớp, lợp, lụp, nón, nập, rạp, rập, sập, sệp, sụp, tấp), but hvdic's exact verbatim transcription gives only ONE genuine "Âm Hán Việt:" reading, `lạp` (also dual-classified under "Âm Nôm:"). Of the other thirteen, most (lép, liếp, lớp, lụp, nập, rạp, rập, sập, sệp, sụp, tấp) are legitimately Nôm-only readings of 笠, but two (lẹp, lợp, nón) don't appear anywhere in hvdic's entry at all — apparent invented/erroneous forms. Reduced to the single genuine reading `lạp`.

**`aliases` — verified a plausible-looking en.Wiktionary list is actually a different-language false positive**: en.Wiktionary's page lists 傘 ("umbrella"), 暈 ("halo"), and 仐 as "alternative forms" near the top of the entry — a follow-up, more targeted fetch confirmed these are explicitly labeled **Japanese-specific alternative spellings for the native kun'yomi word かさ (kasa)**, not variants of the Chinese character 笠 itself (the same distinct-category exclusion as [[characters/筈 (char)|筈]]'s Japanese-only 弭 last iteration). zh.Wiktionary found no clear modern variant either. Left `aliases` empty.

Rebuilt the malformed `## Notes` (missing SKIP/stroke and levels bullets entirely) into the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `HSK No`, `Jinmeiyō`, `Korean Name ㄹ`'s `### 립` subsection all already correct). `## Words` section was already present and correct, citing the sole stand-in [[笠帽]].

Citing word page [[笠帽]]'s blank `vietnamese` field was investigated directly via hvdic for the compound — no attested entry found, confirming a genuine gap; left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 窺 (char) (7444; 816 characters remaining).

### 2026-08-15, iteration 1689 — [[characters/窺 (char)|窺 (char)]]

**`mc_id` off-by-one bug found and fixed**: stored as `2132` (which actually belongs to a different character, 播), but 窺 is the 2133rd entry in `CC 2000.md` — corrected to `2133`. **`pos` gap filled**: was blank, set to `事詞` ("spy on," transitive). **`graphemic_classification: 規` reconfirmed correct** (形声: semantic [[Radical 116|穴]] "hole" + phonetic 規) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/規|規]]'s own `## Derived Characters` section already correctly lists 窺 (char).

**`aliases` gap filled**: both sources agree on the already-present simplified 窥 plus 闚 (newly added, no vault page of its own); excluded en-only candidate 𥨖. `vietnamese: khuy` reconfirmed correct — hvdic shows `khuy` as both genuine Hán Việt and Nôm simultaneously (dual-classified).

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, no other bullets at all) into the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `HSK No`, `Jinmeiyō`, `Korean Name ㄱ` all already correct). **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[窺]] is a standalone word page — added the section citing it.

Self word page [[窺]] checked and fixed two bugs: `vietnamese: null` literal placeholder (fixed to `khuy`, matching the character's own reading) and a missing `pos` value entirely (filled `事詞`).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 磐 (7445; 815 characters remaining).

### 2026-08-15, iteration 1690 — [[characters/磐|磐]]

**`mc_id` off-by-one bug found and fixed**: stored as `3310` (which actually belongs to a different character, 毐), but 磐 is the 3311th entry in `CC 3000.md` — corrected to `3311`. **`pos` gap filled**: was blank, set to `名詞`, matching the citing word [[磐石]]'s own `名詞`. **`graphemic_classification: 般` reconfirmed correct** (形声: semantic [[Radical 112|石]] "stone" + phonetic 般) via en.Wiktionary and zh.Wiktionary agreement. **`aliases` gap filled**: both sources agree on 䃑, added (no vault page of its own); excluded zh-only candidate 䃲. `vietnamese: bàn` reconfirmed correct — hvdic shows `bàn` as both genuine Hán Việt and Nôm simultaneously (dual-classified).

**Found and fixed a missing `HSK No` citation**: `hsk_level` is blank (`""`) rather than the explicit `無`, but cross-checked against an already-perfected character sharing the same blank convention ([[characters/剤|剤]]) and confirmed its own closing bullet still cites `HSK No` — meaning blank and `無` are treated identically for this citation. 磐 was missing entirely from `HSK No`'s manually-maintained list (not a dynamic Base like `Grade Advanced`) — added. **Found and fixed a missing `## Derived Characters` section on [[characters/般 (char)|般 (char)]]** (already perfected earlier this session) — the section didn't exist at all; created it and added 磐.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, no other bullets at all) into the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `Jinmeiyō`, and `Korean Name ㅂ`'s `### 반` subsection (all already correct). `## Words` section was already present and correct, citing the sole stand-in [[磐石]].

Citing word page [[磐石]] was already fully perfected (checked, no bugs found).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 盈 (7446; 814 characters remaining).

### 2026-08-15, iteration 1691 — [[characters/盈|盈]]

`mc_id: 1078` reconfirmed correct against `CC 1000.md` (no off-by-one). **`graphemic_classification: 夃` reconfirmed correct** (会意: 夃 + semantic [[Radical 108|皿]] "vessel") via en.Wiktionary and zh.Wiktionary agreement — 夃 is a pageless component, correctly cited directly rather than duplicated in `aliases`. No aliases added: the only candidate either source offered, 盁, wasn't corroborated by both in a way that survived scrutiny worth trusting alongside a pageless-root citation already covering the graphemic story; left empty.

**`vietnamese` contamination bug found and fixed — a severe case**: the stored field held five readings (diềng, doanh, dềnh, giềng, riêng), but hvdic's exact verbatim transcription gives only one genuine "Âm Hán Việt:" reading, `doanh` (also dual-classified under "Âm Nôm:"); the other four are Nôm-only. Reduced to the single genuine reading `doanh`.

**Found and fixed a missing `Hyōgai` citation**: `joyo_level: 表外字` but 盈 was absent from Hyōgai and every other Japanese classification lookup file entirely — added as new sequential item 346.

Rebuilt the malformed `## Notes` (a bare "Components:" line instead of proper 会意 phrasing, no SKIP/MC/levels bullets at all) into the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `Old HSK 4`, and `Korean Name ㅇ`'s `### 영` subsection. **Found and fixed an entirely missing `## Words` section**: added, citing the `stand_in` [[満盈]].

Citing word page [[満盈]] checked and fixed four bugs: `pos: 実詞` — the non-leaf parent category flagged in this vault's own grammar taxonomy as invalid for actual use — corrected to `性詞`; blank `korean` (filled `만영`, compositional from [[満 (char)|満]]'s own `만` + 盈's own `영`, matching the already-stored `諺文: 만영`); blank `vietnamese` (hvdic has a direct compound entry giving `mãn doanh`; added); and a nonstandard `## Etymology` heading where `## Notes` is the vault's actual convention for word pages (renamed).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 玻 (7448; 813 characters remaining).

### 2026-08-15, iteration 1692 — [[characters/玻|玻]]

`mc_id: 0` verified as a genuine "confirmed absent" sentinel: 玻 doesn't appear anywhere in `CC 0000.md`–`CC 3000.md`. **`pos` gap filled**: was blank, set to `名詞`, matching the citing word [[玻璃]]'s own `名詞`. **`graphemic_classification: 皮` reconfirmed correct** (形声: semantic [[Radical 096|玉]] "jade" + phonetic 皮) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/皮|皮]]'s own `## Derived Characters` section already correctly lists 玻. No aliases added: zh.Wiktionary's only candidate, 頗黎, is a two-character etymological/origin note (a Sanskrit-derived transliteration term), not a true single-character variant; en.Wiktionary explicitly confirms no distinct variant forms. `vietnamese: pha` reconfirmed correct — hvdic shows `pha` as both genuine Hán Việt and Nôm simultaneously (dual-classified).

**Found and fixed a missing `Korean Name ㅍ` citation**: the `### 파` subsection existed but had no entry for 玻 at all — added.

Rebuilt the malformed `# Notes` (wrong heading level, three word-links haphazardly mixed into Notes instead of a proper `## Words` section, one of them — [[玻璃版]] — missing entirely from the actual Words section that DID exist) into the standard 4-bullet format plus a consolidated, corrected `## Words` section citing all three: [[玻璃]] (`stand_in`), [[玻璃版]], and [[玻金]]. Confirmed citation on `Grade Advanced` and `Old HSK 2`.

Citing word pages checked: [[玻金]] was already fully perfected (no bugs). [[玻璃]] and [[玻璃版]] both had the nonstandard `## Etymology` heading (renamed to `## Notes`, matching vault convention, the same fix applied to [[満盈]] last iteration). [[玻璃]] was also missing `vietnamese` — hvdic has a direct compound entry giving `pha ly`; added. [[玻璃版]] was missing `cantonese`, `korean`, and `vietnamese` entirely — `vietnamese` has no attested compound entry (genuine gap, left blank), but `cantonese` and `korean` were compositionally derivable from its own constituent characters ([[璃 (char)|璃]]'s `lei4`/`리` + [[版|版]]'s `baan2`/`판`, combined with 玻's own `bo1`/`파`) and filled accordingly.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 梢 (7449; 812 characters remaining).

### 2026-08-15, iteration 1693 — [[characters/梢|梢]]

`mc_id: 5303` confirmed to be a genuine trusted long-tail value (beyond the vault's tracked `CC 0000`–`CC 3000` range). **`pos` gap filled**: was blank, set to `名詞`, matching the citing word [[末梢]]'s own `名詞`. **`graphemic_classification: 肖` reconfirmed correct** (形声: semantic [[木 (char)|木]] "tree" + phonetic 肖) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/肖|肖]]'s own `## Derived Characters` section already correctly lists 梢. **`aliases` gap filled**: both sources agree on 萷, added (no vault page of its own); excluded three zh-only candidates.

A first hvdic fetch returned content headed "梟" (a different, visually similar character) rather than 梢 — caught by re-fetching with an explicit "quote the headword shown" check before trusting the result, confirming it really was 梢's own entry on the second pass. **`vietnamese` gap filled — adding rather than removing**: the stored field held only `sao`, but hvdic's exact verbatim "Âm Hán Việt:" line (once confirmed to be the right page) gives two genuine readings, `sao, tiêu` (with `sao` also dual-classified under "Âm Nôm:"). Added the missing genuine `tiêu`.

Rebuilt the malformed `# Notes` (wrong heading level, a bare syllable-page link doing nothing useful, two bare unlinked CC-lookup wikilinks) into the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `Old HSK 4`, `Jinmeiyō`, and `Korean Name ㅊ`'s `### 초` subsection. **Found and fixed an entirely missing `## Words` section**: added, citing the `stand_in` [[末梢]].

Citing word page [[末梢]] checked and fixed two bugs: entirely missing `cantonese` and `korean` fields, both compositionally derivable from constituent characters ([[末]]'s own `mut6`/`말` + 梢's own `saau1`/`초`) and filled accordingly (`mut6 saau1`, `말초`). Its blank `vietnamese` was investigated directly via hvdic for the compound — no attested entry found, confirming a genuine gap, left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 杖 (char) (7450; 811 characters remaining).

### 2026-08-15, iteration 1694 — [[characters/杖 (char)|杖 (char)]]

`mc_id: 1365` reconfirmed correct against `CC 1000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `名詞` ("staff, stick"). **`graphemic_classification: 丈` reconfirmed correct** (形声: semantic [[木 (char)|木]] "wood" + phonetic 丈) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/丈 (char)|丈 (char)]]'s own page already cites 杖 as a derived character (in an older, pre-standard `### Derived Character` singular-heading format from an early era — left as-is, out of scope, since the citation itself is present and correct, just stylistically dated). No aliases added: en.Wiktionary's sole candidate, 𨥅, wasn't corroborated by zh.Wiktionary (whose summary conflated the phonetic-series base 丈 itself as a spurious "variant," not a real second source).

**`vietnamese` bug found and fixed — a mixed case**: the stored field held `rường, trượng`, but a headword-verified hvdic fetch (explicitly confirming the page shown really was 杖, following last iteration's mis-fetch lesson) gives the genuine "Âm Hán Việt:" readings as `tráng, trượng` (trượng also dual-classified under "Âm Nôm:"); `rường` is Nôm-only. Replaced `rường` with the previously-missing genuine `tráng`, keeping `trượng`.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, no other bullets at all) into the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 6`, `Jinmeiyō`, `Korean Name ㅈ`'s `### 장` subsection all already correct). **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[杖]] is a standalone word page — added the section citing it.

Self word page [[杖]] checked and fixed two bugs: `vietnamese: null` literal placeholder (fixed to `trượng`, the dual Hán-Việt/Nôm reading judged the best fit for the concrete "staff" object sense) and a missing `pos` value entirely (filled `名詞`).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 拼 (7451; 810 characters remaining).

### 2026-08-15, iteration 1695 — [[characters/拼|拼]]

`mc_id: 8623` confirmed to be a genuine trusted long-tail value (beyond the vault's tracked `CC 0000`–`CC 3000` range). **`graphemic_classification: 并` reconfirmed correct** (形声: semantic [[Radical 064|扌]] "hand" + phonetic 并) via en.Wiktionary and zh.Wiktionary agreement — the Notes bullet's phonetic link was a bare, completely empty `[[]]` wikilink; fixed to `[[并]]`.

**`aliases` bug found and fixed**: stored `拚, 偋` — 拚 reconfirmed correct (both sources agree, and en.Wiktionary notes 拼 is itself a modern simplified form of 拚 in some usages, a genuine variant relationship, no vault page of its own). 偋 was independently verified to be unrelated entirely — it's a variant of two different characters, 摒 and 屏, with no connection to 拼 mentioned by either source; removed.

**`vietnamese` bug found and fixed — a mixed case**: the stored field held a single malformed YAML string `"phanh, bính"` (a comma-joined scalar instead of a proper list) which also undercounted the genuine readings — a headword-verified hvdic fetch gives three genuine "Âm Hán Việt:" readings, `banh, bính, phanh` (phanh also dual-classified under "Âm Nôm:"). Split into a proper list and added the missing `banh`.

**`japanese_native` malformed-YAML bug fixed**: a bare scalar (`したが`) followed by an orphaned list item (`したがう`) under the same key — collapsed to the single correctly-hyphenated form `したが-う`.

**Two missing lookup citations found and fixed**: despite `joyo_level: 表外字` and `hsk_level: 3`, 拼 was absent from `Hyōgai` (added as new sequential item 347) and from `Korean Name ㅂ`'s `### 병` subsection (added); `Old HSK 3` was already correctly citing it.

Rebuilt the malformed `## Notes` (blank first line, a bare hyphen-less word-link doing double duty as both a Words entry and part of Notes) into the standard 4-bullet format plus a properly formatted `## Words` section citing the `stand_in` [[拼音]].

Citing word page [[拼音]] checked and fixed one bug: a duplicate `品詞: 名詞` field exactly redundant with `pos: 名詞` (removed).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 拌 (7452; 809 characters remaining).

### 2026-08-15, iteration 1696 — [[characters/拌|拌]]

`mc_id: 5946` confirmed to be a genuine trusted long-tail value (beyond the vault's tracked `CC 0000`–`CC 3000` range). **`pos` gap filled**: was blank, set to `事詞` ("mix, blend," transitive) rather than matching the citing word [[拌和]]'s own value, since that value was itself the flawed non-leaf `実詞` category (fixed separately below). **`graphemic_classification: 半` reconfirmed correct** (形声: semantic [[Radical 064|扌]] "hand" + phonetic 半) via en.Wiktionary and zh.Wiktionary agreement. **Found and fixed a missing `## Derived Characters` entry on [[characters/半|半]]** (already perfected earlier this session) — its list (絆) was missing 拌; added. No aliases added: neither source offered a genuine single-character variant (en's 抨 was explicitly noted as merely "related," not a formal variant).

**`vietnamese` bug found and fixed — a mixed case**: the stored field held `bạn, bắn`, but a headword-verified hvdic fetch gives four genuine "Âm Hán Việt:" readings, `bàn, bạn, phan, phán` (bạn also dual-classified under "Âm Nôm:"); `bắn` is Nôm-only. Replaced with the corrected four-reading set.

**Found and fixed a missing `Hyōgai` citation**: `joyo_level: 表外字` but 拌 was absent from Hyōgai — added as new sequential item 348. `Old HSK 4` and `Korean Name ㅂ`'s `### 반` subsection were already correctly citing it.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, no other bullets at all) into the standard 4-bullet format. **Found and fixed an entirely missing `## Words` section**: added, citing the `stand_in` [[拌和]] (self-caught a mid-edit typo where zhuyin ㄏ⺢ was briefly mistyped as Korean hangul ㅎㅗ before verifying against the word's own stored 注音 and correcting it).

Citing word page [[拌和]] checked and fixed three bugs: `pos: 実詞` — the non-leaf parent category — corrected to `事詞`; blank `korean` (filled `반화`, compositional from [[拌]]'s own `반` + [[和]]'s own `화`, matching the already-stored `諺文: 반화`); and blank `vietnamese` (hvdic has a direct compound entry giving `phan hoà`; added). `japanese` was left blank — genuinely underivable, since [[和]]'s own `japanese` field is itself empty.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 惚 (7453; 808 characters remaining).

### 2026-08-15, iteration 1697 — [[characters/惚|惚]]

`mc_id: 4275` confirmed to be a genuine trusted long-tail value (beyond the vault's tracked `CC 0000`–`CC 3000` range). **`pos` gap filled**: was blank, set to `性詞`, matching the citing word [[恍惚]]'s own `性詞`. **`graphemic_classification: 忽` reconfirmed correct** (形声: semantic [[Radical 061|忄]] "heart" + phonetic 忽) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/忽|忽]]'s own `## Derived Characters` section already correctly lists 惚. No aliases added: neither source lists any variant form.

**`vietnamese` gap filled — adding rather than removing**: the stored field held only `hốt`, but a headword-verified hvdic fetch gives two genuine "Âm Hán Việt:" readings, `dịch, hốt` (with `hốt` also dual-classified under "Âm Nôm:", alongside a Nôm-only `ghen` that was never stored and thus needed no removal). Added the missing genuine `dịch`.

**`#cranberry` tag reconfirmed valid**: checked [[characters/恍|恍]]'s own `stand_in` field — also `恍惚` — confirming transitivity (恍 = 惚 = 恍惚 as the shared stand-in), the condition required for the tag.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, no other bullets at all) into the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `HSK No`, `Jinmeiyō`, and `Korean Name ㅎ`'s `### 홀` subsection. `## Words` section was already present and correct, citing the sole stand-in [[恍惚]].

Citing word page [[恍惚]] checked and fixed one bug: an entirely missing `vietnamese` field — hvdic has a direct compound entry giving `hoảng hốt`; added.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 庇 (7454; 807 characters remaining).

### 2026-08-15, iteration 1698 — [[characters/庇|庇]]

`mc_id: 2981` reconfirmed correct against `CC 2000.md` (no off-by-one). `pos: 事詞` (already filled) confirmed appropriate, matching the citing word [[庇護]]'s own `事詞`. **`graphemic_classification: 比` reconfirmed correct** (形声: semantic [[Radical 053|广]] "house against a cliff" + phonetic 比) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/比 (char)|比 (char)]]'s own `## Derived Characters` section already correctly lists 庇. No aliases added: zh.Wiktionary's sole candidate, 庀, wasn't corroborated by en.Wiktionary, which states there are no listed variants at all.

**`vietnamese` gap filled — adding rather than removing**: the stored field held only `tí`, but a headword-verified hvdic fetch gives two genuine "Âm Hán Việt:" readings, `tí, tý` (with `tí` also dual-classified under "Âm Nôm:"). Added the missing genuine `tý`.

Rebuilt the malformed `# Notes` (wrong heading level, a bare word-link doing double duty instead of a proper `## Words` section, two bare unlinked CC-lookup wikilinks) into the standard 4-bullet format plus a corrected `## Words` section. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 6`, `Jinmeiyō`, `Korean Name ㅂ`'s `### 비` subsection all already correct).

Citing word page [[庇護]] checked and fixed two bugs: the nonstandard `## Etymology` heading (renamed to `## Notes`, the same recurring fix applied to [[満盈]] and [[玻璃]]/[[玻璃版]] earlier this session) and an entirely missing `vietnamese` field — hvdic has a direct compound entry giving two genuine readings, `tí hộ` and `tý hộ` (added both, matching the character's own dual reading).

Self-corrected a slip mid-edit: twice this iteration (and once last iteration too) a ruby annotation was drafted using Korean hangul syllables instead of zhuyin by mistake before being caught against the word page's own stored `注音` and fixed — noting this as a pattern to watch for, verify the stored 注音 directly rather than composing it from memory when in doubt.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 屎 (char) (7455; 806 characters remaining).

### 2026-08-15, iteration 1699 — [[characters/屎 (char)|屎 (char)]]

`mc_id: 4079` confirmed to be a genuine trusted long-tail value (beyond the vault's tracked `CC 0000`–`CC 3000` range). **`pos` gap filled**: was blank, set to `名詞`. **`graphemic_classification: 會意` reconfirmed correct, with a refined understanding**: both sources agree the character originated as an ideogrammic depiction (dots representing faeces beneath the kneeling figure [[尸]]), with zh.Wiktionary's raw source specifically noting 尸 "亦聲" (also carries the sound) — a 會意兼形聲 (compound-ideogram-that's-also-partly-phonetic) case, distinct from the vault's usual clean semantic+phonetic split; kept the existing `會意` classification since that's the primary/dominant character, but rewrote the Notes prose to capture the 亦聲 nuance rather than force it into the standard two-component bullet template.

**`aliases` gap filled — the largest batch this session**: both en.Wiktionary and zh.Wiktionary independently list overlapping sets of rare variant forms; the true dual-corroborated intersection across both lists came to eight characters — 𦳊, 宩, 𡱁, 𡲑, 𡲔, 𡲖, 𥺶, 𥻐 — all newly added (aliases field was previously empty); confirmed none have their own vault pages. Five zh-only candidates were excluded per the dual-source policy.

**`vietnamese` bug found and fixed — a mixed case**: the stored field held `thỉ, xái`, but a headword-verified hvdic fetch gives three genuine "Âm Hán Việt:" readings, `hi, hy, thỉ` (thỉ also dual-classified under "Âm Nôm:"); `xái` is Nôm-only. Replaced with the corrected three-reading set.

**A typo found and fixed on both the character page and its self-word**: `english: excresion` → `excretion` (present identically on both pages, the same "same bug on both character and self-word" pattern seen with 芬's "bamboo" error and 鹸's "akali" typo earlier).

Rebuilt the malformed `# Notes` (a stray leftover scratch fragment, "Pronunciation from K", sitting where the Notes body should be — the same "leftover artifact" pattern as the fufu/song contamination cases earlier this session — plus two bare unlinked CC-lookup wikilinks) into the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `Old HSK 4`, and `Hyōgai`. **Found and fixed a missing `Korean Name ㅎ` citation**: no `### 히` subsection existed at all between the existing `### 희` and `### 힐` — created it and added 屎 (char), the same "create a new alphabetically-slotted subsection" pattern used for 鬣 earlier this session. **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[屎]] is a standalone word page — added the section citing it.

Self word page [[屎]] checked and fixed four bugs: the same vietnamese contamination and english typo as the character page (fixed identically), a missing `pos` value (filled `名詞`), the same stray "Pronunciation from K" leftover artifact in its own Notes (removed), and a genuine **cross-field mismatch**: `korean: 시` didn't match either the character's own `korean: 히` or the word's own stored `諺文: 흐`/`羅馬字: hǝ` (both ㅎ-initial) — corrected to `히`.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 娶 (7456; 805 characters remaining).

### 2026-08-15, iteration 1700 — [[characters/娶|娶]]

`mc_id: 1471` reconfirmed correct against `CC 1000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `名詞`, matching the citing word [[嫁娶]]'s own `名詞`. **`graphemic_classification: 取` reconfirmed correct** (形声: semantic [[Radical 038|女]] "woman" + phonetic 取) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/取|取]]'s own `## Derived Characters` section already correctly lists 娶. **No aliases added — a source-conflict correctly resolved**: en.Wiktionary listed three candidates (𡣞, 𭒒, 𡞺), but a targeted re-fetch of zh.Wiktionary's own 異體字 section found it names only 取 itself as a "variant" — which is spurious, since 取 is the phonetic component already cited in `graphemic_classification`, the same "phonetic-series member mislabeled as a variant" pattern flagged repeatedly this session (parallel to [[characters/鞘|鞘]]'s 削/箾/韒). None of en's three candidates are corroborated by zh at all; left `aliases` empty. `vietnamese: thú` reconfirmed correct — hvdic shows `thú` as both genuine Hán Việt and Nôm simultaneously (dual-classified).

Rebuilt the malformed `# Notes` (missing SKIP/stroke and levels bullets entirely) into the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 3`, `Hyōgai`, `Korean Name ㅊ`'s `### 취` subsection all already correct). `## Words` section was already present but missing the "(stand-in for 娶)" annotation — added.

Citing word page [[嫁娶]] was already fully perfected (checked, no bugs found).

Stamped `date-last-perfect: 2026-08-15`. This marks iteration **1700** of the ongoing character-perfecting sweep.

Next never-perfected character by `danayo_id`: 妓 (7457; 804 characters remaining).

### 2026-08-15, iteration 1701 — [[characters/妓|妓]]

`mc_id: 6911` confirmed to be a genuine trusted long-tail value (beyond the vault's tracked `CC 0000`–`CC 3000` range). `pos: 名詞` (already filled) confirmed appropriate. **`graphemic_classification: 支` reconfirmed correct** (形声: semantic [[女 (char)|女]] "woman" + phonetic 支) via en.Wiktionary and zh.Wiktionary agreement; confirmed [[characters/支|支]]'s own `## Derived Characters` section already correctly lists 妓. No aliases added: en.Wiktionary explicitly states no distinct variants exist; zh.Wiktionary's list (伎, 𠇞, 技, 𪥩, 姼) is the broader 支-phonetic-series family, not true variants — confirmed by 伎's own independent vault page with a distinct meaning, the same false-positive pattern flagged repeatedly this session.

**`vietnamese` contamination bug found and fixed**: the stored field held three readings (kĩ, kỹ, đĩ), but a headword-verified hvdic fetch gives the genuine "Âm Hán Việt:" readings as `kĩ, kỹ` (both also dual-classified under "Âm Nôm:"); `đĩ` is Nôm-only. Reduced to the two genuine readings.

Rebuilt the malformed `## Notes` (bare unlinked CC-lookup wikilinks, a plain "Components:" line instead of proper 形声 phrasing) into the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `HSK No`, `Hyōgai`, `Korean Name ㄱ`'s `### 기` subsection all already correct). `## Words` section was already present, listing all three citing compounds ([[芸妓]], [[妓女]], [[舞妓]]) — added the missing "(stand-in for 妓)" annotation to the `stand_in` entry, [[芸妓]].

Citing word pages checked: [[妓女]] and [[舞妓]] were both already fully perfected (no bugs found — [[舞妓]]'s own Notes is a particularly thorough entry distinguishing 妓's two semantic poles). [[芸妓]]'s blank `vietnamese` field was investigated directly via hvdic — no attested entry found, confirming a genuine gap (consistent with 芸妓 being a Japanese-specific coinage for "geisha"); left untouched.

Stamped `date-last-perfect: 2026-08-15`.

**Note on this iteration's verification query**: the shell scan for the next never-perfected character timed out again (same intermittent hang seen a few iterations back). Worked around it via direct spot-checks on the two lowest-`danayo_id` candidates from the prior iteration's pre-completion listing (啡 at 7458, confirmed still never-perfected and next in sequence; 靡 at 7459 also confirmed still never-perfected) — a ripgrep-based full recount was launched in parallel but not waited on, since the direct spot-check already gives the answer needed to continue.

Next never-perfected character by `danayo_id`: 啡 (7458; 803 characters remaining).

### 2026-08-15, iteration 1702 — [[characters/啡|啡]]

`mc_id: 0` verified as a genuine "confirmed absent" sentinel: 啡 doesn't appear anywhere in `CC 0000.md`–`CC 3000.md`. `pos: 名詞` (already filled) confirmed appropriate. **`graphemic_classification: 非` reconfirmed correct for the tracked sense** (形声: semantic [[口 (char)|口]] "mouth" + phonetic 非, OC \*pʰɯːlʔ) via en.Wiktionary and zh.Wiktionary agreement; both sources also surfaced two *unrelated* homographic etymologies (淝-related "spray/shoot" in Cantonese, 觱-related "whistling sound" in Hokkien) that share the same glyph but a different origin from this character's coffee/caffeine-transliteration sense — correctly excluded from both `graphemic_classification` and `aliases`, since they're homographs of a different word, not variants of this one. `vietnamese: phê` reconfirmed correct — hvdic's fuller reading list (phi, phê, phôi, phỉ) likely spans those same unrelated senses; only `phê` (dual-classified Hán Việt/Nôm) clearly matches the tracked coffee-sense reading, so the other three were deliberately NOT added, following the established caution from [[characters/屏|屏]] earlier this session about not blindly importing readings that may belong to a different sense entirely. **Found and fixed a missing `## Derived Characters` entry on [[characters/非 (char)|非 (char)]]** (already perfected, very early era, 2026-03-17) — its existing "Descendants:" list (誹, 排 (char)) was missing 啡; added, matching that page's own established (pre-standard) subsection style rather than introducing a different heading.

**Significant discovery, not fixed this iteration**: this character's own `stand_in` field names **珈啡因** ("caffeine") — but no word page for 珈啡因 exists anywhere in the vault (checked directly and via alias search, e.g. 咖啡因; genuinely absent). A character's `stand_in` is supposed to be a real, existing word page that legitimizes the bounded character; here it points to nothing. Word *creation* is a distinct task from word/character *perfecting* (per the vault's own skill-index split) and requires more careful sourcing (attested readings across all five languages) than fits this iteration's scope — flagging this here rather than fabricating a stub page. In the interim, rebuilt the `## Words` section to cite the one caffeine-adjacent word that DOES exist and is already fully perfected, [[珈啡]] ("coffee"), rather than leaving broken/unlinked references to 珈啡因 and 馬啡因 (the latter, "morphine," similarly has no word page).

Rebuilt the malformed `# Notes` (a stray blank line, un-ruby'd word mentions doing double duty as a pseudo-Words list) into the standard 4-bullet format (self-caught a first-pass omission of the SKIP/stroke bullet before finalizing — now genuinely 4 bullets) plus a corrected `## Words` section. **Found and fixed two missing lookup citations**: despite `joyo_level: 表外字`, 啡 was absent from `Hyōgai` (added as new sequential item 349); despite `korean: 비`, it was also absent from `Korean Name ㅂ`'s `### 비` subsection (added). `Grade Advanced` and `Old HSK 1` were already correctly citing it.

Citing word page [[珈啡]] was already fully perfected (checked, no bugs found).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 靡 (7459; 802 characters remaining).

### 2026-08-15, iteration 1703 — [[characters/靡|靡]]

`mc_id: 965` reconfirmed correct against `CC 0000.md` (no off-by-one; the file's blockquote formatting around that line briefly obscured a direct grep match, but the rank itself checks out). **`pos` gap filled**: was blank, set to `性詞`, matching the citing word [[淫靡]]'s own `性詞`.

**`graphemic_classification` bug found and fixed**: stored as `非`, but both en.Wiktionary and zh.Wiktionary agree 非 is actually the *semantic* component ("to scatter") and 麻 is the true phonetic — the stored value had the semantic/phonetic roles swapped, the same category of error as [[characters/翅|翅]]'s backwards Notes prose earlier this session, except here the mistake was in the structured `graphemic_classification` field itself, not just the prose. Corrected to `麻`; confirmed [[characters/麻|麻]]'s own `### Derived Characters` section already correctly lists 靡. No aliases added: zh.Wiktionary's sole candidate, 劘, wasn't corroborated by en.Wiktionary.

**`vietnamese` gap filled with cross-referencing from the citing word**: the stored field held `mi, mị`, both confirmed genuine (hvdic lists six Hán Việt readings total for 靡 — ma, mi, my, mĩ, mị, mỹ — spanning the character's several distinct senses, so not all six necessarily apply to this vault's tracked "extravagant" sense). Checking the citing word [[淫靡]] directly resolved the ambiguity: hvdic's compound entry gives `dâm mĩ`, directly attesting `mĩ` (tilde diacritic, distinct from the already-stored `mị`, dot-below) as the reading matching *this exact sense*. Added the missing `mĩ`.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, a bare word-link doing double duty as the Words section) into the standard 4-bullet format plus a corrected `## Words` section. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `HSK No`, `Hyōgai`, `Korean Name ㅁ`'s `### 미` subsection all already correct).

Citing word page [[淫靡]] checked and fixed one bug: an entirely missing `vietnamese` field — hvdic has a direct compound entry giving `dâm mĩ` (the same fetch that resolved the character-level reading ambiguity above); added.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 彗 (7461; 801 characters remaining).

### 2026-08-15, iteration 1704 — [[characters/彗|彗]]

**`mc_id` off-by-one bug found and fixed**: stored as `1937` (which actually belongs to a different character, 浴), but 彗 is the 1938th entry in `CC 1000.md` — corrected to `1938`. `pos: 名詞` (already filled) confirmed appropriate, matching the citing word [[彗星]]'s own `名詞`. **`graphemic_classification: 會意` reconfirmed correct** (甡 "broom" + [[又 (char)|又]] "hand") via en.Wiktionary and zh.Wiktionary agreement. **`aliases` gap filled**: both sources agree on 篲, added (no vault page of its own); excluded three single-source-only candidates (𥱵, 𥶙 en-only; 蔧 zh-only).

**`vietnamese` bug found and fixed, with the source of the error identified**: the stored field held `chổi, tuệ`; hvdic's exact verbatim transcription gives only `tuệ` under both "Âm Hán Việt:" and "Âm Nôm:" (dual-classified) — `chổi` doesn't appear as a reading of 彗 anywhere. Tracing it further: hvdic's own entry for the citing word [[彗星]] glosses the compound as "sao chổi" ("broom star" = comet, the natural Vietnamese term) — `chổi` is native Vietnamese for "broom," lifted from that gloss and mistaken for a Sino-Vietnamese reading of 彗 itself, the same "definition text mistaken for a pronunciation" pattern as [[characters/笠|笠]]'s "roi" error earlier this session. Reduced to the single genuine reading `tuệ`.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, no other bullets at all) into the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `HSK No`, `Jinmeiyō`, `Korean Name ㅎ`'s `### 혜` subsection all already correct). **Found and fixed an entirely missing `## Words` section**: added, citing the `stand_in` [[彗星]].

Citing word page [[彗星]] checked and fixed one bug: an entirely missing `vietnamese` field — hvdic has a direct compound entry giving `tuệ tinh` (the same fetch that explained the "chổi" error above); added.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 聚 (7462; 800 characters remaining).

### 2026-08-15, iteration 1705 — [[characters/聚|聚]]

`mc_id: 747` reconfirmed correct against `CC 0000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `事詞`, matching the citing word [[聚集]]'s own `事詞`. **`graphemic_classification: 取` reconfirmed correct — but the existing Notes prose had it backwards**: the frontmatter field itself was already right (取 genuinely is the phonetic, OC \*sʰloːʔ), but the Notes text swapped the semantic/phonetic labels AND their glosses, calling 取 "semantic...three men" (取 actually means "to take"; "three men" is 乑's meaning) and 乑 phonetic. En.Wiktionary's detailed OC reconstruction confirms the correct assignment (semantic 乑 "three men" + phonetic 取); zh.Wiktionary's summary had conflated the Kangxi *dictionary-indexing* radical (耳, used only for lookup purposes) with the true etymological semantic component — the same radical-vs-graphemic-classification distinction established earlier this session (e.g. 舵). Rewrote the Notes bullet with the correct assignment; confirmed [[characters/取|取]]'s own `## Derived Characters` section already correctly lists 聚.

**`aliases` bug found and fixed**: the stored candidate, 𧰨, was independently verified to be a completely unrelated character (different pronunciation "gèng," different radical 豕 "pig," no documented connection to 聚 anywhere) — removed. No replacement added: en.Wiktionary and zh.Wiktionary's variant lists for 聚 itself had zero overlap with each other, so nothing passed the dual-source bar.

**`vietnamese` bug found and fixed — the most severe contamination this session besides 笠's**: the stored field held five readings (sụ, tọ, tụ, xụ, xủ), but a headword-verified hvdic fetch gives only one genuine "Âm Hán Việt:" reading, `tụ` (also dual-classified under "Âm Nôm:"); `sụ, tọ, xụ` are Nôm-only, and `xủ` doesn't appear in hvdic's entry at all. Reduced to the single genuine reading `tụ`.

Rebuilt the malformed `## Notes` (bad prose noted above, a stray blank line, an unlabeled `## Words` entry reading "not 集落" with no gloss) into the standard 4-bullet format plus a corrected `## Words` section citing both [[聚集]] (`stand_in`) and [[聚落]] with proper glosses. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 3`, `Hyōgai`, `Korean Name ㅊ`'s `### 취` subsection all already correct).

Citing word pages checked: [[聚落]] was already fully perfected (its blank `vietnamese` field independently confirmed via hvdic as a genuine gap, no compound entry exists). [[聚集]] had three bugs fixed: a duplicate `品詞: 事詞` field exactly redundant with `pos: 事詞` (removed); a blank `korean: ""` (filled `취집`, compositional from 聚's own `취` + [[集]]'s own `집`, matching the already-stored `諺文: 취집`).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 俘 (7463; 799 characters remaining).

### 2026-08-15, iteration 1706 — [[characters/俘|俘]]

`mc_id: 3111` reconfirmed correct against `CC 3000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `名詞`. **`graphemic_classification: 孚` reconfirmed correct** (形声: semantic [[人 (char)|人]] "person" + phonetic 孚) via en.Wiktionary and zh.Wiktionary agreement. No aliases added: neither source offers a clean single-character variant of 俘 itself (zh's 𤓽 is a variant of the phonetic root 孚, not of 俘).

**A reverse-direction alias bug found on the phonetic parent, [[characters/孚|孚]]** (not yet perfected): its own `aliases` field wrongly included **俘 itself** — but 俘 is an independently-meaningful, page-having derived character (exactly the "alias = parent form" pattern this memory system already tracks, applied here in the opposite direction: a true derivative mistakenly demoted to "variant" status on its root's own page). Removed 俘 from 孚's aliases and added a new `## Derived Characters` section citing it instead (the section didn't exist at all yet).

**`vietnamese` bug found and fixed — a tone-mark substitution, not a simple contamination**: the stored field held `phù` (grave accent), but a headword-verified hvdic fetch gives the genuine "Âm Hán Việt:" reading as `phu` (no accent) — `phù` is actually the character's separate **Âm Nôm** reading, not Hán Việt at all. Replaced `phù` with the correct `phu`.

**`#cranberry` tag reconfirmed valid**: checked [[characters/虜|虜]]'s own `stand_in` field — also `俘虜` — confirming transitivity.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, no other bullets at all) into the standard 4-bullet format. Confirmed citation on `Grade Advanced` and `Old HSK 4`. **Found and fixed a missing `Korean Name ㅂ` citation**: the `### 부` subsection existed but had no entry for 俘 at all — added. `joyo_level` and `hanmun_edu_level` both confirmed genuinely blank per established convention, no Japanese-classification citation needed. **Found and fixed an entirely missing `## Words` section**: added, citing the `stand_in` [[俘虜]].

Citing word page [[俘虜]] checked and fixed one bug: the same tone-mark substitution as the character itself — `vietnamese: phù lỗ` corrected to `phu lỗ` (hvdic's own compound entry directly confirms `phu lỗ` as genuine), with its explanatory Notes prose updated to match.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 錦 (7464; 798 characters remaining).

### 2026-08-15, iteration 1707 — [[characters/錦|錦]]

`mc_id: 2024` reconfirmed correct against `CC 2000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `名詞`. **`graphemic_classification: 金` reconfirmed correct** (形声: semantic 帛 "silk" + phonetic [[金 (char)|金]], OC \*krɯm) via en.Wiktionary's precise OC reconstruction, which zh.Wiktionary's own summary garbled (claiming phonetic 禁, an unsupported claim not corroborated anywhere else) — trusted en's detailed etymology over zh's confused extraction. `aliases: 锦` reconfirmed complete — both sources agree on only this simplified variant. **`#cranberry` tag reconfirmed valid**: checked [[characters/繍|繍]]'s own `stand_in` field — also `錦繍` — confirming transitivity.

**`vietnamese` contamination bug found and fixed**: the stored field held four readings (cẩm, gấm, gắm, ngẫm), but hvdic's exact verbatim transcription gives only `cẩm` under the genuine "Âm Hán Việt:" line (also dual-classified under "Âm Nôm:"); `gấm, gắm, ngẫm` are all Nôm-only. Reduced to the single genuine reading `cẩm`.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, a bare unlabeled word-link instead of a proper `## Words` entry) into the standard 4-bullet format plus a corrected `## Words` section (self-caught a mid-edit hangul/zhuyin ruby slip again, verified against the word's own stored 注音 before finalizing). Confirmed citation on `Grade Advanced`, `Old HSK 4`, and `Jōyō - Kōtō`. **Found and fixed a missing `Korean Name ㄱ` citation**: the `### 금` subsection existed but had no entry for 錦 — added. **Found and fixed a missing `## Derived Characters` section on [[characters/金 (char)|金 (char)]]** (already perfected, very early era, 2026-03-12) — didn't exist at all despite 金 clearly having a large derived family; created it and added 錦 as the one directly relevant here (not attempting a full family audit of this heavily-used root, out of scope).

Citing word page [[錦繍]] checked and fixed two bugs: the nonstandard `## Etymology` heading (renamed to `## Notes`, the recurring fix seen several times this session) and its blank `vietnamese` field investigated directly via hvdic — no attested entry found (checked both the stored form 錦繍 and its alias 錦繡), confirming a genuine gap; left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 髯 (7465; 797 characters remaining).

### 2026-08-15, iteration 1708 — [[characters/髯|髯]]

`mc_id: 3427` reconfirmed correct against `CC 3000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `名詞`, matching the citing word [[鬚髯]]'s own `名詞`. **Self-caught a URL-encoding slip mid-verification**: the first round of en.Wiktionary/zh.Wiktionary/hvdic fetches for 髯 all silently returned content for a different character (鬚) due to a wrong percent-encoding in the URL — caught by noticing en.Wiktionary's own response explicitly said "the page shown is for 鬚, not 髯," re-derived the correct encoding, and re-fetched all three before trusting any of the data (the same discipline as last iteration's headword-mismatch catch on 梢/梟).

**`graphemic_classification: 冉` reconfirmed correct** (形声: semantic [[Radical 190|髟]] "long hair" + phonetic 冉) via the corrected en.Wiktionary and zh.Wiktionary fetches; confirmed [[characters/冉|冉]]'s own `### Derived Characters` section already correctly lists 髯. `aliases: 髥` reconfirmed complete — both sources agree on only this one variant; en.Wiktionary's long tail of ancient/obscure forms wasn't corroborated by zh.

**`vietnamese` bug found and fixed — a mixed case**: the stored field held three readings (nhem, nhiêm, nhẹm), but hvdic's exact verbatim transcription (correctly headword-verified this time) gives the genuine "Âm Hán Việt:" reading as `nhiêm` alone (also dual-classified under "Âm Nôm:"); `nhem` is Nôm-only, and `nhẹm` doesn't appear in hvdic's entry at all. Reduced to the single genuine reading `nhiêm`.

Rebuilt the malformed `## Notes` (a stray unlinked bare-text radical reference instead of a proper wikilink, two bare unlinked CC-lookup wikilinks) into the standard 4-bullet format. **Found and fixed two missing lookup citations**: despite `joyo_level: 表外字`, 髯 was absent from `Hyōgai` (added as new sequential item 350); despite blank `hsk_level` (which, per the established `HSK No`-still-applies precedent from [[characters/剤|剤]]/[[characters/磐|磐]], still requires the citation), it was also absent from `HSK No`'s manually-maintained list (added). `Korean Name ㅇ`'s `### 염` subsection was already correctly citing it (via the alias glyph 髥, pointing to the right file). `## Words` section was already present, missing only the "(stand-in for 髯)" annotation — added.

Citing word page [[鬚髯]] was already fully perfected; its blank `vietnamese` field had already been investigated and confirmed a genuine gap in an earlier iteration this session ([[characters/鬚|鬚]]'s own turn) — no re-check needed.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 禿 (char) (7466; 796 characters remaining).

### 2026-08-15, iteration 1709 — [[characters/禿 (char)|禿 (char)]]

`mc_id: 3839` reconfirmed correct against `CC 3000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `性詞` ("bald," a stative). **`graphemic_classification: 會意` reconfirmed correct** (毛 "hair," later corrupted into 禾, + [[儿]] "person") via en.Wiktionary and zh.Wiktionary agreement — verified the correct URL encoding for 禿 before fetching, per last iteration's headword-mismatch lesson.

**`aliases` gap filled**: both sources agree on the already-present simplified 秃 plus three additional variants — 秂, 𣬜, 痜 — all newly added (no vault pages of their own).

**`vietnamese` contamination bug found and fixed — another severe case**: the stored field held five readings (ngốc, sốc, thóc, thốc, trọc), but hvdic's exact verbatim transcription gives only two genuine "Âm Hán Việt:" readings, `ngốc, thốc` (thốc also dual-classified under "Âm Nôm:"); `sốc, thóc, trọc` are all Nôm-only. Reduced to the two genuine readings.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, an unglossed bare word-link) into the standard 4-bullet format plus a corrected `## Words` section (adding the missing self-word entry [[禿]] alongside the existing [[禿就]]). Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 4`, `Hyōgai`, `Korean Name ㄷ`'s `### 독` subsection all already correct).

Self word page [[禿]] checked and fixed two bugs: `vietnamese: null` literal placeholder (fixed to `thốc`, matching the character's own corrected dual-classified reading) and a missing `pos` value entirely (filled `性詞`).

Citing word page [[禿就]] checked and fixed one bug: the nonstandard `## Etymology` heading (renamed to `## Notes`); its blank `vietnamese` field investigated directly via hvdic (checked both the stored form 禿就 and its alias 禿鷲) — no attested entry found, confirming a genuine gap, left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 泛 (7467; 795 characters remaining).

### 2026-08-15, iteration 1710 — [[characters/泛|泛]]

`mc_id: 3324` reconfirmed correct against `CC 3000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `動詞`. **`graphemic_classification: 乏` reconfirmed correct** (形声: semantic [[Radical 085|水]] "water" + phonetic 乏) via en.Wiktionary and zh.Wiktionary agreement (headword-verified before fetching). **Found and fixed a missing `## Derived Characters` section on [[characters/乏|乏]]** (already perfected) — didn't exist at all; created it and added 泛.

**`aliases` gap filled, with two false positives correctly excluded**: both sources agree on three candidates — 汎, 氾, 滼 — but 汎 and 氾 both turned out to be independent vault characters with their own distinct current meanings and pages ("pan-" and "overflow" respectively, each with its own frontmatter), the same established exclusion pattern applied repeatedly this session. Added only 滼 (no vault page of its own).

**`vietnamese` bug found and fixed — a mixed case**: the stored field held `mẹp, phiếm, phím`, but a headword-verified hvdic fetch gives the genuine "Âm Hán Việt:" readings as `phiếm, phủng` (phiếm also dual-classified under "Âm Nôm:"); `mẹp, phím` are Nôm-only. Replaced with the corrected two-reading set.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, an unlabeled word-link) into the standard 4-bullet format plus a corrected `## Words` section. Confirmed citation on `Grade Advanced`, `Old HSK 2`, and `Korean Name ㅂ`'s `### 범` subsection; `joyo_level` confirmed genuinely blank (no Japanese-classification citation needed).

Citing word page [[泛濫]] checked and fixed one bug: an entirely missing `vietnamese` field — hvdic has a direct compound entry giving `phiếm lạm` (noting the entry cross-references 氾濫 as an equivalent form); added.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 欽 (7468; 794 characters remaining).

### 2026-08-15, iteration 1711 — [[characters/欽|欽]]

`mc_id: 1785` reconfirmed correct against `CC 1000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `事詞`, matching the citing word [[欽敬]]'s own `事詞`. **`graphemic_classification: 金` reconfirmed correct** (semantic [[欠 (char)|欠]] "to beg, kneeling person" + phonetic [[金 (char)|金]]) via en.Wiktionary and zh.Wiktionary agreement (headword-verified before fetching). `aliases: 钦` reconfirmed complete — the only single-source extras (𣣽, noted by en itself as possibly not existing; 撳, zh-only) didn't clear the dual-source bar. **Found and fixed a missing `## Derived Characters` entry on [[characters/金 (char)|金 (char)]]** (already perfected) — its list, only just created last iteration with 錦, was missing 欽; added.

**`vietnamese` bug found and fixed — a mixed case**: the stored field held three readings (khom, khoăm, khâm), but a headword-verified hvdic fetch gives the genuine "Âm Hán Việt:" readings as `khâm, khấm` (khâm also dual-classified under "Âm Nôm:"); `khom` is Nôm-only, and `khoăm` doesn't appear in hvdic's entry at all. Replaced with the corrected two-reading set.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, a `## Words` section placed before Notes) into the standard 4-bullet format plus a consolidated `## Words` section (adding the missing "(stand-in for 欽)" annotation to [[欽敬]], alongside the already-present [[欽婁]]). Confirmed citation on `Grade Advanced`, `Old HSK 4`, `Jinmeiyō`, and `Korean Name ㅎ`'s `### 흠` subsection.

Citing word pages checked: [[欽婁]] was already fully perfected (a deliberate Dan'a'yo phonetic-coinage placename for Wales/Cymru, its own mechanical CJKV readings explicitly caveated in its own Notes — no bugs). [[欽敬]] had four bugs fixed: the nonstandard `## Etymology` heading (renamed to `## Notes`); blank `korean` (filled `흠경`, compositional from 欽's own real Sino-Korean `흠` + [[敬]]'s own `경` — careful here to use the characters' actual `korean` fields, not their `諺文` Danayo-syllable fields, which use a different derivation system entirely and would have given the wrong compound); and blank `vietnamese` (hvdic has a direct compound entry giving `khâm kính`; added). `japanese` was left blank — genuinely underivable, since [[敬]]'s own `japanese` field is itself empty.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 霫 (7469; 793 characters remaining).

### 2026-08-15, iteration 1712 — [[characters/霫|霫]]

`mc_id: 0` verified as a genuine "confirmed absent" sentinel: 霫 doesn't appear anywhere in `CC 0000.md`–`CC 3000.md`. `pos: 名詞` (already filled) confirmed appropriate. **`graphemic_classification: 習` reconfirmed correct** (形声: semantic [[Radical 173|雨]] "rain" + phonetic 習) via en.Wiktionary and zh.Wiktionary agreement (headword-verified before fetching); confirmed [[characters/習|習]]'s own `## Derived Characters` section already correctly lists 霫. No aliases added: en's sole candidate (𮊙) and zh's sole candidate (雭) don't overlap, so neither clears the dual-source bar. `vietnamese: tập` reconfirmed correct — hvdic gives it as the sole genuine Hán Việt reading with no Nôm line at all, no contamination.

**`#cranberry` tag inconsistency found and fixed on the phonetic sibling, [[characters/雴|雴]]** (already perfected): its own `stand_in` is also `雴霫`, confirming transitivity — but its `tags` list was missing the `#cranberry` tag that 霫 itself carries for the exact same shared-stand-in relationship. Added the tag to 雴 for consistency.

Rebuilt the malformed `## Notes` (missing SKIP/stroke and levels bullets entirely) into the standard 4-bullet format. **Found and fixed two missing lookup citations**: despite `joyo_level: 表外字`, 霫 was absent from `Hyōgai` (added as new sequential item 351); despite `hsk_level: 無` (which, per the established `HSK No`-still-applies precedent, still requires the citation), it was also absent from `HSK No`'s manually-maintained list (added). `Korean Name ㅅ`'s `### 습` subsection existed but had no entry for 霫 either — added. `## Words` section was already present, missing only the "(stand-in for 霫)" annotation — added.

Citing word page [[雴霫]] was already fully perfected; its blank `vietnamese` field was investigated directly via hvdic — no attested entry found, consistent with its own Notes explicitly flagging both characters as too obscure for CJKV dictionary coverage; left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 凜 (char) (7470; 792 characters remaining).

### 2026-08-15, iteration 1713 — [[characters/凜 (char)|凜 (char)]]

`mc_id: 6213` confirmed to be a genuine trusted long-tail value (beyond the vault's tracked `CC 0000`–`CC 3000` range). `pos: 性詞` (already filled) confirmed appropriate. **`graphemic_classification: 稟` reconfirmed correct** (形声: semantic [[Radical 015|冫]] "ice" + phonetic 稟) via en.Wiktionary and zh.Wiktionary agreement (headword-verified before fetching); confirmed [[characters/稟|稟]]'s own `## Derived Characters` section already correctly lists 凜. `vietnamese: lẫm` reconfirmed correct — hvdic shows it as both genuine Hán Việt and Nôm simultaneously (dual-classified).

**`aliases` bug found and fixed**: the stored field held `凛, 澟` — 凛 reconfirmed correct (both sources agree), but 澟 was NOT corroborated by en.Wiktionary at all despite being already stored (a targeted re-fetch explicitly confirmed en.Wiktionary makes no mention of 澟 whatsoever); only zh.Wiktionary lists it. Removed per the dual-source policy; zh's other candidate, 癛, was never added in the first place and stays excluded for the same reason.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, no other bullets at all) into the standard 4-bullet format. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `HSK No`, `Jinmeiyō`, `Korean Name ㄹ`'s `### 름` subsection all already correct). **Found and fixed an entirely missing `## Words` section**: this character's `stand_in` is itself — [[凜]] is a standalone word page — added the section citing it.

Self word page [[凜]] was already fully perfected (checked, no bugs found — its own Notes is a particularly thorough entry tracing the "cold → stern dignity" semantic shift across all four languages, including a Vietnamese fixed-idiom survival case).

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 闖 (7471; 791 characters remaining).

### 2026-08-15, iteration 1714 — [[characters/闖|闖]]

`mc_id: 8481` confirmed to be a genuine trusted long-tail value (beyond the vault's tracked `CC 0000`–`CC 3000` range). `pos: 事詞` (already filled) confirmed appropriate. **`graphemic_classification: 會意` reconfirmed correct** (a horse, [[馬 (char)|馬]], rushing through a gate, [[門]]) via en.Wiktionary and zh.Wiktionary agreement (headword-verified before fetching). `aliases: 闯` reconfirmed complete — en.Wiktionary's two extra candidates (𨳐, 𰿧) weren't corroborated by zh.

**`vietnamese` contamination bug found and fixed**: the stored field held `sấm, sấn`, but hvdic's exact verbatim transcription gives only `sấm` under the genuine "Âm Hán Việt:" line; `sấn` appears exclusively under "Âm Nôm:" (alongside `sấm` itself, dual-classified). Reduced to the single genuine reading `sấm`.

**Found and fixed two missing `## Derived Characters` entries — on both semantic components at once, since this is a `會意` (ideogrammic compound) character with two equally-contributing parts**: [[characters/門|門]]'s list (聞, 問, 悶) and [[characters/馬 (char)|馬 (char)]]'s list (碼, 媽, 罵) were both missing 闖; added to both, consistent with the established rule that semantic-only (`會意`) derivations belong in `Derived Characters` just as much as phonetic ones.

Rebuilt the malformed `# Notes` (wrong heading level, two bare unlinked CC-lookup wikilinks, no other bullets at all) into the standard 4-bullet format. Confirmed citation on `Grade Advanced`, `Old HSK 2`, and `Korean Name ㅌ`'s `### 틈` subsection. **Found and fixed a missing `Hyōgai` citation**: despite `joyo_level: 表外字`, 闖 was absent — added as new sequential item 352. `## Words` section was already present, missing only the "(stand-in for 闖)" annotation — added.

Citing word page [[闖入]]'s blank `vietnamese` field was investigated directly via hvdic — no attested entry found, confirming a genuine gap; left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 浣 (7474; 790 characters remaining).

### 2026-08-15, iteration 1715 — [[characters/浣|浣]]

`mc_id: 3634` reconfirmed correct against `CC 3000.md` (no off-by-one). **`pos` gap filled**: was blank, set to `動詞`, matching the citing word [[浣衣]]'s own `動詞`. **`graphemic_classification: 完` reconfirmed correct** (形声: semantic [[Radical 085|水]] "water" + phonetic 完) via en.Wiktionary and zh.Wiktionary agreement (headword-verified before fetching); confirmed [[完]]'s own `## Derived Characters` section — missing 浣 entirely — added. `aliases: 澣` reconfirmed complete — both sources agree on only this one variant.

**`vietnamese` gap filled — adding rather than removing**: the stored field held only `hoán`, but hvdic's exact verbatim "Âm Hán Việt:" line gives two genuine readings, `cán, hoán` (hoán also dual-classified under "Âm Nôm:"). Added the missing genuine `cán`.

**Found and fixed a missing `HSK No` citation**: `hsk_level` is blank rather than the explicit `無`, but per the established precedent (blank still requires the citation), 浣 was absent from `HSK No`'s manually-maintained list — added. `joyo_level` also blank, confirmed genuinely so (no Japanese lookup file mentions 浣). `Korean Name ㅎ`'s `### 한` subsection already cited it (via the alias glyph 澣).

Rebuilt the malformed `## Notes` (missing SKIP/stroke and levels bullets entirely) into the standard 4-bullet format. `## Words` section was already present, missing only the "(stand-in for 浣)" annotation — added.

Citing word page [[浣衣]] checked and fixed one bug: a duplicate `品詞: 動詞` field exactly redundant with `pos: 動詞` (removed); its blank `vietnamese` field investigated directly via hvdic — no attested entry found, confirming a genuine gap, left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 晋 (7475; 789 characters remaining).

### 2026-08-15, iteration 1716 — [[characters/晋|晋]]

`mc_id: 178` reconfirmed correct against `CC 0000.md` (indexed under the traditional form 晉, matching the vault's own stored alias, no off-by-one). **`pos` gap filled**: was blank, set to `動詞`, matching the citing word [[晋升]]'s own `動詞`. **`graphemic_classification: 會意` reconfirmed correct** (臸 "to arrive" + [[日 (char)|日]] "sun") via en.Wiktionary and zh.Wiktionary agreement — verified no separate vault page exists for the traditional form 晉 before trusting the existing alias. **Found and fixed a missing `## Derived Characters` entry on [[characters/日 (char)|日 (char)]]** (already perfected) — its list (only 涅, unusually sparse for such a common root) was missing 晋; added.

**`aliases` gap filled — the largest batch this session, matching 屎's earlier 8-item find**: both en.Wiktionary and zh.Wiktionary independently list an identical set of nine ancient/rare variant forms (㬜, 𣈆, 𫞄, 𣋤, 𣌇, 𣋧, 㬐, 𡥨, 𦗎) alongside the already-present traditional form 晉 — full agreement on all nine, all newly added; confirmed none have their own vault pages.

**`vietnamese` contamination bug found and fixed**: the stored field held three readings (tấn, tắn, tớn), but hvdic's exact verbatim transcription gives only `tấn` under the genuine "Âm Hán Việt:" line (also dual-classified under "Âm Nôm:"); `tắn, tớn` are both Nôm-only. Reduced to the single genuine reading `tấn`.

Rebuilt the malformed `## Notes` (which was oddly placed as `# Notes` — H1 — after the `## Words` section entirely, reversing the normal order) into the standard 4-bullet format plus a corrected, properly-ordered `## Words` section. Confirmed citation on all four closing-bullet lookup pages (`Grade Advanced`, `Old HSK 4`, `Jinmeiyō`, `Korean Name ㅈ`'s `### 진` subsection all already correct, citing via the alias glyph 晉).

Citing word page [[晋升]] was already fully perfected; both its blank `japanese` (genuinely underivable, since [[升 (char)|升]]'s own `japanese` field is itself empty) and blank `vietnamese` (no attested compound entry via hvdic) fields confirmed as genuine gaps, left untouched.

Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 唳 (char) (7476; 788 characters remaining).

### 2026-08-15, iteration 1717 — [[characters/唳 (char)|唳]]

A largely unperfected page: only two Notes bullets existed (a bare "[口] + [戻]" fragment and floating, unlinked CC-lookup wikilinks at the bottom), no `## Words` or `## Chengyu` sections despite both existing, and three blank level fields (`joyo_level`, `hsk_level`, `hanmun_edu_level`) that had never actually been checked.

**`graphemic_classification: 戻` reconfirmed correct** — en.Wiktionary and zh.Wiktionary agree 唳 is 形聲 with semantic [[Radical 030|口]] ("mouth") + phonetic 戾/戻, and pulled the Zhengzhang Old Chinese reconstruction (*rɯːds*) for the graphemic bullet.

**`aliases` false-positive removed**: 悷 was listed as an alias, but both sources confirm it's merely a fellow member of the 戾 phonetic series with its own distinct meaning ("sorrowful"), not a variant of 唳 itself — matches the established "phonetic-series member mistaken for variant" false-positive category (cf. 取/娶, 支/妓). Removed, leaving aliases empty; no genuine variant surfaced to replace it.

**`vietnamese: lệ` reconfirmed correct** via hvdic — dual-classified as both Âm Hán Việt and Âm Nôm with the identical reading, no contamination.

**Three level fields filled from genuine "never checked" blanks**: `joyo_level` → `表外字` (en.Wiktionary explicitly classifies 唳 as hyōgai kanji; added as entry #353 to [[Lookup/Japanese/Hyōgai]]); `hsk_level` → `無` (obscure literary character, no HSK attestation; added to the manual [[Lookup/HSK/HSK No]] list); `hanmun_edu_level` → `無` (no evidence of inclusion in the Korean 1800-hanja education set; [[Lookup/Korean/Korean Missing]] is a pure dataview query keyed on the frontmatter field, so no manual list edit was needed there).

Rebuilt the four-bullet Notes in standard order, added the missing `## Words` (citing the self-named stand-in word [[唳]]) and `## Chengyu` (citing [[風声鶴唳]], ruby-annotated from its own stored 注音) sections. Confirmed no other vault character cites 唳 as a phonetic/semantic component, so no `## Derived Characters` section applies. Fixed a `../` path bug in the disambiguation callout's link to the word page. Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 缺 (7477; 787 characters remaining).

### 2026-08-15, iteration 1718 — [[characters/缺|缺]]

**`graphemic_classification` bug found and fixed in the field itself**: stored as `叏`, but the Notes bullet's own body text linked `[[夬]]` — a genuine field/prose mismatch. Dual-source check (en.Wiktionary + zh.Wiktionary) resolved it: 叏 is explicitly recorded as a variant form of 夬 with no independent meaning of its own ("關於「叏」的發音和釋義，請見「夬」"), while 夬 is unambiguously the true phonetic component both sources cite for 缺. Corrected the field to `夬`. A new sub-pattern for the graphemic-classification bug taxonomy: a variant-of-the-phonetic used in place of the true phonetic form, rather than a sibling/parent swap.

`mc_id: 1506` verified against `CC 1000.md` line 531 — exact match, no off-by-one.

**`vietnamese` contamination fixed**: stored `khoét, khuyết`, but hvdic's entry for 缺 gives only `khuyết` under both Âm Hán Việt and Âm Nôm — no `khoét` anywhere. Removed as unattested.

**`joyo_level` gap filled**: blank → `表外字`, per en.Wiktionary's explicit hyōgai classification (缺 is the old/pre-reform form, superseded by 欠 in modern Japanese). Added as entry #354 to [[Lookup/Japanese/Hyōgai]]. `hsk_level: "2"` and `hanmun_edu_level: 高等` were already correctly set and confirmed cited in [[Lookup/HSK/Old HSK 2]] and [[Lookup/Korean/Korean HS]] respectively.

**`pos` gap filled**: blank → `動詞`, matching the citing stand-in word [[欠缺]]'s own `動詞`.

Checked en.Wiktionary's "Alternative forms" list (缼, 𦈫, 𧖫, 𡙇, 𡚆) as potential `aliases` additions, but zh.Wiktionary didn't corroborate them as clearly as required by the dual-source policy — left `aliases` empty rather than add single-source-only forms.

Rebuilt the malformed Notes section: three word-citation bullets (缺勤, 缺席, 缺点) had been stuffed into `## Notes` instead of `## Words`, alongside floating unlinked CC initial/final wikilinks. Rebuilt into the standard four-bullet Notes and moved all three words — plus the already-present stand-in [[欠缺]] — into a complete `## Words` section. No chengyu cite 缺; no other character names it as a phonetic/semantic component, so no `## Derived Characters` applies. Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 鞍 (7478; 786 characters remaining).

### 2026-08-15, iteration 1719 — [[characters/鞍|鞍]]

`mc_id: 3088` verified against `CC 3000.md` line 93 — exact match. `graphemic_classification: 安` and `joyo_level: 日本人名用漢字` both reconfirmed correct via en.Wiktionary + zh.Wiktionary (形声, semantic 革 "leather" + phonetic 安; Jinmeiyō, not Jōyō). `vietnamese: an, yên` reconfirmed correct via hvdic — both dual-classified as Hán Việt and Nôm, no contamination.

**`stand_in` bug found and fixed**: stored `鞍裝`, but the actual citing word file is [[鞍装]] (shinjitai 装, not 裝) — 鞍裝 is merely one of *that word's own* `aliases`, not its filename. A reverse instance of the established alias/parent-form rule: the CHARACTER page's `stand_in` field, not just a word's `characters:` list, can point at an alias instead of the true form. Corrected to `鞍装`.

**`aliases` gap filled**: both en.Wiktionary ("See also: 鞌") and zh.Wiktionary ("異體字（鞌）") independently confirm 鞌 as a genuine variant of 鞍; no separate vault page exists for it, ruling out a false-positive. Added.

**`pos` gap filled**: blank → `名詞`, matching the citing word 鞍装's own `名詞`.

Confirmed the phonetic parent [[characters/安|安]]'s own `## Derived Characters` list already correctly cites 鞍 — no consequence-fix needed there. Rebuilt the malformed Notes (previously one merged 形声/会意 bullet plus two floating CC-lookup wikilinks) into the standard four-bullet format, and added the missing `## Words` section citing [[鞍装]]. No chengyu cite 鞍. Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 庵 (7479; 785 characters remaining).

### 2026-08-15, iteration 1720 — [[characters/庵|庵]]

`graphemic_classification: 奄` and `joyo_level: 日本人名用漢字` both reconfirmed correct via dual-source agreement (形声, semantic [[Radical 053|广]] "dwelling" + phonetic 奄; Jinmeiyō, not Jōyō). `mc_id: 10574` is trusted long-tail (>4000), left as-is per policy.

**`vietnamese` contamination fixed**: stored `am, im`, but hvdic's entry gives `am` alone under "Âm Hán Việt:", with `im` appearing only under "Âm Nôm:" alongside `am` — a pure Nôm-only-reading removal, the same sub-pattern as several earlier fixes this session. Reduced to `am`.

**`aliases` gap filled**: en.Wiktionary's own "Alternative forms" list and zh.Wiktionary's 異體字 list both independently include 菴 and 盦 — added both. zh.Wiktionary's list also threw in 奄 itself, 广, and 厂, but those are excluded as the established "phonetic-series/radical member mistaken for variant" false-positive category — 奄 is 庵's own phonetic parent with a fully independent vault page and meaning, and 广/厂 are unrelated Kangxi radicals, not variants of 庵.

**`pos` gap filled**: blank → `名詞`, matching the citing stand-in word [[庵子]]'s own `名詞`.

Checked the phonetic parent [[characters/奄|奄]]'s own `## Derived Characters` list — 庵 is already cited there (alongside 掩/淹/俺/唵), though none of that list's five entries carry the ruby-annotated syllable the checklist calls for. Left untouched: fixing only 庵's own entry would leave it inconsistently formatted against its four unruby'd siblings, and reformatting the whole list is beyond this iteration's one-character scope — flagging here for whenever 奄 itself comes up for re-perfection.

Rebuilt the malformed Notes section (previously a bare `# Notes` H1 heading over two floating, unlinked CC wikilinks) into the standard four-bullet format, and added the missing `## Words` section citing the stand-in [[庵子]]. No chengyu cite 庵. Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 埃 (7480; 784 characters remaining).

### 2026-08-15, iteration 1721 — [[characters/埃|埃]]

`mc_id: 2611` verified against `CC 2000.md` line 640 — exact match. `graphemic_classification: 矣` reconfirmed correct (形声, semantic [[Radical 032|土]] "earth" + phonetic 矣, per Shuowen Jiezi quoted directly on zh.Wiktionary: "塵也。从土矣聲"). `joyo_level: 表外字` reconfirmed correct via zh.Wiktionary and was already properly cited on [[Lookup/Japanese/Hyōgai]]. `vietnamese: ai` reconfirmed correct via hvdic, dual-classified identically, no contamination.

**`hsk_level` gap filled**: blank → `無` — no attestation in any of the vault's HSK lookup lists despite the character's everyday-sounding gloss ("dust"); added to the manual [[Lookup/HSK/HSK No]] list.

**`pos` gap filled**: blank → `名詞`, matching the citing stand-in word [[塵埃]]'s own `名詞`.

zh.Wiktionary's page threw in "雉" (pheasant) as a purported variant form, but this had no en.Wiktionary corroboration and is semantically implausible for a dust/dirt character — treated as a spurious extraction rather than a genuine alias and not added. Confirmed the phonetic parent [[characters/矣 (char)|矣]] already cites 埃 in its own Derived Characters list — no consequence-fix needed.

Rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks) into the standard four-bullet format, and added the missing `## Words` section citing [[塵埃]]. No chengyu cite 埃. Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 涛 (7481; 783 characters remaining).

### 2026-08-15, iteration 1722 — [[characters/涛|涛]]

`mc_id: 3313` verified against `CC 3000.md` line 330 (indexed under the traditional form 濤, already the vault's own stored alias). `graphemic_classification: 寿` reconfirmed correct — both en.Wiktionary and zh.Wiktionary agree 涛/濤 is 形聲 with semantic [[Radical 085|水]] ("water") + phonetic 壽/寿, and pulled the Zhengzhang OC reconstruction (*duː*, from the traditional-form entry, since the simplified page lacked one). `vietnamese: đào` reconfirmed correct via hvdic, dual-classified identically. `pos: 名詞` already correctly matched the citing stand-in word [[怒涛]]'s own value.

**`joyo_level` gap filled**: blank → `表外字`, per en.Wiktionary's explicit hyōgai classification for the shinjitai form. Added as entry #355 to [[Lookup/Japanese/Hyōgai]]'s numbered list — note a `濤 --> 涛` line already existed in that file's separate "Redirects" section, but that's a distinct manual cross-reference list, not the actual Hyōgai citation, so it didn't already satisfy the checklist requirement.

Confirmed the phonetic parent [[characters/寿|寿]]'s own `## Derived Characters` list already correctly cites 涛 with ruby. Rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks) into the standard four-bullet format, and added the missing `## Words` section citing [[怒涛]]. No chengyu cite 涛. Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 灘 (char) (7482; 782 characters remaining).

### 2026-08-15, iteration 1723 — [[characters/灘 (char)|灘]]

`graphemic_classification: 難`, `joyo_level: 日本人名用漢字` (Jinmeiyō, not Jōyō), and `vietnamese: than` all reconfirmed correct via dual-source agreement (形声, semantic [[Radical 085|水]] "water" + phonetic 難; hvdic gives `than` identically under both Hán Việt and Nôm). `mc_id: 5301` is trusted long-tail (>4000).

**`aliases` gap filled**: both en.Wiktionary and zh.Wiktionary confirm 潬 as a genuine ancient variant of 灘 (alongside the already-stored simplified form 滩); no independent vault page exists for it. Added.

**`pos` gap filled**: blank → `名詞`. Unlike most recent iterations, the citing stand-in here is the character's own name (`stand_in: 灘`), and that word page ([[words/灘]]) is itself unperfected with no `pos` of its own to match — so this was an independent judgment call from the English gloss ("bank, shoal") rather than a cross-reference.

Confirmed the phonetic parent [[characters/難|難]]'s own `## Derived Characters` list already correctly cites 灘 with ruby — no consequence-fix needed. Fixed a `../` path bug in the disambiguation callout's link to the word page. Rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks) into the standard four-bullet format, and added the missing `## Words` section citing the self-named word [[灘]]. No chengyu cite 灘. Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 蘇 (7483; 781 characters remaining).

### 2026-08-15, iteration 1724 — [[characters/蘇|蘇]]

`mc_id: 993` verified against `CC 0000.md`'s blockquote-formatted listing ("> 993. 蘇") — exact match. `graphemic_classification: 穌` and `joyo_level: 日本人名用漢字` both reconfirmed correct (形声, semantic [[Radical 140|艸]] "grass" + phonetic 穌 — the character's own historical root form, later given the 艸 determinative; Jinmeiyō, not Jōyō).

**`vietnamese` contamination fixed**: stored `su, to, tua, tô`, but hvdic's "Âm Hán Việt:" line gives only `tô, tố` — `su, to, tua` are Nôm-only (confirmed under a separate "Âm Nôm:" line that also includes `tô`). Reduced to the two genuine Hán Việt readings and added the previously-missing `tố`.

**`aliases` all three re-verified rather than assumed correct**: 苏 (simplified) is uncontroversial; 穌 and 甦 both initially looked like the established "phonetic-series member with independent meaning" false-positive pattern (en.Wiktionary explicitly called 穌 phonetic-only and 甦 an independently-defined compound), but zh.Wiktionary's own 蘇 page explicitly lists both in its 異體字 section, and the citing word [[蘇生]]'s own Notes independently confirm 甦生 as an attested graphic-variant spelling. Kept both — a case where an etymologically-distinct sibling character can still be a genuine, dual-corroborated variant in actual usage, not just a lookalike.

**`pos` gap filled**: blank → `事詞`, matching the citing stand-in word [[蘇生]]'s own `事詞`.

Checked five chengyu that mention 蘇 in passing (all incidental references to the historical figure 蘇軾/蘇秦 in prose, none listing 蘇 in their own `characters:` field) — confirmed none belong in `## Chengyu`. Rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks, with an otherwise-correct `## Words` section already in place) into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 灌 (7484; 780 characters remaining).

### 2026-08-15, iteration 1725 — [[characters/灌|灌]]

`mc_id: 1313` verified against `CC 1000.md` line 330 — exact match. **Near-miss on `graphemic_classification`**: the stored value `鸛` (stork) initially looked like the same "wrong sibling character" bug found on 缺 and 涛, since the true phonetic component is 雚 and en.Wiktionary confirms 灌 = semantic 水 + phonetic 雚, not 鸛. But checking the phonetic-parent page itself first — [[characters/鸛|鸛]], already perfected 2026-07-29 — revealed this is a deliberate, documented vault convention: 雚 has no character page of its own, so it's registered as an *alias* of 鸛's page, and citations of the phonetic component correctly point to 鸛 as the parent form holding that alias (per the vault's own `feedback_alias_parent_form` policy, cited directly in 鸛's Notes). Left `鸛` unchanged — correcting it to 雚 would have broken this convention, not fixed a bug.

**`vietnamese` gap filled**: stored `quán` alone, but hvdic's "Âm Hán Việt:" line gives both `hoán` and `quán` — added the missing `hoán` rather than removing anything (a "missing genuine reading" gap, the mirror image of the more common contamination-removal pattern). `joyo_level: 表外字` and both `aliases` (浂, 潅) all reconfirmed correct via en.Wiktionary.

**`pos` gap filled**: blank → `名詞`, matching the citing stand-in word [[灌漑]]'s own `名詞`.

Confirmed [[characters/鸛|鸛]]'s own `## Derived Characters` list already correctly cites 灌 with ruby — no consequence-fix needed. Rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks, with an otherwise-correct `## Words` section already in place) into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 膿 (char) (7485; 779 characters remaining).

### 2026-08-15, iteration 1726 — [[characters/膿 (char)|膿]]

**`mc_id` off-by-one found and fixed**: stored `2735`, but `CC 2000.md` line 768 shows 2735 is actually 楯's rank — 膿 itself is line 769, rank `2736`. Corrected. `graphemic_classification: 農` reconfirmed correct (形声, semantic [[Radical 130|肉]] "flesh" + phonetic 農) and `joyo_level: 表外字` reconfirmed correct, both via en.Wiktionary.

**`vietnamese` fixed with both a removal and an addition**: stored `nùng, nọng, nồng`, but hvdic's "Âm Hán Việt:" line gives only `nung, nùng` — `nọng` and `nồng` are Nôm-only (removed), and the genuine `nung` was missing entirely (added). Net result: `nung, nùng`.

**`pos` gap filled**: blank → `名詞`. As with 灘 earlier this session, the citing stand-in is the character's own name and the word page ([[words/膿]]) is itself unperfected with no `pos` to cross-reference, so this was an independent call from the English gloss ("pus").

Confirmed the phonetic parent [[characters/農|農]]'s own `## Derived Characters` list already correctly cites 膿 with ruby — no consequence-fix needed. Fixed a `../` path bug in the disambiguation callout's link to the word page. Rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks) into the standard four-bullet format, and added the missing `## Words` section citing the self-named word [[膿]]. Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 醤 (7486; 778 characters remaining).

### 2026-08-15, iteration 1727 — [[characters/醤|醤]]

**`mc_id` off-by-one found and fixed**: stored `2930`, but `CC 2000.md` line 971 shows 2930 is actually 誄's rank; 醬 itself is line 972, rank 2931. Corrected.

**`joyo_level` bug found and fixed**: stored `日本人名用漢字` (Jinmeiyō), but en.Wiktionary explicitly classifies 醤 as **Hyōgai kanji** (表外字), not Jinmeiyō — a genuine field error, not just a blank gap. Corrected, and added as entry #356 to [[Lookup/Japanese/Hyōgai]]'s numbered list (both Hyōgai's and Jinmeiyō's files had only a `醬 --> 醤` cross-reference in their separate "Redirects" sections, neither of which counts as the real citation — the same distinction caught on 涛 two iterations ago).

**`vietnamese` gap filled**: was entirely blank; hvdic gives `tương` (dual-classified Hán Việt/Nôm identically) for 醬 — added. `graphemic_classification: 将` reconfirmed correct (形声, semantic [[Radical 164|酉]] "wine vessel, fermentation" + phonetic 将).

Checked the phonetic component 将 for a vault character page to consequence-fix — none exists, same as 雚/穌 earlier this session, so the field correctly names a pageless phonetic component. Also caught and fixed a duplicate `vietnamese:` YAML key introduced mid-edit (an empty leftover key from the file's pre-edit state that my first pass missed) before it could corrupt the frontmatter.

Rebuilt the malformed Notes (an out-of-order `## Words` section preceding a bare `# Notes` H1, itself just two floating CC wikilinks plus a third stray word-citation bullet) into the standard four-bullet format, and consolidated the full `## Words` list — the stand-in [[果醤]], plus already-cited [[芝麻醤]] and [[醤油]] — in one place. No chengyu or vault-paged phonetic parent needed touching. Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 幇 (7487; 777 characters remaining).

### 2026-08-15, iteration 1728 — [[characters/幇|幇]]

`mc_id: 0` re-verified per policy — grepped all four `CC 0000–3000.md` files for both 幇 and 幫, zero hits confirmed, genuinely absent from the ranking rather than an unchecked placeholder. `graphemic_classification: 封` reconfirmed correct (形声, semantic [[Radical 050|巾]] "cloth" + phonetic 封).

**`joyo_level` gap filled**: blank → `表外字`, per en.Wiktionary (幇 is the shinjitai/extended form, hyōgai, with 幫 as kyūjitai). Added as entry #357 to [[Lookup/Japanese/Hyōgai]]. **`vietnamese` gap filled**: blank → `bang`, per hvdic (dual-classified Hán Việt/Nôm identically for 幫/幇). **`pos` gap filled**: blank → `動詞`, matching the citing stand-in word [[幇助]]'s own `動詞`.

**`aliases` gap filled**: 幫 (traditional/kyūjitai, already stored) reconfirmed correct; added `帮` (simplified), dual-corroborated by en.Wiktionary and zh.Wiktionary as the modern simplified form, with no independent vault page of its own.

Confirmed the phonetic parent [[characters/封 (char)|封]]'s own `## Derived Characters` list already correctly cites 幇 with ruby — no consequence-fix needed. Rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks, with an otherwise-correct `## Words` section already in place) into the standard four-bullet format, phrasing the MC bullet per the `mc_id: 0` convention ("Not present in the Classical Chinese usage ranking"). Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 牆 (7488; 776 characters remaining).

### 2026-08-15, iteration 1729 — [[characters/牆|牆]]

**`graphemic_classification` semantic/phonetic swap found and fixed in the field itself**: stored `嗇`, but both en.Wiktionary ("phonetic 爿 + semantic 嗇") and zh.Wiktionary ("聲符 爿 + 意符 嗇") explicitly and unambiguously identify 爿 as the phonetic component and 嗇 as semantic — the reverse of what was stored. A genuine field-level swap, not a citation-vs-prose mismatch (matching the rarer bug sub-category previously seen only on 靡/聚). The likely cause: 爿 has no character page of its own in this vault, while 嗇 does — an easy trap where the "citable" component gets used regardless of whether it's actually the phonetic or semantic one. Corrected to `爿`, linked via `[[Radical 090|爿]]` in the Notes bullet per the radical-linking rule (爿 is itself Kangxi Radical 090), with 嗇 now linked as a bare `[[嗇]]` semantic component instead. Verified no consequence-fix was needed on [[characters/嗇|嗇]] (itself still unperfected, danayo_id 7551, further down the queue) — since 牆 was never really 嗇's derived child, there was nothing wrongly cited there to remove.

`mc_id: 1734` verified against `CC 1000.md` line 767 — exact match. `vietnamese: tường` reconfirmed correct via hvdic (dual-classified identically). **`pos` gap filled**: blank → `名詞`, matching the citing stand-in word [[牆壁]]'s own `名詞`. Both aliases (墙, 墻) reconfirmed correct via en.Wiktionary.

Rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks, with an existing `## Chengyu` section but no `## Words` at all) into the standard four-bullet format, and added the missing `## Words` section citing the stand-in [[牆壁]]. Stamped `date-last-perfect: 2026-08-15`.

Next never-perfected character by `danayo_id`: 諡 (7489; 775 characters remaining).

### 2026-08-16, iteration 1730 — [[characters/諡|諡]]

`mc_id: 2003` verified against `CC 2000.md` line 8 — exact match. `graphemic_classification: 益` reconfirmed correct (形声, semantic [[Radical 149|言]] "speech" + phonetic 益, OC *ɢliɡs). `vietnamese: thuỵ` reconfirmed correct via hvdic, dual-classified identically. `joyo_level: 表外字` reconfirmed correct via en.Wiktionary, and was already properly cited on [[Lookup/Japanese/Hyōgai]]. The alias 謚 reconfirmed as a genuine mutual variant via both en.Wiktionary ("諡 is a variant form of 謚") and zh.Wiktionary (異體字), with no independent vault page of its own.

**`pos` gap filled**: blank → `名詞`, matching the citing stand-in word [[諡号]]'s own `名詞`. Also fixed an unrelated typo in the `english` field ("posthumus" → "posthumous").

Confirmed the phonetic parent [[characters/益|益]]'s own `## Derived Characters` list already correctly cites 諡 with ruby — no consequence-fix needed. Rebuilt the malformed structure (an out-of-order `## Words` section preceding a bare, unlinked `# Notes` block) into the standard four-bullet Notes plus a properly-ordered `## Words` section. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 錐 (7490; 774 characters remaining).

### 2026-08-16, iteration 1731 — [[characters/錐|錐]]

`mc_id: 2950` verified against `CC 2000.md` line 991 — exact match. `graphemic_classification: 隹` and `joyo_level: 日本人名用漢字` both reconfirmed correct (形声, semantic [[Radical 167|金]] "metal" + phonetic 隹; Jinmeiyō).

**`vietnamese` heaviest contamination fix this session**: stored five readings (`chui, chuỳ, chõi, chỏi, dùi`), but hvdic's genuine "Âm Hán Việt:" line gives only `chuỳ, truỳ`. Of the other four, `dùi` is Nôm-only, and `chui`, `chõi`, `chỏi` don't appear under either Hán Việt or Nôm at all — pure fabrication, not even a contamination category previously seen (Nôm-misattribution), more like unattested noise. Reduced to the two genuine readings, adding the missing `truỳ`.

**`hsk_level` gap filled**: blank → `無`, no attestation in any vault HSK list; added to [[Lookup/HSK/HSK No]]. **`pos` gap filled**: blank → `名詞`, matching the citing stand-in word [[錐子]]'s own `名詞`.

**Consequence-fix applied to an out-of-scope, still-unperfected page**: the phonetic parent [[characters/隹|隹]] (danayo_id 8774, not yet reached in the queue) had no `## Derived Characters` section at all despite 錐 citing it as phonetic — added one with the single 錐 entry, following the established practice of minimal fixes on parent pages regardless of their own perfection status.

Rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks, with an otherwise-correct `## Words` section already in place) into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 畿 (7491; 773 characters remaining).

### 2026-08-16, iteration 1732 — [[characters/畿|畿]]

`mc_id: 3284` verified against `CC 3000.md` line 297 — exact match. `graphemic_classification: 幾` reconfirmed correct (形声, semantic [[Radical 102|田]] "field" + abbreviated phonetic 幾). `vietnamese: kì, kỳ` reconfirmed correct via hvdic, both dual-classified identically. The alias 㙨 reconfirmed via both en.Wiktionary and zh.Wiktionary as a genuine variant, no independent vault page.

**Near false-alarm on `joyo_level`**: en.Wiktionary calls 畿 a plain "Jōyō kanji," which at first glance looked like a mismatch against the stored value `高等`. But the vault's own mapping table treats `高等` as a valid `joyo_level` value in its own right — Jōyō-Kōtō, the secondary-school-taught subset of Jōyō kanji, distinct from the elementary Kyōiku set — so the stored value was already correct; it just needed the right lookup link ([[Lookup/Japanese/Jōyō - Kōtō]], not the identically-spelled Korean [[Lookup/Korean/Korean HS]] that `hanmun_edu_level: 高等` maps to). A reminder that the same string can be a legitimate value across two unrelated fields with two different lookup targets.

**`hsk_level` gap filled**: blank → `無`, no attestation in any vault HSK list; added to [[Lookup/HSK/HSK No]]. **`pos` gap filled**: blank → `名詞`, matching the citing stand-in word [[京畿]]'s own `名詞`.

**Fixed a rendering bug in the Notes bullet itself**: the semantic radical's gloss was empty (`("")`) and the phonetic link was a bare empty wikilink (`[[]]`) — both silently swallowed, presumably from a failed substitution upstream. Restored the gloss ("field") and the link ([[幾 (char)|幾]]). Confirmed the phonetic parent [[characters/幾 (char)|幾]]'s own `## Derived Characters` list already correctly cites 畿 with ruby — no consequence-fix needed. Fixed the malformed `## Words` entry for [[京畿]] (was a bare wikilink with no ruby or gloss) and rebuilt the four-bullet Notes structure. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 楚 (7493; 772 characters remaining).

### 2026-08-16, iteration 1733 — [[characters/楚|楚]]

`mc_id: 114` verified against `CC 0000.md` line 122 (blockquote-formatted) — exact match, one of the highest-frequency characters perfected this session. `graphemic_classification: 疋` reconfirmed correct via dual-source agreement (形声, semantic [[Radical 075|木]] "wood, forest" + phonetic 疋). `joyo_level: 日本人名用漢字` reconfirmed correct (Jinmeiyō).

**`vietnamese` contamination fixed**: stored `sở, sỡ`, but hvdic's genuine entry gives only `sở` — `sỡ` doesn't appear under either Hán Việt or Nôm at all, unattested fabrication rather than a Nôm-misattribution. Removed.

**`aliases` gap filled**: both en.Wiktionary and zh.Wiktionary independently list the same four ancient variant forms (椘, 䠂, 𣕑, 𣗂) — all added, none with existing vault pages.

**`pos` gap filled**: blank → `性詞` (stative), based on the character's own core meaning "clear" rather than borrowing the citing compound word [[清楚]]'s broader `実詞` (a superordinate content-word category, not a specific POS tag fit for an individual character entry).

**Consequence-fix applied to an out-of-scope, still-unperfected page**: the phonetic parent [[characters/疋|疋]] (danayo_id 8017, not yet reached) had no `## Derived Characters` section at all — added one with the single 楚 entry.

Rebuilt the malformed Notes (bare floating unlinked CC wikilinks with an out-of-order but otherwise-correct `## Words` section preceding them) into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 爺 (7494; 771 characters remaining).

### 2026-08-16, iteration 1734 — [[characters/爺|爺]]

`mc_id: 0` re-verified — grepped all four `CC 0000–3000.md` files for both 爺 and its phonetic 耶; only 耶 itself appears (rank 1818), 爺 genuinely absent. `graphemic_classification: 耶` reconfirmed correct (形声, semantic [[Radical 088|父]] "father" + phonetic 耶, OC *laː). `joyo_level: 表外字` reconfirmed correct via zh.Wiktionary, already properly cited on [[Lookup/Japanese/Hyōgai]].

**`vietnamese` gap filled**: stored `gia` alone, but hvdic's "Âm Hán Việt:" line gives both `da` and `gia` — added the missing `da`.

**`aliases` false-positive avoided**: zh.Wiktionary's own 異體字 list for 爺 includes both 爷 and 耶, but 耶 is 爺's phonetic-series source with its own independent vault page and distinct grammatical-particle meaning — the same "phonetic-series member listed as variant" pattern caught repeatedly this session (cf. 悷/唳, 取/娶). Kept only 爷 (genuine simplified form).

**`pos` gap filled**: blank → `名詞`, matching the citing stand-in word [[老爺]]'s own `名詞`.

Confirmed the phonetic parent [[characters/耶 (char)|耶]]'s own Words/Derived section already correctly cites 爺 with ruby — no consequence-fix needed. Rebuilt the malformed Notes (missing SKIP/Stroke and Levels bullets entirely, a word citation for [[爺爺]] stuck inside Notes instead of Words) into the standard four-bullet format plus a complete `## Words` section citing both [[老爺]] and [[爺爺]]. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 惮 (7495; 770 characters remaining).

### 2026-08-16, iteration 1735 — [[characters/惮|惮]]

**`mc_id` off-by-one found and fixed**: stored `1712`, but `CC 1000.md` line 745 shows 1712 is actually 冤's rank — 憚 itself is line 746, rank `1713`. Corrected.

**Near-miss on `graphemic_classification`**: stored `単` (the Japanese shinjitai form), which at first glance looked mismatched since 惮 is itself the simplified Chinese form and its "native" phonetic component would be 单. But checking the parent page first — [[characters/単|単]], already perfected — showed it already holds both 單 (traditional) and 单 (simplified) as its own aliases, meaning 単 is the vault's established registered parent for this entire phonetic-series triplet, the same convention documented on 鸛 (single canonical page absorbing sibling forms as aliases). Left unchanged — correct as stored.

**`vietnamese` fully re-derived, not just trimmed**: stored `dạn, đạn, đặn`, but hvdic's genuine "Âm Hán Việt:" line gives `đát, đạn` — of the three stored readings, only `đạn` is dual-classified/genuine; `dạn` and `đặn` are Nôm-only. Removed both and added the missing `đát`.

**Consequence-fix applied**: added a `## Derived Characters` section to [[characters/単|単]] (it had none) citing 惮.

Rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks, with a word citation stuck inside Notes instead of `## Words`) into the standard four-bullet format. `pos: 性詞` was already correctly filled. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 梁 (char) (7497; 769 characters remaining).

### 2026-08-16, iteration 1736 — [[characters/梁 (char)|梁]]

`mc_id: 368` verified against `CC 0000.md` line 383 (blockquote-formatted) — exact match. `graphemic_classification: 刅` and `joyo_level: 日本人名用漢字` both reconfirmed correct (形声, a three-part compound with semantic [[Radical 085|水]] "water" + [[Radical 075|木]] "wood" + phonetic 刅; Jinmeiyō). `vietnamese: lương` reconfirmed correct via hvdic, dual-classified identically.

**`aliases` false-positive avoided**: en.Wiktionary's "Alternative forms" list for 梁 includes 粱 alongside the already-stored 樑, but 粱 has its own fully independent meaning ("millet, sorghum, grain") rather than being a variant of 梁 (beam/bridge) — a textbook instance of the phonetic-series false-positive pattern, kept out of `aliases`. 樑 itself reconfirmed genuine via en.Wiktionary's "See also" note.

Confirmed no vault page exists for the phonetic component 刅, so no consequence-fix was possible/needed there. Rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks) into the standard four-bullet format, fixed a `../` path bug in the disambiguation callout, and added the missing self-named word [[梁]] to `## Words` (already had [[棟梁]] and [[跳梁]]). Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 芻 (7498; 768 characters remaining).

### 2026-08-16, iteration 1737 — [[characters/芻|芻]]

`mc_id: 1763` verified against `CC 1000.md` line 796 — exact match. `graphemic_classification: 會意` reconfirmed correct (ideogrammic, [[Radical 020|勹]] "hand" + [[Radical 045|屮]] "grass" — a hand plucking grass), both components linked via their Radical pages per the radical-linking rule. `joyo_level: 表外字` reconfirmed correct.

**`vietnamese` contamination fixed**: stored `ro, so, sô, sồ`, but hvdic's genuine "Âm Hán Việt:" line gives only `sô` — `ro` and `so` are Nôm-only, and `sồ` is unattested under either category. Reduced to the single genuine reading.

**`pos` gap filled**: blank → `名詞`, matching the citing stand-in word [[乾芻]]'s own `名詞`. Also added a missing "(stand-in for 芻)" annotation to that same Words entry.

**Consequence-fix applied to an out-of-scope, still-unperfected page**: [[characters/屮|屮]] (danayo_id 8732, not yet reached) had no `## Derived Characters` section — added one citing 芻.

Rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks) into the standard four-bullet format; the existing `## Words` and `## Derived Characters` sections (already correctly citing [[趨 (char)|趨]]) needed no other changes. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 哥 (7499; 767 characters remaining).

### 2026-08-16, iteration 1738 — [[characters/哥|哥]]

An etymological outlier: en.Wiktionary explicitly describes 哥 as a *stacked* form of 可 (⿱可可, "perhaps an open mouth with breath going out") rather than a standard semantic+phonetic 形声 compound — a later vernacular coinage that doesn't appear in the Shuowen Jiezi at all, per the citing word [[哥哥]]'s own Notes. Left `graphemic_classification: 可` unchanged (it correctly names the reused component either way) but rewrote the Notes bullet to describe the actual stacked-form etymology rather than force it into the standard 形声 phrasing. `mc_id: 5886` is trusted long-tail (>4000).

**`vietnamese` heavily contaminated, fixed**: stored `ca, cả, gã, kha`, but hvdic's genuine "Âm Hán Việt:" line gives only `ca` — `kha` is Nôm-only, and `cả`/`gã` are unattested under either category. Reduced to `ca` alone.

**`hanmun_edu_level` gap filled**: blank → `無` (a colloquial Tang-era vernacular coinage, not part of Korean's classical hanja curriculum; [[Lookup/Korean/Korean Missing]] is a pure dataview query, no manual list edit needed). **`pos` gap filled**: blank → `名詞`, matching the citing stand-in word [[哥哥]]'s own `名詞`.

**Pre-existing citation gap found and fixed independent of any value change**: `joyo_level: 表外字` was already correctly set before this iteration, but had never actually been added to [[Lookup/Japanese/Hyōgai]]'s numbered list — added as entry #358.

Fixed a duplicate: the Notes section had a stray "abbreviation for copernicium: [[哥金]]" bullet duplicating an entry already properly present in `## Words` — removed from Notes, left the Words entry as the single source. Rebuilt the four-bullet Notes structure and confirmed the phonetic parent [[characters/可 (char)|可]]'s own Words list already correctly cites 哥. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 伍 (char) (7500; 766 characters remaining).

### 2026-08-16, iteration 1739 — [[characters/伍 (char)|伍]]

`mc_id: 1160` verified against `CC 1000.md` line 169 — exact match. `graphemic_classification: 五` and `joyo_level: 日本人名用漢字` both reconfirmed correct (形声, semantic [[Radical 009|人]] "person" + phonetic 五; Jinmeiyō). `vietnamese: ngũ` reconfirmed correct via hvdic, dual-classified identically.

**`pos` gap filled**: blank → `名詞`, matching the citing self-named word [[伍]]'s own `名詞`. No `aliases` needed — en.Wiktionary describes 伍 itself as 五's dedicated anti-forgery financial-numeral variant (matching the citing word's own Notes, which lists it alongside 壱/貳/漆/玖 for 一/二/七/九), not the reverse.

Checked the phonetic parent [[characters/五 (char)|五]] (itself badly malformed and unperfected, with non-standard heading names like `### Descendants` and `## Important Words` instead of the standard section names) — it already informally cites 伍 there, so left it untouched rather than reformat an unrelated section beyond this iteration's scope. Fixed a `../` path bug in the disambiguation callout, rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks, no `## Words` at all) into the standard four-bullet format plus a `## Words` section citing the self-named word [[伍]]. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 兪 (char) (7501; 765 characters remaining).

### 2026-08-16, iteration 1740 — [[characters/兪 (char)|兪]]

**Near-miss on `mc_id`**: stored `1536`, which at first glance looked like it might be the familiar off-by-one bug pattern. But `CC 1000.md` line 561 shows 1536 is exactly the rank of **俞** — and since en.Wiktionary explicitly states "兪 is a variant form of 俞" (deferring to it for pronunciation and definition), and 俞 has no separate vault page of its own (registered only as 兪's alias, mirroring the 雚/鸛 convention), citing 俞's own CC rank for 兪 is the established, correct pattern here — not a bug. Left unchanged.

**`vietnamese` gap filled, not contamination**: stored `dũ` alone; fetching hvdic for the alias-parent 俞 (since 兪 defers to it) showed `du, dũ` both listed as genuine Hán Việt — added the missing `du`.

**Large `## Derived Characters` reformatting**: the existing list (蝓, 喩, 愈, 愉, 揄, 諭, 逾) was present but entirely unformatted — six of the seven were bare, unlinked plaintext with no ruby or gloss. Verified each descendant's own stored `注音` (all identically ⼜ㄇ, confirming the page's own "-m by fiat" homophony-reduction note) and rebuilt the section with proper ruby-annotated links and glosses pulled from each descendant's `english` field.

Rebuilt the malformed Notes (mixed heading levels, an out-of-order `### Derived characters` before the CC bullet, word citations scattered after) into the standard four-bullet format plus a clean `## Words` section. `pos: 事詞` was already correctly filled. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 祐 (7502; 764 characters remaining).

### 2026-08-16, iteration 1741 — [[characters/祐|祐]]

`mc_id: 1809` verified against `CC 1000.md` line 846 — exact match. `graphemic_classification: 右` reconfirmed correct (形声, semantic [[Radical 113|示]] "spirit" + phonetic 右). `joyo_level: 日本人名用漢字` reconfirmed correct.

**`aliases` false-positive avoided**: en.Wiktionary calls 祐 an "alternative form of 佑," but 佑 has its own fully independent, already-perfected vault page (distinct `stand_in: 名専字`, different syllable ⼜ㄛ) — the established "independent vault character with own distinct meaning/page" false-positive category. Left `aliases` empty.

**`vietnamese` gap filled**: stored `hựu` alone; hvdic gives both `hữu` and `hựu` as genuine Hán Việt — added the missing `hữu`. **`pos` gap filled**: blank → `名詞`, matching the citing stand-in word [[天祐]]'s own `名詞`. Also fixed a stray typo in `english` ("divine aide" → "divine aid," the identical typo already caught and fixed on 天祐 itself).

**Consequence-fix applied**: [[characters/右|右]] (already perfected, danayo_id 62) had no `## Derived Characters` section despite being the phonetic parent for both 祐 and the already-perfected 佑 — added one citing both, ruby-annotated from each descendant's own syllable.

Rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks, no `## Words` at all) into the standard four-bullet format plus a `## Words` section citing [[天祐]]. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 洲 (char) (7503; 763 characters remaining).

### 2026-08-16, iteration 1742 — [[characters/洲 (char)|洲]]

A largely already-perfected page needing mostly light touch-ups. `mc_id: 3213` verified against `CC 3000.md` line 226 — exact match. `graphemic_classification: 州` reconfirmed correct.

**`vietnamese` contamination fixed**: stored `chao, châu`, but hvdic's genuine "Âm Hán Việt:" line gives only `châu` — `chao` is Nôm-only. Reduced to the single genuine reading. (Noted in passing that the already-perfected citing word [[洲]] carries the identical `chao, châu` contamination in its own frontmatter — left untouched as out-of-scope for this character-focused loop, but flagging it here for whenever word-perfecting resumes.)

**Path/link cleanup**: fixed a missing `../` prefix on the disambiguation callout's link to the word page; normalized four lowercase `lookup/...` path fragments to the vault's standard `Lookup/...` capitalization (SKIP, Stroke, HSK, Japanese, Korean lookup links); fixed a bare `[[州]]` wikilink in the graphemic bullet to correctly resolve to the actual filename `[[州 (char)|州]]`.

**`## Words` gap filled**: the self-named citing word [[洲]] (this character's own `stand_in`) was missing from its own Words list despite five compound words already being present — added.

**Consequence-fix applied**: the phonetic parent [[characters/州 (char)|州]] (already perfected) had no `## Derived Characters` section despite 洲 explicitly deriving from it — added one citing 洲.

`pos`, `joyo_level`, `hsk_level`, `hanmun_edu_level` were all already correctly filled; no changes needed there. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 珈 (7504; 762 characters remaining).

### 2026-08-16, iteration 1743 — [[characters/珈|珈]]

`mc_id: 7961` is trusted long-tail (>4000). `graphemic_classification: 加` reconfirmed correct (形声, semantic [[Radical 096|玉]] "jade" + phonetic 加).

**`aliases` false-positive category found and fully cleared**: all three stored aliases (迦, 袈, 咖) were phonetic-series cognates sharing 加 as their own root, not genuine variants of 珈 itself — confirmed by checking zh.Wiktionary's actual 異體字 section, which is empty for 珈 despite the etymology prose mentioning the related characters in passing. A instructive case: a plausible reading of Wiktionary's prose ("shares the same phonetic component") can look like alias evidence but isn't the same as an explicit variant-form declaration — the dual-source policy requires checking the dedicated variant-forms section, not just component-sharing language. Cleared all three, aliases now empty.

**`vietnamese` gap filled**: stored `gia` alone; hvdic gives both `gia` and `già` as genuine Hán Việt — added the missing `già`.

Rebuilt the malformed Notes (mixed content: word citations partially with ruby/paths, partially bare wikilinks with dash-glosses, all crammed into `## Notes` instead of `## Words`; floating unlinked CC wikilinks at the bottom) into the standard four-bullet format plus a proper `## Words` section, pulling each citing word's own stored 注音 for ruby rather than guessing (confirmed via direct grep on each of [[珈啡]], [[珈沙]], [[釈珈文尼]], [[珈拿陀]]). Confirmed the phonetic parent [[characters/加|加]]'s own Words list already correctly cites 珈 — no consequence-fix needed. `pos: 名詞` was already correctly filled. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 笙 (7505; 761 characters remaining).

### 2026-08-16, iteration 1744 — [[characters/笙|笙]]

**`mc_id` off-by-one found and fixed**: stored `2590`, but `CC 2000.md` line 615 shows 2590 is actually 頑's rank — 笙 itself is line 616, rank `2591`. Corrected. `graphemic_classification: 生` reconfirmed correct (形声, semantic [[Radical 118|竹]] "bamboo" + phonetic 生), `joyo_level: 日本人名用漢字` reconfirmed correct.

**`vietnamese` heavily contaminated, fixed**: stored five readings (`sanh, sinh, sênh, sềnh, xênh`), but hvdic's genuine "Âm Hán Việt:" line gives only `sanh, sinh` — `sênh` and `xênh` are Nôm-only, and `sềnh` is unattested under either category. Reduced to the two genuine readings.

**`hsk_level` gap filled**: blank → `無`, no attestation in any vault HSK list; added to [[Lookup/HSK/HSK No]]. **`pos` gap filled**: blank → `名詞`, matching the citing stand-in word [[鳳笙]]'s own `名詞`.

**Consequence-fix applied**: the phonetic parent [[characters/生|生]] (already perfected, a very large page with 30 Words entries and 4 existing Derived Characters) was missing 笙 from its `## Derived Characters` list — added it as the fifth entry.

Rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks, with an otherwise-correct `## Words` section already in place) into the standard four-bullet format. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 壱 (char) (7506; 760 characters remaining).

### 2026-08-16, iteration 1745 — [[characters/壱 (char)|壱]]

`mc_id: 1256` verified against `CC 1000.md` line 269 (indexed under the traditional/kyūjitai form 壹, already the vault's own stored alias). `graphemic_classification: 吉` reconfirmed correct (形声, semantic 壺 "jar" + phonetic 吉).

**`joyo_level: 高等` initially looked like a possible mismatch** — en.Wiktionary calls 壱 plain "Jōyō kanji" without specifying a sub-tier — but cross-checking Wikipedia's actual jōyō kanji table confirmed 壱 is grade "S" (Secondary school), which correctly maps to this vault's `高等` (Jōyō-Kōtō) convention. Left unchanged, correctly stored.

**`aliases` false-positive removed**: 佾 was stored as an alias, but en.Wiktionary confirms it has its own fully distinct meaning ("a row of dancers during a sacrificial rite," attested in the Analects' 八佾) — no connection to the numeral one beyond superficial visual similarity. Removed. 壹 (kyūjitai) and 弌 (ancient variant) both reconfirmed genuine via en.Wiktionary.

**`hsk_level` near-miss caught before shipping wrong data**: initially found no citation in [[Lookup/HSK/HSK No]] and almost filled `hsk_level: 無`, but a broader grep across the whole `Lookup/HSK` directory turned up 壹 already listed in [[Lookup/HSK/Old HSK 4]] — corrected to `hsk_level: "4"` instead, and reverted the erroneous HSK No addition before it went uncaught.

**`vietnamese` and `pos` gaps filled** by cross-referencing the citing stand-in word [[壱]]'s own already-perfected page: `vietnamese: nhất`, `pos: 性詞`.

Confirmed the phonetic parent [[characters/吉 (char)|吉]]'s own Words list already correctly cites 壱. Rebuilt the malformed Notes (a single stray dropped-from-list note, no proper Notes/Words structure at all) into the standard four-bullet format plus a `## Words` section, folding the original Korean-list note into the Words entry's own gloss. Fixed a `../` path bug in the disambiguation callout. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 灼 (7507; 759 characters remaining).

### 2026-08-16, iteration 1746 — [[characters/灼|灼]]

Mostly already-perfected fields, needing light verification and structural cleanup. `mc_id: 2595` verified against `CC 2000.md` line 620 — exact match. `graphemic_classification: 勺` reconfirmed correct (形声, semantic [[Radical 086|火]] "fire" + phonetic 勺). `vietnamese: chước`, `pos: 事詞`, `joyo_level`, `hsk_level`, `hanmun_edu_level` were all already correctly filled.

**Bare-wikilink filename bug found and fixed**: the graphemic bullet's `[[勺]]` link silently resolved to the unrelated word page `words/勺.md` rather than the character page — the actual file is `characters/勺 (char).md`. Corrected to `[[勺 (char)|勺]]`.

**Consequence-fix applied at scale**: the phonetic parent [[characters/勺 (char)|勺]]'s own `## Derived Characters` list (already citing all six of its descendants — 的/豹/約/釣/酌/灼) had every single entry as a bare unformatted wikilink with no ruby or gloss. Verified each descendant's own stored 注音 and English gloss directly, then reformatted the whole list to the standard ruby-annotated format — not just the one new entry, since leaving five siblings malformed next to one properly-fixed entry would have been visibly inconsistent.

Rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks, with one word citation dangling loose rather than in `## Words`) into the standard four-bullet format plus a complete `## Words` section citing both [[焼灼]] (the stand-in) and [[灼熱]]. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 汎 (char) (7508; 758 characters remaining).

### 2026-08-16, iteration 1747 — [[characters/汎 (char)|汎]]

`mc_id: 2778` verified against `CC 2000.md` line 811 — exact match. `graphemic_classification: 凡` reconfirmed correct (形声, semantic [[Radical 085|水]] "water" + phonetic 凡). Empty `aliases` reconfirmed correct — 泛 is en.Wiktionary's cited relative, but per the established `feedback_alias_parent_form` policy this vault treats 汎/氾/泛 as independently-meaningful vault characters, not aliases of each other.

**`joyo_level` bug found and fixed, contradicting the source that first surfaced it**: en.Wiktionary's summary flatly called 汎 "Jōyō kanji," which would have overwritten the correct stored value `高等` with an incorrect one. Cross-checked Wikipedia's actual jōyō kanji table directly — 汎 does **not** appear there at all; it's confirmed Jinmeiyō instead. Corrected `joyo_level` from `高等` to `日本人名用漢字` and added as entry #478 to [[Lookup/Japanese/Jinmeiyō]]. A second instance this session (after 壱) of Wiktionary's prose needing verification against the primary source table rather than trusted at face value — this time catching a wrong claim rather than confirming a right one.

**`vietnamese` gap filled with three genuine readings**: stored `phiếm, vàm`; hvdic's "Âm Hán Việt:" line gives `phiếm, phùng, phạp` — `vàm` is unattested under either Hán Việt or Nôm (removed), while `phùng` and `phạp` were missing entirely (added). **`pos` gap filled**: blank → `修飾語`, an independent judgment call from the character's own "pan-" gloss (a bound modifying prefix, not a noun or verb).

**Mid-fix citation-target error caught and corrected**: while filling the Levels bullet, initially linked `hanmun_edu_level: 名`'s citation to [[Lookup/Korean/Korean HS]] by reflex (echoing the page's own pre-existing "dropped from Korean HS in 2000" note) — caught before finalizing that this field value maps to [[Lookup/Korean/Korean Name ㅂ]] per the checklist's own mapping table, not Korean HS; the "dropped in 2000" fact explains *why* it's now name-only, but doesn't change which lookup page the current value cites. Corrected.

Fixed an empty radical gloss (`("")` → `("water")`) and a `../` path bug in the disambiguation callout. Rebuilt the malformed Notes/Words ordering into the standard structure. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 戍 (7509; 757 characters remaining).

### 2026-08-16, iteration 1748 — [[characters/戍|戍]]

`mc_id: 1623` verified against `CC 1000.md` line 652 — exact match. `graphemic_classification: 會意` reconfirmed correct ([[Radical 009|人]] "person" + [[Radical 062|戈]] "spear," both linked via their Radical pages per the radical-linking rule). `vietnamese: thú` and `joyo_level: 表外字` both reconfirmed correct; the latter had never actually been added to [[Lookup/Japanese/Hyōgai]] despite being correctly set — added as entry #360.

**`pos` gap filled**: blank → `名詞`, matching the citing stand-in word [[守戍]]'s own `名詞`. Also fixed a minor spacing typo in `english` ("borderguard" → "border guard," matching the citing word's own two-word gloss).

Rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks, no `## Words` at all) into the standard four-bullet format plus a `## Words` section citing [[守戍]]. No phonetic-parent consequence-fix applicable (this is a 會意 character with no single phonetic component). Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 尼 (7510; 756 characters remaining).

### 2026-08-16, iteration 1749 — [[characters/尼|尼]]

**`graphemic_classification` bug found and fixed**: stored `匕` (implying 形声 with 匕 as phonetic), but en.Wiktionary explicitly states 尼 is 會意 (two figures of 尸 leaning together) and that the traditional Shuowen 形声 analysis "is widely discredited by later scholars" — a genuine field-level classification error, not just a citation mismatch. Corrected to `會意`, with the outdated theory noted in the Notes bullet for context (matching the established precedent of documenting a superseded historical analysis, cf. 奄).

`mc_id: 1204` verified against `CC 1000.md` line 217 — exact match. `joyo_level: 高等` reconfirmed correct — jisho.org's own classification data confirms 尼 is Jōyō, taught at junior-high (secondary) level, matching this vault's Jōyō-Kōtō convention.

**`vietnamese` heavily contaminated, fixed**: stored seven readings (`nay, ni, này, nê, nì, nơi, nầy`), but hvdic's genuine "Âm Hán Việt:" line gives only `ni, nê, nật, nặc, nệ` — most of the stored set (`nay, này, nì, nơi, nầy`) were Nôm-only or entirely unattested. Replaced with the five genuine Hán Việt readings.

**`pos` gap filled**: blank → `名詞`, matching the citing stand-in word [[尼僧]]'s own `名詞`.

Rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks, with an otherwise-correct `## Words` section already in place) into the standard four-bullet format, and added the missing self-named-alternative stand-in citation [[尼僧]] to Words. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 帛 (7511; 755 characters remaining).

### 2026-08-16, iteration 1750 — [[characters/帛|帛]]

`mc_id: 1010` verified against `CC 1000.md` line 15 — exact match. `graphemic_classification: 白` and `joyo_level: 表外字` both reconfirmed correct (形声, semantic [[Radical 050|巾]] "cloth" + phonetic 白). `vietnamese: bạch` reconfirmed correct via hvdic, dual-classified identically — no contamination this time.

**`pos` gap filled**: blank → `名詞`, matching the citing stand-in word [[布帛]]'s own `名詞`.

**Consequence-fix applied**: the phonetic parent [[characters/白 (char)|白]] (already perfected, a large page with an existing five-entry Derived Characters list — 柏/百/珀/魄/拍) was missing 帛 — added it as the sixth entry.

Rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks, no `## Words` at all) into the standard four-bullet format plus a `## Words` section citing [[布帛]]. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 叭 (7512; 754 characters remaining).

### 2026-08-16, iteration 1751 — [[characters/叭|叭]]

`mc_id: 0` re-verified — grepped all four `CC 0000–3000.md` files, zero hits, genuinely absent. `graphemic_classification: 八` reconfirmed correct (形声, semantic [[Radical 030|口]] "mouth" + phonetic 八).

**`vietnamese` heavily contaminated, fixed**: stored seven readings, but hvdic's genuine "Âm Hán Việt:" line gives only `bá` — the other six (`bát, bớ, bớt, bợt, váp, vát`) were Nôm-only or entirely unattested. Reduced to the single genuine reading.

**`joyo_level` gap filled**: blank → `表外字`, per en.Wiktionary; added as entry #361 to [[Lookup/Japanese/Hyōgai]]. **`pos` gap filled**: blank → `名詞`, matching the citing stand-in word [[喇叭]]'s own `名詞`.

**Consequence-fix applied to an old-format, already-perfected page**: the phonetic parent [[characters/八 (char)|八]] (perfected 2026-03-19, an early-session page using non-standard section names like `### Data check` and a `### Links` numeral-navigation block) had no `## Derived Characters` section at all — added one citing 叭.

Rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks) into the standard four-bullet format, phrasing the MC bullet per the `mc_id: 0` convention, and added the missing `## Words` section citing [[喇叭]]. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 汀 (char) (7513; 753 characters remaining).

### 2026-08-16, iteration 1752 — [[characters/汀 (char)|汀]]

`mc_id: 9819` is trusted long-tail (>4000). `graphemic_classification: 丁` and `joyo_level: 日本人名用漢字` both reconfirmed correct (形声, semantic [[Radical 085|水]] "water" + phonetic 丁; Jinmeiyō).

**`vietnamese` contamination fixed**: stored `thinh, đinh, đênh`, but hvdic's genuine "Âm Hán Việt:" line gives only `đinh` — `thinh` and `đênh` are Nôm-only. Reduced to the single genuine reading.

**`pos` gap filled**: blank → `名詞`, matching the citing self-named stand-in word [[汀]]'s implicit noun sense (the word page itself has no `pos` set, so this was an independent judgment call from the shared gloss "sand bar").

**Large consequence-fix applied at scale**: the phonetic parent [[characters/丁 (char)|丁]]'s own `## Derived Characters` list (ten entries: 打/正/成/頂/庁/亭/訂/汀/釘/町) was entirely composed of bare, unformatted wikilinks with no ruby or gloss. Verified each descendant's own stored 注音 and English gloss directly, then reformatted the whole list to the standard ruby-annotated format — the same "fix the whole malformed sibling list, not just the newly-touched entry" pattern established earlier this session with 勺 and 兪.

Fixed a `../` path bug in the disambiguation callout. Rebuilt the malformed Notes (bare `# Notes` H1 over two floating unlinked CC wikilinks, no `## Words` at all) into the standard four-bullet format plus a `## Words` section citing the self-named word [[汀]]. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 曰 (char) (7514; 752 characters remaining).

### 2026-08-16, iteration 1753 — [[characters/曰 (char)|曰]]

`mc_id: 8` verified against `CC 0000.md` line 13 (blockquote-formatted, near the top of the entire ranking) — exact match, one of the highest-frequency characters perfected this session.

**`graphemic_classification` bug found and fixed**: stored `象形` (pictograph), but both en.Wiktionary and zh.Wiktionary explicitly classify 曰 as `指事` (ideogrammic-indicator: a mouth [[Radical 030|口]] with a breath/word-stroke coming out) — a genuine field-level type error, not just a citation mismatch. Corrected, and rewrote the Notes bullet using the standard 指事 format (linking [[Lookup/List of 指事]] per the checklist's own template).

**`vietnamese` contamination fixed**: stored `viết, vít, vất, vết`, but hvdic's genuine "Âm Hán Việt:" line gives only `viết` — the other three are Nôm-only. Reduced to the single genuine reading, matching the citing word [[曰]]'s own already-correct `viết`.

**`pos` gap filled**: blank → `実詞`, matching the citing self-named stand-in word [[曰]]'s own `実詞`. `joyo_level: 表外字` reconfirmed correct but had never actually been cited on [[Lookup/Japanese/Hyōgai]] — added as entry #362.

Fixed a `../` path bug in the disambiguation callout. Rebuilt the malformed Notes/Words structure into the standard format. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 軛 (char) (7516; 751 characters remaining).

### 2026-08-16, iteration 1754 — [[characters/軛 (char)|軛]]

A largely already-perfected page (`pos`, `joyo_level`, `hsk_level`, `hanmun_edu_level` all already correctly filled). `mc_id: 4283` is trusted long-tail (>4000). `graphemic_classification: 厄` reconfirmed correct (形声, semantic [[Radical 159|車]] "chariot" + phonetic 厄, which itself originally meant "yoke" before 車 was added to differentiate). `vietnamese: ách` reconfirmed correct via hvdic, dual-classified identically.

**`aliases` both reconfirmed genuine, with two additional Wiktionary-suggested candidates correctly excluded**: 軶 and 轭 (already stored) both confirmed as true variant/simplified forms. en.Wiktionary's "alternative forms" list also included 扼 and 戹, but these are independently-meaningful phonetic-series relatives ("grasp/strangle" and "difficulty/misfortune" respectively, not variants of 軛 itself) — correctly left out of the existing aliases, no change needed.

**Consequence-fix applied**: the phonetic parent [[characters/厄|厄]]'s own `## Derived Characters` entry for 軛 was a bare unformatted link — reformatted with ruby annotation and gloss.

Fixed a `../` path bug in the disambiguation callout, added the missing self-named word [[軛]] to `## Words`, and rebuilt the Notes into the standard four-bullet format (all four bullets were previously merged into one dense sentence with floating unlinked CC wikilinks below). Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 矩 (char) (7517; 750 characters remaining).

### 2026-08-16, iteration 1755 — [[characters/矩 (char)|矩]]

**`mc_id` off-by-one found and fixed**: stored `1665`, but `CC 1000.md` line 694 shows 1665 is actually 渡's rank — 矩 itself is line 695, rank `1666`. Corrected.

**Investigated a potential `graphemic_classification` bug, concluded it was already correct**: en.Wiktionary's glyph-origin prose calls 矩 a "Pictogram" and says 巨 is "a later simplification, not the original structure" — worded ambiguously enough to look like another 尼/曰-style type-error at first read. But checking the phonetic parent [[characters/巨|巨]]'s own already-perfected page revealed this exact tension is already documented there in detail: Shuowen treats 巨 as its own pictogram, while a 2021 scholarly source (Chen) argues 矩 is the etymologically prior form with the person-radical later dropped — an unresolved scholarly debate, not a settled reclassification. Since the vault's own established page for 巨 already treats the modern structural analysis (矢-corrupted-from-大 + phonetic 巨) as the operative one, left `graphemic_classification: 巨` unchanged and added a concise note pointing to 巨's fuller discussion rather than duplicating it.

`vietnamese: củ` and the alias 榘 (a true derived variant sharing 矩's exact OC reading, not an independent character) both reconfirmed correct. **`pos` gap filled**: blank → `名詞`, matching the citing self-named stand-in word [[矩]]. Linked the semantic component 矢 via its Radical page ([[Radical 111|矢]]) per the radical-linking rule.

Fixed a `../` path bug in the disambiguation callout and rebuilt the malformed Notes/Words structure into the standard format. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 䋇 (char) (7518; 749 characters remaining).

### 2026-08-16, iteration 1756 — [[characters/䋇 (char)|䋇]]

**`mc_id` off-by-one found and fixed**: stored `2499`, but `CC 2000.md` line 520 shows 2499 is actually 邕's rank — 繹 itself (the traditional form this rank is indexed under) is line 521, rank `2500`. Corrected.

**`graphemic_classification` investigated and left unchanged after a nuanced check**: en.Wiktionary and zh.Wiktionary both name **睪**, not 尺, as the traditional form 繹's true phonetic component — initially looked like a clear-cut error matching the 尼/曰 pattern. But 䋇 is itself the *extended shinjitai* simplification of 繹, and its actual glyph literally contains 尺 (not 睪) as a graphic substitute; the pre-existing Notes bullet had already researched and cited three OC readings for 尺 including *laːɡ — an exact match to 繹's own OC value, suggesting 尺 carries a genuine (if obscure) ancient phonetic loan value of its own rather than being an arbitrary shape-only substitution. Since the character being perfected is the glyph that actually contains 尺, and no vault page exists for 睪 (which doesn't even appear in this glyph), left `graphemic_classification: 尺` unchanged and rewrote the Notes bullet to explain the shinjitai-substitution relationship explicitly rather than leaving it ambiguous.

**`vietnamese` fixed on two axes at once**: the stored value was a single malformed YAML string (`"gịt, dịch, dịt"` as one list item rather than three) AND contaminated — hvdic's genuine "Âm Hán Việt:" line gives only `dịch`, with `dịt`/`gịt` being Nôm-only. Fixed the YAML structure and reduced to the single genuine reading in one edit.

Fixed a `../` path bug in the disambiguation callout. Rebuilt the malformed Notes/Words structure into the standard format. `pos: 事詞` was already correctly filled. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 涜 (7519; 748 characters remaining).

### 2026-08-16, iteration 1757 — [[characters/涜|涜]]

**`mc_id` off-by-one found and fixed**: stored `1875`, but `CC 1000.md` line 912 shows 1875 is actually 酎's rank — 瀆 itself (the traditional-form rank this indexes under) is line 913, rank `1876`. Corrected.

**`graphemic_classification` investigated and confirmed already correct, with the same shinjitai-substitution pattern seen on 䋇 last iteration**: the field stores `𧶠`, en.Wiktionary's own entry for the traditional form 瀆 explicitly names 𧶠 (not 賣/売) as the true phonetic — matching the stored field exactly. The Notes bullet's prose describing "[氵] + [売]" isn't a contradiction; it's describing what's visually present in *this* shinjitai glyph (賣→売 is a standard simplification substitution, same pattern as 睪→尺 on 䋇), while the field correctly records the deeper phonetic root. Rewrote the Notes bullet to make this relationship explicit rather than leaving it as a bare, unexplained pair of links. Confirmed no vault page exists for 売 that should receive 涜 as a Derived Characters consequence-fix, since 売 is not what the `graphemic_classification` field actually names.

**`vietnamese` gap filled**: stored `độc` alone; hvdic's genuine "Âm Hán Việt:" line gives both `đậu` and `độc` — added the missing `đậu`.

Fixed a warning-callout typo ("on it's own" → "on its own") and a `../` path bug in its link. Rebuilt the malformed Notes/Words structure into the standard format. `pos: 名詞` was already correctly filled. Stamped `date-last-perfect: 2026-08-16`.

Next never-perfected character by `danayo_id`: 圄 (7520; 747 characters remaining).
