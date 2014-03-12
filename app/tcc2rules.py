#!/usr/bin/env python
import sys, random
from tcc import tcc

tag_whitelist = ('JJ', 'NNP', 'VB', 'NN', 'CD')
word_blacklist = ('@', '(', ')', 'GMT', 'be', '..')
IGNORE = '--IGNORE--'

words = []
tags = []
for line in sys.stdin:
    word, tag = line.strip().rsplit('/', 1)

    if tag in tag_whitelist and word not in word_blacklist:
        words.append(word)
        tags.append(tag)
    else:
        words.append(str(random.random())) # just stop it from matching
        tags.append(IGNORE)

for phrase_len in range(1, 20):
    results = tcc(words, tags, phrase_len, 15)
    for count, phrase, variations in results:
        for variation in variations:
            if IGNORE in variation:
                continue

            uniq = set(variation.split())
            if len(uniq) == 1:
                print uniq.pop(),
            elif 'NNP' in variation:
                print 'NNP',
            else:
                print 'PHRASE',
            print phrase
