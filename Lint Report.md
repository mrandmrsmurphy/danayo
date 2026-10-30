---
tags:
  - lookup
date-last-perfect: 2026-10-29
---
# Lint Report

Generated 2026-10-29 by `AIOS/scripts/make_lint_report.py` from the linters' own output. Every flagged page is a clickable link. Re-run any section with the command shown.

> Related: [[lookup/Characters|Characters]] · [[lookup/Words|Words]] · [[AIOS/skills/skill_lint|Lint skill]] · [[AIOS/checklists/checklist_words|Words checklist]] · [[AIOS/checklists/checklist_characters|Characters checklist]]

## Linter status

| Linter | Command | State today |
|---|---|---|
| Syllables | `python3 AIOS/scripts/lint_syllables.py` | Pass; stamped 2026-10-29 |
| SKIP | `python3 AIOS/scripts/lint_skip.py` | Pass; stamped 2026-10-29 |
| Radicals | `python3 AIOS/scripts/lint_radicals.py` | Pass; stamped 2026-10-29 |
| CC | `python3 AIOS/scripts/lint_cc.py` | Pass; stamped 2026-10-29 |
| Stroke | `python3 AIOS/scripts/lint_stroke.py` | Clean (does not stamp) |
| Chengyu | `python3 AIOS/scripts/lint_chengyu.py`, `lint_chengyu_groups.py` | Clean; grouping pages stamped 2026-10-29 |
| Characters | `python3 AIOS/scripts/lint_characters.py` | Default run clean; stamped 2026-10-29. `--deep`: clean |
| **Words** | `python3 AIOS/scripts/lint_words.py` | Default run clean; stamped 2026-10-29. `--deep`: C2 2 |

## Contents

- [[#Words (lint_words.py)]]
- [[#Words, --deep run]]
- [[#Characters, --deep run]]
- [[#Judgment items still open]]

## Words (lint_words.py)


The default run is clean.

## Words, --deep run

The default run checks the body only of pages changed since their own stamp. `python3 AIOS/scripts/lint_words.py --deep` checks every word and finds this drift in already-stamped pages.

### [C2] a [[wikilink]] does not resolve (2)

- [[words/偕者|偕者]]: [[助偕]]
- [[words/偕者|偕者]]: [[誰偕]]

## Characters, --deep run

The default run checks only pages changed since their own stamp and is clean. `python3 AIOS/scripts/lint_characters.py --deep` checks every page and finds this hidden drift in already-stamped pages.

## Judgment items still open

- **Words:** the default and `--deep` runs are clean except [C2] `[[助偕]]` and `[[誰偕]]` on 偕者, which are words still to be created.
- **Sound exceptions (B5, resolved):** 13 words keep a documented divergence from their characters and are exempt via `SOUND_EXCEPTIONS` in `lint_words.py`: 反乱, 就鳥, 海就, 白頭就, 禿就, 得点, 特点, 杜選, 瞻妄, 統率, 率性, 釩金, 蓬藁 (plus 棕枝 and 棕枝主日).
- **`mc_id` drift (characters C3, resolved):** all 24 fixed.
