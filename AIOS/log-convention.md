---
name: log-convention
description: The vault's change log, Log/log.md — what it records, entry format, when to write it, and how it differs from page stamps, AIOS memory and project status.
type: reference
---

# Change log convention

The vault's change history is **`Log/log.md`**: one append-mostly file where every session records what it did to the vault's content and infrastructure, so the owner can audit a session without diffing files.

**Rule: history lives in the log and nowhere else.** Content pages hold only the current working state (this is also the "Document the current state" principle in [[Design Philosophy]]). Never write "corrected", "previously", "was wrong", "this sweep", or the date of a change on a content page. Fix the page silently and log the fix.

## Structure of `Log/log.md`

- Header: `# Log`, then one line saying changes are listed newest first and history lives here and nowhere else.
- One section per date, `## YYYY-MM-DD` (ISO, local timezone), **newest date first** — a new date goes immediately under the header, not at the bottom.
- Bullets under each date, **newest entries first within the day**.

## Rolling over

Standing rule (user, 2026-11-13): keep each log file to about 300 KB. When `Log/log.md` approaches that size, move the oldest whole date sections into an archive file beside it, named `Log/log YYYY-MM-DD to YYYY-MM-DD.md` (first and last date it holds, same newest-first order, a short header that points back to `Log/log.md`), and leave the newest dates in `Log/log.md`. Cut only at a date heading, never inside a day. Check the size (`ls -l Log`) at the start of any session that writes the log.

## Entry format

One bullet per logical change, not per file:

```markdown
- **Bold summary naming the pages and the authority:** what was done, in enough detail that the owner never needs to diff files to understand it.
```

1. **Bold summary first**, a clause: "Lexipedia Trade perfected", "New word 犯肉", "Typo fixes on Sensation".
2. **Name the authority.** `(user: …)` when the owner directed or decided the change, `[AI]` when the agent proposed the content. The log must be able to answer "which parts did a human decide?".
3. **Backtick vault-relative paths** for pages: `lexipedia/Trade`, `words/犯肉`.
4. **Report substance, not just actions**: name the words coined, the readings chosen, the rule applied, not "updated the page".
5. **Report verification**: the Wiktionary survey and the two-language rule for each coinage, lints run, claims checked; flag anything left unverified.
6. **Record what was not done**: deliberate omissions ("left alone: …", "not coined: …, needs a character the vault lacks") are part of the history. Say whether it was left alone deliberately or is not done yet.
7. **Mechanical fixes** the linters force (homophone callouts, `kwin` values, backlinks) are named briefly in the entry of the change that triggered them.

## When to log

In the same session as the change, as it happens or immediately after, never reconstructed at the end from memory:

- new words, characters, chengyu, syllables and lexipedia pages; deletions; renames and moves (with the alias that was kept)
- substantive edits to existing pages, including stale-prose rewrites
- typo and error fixes (silent on the page, still logged)
- changes to index pages, lookup lists, checklists, skills and project status
- infrastructure that affects the owner's workflow: new folders, renamed files, `AGENTS.md` and AIOS rule changes

Purely internal AI memory writes need no entry.

## Fixing mistakes

Fix a **verified** error in place with no marker on the page, and log it with enough detail to reconstruct it. If an error is **contested or a judgment call**, do not fix it: flag it for the owner and log that it was flagged. Preserve the owner's wording and decisions.

## How the log differs from the rest of AIOS

- `Log/log.md` — what happened to the vault's content. Permanent, human-facing, written every session that changes content.
- `AIOS/memory/` and [[AIOS/memory-index.md]] — how to work in this vault: conventions, feedback, standing facts.
- [[AIOS/projects.md]] — where ongoing work stands and where to resume.
- `date-last-perfect` on a page — the date a page last met its checklist. It is a stamp, not a history; the log says what was done and why.

Git commits (the vault commits itself on a timer) hold the files; the log holds the reasons and the authority.

## Failure modes

Logging at the bottom; vague entries ("updated several pages"); annotating a page instead of logging; copying log content into AIOS memory (one cross-reference is enough); batching entries at the end from memory.
