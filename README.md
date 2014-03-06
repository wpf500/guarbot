You'll need `nltk` and `bs4`

## Getting the data
Choose your search,
e.g. `<url>` = http://content.guardianapis.com/search?tag=profile%2Fpollytoynbee&show-fields=body

Then:
```
wget <url> -O articles.json
./json2txt.py < articles.json > articles.txt
./txt2tag.py < articles.txt > articles.words 2> articles.tags
```

Or the quick way:
```
wget <url> -O - | ./json2txt.py | ./txt2tag.py > articles.words 2> articles.tags
```

### `json2txt.py`
Extracts article content from the results of a Content API content search

### `txt2tag.py`
Takes a body of text and tag each word, outputting each word to `stdout` and
its tag to `stderr`

## Analysing the data

### Text concordance checker: `tcc.py`
Most popular words/phrases by tag
```
./tcc.py <file name> <phrase length> <results>
```
`<results>`: number of different phrases to return

### Context-free grammar parser: `cfg.py`
Parses a set of CFG rules and generates some text from a given base rule.
Heavily based on http://pdos.csail.mit.edu/scigen/

```
./cfg.py [-l] <base rule> < <rules file>
```
`-l` lists the rules related to `<base rule>` instead of generating text

#### Rules file format
```
non-terminal <terminal/non-terminal>...
```
`non-terminal` must be of the format `[A-Z][A-Z0-9_]*`

e.g.
```
SENTENCE This is WORD

WORD easy
WORD hard
WORD another WORD2

WORD2 level
```
```
./cfg.py SENTENCE < eg.rules
This is easy
```

See also `examples.rules` (taken from SCIgen)
