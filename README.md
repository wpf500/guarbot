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
wget <url> -O articles.json
./json2txt.py < articles.json > articles.txt
./txt2tag.py < articles.txt > articles.tags
```

Or the quick way:
```
wget <url> -O - | ./json2txt.py | ./txt2tag.py > articles.tags
```

### `json2txt.py`
Extracts article content from the results of a Content API content search

### `txt2tag.py`
Takes a body of text and tags each word, outputting a word and its tag to
each line.

## Analysing the data

### Text concordance checker: `tcc.py`
Most popular words/phrases by tag
```
./tcc.py -t|-w <phrase length> <results> < <tagged words>
```
`-t|-w`: check tags or words respectively

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

### Generate rules based on text concordance: `tcc2rules.py`
Generates some rules based on common proper nouns, adjectives and verbs in
the given text

```
./tcc2rules < <tagged words> > example.rules
```
