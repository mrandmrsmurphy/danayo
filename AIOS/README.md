---
name: AIOS-readme
description: What AIOS is and how the persistence system (memory, skills, checklists, projects) is structured. Read to understand where standing knowledge lives.
type: reference
---

**All durable memory lives inside this vault, in `AIOS/` ("AI Operating System") — never in external `~/.claude/projects/.../memory/` or `~/.kimi/.../` locations.**

That external location isn't backed up the way this git-tracked vault is, and isn't portable across machines — anything written there can be lost between sessions or left behind on a new one. `AIOS/` is the canonical home for everything meant to survive: standing knowledge of the user, feedback on collaboration style, ongoing-project status, and workflow skills.

Structure:
- **`AIOS/memory-index.md`** — index of standing memories: who the user is, feedback/corrections on how to work here, pointers to external systems. **Read this at the start of every session.**
- **`AIOS/memory/`** — individual files: `user_*.md` (who 武明帥 is, how he thinks), `feedback_*.md` (corrections and confirmations — lead with the rule, then `**Why:**` and `**How to apply:**`), `reference_*.md` (pointers to external systems)
- **`AIOS/skill-index.md`** — index of step-by-step workflow guides; read the relevant skill in full before starting that kind of work
- **`AIOS/skills/`** — individual `skill_*.md` guides (how to *create* something)
- **`AIOS/checklist-index.md`** — index of completion rubrics, one per content type; read the relevant checklist before perfecting or auditing that kind of page
- **`AIOS/checklists/`** — individual `checklist_*.md` rubrics (how to judge whether something that already exists is *complete* — the "date-last-perfect" spec)
- **`AIOS/projects.md`** — living status document for ongoing work; read at the start of every session to see what's active and where to resume
- **`AIOS/projects/`** — deeper history for individual projects, as `project_*.md` files linked from `projects.md`

When you discover something valuable for future sessions — architectural decisions, gotchas, corrections, project status changes — write it into the appropriate `AIOS/` file and index it. Don't wait to be asked, and don't wait for the session to end.
