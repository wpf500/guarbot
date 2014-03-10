#!/usr/bin/python
import sys, random
from itertools import izip
from tcc import tcc

tag_whitelist = ('JJ', 'NNP', 'VB')
word_blacklist = ('@', '(', ')', 'GMT', 'be')
IGNORE = '--IGNORE--'

words = open('%s.words' % sys.argv[1]).read().split()
tags = open('%s.tags' % sys.argv[1]).read().split()

word_list = []
tag_list = []
for word, tag in izip(words, tags):
    if tag in tag_whitelist and word not in word_blacklist:
        word_list.append(word)
        tag_list.append(tag)
    else:
        # just stop it from matching
        word_list.append(str(random.random()))
        tag_list.append(IGNORE)

for phrase_len in range(1, 6):
    results = tcc(word_list, tag_list, phrase_len, 10)
    for count, phrase, tags in results:
        for tag in tags:
            if IGNORE in tag:
                continue

            if phrase_len == 1:
                print tag, phrase
            elif 'NNP' in tag:
                print 'NNP', phrase
            else:
                print 'PHRASE', phrase
