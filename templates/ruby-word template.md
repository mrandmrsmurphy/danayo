<%*
const word = await tp.system.prompt("Enter Word");
if (!word) return;

const path = `words/${word}.md`;
const targetFile = app.vault.getAbstractFileByPath(path);

if (targetFile) {
    const cache = app.metadataCache.getFileCache(targetFile);
    const zhuyin = cache?.frontmatter?.["注音"];
    
    // Only encode SPACES, leave the beautiful characters alone
    const cleanPath = path.replace(/ /g, "%20");
    
    if (zhuyin) {
        tR += `<ruby>[${word}](/${cleanPath})<rt>${zhuyin}</rt></ruby>`;
    } else {
        new Notice(`"注音" missing for ${word}`);
        tR += word;
    }
} else {
    new Notice(`File not found: ${path}`);
    tR += word;
}
%>