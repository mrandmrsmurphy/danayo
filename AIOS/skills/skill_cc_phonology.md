# Skill: CC Initials/Finals Page Creation

How to build and perfect `lookup/CC/initials/聲 X.md` and `lookup/CC/finals/韻 X.md` pages — the pages documenting how a single Middle Chinese initial or final evolved into its Dan'a'yo outcome(s) across the character corpus. Distinct from `skill_character_creation.md` (how an individual character's own phonology is derived) — this is about summarizing what actually happened across every character that shares one MC initial or final.

---

## Page structure (both initials and finals)

```markdown
---
size: N
middle_chinese_initial: X   # or middle_chinese_final: X
date-last-perfect: DATE
tags: [lookup]
---
> [Classical Chinese](../Classical%20Chinese.md)
> **Initial/Final X** [evolved into Y | mostly evolved into Y, with ... | splits N ways]

## CJKV Evolution
[prose — see below]

## Characters
### In Use
- [outcome group]: <ruby>[[char]]<rt>注音</rt></ruby>, ...
- [outcome group 2]: ...

## Datacheck
​```base
... (canonical query, see below)
​```
```

`Classical Chinese.md` is NOT a manual index of every initial/final — it's a general-context page whose own `## Initials Check` / `## Finals Check` base queries pull the leaf pages dynamically by folder. No cross-reference step needed there.

### Datacheck query — always include the folder filter

The pre-existing stub pages for most initials/finals have a self-referential bug: the query has no `file.inFolder(...)` filter, so it matches the lookup page's *own* frontmatter (which also carries `middle_chinese_initial`/`middle_chinese_final`) in addition to every real character — inflating the apparent count by exactly 1. Always add:
```yaml
filters:
  and:
    - file.inFolder("characters")
    - middle_chinese_initial == "X"   # or middle_chinese_final
```
Found and fixed on nearly every page touched in the initials sweep (2026-07-09); `size` was wrong on the majority of pre-existing stub pages for this reason alone, before any real data corrections.

---

## Ground-truth-first methodology

Never trust the stub's stated `size`. Build ground truth mechanically every time:
```bash
grep -lE '^middle_chinese_initial: "?X"?$' characters/*.md | wc -l
```
(swap `middle_chinese_initial` for `middle_chinese_final` as needed). Compare against the stated `size` and correct it — corrections ranged from off-by-one to +26 (`聲 匣`: 148→174) to +42 (`聲 曉`: 64→106). Never assume a small or zero delta without checking.

For each matching character, extract its own `注音` (and `mandarin`/`cantonese`/`korean`/`middle_chinese_initial`/`middle_chinese_final` as needed) directly from its frontmatter — never trust a cross-file assumption.

---

## Grouping rule: initials pages vs. finals pages

**Initials pages** (`聲 X.md`): group characters by their **resulting Dan'a'yo initial letter** — the first bopomofo consonant letter in `注音` (ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄐㄑㄙㄏ), or `ø` for characters whose 注音 starts directly with a vowel/glide marker (null initial).

**Finals pages** (`韻 X.md`): group characters by their **resulting Dan'a'yo final** — i.e. `注音` with the initial letter (if any) stripped off. Two mistakes to avoid here, confirmed on `韻 屋三.md` (2026-07-10):

1. **Don't treat initial-driven glide spelling as a final-level fact.** A null/glide-MC-initial character (以/j, 影/ʔ, etc.) fuses its glide into a single bopomofo vowel-letter (e.g. ⼜ = "yu") the same way it does on its own initials page. If a character's only reason for a different-looking final spelling is that fusion, its real final is the plain form — fold it into the main group. Confirmed: 育/郁 (null initials) spell `uk` as `⼜ㄎ`, but that's not an alteration of the final — they belong with the regular `ㄨㄎ` group.
2. **Never include the initial letter in a final-group's label**, even when a character genuinely does show an exceptional final. A real consonant initial followed by an unexpected glide/final IS a genuine final-level fact worth its own group — but the label is just the final substring (e.g. `⼜ㄎ`), never initial+final concatenated (not `ㄙ⼜ㄎ`). Confirmed: 尗 (real initial 書/ɕ) genuinely inserts a glide in its final; group label is `⼜ㄎ`, matching the final itself.

**How to apply:** before finalizing a finals page's groups, check each non-majority entry's own `middle_chinese_initial`. Null/glide-type → the odd spelling is probably initial-driven, fold into the main group. Real consonant → the odd spelling is a genuine final-level exception, but strip the initial letter from the label regardless.

---

## Explaining minority outcomes: check ALL daughter languages, not just Mandarin

Before calling a minority-group character "unexplained" or "poll-only," pull `mandarin`, `cantonese`, `korean` (and `vietnamese` if present) and check whether *any* of them supports the outcome. Mandarin alone is not enough. Confirmed repeatedly across the initials sweep (2026-07-09): 定/錠 palatalize per Korean 정, not Mandarin/Cantonese; several 從 "exceptions" turned out to be plain aspirated Mandarin misread as unaspirated (`c-` is aspirated `/tsʰ/`, `z-` is unaspirated `/ts/` — don't eyeball pinyin letters, check the actual value); 就/聚 explained by Korean 취 alone. Only call something a genuine unexplained exception when *every* checked daughter language disagrees with the outcome.

---

## The vault's actual derivation rule (found 2026-07-10, in `文法 - 02音韻論.md` line 15)

*"單亜語音韻 is determined in two ways. In some cases it represents the average or mean value across the CJKV languages. In other cases, when no middle ground exists, it follows the principle of simplicity, choosing the sound easiest for human learners."*

This is why some initials/finals converge cleanly (daughter languages agree → average) and others fracture unpredictably by character (no agreement → arbitrary "simplicity" pick, often tracking whichever phonetic-family sibling was created first — the same "guessability" phenomenon documented throughout the initials sweep). **A clean split with no findable conditioning factor is not a research gap — it's this documented mechanism operating as designed.** Say so plainly rather than searching indefinitely for a rule that isn't there.

### Phonotactic constraints (same file, `分布の制限`, lines ~122–139) — mechanically checkable

- ㄉ, ㄊ, ㄑ, ㄐ cannot combine with a y-glide.
- ㄈ cannot take an **on-glide** (a medial glide between the initial and the vowel nucleus, e.g. a w- or y- glide immediately after ㄈ). Off-glides (a glide as part of the coda, after the vowel nucleus — the ㄧ in ㄈㄨㄧ, where ㄨ is the vowel and ㄧ closes the syllable) are unaffected and perfectly normal.
- w-glide (on-glide) only precedes ㄚ/ㄝ, and cannot co-occur with ㄋㄌㄅㄆㄇ.

Confirmed against real data: on `韻 尤`, 9 of the 12 "plain ㄨ" (no-glide) group members are ㄑ/ㄐ-initial — exactly the barred consonants. On `韻 屋三`, all 6 ㄈ-initial characters land on plain `uk`, zero exceptions. `韻 微合` initially looked like a counter-example (斐, 扉, 緋 = ㄈㄨㄧ) until re-parsed correctly: ㄨ there is the vowel nucleus with ㄧ as an off-glide coda, not an on-glide — so the rule holds. **Check this before calling a split "unexplained"** — it may just be phonotactics forcing specific initials out of an on-glide-final group. When checking, be careful to distinguish on-glide (medial, before the vowel) from off-glide (coda, after the vowel) — they look identical in bopomofo notation but only the on-glide is constrained.

### 合 (rounded) finals reliably take a w-glide — a free, ready-made rule

Checked every 開/合 pair in `文法 - 99韻図.md`'s own Vowels-table D column: every single 合 final's Dan'a'yo output contains a w-glide, every 開 counterpart doesn't. Held for all 9 pairs checked (泰開/泰合, 寒/桓, 曷/末, 刪開/刪合, 黠開/黠合, 歌/戈一合, 藥開/藥合), zero exceptions. **Cite this directly for any 合 final's CJKV Evolution prose** instead of re-deriving it from scratch.

### Division (等) predicts how much a final will fracture

一等 (division-1) finals converge cleanly: 東一 (all 46 → one group), 寒 (47 of 48 → one group, 1 singleton exception). 三等 (division-3) finals fracture: 尤 (114 → 4-way split), 陽開 (fractures into 4+ groups, some even changing the coda, not just the vowel). This tracks real historical linguistics — division-3 rimes are exactly where daughter languages independently diverge most (medial/palatalization splits differ by language), so there's less "middle ground" for the average-value rule to find. **Check a final's own name for its division/開合 status before starting a page — it sets expectations for how much splitting to expect.**

---

## Reference table coverage caveat

`文法 - 99韻図.md`'s Vowels table has **real M/C/J/K/V daughter-language data on only a handful of rows** (東一, 東三, 屋一, and any others since filled in) — the vast majority of its 160 rows have only the MC IPA and the Dan'a'yo (D) column. Don't expect a per-final CJKV cheat-sheet there; the character-by-character corpus check (pulling `mandarin`/`cantonese`/`korean` for the *minority/exception* characters only, not the whole roster) remains the real evidence source. The `92`–`96小冊子` (per-language phrasebook) files were checked and confirmed to have zero MC-correspondence content — not a source for this work.
