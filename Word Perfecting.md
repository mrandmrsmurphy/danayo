# Word Perfecting

Running log for the word-perfecting backlog sweep (see [[AIOS/checklists/checklist_words.md|Checklist: Word Pages]]). The prior log (iterations 1–1040) grew to ~8,500 lines and was archived by the user to `Word Perfecting.md.zip`; this file continues from there. Iteration numbering continues unbroken from the archived log.

**Process**: one word per iteration (per standing pacing preference). Find the next candidate via `grep -L "^date-last-perfect" words/*.md`, sorted alphabetically by filename (Unicode/`LC_ALL=C` order), continuing from the last-processed filename's position in that sort. Check the word's own `characters:` constituents for a `stand_in` match (add the stand-in note if so), verify `羅馬字`/`諺文`/`注音` are the correct concatenation of each constituent's own fields, verify `kwin` via the AND-rule (all constituents' own `kwin` must be `true` for the compound to be `true`), fill blank cross-linguistic fields only when a real value can be verified (leave deliberately blank with a reason otherwise), and check for genuine Dan'a'yo-level homophones (not just same-spelling coincidences in a real language) before stamping `date-last-perfect`.

Next (re-scoped tail, alphabetical-by-filename): 家具 (3222 files remaining per full-vault rescan, per the archived log's last iteration).

### 2026-08-05, iteration 1041 — [[words/家具|家具]]

Neither constituent's `stand_in` points to this word (家's is 家庭, 具's is 工具), so no stand-in note applies. **Content added**: filled blank `hsk_level: "4"` (verified). **Left `vietnamese` blank rather than guessing**: mechanical "gia cụ" doesn't appear to be a standing everyday term — Vietnamese uses native đồ nội thất/đồ đạc instead. Added missing `>[!tip]` header and `## Notes`. `kwin: true` confirmed (AND-rule). No homophones (注音 ㄍㄚㄍㄨ unique). Stamped `date-last-perfect: 2026-08-05`.

Next (re-scoped tail, alphabetical-by-filename): 家庭 (3221 files remaining per full-vault rescan).
