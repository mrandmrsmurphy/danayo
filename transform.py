from pathlib import Path

WORD_DIR = Path("words")

for file in WORD_DIR.iterdir():
    if not file.is_file():
        continue
    if file.suffix != ".md":
        continue

    word = file.stem

    # Keep true one-character files untouched
    if len(word) == 1:
        continue

    text = file.read_text(encoding="utf-8")
    lines = text.splitlines()

    tip1 = f">[!tip] This is a page about the word {word}."
    tip2 = f"> For the character, see [{word}](/characters/{word}%20(char).md)."

    changed = False
    new_lines = []
    i = 0

    while i < len(lines):
        if i + 1 < len(lines) and lines[i] == tip1 and lines[i + 1] == tip2:
            i += 2
            changed = True
            if i < len(lines) and lines[i] == "":
                i += 1
            continue

        new_lines.append(lines[i])
        i += 1

    if changed:
        file.write_text("\n".join(new_lines) + "\n", encoding="utf-8")
        print(f"Cleaned: {file.name}")

print("Done.")
