<%*
// 1. Prompt for the character
const char = await tp.system.prompt("Enter Character (e.g., 万)");
if (!char) return;

// 2. Define the path (adjust "characters/" if your folder name is different)
const path = `characters/${char}.md`;
const file = app.vault.getAbstractFileByPath(path);

if (file) {
    // 3. Get the "注音" property from the file's frontmatter
    const cache = app.metadataCache.getFileCache(file);
    const zhuyin = cache?.frontmatter?.["注音"] || "No Zhuyin found";
    
    // 4. Handle URL encoding for the path (in case of spaces)
    const encodedPath = path.replace(/ /g, "%20");
    
    // 5. Output the Ruby tag with the Markdown link
    const output = `<ruby>[${char}](/${encodedPath})<rt>${zhuyin}</rt></ruby>`;
    tR += output;
} else {
    // Fallback if the file doesn't exist
    new Notice(`File for "${char}" not found at ${path}`);
    tR += char; 
}
%>