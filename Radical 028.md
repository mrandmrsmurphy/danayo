

## Dataview
```dataview
TABLE 韓文 AS "Sound", english AS "en", radical AS "Radical", stroke_count AS "SC"
FROM "characters"
WHERE radical = "厶"
SORT stroke_count ASC
```


```base
views: 
	- type: table 
	  name: Table 
	  filters: 
		  and: 
			- file.folder == "characters"
```