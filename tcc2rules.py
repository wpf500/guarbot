#!/usr/bin/python
import sys, random
from tcc import tcc

tag_whitelist = ('JJ', 'NNP', 'VB')
word_blacklist = ('@', '(', ')', 'GMT', 'be')
IGNORE = '--IGNORE--'

words = []
tags = []
for line in sys.stdin:
    word, tag = line.split().rsplit('/', 1)

    if tag in tag_whitelist and word not in word_blacklist:
        words.append(word)
        tags.append(tag)
    else:
        # just stop it from matching
        words.append(str(random.random()))
        tags.append(IGNORE)

for phrase_len in range(1, 6):
    results = tcc(words, tags, phrase_len, 10)
    for count, phrase, variations in results:
        for variation in variations:
            if IGNORE in variation:
                continue

            if phrase_len == 1:
                print variation, phrase
            elif 'NNP' in variation:
                print 'NNP', phrase
            else:
                print 'PHRASE', phrase
