---
name: project-lexipedia-numbers
description: "Closed 2026-09-17 - Numbers lexipedia page audited, all existing words linked, 14 new Math-domain words coined and cross-linked"
type: project
---

**Status: closed.** `lexipedia/Numbers.md` (a page following Mark Rosenfelder's *Conlanger's Lexipedia* topic-list structure — numbered cardinal/quantity items 1–28, then a `## Math` section of freestanding bullets) audited against existing vault vocabulary and filled in. Given a `date-last-perfect` field, matching the treatment already established for `lexipedia/Periodic Table.md` — no formal lexipedia checklist exists yet (see that project's own note on this), but stamping is reasonable once a page is genuinely complete.

## Numbered list (items 1–28): already solid

Every markdown-link and wikilink entry in the cardinal/ordinal/quantity list already pointed to a real, perfected word file — full sweep confirmed. Two items were genuinely wrong fits, both fixed:
- **Item 20, "dozen"**: was a bare unlinked `打数??` placeholder. Created **[[一打]]** ("a dozen"), documenting a genuine triple-loan situation: Mandarin/Cantonese 打 (dǎ) is a *phonetic* loan of English "dozen" (unrelated to 打's ordinary "hit" sense, same pattern as 苏打 "soda"/西打 "cider"), while Japanese/Korean instead borrow the English word directly (ダース/다스, the latter via Japanese) rather than following the Chinese loan. Vietnamese has no attested compositional or loan form at all (uses native *một tá*) — left blank rather than fabricated.
- **Item 27, "twice"**: was linked to **[[再度]]**, which only means "again, once more" — no specific count, not a genuine match for "exactly two times." Created **[[二度]]** ("twice") and relinked; 再度 stays valid where it already was, just no longer misapplied here.

## Math section: nearly the whole thing was unlinked

The `## Math` section (add/subtract/multiply/divide/equal/odd/even/number/real/complex/whole/fraction/negative/exponent/infinity/logarithm/sine/cosine/tangent/integrate/differentiate) had only 6 of ~20 items linked at the start. Filled in:

**Already-existing words linked in** (found via `words/` search, not previously connected to this page): [[加算]] (add), [[減算]] (subtract), [[乗算]] (multiply), [[奇数]] (odd), [[偶数]] (even), [[数字]] (number).

**A real semantic-fit bug caught and avoided**: [[同等]] looked like an obvious candidate for "equal," but its own Notes explicitly rule this out — "not a general word for equality," specifically a rank/status-parity term (contrasted there with 平等 and 対等). Created [[相等]] instead, the genuine mathematical-equality term, rather than mislinking a word that documents its own unsuitability.

**14 new words coined** (all real, independently-attested CJKV mathematical/scientific compounds — none fabricated), each following the vault's full word-perfection standard (frontmatter, etymology-linking Notes, cross-linguistic verification via WebSearch/hvdic, `kwin` computed from each constituent's own stored reading, backlinked on every constituent character's own `## Words` section):

- **[[除法]]** / **[[除算]]** (division, noun/verb pair) — the standout find: [[乗法]]'s own pre-existing Notes already said "parallel to 加法, 減法, and 除法" as if 除法 existed, but it didn't. This vault has a deliberate, well-established X法/X算 parallel system for all four arithmetic operations (法 = "the method," Mandarin/Cantonese register; 算 = "to calculate," Japanese/Korean register) — 加法/減法/乗法 and 加算/減算/乗算 all existed; division was the one gap in an otherwise-complete 4×2 grid.
- **[[整数]]** (whole number/integer), **[[分数]]** (fraction), **[[指数]]** (exponent), **[[積分]]** (integrate), **[[微分]]** (differentiate) — all standard, fully compositional, genuinely living terms across Mandarin/Cantonese/Japanese/Korean/Vietnamese, no register split.
- **[[負数]]** (negative number) — Korean does **not** follow the compositional 負數 pattern here (that would collide with 부수, "Kangxi radical" = 部首); Korean instead uses 음수 (陰數, "yin number"), and Vietnamese independently uses the same yin-based logic (số âm) rather than a 負-based calque. Both filled with the real attested terms, not compositional guesses, per this vault's cross-linguistic-field convention.
- **[[実数]]** (real number) — flagged a genuine Korean-internal homophone: 실수 (實數, "real number") is a perfect homophone of 실수 (失手, "mistake"), independently confirmed, disambiguated only by context — same shape of collision as [[計数]]'s documented 계수 case.
- **[[複素数]]** (complex number) — the most interesting case. Mandarin/Cantonese genuinely use 複數/复数 for *both* "plural" (grammar) and "complex number" (math), disambiguated only by context. This vault's own [[複数]] already claims the grammatical sense, so reusing it for math would create a real Dan'a'yo-internal collision. Japanese and Korean independently solved the identical problem by inserting 素 ("element") — 複素数/복소수 — and Dan'a'yo follows their solution rather than Mandarin's ambiguous one, for the same underlying reason they did.
- **[[対数]]** (logarithm) — Vietnamese has no Sino-Vietnamese compound at all; the real, only-attested term is the French loanword lôgarit. Caught and avoided a near-miss: 対数's own characters would compositionally read "đối số," which **is** real Vietnamese — but means "argument" (the input to a logarithm), a different concept entirely. Documented explicitly so a future pass doesn't wrongly "fix" the field to that plausible-looking but wrong compositional form.
- **[[相等]]** (equal, mathematical sense) — real term in Mandarin/Japanese/Korean; flagged its own Japanese-internal homophone risk (そうとう also reads the unrelated [[相当]], "considerable"). Vietnamese tương đẳng is independently attested as real Vietnamese math/geometry vocabulary, though its precise sense leans toward "congruent" rather than bare equality — close enough, and built on the exact same pattern as [[同等]]'s own đồng đẳng.
- **[[一打]]** (dozen) and **[[二度]]** (twice) — see numbered-list section above.

## Character-level fixes made in passing

Two Vietnamese-field bugs found via the standard "always re-verify against hvdic before trusting a character's own stored field" check: `characters/除.md` was missing its own primary Hán Việt reading (trừ) entirely, listing only secondary Nôm variants; `characters/整 (char).md` had the same gap (missing chỉnh). Both fixed. One minor structural fix: `characters/打.md` had a missing blank line between `## Words` and `## Chengyu`.

## Method note for future lexipedia work

This page is a Rosenfelder-style topic list (numbered items = the book's own word list for the domain), distinct from the tiered-vocabulary `lexipedia/format.md` template used for domain pages like Kinship/Animals. When auditing a Rosenfelder-style list: (1) check every existing link resolves and matches its target word's own actual sense (don't trust a plausible-looking existing link — [[同等]]/"equal" would have been wrong), (2) grep `words/` broadly for the real CJKV term of each unlinked concept before assuming a gap needs new coinage, (3) when coining is genuinely needed, verify each candidate compound is a real, attested term in at least one source language (not an invented compositional guess) unless the vault's established practice for that domain explicitly allows original coinage, (4) watch for Dan'a'yo-internal collisions with already-existing words (the 複数/複素数 case) — check `words/` for the plain compositional form before adopting it if a semantically related word might already claim it.
