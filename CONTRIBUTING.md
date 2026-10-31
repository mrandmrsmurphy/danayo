# Contributing

Corrections, sources and design discussion for Dan'a'yo (単亜語) are welcome. This repository is the flagship of the Universal Languages project; the [parent repository](https://github.com/mrandmrsmurphy/universal-languages) holds the shared pages and the other languages.

## How it works

1. **Propose through a pull request** (or an issue, for a question or suggestion). Describe what you changed and why.
2. **The maintainer reviews all contributions.** Nothing is merged unseen. A design decision may already be settled (see [AIOS/memory-index.md](AIOS/memory-index.md) for the standing rulings) or may be one the maintainer wants to make.
3. **Vetted contributors can be given direct access** once their work has been reviewed and found careful.

## Where help is most useful

- **Native-reader checks.** The Mandarin, Cantonese, Japanese, Korean and Vietnamese readings on word and character pages.
- **Vietnamese readings.** Many words carry none. A reading is welcome with its source (Wiktionary or hvdic.thivien.net).
- **Sources for Notes.** Etymology, historical context and cross-linguistic variation, each with a citation.
- **Gaps in the lexipedia.** Entries marked *(needs a word)* on the [lexipedia](lexipedia/Lexipedia.md) pages.
- **The grammar pragmatics chapter and the lessons.** See [単亜語之文法書](grammar/単亜語之文法書.md) and [lessons/lesson-outline.md](lessons/lesson-outline.md).
- **Errors.** A wrong reading, a gloss that disagrees with its character page, a link that does not resolve.

## Standards

- **Check the checklist first.** [AIOS/checklist-index.md](AIOS/checklist-index.md) says what makes a character, word, chengyu, syllable or lexipedia page complete. Do not add a `date-last-perfect` stamp unless every criterion is met.
- **Characters are not words.** `characters/` holds characters only; `words/` holds the vocabulary. A character that can also stand alone is named `X (char).md` so that `words/X.md` stays free. See [AIOS/vault-structure.md](AIOS/vault-structure.md).
- **The character page sets the reading.** If a word disagrees with its characters, fix the word.
- **Pronunciation is written in 注音 (Bopomofo)**, not romanization. The `korean` field uses the North Korean form, which keeps initial ㄹ and ㄴ.
- **Cite evidence.** Do not invent an attestation to fill a gap. Verify a classical citation in its named source before listing it.
- **Prefer an existing word.** Render a new term as two existing words before coining a compound, and keep any coinage transparent from its characters. Propose coinages in an issue first.
- **Content pages state facts only.** No changelog, "this sweep", or process commentary in a Notes section.
- **Use relative Markdown links** (`../words/X.md`, with `%20` for spaces) so pages also read on GitHub, and write Dan'a'yo words as `<ruby>` text with their 注音.
- **Say if AI helped.** Note it in the pull request, and check what the assistant gave you.

## Licence

By contributing you agree that your contribution is licensed under [CC BY-SA 4.0](LICENSE), like the rest of the repository. Do not contribute text or images you do not have the right to share under that license.
