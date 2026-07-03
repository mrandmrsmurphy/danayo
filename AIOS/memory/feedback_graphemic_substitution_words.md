---
name: feedback_graphemic_substitution_words
description: 借代字 substitution words (legal characters standing in for obscure ones) carry the target word's real cross-linguistic readings, but the conlang's own romanization is mechanically derived from the substitute characters
metadata:
  type: feedback
---

Some character pages document a `### 借代字` ("borrowed/substitute character") note explaining that the character is being used to spell a different, obscure character's sound/role because the real character isn't in the Dan'a'yo set (e.g. [[爵]] aliased to 嚼, with 且 substituting for 咀, so that [[且爵]] stands in for the real word 咀嚼).

This differs from [[feedback_standin_note]] (a word legitimizing one of its own constituent characters) — here, *neither* surface character is the "real" character for the target word; both are substitutes for entirely different, vault-excluded characters.

**Why:** 武明帥 confirmed this when I flagged 且爵 as not itself attested in any real CJKV language: "This is a version of 咀嚼, which IS well-attested... We just don't want to create a bunch of new characters just for this word ... 且爵 is a kind of substitute for a well-documented word." The pedigree test applies to the real target word (咀嚼), not the substitute spelling.

**How to apply:**
- The `mandarin`/`cantonese`/`japanese`/`korean`/`vietnamese` fields should carry the *target* word's actual real-world readings (e.g. jǔjué/そしゃく/저작 for 咀嚼), not a mechanical reading of the substitute characters.
- The `羅馬字`/`諺文`/`注音` fields still follow the standard mechanical-concatenation rule ([[feedback_word_pronunciation_derivation]]), built from the substitute characters' own bound forms (e.g. 且's "co" + 爵's "jag" → cojag), since that's what's actually being written/read in Dan'a'yo.
- Add a Notes line explaining the substitution explicitly, naming the real target word and why the obscure character was avoided.
- **Add the substituted-for character(s) to the substitute character's own `aliases:` field**, even though they share no semantic link (e.g. `秕`/`粃` added to [[比]]'s aliases, despite 比 meaning "compare" and 秕/粃 meaning "blighted grain") — confirmed by 武明帥 for the 比/秕/粃 case. This differs from the ordinary aliases use (graphemic variants of one character, see [[feedback_character_inclusion_philosophy]]'s aliasing rules) — here the alias records "this vault-excluded character's role is filled by this one," not "these are the same character."
