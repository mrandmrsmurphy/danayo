# Character Perfecting (Solo Loop)

A self-paced `/loop` sweep perfecting one character file per iteration against [[AIOS/checklists/checklist_characters.md|checklist_characters.md]]. Started 2026-07-22. **Deliberately a separate log from [[Loop Work.md]]**, at the user's request — don't merge the two, and don't treat "last done" pointers in one as authoritative for the other.

**Ordering**: continuing the `danayo_id`-ascending thread where [[Loop Work.md]] left off (last done there: 気, id 81). Checked ids 82–86: 年 (82) and 肉 (83) were already perfected (2026-07-16, in a session not logged back to Loop Work.md) — skipped. 84 (多) was next never-perfected id.

**Policy for this loop**: skip any character whose fix would require a judgment call this loop isn't confident resolving alone (e.g. an unresolved etymology dispute, a `stand_in`/alias ambiguity) — move to the next `danayo_id` instead of guessing or asking. Any content removed from a page is recorded here explicitly.

## Log

### 2026-07-22, iteration 1 — [[characters/多 (char)|多]]

Next never-perfected character by `danayo_id` (84). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already complete and correct — `graphemic_classification: 會意` matched the page's own already-written 会意 bullet, `stand_in: 多` correct (word file exists), `aliases:` correctly left blank (empty, matching the vault's established convention for "no aliases" rather than an empty-list `[]`).

**Body defects found**: `## Words` was sitting *before* `## Notes` (wrong section order); `## Notes` had only bullet 1 (graphemic) — bullets 2–4 (SKIP/Stroke, MC rank, Levels) were entirely missing; `### Derived Characters` was H3 instead of H2; the two CC-initial/final links (`[[Lookup/CC/initials/聲 端]]`, `[[Lookup/CC/finals/韻 歌]]`) were floating on their own lines inside Derived Characters instead of embedded in the MC-rank bullet; no `## Chengyu` section existed despite 2 real hits.

**Content removed**: a bullet under the old (mis-leveled) Derived Characters reading "abbreviation for 'gadolinium': [[加多金]] ... uses 多, the word's second character, since 加 is already taken as the abbreviation for californium" — this described a real word ([[加多金]], confirmed existing), not an actual derived *character*, so it didn't belong in that section. Relocated (not deleted) into `## Words` with the gloss "gadolinium," keeping the phonosemantic-coinage note in shortened form.

**Words cross-check** (18 total ground-truth hits via `characters:` field grep, tolerant of quoted entries): only 2 were previously listed (加多, 多様); added 16 more — the stand-in 多 itself, the full correlative-degree paradigm (多少, 此多, 其多, 彼多, 何多, 皆多, 某多, 毎多 — all already existed as word files, none were listed on the character page at all), 繁多, 衆多, 多彩, 多辺, and 加多金. Also corrected 加多's gloss from a paraphrase ("to add more; to increase") to the word file's actual verbatim stored `english` field ("to add; to augment; to increase").

**Chengyu section built from scratch** (2 hits): 多召少選 ("many are called, few are chosen," Bible-derived) and 少即是多 ("less is more," attributed to Mies van der Rohe) — neither had been backlinked from 多's page before.

**Flagged, not fixed — recurring `注音` mismatch pattern, same class documented elsewhere in [[AIOS/projects.md]] (恩/慣/調·酒)**: three existing word/chengyu files spell 多's contribution as `ㄉㄚ` instead of 多's own stored `ㄉㄜ` — `words/多彩.md` (注音 `ㄉㄚㄑㄚㄧ`), `chengyu/多召少選.md` (`ㄉㄚ...`), and `chengyu/少即是多.md` (`...ㄉㄚ`). Used each file's actual stored 注音 verbatim in the ruby markup per the checklist's byte-for-byte rule, rather than "correcting" it — fixing the downstream files is out of scope for a character-page perfection pass and needs its own dedicated look (worth checking whether this is one systematic bug, given three independent hits with the identical shape).

