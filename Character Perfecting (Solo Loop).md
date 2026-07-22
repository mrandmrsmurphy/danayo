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
