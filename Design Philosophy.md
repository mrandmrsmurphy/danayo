# Design Philosophy

> Parent: [Universal Languages](https://github.com/mrandmrsmurphy/universal-languages) · Grammar preface: [文法 - 01序文.en](grammar/文法%20-%2001序文.en.md) · Orthography: [文法 - 03文字法.en](grammar/文法%20-%2003文字法.en.md)

The principles behind the design choices of Dan'a'yo, each with its reason and the pages where it is carried out. The language is the flagship of the [Universal Languages](https://github.com/mrandmrsmurphy/universal-languages) project and satisfies its two shared principles (easier than any other regional language; its own script).

## The Renewed Sinosphere chooses unity

This is the maxim of the language. For centuries the Civil Service Examination gave East Asia one written standard and one corpus of classical texts. That unity has declined, and when delegates of China, Japan, Korea and Vietnam meet today they usually speak English, with losses of nuance and shared heritage. Dan'a'yo is a tool for communication, not a replacement for any mother tongue. Speakers keep writing poetry and living their daily lives in their own languages, as Ecclesiastical Latin once let Europeans talk across theirs.

## Japanese orthography, Korean phonology, Chinese grammar

Three observations give three rules.

- **Phonology favors Old Korean**, which lies between Chinese and Japanese. Dan'a'yo sounds somewhat like older Korean. See [音韻論](grammar/文法%20-%2002音韻論.en.md).
- **Orthography follows Japanese simplification**, a compromise between Traditional and Simplified Chinese characters (新字体). See [文字法](grammar/文法%20-%2003文字法.en.md).
- **Grammar continues the framework of Classical Chinese**, which historically served all of them: mostly analytic, SVO, topic-prominent, with classifiers, postpositions and pro-drop. The older VO order is restored where Japanese compounding shifted to SOV. See [句法](grammar/文法%20-%2004句法.en.md).

## A shared stratum: Classical Chinese

No proto-language gives all the source languages a common ancestor. The shared layer is Classical Chinese, which is well-known and actually exists in documented form. Vocabulary is drawn from it first, and from pan-Asian, widely recognized terms next. A modern term is formed analytically only when no such word exists, and aims to be transparent (新語).

## Easier than any other regional language

For every speaker in its zone, Dan'a'yo must be easier to learn than any other language of the region is for that speaker. It is not necessarily rock-bottom easy. A Korean should find it easier than Mandarin. This is the test applied to each contested choice of sound, script, grammar and vocabulary. In practice, any speaker of Chinese, Japanese, Korean or Vietnamese should recognize more than half of a Dan'a'yo text by sight or by ear, and more with a little training.

## Its own script

Every word has a Chinese-character base. 注音 (Bopomofo) is presented with it whenever possible and is the system for phonetic transcription. A pinyin-style Latin alphabet for Dan'a'yo phonetics was never an option, so that the language is never mistaken for a national one and its spelling matches its sounds. Readings are written in 注音, never in romanization.

## The character base is an intersection

The character base follows the intersection of three educational standards: Japan's Jōyō list, Korea's secondary-school list and China's HSK vocabulary list. Official name-character lists in Japan and Korea are consulted as well, and together they define the maximal set of allowable characters. Characters that are ruled out are listed in [文法 - 98違法字](grammar/文法%20-%2098違法字.md).

## Characters are building blocks, words are the vocabulary

A character is a bound unit with readings, strokes and a radical; it is not itself a lexical entry. The vocabulary lives in `words/`, and words are mostly compounds, though a word may be as small as one character. A character that cannot stand alone is given a stand-in word that carries its meaning, so that every character has a usable form. See [vault-structure](AIOS/vault-structure.md).

## One authority for each reading

The character page sets the reading, and any word or chengyu built from it is corrected to match, never the reverse. Korean readings keep initial ㄹ and ㄴ, in line with the Old Korean phonology above.

## Split before coining

When a needed term can be said with two existing words, it is said that way rather than coined as a new compound. A coinage is made only when no split exists, and its meaning is worked out against the five source languages in the [lexipedia](lexipedia/Lexipedia.md) page of its field. Where Dan'a'yo's own sense should narrow, shift or broaden the shared meaning, the Semantic Range Notes say so; an honest "same as the shared sense" is the usual answer.

## Document the current state

Content pages describe the language as it is now. They carry no changelog, no process commentary and no unsourced claims. A claim that could not be confirmed is flagged on the page itself, tersely.