**Derived Characters** (3 hits via `graphemic_classification: 多`, all pre-existing frontmatter values, not re-litigated here): 爹 (already independently perfected, its own page already documents phonetic 多), 移 (Shuowen's traditional 从禾多聲 analysis, despite a large synchronic MC divergence — same "trust the attested classical analysis over surface MC mismatch" pattern as 石/生's phonetic families), 宜 (Shuowen: 从宀，多省聲, an abbreviated-phonetic reading — modern pictographic reinterpretations exist but the vault's own stored classification already commits to this traditional account, left as-is). None of the three were previously listed on 多's own page.

**Graphemic bullet**: rewrote to name the actual doubled component (肉 "meat," corrupted in bronze script into 夕) and linked 夕 to its Radical page (`[[Radical 036|夕]]`, since 多's own `radical:` field is 夕) — the old bullet described this correctly in prose but named neither.

Next: continuing ascending by `danayo_id` — 87 (糸), 88 (回), 91 (会), 92 (米), ... (89, 90 already have a `date-last-perfect` stamp on inspection).

### 2026-07-22, iteration 2 — [[characters/糸|糸]]

Next never-perfected character by `danayo_id` (87; checked 89/次 and 90/先 too — both already stamped, 2026-07-21 and 2026-07-10 respectively, in sessions not logged to this file). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter bugs fixed**: `japanese_native` was malformed YAML — a bare scalar `いと` immediately followed by a stray `- いと` list item (same defect class as [[characters/野獣|野獣]]'s fix, noted in [[Loop Work.md]]) — collapsed to a proper single-item list. `vietnamese` was a single comma-joined string (`"tơ, tưa, ty, ti"`) instead of a real YAML list — reformatted into four separate list items, preserving all four existing values as-is (no new content invented, just re-shaped).

**Content removed**: none — no incorrect or contradicted data on this page, just formatting and missing structure.

**Body defects found**: `## Notes` had only a bare "Components: [[幺]], [[小]]" line (non-canonical, no real classification prose) plus two floating CC-initial/final links on their own lines and a bare `[[糸線]] "silk thread"` bullet with no `## Words` heading at all — no SKIP/Stroke/MC/Levels bullets existed. Rewrote the graphemic bullet as a proper 象形 entry (checked against the character's own already-correct `graphemic_classification: 象形` — 糸 depicts a skein of twisted silk thread with the two ends knotted, not two components combining, so the old "Components: 幺, 小" text was describing surface visual resemblance, not real etymology; dropped rather than carried forward) and linked the radical (`[[Radical 120|糸]]`, since 糸's own `radical:` field is itself). Added the missing SKIP/Stroke/MC/Levels bullets and moved the sole Words entry into a proper `## Words` heading.

**Words cross-check**: only one real hit vault-wide (`stand_in: 糸線`, confirmed via `characters:`-field grep across all of `words/`) — already present, just needed the heading and ruby (`ㄙㄚㄙ⼶ㄋ`, pulled from `words/糸線.md`'s own stored `注音`). No chengyu hits, no `graphemic_classification: 糸` hits (no Derived Characters section needed).

**Verified, not touched**: `mc_id: 1392` matches `lookup/CC/CC 1000.md` line "1392. 絲" exactly (絲 is 糸's own listed traditional-form alias, not a different character — same-character variant, not a market/city-style false match). `aliases: [絲, 丝]` left as-is, plausible and unverified-but-not-contradicted.

Next: 88 (回), 91 (会), 92 (米), 93 (耳), 94 (地), continuing ascending by `danayo_id`.

### 2026-07-22, iteration 3 — [[characters/回 (char)|回]]

Next never-perfected character by `danayo_id` (88). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: blank `pos: ""` → `事詞`. Reasoning: Dan'a'yo's own closed classifier set ([[grammar/文法 - 97品詞]]) already assigns the "turns/repeats" counter role to 番, not 回, so 回's own gloss "turns" doesn't make it a classifier — its actual corpus role is verbal/eventive (回答, 回復, 回転, 回収, 挽回 are all action compounds), so 事詞 fits its real behavior rather than its bare gloss.

**Content removed**: none — no wrong or contradicted data, just misplaced/missing structure.

**Body defects found, the messiest page this loop has hit so far**: only one Notes bullet existed (a terse graphemic aside, no SKIP/Stroke/MC/Levels bullets); `## Chengyu` had the real chengyu hit (起死回生) but with no gloss, followed immediately by two floating CC-initial/final links, and then — the real structural bug — **six genuine Words entries were sitting under the `## Chengyu` heading** (回教徒, 回紇, 回答, 回教, 回復, 回収), none of which are chengyu at all. Moved all six into `## Words` where they belong. Several existing Words entries were also malformed: `回路` used a markdown link with a bare-dash gloss and a trailing space instead of ruby+quoted-gloss format; `迂回`, `回転`, `回廊` were bare `[[link]]` with no ruby or gloss at all.

**Words cross-check** (18 total ground-truth hits including the stand-in itself): 14 were already present in some form (several needing ruby/gloss fixes as above); 4 were missing outright — 回帰, 回族, 回生, 挽回 — added, all rubies/glosses pulled from each word's own stored `注音`/`english` fields.

**Chengyu**: 起死回生 already linked but glossless — first drafted a paraphrased gloss from general knowledge ("bring back to life; save from a desperate situation") before catching myself and checking the chengyu file's actual stored `english` field ("revival from the point of death") — corrected before finalizing, same near-miss class documented repeatedly in [[Loop Work.md]].

**Derived Characters** (1 hit via `graphemic_classification: 回`): 徊 ("loiter," as in 徘徊) — exact `注音` match (ㄏㄛㄧ both), a clean phonetic pair, added.

**Graphemic bullet**: rewrote from a two-word aside ("rotation (originally a spiral)") into a full sentence describing the whirlpool/spiraling-water pictograph and its oracle-bone-to-modern squaring-off, matching the checklist's 象形 template.

**Incidental fix**: `words/挽回.md`'s `english` field had a typo, "retreive" → "retrieve."

Next: 91 (会), 92 (米), 93 (耳), 94 (地), continuing ascending by `danayo_id` (89/次 and 90/先 already stamped from an earlier, unlogged session).

### 2026-07-22, iteration 4 — [[characters/会 (char)|会]]

Next never-perfected character by `danayo_id` (91). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: blank `pos:` (no value at all) → `事詞`, matching its real behavior as an action/eventive root across its compounds (会議, 会話, 会社 etc. all build on a "to meet/gather" action sense). `graphemic_classification: 會意` already correct — kept.

**Content removed**: none.

**Body defects found**: `# Notes` was the wrong heading level (H1 instead of H2) and had no real graphemic-classification prose at all — just two floating CC-initial/final links immediately followed by 8 Words entries dumped directly under it, no `## Words` heading anywhere on the page. Several of those 8 entries were bare `[[link]] "gloss,with,no,spaces"` (comma-run glosses, no ruby) rather than proper ruby+quoted-gloss format.

**Words cross-check** (13 total ground-truth hits including the stand-in): 7 already present needed ruby/gloss reformatting; 4 were missing outright — 協会, 教会, 社会, 社会主義 — added, all rubies/glosses from each word's own stored fields. Added the stand-in 会 itself as the first entry (had not been listed).

**Chengyu built from scratch** (1 hit): 一期一会, ruby+gloss pulled verbatim from the chengyu's own stored `注音`/`english` fields.

**Graphemic bullet rewritten from nothing**: 会意 of 亼 ("to converge") over an abbreviated 曾 (a tiered steamer, 曰 omitted) — a lid fitting its vessel, hence "to meet, to join." Neither 亼 nor 曾 has a character page in this vault, so described in prose without a wikilink (same precedent as 気/气, 左/𠂇, 卑/𠂇 in [[Loop Work.md]]). Noted 会 is the Jōyō-simplification of 會, already in the page's own `aliases` — did not link `[[會]]` since no such page exists.

**Derived Characters** (1 hit via `graphemic_classification: 会`): 桧 ("cypress," `guì`/ㄍ⺢ㄧ) — a real, if non-obvious, phonetic pairing: 桧/檜's traditional 形声 analysis derives from 會's *other* Mandarin reading (kuài, as in 会計 "accounting"), not the huì-sense this vault's own Dan'a'yo reading was built from — same "genuine attested relationship despite this vault's own single-sense MC transcription not matching" pattern documented for 母/毎 and 石's phonetic family. Included, not excluded.

Next: 92 (米), 93 (耳), 94 (地), 95 (有), continuing ascending by `danayo_id`.

### 2026-07-22, iteration 5 — [[characters/米 (char)|米]]

Next never-perfected character by `danayo_id` (92). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: blank `pos: ""` → `名詞` (a concrete noun, "rice"). `graphemic_classification: 象形` already correct — matches a straightforward, uncontested pictograph.

**Content removed**: none.

**Body defects found**: `# Notes` was the wrong heading level and held no actual content — it was immediately followed by `## Words` with no Notes bullets at all. Two floating CC-initial/final links sat in the middle of the Words list rather than embedded in an MC-rank bullet (which didn't exist). No SKIP/Stroke/Levels bullets existed either.

**Words cross-check** (7 total ground-truth hits): 3 already listed (one, 玄米, as a bare dash-gloss instead of ruby format); 4 missing — 米飯, 玄米茶, 千米, 毫米 — added, all rubies/glosses from each word's own stored fields. Added the stand-in 米 itself, which hadn't been listed. No chengyu hits.

**Graphemic bullet written from scratch**: standard 象形 template — scattered grains of husked rice around a central cross, following the checklist's List-of-象形 opening format.

**Derived Characters** (1 hit via `graphemic_classification: 米`): 迷 ("be lost; be confused") — exact `注音` match (ㄇㄝㄧ both), a clean phonetic pair, added.

Next: 93 (耳), 94 (地), 95 (有), 96 (当), continuing ascending by `danayo_id`.

### 2026-07-22, iteration 6 — [[characters/耳 (char)|耳]]

Next never-perfected character by `danayo_id` (93). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter fixed**: `japanese_native` had the same malformed-YAML shape as [[characters/糸|糸]] two iterations ago (bare scalar `みみ` plus a stray duplicate `- みみ` list item) — collapsed to a proper single-item list. `pos: 名詞` and `graphemic_classification: 象形` were already correct.

**Content removed**: none.

**Body defects found**: only one Notes bullet existed (terse, "an ear"); no SKIP/Stroke/MC/Levels bullets. Two floating CC-initial/final links sat inside the Words list rather than embedded in an MC bullet. Several Words entries were bare `[[link]] "gloss"` with no ruby (耳根, 耳朶, 耳目), and one (巻耳) had ruby but no gloss.

**Words cross-check** (8 total ground-truth hits including the stand-in): 5 already present in some form, needing ruby/gloss fixes; 3 missing — the stand-in 耳 itself, 中耳, 日耳曼 — added, all fields from each word's own stored `注音`/`english`.

**Chengyu built from scratch** (1 hit): 愛主耳錐 (Bible-origin), ruby+gloss from its own stored fields.

**Derived Characters — 3 included, 1 deliberately excluded and flagged instead of decided**: `graphemic_classification: 耳` hits 4 characters (恥, 茸, 餌, 摂). Verified 恥 (心+耳, OC *n̥ʰɯːʔ vs *nɯʔ, textbook match), 茸 (艸+耳, shared nasal-initial family, standard Shuowen 从艸耳聲), and 餌 (食+耳, identical Mandarin/MC to 耳 itself) as genuine, well-documented phonetic derivatives — all three added. **`characters/摂 (char).md` excluded, not silently fixed**: its real traditional phonetic component is 聶 ("whisper," itself built from three 耳 but with no character page of its own in this vault, so unlinkable even if used), not 耳 directly — 摂's own stored MC (`n`+`ep`) tracks 聶's reading family, not 耳's (`ȵ`+`ɨ`), and its Mandarin `shè` is unrelated to `ěr`. This looks like the same "wrong-character-named-as-phonetic" error class as [[千]]'s old `遷`-vs-`人` bug, but fixing another character's own frontmatter is out of scope for perfecting 耳's page — left 摂's file untouched and excluded it from 耳's Derived Characters rather than guessing either way. Worth a dedicated look in a future iteration when 摂 itself comes up by `danayo_id`.

**Graphemic bullet**: expanded from a two-word stub ("an ear") into a full sentence per the 象形 template.

Next: 94 (地), 95 (有), 96 (当), 97 (行), continuing ascending by `danayo_id`.

### 2026-07-22, iteration 7 — [[characters/地 (char)|地]]

Next never-perfected character by `danayo_id` (94), and the largest page this loop has hit so far (33 words, 7 chengyu, 5 derived characters). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already complete and correct (`pos: 名詞`, `graphemic_classification: 也` matching the page's own already-written 形声 bullet).

**Content removed**: a literal duplicate — the graphemic bullet existed twice back to back (a terse first copy, then a fuller second copy with the same OC reconstruction plus extra historical-form detail). Merged into the single fuller version; nothing substantive lost, just the redundant terse copy dropped.

**Body defects found**: `## Chengyu` was sitting before `## Words` (wrong section order); two floating CC-initial/final links sat after the Words list instead of embedded in an MC bullet (which didn't exist); no SKIP/Stroke/Levels bullets existed; most Words entries were bare `[[link]] - gloss` (dash instead of quoted gloss, no ruby); one Chengyu entry (塩地光世) had no gloss at all.

**Words cross-check** (33 total ground-truth hits including the stand-in, the largest single count this loop has done): 22 already listed in some form (all reformatted to ruby+quoted-gloss); 11 missing outright — 地域, 地理, 地理学, 地下道, 地平線, 天地, 山地, 陸地, 地龍, 天神地祇, and the stand-in 地 itself — added, all fields pulled from each word's own stored `注音`/`english`. Note: `窪地` was on the page already but doesn't turn up in a plain characters-field-list grep (its `characters:` frontmatter is written as an inline array, `[窪, "地 (char)"]`, not a block list) — worth remembering as a ground-truth-search blind spot for future iterations on other characters, same lesson as [[Loop Work.md]]'s note about the inline-array form on other pages.

**Chengyu cross-check** (7 total): 4 already present (塩地光世 needed its gloss added); 3 missing — 乳蜜流地, 天圓地方, 詛地哀食 — added, all Bible/classical-origin, fields from their own stored records.

**Derived Characters** (5 hits via `graphemic_classification: 也`, excluding 地 itself): 他, 池, 馳, 弛, 施 — all members of the well-known, uncontroversial 也-phonetic family (yě → tā/chí/chí/chí/shī), no individual verification needed beyond confirming each hit was real.

Next: 95 (有), 96 (当), 97 (行), 98 (両), continuing ascending by `danayo_id`.

### 2026-07-22, iteration 8 — [[characters/有 (char)|有]]

Next never-perfected character by `danayo_id` (95). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: blank `pos: ""` → `系詞` (Copula) — confident call, not a guess: [[grammar/文法 - 97品詞]] explicitly lists 有 ("to have") as one of the six closed-class copula words (是/非/有/無/在/莫), so this is the one pos value with direct textual backing rather than inferred from gloss alone.

**Content removed**: none — but a real content *error* was fixed, not just reformatted (see below).

**Real etymology bug found and fixed**: the existing graphemic bullet read "形声: semantic 又 ('meat') + phonetic 肉 (OC \*ɢʷɯs)" — this has the semantic/phonetic roles and glosses backwards. 又 means "hand," not "meat" (肉 means "meat"); and the OC reconstruction `*ɢʷɯs` cited for "phonetic 肉" is actually 又's own OC reading (肉's real OC is an unrelated entering-tone form). The vault's own `graphemic_classification: 又` field was already correct (又 genuinely is 有's phonetic component per Wiktionary — OC \*ɢʷɯʔ vs \*ɢʷɯs, near-identical), it was only the body prose that had the labels swapped. Corrected to: semantic [[Radical 074|月]] ("meat," an old form of 肉, matching 有's own `radical: 月` field) + phonetic 又 ("hand; again") — "grasping meat in the hand" → "to have, to possess." 又 has no character page of its own but is Radical 029; linked as bare `又` text rather than `[[Radical 029|又]]` since — unlike a case where a component visually *is* the radical shape being depicted — 有's own `radical:` field is 月, not 又, so 又 here is just the phonetic, described in prose without forcing a radical link that doesn't match this page's own radical assignment.

**Body defects found**: no SKIP/Stroke/Levels bullets existed; two floating CC-initial/final links sat inside the Words list instead of an MC bullet; one Words entry (希有) used a dash instead of a quoted gloss.

**Words cross-check** (10 total ground-truth hits including the stand-in and one inline-array blind spot): 5 already listed (needing ruby/gloss fixes); 4 missing — 共有, 占有, 固有, 所有 — added. **Second inline-array `characters:` field found this loop** (after [[characters/地 (char)|地]]'s 窪地 last iteration): `words/有机.md` stores `characters: ["有 (char)", 机]`, invisible to a plain-list grep — caught it, added 有机 to the Words list. Worth treating this as a recurring, not incidental, blind spot in ground-truth searches going forward.

**Derived Characters** (4 hits via `graphemic_classification: 又`, excluding 有 itself): 右 (already independently Wiktionary-verified in an earlier iteration per [[Loop Work.md]]), 友, 尤, 馭 — all cluster in the same OC neighborhood as 又/有 itself (\*ɢʷɯ-family), a well-attested phonetic series. Added all four.

**Incidental fix**: `characters/尤.md`'s `english` field had a typo, "particularlly" → "particularly."

Next: 96 (当), 97 (行), 98 (両), 99 (死), continuing ascending by `danayo_id`.

### 2026-07-22, iteration 9 — [[characters/当 (char)|当]]

Next never-perfected character by `danayo_id` (96). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: blank `pos: ""` → `性詞`, matching its adnominal/modal behavior across compounds (当然 "of course," 相当 "considerable," 妥当 "appropriate" all read adjectivally or adverbially rather than as a transitive action). `graphemic_classification: 尚` already correct — confirmed via the standard 形声 analysis (semantic 田 + phonetic 尚).

**Content removed**: a stray empty bullet (`-` with nothing after it) sitting right after a lone, out-of-place Levels-only bullet (`[Korean MS](...)` with no companions) — both replaced by the full four-bullet structure.

**Body defects found**: Notes had only a single bare Levels-link bullet plus the empty stray bullet — no graphemic/SKIP-Stroke/MC content at all. Two floating CC-initial/final links sat inside the Words list instead of an MC bullet. Several Words entries were bare `[[link]] "gloss,with,commas"` instead of ruby+semicolon-joined gloss.

**Graphemic bullet written from scratch**: 形声, semantic [[田]] ("field," matching plots of equal size) + phonetic [[尚 (char)|尚]] — "two fields of equal value facing each other," extended to "correspond to, be equal to, ought." Note: 当's own `radical:` field is 小 (a modern-glyph dictionary classification, not part of the real etymology, same non-forcing treatment as [[characters/会 (char)|会]]'s unrelated 人-radical two iterations ago) — did not link it since it plays no role in the actual derivation.

**Words cross-check** (14 total ground-truth hits including the stand-in): 4 already listed (reformatted); 9 missing — 当然, 当世, 当代, 当年, 当日, 当月, 当週, 当世紀, 不当 — added. **Third inline-array `characters:` blind spot this loop** (after 窪地 and 有机): `words/妥当.md` stores `characters: [妥, "当 (char)"]` — caught via a broader secondary grep (search for the raw glyph anywhere in the file, then confirm via the `characters:` block, rather than relying solely on the strict per-line list pattern) — this is now the third hit of the same shape in three consecutive iterations, confirming it's a systemic, not incidental, gap in a plain-list-only ground-truth search. No chengyu hits.

**Derived Characters** (6 hits via `graphemic_classification: 尚`): 賞, 党, 嘗, 堂, 掌, 常 — a large, standard, uncontroversial 尚-phonetic family, all added without individual dispute.

**Incidental fix**: `words/当代.md`'s `english` field had a typo, "contempory" → "contemporary."

Next: 97 (行), 98 (両), 99 (死), 102 (名), continuing ascending by `danayo_id` (100, 101 were already stamped on inspection).

### 2026-07-22, iteration 10 — [[characters/行 (char)|行]]

Next never-perfected character by `danayo_id` (97) — already had frontmatter and all four Notes bullets in reasonable shape, so this iteration was mostly a Words/Chengyu gap-fill. Stamped `date-last-perfect: 2026-07-22`.

**Content removed**: a stale leftover line, "- Components: [[彳]], [[亍]]," sitting above the real, already-correct 指事 bullet — redundant with (and superseded by) the prose bullet directly below it; neither 彳 nor 亍 has a character page in this vault, so the line wasn't even a resolvable link. Dropped rather than merged, since the real bullet already covers the same "crossroads" etymology in full prose.

**Small format fix**: the graphemic bullet's own link read `[指事](lookup/List%20of%20指事.md)` — display text was the bare label instead of the canonical "List of 指事" used everywhere else in the checklist (see [[characters/本 (char)|本]] for the correct precedent) — corrected the display text without touching the link target.

**False alarm caught before editing anything**: `chengyu/修飾先行.md`'s `characters:` field looked like it was missing `行 (char)` entirely on a first `grep -A3` pass (only showed 修/飾/先) — before "fixing" it, re-read the full field and found a 4th line, `行 (char)`, that the truncated grep had simply cut off. No bug existed; worth remembering not to trust a length-limited grep as proof of an omission, always read the actual full field before editing another file based on it.

**Words cross-check** (25 total ground-truth hits including the stand-in, found via a broader glyph-then-field search after the plain-list grep undercounted): 7 already listed (航行, 行動, 行列, 矮行星, 小行星帯, 行伝, 行政 — the latter three already fine, 行動/行列 needed ruby+quote-gloss fixes); 18 missing — 行 itself, 旅行, 飛行, 銀行, 行事, 通行, 通行証, 進行, 運行, 執行, 施行, 刊行, 随行, 爬行, 五行, 行星, 小行星, 飛行机 — added, all fields from each word's own stored `注音`/`english`.

**Chengyu cross-check** (5 total): 2 already present (令行禁止's gloss corrected from an old paraphrase, "what is commanded is done, what is forbidden is not," to the chengyu file's actual stored `english`, "total command discipline" — same never-paraphrase discipline as [[Loop Work.md]]'s repeated near-miss warnings; 修飾先行 already fine); 3 missing — 言行一致, 諸行無常, 腹行食塵 (the last two Bible/classical-origin) — added.

**Derived Characters** (3 hits via `graphemic_classification: 行`): 桁 ("beam"), 衡 ("weigh; measure"), 荇 ("Limnanthemum nymphoides," a water plant) — a standard, well-attested 行-phonetic family (héng/xíng), all added.

Next: 98 (両), 99 (死), 102 (名), 103 (西), continuing ascending by `danayo_id`.

### 2026-07-22, iteration 11 — skipped [[characters/両 (char)|両]], perfected [[characters/死|死]]

**Skipped 98 (両)**: this page is exactly the case already flagged in [[AIOS/projects.md]] as an unresolved cross-sense conflation — its `cantonese` field and alias list bundle together at least two genuinely distinct senses/characters (両/兩 "two, both," reading loeng5, vs. 両-as-"tael"/currency unit, reading loeng2; plus 魎/魉 "demon," a different word entirely, folded in via a 借代字 note). A prior session explicitly deferred this as "a genuine character-level disambiguation question for a dedicated pass, not something to silently fix by breaking the compounds." Per this loop's standing rule to skip anything questionable or decision-requiring rather than guess, moved on without touching the file.

**Perfected 99 (死) instead.** Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already complete (`pos: 性詞`, `graphemic_classification: 會意` already correct).

**Content removed**: a bare `[[死体]]` Words entry — `words/死体.md` does not exist anywhere in the vault (confirmed by direct file check), so this was a broken link to a word that was never created, not a formatting slip on an existing page. Removed rather than left dangling or invented; 死骸 already covers the same "corpse" concept with a real file.

**Body defects found**: the Notes section held only a single (genuinely useful) grammar/valency note about Classical Chinese direct-object marking vs. Dan'a'yo's postposition 于 requirement — none of the four canonical bullets existed. Kept the valency note as a fifth, trailing bullet rather than discarding real content that doesn't fit the four-bullet template, and built the four canonical bullets in front of it. No `## Chengyu` section existed despite 2 real hits.

**Graphemic bullet written from scratch**: 会意 of [[Radical 078|歹]] ("death; remains of stripped bone") and 人 ("person," kneeling/bowing) — a mourner beside the dead.

**Words cross-check** (8 total ground-truth hits): 4 already listed (needing ruby/gloss fixes, plus the broken 死体 entry removed); 4 missing — 生死, 起死, 死亡率, 死亡人数 — added, all from stored fields. `生死` was found only via the broader glyph-then-field search, not the plain-list grep — a fourth instance of the inline-array blind spot this loop keeps running into.

**Chengyu built from scratch** (2 hits): 起死回生 (ruby/gloss reused from [[characters/回 (char)|回]]'s own already-perfected entry) and 剣生剣死 — first drafted both the ruby and gloss for the latter from memory/inference before checking the actual stored `注音`/`english` fields and correcting both; caught before finalizing, same near-miss class flagged repeatedly in [[Loop Work.md]]. No `graphemic_classification: 死` hits — no Derived Characters section applies.

Next: 102 (名), 103 (西), 104 (全), 105 (灯), continuing ascending by `danayo_id` (98/両 left unstamped, skipped per above).

### 2026-07-22, iteration 12 — [[characters/名 (char)|名]]

Next never-perfected character by `danayo_id` (102; 100/虫 and 101/向 already stamped on inspection). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: blank `pos: ""` → `名詞`. `graphemic_classification: 會意` already correct.

**Content removed**: none.

**Ground-truth search note**: a first broad grep for "名 anywhere in a file with a characters: field" produced a long list of false positives (今, 卦, 石, 業, 龍, 悪魔, 霊魂, etc.) — all matches were actually hitting the substring "名" inside an unrelated `pos: 名詞`/`品詞: 名詞` line that happened to fall inside the grep's context window, not a real `characters:` entry. Tightened the pattern to require 名 as a standalone list item, bare scalar, or bracket/comma-delimited inline-array element — this is worth remembering as a sharper version of the inline-array lesson from recent iterations: a loose substring search on CJK text can produce false positives just as easily as it can miss real hits.

**Body defects found**: `# Notes` was the wrong heading level and held only two floating CC-initial/final links before jumping straight to unstructured Words entries — no graphemic/SKIP-Stroke/MC/Levels bullets existed at all.

**Graphemic bullet written from scratch**: 会意 of [[Radical 036|夕]] ("evening, dusk") and [[Radical 030|口]] ("mouth") — calling out one's name in the dark. Both components are genuine Kangxi radicals (036 and 030) even though only 口 matches 名's own `radical:` field — linked both per the checklist's explicit "any component that is itself a radical" rule, not just the one matching the page's own radical field.

**Words cross-check** (22 total ground-truth hits, precise search): 4 already listed (needing reformatting); 18 missing — added, including a full seven-member polite/honorific-pronoun paradigm (此名/其名/彼名/何名/皆名/某名/毎名) that parallels [[characters/多 (char)|多]]'s quantity-correlative family from earlier this loop (此多/其多/彼多/何多/皆多/某多/毎多) — same X-此/其/彼/何/皆/某/毎 productive pattern, different head character.

**Chengyu built from scratch** (2 hits): 勿妄称名 (Bible) and 義以立名 (単亜語-origin), both ruby/gloss from stored fields.

**Derived Characters** (2 hits via `graphemic_classification: 名`): 酩 ("drunk; intoxicated") and 銘 ("inscription") — both exact `注音` matches (ㄇㄝㄫ), a clean phonetic pair.

Next: 103 (西), 104 (全), 105 (灯), 107 (百), continuing ascending by `danayo_id` (106 already stamped on inspection).

### 2026-07-22, iteration 13 — [[characters/西|西]]

Next never-perfected character by `danayo_id` (103). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: blank `pos: ""` → `名詞`. `graphemic_classification: 象形` already correct, and the existing bullet was already good encyclopedic content (a genuinely disputed etymology, both sides cited) — kept verbatim.

**Content removed**: a literal duplicate — the "abbreviation for seaborgium" note ([[西博金]]) was written out twice, once as a stray Notes bullet 2 and again as a proper Words entry at the bottom. Dropped the Notes-bullet copy, kept the Words entry (same "relocate periodic-table trivia into Words, don't keep it in Notes" pattern as [[characters/多 (char)|多]]'s gadolinium note earlier this loop).

**Body defects found**: no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final links sat inside the Words list; several entries were bare `[[link]] "gloss"` or `[[link]]`-only with no ruby (西班牙, 西端, 西瓜, 西北, 西蔵).

**Words cross-check** (20 total ground-truth hits, using the precise pattern refined last iteration): 9 already listed in some form (reformatted); 8 missing — the stand-in compound 西方 itself, 東西, 西部, 大西洋, 新西蘭, 西班牙語, 馬来西亜, 印度尼西亜 — added, all from stored fields.

**Chengyu built from scratch** (2 hits): 古今東西, 東奔西走 — ruby/gloss from stored fields.

**Derived Characters** (1 hit via `graphemic_classification: 西`): 茜 ("madder," a red dye plant) — exact `注音` match (ㄑㄝㄋ is the Dan'a'yo reading tied to the same MC series), added.

Next: 104 (全), 105 (灯), 107 (百), 109 (早), continuing ascending by `danayo_id` (108 already stamped on inspection).
