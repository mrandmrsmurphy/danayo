---
name: feedback-character-inclusion-philosophy
description: Rules of thumb for deciding whether a marginal character gets its own entry, becomes an alias on a phonetic parent, or qualifies for 名 (naming) grade
type: feedback
---

See also [[AIOS/memory/Character Inclusion Philosophy.md|Character Inclusion Philosophy]] for the full statistical rubric — grade-level thresholds, the 借代字 inclusion checklist, and the long-tail inclusion-pressure table. This memory captures the narrower judgment calls that came up in practice, which the rubric doesn't fully spell out.

**Alias as stand-in:** when a character is too narrow to justify a full entry but still needs "no recourse" coverage for names, add it as an alias on its phonetic parent rather than creating a new character file — provided the two are phonetically identical across all CJKV languages.

**Why:** keeps the database from bloating with near-duplicates while still giving every name-character a path into the system. The alias is cleanest when the parent is *both* phonetic and semantic source (寄 [布 ← 佈] is cleaner than 蒔 ← 時, where 時 is only phonetic, not semantic, parent of 蒔).

**How to apply:** before aliasing, confirm identical Dan'a'yo-relevant readings across Mandarin/Cantonese/Japanese/Korean/Vietnamese — examples: 蒔 (Jinmeiyō-only, 艹+時) → alias on 時; 佈 (traditional 布, names-only outside China, 亻+布) → alias on 布. See also [[feedback_session_pacing]]'s sibling project notes on alias judgment calls (legitimate aliasing requires both matching sound *and* a transparent meaning link — bad cases get reverted, e.g. 歇≠欠).

---

**The "no recourse" argument for 名 grade:** a character that appears in personal names across the CJKV sphere, with no substitutable form in Dan'a'yo, qualifies for `grade_level: 名` and `stand_in: 名専字` even when it fails ordinary vocabulary-grade criteria.

**Why:** Dan'a'yo needs to be able to render real names; a character can be indispensable for that purpose while being useless for general vocabulary. Korean Name-lookup presence is a direct signal that a character lives in this space.

**How to apply:** when a character fails HSK/Jōyō/vocabulary thresholds but turns up in the Korean Name lookup (or equivalent name indexes for other languages), default to 名 + `名専字` rather than excluding it.

---

**Semantic divergence across CJKV doesn't block 名 inclusion, only productive-vocabulary grades.** Example: 舅 means "maternal uncle" in Chinese/Vietnamese but "father-in-law" in Japanese — that mismatch disqualifies it from a shared-meaning vocabulary grade, but not from 名.

**Why:** 名-grade characters only need to render correctly in names, where the semantic-drift problem doesn't arise the same way it would in shared vocabulary.

**How to apply:** don't let cross-linguistic meaning mismatches talk you out of a 名 entry — check separately whether the *naming* use case is solid.

---

**Lopsided language presence (strong in some branches, absent in others) argues for 名 over 先進**, even when the character's HSK level looks low. Example: 址 has strong Chinese/Vietnamese presence but no real Japanese/Korean vocabulary footprint.

**Why:** 先進 (advanced vocabulary) implies the character pulls its weight across the whole CJKV sphere; a character that's productive in only two of the five branches is better classified by its narrower (naming) role.

**How to apply:** when assessing grade, weigh cross-linguistic *breadth* of vocabulary use, not just the strength of presence in any single language's frequency lists.

---

**Naming the long-tail problem itself: 舎本逐末 as the warning, [[保頭断尾]] as the remedy.** As the database approaches the statistical "long tail" — the point where nearly every remaining gap is a marginal, low-frequency character — 武明帥 named the failure mode and its fix as a matched pair of chengyu: [[舎本逐末]] ("neglecting the fundamentals while chasing the trivial," an extant classical idiom, Dan'a'yo-spelled with shinjitai 舎/末 per [[覧昭和決]]) names what NOT to do — burning effort on marginal completism at the expense of the productive core; [[保頭断尾]] ("guard the core, prune the periphery," coined 2026-06-08 as a Dan'a'yo-original chengyu) names the actionable remedy — protect and keep investing in the ~3000-character core chosen for centrality/ubiquity/utility, and don't hesitate to alias, consolidate, or prune the marginal remainder rather than minting full entries for it.

