# Checklist Index

Completion rubrics for each content type in the vault — the "date-last-perfect" spec for what a fully correct page of that kind looks like. Formerly the vault's "BP" (best practice) pages; moved here because their actual audience is AI checking pages against them, not a human browsing Obsidian — none of the vault's actual content (templates, nav files, character/word/chengyu pages) links to them. The one exception is `lexipedia/Lexipedia.md`, which points authors at [[AIOS/checklists/checklist_lexipedia.md]] before they create or expand a domain page (moved here 2026-09-18 from `lexipedia/format.md`, which had been living as vault content despite being a how-to-validate page, not a lexipedia page itself). Read the relevant checklist in full before perfecting or auditing that kind of page.

Distinct from `AIOS/skills/` (how to *create* something) — checklists are how to judge whether something that already exists is *complete*.

- [[AIOS/checklists/checklist_characters.md|Characters]] — frontmatter, four-bullet Notes structure, Words/Chengyu sections, 10-point date-last-perfect criteria
- [[AIOS/checklists/checklist_words.md|Words]] — frontmatter, constituent character links, Bases queryability
- [[AIOS/checklists/checklist_chengyu.md|Chengyu]] — encyclopedic depth, origin/textual history, cross-CJKV pronunciation
- [[AIOS/checklists/checklist_syllables.md|Syllables]] — linking every character at that reading, identifying the stand-alone word
- [[AIOS/checklists/checklist_stroke.md|Stroke lookup pages]] — SKIP-grouped inventory per stroke count
- [[AIOS/checklists/checklist_skip.md|SKIP lookup pages]] — index vs. leaf file structure, SKIP-4's distinct layout
- [[AIOS/checklists/checklist_radicals.md|Radical lookup pages]] — stroke-grouped inventory per Kangxi radical
- [[AIOS/checklists/checklist_cc.md|CC initials/finals pages]] — outcome-grouped character inventory per Middle Chinese initial/final, exception diagnosis categories
- [[AIOS/checklists/checklist_lexipedia.md|Lexipedia domain pages]] — tiered vocabulary structure (A1–C1+), Semantic Range Notes, Dan'a'yo-specific divergence from source-language meaning

## On a future delinter

If a validation/linting tool for this vault ever gets built, these checklists are the intended source of truth for its rules — each one is already written as a checkable rubric (see each file's "date-last-perfect criteria" or equivalent section), not prose documentation. Keep that in mind when editing them: precision and unambiguous pass/fail criteria matter more than readability for a human audience.
