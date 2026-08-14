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
