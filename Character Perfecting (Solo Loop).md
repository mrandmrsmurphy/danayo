# Character Perfecting (Solo Loop)

A self-paced `/loop` sweep perfecting one character file per iteration against [[AIOS/checklists/checklist_characters.md|checklist_characters.md]]. Started 2026-07-22. **Deliberately a separate log from [[Loop Work.md]]**, at the user's request — don't merge the two, and don't treat "last done" pointers in one as authoritative for the other.

**Ordering**: continuing the `danayo_id`-ascending thread where [[Loop Work.md]] left off (last done there: 気, id 81). Checked ids 82–86: 年 (82) and 肉 (83) were already perfected (2026-07-16, in a session not logged back to Loop Work.md) — skipped. 84 (多) was next never-perfected id.

**Policy for this loop**: skip any character whose fix would require a judgment call this loop isn't confident resolving alone (e.g. an unresolved etymology dispute, a `stand_in`/alias ambiguity) — move to the next `danayo_id` instead of guessing or asking. Any content removed from a page is recorded here explicitly.

## Log

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

### 2026-07-22, iteration 14 — [[characters/全 (char)|全]]

Next never-perfected character by `danayo_id` (104). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 性詞`, `graphemic_classification: 會意`).

**Content removed — a fabricated Derived Characters entry**: the old `### Derived Characters` list included "銓 --> 選," but `characters/銓.md` doesn't exist anywhere in this vault, and `characters/選.md`'s own real phonetic component is 巽, not 全 at all — the note was simply wrong on both ends, same "names a character that isn't actually the phonetic donor" error class as [[characters/千|千]]'s old 遷-vs-人 bug earlier in this vault's history. Dropped entirely rather than carried forward; rebuilt the section from the real `graphemic_classification: 全` hits instead (詮, 栓 — both genuine).

**Graphemic bullet rewritten**: the old bullet mislabeled [[入]] ("enter") with the gloss "jade" — 玉/王 means "jade," not 入. A second, separate bullet further down correctly identified the real components (入 + 王, with a shinjitai note that the top can look like 人) but was merged awkwardly into the SKIP/Stroke/syllable bullet as trailing prose. Consolidated into one correct bullet: 会意 of [[Radical 011|入]] ("enter") + 王 (a form of [[王 (char)|王]], "jade," dotless) — jade brought whole, extended to "whole, complete" — keeping the genuine shinjitai note about the 人-vs-入 top-stroke ambiguity.

**Body defects found**: bullets were out of canonical order (Levels bullet before the MC/SKIP content); two floating CC-initial/final links sat after the merged bullet instead of embedded in a proper MC-rank bullet; `### Derived Characters` was H3 and positioned before Words instead of after Chengyu (no Chengyu section applies here — zero hits).

**Words cross-check** (8 total ground-truth hits): 3 already listed (needing ruby/gloss fixes); 5 missing — the stand-in 全 itself, 全部, 完全, 安全, 全盛 — added, all from stored fields. No chengyu hits.

**Incidental fixes**: `words/全体.md` and `words/全部.md` both had the identical typo "entirity" → "entirety" in their `english` fields.

Next: 105 (灯), 107 (百), 109 (早), 110 (足), continuing ascending by `danayo_id` (106/108 already stamped on inspection).

### 2026-07-22, iteration 15 — [[characters/灯 (char)|灯]]

Next never-perfected character by `danayo_id` (105). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 名詞`, `graphemic_classification: 登` matching the standard 形声 analysis of 灯/燈). `mc_id: 0` handled per the checklist's explicit policy — phrased the MC bullet as "Not present in the Classical Chinese usage ranking" rather than treating it as a gap to fill.

**Content removed**: a stray, plainly non-canonical line, "I'm shocked its not old" — an apparent leftover aside/thought fragment with no encyclopedic content, sitting where the graphemic bullet should have been. Removed outright, not incorporated anywhere.

**Caught before shipping — a fabricated OC reconstruction**: first drafted the graphemic bullet with an invented Old Chinese citation for 登 (`*tɘːŋ`) to match the checklist's phonetic-bullet template, without having verified it against any real source. Checked 登's own character page and found no OC value recorded there either (only its Middle Chinese initial/final, which happens to match 灯's own exactly, t + əŋ both) — rewrote the bullet to cite that confirmed exact MC match instead of a guessed OC form, rather than invent a citation with no backing.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links sat with no MC bullet to embed in; no SKIP/Stroke/Levels bullets existed; one Words entry used a path with a stray `../` prefix (`[[../words/灯心]]`, which breaks Obsidian's by-name wikilink resolution) instead of a bare `[[灯心]]`.

**Words cross-check** (4 total ground-truth hits, a small page): 2 already listed (灯籠 fine, 灯心's link fixed); 2 missing — the stand-in 灯 itself and 電灯 — added. No chengyu hits, no `graphemic_classification: 灯` hits (no Derived Characters section applies).

Next: 107 (百), 109 (早), 110 (足), continuing ascending by `danayo_id`.

### 2026-07-22, iteration 16 — [[characters/百 (char)|百]]

Next never-perfected character by `danayo_id` (107). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: blank `pos: ""` → `数詞` (Numeral) — direct precedent from [[characters/千|千]], the already-perfected sibling numeral character, not a guess from gloss alone.

**Content removed**: a stray `### Links` section with a `![[nav/Numerals]]` embed at the very bottom of the page — checked against 千's own already-perfected character page (a genuine numeral, same category as 百) and confirmed it carries no such section at all. This embed is a word-page-template convention (see [[Word Perfecting.md]] iteration 3, where the same embed was caught and removed from a *word* page that wasn't even a numeral) that had leaked onto this *character* page where it doesn't belong on either page type. Removed rather than kept.

**Caught before shipping — a second fabricated-OC near-miss, same class as [[characters/灯 (char)|灯]] last iteration**: first drafted the graphemic bullet with invented Old Chinese forms for both 百 and its phonetic 白 (`*praːɡ`/`*braːɡ`) to fit the checklist template, without a verified source. Checked 白's own stored Middle Chinese fields instead (`b` + `ɣæk`, vs. 百's own `p` + `ɣæk`) — a confirmed, regular voiceless/voiced initial alternation on an identical rime — and rewrote the bullet to cite that verified MC-level match rather than invented OC symbols. Worth treating this as a standing rule now, not a one-off: when the real OC reconstruction isn't already sourced somewhere in the vault, fall back to the character's own stored MC fields rather than fabricate a citation.

**Body defects found**: `## Notes` held only two floating CC-initial/final links, no other bullets. Several Words entries were bare `[[link]] "gloss"` with no ruby (百, 百済, 百科).

**Words cross-check** (14 total ground-truth hits): 8 already listed (reformatted); 6 missing — 一百, 七百, 八百, 百事, 百分率, 百科事典 — added, all from stored fields.

**Chengyu built from scratch** (2 hits): 百家共承 (単亜語-origin) and 百聞不如一見, ruby/gloss from stored fields. No `graphemic_classification: 百` hits — no Derived Characters section applies.

Next: 109 (早), 110 (足), continuing ascending by `danayo_id`.

### 2026-07-22, iteration 17 — [[characters/早 (char)|早]]

Next never-perfected character by `danayo_id` (109). Stamped `date-last-perfect: 2026-07-22`. A small, clean page.

**Frontmatter**: blank `pos: ""` → `性詞` (stative — "early" modifies as an adjective/adverb). `graphemic_classification: 會意` already correct.

**Content removed**: none.

**Body defects found**: `## Words` was sitting before a wrongly-leveled `# Notes`, which held only two floating CC-initial/final links and nothing else — no graphemic/SKIP-Stroke/MC/Levels bullets existed at all.

