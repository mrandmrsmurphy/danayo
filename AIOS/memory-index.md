# Memory Index

Standing memories about 武明帥 and how to collaborate with him on this vault: who he is, his preferences, corrections he's given, and pointers to external systems. Read this at the start of every session — see the Persistence section in `CLAUDE.md`.

**For who 武明帥 is and how he likes to work, start with [[AIOS/me.md|me.md]]** (the canonical profile, at the AIOS root — read it at the start of every session alongside this index).

For step-by-step workflow guides, see `AIOS/skill-index.md`. For ongoing project status, see `AIOS/projects.md`.

## Feedback
- [Character Notes format](memory/feedback_character_notes_format.md) — syllable link only on bullet 3, `(char)` suffix rules, blank `mc_id` when not in CC corpus
- [Character inclusion philosophy](memory/feedback_character_inclusion_philosophy.md) — when to alias a marginal character onto its phonetic parent vs. give it its own entry vs. mark it `名専字`; the "no recourse" argument for 名 grade
- [English field format](memory/feedback_english_field_format.md) — `english` must be a YAML list, never semicolon-separated (breaks Bases queries)
- [Date era format](memory/feedback_date_era.md) — always BC/AD, never BCE/CE
- [Notes style: encyclopedic](memory/feedback_notes_style.md) — word Notes should be multi-paragraph: etymology, history, cross-linguistic comparison, semantic drift
- [Obsidian CLI usage](memory/feedback_obsidian_cli.md) — use `obsidian properties`/`property:read` for lookups; grep only for 注音 searches and file discovery
- [Stand-in note on word pages](memory/feedback_standin_note.md) — explicitly flag when a word legitimizes a bound character
- [Stroke/Radical link zero-padding](memory/feedback_stroke_link_format.md) — `Stroke 02` (2-digit), `Radical 085` (3-digit), never unpadded
- [Syllable completion on word creation](memory/feedback_syllable_completion.md) — unblocking a syllable means finishing its page in the same pass (ruby + date-last-perfect)
- [Syllable data-check bug](memory/feedback_syllable_datacheck.md) — broken `WHERE 諺文` queries hide characters; always cross-check by grepping 注音
- [Session pacing](memory/feedback_session_pacing.md) — pause autonomous batch work at natural set boundaries (e.g. a completed syllable), not just at the end of the whole backlog
- [Word pronunciation derivation](memory/feedback_word_pronunciation_derivation.md) — 羅馬字/諺文/注音 = direct concatenation of `characters/` bound-form values; no sound-shift rules exist, don't derive from other (possibly unperfected) word pages
- [Idiom-component attestation](memory/feedback_idiom_component_attestation.md) — before calling a 2-char candidate "unattested," check if it's the head of a longer idiom, and check Japanese dictionaries independently (don't assume from a Chinese-only check)
- [Conlang-original coinages](memory/feedback_conlang_original_coinages.md) — "unattested in real-world CJKV" isn't automatic grounds to skip; some terms are intentional Dan'a'yo-original coinages (`origin: 単亜語`) — flag and ask, don't silently unlink
- [Variant character check](memory/feedback_variant_character_check.md) — before calling a character "missing," grep existing characters' `aliases:` for shinjitai/traditional variants (e.g. 氷/冰) before assuming a new character is needed
- [No redundant combined entries](memory/feedback_no_redundant_combined_entries.md) — before creating an N-character word, check if it's just two already-real shorter words composed transparently; if so link `[[A]][[B]]`, don't make a third entry
- [Japan-rooted concept pedigree](memory/feedback_japan_rooted_concept_pedigree.md) — a Japan-rooted concept can still pass "more than Japanese pedigree" if another CJKV language reads the same characters natively (e.g. 猿楽); contrast with true Japan-only cases like 伊吹
- [Graphemic substitution words](memory/feedback_graphemic_substitution_words.md) — 借代字 words (e.g. 且爵 for 咀嚼): foreign-language fields carry the real target word's readings, 羅馬字/諺文/注音 are mechanical from the substitute characters
- [Variant word check](memory/feedback_variant_word_check.md) — before creating a word, grep `words/` for the same compound spelled with a character alias (shinjitai/traditional) — don't duplicate an existing word under a different spelling

## Reference
- [conlang.org wiki](memory/reference_conlang_wiki.md) — legacy MediaWiki site being migrated into the vault; self-signed cert, use curl not WebFetch
