# Memory Index

Standing memories about Robert and how to collaborate with him on this vault: who he is, his preferences, corrections he's given, and pointers to external systems. Read this at the start of every session — see the Persistence section in `CLAUDE.md`.

For step-by-step workflow guides, see `AIOS/skill-index.md`. For ongoing project status, see `AIOS/projects.md`.

## User
- [User profile](memory/user_profile.md) — who Robert is, his interests (historical phonology, comparative CJKV etymology), and working style

## Feedback
- [Character Notes format](memory/feedback_character_notes_format.md) — syllable link only on bullet 3, `(char)` suffix rules, blank `mc_id` when not in CC corpus
- [English field format](memory/feedback_english_field_format.md) — `english` must be a YAML list, never semicolon-separated (breaks Bases queries)
- [Date era format](memory/feedback_date_era.md) — always BC/AD, never BCE/CE
- [Notes style: encyclopedic](memory/feedback_notes_style.md) — word Notes should be multi-paragraph: etymology, history, cross-linguistic comparison, semantic drift
- [Obsidian CLI usage](memory/feedback_obsidian_cli.md) — use `obsidian properties`/`property:read` for lookups; grep only for 注音 searches and file discovery
- [Stand-in note on word pages](memory/feedback_standin_note.md) — explicitly flag when a word legitimizes a bound character
- [Stroke/Radical link zero-padding](memory/feedback_stroke_link_format.md) — `Stroke 02` (2-digit), `Radical 085` (3-digit), never unpadded
- [Syllable completion on word creation](memory/feedback_syllable_completion.md) — unblocking a syllable means finishing its page in the same pass (ruby + date-last-perfect)
- [Syllable data-check bug](memory/feedback_syllable_datacheck.md) — broken `WHERE 諺文` queries hide characters; always cross-check by grepping 注音
- [Session pacing](memory/feedback_session_pacing.md) — pause autonomous batch work at natural set boundaries (e.g. a completed syllable), not just at the end of the whole backlog

## Reference
- [conlang.org wiki](memory/reference_conlang_wiki.md) — legacy MediaWiki site being migrated into the vault; self-signed cert, use curl not WebFetch