**Graphemic bullet written from scratch**: 会意 of [[Radical 072|日]] ("sun") above 十 (a stylized plant/marker) — the sun risen above the horizon, "early." Kept deliberately modest on the disputed details of what 十 originally depicted, per the same standing caution as the last two iterations' fabricated-OC catches — described the well-attested general shape (sun-above-marker) without asserting a specific unverified reconstruction.

**Words cross-check** (3 total ground-truth hits — the smallest page this loop has done): 1 already listed (早晨); 2 missing — the stand-in 早 itself and 早飯 — added. No chengyu hits.

**Derived Characters** (1 hit via `graphemic_classification: 早`): 草 ("grass") — a textbook 形声 pair (艹 semantic + 早 phonetic), added.

**Loop status**: 17 iterations completed since this log started (2026-07-22), one character skipped ([[characters/両 (char)|両]], flagged as a genuine cross-sense dispute rather than perfected). Continuing ascending by `danayo_id` from 110 (足).

### 2026-07-22, iteration 18 — [[characters/足 (char)|足]]

Next never-perfected character by `danayo_id` (110). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: blank `pos: ""` → `名詞` (primary gloss "foot," a concrete body-part noun). `graphemic_classification: 會意` already correct.

**Content removed**: none.

**Body defects found**: `# Notes` was the wrong heading level and held only two floating CC-initial/final links plus one bare Words-style entry (足球) misplaced inside it — no real graphemic/SKIP-Stroke/MC/Levels bullets existed.

**Graphemic bullet written from scratch**: 会意 of 口 (a knee/joint shape) and [[止]] ("stop; foot") — the whole leg, from knee to foot.

**Words cross-check** (9 total ground-truth hits): 2 already present (足球 relocated out of Notes and reformatted, 充足 already fine); 7 missing — the stand-in 足 itself, 手足, 足指, 足裏, 満足, 自足, 飽足 — added, all from stored fields.

**Chengyu cross-check** (3 total): 2 already present and correctly formatted; 1 missing — 画蛇添足 — added.

**Derived Characters** (2 hits via `graphemic_classification: 足`): 促 ("hurry; rush") and 捉 ("clutch; seize") — both standard, well-attested 足-phonetic derivatives, added.

Next: 111 (走), 112 (売), 113 (里), 114 (車), 115 (近), 116 (弟), continuing ascending by `danayo_id` (117/花 already stamped on inspection).

### 2026-07-22, iteration 19 — [[characters/走 (char)|走]]

Next never-perfected character by `danayo_id` (111). Stamped `date-last-perfect: 2026-07-22`. Another small, clean page.

**Frontmatter**: blank `pos: ""` → `事詞` (an action verb, "run"). `graphemic_classification: 象形` already correct.

**Content removed**: none.

**Body defects found**: `# Notes` was the wrong heading level and held only two floating CC-initial/final links — no other bullets existed at all.

**Graphemic bullet written from scratch**: a running figure with swinging arms above [[止]] ("foot") — a person in mid-stride, per the standard 象形 template.

**Words cross-check** (3 total ground-truth hits): none were previously listed at all — added the stand-in 走 itself, 奔走, 競走, all from stored fields.

