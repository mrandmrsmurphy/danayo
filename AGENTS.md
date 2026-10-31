# AGENTS.md

This file provides guidance to AI Code software when working with code in this repository.

An **Obsidian vault** for *単亜語* (Dan'a'yo), a constructed zonal auxiliary language for the East Asian cultural sphere (Mandarin, Cantonese, Japanese, Korean, Vietnamese).

**It is a daughter project.** Dan'a'yo is the flagship of the Universal Languages (UL) project (parent vault: UL; see [[AIOS/memory/reference_ul_family_structure.md]]). It is free-standing, with its own vault, grammar and vocabulary, but it is also in line with the UL family, whose design principles it must satisfy:

- **Every UL has its own script.** Dan'a'yo's is Han characters, with Bopomofo (注音) for sound. A pinyin-style Latin alphabet for Dan'a'yo phonetics was never an option.
- **Each UL should be easier for its region's speakers than any other language of that region**, not necessarily rock-bottom easy. Dan'a'yo should be easier for a Korean to learn than Mandarin, for example.

When describing the vault, include this framing, and when judging a design choice, test it against both principles.

## Orientation (read before describing this vault to anyone)

Four atomic entry types, each in its own folder:

- **`characters/`** — individual Han characters, and *only* characters. **No file here is a word.** A character is a bound building block; it has readings, strokes, radical, etc., but it is not itself a lexical entry.
- **`words/`** — the actual vocabulary: every Dan'a'yo word, including single-character words (`words/X.md`). Words far outnumber characters (roughly 2:1), because words are mostly compounds.
- **`chengyu/`** — idioms. **`syllables/`** — the phonetic inventory in Bopomofo.

**Naming rule:** `X.md` in `words/` is the word. A character that can *also* stand alone as a word is saved as `characters/X (char).md`, so it doesn't collide with `words/X.md`. A character that is bound-only is plain `characters/X.md`. So `(char)` doesn't mean "this is a word" — it means "a word of the same name exists, and this is the character behind it." Don't count `characters/` files as words or `words/` files as characters; the two folders measure different things.

Counts change daily — compute them (`git ls-files characters | wc -l`) rather than quoting a number from memory or from another agent's summary. For how complete each part is (all four folders are fully perfected; grammar pragmatics and the lessons are the gaps), see "Current state" in [[AIOS/vault-structure.md]].

## Where things are

- **Vault structure, setup, frontmatter conventions, ruby text, databases:** [[AIOS/vault-structure.md]]
- **Who the user is and how to collaborate:** [[AIOS/me.md]]
- **Standing memory — feedback, corrections, external references:** [[AIOS/memory-index.md]]
- **Ongoing project status:** [[AIOS/projects.md]]
- **How to create characters/words/chengyu:** [[AIOS/skill-index.md]]
- **How to judge whether an existing page is complete:** [[AIOS/checklist-index.md]]
- **What AIOS is and how this persistence system works:** [[AIOS/README.md]]

License: CC BY-SA 4.0 for all content and code (see `LICENSE`).
