```dataviewjs
// ...code above...
```
```dataviewjs
// ...code above...
```
```dataviewjs
// ...code above...
```
```dataviewjs
// ...code above...
```
```dataviewjs
// Change this:
const prop = "羅馬字";          // name of your property
const source = dv.pages('"characters"'); // dv.pages('"FolderName"')

// Build a histogram: {value -> count}
let counts = {};
for (let p of source) {
  let v = p[prop];
  if (v == null) continue;
  counts[v] = (counts[v] ?? 0) + 1;
}

// Turn it into a table
dv.table(
  ["Value", "Count"],
  Object.entries(counts)
        .sort((a,b) => b[1] - a[1]) // sort by count desc
        .map(([v,c]) => [v, c])
);

```