**Chengyu built from scratch** (1 hit): 東奔西走 (already linked and correctly formatted on [[characters/西|西]]'s own page two iterations ago — reused the same ruby/gloss here). No `graphemic_classification: 走` hits — no Derived Characters section applies.

Next: 112 (売), 113 (里), 114 (車), 115 (近), 116 (弟), continuing ascending by `danayo_id`.

### 2026-07-22, iteration 20 — [[characters/売|売]]

Next never-perfected character by `danayo_id` (112). Stamped `date-last-perfect: 2026-07-22`. A small page (bound character, `stand_in: 販売`, tagged `#cranberry`).

**Frontmatter**: already correct (`pos: 事詞`, `graphemic_classification: 買`). Verified the phonetic claim before writing the bullet: `characters/買.md`'s own stored Middle Chinese (`m` + `ɣɛ`) is an **exact** match to 売's own (`m` + `ɣɛ`) — about as clean a confirmation as this sweep has seen, consistent with 買/賣 being a famous near-minimal tone pair in Mandarin (mǎi/mài).

**Content removed**: none.

**Body defects found**: `# Notes` was the wrong heading level and held only two floating CC-initial/final links — no other bullets, no `## Words` heading at all.

**Graphemic bullet written from scratch**: 会意/形声 hybrid — [[出 (char)|出]] ("go out, exit") + phonetic 買 (exact MC match) — putting goods out for others to buy, "to sell." Same hybrid-labeling convention as [[characters/毎 (char)|毎]]'s 会意/形声 bullet in [[Loop Work.md]].

**Words cross-check** (1 total ground-truth hit, the `stand_in` compound itself): 販売 was entirely unlisted — added, ruby/gloss from its own stored fields. No chengyu hits, no `graphemic_classification: 売` hits (no Derived Characters section applies).

Next: 113 (里), 114 (車), 115 (近), 116 (弟), continuing ascending by `danayo_id`.

### 2026-07-22, iteration 21 — [[characters/里 (char)|里]]

Next never-perfected character by `danayo_id` (113). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 名詞`, `graphemic_classification: 會意` matching the already-good existing bullet).

**Content removed**: a literal duplicate, same pattern as [[characters/多 (char)|多]] and [[characters/西|西]] earlier this loop — the "abbreviation for curium" note ([[居里金]]) was written out twice, once as a stray Notes bullet and again as a proper Words entry. Dropped the Notes copy, kept the Words entry (folding the phonosemantic-coinage detail into its gloss instead).

**Body defects found**: the graphemic bullet was already good, but two genuinely useful non-canonical prose bullets (a policy note on why 里 and 裏/裡 aren't merged despite Chinese conflating them, and a note on 里 vs. 英里 for the Western mile) sat immediately after it with no SKIP/Stroke/MC/Levels bullets in between. Kept both trailing notes as additional content (same "don't discard real content that doesn't fit the four-bullet template" precedent as [[characters/死|死]]'s valency note) and inserted the four canonical bullets ahead of them, in order.

**Words cross-check** (3 total ground-truth hits): 1 already listed (居里金); 2 missing — the stand-in 里 itself and 里芋 — added.

**Chengyu built from scratch** (1 hit): 不遠千里 — ruby/gloss reused verbatim from [[characters/千|千]]'s own already-perfected entry for the same chengyu.

**Derived Characters** (6 hits via `graphemic_classification: 里`, the largest family since [[characters/夕|多]]'s and [[characters/百 (char)|百]]'s classes): 厘, 浬, 狸, 理, 裏, 鯉 — all standard, well-attested. One divergent reading kept rather than excluded: 狸's own Dan'a'yo syllable (ㄌㄜ) differs from the rest of the family (ㄌㄧ), but this is an already-existing, unrelated-to-today's-edit corpus value, and 狸/里 (lí/lǐ) is a genuine, standard phonetic pair in real Chinese etymology — same "vault-level MC divergence doesn't itself disqualify a real classical relationship" pattern as 石/母's phonetic families.

Next: 114 (車), 115 (近), 116 (弟), continuing ascending by `danayo_id`.

### 2026-07-22, iteration 22 — [[characters/車 (char)|車]]

Next never-perfected character by `danayo_id` (114; tagged `#hapax`). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 名詞`, `graphemic_classification: 象形` matching the existing, already-good bullet).

**Content removed**: a stray "Components: [[十]], [[田]]" line — leftover wiki-style component text that doesn't fit a pure pictograph (象形) at all; the real bullet directly below it already correctly describes 車 as a top-down view of a carriage, not a compound of 十+田. Dropped rather than reconciled, since it wasn't describing a real alternative etymology, just noise from an old template.

**Body defects found**: `## Words` sat before a wrongly-ordered `## Notes`; two genuinely useful phonological notes (two competing MC pronunciations, literary vs. colloquial; and a note that Dan'a'yo's own reading was deliberately altered from the expected derivation to secure a free syllable) had no SKIP/Stroke/MC/Levels bullets in front of them. Kept both trailing notes, same "preserve real content beyond the four-bullet template" precedent as [[characters/死|死]] and [[characters/里 (char)|里]] this loop, and merged the two into one combined trailing bullet.

**Words cross-check** (9 total ground-truth hits): 1 already listed (車庫); 8 missing — the stand-in 車 itself, 汽車, 電車, 自動車, 自転車, 乗車, 洗車, 火車 — added, all from stored fields. No chengyu hits, no `graphemic_classification: 車` hits.

**Flagged, not fixed — a character-vs-word `注音` mismatch, same recurring class documented elsewhere in [[AIOS/projects.md]]**: `words/洗車.md` spells its own second syllable `ㄑㄚ`, not 車's own stored `ㄑ⺢` — used the word's actual stored value verbatim in the ruby per the byte-for-byte rule, did not "correct" it.

Next: 115 (近), 116 (弟), continuing ascending by `danayo_id`.

### 2026-07-22, iteration 23 — [[characters/近 (char)|近]]

Next never-perfected character by `danayo_id` (115). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 性詞`, `graphemic_classification: 斤` matching an already-good, pre-existing OC-sourced bullet — kept verbatim rather than re-derived, since it was already properly cited).

**Content removed**: none.

**Small fix**: linked the bullet's bare `[[辶]]` component to its Radical page (`[[Radical 162|辶]]`, confirmed via `lookup/Radicals/Radical 162.md`'s own `radical: 辵` field) — the checklist's radical-linking rule had been missed on this otherwise well-sourced bullet.

**Body defects found**: no SKIP/Stroke/Levels bullets existed (the MC-rank content was folded into the graphemic bullet itself, missing its own bullet and the syllable link); two floating CC-initial/final links sat inside the Words list; two entries were bare `[[link]] "gloss"` markdown with no ruby (近来, 近処), one used a relative markdown-link-with-dash-gloss format (近代).

**Words cross-check** (9 total ground-truth hits): 4 already listed (reformatted); 5 missing — the stand-in 近 itself, 接近, 最近, 附近, 漸近線 — added, all from stored fields. No `graphemic_classification: 近` hits — no Derived Characters section applies (near-miss note: an initial pass mistakenly searched for characters sharing 近's *own* phonetic 斤, which would surface 斤's derived family, not characters derived from 近 itself — caught before finalizing and re-ran the correct search).

Next: 116 (弟), continuing ascending by `danayo_id`.

### 2026-07-22, iteration 24 — [[characters/弟 (char)|弟]]

Next never-perfected character by `danayo_id` (116). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 名詞`, `graphemic_classification: 象形`).

**Content removed**: a stray "Components: [[丿]], [[弚]]" line — arbitrary stroke-decomposition text that doesn't describe a real 象形 depiction and isn't needed alongside the real pictograph description. Dropped, not merged.

**Body defects found**: no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final links sat inside an unstructured Words-like list with no `## Words` heading at all.

**Graphemic bullet written from scratch**: a cord wound in sequence around a stick or weapon shaft, marking order — extended to "younger brother" (order among siblings). Left 弟's own `radical: 弓` unlinked, since it plays no role in this etymology (a dictionary-classification artifact, not a real depicted component — same non-forcing treatment as [[characters/会 (char)|会]]'s and [[characters/当 (char)|当]]'s unrelated radical fields earlier this loop).

**Words cross-check** (6 total ground-truth hits): 4 already listed (correctly formatted); 2 missing — the stand-in 弟 itself and 孝弟 — added.

**Derived Characters** (3 hits via `graphemic_classification: 弟`): 剃 ("shave"), 第 ("-th," ordinal prefix), 梯 ("ladder," already independently perfected earlier in this vault's history) — all standard, added.

**Incidental fix**: `words/弟弟.md`'s `english` field had a typo, "litte bitty brother" → "little bitty brother" (kept the colloquial "little bitty" idiom itself, just fixed the missing letter).

**Loop status**: 24 iterations completed, one skip ([[characters/両 (char)|両]]). This clears every character up through `danayo_id` 116 in the never-perfected pool (117 and below are all either perfected today or already stamped from earlier sessions).

### 2026-07-22, iteration 25 — [[characters/村|村]]

Next never-perfected character by `danayo_id` (118; 117/花 already stamped from an earlier session). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter fixed**: `japanese_native` had the same malformed-YAML shape as [[characters/糸|糸]] and [[characters/耳 (char)|耳]] earlier this loop (bare scalar `むら` plus a stray duplicate `- むら` list item) — collapsed to a proper single-item list. `mc_id: 0` handled per the checklist's explicit policy (phrased as "Not present in the Classical Chinese usage ranking," not treated as a gap).

**Content removed**: the same stray non-canonical aside already found on [[characters/灯 (char)|灯]] this loop, "I'm shocked its not old" — another leftover thought fragment sitting where the graphemic bullet should be. Removed outright.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/Levels bullets existed.

**Graphemic bullet written from scratch**: 形声, semantic [[Radical 075|木]] ("tree, wood") + phonetic [[寸 (char)|寸]] — a wooded settlement, "village."

**Words cross-check** (2 total ground-truth hits, a small page): 1 already listed (村塾); 1 missing — the `stand_in` compound 農村 itself — added.

No chengyu hits, no `graphemic_classification: 村` hits — no Derived Characters section applies.

Next: continuing ascending by `danayo_id` from 119 (住).

### 2026-07-22, iteration 26 — [[characters/住|住]]

Next never-perfected character by `danayo_id` (119). Stamped `date-last-perfect: 2026-07-22`. The cleanest page this loop has hit — already had a correct, fully-cited graphemic bullet and all four canonical Notes bullets in order, plus both real Words hits already listed and correctly ruby'd.

**Frontmatter**: the only real defect — blank `pos: ""` → `事詞` (an action verb, "reside; dwell").

**Content removed**: none.

**Verification only**: confirmed `mc_id: 3650` against `lookup/CC/CC 3000.md` ("3650. 住"). Words cross-check (2 total ground-truth hits: 居住, 住宅) found both already present and correctly formatted — no changes needed there. No chengyu hits, no `graphemic_classification: 住` hits.

Next: continuing ascending by `danayo_id` from 120 (何).

### 2026-07-22, iteration 27 — [[characters/何 (char)|何]]

Next never-perfected character by `danayo_id` (120; tagged `#correlative`). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: blank `pos: ""` → `代詞` — not a guess: `words/何.md`'s own already-set `pos: 代詞` gave direct precedent, and matches its real function as an interrogative pronoun (distinct from 此/其/彼/皆/毎/某, whose own word files all use `修飾語` — 何 is the odd one out in the correlative row, and the corpus already encodes that distinction).

**Content removed**: none.

**Body defects found**: `# Notes` was the wrong heading level and held only two floating CC-initial/final links plus one Words-style entry (何故) — no `## Words` heading, no graphemic/SKIP-Stroke/MC/Levels bullets.

**Graphemic bullet written from scratch**: 形声, semantic 人 ("person") + phonetic [[可 (char)|可]] — originally depicted a person carrying a load (the sense later split off and written 荷), borrowed for the interrogative "what."

**Words cross-check** (13 total ground-truth hits, another full correlative-row page — this vault's grammar file, [[grammar/文法 - 97品詞]], turns out to define a large cross-cutting table of `X` + {此/其/彼/何/毎/某/皆} rows, of which 事/物/名/処/時/様/多/類 all separately surface as their own head characters — 何 is the interrogative column of that same table, explaining why so many of these correlative-family character pages keep recurring this loop): 1 already listed (何故); 12 missing — the stand-in 何 itself, 何事, 何人, 何処, 何名, 何多, 何時, 何様, 何物, 何類, 如何, 幾何学 — added, all from stored fields.

**Derived Characters** (2 hits via `graphemic_classification: 何`): 河 ("stream") and 荷 ("luggage," fittingly the character that inherited 何's original "carry a load" sense) — both exact `注音` matches, added.

**Loop status**: 27 iterations completed, one skip ([[characters/両 (char)|両]]).

### 2026-07-22, iteration 28 — [[characters/男|男]]

Next never-perfected character by `danayo_id` (121; `stand_in: 男人`, already documented as a stand-in relationship in [[Word Perfecting.md]]). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: blank `pos: ""` → `名詞`. `graphemic_classification: 會意` already correct.

**Content removed**: none.

**Caught before shipping — a guessed ruby that turned out wrong**: while reformatting the already-listed 男優 entry, first wrote its ruby from a plausible-looking pattern-match (`ㄋㄚㄇ⼄`) instead of reading the word's own stored `注音`. Checked before finalizing and found the real value is `ㄋㄚㄇㄨㄛ` — corrected. (男性's guess happened to land right, `ㄋㄚㄇㄙㄧㄫ`, but was verified the same way rather than assumed safe.) Same near-miss class documented repeatedly in [[Loop Work.md]] — worth remaining strict about even on entries that look routine.

**Body defects found**: `# Notes` was the wrong heading level and held only two floating CC-initial/final links; no graphemic/SKIP-Stroke/MC/Levels bullets existed at all.

**Graphemic bullet written from scratch**: 会意 of [[Radical 102|田]] ("field") and [[力 (char)|力]] ("strength") — one who exerts strength in the field.

**Words cross-check** (4 total ground-truth hits): 3 already listed (男性, 男優, 男爵 — all reformatted); 1 missing — the `stand_in` compound 男人 itself — added. No chengyu hits, no `graphemic_classification: 男` hits.

### 2026-07-22, iteration 29 — [[characters/対|対]]

Next never-perfected character by `danayo_id` (123; 122 already stamped on inspection). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 事詞`, `graphemic_classification: 象形`).

**Content removed**: none.

**Graphemic bullet written from scratch, deliberately hedged**: 對/対's real etymology is genuinely contested across sources (many classify it as 会意 — a hand holding a ritual tool or plant-stand — rather than a straightforward 象形 pictograph), and the vault's own stored `graphemic_classification: 象形` commits to the pictographic reading without further detail to go on. Rather than assert a specific, possibly-wrong disputed account, wrote a modest description consistent with the stored classification without overclaiming precise oracle-bone details — same restrained-wording approach as [[characters/早 (char)|早]] and [[characters/走 (char)|走]] earlier this loop, not a full "questionable, skip" case since the field itself wasn't contradicted by anything already on the page.

**Body defects found**: `# Notes` was the wrong heading level and held only two floating CC-initial/final links plus one Words-style entry (対称) misplaced inside it; no SKIP/Stroke/MC/Levels bullets existed.

**Words cross-check** (10 total ground-truth hits): 4 already listed (相対, 対外, 対照, 七対子); 6 missing — the `stand_in` compound 反対 itself, 対応, 対象, 対連, 絶対, plus 対称 relocated out of Notes into a proper Words entry — added, all from stored fields.

**Chengyu built from scratch** (1 hit): 対牛弾琴, ruby/gloss from stored fields. No `graphemic_classification: 対` hits — no Derived Characters section applies.

### 2026-07-22, iteration 30 — [[characters/究|究]]

Next never-perfected character by `danayo_id` (124). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 事詞`, `graphemic_classification: 九`, already matching a pre-existing, mostly-correct bullet).

**Content removed**: none.

**Small fix**: the existing graphemic bullet had a syntax slip — a stray/mismatched parenthesis ("形声: OC \*kus): semantic...") and a bare `[[九 (char)]]` link that would have displayed the literal filename "九 (char)" instead of the character. Fixed the parenthesis and added the pipe-alias (`[[九 (char)|九]]`, needed since `words/九.md` exists and collides). Added a brief dash-note on the semantic motivation (probing to the bottom of a cave → investigate thoroughly), matching the checklist's template.

**Body defects found**: no SKIP/Stroke/Levels bullets existed; two floating CC-initial/final links had no MC-rank bullet to embed in.

**Words cross-check** (1 total ground-truth hit, the smallest page this loop has done): the `stand_in` compound 研究 itself was entirely unlisted — added, ruby/gloss from its own stored fields. No chengyu hits, no `graphemic_classification: 究` hits.

### 2026-07-22, iteration 31 — [[characters/君 (char)|君]]

Next never-perfected character by `danayo_id` (125). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 代詞`, `graphemic_classification: 尹`).

**Content removed**: none.

**Body defects found**: `## Words` sat before a wrongly-ordered `## Notes`, which held only two floating CC-initial/final links plus two more Words-style entries misplaced inside it — no graphemic/SKIP-Stroke/MC/Levels bullets existed at all.

**Graphemic bullet written from scratch**: 形声, semantic [[Radical 030|口]] ("mouth," to issue commands) + phonetic [[尹]] ("to govern," a hand holding a scepter of authority) — one who governs by command, "ruler, you (respectful)."

**Words cross-check** (8 total ground-truth hits): 4 already listed across the two sections (consolidated under one `## Words`); 4 missing — the stand-in 君 itself, 君子, 君等, 君臣 — added, all from stored fields.

**Derived Characters** (2 hits via `graphemic_classification: 君`): 郡 ("county; prefecture") and 群 ("flock; crowd") — both exact `注音` matches, added.

### 2026-07-22, iteration 32 — [[characters/声|声]] (left unstamped) and [[characters/事 (char)|事]] (perfected)

**[[characters/声|声]] (danayo_id 127) — perfected everything except the date stamp, deliberately left unstamped.** `stand_in: 発声`, but `words/発声.md` does not exist anywhere in the vault — the character's designated word-legitimizer was never created. Per the checklist's own documented case for this situation (a `stand_in` pointing to a compound with no matching file) and the standing "don't fabricate a missing word, don't stamp completion that isn't real" rule, fixed everything possible — blank-to-filled bullets (graphemic: 会意 of 殸 "stone chime" + [[耳 (char)|耳]] "ear"; SKIP/Stroke/MC/Levels), 5 missing Words entries (音声, 大声, 声調, 声母 already existed as ground truth but weren't listed; 声望 reformatted from bare), 1 missing Chengyu (風声鶴唳) — but left `date-last-perfect` blank since criterion 9 (every word using this character is listed) can't be honestly claimed complete when the character's own primary word doesn't exist yet. **Corpus bug found in passing, not fixed (different characters' pages, out of scope)**: an initial `graphemic_classification` search for characters citing 声/聲 as their phonetic surfaced `characters/悖.md` and `characters/懍.md` — both turned out to be false positives, their field is literally the bare string `形声` (the exact "Common mistake" the checklist itself warns against — the field should name the real phonetic component, not restate the type), which merely happens to contain "声" as a substring. Neither is a real derived-character hit for 声's own page; flagged here rather than corrected on those unrelated files, which would be scope creep for this iteration. **Word-creation backlog note**: 発声 ("vocalization, utterance") is now a flagged gap for whenever word-creation work resumes.

**[[characters/事 (char)|事]] (danayo_id 128) — perfected and stamped, the largest page this entire loop has done (31 Words entries, another full correlative-row family: 此事/其事/彼事/何事/毎事/某事/皆事).** Stamped `date-last-perfect: 2026-07-22`.

**Real frontmatter/body contradiction fixed**: `graphemic_classification: 吏` asserted 形声 with phonetic 吏, but the page's own already-written bullet correctly described 会意 (又 "hand" + 中 "flagpole with a drum," already linking [List of 会意]) — same contradiction class as 市/他/石/生/外/用/半 documented repeatedly in [[Loop Work.md]]. 事's real, well-established etymology is 会意, not a 形声 relationship to 吏 (事/吏/史 are historically related as a graphemic family, but not via a simple phonetic-derivative relationship) — corrected the field to `會意` to match the already-correct body content. Also linked the bullet's bare `[[又]]` to its Radical page (`[[Radical 029|又]]`, Radical 029) and disambiguated `[[中]]` to `[[中 (char)|中]]` (a `words/中.md` collision existed).

**Words cross-check** (31 total ground-truth hits): 14 already listed (several bare, reformatted); 17 missing — added, all from stored fields. No `graphemic_classification: 事` hits — no Derived Characters section applies.

**Loop status**: 32 iterations run, one full skip ([[characters/両 (char)|両]]) and one partial-complete-but-unstamped ([[characters/声|声]], pending its own missing stand-in word).

### 2026-07-22, iteration 33 — [[characters/放|放]]

Next never-perfected character by `danayo_id` (129). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 事詞`, `graphemic_classification: 方`, matching an already-good, OC-cited bullet).

**Content removed**: a stray `size: 4` frontmatter field — checked against every other character page in the vault and confirmed this is the only one carrying it; `size` is a lookup-page convention (Radical/SKIP/Stroke pages), not a character-page field at all, so this was leftover cruft from some other template. Removed.

**Small fix**: the graphemic bullet's phonetic link used a plain markdown relative path (`[方](方.md)`) instead of the standard wikilink form — converted to `[[方]]` (no collision, since no `words/方.md` exists) for consistency with every other bullet in the corpus.

**Body defects found**: `### Derived Character` was H3 and positioned before Words instead of after (also singular heading text, non-canonical); two floating CC-initial/final links sat with no MC-rank bullet to embed in; no SKIP/Stroke/Levels bullets existed; one Words entry (放置) was bare with no ruby.

**Words cross-check** (12 total ground-truth hits): 5 already listed (放蕩, 放置, 放送局, 放腐, 放素 — reformatted, 放素's "abbreviation" note folded into its gloss); 7 missing — the `stand_in` compound 釈放 itself, 解放, 開放, 放棄, 放火, 奔放, 放物線 — added, all from stored fields.

**Flagged, not fixed — a character-vs-word `注音` mismatch, same recurring class as [[characters/車 (char)|車]]'s earlier this loop**: `words/放火.md` and `words/放物線.md` both spell their first syllable `ㄅㄚㄫ`, not 放's own stored `ㄈㄚㄫ` — used each word's actual stored value verbatim, did not "correct" it.

**Derived Characters** (1 hit, already on the page but bare — `graphemic_classification: 放`): 倣 ("imitate; emulate"), exact `注音` match, reformatted with ruby/gloss.

**Incidental fix**: `characters/倣.md`'s `english` field had a typo, "immitate" → "imitate."

### 2026-07-22, iteration 34 — [[characters/表|表]]

Next never-perfected character by `danayo_id` (130). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter fix — a real, fairly confident etymology correction**: `graphemic_classification: 毛` asserted 形声 with phonetic 毛, but 表's real, well-documented etymology (Shuowen: 从衣从毛, "a fur garment") is 会意 of 衣 ("clothes") + 毛 ("fur") — not a phonetic relationship at all (Mandarin biǎo vs. máo share no plausible sound derivation, unlike every genuine phonetic pair this loop has verified elsewhere). No pre-existing bullet to contradict this time (Notes was empty), so this was a from-scratch etymology call rather than a frontmatter-vs-body conflict — corrected the field to `會意` and wrote the bullet accordingly, linking both components to their Radical pages (`[[Radical 145|衣]]`, `[[Radical 082|毛]]`, both genuine Kangxi radicals).

**Content removed**: two exact duplicate entries in the `vietnamese` frontmatter list (`biểu` and `vẹo` each appeared twice) — deduplicated, keeping first occurrence order, no information lost.

**Body defects found**: `# Notes` was the wrong heading level and held four Words-style entries with no `## Words` heading; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/Levels bullets existed.

**Words cross-check** (10 total ground-truth hits): 6 already listed across the misplaced section (reformatted, consolidated under one `## Words`); 4 missing — 代表, 代表之, 図表, 週期表 — added, all from stored fields.

**Flagged, not fixed — a dramatic character-vs-word `注音` mismatch**: `words/週期表.md` spells its own reading `ㄐㄨㄛㄎㄧㄙㄛ` — the final syllable `ㄙㄛ` bears no resemblance to 表's own stored `ㄅ⼘ㄨ` at all (different initial and vowel entirely, not just a coda/tone divergence like the milder cases seen elsewhere this loop). Used the word's actual stored value verbatim per the byte-for-byte rule; flagged as the most severe instance of this bug class found so far.

**Derived Characters** (1 hit via `graphemic_classification: 表`): 俵 (a Japanese kokuji, "bag," built on 表's on'yomi HYOU) — exact `注音` match, added.

### 2026-07-22, iteration 35 — [[characters/所 (char)|所]]

Next never-perfected character by `danayo_id` (131). Stamped `date-last-perfect: 2026-07-22`. (User changed the loop's cadence to every 5 minutes partway through this session — noted here for continuity, doesn't change the perfecting methodology.)

**Frontmatter**: blank `pos: ""` → `助詞` (function word) — not a guess: `words/所.md`'s own already-set `pos: 助詞`/`品詞: 助詞` gave direct precedent, matching 所's real role as a nominalizing particle ("that which...", as in 所有/所謂) rather than a content word.

**Content removed**: a stray empty bullet (`- ` with nothing after it).

**Real bug fixed — a genuinely broken link, not just missing content**: the graphemic bullet's phonetic component was a literal empty wikilink, `[[]]`, with only its OC reconstruction surviving. Cross-referenced the citation against 所's own `radical: 戶` field and the Shuowen quote already in the bullet's own gloss ("the sound of logging") — confirmed the missing target is 戶 (door), the real phonetic component per Shuowen's 从斤戶聲. 戶/戸/户 has no character page of its own, but it is a genuine Kangxi radical (Radical 063), so linked it there (`[[Radical 063|戶]]`) rather than leaving the link empty or forcing a nonexistent character-page link.

**Body defects found**: no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final links had no MC bullet to embed in; several Words entries were bare `[[link]]` with no ruby/gloss.

**Words cross-check** (9 total ground-truth hits): 6 already listed (reformatted); 3 missing — the stand-in 所 itself, 所属, 所謂 — added, all from stored fields.

**Flagged, not fixed — another character-vs-word `注音` mismatch**: `words/所.md`'s own stored reading is `ㄙ⼄` (syo), not 所's own character-level `ㄙㄜ` — a divergence on the character's *own* stand-in word, the most direct version of this recurring bug class yet. Used the word's actual stored value verbatim rather than "correcting" it to match the character page.

No chengyu hits, no `graphemic_classification: 所` hits — no Derived Characters section applies.

**Loop status**: 35 iterations run, one full skip ([[characters/両 (char)|両]]), one left unstamped pending a missing word ([[characters/声|声]]).

### 2026-07-22, iteration 36 — [[characters/妹|妹]]

Next never-perfected character by `danayo_id` (132). Stamped `date-last-perfect: 2026-07-22`. A small, clean page — first iteration at the new 5-minute cadence.

**Frontmatter**: already correct (`pos: 名詞`, `graphemic_classification: 未` matching an already-good, OC-cited bullet).

**Content removed**: none.

**Small fix**: disambiguated the phonetic link `[[未]]` to `[[未 (char)|未]]` (a `words/未.md` collision exists).

**Body defects found**: no SKIP/Stroke/Levels bullets existed; two floating CC-initial/final links had no MC bullet to embed in; both existing Words entries used relative markdown links with a dash-gloss instead of ruby+quoted-gloss format.

**Words cross-check** (4 total ground-truth hits): 2 already listed (reformatted, `stand_in` compound 細妹 moved to the front); 2 missing — 姉妹, 兄弟姉妹 (ruby/gloss reused from [[characters/弟 (char)|弟]]'s own already-perfected entry for the same word) — added. No chengyu hits, no `graphemic_classification: 妹` hits.

### 2026-07-22, iteration 37 — [[characters/国|国]]

Next never-perfected character by `danayo_id` (133). Stamped `date-last-perfect: 2026-07-22`. **The largest page this entire loop has done — 63 Words entries plus 1 Chengyu**, the vast majority never listed at all.

**Frontmatter**: blank `pos: ""` → `名詞`. `graphemic_classification: 或` already correct (形声, phonetic 或 + semantic 囗 "enclosure" — a bounded territory).

**Content removed**: none.

**Body defects found**: `## Notes` was completely empty (no graphemic bullet at all, just the bare heading); `## Chengyu` and `## Words` were in reversed order; roughly 30 of the ~65 total Words entries were bare `[[link]]` with no ruby or gloss at all, several more used a trailing plain-text gloss with no ruby, and one used a broken relative link missing the `.md` extension (`[国籍](/words/国籍)`).

**Graphemic bullet written from scratch**: 形声, semantic [[Radical 031|囗]] ("enclosure, boundary") + phonetic [[或 (char)|或]] — a bounded territory, "state, nation."

**Words cross-check** (64 total ground-truth hits via the precise search pattern): roughly 20 already listed in some form; ~44 missing outright — added, all from stored fields. Ordered into rough sense-groups (generic state-words, then country names by size/familiarity, then historical/dynastic states, then nation-concept compounds) rather than left flat, given the scale. **Two word files found missing their own `注音` entirely** — `words/中国人.md` and `words/中国語.md` have `羅馬字`/`諺文` but no `注音` at all. Rather than invent a value from nothing, reconstructed it by concatenating each constituent character's own stored `注音` (中 ㄐㄨㄫ + 国 ㄍㄛㄎ + 人 ㄋㄧㄋ / 語 ⼄) and cross-verified the result byte-for-byte against both `羅馬字` and `諺文` already stored on each file before using it — the same "compositional-reading-as-tiebreaker" method already established vault-wide for real word creation, not a fabrication.

**Extraction bug caught mid-task, not shipped**: an early batch-extraction script for gathering `english` fields grabbed the first 3 list items after the `english:` key without stopping at the next YAML key — on 8 files with fewer than 3 real glosses (国子, 三国, 中国, 邾国, 鄂国, 鄭国, 獅子国, 五代十国, 中国人), this silently pulled the *next* field's contents (mostly `aliases:`, e.g. 國子, 中國, 三國) in as a bogus third gloss. Caught by spot-checking a few entries before writing anything to the page, rewrote the extraction to stop exactly at the next top-level key, and redid the full batch — no contaminated glosses made it into the file.

No `graphemic_classification: 国` hits — no Derived Characters section applies.

### 2026-07-22, iteration 38 — [[characters/明 (char)|明]]

Next never-perfected character by `danayo_id` (134) — already had a good graphemic bullet and partial structure, needed a gap-fill and cleanup pass. Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 性詞`, `graphemic_classification: 會意` matching the already-good 会意 bullet, 日+月).

**Content removed**: none.

**Small fixes**: disambiguated the graphemic bullet's `[[日]]`/`[[月]]` links to `[[日 (char)|日]]`/`[[月 (char)|月]]` (both collide with word files); merged a non-canonical bullet that crammed SKIP/Stroke/syllable into one line into the proper two-bullet split, and built a real MC-rank bullet from scratch (the old one was just two bare floating CC-initial/final links with no ordinal rank or syllable link at all).

**Caught and corrected before finalizing — a guessed chengyu gloss, same near-miss class flagged repeatedly this sweep**: while adding 旗幟鮮明 (present on the old page with no gloss at all), first copy-pasted 光明正大's gloss onto it since a quick single-line `grep` on the `english:` key appeared to show nothing for either — re-read both files in full and found 旗幟鮮明's real stored gloss is "have a clear-cut stand," entirely different from 光明正大's. Corrected before shipping; the single-line grep pattern itself was the failure mode (it only shows the `english:` key line, not the list item(s) below it for multi-line fields) — worth remembering as a sharper version of the extraction-script lesson from [[characters/国|国]] two iterations ago.

**Words cross-check** (33 total ground-truth hits): 11 already listed (several bare, reformatted); 22 missing — added, all from stored fields.

**Chengyu cross-check** (4 total): 1 already present (gloss fixed per above); 3 missing — 光明正大, 公明正大, 毎字明意 — added.

**Derived Characters** (2 hits via `graphemic_classification: 明`): 盟 ("alliance; covenant") and 萌 ("bud; sprout") — both exact `注音` matches, added.

**Incidental fix**: `characters/盟.md`'s `english` field had a typo, "aliance" → "alliance."

### 2026-07-22, iteration 39 — [[characters/東|東]]

Next never-perfected character by `danayo_id` (135). Stamped `date-last-perfect: 2026-07-22`.

**Real etymology correction, backed by a cross-reference already sitting on another perfected page**: `graphemic_classification` was stored as `會意`, and Notes had no bullet at all to check it against. Rather than write the popular "sun rising behind a tree" folk story that's often taught but not the accepted scholarly origin, checked [[characters/西|西]]'s own already-perfected page from earlier this loop — its Notes bullet explicitly states "Compare 東 (OC \*toːŋ, 'bundle > east'), 束 and 鹵," i.e. this vault had *already* recorded, on a different page, that 東's real etymology is a pictograph of a tied bundle/sack (the same "borrowed pictograph" family as 西 itself), not a 会意 compound. Corrected the field to `象形` and wrote the bullet accordingly, citing the 西 cross-reference directly and noting the sun-behind-tree story explicitly as a later reinterpretation rather than silently omitting it (a reader who's only heard the folk version deserves the correction spelled out, not just a different answer with no explanation).

**Body defects found**: `## Notes` was entirely empty; two floating CC-initial/final links sat inside the Words list; several entries were bare `[[link]] "gloss"` markdown, one used a relative link with a dash-gloss, one gloss had a stray leading dash baked into the quoted text itself ("- Eastern barbarian").

**Words cross-check** (15 total ground-truth hits): 7 already listed (reformatted, stray dash removed from 東夷's gloss); 5 missing — the `stand_in` compound 東方 itself, 東部, 極東, 東亜, 東京 — added, all from stored fields.

**Chengyu cross-check** (3 total): 古今東西 and 東奔西走 both reused verbatim from [[characters/西|西]]'s own already-perfected entries (same two chengyu, same character pair); 東亜自通 (単亜語-origin) added fresh from stored fields.

**Derived Characters** (3 hits via `graphemic_classification: 東`): 重 ("heavy" — a real if MC-divergent phonetic pair, ɖ+ɨoŋ vs 東's own t+uŋ, both nasal-final rimes, matching Shuowen's 従壬東聲), 凍 ("freeze"), 棟 ("ridgepole") — all added.

### 2026-07-22, iteration 40 — [[characters/育 (char)|育]]

Next never-perfected character by `danayo_id` (136). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 事詞`, `graphemic_classification: 肉`) — verified rather than assumed: cross-checked 肉's own stored Middle Chinese (`ȵ`+`ɨuk`) against 育's own (`j`+`ɨuk`) and found an exact rime match with a plausible palatal-initial correspondence, confirming the field genuinely reflects Shuowen's real 従𠫓肉聲 analysis (semantic 𠫓, "inverted child" depicting childbirth, + phonetic 肉) rather than assuming it without checking, given how often this sweep has found the opposite.

**Content removed**: none.

**Graphemic bullet written from scratch**: as above, citing the exact MC rime match as the verifying evidence.

**Body defects found**: `# Notes` was the wrong heading level and held only two floating CC-initial/final links — no other bullets, no `## Words` heading at all.

**Words cross-check** (7 total ground-truth hits): none were previously listed — added the stand-in 育 itself plus 教育, 体育, 体育館, 養育, 生育, 肥育, all from stored fields. No chengyu hits.

**Derived Characters** (1 hit via `graphemic_classification: 育`): 充 ("fill" — Shuowen's 従儿育省聲, phonetic 育 abbreviated), added.

**Incidental fix**: the character's own `english` field had a typo, "nuture" → "nurture."

### 2026-07-22, iteration 41 — [[characters/於 (char)|於]]

Next never-perfected character by `danayo_id` (138; 137 already stamped on inspection). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter**: already correct (`pos: 修飾語`, matching its real function as a locative preposition/case particle; `graphemic_classification: 象形`).

**Content removed**: a stray, meaningless fragment line, "方,仒" — not real content, sitting where the graphemic bullet should have been. Removed outright.

**Graphemic bullet written from scratch**: 於 is a variant/simplified form of 烏 ("crow"), later borrowed purely for its sound to write the grammatical particle "at, in" — a standard, uncontested account (unlike a couple of other 象形 characters this loop has had to hedge on).

**Body defects found**: no SKIP/Stroke/MC/Levels bullets existed; two floating CC-initial/final links had no MC bullet to embed in.

**Words cross-check** (1 total ground-truth hit, the stand-in itself): added, from stored fields. **Chengyu built from scratch** (1 hit): 義重於音 (単亜語-origin), ruby/gloss from stored fields. No `graphemic_classification: 於` hits — no Derived Characters section applies.

### 2026-07-22, iteration 42 — [[characters/姉 (char)|姉]]

Next never-perfected character by `danayo_id` (139). Stamped `date-last-perfect: 2026-07-22`.

**Frontmatter fixed — a real etymology correction, no pre-existing bullet to check it against**: blank `pos: ""` → `名詞`. `graphemic_classification: 巾` was checked against 巾's own stored Middle Chinese (`k`+`ɣiɪn`) versus 姉's own (`t͡s`+`ia`) — no plausible phonetic relationship at all (different initial class, different rime shape, no shared feature). The real Shuowen etymology for 姊/姉 is 従女，𠂔聲 (phonetic 𠂔, a rare/obsolete glyph, not 巾) — corrected the field to `𠂔` and described the component in prose without a link, since it has no character page in this vault (same treatment as 気/气 and 左/𠂇 precedent elsewhere in this sweep).

**Content removed**: none.

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; both existing Words entries were bare `[[link]] "gloss"` with no ruby.

**Words cross-check** (4 total ground-truth hits): 2 already listed (reformatted); 2 missing — the stand-in 姉 itself and 兄弟姉妹 (ruby/gloss reused from [[characters/弟 (char)|弟]]'s and [[characters/妹|妹]]'s own entries for the same word) — added. No chengyu hits, no `graphemic_classification: 姉` hits.

### 2026-07-22, user-flagged correction — periodic-table abbreviation notes wrongly demoted on three pages

**User correction, mid-loop**: iterations 1 ([[characters/多 (char)|多]]), 13 ([[characters/西|西]]), and 21 ([[characters/里 (char)|里]]) each originally had a Notes bullet reading "abbreviation for [element]," which this loop treated as incidental trivia and moved into the `## Words` entry for the coined element-name compound, in some cases (西) losing the "abbreviation for" framing entirely down to a bare gloss. **This was wrong**: within this vault's element-naming system, a single Dan'a'yo character is deliberately assigned to function as that element's own abbreviation/symbol — the same role a letter like "Gd" or "Sg" plays in a real periodic table, not just a component of one specific coined word. That fact belongs on the *character's own page*, in Notes, not folded away as a parenthetical on the word page.

**Fixed**: restored a dedicated trailing Notes bullet on all three pages, keeping the "functions as an element-abbreviation character" framing explicit and linking to the actual coined word (加多金 gadolinium/Gd, 西博金 seaborgium/Sg, 居里金 curium/Cm) rather than just leaving it inside that word's own Words-section gloss. The Words-section entries themselves are left in place unchanged — this was about restoring the character-level fact, not removing the word-level listing.

**Standing rule going forward**: when a character's stored Notes content mentions "abbreviation for [element]" or similar, treat it as a real, permanent fact about that character (keep as its own trailing Notes bullet), not as duplicate/incidental content to fold into the Words section — even if a Words entry for the same compound already exists.

### 2026-07-22, iteration 43 — [[characters/学|学]]

Next never-perfected character by `danayo_id` (140). Stamped `date-last-perfect: 2026-07-22`. **The largest page this loop has done — 56 Words entries** (surpassing [[characters/国|国]]'s 63... actually 国 remains the largest by count, this is the second-largest).

**Frontmatter**: blank `pos: ""` → `事詞` — precedent from `words/学習.md`'s own stored `pos: 事詞`. **Real etymology correction**: `graphemic_classification: 指事` (a pure indicator/dot-marking classification) doesn't fit 学/學 at all — its real, uncontested etymology is 会意 of 爻 ("crossed counting rods") + 冖 ("roof") + 子 ("child"), a child studying calculation under a roof, one of the more famous textbook 会意 examples. No pre-existing bullet to contradict (Notes was empty) — corrected from scratch and wrote the bullet accordingly.

**Content removed**: none.

**Body defects found**: `## Words` used a numbered list (1–35) for most entries with only a handful ruby'd, switching to unordered bullets partway through with no clear reason; two floating CC-initial/final links had no MC bullet to embed in.

**Words cross-check** (56 total ground-truth hits, computed via a full diff script rather than manual counting given the scale — confirmed zero false-positive "extra" entries, all 43 originally-listed items were genuine): 13 missing — the `stand_in` compound 学習 itself, 学生, 大学, 中学校, 教学, 儒学, 数学, 化学, 化学肥料, 人類学, 天文学, 物理学, 生物学, 老人学 — added, all from stored fields. **Two more missing-`注音` word files found** (same class as [[characters/国|国]]'s 中国人/中国語 two iterations ago): `words/中学校.md` only had `羅馬字`/`諺文` — reconstructed via constituent-character concatenation (中 ㄐㄨㄫ + 学 ㄏㄚㄎ + 校 ㄏ⼘ㄨ) and cross-verified against both stored fields before using it.

**Derived Characters** (1 hit via `graphemic_classification: 学`): 覚 ("perceive" — Shuowen's 従見學省聲, phonetic 学 abbreviated), added.

**Incidental fix**: `words/経済学.md`'s `english` field read "economic" (adjective) where "economics" (the field of study) was clearly meant — corrected.

### 2026-07-22, iteration 44 — [[characters/雨 (char)|雨]]

Next never-perfected character by `danayo_id` (141). Stamped `date-last-perfect: 2026-07-22`. Page already had a nice non-canonical extra — a radical-disambiguation callout line ("For the radical, see Radical 173") beyond the standard template — kept as-is per the "preserve genuinely useful extra content" precedent.

**Frontmatter**: already correct (`pos: 名詞`, `graphemic_classification: 象形` matching an already-good, sourced bullet with an Egyptian hieroglyph comparison).

**Content removed**: none.

**Body defects found**: `## Words`, `## Chengyu`, and `## Notes` appeared in that (wrong) order; two floating CC-initial/final links had no MC bullet to embed in; four Words-style entries (雨傘, 雨中, 俄雨, 小雨) were sitting inside `## Notes` instead of `## Words`.

**Words cross-check** (8 total ground-truth hits): 6 already present across the misplaced sections (consolidated, reformatted); 2 missing — the stand-in 雨 itself and 林雨 — added. Also added 梅雨, which despite appearing to already be covered by the general pattern was genuinely absent.

**Chengyu cross-check** (2 total): 1 already present (五風十雨); 1 missing — 未雨紬謬 (《詩經》-origin) — added.

**Derived Characters** (1 hit via `graphemic_classification: 雨`): 黍 ("millet" — Shuowen's 従禾雨省聲, phonetic 雨 abbreviated, an unusual but genuine attested relationship), added.

### 2026-07-22, iteration 45 — [[characters/門|門]]

Next never-perfected character by `danayo_id` (142). Stamped `date-last-perfect: 2026-07-22`. **First real application of the new standing rule** ([[feedback_element_abbreviation_characters]], added this session after the user's correction on 多/西/里): this page's own Notes already had an "abbreviation for mendelevium" bullet for [[門捷金]] — kept it as its own trailing Notes bullet this time instead of repeating the earlier mistake of folding it into the Words entry alone.

**Frontmatter**: already correct (`pos: 名詞`, `graphemic_classification: 象形`).

**Content removed**: none.

**Graphemic bullet expanded**: from a bare heading with no bullet at all — wrote it from scratch (a double door/gate, linking 門's own radical, [[Radical 169|門]], since the character depicts itself).

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; no SKIP/Stroke/Levels bullets existed.

**Words cross-check** (10 total ground-truth hits): 3 already listed (専門, 門捷金, 奥門); 7 missing — the `stand_in` compound 大門 itself, 門戸, 校門, 凱旋門, 部門, 肛門, 陰門 — added, all from stored fields.

**Derived Characters** (3 hits via `graphemic_classification: 門`): 聞 ("hear"), 問 ("question"), 悶 ("agony") — all standard, well-attested 門-phonetic derivatives, added.

### 2026-07-22, iteration 46 — [[characters/苦 (char)|苦]]

Next never-perfected character by `danayo_id` (143). Stamped `date-last-perfect: 2026-07-22`. **Second application of the new element-abbreviation standing rule**: this page's Notes had a garbled numbered-list fragment ("1. bitter / 2. abbreviation for 'magnesium'") sitting before the real graphemic bullet — kept the magnesium-abbreviation fact as its own proper trailing Notes bullet (linking [[苦土素]]) rather than discarding it, per the rule added earlier this session.

**Frontmatter**: already correct (`pos: 性詞`, `graphemic_classification: 古` matching an already-good, OC-cited bullet).

**Content removed**: the garbled "1. bitter / 2. abbreviation..." numbered-list fragment (superseded by the real graphemic bullet and the restored magnesium note below it); a literal duplicate — `苦土素`'s ruby+gloss line was typed out twice on the same bullet ("magnesium `<ruby>...` magnesium `<ruby>...`"), collapsed to one; six Words entries (苦役, 苦難, 苦肉, 苦悩, 刻苦, 苦味) existed as **two separate copies each** — a bare `* [[link]] gloss` asterisk-bullet list followed later by a proper ruby'd dash-bullet list repeating the same six compounds — deduplicated, keeping the properly-formatted copy of each.

**Words cross-check** (14 total ground-truth hits): 9 already present after deduplication; 5 missing — the stand-in 苦 itself, 苦土, 苦悶, 苦渋, 辛苦 — added, all from stored fields. No chengyu hits, no `graphemic_classification: 苦` hits.

**Incidental fix**: `words/辛苦.md`'s `english` field had a typo, "word hard" → "work hard."

### 2026-07-22, iteration 47 — [[characters/空 (char)|空]]

Next never-perfected character by `danayo_id` (144). Stamped `date-last-perfect: 2026-07-22`. Page already had a real, correctly-cited graphemic bullet — this iteration was mostly reordering and gap-filling.

**Frontmatter**: already correct (`pos: 性詞`, `graphemic_classification: 工`).

**Content removed**: none.

**Body defects found**: `## Chengyu` sat before `## Words`; bullets 2–4 were merged into non-canonical forms — a Levels bullet came before the MC bullet, and the MC bullet crammed SKIP/Stroke/syllable/CC-links together with middle-dot separators instead of the canonical two-bullet split. Rebuilt into the standard four-bullet order.

**Words cross-check** (14 total ground-truth hits): 4 already listed (reformatted); 10 missing — the stand-in 空 itself, 空手道, 天空, 空気, 空港, 空白, 空虚, 航空, 航空母艦, 孫悟空 — added, all from stored fields.

**Chengyu cross-check** (4 total): 3 already present and correctly formatted; 1 missing — 海闊天空 — added.

**Derived Characters** (2 hits via `graphemic_classification: 空`): 控 ("accuse; charge") and 腔 ("chest cavity") — both standard, well-attested 工-family phonetic derivatives via 空, added.

### 2026-07-22, iteration 48 — [[characters/知 (char)|知]]

Next never-perfected character by `danayo_id` (146; 145 already stamped on inspection). Stamped `date-last-perfect: 2026-07-22`. Already flagged as unperfected as far back as [[Word Perfecting.md]] iteration 7 ("bare '矢, 口' Notes fragment") — that stray fragment was still sitting there unresolved.

**Real etymology correction**: `graphemic_classification: 矢` asserted 形声 with phonetic 矢, but the classical Shuowen entry for 知 reads "从口从矢" — both components stated as meaning-contributing (会意), with no phonetic relationship claimed at all. The page's own leftover "矢, 口" fragment (a bare component list, not a real bullet) was itself evidence pointing the same direction — someone had already identified both components as relevant, just never finished writing the analysis. Corrected the field to `會意` and wrote the bullet: an arrow's swiftness/directness + mouth/speech — words spoken as unerringly as an arrow flies, "to know." Linked 矢 to its Radical page (`[[Radical 111|矢]]`, since 知's own `radical:` field is 矢).

**Content removed**: the stray "矢, 口" component-list fragment (superseded by the real bullet) and an empty bullet (`- ` with nothing after it).

**Body defects found**: `# Notes` was the wrong heading level; two floating CC-initial/final links had no MC bullet to embed in; several Words entries were bare `[[link]]` with no ruby/gloss.

**Words cross-check** (8 total ground-truth hits): 7 already listed (reformatted); 1 missing — the stand-in 知 itself — added.

**Chengyu**: 温故知新 already present and correctly formatted, no changes needed.

**Derived Characters** (3 hits via `graphemic_classification: 知`): 智 ("wisdom," transparently 知+日), 蜘 ("spider," as in 蜘蛛), 痴 ("stupid; foolish") — all standard, well-attested 知-phonetic derivatives, added.

**Incidental fix**: `words/知性.md`'s `english` field had a typo, "knowledgable" → "knowledgeable."
