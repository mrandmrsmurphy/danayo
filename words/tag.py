import os
import re
import argparse
import difflib

ROOT = "."

def parse_tags(tag_block):
    tag_block = tag_block.strip()

    if tag_block.startswith('['):
        return [t.strip().strip('"\'') for t in tag_block.strip('[]').split(',') if t.strip()]

    if '\n' in tag_block:
        return [
            line.strip().lstrip('-').strip()
            for line in tag_block.splitlines()
            if line.strip().startswith('-')
        ]

    return [tag_block.strip('"\'')]

def format_tags(tags):
    return "tags:\n" + "\n".join(f"  - {t}" for t in tags)

def transform(content):
    if content.startswith('---'):
        match = re.match(r'^---\n(.*?)\n---\n?', content, re.DOTALL)
        if not match:
            return content, False

        fm = match.group(1)
        body = content[match.end():]

        tag_match = re.search(r'^tags:\s*(.*(?:\n(?:\s*-\s*.*))*)', fm, re.MULTILINE)

        if tag_match:
            existing = parse_tags(tag_match.group(1))
            if "word" in existing:
                return content, False

            existing.append("word")
            new_tags = format_tags(existing)
            new_fm = fm[:tag_match.start()] + new_tags + fm[tag_match.end():]
        else:
            new_fm = fm.strip() + "\n" + format_tags(["word"])

        new_content = f"---\n{new_fm.strip()}\n---\n{body}"
        return new_content, True

    new_content = f"---\n{format_tags(['word'])}\n---\n\n{content}"
    return new_content, True

def show_diff(old, new, path):
    diff = difflib.unified_diff(
        old.splitlines(),
        new.splitlines(),
        fromfile=f"{path} (original)",
        tofile=f"{path} (modified)",
        lineterm=""
    )
    print("\n".join(diff))
    print()

def process_file(path, apply_changes):
    with open(path, "r", encoding="utf-8") as f:
        original = f.read()

    modified, changed = transform(original)

    if not changed:
        return

    show_diff(original, modified, path)

    if apply_changes:
        with open(path, "w", encoding="utf-8") as f:
            f.write(modified)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="actually write changes")
    args = parser.parse_args()

    for filename in os.listdir(ROOT):
        if filename.endswith(".md"):
            process_file(os.path.join(ROOT, filename), args.apply)

if __name__ == "__main__":
    main()

