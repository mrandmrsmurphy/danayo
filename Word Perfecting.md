# Word Perfecting Log

**2026-09-11: Methodology pivot.** The sweep previously ran a strict alphabetical (`LC_ALL=C`) resweep over *every* file in `words/`, re-verifying and re-stamping each one regardless of whether it already had a `date-last-perfect`. That's slow and wasteful: as of this pivot, 6011 words exist total, but only **246 have never been touched at all** (no `date-last-perfect` field whatsoever) — the rest already carry a stamp from an earlier pass. The user corrected this: going forward, the sweep processes **only the 246 never-perfected words**, one per cron firing, until that list is empty. The full alphabetical resweep can resume afterward if desired.

### 2026-09-11, word 1/246 — [[words/僧伽|僧伽]]
Never-perfected word, genuinely untouched. Fixed inline-flow `characters:`, filled blank `pos:` (名詞), unspaced cantonese, removed dangling blank `hsk_level:`/`swadesh:`/empty `aliases: []`, merged thin `## Etymology` into a full `## Notes` section. **Found and fixed a real internal self-contradiction**: this word's own `注音` (ㄙㄜㄫㄍ⼘, "seng"-pattern) didn't match its own `諺文`/`羅馬字` (숭갸/sunggya, "sung"-pattern) — corrected `注音` to ㄙㄨㄫㄍ⼘, joining the "sung" variant already used consistently by sibling words [[僧侶]]/[[尼僧]]/[[密陀僧]] (per 僧(char)'s own long-standing flagged note about this cross-word inconsistency, now updated to record the fix). Updated the citation ruby on 僧.md to match. **Found and fixed an entirely-missing `## Words` section** on 伽.md (had no Words list at all) — added citations for both 僧伽 and 揄伽. `kwin: false` confirmed (own 諺文 숭갸 vs own korean 승가 diverge), no homophone collision, both constituent citations now present.

Next: 僧家.

### 2026-09-11, word 2/246 — [[words/僧家|僧家]]
Never-perfected word. Filled two entirely-blank fields (`cantonese: ""` and `vietnamese: ""`) with compositional readings (zang1 gaa1, tăng gia — the latter a coincidental homograph with the common phrase "to increase," disclosed rather than avoided). Removed duplicate `品詞` key, merged thin `## Etymology` into a full `## Notes` section, filled a missing `date-last-perfect` entirely. Added a missing legitimizing note for 僧, whose own `stand_in` points to this word. Both character-page citations already present, `kwin: true` confirmed exact match, no homophone collision.

Next: 儀式.

### 2026-09-11, word 3/246 — [[words/儀式|儀式]]
Never-perfected word. Filled entirely-missing `kwin` (false, verified byte-level: own 諺文 읫식 U+C76B ≠ own korean 의식 U+C758, same 읫/의 divergence pattern as 倚/義) and entirely-missing `date-last-perfect`; wrote a `## Notes` section from scratch (page had none). Added a missing legitimizing note for 儀, whose own `stand_in` points to this word. Both character-page citations already present, no homophone collision.

Next: 儀礼.

### 2026-09-11, word 4/246 — [[words/儀礼|儀礼]]
Never-perfected word. Removed duplicate `品詞` key, flattened single-item `japanese`/`vietnamese` lists, filled entirely-missing `kwin` (false) and `date-last-perfect`, fixed broken relative links, integrated a stray unformatted note ("Also the name of a famous book") into proper prose about the Confucian classic 儀禮. `characters:` confirmed correct via `ls` (礼 (char) disambiguation necessary), both character-page citations already present, no homophone collision.

Next: 儒学.

The prior log (4397 iterations, 2026-08-05 through 2026-09-11) is archived as `Word Perfecting 5.md.zip`, following the same rollover convention as archives 2–4.

**The 246-word backlog** (confirmed via `grep -L "^date-last-perfect:" words/*.md`, LC_ALL=C sorted) is tracked in the memory file `project_word_sweep_position.md`, with a checked-off copy maintained there as the authoritative remaining-work list. This log records one entry per completed word going forward, same format as before.

---
