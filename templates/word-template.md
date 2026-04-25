<%*
// 1. Gather all inputs
const char = await tp.system.prompt("Constituent characters");
const romaji = await tp.system.prompt("羅馬字");
const hanmun = await tp.system.prompt("諺文");
const mandarin = await tp.system.prompt("Mandarin pinyin");
const cantonese = await tp.system.prompt("Cantonese jyutping");
const korean = await tp.system.prompt("Korean readings");
const japanese = await tp.system.prompt("Japanese reading");
const vietnamese = await tp.system.prompt("Vietnamese reading");
const pos = await tp.system.prompt("Part of speech");
const pos_jp = await tp.system.prompt("品詞");
const english = await tp.system.prompt("English meanings");
const bopomofo = await tp.system.prompt("Bopomofo spelling");

// 2. Build the page
tR += `---
characters: ${char}
羅馬字: ${romaji}
諺文: ${hanmun}
mandarin: ${mandarin}
cantonese: ${cantonese}
korean: ${korean}
japanese: ${japanese}
vietnamese: ${vietnamese}
pos: ${pos}
品詞: ${pos_jp}
english: ${english}
注音: ${bopomofo}
---
\`\`\`meta-bind-embed
[[nav/word_info]]
\`\`\`
## Notes`
%>