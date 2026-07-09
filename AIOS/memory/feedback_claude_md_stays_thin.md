---
name: feedback_claude_md_stays_thin
description: CLAUDE.md must stay a thin redirect index — new reference content goes into AIOS/, not inline in CLAUDE.md.
type: feedback
---

CLAUDE.md is a redirect-only index (`see [[here]], see [[there]]`), not a place to grow real reference content. When something new needs documenting — a new content type, a new convention, a new workflow — it gets its own file (or a section in an existing one) under `AIOS/`, and CLAUDE.md gets at most a one-line pointer to it.

**Why:** CLAUDE.md had drifted from this model — data model, frontmatter schemas, ruby-text syntax, plugin setup, and the full AIOS persistence explanation had all accumulated inline (105 lines), duplicating/competing with the AIOS/ index files. Restored on 2026-07-08 by moving that content into [[AIOS/vault-structure.md]] (vault structure/setup/frontmatter/conventions) and [[AIOS/README.md]] (what AIOS is), leaving CLAUDE.md at 15 lines of links.

**How to apply:** Before adding anything to CLAUDE.md beyond a link, ask whether it belongs in `AIOS/vault-structure.md` (vault mechanics: data model, frontmatter, conventions, plugins), `AIOS/README.md` (how the AIOS system itself works), or a new dedicated AIOS file — then link to it instead of inlining.
