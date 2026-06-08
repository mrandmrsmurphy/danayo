---
name: skill-character-creation
description: Step-by-step process for creating Dan'a'yo character files in /characters/, including all field sources, phonology derivation, Notes format, and decision rules
type: skill
---

# Skill: Character Creation

See `Character Creation.md` (vault root) for the full guide. This memory captures the operational details learned by doing it.

## Key points

- **Filename**: `X.md` by default; use `X (char).md` only when a word file with the same name exists (disambiguation). Characters with `stand_in: 名専字` never get the `(char)` suffix (no word file will ever share the name).
- **SKIP number**: always from EDRDG (`edrdg.org/cgi-bin/wwwjdic/wwwjdic?1MMJ<char>`), never calculated manually
- **Dan'a'yo phonology**: derived by finding a vault character with the same MC initial+final; when two matches exist with the same MC initial+final, the phonetic component determines which reading applies. A character whose phonetic component is already in the vault with the *same* MC initial+final very often shares its exact 注音/羅馬字/諺文 (e.g. 汐 ← 夕, both z+iᴇk → ㄙㄝㄎ/seg/석).
- **mc_id**: check vault's `lookup/CC/CC 3000.md` when Wiktionary doesn't list a CC frequency rank — the rank number there IS the mc_id. If absent from both Wiktionary and CC 3000 (i.e. outside the top ~3000 most-used Classical Chinese characters), leave `mc_id:` blank — guessing a rank is worse than leaving it empty (this also blocks `date-last-perfect`).
- **danayo_id**: increment from the highest current ID *within the character's grade level* — grep all character files for that `grade_level` and take max+1; don't guess, verify against the actual files.
- **stand_in decision**:
  - Character is independently meaningful, appears in multiple compounds → the character itself
  - Character only makes sense in one specific compound → that compound
  - Character appears only in proper names, or is being created specifically as a name character → `名専字`
- **Korean Name** lookup bullet is indexed by the initial consonant of the `korean` reading (e.g. 석 → ㅅ → `Korean Name ㅅ`)
- **Grade 先進** → link as `[Grade Advanced](lookup/Grade%20Advanced.md)`
- **vietnamese**: omit key entirely when absent from Wiktionary; a phonologically-derived guess is acceptable for obscure characters
- **date-last-perfect**: leave blank if any verifiable criterion is unmet — unresolved `[[component]]` links, missing `mc_id`, or a missing word file in `## Words` all block it
- **korean_native**: hard to source reliably from Wiktionary/Naver via tooling — prefer asking the user directly, or cross-checking multiple Korean dictionary search results for a consistent native gloss (e.g. 汐 → 조수 confirmed across several sources)
- **After creating a character**: always update the corresponding syllable page — add the new character under the correct grade heading (Common/Advanced/Naming), update `size` frontmatter, and add the ruby-annotated entry once its legitimizing word exists

## Notes body format

- **Bullet 1 (Graphemic)**: one Radical link + one character page link, most commonly.
  - Semantic component → `[char](Radical%20NNN)` if it's a Kangxi radical (3-digit zero-padded), else `[[char]]`
  - Phonetic component → always `[[char]]`
  - 形声 example: `形声 (OC \*lats): semantic [水](Radical%20085) ("water") + phonetic [[夕]] ("evening") – brief note.`
- **Bullet 2 (SKIP/Stroke)**: `[SKIP-X-Y-Z](...) ([Stroke NN](...))` — **stop there**. No syllable link, no em-dash. Stroke files are zero-padded to 2 digits (`Stroke 06.md`, `Stroke 13.md` — do not grep "Stroke 6"). Radical files are zero-padded to 3 digits (`Radical 085.md` — do not grep "Radical 85"). Always list the directory to verify exact filenames rather than assuming.
- **Bullet 3 (MC rank)**: `Ancient [[Lookup/CC/initials/聲 X|ipa]] + [[Lookup/CC/finals/韻 Y|ipa]] → [注音](../syllables/注音.md)`. **The syllable link belongs here, at the end — never on bullet 2.**
- **Bullet 4 (Levels)**: `[Jōyō-or-Jinmeiyō], [HSK], [Korean Name], [Grade]` — order matters: Jōyō, HSK, Korean, Grade. Omit any that don't apply (e.g. no HSK link if `hsk_level: 無`).

## Words section

List every Dan'a'yo word using this character with its full 注音 in the `<rt>` tag — it's fine to list a word whose file doesn't yet exist:
```markdown
- <ruby>[[後裔]]<rt>ㄏㄨㄛ⼶</rt></ruby> "descendant"
```

## `date-last-perfect` criteria

Leave blank if **any** of:
- Any required frontmatter field is missing or unverified
- Graphemic bullet is missing or links to unresolved components
- Levels bullet is missing any link (except the 先進 grade link, which has no target file)
- Words section is missing a word that uses this character

Set to today's date when all verifiable criteria are met.
