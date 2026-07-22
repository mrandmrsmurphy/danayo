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
