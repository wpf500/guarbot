```
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt
```

## Getting the data
Choose your search,
e.g. `<url>` = http://content.guardianapis.com/search?tag=profile%2Fpollytoynbee&show-fields=body

Then:
```
wget <url> -O example.json
./json2txt.py < example.json > example.txt
./txt2tags.py < example.txt > example.tags
./rules.py < example.tags > example.rules
```

Or the quick way:
```
wget <url> -O - | ./json2txt.py | ./txt2tags.py | ./rules.py  > example.rules
```

### `json2txt.py`
Extracts article content from the results of a Content API content search

### `txt2tags.py`
Takes a body of text and tags each word, outputting a word and its tag to
each line.

## Analysing the data

### Text concordance checker: `tcc.py`
Most popular words/phrases by tag
```
./tcc.py -t|-w <phrase length> <results> < example.tags
```
`-t|-w`: check tags or words respectively

`<results>`: number of different phrases to return

### Context-free grammar parser: `cfg.py`
Parses a set of CFG rules and generates some text from a given base rule.
Heavily based on http://pdos.csail.mit.edu/scigen/

```
./cfg.py [-l] <base rule> < examples.rules
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

See also `data/base.rules`

### Generate rules based on text concordance: `rules.py`
Generates some rules based on common proper nouns, adjectives and verbs in
the given text

```
./rules.py < example.tags > example.rules
```

Use `rules2json.py` to convert the rules to a JSON object the app can use.