**Why:** every individual aliasing call (淘→陶, 鷲→就, 瘠→脊...) was being made ad hoc on its own merits; naming the pattern turns a string of one-off judgment calls into a single invokable principle, and gives the failure mode it guards against a name too — so both the temptation (chase every last rare character) and the discipline (guard the head, cut the tail) are now nameable in-world, in Dan'a'yo's own voice.

**保頭断尾 also covers the "don't even mint the character" case, via 借代字 substitution rather than character aliasing.** Example: 糠's stand-in word needed a partner character (秕/粃, "blighted grain") that would anchor only that single compound. Rather than creating 秕 as a full character (or aliasing it onto anything), the word was spelled [[比糠]] — using 比 (already a core, unrelated-in-meaning character) as a pure phonetic/graphemic substitute, since 比 is literally 秕's own phonetic component (形声: 禾 + 比) and near-identical in reading across Mandarin/Cantonese/Korean. This is the `borrowed/substitute character` (`借代字`) mechanism from [[feedback_graphemic_substitution_words]] (precedent: 且爵 for 咀嚼), not the semantic-alias mechanism (precedent: 蒔→時) — the substitute need not carry any meaning relationship, only sound.

**How to apply:** when a would-be new character fails 保頭断尾's "few to one word" test *and* has no clean semantic-alias parent (no existing character shares both its sound and a transparent meaning link), check whether its own phonetic component is already a vault character — if so, prefer 借代字 substitution over minting the marginal character, and use the substitution word to simultaneously serve as the stand-in for whichever other character actually needed legitimizing.

---

**Real-world attested orthographic variants pre-empt creation entirely — check for them before even reaching for 借代字 substitution.** Example: 兢 (bound only in 戰戰兢兢 and 兢兢業業, Hyōgai, no clean vault phonology precedent for its k+ɨŋ rhyme) was rejected outright, not aliased, because both idioms it would anchor already have *attested real dictionary variants* substituting a different character for the same sound: 戦戦恐恐 (confirmed interchangeable with 戦々兢々 across multiple Japanese dictionaries) already existed in the vault as the chengyu, built around the existing character [[恐]] — with [[恐]]'s own Words section already annotating "恐恐 ... (alias: 兢兢)" from a prior session. 兢兢業業 has its own attested classical variant 矜矜業業 (『三國志・王基傳』; 陳喬樅's 經説考: "兢、矜聲同").

**Why:** this is a stronger basis for skipping character creation than the borrowed/substitute-character (借代字) mechanism in [[feedback_graphemic_substitution_words]] — that mechanism uses an *unrelated* existing character purely for its sound (且 for 咀, 比 for 秕/粃), a Dan'a'yo-internal workaround. Here, real-world Chinese/Japanese sources *already* treat the two characters as interchangeable in that exact phrase, independent of anything Dan'a'yo needs — so the "substitution" isn't a conlang workaround at all, it's just recording which attested spelling the vault picked.

**How to apply:** before creating a character whose only use is inside one or two idioms, search for attested variant spellings of those idioms (WebSearch `"<idiom>" 異体字 OR 同義語 OR 同義表記`, or check if a classical source already glosses the two characters as phonetically/graphemically equivalent, e.g. "X、Y聲同"). If a variant exists using an already-vault character, prefer spelling the idiom that way and skip creating the character — don't even reach for 借代字 first.

---

**How to apply:** 保頭断尾's own `## Invocation` section spells out the trigger precisely — *"When a character is proposed and it has few to one word across CJKV where it is needed, it is time to invoke this chengyu and make that character an alias of something close, a 代用字."* Treat that as the operative test: a proposed character that would anchor at most one or two words, especially if its main use is names, is a 保頭断尾 candidate for aliasing onto a close phonetic/semantic parent rather than a full entry — exactly the move already made for 瘠→脊, 淘→陶, and 鷲→就, each cited in [[保頭断尾]]'s own Source and Origin section as "保頭断尾 in practice, before the principle had a name." Reach for [[舎本逐末]] when explaining *why* completism is the wrong instinct here, and for [[保頭断尾]] when deciding *what to do instead*.
