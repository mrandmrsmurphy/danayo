---
name: feedback-notes-prose-rules
description: What belongs and does not belong in word and character Notes prose — keep stand-in and dual-source notes, no kwin/no-homophone/sweep commentary, links must resolve
metadata:
  type: feedback
---

User rulings of 2026-10-21, given after a long perfecting loop had been stripping prose it judged to be "process commentary."

**Keep**
- **Stand-in / legitimizing note.** A word that is the `stand_in` of one of its constituent characters says so (see [[AIOS/memory/feedback_standin_note.md]]). This includes a single-character word that stands in for its own bound character. It is explanatory, not process commentary. Never delete it.
- **Dual-source confirmation.** A sentence that says a character's analysis or reading was confirmed in two sources (en.Wiktionary and zh.Wiktionary) is welcome on character pages. Keep it, and add it when it is true.

**Leave out**
- **`kwin` prose.** `kwin` is a bare boolean; verify the value but write no Notes sentence or paragraph explaining it. This supersedes the older short-kwin-paragraph rule in [[AIOS/memory/feedback_kwin_length.md]].
- **"No homophones" remarks.** The absence of a homophone callout already says it. Do not add (or keep) a sentence saying a word has no homophones. A real homophone still gets the `>[!warning] Homophones` callout, and nothing more in prose.
- **Sweep / session history.** "This sweep," "already perfected," "awaiting its own turn," "now fully cross-linked," "added reciprocal callouts," "root-cause fix," "corrected," "formerly," "previously missing" and similar changelog or process sentences. State the fact, not how it was found or fixed.

**Links must resolve.** A broken link is never acceptable. From inside `characters/`, `words/`, `chengyu/` etc. every relative link to another top-level folder needs the `../` prefix (`../lookup/...`, `../syllables/...`, `../characters/...`, `../words/...`, `../lexipedia/...`). Check the target file exists before stamping.

**Why:** The loop deleted stand-in notes and dual-source confirmations that the vault wants, left broken links in pages it stamped, and kept adding "no homophones" lines.

**How to apply:** Before stamping a page, read its Notes for the three categories above, and run a link check on every `](...)` and `[[...]]` target in the page.
