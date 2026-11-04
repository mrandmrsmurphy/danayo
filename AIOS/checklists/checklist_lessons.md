---
name: checklist-lessons
description: Completion rubric for lesson pages (lessons/Lesson NN.md) — what must be verified against the vault before a lesson's date-last-perfect is set, with extra checks by lesson type
metadata:
  type: checklist
---

# Checklist: Lesson Pages

A lesson page — `lessons/Lesson NN.md` — teaches one step of the course planned in `lessons/lesson-outline.md`. A lesson is built *out of* the vault's other pages (grammar, characters, words, syllables, lookup pages), so recertifying it means checking it against those pages, not against itself.

**What the stamp certifies.** The `date-last-perfect` on a lesson certifies **facts and consistency**: every claim, reading, gloss, count and answer has been checked against the vault, and the lesson agrees with its outline entry and its indexes. It does **not** certify that the teaching works. No learner testing is part of this rubric, and an AI cannot supply it. Say so in any report on a recertified lesson.

---

## Frontmatter

```yaml
---
language: English
date-last-perfect: YYYY-MM-DD
---
```

`date-last-perfect` is set only once every criterion below holds.

## Opening

The line immediately after the frontmatter is the back link: `> [[lesson-outline]]`. The first section is `## Learning objectives`, a bullet list that starts "By the end of this lesson you will be able to:".

---

## Core criteria (every lesson)

### 1. Objectives are testable
Every objective is practised by at least one exercise, and every exercise serves an objective. No objective promises something the lesson never teaches.

### 2. Outline match
The lesson delivers every bullet of its entry in `lesson-outline.md` (its **Goal**, topics and **Practice** line), or the outline entry is updated in the same pass. Numbers stated in the outline (for example "20 common characters") equal the numbers in the lesson.

### 3. Sources are linked
The lesson links to the vault pages it teaches from (the outline's **Reference** line names them). Every link resolves. A lesson never teaches a rule it does not link to.

### 4. Every fact agrees with the vault
Each claim is checked against the page that owns it:

| Claim about | Check against |
|---|---|
| Sounds, syllable shape, letters | `grammar/文法 - 02音韻論.en.md`, `grammar/Bopomofo.md`, `syllables/` |
| Writing system, character classes | `grammar/文法 - 03文字法.en.md`, character pages, `lookup/` |
| Word classes, particles, sentence rules | `grammar/文法 - 04句法.en.md`, `05形態.en.md`, `97品詞.md` |
| Readings, glosses, strokes, radicals, SKIP | the character or word page itself |

If a lesson and its source disagree, **work out which is right and fix the wrong one**. Never leave them disagreeing, and never "fix" a lesson by teaching a rule that contradicts the grammar page. If two source pages disagree with each other, resolve that first (ask the user), then the lesson.

### 5. Examples and glosses
- Every character or word shown has its 注音 as `<ruby>` text, copied from its page, not from memory.
- Every gloss is a meaning the page records.
- No invented words, readings or sentences. A Dan'a'yo example sentence uses only words that exist and obeys the grammar pages.

### 6. Latin spelling
Where a lesson writes the Latin spelling it uses the vault's `羅馬字` **exactly**: final stops are written with the voiced letters `b`, `d`, `g` (sib, nid, mog) where the Bopomofo writes ㄆ ㄊ ㄎ, and a null onset is written with an apostrophe ('id, 'yu). A lesson that teaches or uses the Latin says so in plain words; it never uses a looser respelling (sip, nit, mok) as if it were the vault's.

### 7. Exercises and answers
- Every exercise has an answer block (`>[!answer]- Answers`).
- Every answer is **computed independently** from the vault, not copied from the lesson's own claim.
- Counts in prompts and headings ("20 characters", "65 characters") equal the real counts.
- Numbering is consecutive, and exercises cover recognition, production and analysis where the lesson type allows (outline principle 6).

### 8. Indexes
The characters and words the lesson assigns match its rows in `lessons/lessons characters index.md` and `lessons/lessons word index.md`: same members, same counts, the running totals add up, and no character or word is assigned to two lessons.

---

## Extra criteria by lesson type

### Sound lessons (Lesson 01)
- The inventory counts equal the grammar pages' (six vowels, six glide letters, fifteen consonants) and the lesson's list agrees with `02音韻論` Figure 2.3 and the `Bopomofo.md` table.
- Every sound description (voiced or aspirated, palatalisation, unreleased finals) agrees with `02音韻論`.
- Every statement about which syllables exist (letters per syllable, forbidden combinations, exceptions) is checked against the syllable pages. State exceptions that exist; do not state rules the syllable pages break.
- Every drill reading matches its character's page.

### Character lessons (Lessons 02, 03)
- Each character listed is in the grade the lesson claims, with the stroke count, radical and SKIP code its page gives.
- The class (pictogram, symbol, compound, phono-semantic) agrees with the character's `graphemic_classification` and the `List of` pages.

### Grammar lessons (Lessons 04 to 17)
- Each rule matches the grammar chapter and `97品詞`, using their terms (関詞, 事詞, 性詞, 系詞, 特詞, 修飾語).
- Every example is glossed word by word, and a second reader can check each particle's slot against the chapter.
- Register labels (古雅体, 書面体, 網語体) match 04 and 01.

### Reading and writing lessons (Lessons 18 to 20)
- Every text has a stated source, and its words and readings are checked against the vault.
- Every glossed word exists on a word page.

---

## Staleness

A lesson's stamp stops counting when any page it relies on has changed since the stamp. Check with git, using each source page:

```bash
git log -1 --format=%cs -- <source page>
```

If that date is later than the lesson's `date-last-perfect`, recheck the lesson against the changed page. The usual sources by lesson type are the tables above, plus the lesson's entry in `lesson-outline.md` and its two index rows.

---

## What "done" means

Set `date-last-perfect` to today when all of the following hold:

1. The frontmatter, back link and objectives section are as above.
2. Every objective has an exercise and every exercise an answer.
3. The outline entry and the lesson agree.
4. Every fact, reading, gloss, count and answer was checked against the vault in this pass.
5. The Latin spelling follows the vault exactly.
6. The indexes match.
7. No source page is newer than the lesson's earlier stamp without having been rechecked.
8. The report says plainly that the stamp certifies facts and consistency, not teaching.

---

## Common mistakes to avoid

- **Trusting the lesson's own claims.** Lesson 01 said ǝ takes no off-glide except in ㄜㄧ, while 02 said ǝ never takes one. The syllable pages showed the lesson was right and 02 was wrong. Check against the pages, not against whichever sounds better.
- **A looser Latin spelling** such as sip, nit, mok for what the vault writes sib, nid, mog.
- **A lesson with no source links**, so a reader cannot check any claim.
- **Answers copied from the lesson's own table** instead of recomputed.
- **Counts left stale** after an index or a grade page changes.
- **Claiming the lesson teaches well.** The stamp does not say that.
