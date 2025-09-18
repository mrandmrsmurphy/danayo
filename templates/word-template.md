---
characters: <% tR = await tp.system.prompt("Constituent characters comma-sep") %>
羅馬字 : <% tR = await tp.system.prompt("羅馬字") %>
韓文 : <% tR = await tp.system.prompt("韓文") %>
mandarin: <% tR = await tp.system.prompt("Mandarin pronunciation pinyin") %>
cantonese: <% tR = await tp.system.prompt("Cantonese pronunciation jyutping") %>
korean: <% tR = await tp.system.prompt("Korean reading Hangul") %>
japanese: <% tR = await tp.system.prompt("Japanese readings") %>
vietnamese: <% tR = await tp.system.prompt("Vietnamese readings") %>
pos: <% tR = await tp.system.prompt("Part of speech") %>
品詞: <$% tR = await tp.system.prompt("品詞") %>
meanings: <% tR = await tp.system.prompt("English meanings comma-separated") %>
variants: <% tR = await tp.system.prompt("Variant characters") %>
swadesh: <% tR = await tp.system.prompt("Swadesh") %>
---
