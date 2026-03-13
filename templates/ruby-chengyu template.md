<%*
const chengyu = await tp.system.prompt("Enter Chengyu");
if (!chengyu) return;

const path = `chengyu/${chengyu}.md`;
const targetFile = app.vault.getAbstractFileByPath(path);

if (targetFile) {
    const cache = app.metadataCache.getFileCache(targetFile);
    const zhuyin = cache?.frontmatter?.["注音"];
    
    // Only encode SPACES, leave the beautiful characters alone
    const cleanPath = path.replace(/ /g, "%20");
    
    if (zhuyin) {
        tR += `<ruby>[${chengyu}](/${cleanPath})<rt>${zhuyin}</rt></ruby>`;
    } else {
        new Notice(`"注音" missing for ${chengyu}`);
        tR += word;
    }
} else {
    new Notice(`File not found: ${path}`);
    tR += chengyu;
}
%>