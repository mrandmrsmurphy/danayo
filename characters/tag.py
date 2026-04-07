import os
import re

ROOT = "."  # run this inside /characters

def parse_tags(tag_block):
    """
    Accepts:
      tags: character
      tags: [character, foo]
      tags:
        - character
        - foo
    Returns a Python list of strings.
    """
    tag_block = tag_block.strip()

    # inline list: [a, b]
    if tag_block.startswith('['):
        return [t.strip().strip('"\'') for t in tag_block.strip('[]').split(',') if t.strip()]

    # multiline list
    if '\n' in tag_block:
        return [line.strip().lstrip('-').strip() for line in tag_block.splitlines() if line.strip().startswith('-')]

    # single value
    return [tag_block.strip('"\'')]

def format_tags(tags):
    return "tags:\n" + "\n".join(f"  - {t}" for t in tags)

def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if content.startswith('---'):
        # has frontmatter
        match = re.match(r'^---\n(.*?)\n---\n?', content, re.DOTALL)
        if not match:
            return  # malformed, skip

        fm = match.group(1)
        body = content[match.end():]

        # find tags block
        tag_match = re.search(r'^tags:\s*(.*(?:\n(?:\s*-\s*.*))*)', fm, re.MULTILINE)

        if tag_match:
            existing = parse_tags(tag_match.group(1))
            if "character" not in existing:
                existing.append("character")

            new_tags = format_tags(existing)
            fm = fm[:tag_match.start()] + new_tags + fm[tag_match.end():]
        else:
            # no tags field
            fm = fm.strip() + "\n" + format_tags(["character"])

        new_content = f"---\n{fm.strip()}\n---\n{body}"

    else:
        # no frontmatter
        new_content = f"---\n{format_tags(['character'])}\n---\n\n{content}"

    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)

def main():
    for filename in os.listdir(ROOT):
        if filename.endswith(".md"):
            process_file(os.path.join(ROOT, filename))

if __name__ == "__main__":
    main()

