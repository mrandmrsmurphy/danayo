---
name: skill-lint
description: Argument-driven bulk-consistency sweep over one content type at a time (e.g. "lint SKIP"). Cross-references lookup pages against the character/word corpus to find gaps, truncated previews, stale entries, and stamps date-last-perfect once verified.
type: skill
---

# Skill: Lint

The vault is too large and heterogeneous for one linter to cover everything at once. `lint` always takes an argument naming *what* to sweep — `lint SKIP`, `lint Radicals`, `lint Syllables`, and later `lint Stroke`, etc. Each argument gets its own procedure section below, grounded in that content type's `AIOS/checklists/checklist_*.md` rubric. Don't run `lint` bare.

## General shape of a lint pass

1. **Ground truth first.** Every lookup tree (SKIP, Radicals, Stroke, ...) is a derived index over the real data in `characters/` (and sometimes `words/`). Before touching any lookup page, grep the corpus for the field that tree is indexing (`skip_number`, `radical`, `stroke_count`, ...) and build the authoritative map of what *should* exist. Never trust the lookup tree's current content as ground truth — it's exactly what's being checked.
2. **Fix bottom-up.** Leaf files (the actual per-code lookup targets) before index/stem files (the pages that summarize and link leaves), before any top-level overview. Index previews are derived from leaf contents (character list, `size`), so fixing leaves first means the index rebuild has correct data to summarize instead of propagating stale numbers. This was confirmed necessary in practice: `SKIP-1-9-11`'s `size` had to be corrected before `SKIP-1-9.md`'s preview line could be trusted.
3. **Batch by folder, not by file.** At hundreds of files, work stroke-group by stroke-group (e.g. everything under `SKIP-1/` for left-half-count 9) rather than one file at a time — one ground-truth query serves an entire folder.
4. **Dispatch to forks for the mechanical sweep.** The per-file diff-and-fix work is high-volume, low-judgment, and its raw tool output isn't worth keeping in the main conversation. Fork per batch (e.g. one fork per `SKIP-N-M` folder-group), report back a short list of what was fixed/created/flagged, and keep the coordinating conversation to the summary level. Judgment calls (e.g. "is this character actually forbidden, or just miscategorized") get surfaced back, not resolved silently by the fork.
5. **Stamp `date-last-perfect` last**, only after a file's own checklist criteria are actually satisfied — not as a bulk find-replace independent of verification. A page whose gaps couldn't be resolved (e.g. a leaf file is missing and creating it requires data not on hand) keeps its old date or stays unstamped, and gets flagged in the summary instead.

## `lint SKIP`

Rubric: [[AIOS/checklists/checklist_skip.md]] — read it in full before running this; the summary below assumes it.

### 0. Scope

`lookup/SKIP/` is ~536 files: `SKIP.md` (one top-level overview), four first-number folders `SKIP-1/` (189 files) through `SKIP-4/` (62 files), each containing index files (`SKIP-#-#.md`) and leaf files (`SKIP-#-#-#.md`). SKIP-4 additionally has stroke-count indexes (`SKIP-4-#.md`) and four subtype-overview files (`SKIP-4-0-#.md`) — see the checklist for how its breadcrumbs and structure differ from SKIP-1/2/3.

### 1. Build ground truth

```bash
grep -h "^skip_number:" characters/*.md
```
normalized into a map of `skip_number → [character files]`. This tells you definitively which leaf codes should exist and which characters belong on each — independent of what the lookup tree currently says.

### 2. Leaf files first

