# tsv2json
Converting a TSV file which is in a specific format to JSON.

This is a very specialized code almost hard coded to work on a specific schema and it is not a general purpose tool by any means.

Columns of the TSV file are:

Field | Type
--- | ---
name | string
language_iso | string
level	| enum: -1, 1, 2, 3, 4
keywords | array of strings

The TSV file is downloaded from a Google Sheet. The `keywords` field ends up being a comma separated list of strings
which are in different locales.

This tool is priamily used to convert the TSV file to a JSON file with the `keywords` as an array of strings keeping
their original encoding. 

The JSON file can then be imported into a MongoDB colleciton. As such a few extra fields are needed like `createdAt`,
`updatedAt`, `updatedBy` and the soft delete indicator boolean `_deleted`.  As these could all be the same for all the
associated MongoDB document, they are hard coded just for simplification.

# Usage
```
./tsv2json.py -i <input-file.tsv> -o <output-file.json>
```
e.g.
```
./tsv2json.py -i data-zh.tsv -o data4-zh.json
```
