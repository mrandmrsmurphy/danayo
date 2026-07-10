# Skill Index

Step-by-step workflow guides for the complex, multi-source tasks in this vault. These are operational playbooks — read the relevant one in full before starting that kind of work, rather than relying on a one-line summary.

- [Word creation](skills/skill_word_creation.md) — full process for creating `/words/` files: pre-flight checklist, frontmatter field sources, linter behavior, body structure, stand-in handling, gotchas (羅馬字 apostrophes, 注音 junctions, special Japanese readings, Vietnamese sourcing, duplicate-checking)
- [Character creation](skills/skill_character_creation.md) — full process for creating `/characters/` files: phonology derivation from Middle Chinese, field sources (SKIP, mc_id, danayo_id, stand_in decision table), Notes bullet format, `date-last-perfect` criteria
- [MediaWiki migration](skills/skill_mediawiki_migration.md) — checklist for comparing conlang.org wiki pages against vault files, what to import vs. leave alone, POS mapping table
- [Lint](skills/skill_lint.md) — argument-driven bulk-consistency sweep over one content type at a time (`lint SKIP`, `lint CC`, etc.); ground-truth-first, leaves-before-stems, forked-batch execution
- [CC initials/finals](skills/skill_cc_phonology.md) — building `聲 X.md`/`韻 X.md` pages: grouping rules, ground-truth methodology, the vault's actual average-vs-simplicity derivation rule, phonotactic constraints, and the 合→w-glide/division-predicts-fracture patterns
