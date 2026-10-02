---
name: feedback-affix-naming-and-productivity
description: Productive/semi-productive affix policy — `－X.md` word files (fullwidth hyphen U+FF0D) mark fully productive affixes; every word with a fullwidth hyphen in its name gets the ASCII `-` form as an alias
type: feedback
---

**Rule 1 — fullwidth-hyphen words get an ASCII alias.** Any word file whose name contains the fullwidth hyphen-minus `－` (U+FF0D) must carry an `aliases:` entry with the ASCII `-` version (`－化.md` → `aliases: ["-化"]`). Quote it — a bare leading `-` is YAML-hostile.

**Why:** the user chose `－` over ASCII `-` (shell tools read a leading ASCII `-` as a flag; `－` also fits CJK width). But `－`, `ー` (U+30FC), `−` (U+2212) and `-` are visually near-identical, and NFKC folds `－` to `-`, so the ASCII alias keeps lookups, search and typing-by-hand working.

**How to apply:** when creating or perfecting any `－X.md` / `X－.md`, add the alias; lint with `git ls-files words | grep '－'` and check each has it.

**Rule 2 — two productivity tiers, encoded structurally (no frontmatter property):**
- **Fully productive** = a word file named `－X.md` (suffix, hyphen leads) or `X－.md` (prefix, hyphen trails; not yet applied to any prefix). Any transparent `stem + affix` is valid Dan'a'yo without its own file; a derivative gets a file only if lexicalized/non-compositional (文化, 化学) or it needs notes/Lexipedia placement. The character stays bound-only, so it keeps the plain `X.md` name (no `(char)` — that suffix exists only to avoid a collision with a standalone word `X.md`).
- **Semi-productive** = no affix word file; a standard note on the character page says so (as 子 has). No *new* coinage using it without authority review; every derivative needs its own file. Productive in ≥1 source language, now or historically.

**Bar for full:** simple majority — productive in ≥3 of the 5 source languages with a clear transparent meaning. The user reserves the right to grant full status by fiat so Dan'a'yo stays speakable; no such cases yet.

**Current tiers (2026-10-02):** full — 化 (-ification), 者 (-er/-ist), 論 ("theory of"), 文 (patterned/written form of X: 天文, 英文, 疑問文), 性 ("nature"). Semi — 的 (conflicts with Dan'a'yo TI), 語, 音, 学, 家, 子, 表, 法; 式 treated as semi pending a call.

**Status (2026-10-02):** migration done. `words/－化.md`, `－者.md`, `－論.md`, `－文.md`, `－性.md` exist (each aliased to its ASCII form); `化`/`者` characters reverted to plain `X.md` (no `(char)`), `論`/`文`/`性` always were. Obsidian resolves `[[－化]]` (user-verified on 火 and 化 — the NFKC fear did not materialize). Listed under "productive suffix" in `lexipedia/Grammar.md`. Bound-only characters keep a compound `stand_in` (化→変化, 者→学者, 論→理論, 文→文化, 性→性別), never the affix word.

**Not done yet:** (1) the standard "semi-productive" note on the character pages for 的, 語, 音, 学, 家, 表, 式, 法 (子 already has one); (2) prefix convention `X－.md` for 非/無/不/超 etc. is decided in principle but applied to none; (3) the grammar chapter `文法 - 97品詞` already classifies grammatical suffixes (者, 被, 物, 事, 只, 且, 公, plus 等/然/之 in lexipedia/Grammar) as `関詞`; whether those get `－X` treatment is undecided — 者 already has it, the rest do not. Note the existing `接辞` and `接尾辞` words ('affix', 'suffix'); (4) `音韻論`-page red links for semi-productive coinages (-音, -語, -的) still need an authority-review decision each.

Related: [[feedback-word-alias-no-real-word]] — the ASCII alias is not a real word, so it doesn't violate that rule.
