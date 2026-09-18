---
name: project-periodic-table-perfection
description: "Closed 2026-09-17 - Periodic Table lexipedia page and all 118 element word files audited and perfected in one pass"
type: project
---

**Status: closed.** `lexipedia/Periodic Table.md` given a `date-last-perfect` field (it had none before — no checklist exists for lexipedia pages at all; `lexipedia/format.md`'s tiered-vocab template (A1–C1+, `status: new|stub|partial|complete`) is built for semantic-domain pages like Kinship/Animals and doesn't map onto this page's reference-table structure) and systematically audited against all 118 real elements (H–Og) plus 2 adjacent coined words (週期表 "periodic table" itself, 錀琴 "röntgen" the unit).

## Page-level fixes

- Stripped 11 lines of stale, fully-redundant HTML comment scaffolding under the Main and D-Block tables (old romanization lists that just duplicated the live, already-rendered table).
- **Real chemistry error** in the Formula Notation worked examples: InP (indium phosphide) was rendered `紫窒` — 紫 (indium) + **窒 (nitrogen)** — instead of `紫燐` — 紫 + **燐 (phosphorus)**. 窒素/燐素 are easy to confuse on sight; always verify via each word's own `english:` frontmatter field, not visual similarity of the glyphs.
- The two naming-rule bullets said "rows 1, 2, and 13-18" and "rows 2-12" — internally inconsistent (the rule is genuinely about periodic-table **groups/columns**, confirmed by cross-checking the actual table), and "rows 2-12" would even overlap "row 2" from the first bullet. Reworded both to "groups," and dropped a dangling footnote asterisk that had no corresponding footnote text anywhere in the file.
- Reworded an awkward trailing sentence about element 111 lending its phonetic to 錀琴 (röntgen, the unit).

## Word-file bugs found (6 words) — method

Wrote a script cross-checking every word's own stored `羅馬字`/`諺文`/`注音` against the live concatenation of its own listed `characters:` field's own stored readings (not eyeballing) — 120 words checked, all constituent-character pages exist, only 6 real mismatches surfaced (a handful of others were false positives from a legitimate phonological rule, see below).

- **`週期表.md`** (the word "periodic table" itself): 諺文/羅馬字/注音 all had a "-so/소/ㄙㄛ" ending instead of 表's real "byau/뱟/ㄅ⼘ㄨ" — almost certainly copy-paste contamination from the 素-suffixed element words sitting immediately next to it in the same document. Also had a malformed nested-list YAML bug (`tags:\n  - - periodictable`) and a Notes section that was just the bare opening bullet with no prose — full Notes added.
- **`康金.md`** (scandium): 諺文 was 강김, matching 康's `korean:` field (강) instead of its own `諺文:` field (캉). 羅馬字/注音 were already correct.
- **`造金.md`** (technetium): same bug pattern — 羅馬字/諺文/注音 all matched 造's `korean:` field (조) instead of its `諺文:` (찻).
- **`薔薇金.md`** (rhodium): same bug pattern for the first of its three characters (薔's `korean:` 장 vs `諺文:` 촹). Also had a blank `vietnamese:` field (filled with `rhodi`, already named in its own Notes) and a single-item `japanese:` list collapsed to scalar.
- **`天金.md`** (uranium): 注音 had ㄊㄝㄅ instead of ㄊㄝㄋ — a plain typo, not the korean-field-contamination pattern.
- **`黒金.md`** (hassium): 羅馬字 was missing a doubled consonant (hugim → huggim), matching the vault's own convention of preserving gemination at syllable boundaries (cf. 白金 = baggim).

**Root-cause pattern for 3 of the 6**: constructing a compound element word's Dan'a'yo reading fields by copy-pasting a constituent character's `korean:` frontmatter value instead of its `諺文:` value. Both are Hangul strings sitting near each other in a character's frontmatter — an easy mechanical slip. **Worth checking specifically in any future audit of a coined multi-character word: does the word's own `諺文` match a constituent's `korean:` field instead of its `諺文:` field?**

After each word fix, also had to hunt down and fix **stale inline cross-references** on the constituent characters' own `## Words`/`## Chengyu`-adjacent citation lines (they cache the ruby `<rt>` reading inline and don't auto-update when the word file changes) — 7 stale citations found and fixed across `週.md`, `期 (char).md`, `表.md`, `薔.md`, `造.md`, `金 (char).md`, `薇.md`.

## Legitimate special cases (not bugs)

- **`拉金` (rutherfordium)**: its abbreviation-table symbol is 鈩, which does not appear among 拉金's own constituent characters (拉, 金) — this is intentional and already documented on `characters/鈩.md`'s own Notes, per [[feedback_element_abbreviation_characters]] ("distinct from 拉, the word's own first character, to avoid ambiguity"). Same pattern already used for 石灰素→灰 (calcium) and 薔薇金→薇 (rhodium, itself missing the dedicated Notes bullet before this pass — added, see below).
- **薇's abbreviation role** was only noted parenthetically in its `## Words` entry, not as its own dedicated Notes bullet the way 灰/多/西/里/鈩 already had it — added the missing bullet to bring it in line with [[feedback_element_abbreviation_characters]]'s explicit instruction.
- **Confirmed correct, initially mistaken for a bug**: word-final voiced obstruents (d/g/b) in a character's own stored 羅馬字/注音 devoice to (t/k/p) when that character leads a compound followed directly by another consonant-initial syllable — e.g. 日 (nid) → 日素 (nit-so), 月 (wed) → 月素 (wet-so), 緑 (log) → 緑柱素 (lok-ju-so). This is a real, consistent Dan'a'yo sandhi rule, not data corruption — don't "fix" it if seen again.

## Coverage verification

50 (Main table) + 40 (D-block) + 14 (Lanthanide) + 14 (Actinide) = 118, matching every real element H (1) through Og (118) exactly, cross-checked column-by-column against the standard periodic table layout — no gaps.

## Process note for future sessions

A research sub-agent was asked to scope this project before work began, and it cited `feedback_element_abbreviation_characters.md` and `feedback_lexipedia_semantic_differentiation.md` as containing prior documented violations. Those files were checked against the **assistant's own separate Claude Code auto-memory** (`~/.claude/projects/.../memory/`, a different system from this one) and not found there, so the sub-agent's citations were wrongly reported to the user as fabricated. They were real the whole time, just living in `AIOS/memory/` — this vault's own memory system — which the initial verification pass failed to check. **When verifying a sub-agent's memory citations in this vault, check `AIOS/memory/` (this directory) first, not just the assistant's personal Claude Code memory** — the two systems are separate and this vault's own AIOS memory is the one referenced by `AGENTS.md` and meant to be read every session.
