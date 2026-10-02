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

**Part of speech (decided 2026-10-02): `派生辞` ("derivational affix").** Every `－X.md` / `X－.md` word has `pos: 派生辞`. The word page `words/派生辞.md` is a Dan'a'yo coinage on the model of 関詞. Rejected alternatives: reusing `接辞` (05形態 already uses it as the umbrella for *all* affixes, including TAM) and filing under `関詞` (function words; these affixes create new lexical items). `者` was moved out of 関詞/topic-retaining in `文法 - 97品詞` — it is 派生辞 now. 97品詞 group 4 "Derivational Affixes" lists the five; 05形態's intro points to it. 辞 not 詞 is deliberate (bound, not a free word); beware Mandarin 派生词 'derived word' = the product, not the affix.

**Design principle (user, 2026-10-02): affixes vs relational markers.** A 派生辞 derives a *new lexical item* and **stacks** (進化 → 進化論 → 進化論者); each step is constrained by what the affix attaches to and returns. Case markers (関詞, frame-forming) create no lexical item and **never stack — banned by the user 2026-10-02** ("case-stacking is very J/K, not even conceived of in C/V"). Rule as written in 05形態 §Adverbial Morphology and 97品詞: a noun phrase takes at most one 格助詞 and nothing attaches after it, including a second case particle or a restrictive/focus particle (只/且/就). The existing 05形態 examples already comply. This reading is deliberately broad (it also bans J/K-style case+focus combinations like には/에서는); narrow it only if the user says so.

**物 and 事 (done 2026-10-02):** both are free words *and* nominalizing affixes (05形態 §名詞化), so each has a separate affix page — `－物.md`, `－事.md` (pos 派生辞) — beside the free `物.md`/`事.md` (which stay 代詞/名詞). Their characters keep the `(char)` suffix because the free word still occupies `X.md`. Each free page carries an "Also a suffix" info callout. Moved out of 関詞/topic-retaining in 97品詞 into group 4. Full productivity here rests on the grammar's own nominalization system (a design requirement) as well as zh/ja/ko attestation — closer to the user's fiat clause than to the simple-majority rule. The same free-word-plus-affix pattern will recur (有/無/在/莫 as prefixes, 法 possibly).

**接頭辞 (coined 2026-10-02):** the category of *verbal prefixes* (動詞接頭辞): 有–/無– experiential, 在–/莫– progressive, plus 可– ability. It is also the general J/K word for "prefix". 97品詞 group 5 "Verbal Prefixes". The mood prefixes (可–, 不–, 不可–…) are still listed under Modifiers > Moods in 97品詞; whether they move into 接頭辞 is **undecided**. No prefix word pages exist yet (`有－.md` etc. would follow the trailing-hyphen convention); they would be free words with a separate affix page, like 物/事.

**Semi-productive notes (done 2026-10-02):** a `>[!info] Semi-productive affix` callout above the meta-bind-embed on the character pages of 子, 的, 語, 音, 学, 家, 表, 式, 法. (子 had *no* note before — the "standard" format did not exist until now.) Find them with `git grep -l "Semi-productive affix" -- characters`. Each states the meaning, that it is not a 派生辞, the no-new-coinage rule, and up to six existing derivatives. To promote an affix to fully productive, delete the callout and create its `－X.md` page.

**Not done yet:** (1) the other 関詞 suffixes (公, 被, 只, 且, 就, 等, 然) stay 関詞 and are not `－X` files — correct unless the user decides otherwise; (2) red links for semi-productive coinages on the 音韻論 page (-音, -語, -的) each need an authority-review decision; (3) 法 may need an affix page like 物/事 (callout says undecided); (4) the mood-prefix question above.

Related: [[feedback-word-alias-no-real-word]] — the ASCII alias is not a real word, so it doesn't violate that rule.