For every `skip_number` that appears in the ground-truth map:
- **Missing leaf file** → create it: frontmatter (`stroke_count`, `size`, `skip_number`, `date-last-perfect`), breadcrumb, `## Characters` (numbered, ruby + gloss, per checklist format), `## Datacheck` block. SKIP-4 leaves need the double breadcrumb (stroke-count index + subtype overview).
- **Existing leaf file** → verify:
  - `size` equals the actual character-entry count (aliases/redirects don't count)
  - every character in the ground-truth map for this code appears in the `## Characters` list, and vice versa (catches both omissions and stale/wrong entries — a character listed here that no longer has this `skip_number` in its own file)
  - `### Aliases` / `### Forbidden` sections present where applicable, per the checklist's definitions of each
  - `Datacheck` query's `skip_number` string matches frontmatter exactly
  - Fix what's wrong, then stamp `date-last-perfect` to today.

### 3. Index (stem) files second

For every `SKIP-#-#.md` (and SKIP-4's `SKIP-4-#.md` / `SKIP-4-0-#.md`):
- List **every leaf file that exists** on disk under it, in numeric order — not just the ones an old preview happened to mention.
- Each preview line shows **every** character in that leaf, no truncation. (`SKIP-1-9-4` had 12 characters; the index preview showed 8 and an ellipsis — that's the exact bug class to hunt for. Cross-check preview character count against the leaf's own `size` field to catch this mechanically.)
- Positions with no leaf file get an explicit `none`/`no` line — don't just omit them silently, and don't extend the list past the highest position that actually has data or an intentional gap-marker.
- `## Base check` block present.
- Stamp `date-last-perfect` once the above hold.

### 4. Top-level `SKIP.md`

One file, checked last since it just links the 1/2/3/4 category pages and the four `SKIP-4-0-#` placeholders. Confirm every linked stroke-count page (`SKIP-1-1` through `SKIP-1-15`, etc.) actually exists and is a real link, not dead text — `SKIP.md` currently has exactly this bug at its "14." entry under First Number 1: literal text `14` instead of a link, because `SKIP-1-14.md` doesn't exist yet. Either create the missing index (if the ground-truth map has characters at that position) or confirm it's legitimately empty and represent that explicitly rather than leaving broken filler text.

### 5. Report

Per folder-group: counts of leaves created / leaves fixed / indexes fixed / dates stamped, plus a short list of anything that needed a judgment call rather than a mechanical fix (miscategorized character, ambiguous alias, etc.) for the user to weigh in on.

## `lint Radicals`

Rubric: [[AIOS/checklists/checklist_radicals.md]] — read it in full before running this; the summary below assumes it.

### 0. Scope

`lookup/Radicals/` is 215 files: 214 leaf pages (`Radical 001.md` through `Radical 214.md`), one per Kangxi radical, plus the top-level `Radicals.md` overview that lists all 214 grouped by stroke count. There is no intermediate index tier here (unlike SKIP's index/leaf split) — each `Radical NNN.md` is simultaneously the leaf (full character inventory) and the only page between a character and the top overview.

### 1. Build ground truth, and check the source property itself

```bash
grep -L "^radical:" characters/*.md
```
Any character file this returns is a hard gap — a character that cannot be placed on any radical page because it lacks the property being indexed. Flag every one; this is a character-page defect, not a Radicals-page one, so fix it by adding the correct `radical:` value to the character's own frontmatter (per [[AIOS/checklists/checklist_characters.md]]), not by working around it on the lookup side.

```bash
grep -h "^radical:" characters/*.md
```
normalized into a map of `radical → [character files]`. Some radicals have multiple canonical written forms (e.g. 丿/乀/乁, 儿/兒) — `Radicals.md`'s own stroke-grouped listing documents which forms belong to which radical number; fold variants into the same map entry rather than treating them as separate radicals. This map, not the current contents of any `Radical NNN.md`, is ground truth for what belongs where.

### 2. Leaf files (`Radical NNN.md`)

First determine which of the two valid styles applies (see [[AIOS/checklists/checklist_radicals.md]]): **grouped** (`## Strokes` / `+N Strokes` subsections) is required at `size >= 20`; below that, either grouped or **prosaic** (`## Characters` with encyclopedic opening + `### Used`/`### Variants`/`### Illegal`) is acceptable — don't force a `size < 20` page into grouped format if it's already properly prosaic, and don't accept a bare flat list under either style as if it were finished prosaic work.

For each of the 214:
- Every character in the ground-truth map for this radical has a numbered entry (in the correct `+N Strokes` group for grouped-style, or under `### Used` for prosaic-style), and vice versa (catches both omissions and stale/misfiled entries).
- **Linkage, not backlink**: confirm the character is *linked to from* the radical page (numbered entry with a working link to the character file). Do **not** require the reverse — a `radical`-type backlink from the character page to `[[Radical NNN]]` — since that reciprocal link doesn't exist on most character pages yet. Flag its absence as a to-do for a future pass once character pages are further along, but it does not block stamping this page's `date-last-perfect`.
- **Grouped style**: `+0 Strokes` group present and containing exactly the radical itself as entry 1 — **but only when the radical symbol is itself a standalone character in `characters/`**. If it isn't (component-only radicals like 儿, 冫, 宀, 彳, 艸), a missing `+0` is correct as long as the opening description says so explicitly (e.g. "No character is filed at +0, so groupings below start at +1") — don't flag it. Also watch for legitimate negative-stroke groups (e.g. `Radical 064.md`'s `-1 Stroke` for 才, which has fewer strokes than 手): confirm against the character's own `stroke_count` before assuming a negative heading is wrong.
- **Prosaic style**: opening is a real multi-sentence encyclopedic passage, not a one-liner; illegal/forbidden entries each carry a short reason, not a bare label.
- `size` equals the actual count of numbered entries (aliases/forbidden/Others/Variants/Illegal excluded).
- `radical` frontmatter value matches exactly what the data check query and the character-frontmatter ground truth use.
- `## Data check` heading and query present, sorted `stroke_count ASC` (grouped) or `file.name ASC` (prosaic, matching `Radical 212.md`'s convention); queries every variant form with `OR radical = "..."` when the radical has more than one written form.
- Fix what's wrong, then stamp `date-last-perfect` to today.

### 3. Top-level `Radicals.md`

Checked last. For each of the 214 stroke-grouped entries:
- Links to a real `Radical NNN.md` file (wiki-link or relative markdown link, not dead text).
- The character count shown in parentheses matches that leaf's `size` field.
- All 214 radicals are present, correctly grouped under their stroke-count heading, in radical-number order within each group.
- Combining/simplified-radical callout lists (e.g. "Combining or simplified radicals with 2 strokes") stay consistent with what each affected leaf page's frontmatter and data check actually say.
- `## Base check` block present and querying `lookup/Radicals`.

### 4. Report

Counts of: character pages missing `radical:` entirely (flag prominently — these are corpus gaps, not lookup-page bugs), leaves fixed, dates stamped, and any characters found linked from the wrong radical page. Separately note the running total of character pages still missing the reciprocal `radical`-page backlink, without treating it as a blocker.

## `lint Syllables`

Rubric: [[AIOS/checklists/checklist_syllables.md]] — read it in full before running this; the summary below assumes it.

### 0. Scope

`syllables/` is 895 files, one per Bopomofo syllable code, plus one top-level `syllables/Syllables.md` (a hand-written phonology-table + series-listing overview, not a generated index). Like Radicals, there's no index/leaf split — each syllable file is simultaneously the ground-truth target and the only page between a character and the overview.

### 1. Build ground truth

```bash
grep -hE '^注音: "?VALUE"?$' characters/*.md
```
normalized into a map of `注音 → [character files]`. **The `"?` tolerance is mandatory, not optional** — `注音` is stored quoted on some character pages and bare on others (both forms coexist throughout `characters/`), and a plain `grep -h "^注音:"` / exact unquoted match silently drops every quoted file from ground truth. This was confirmed to zero out ground truth entirely for several codes in the April batch before being caught — always sanity-check a zero-character result against the page's own existing content before concluding a syllable is legitimately empty.

This is ground truth, not the syllable page's current content (often a leftover `dataviewjs` placeholder) — never trust the page over it. Pull `grade_level` and `stand_in` from each matched character's frontmatter at the same time:
- `grade_level` drives categorization — `1`-`6` is **Common**, `先進` is **Advanced**, `名` is **Naming**.
- `stand_in` determines entry *format*, independently of `grade_level`'s subsection choice (see below): compare it against the character's own filename (minus the ` (char)` suffix, if present).
  - Equal to the character's own name → **stand-alone** (a word file exists at that name).
  - Literally `名専字` → **naming-restricted**.
  - Any other value → **bound**, and that value *is* the exact compound to cite in the `"but requires"` clause — no need to search for which compound applies, `stand_in` already names it.
- Build the map from the full `grep -h` output grouped by exact field value, not a per-page substring grep — `注音: ㄨㄨㄨ` must never match a page for `ㄋㄨㄨㄨ` just because one contains the other as a substring.

### 2. Leaf files (`syllables/X.md`)

For every `注音` code in the ground-truth map:
- **Frontmatter**: `羅馬字`, `諺文`, `注音` match the filename and each other; `english` has exactly one entry per stand-alone character (primary meaning only — not every meaning), in the same order those stand-alones are first introduced in the intro line / Characters section (not an arbitrary or inherited order); `ø` if there is no stand-alone; `size` equals the total Common+Advanced+Naming entry count. Array-type fields (`english`, `japanese`, etc.) must stay YAML lists even with one entry — a bare scalar (`english: ford`) is a defect, not a shorthand.
- **Intro block**: three-script line `**注音/諺文/羅馬字**` stating the meaning(s), citing the stand-alone(s) in parentheses, joined with "or" if there are multiple. Both scripts must actually be bopomofo-first — a page reading `**fai** means...` (romanization standing in for the whole header) is a more severe variant of "missing a script," not just an omission. Breadcrumb directly above it must be the canonical `> [Syllables](syllables/Syllables.md)` (from `syllables/X.md`, that's `syllables/Syllables.md` — a bare `Syllables.md` with no `syllables/` prefix is a dead relative link even though it reads as "right") — watch for drift like a singular "Syllable" or an absolute-path/wiki-link variant too.
  - **No stand-alone at all**: write exactly `> **注音** has no intrinsic meaning.` — bopomofo code only, no 諺文/羅馬字, single space, trailing period. This is `checklist_syllables.md`'s own literal example; don't expand it to the three-script form used for pages that do have a meaning. (Wave-1 page `syllables/ㄨㄆ.md` was stamped with the three-script variant before this was caught — revisit it for consistency.)
  - **Audio line**: `![x](/images/X.ext)` with a **leading slash is correct** — that's the checklist's own canonical form, root-relative, not a hygiene defect to "fix" into a relative link. Do verify the file actually exists on disk, both before adding a new audio line and before trusting one that's already there — a stale reference to a file that was never actually placed does occur.
- **Primary meaning, not just any meaning**: applies everywhere a gloss appears on the page — frontmatter `english`, the intro line, *and* each Characters-list entry's own quoted description. All must trace to the character's *first-listed* `english` sense in its own frontmatter, not whichever sense (or paraphrase) an older revision happened to pick. This holds even when the old gloss is arguably more specific/informative (e.g. "Emperor Shun" vs. the frontmatter's generic "a legendary ruler") — don't inject outside knowledge not present in the corpus; keep every gloss traceable to its source data. Strip trailing parenthetical qualifiers from that primary sense for the syllable-page gloss (`"lead (substance)"` → `"lead"`, `"Yanzhou (place name)"` → `"Yanzhou"`) — the qualifier belongs to the character page's own disambiguation, not the syllable page's short gloss. Check this on every page, even one that already "looks" done. If a character's own `english` order looks backwards (a rarer/less-expected sense listed first), don't silently "fix" it to what seems obviously right — that's a character-page edit outside this page's scope; flag it instead.
- **Characters section**: replace any leftover `dataviewjs` block entirely with the hand-curated list, split into `### Common` / `### Advanced` / `### Naming`. Every character in the ground-truth map for this code has exactly one numbered entry in the correct subsection, and vice versa (catches both omissions — a ground-truth character simply absent from the page — and stale/misfiled entries — a character listed here whose own `注音` frontmatter actually points elsewhere; both occurred repeatedly in March/April batches, always verify both directions).
  - **Grade_level (subsection) and stand_in (entry format) are fully independent axes — do not assume they correlate.** A `名`-grade character in `### Naming` is *not* automatically 名専字-formatted; it may have a `stand_in` making it stand-alone or bound, formatted exactly as it would be in Common/Advanced. This recurs often enough (multiple times per 10-file batch) that it's the single easiest mistake to make skimming this procedure — check `stand_in`'s actual value for every entry regardless of which subsection it lands in.
  - Stand-alone: char-link, quoted meaning, `-->` word-link — and confirm the arrow actually targets the `words/` file, not (as found once) a copy-paste that still points back at the character page under `characters/`.
  - Bound: `"but requires"` (exact phrasing — normalize variants like `"- **requires**"` found in the wild) + ruby-annotated compound link. Verify the compound word file actually exists under `words/` before citing it. The ruby text itself must match that word file's own stored `注音` value **byte-for-byte**, including presence/absence of a `·` separator — don't assume simple concatenation of the parts' readings; some compounds' `注音` includes the dot, most don't, and it's a distinct check from "ruby is present." If `stand_in` doesn't match any file on disk and isn't a plausible typo (see below), the corpus has a real gap — flag it, don't stamp. Existence alone isn't full confirmation either: if the word file exists but the compound string doesn't actually contain the syllable's own character (e.g. `stand_in: 練習` cited for a character not present in 練習), that's a likely `stand_in` mismatch — cite it as found (don't silently drop the link) but flag it as a probable corpus error rather than treating "file exists" as case-closed.
  - Naming-restricted: `"but it's a 名専字"`.
  - Numbering is continuous 1-N straight through all three subsections in order — no restarting the count at `### Advanced`, no gaps, no duplicates. Within each subsection, order entries by `grade_level` ascending (mirroring the Data check's own sort) rather than leaving stale/arbitrary insertion order.
- **Data check block**: `dataview` query filtered on `注音` (never `諺文`) matching frontmatter exactly — including dropping any dead extra `OR 注音 = "..."` clause that doesn't correspond to a real character — sorted `grade_level ASC` (never `file.name` or anything else). A stale query shape is a defect even if its results happen to look right today.
- **Fence, link, and content hygiene**: check for an unclosed ` ```dataview ` fence (silently swallows everything after it — same bug class found in the Radicals sweep); relative links missing `../`; links mixing wiki-syntax with a path (`[[../words/X]]`); and stray orphan content left outside the defined sections (e.g. a leftover debug link sitting between the intro and `## Characters`) — pick one link style consistently and remove anything that isn't intro block / Characters section / Data check block. (Absolute leading-slash links are correct for audio embeds specifically — see above — this bullet is about everything else.)
- **Unresolved corpus gaps are not blockers to leave silently** — if a character's `stand_in` points to itself (implying stand-alone) but no matching word file exists anywhere, don't fabricate the link and don't stamp `date-last-perfect`; leave the old date and surface it as an explicit corpus decision (create the missing word, or the `stand_in` field itself is wrong) for the user.
- Fix what's wrong, then stamp `date-last-perfect` to today — only once the page genuinely satisfies all of the above, not as a bulk action independent of verification.

### 3. Top-level `Syllables.md`

Checked last, and lightly — it's a hand-authored phonology table plus per-series link lists (`## A vowels` / `### ㄚ series` etc.), not a mechanical index, so don't try to regenerate it wholesale each pass. For any syllable code touched in this batch: confirm it appears as a real link (not bare text) if the leaf page exists, and stays bare/unlinked only for codes that are legitimately unattested (not just missing a page). Flag broader drift here for a dedicated pass rather than fixing it inline.

### 4. Report

Per batch: counts of leaves fixed / dates stamped, plus a short list of judgment calls for the user — ambiguous stand-alone determination, a `but requires` compound that turned out not to exist as a word, or an unclear `grade_level` categorization.
