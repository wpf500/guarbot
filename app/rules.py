#!/usr/bin/python
import sys, collections, random
from tcc import tcc

sample_size = 15

tag_whitelist = (
    'RB', 'CD', 'VB', 'VBD', 'VBG', 'VBZ', 'JJ', 'JJR', 'JJS',
    'NN', 'NNS', 'NNP', 'NNPS'
)

tag_whitelist_phrases = ('JJ', 'NNP', 'NNPS', 'VB', 'NN', 'CD')

word_blacklist = (
    'be', 'is', '\'s', '(', ')', 'was', 'n\'t', 'so', 'have',
    'here', '@', '..', 'GMT'
)

IGNORE = '--IGNORE--'

rules = collections.defaultdict(list)
words = []
tags = []
for line in sys.stdin:
    word, tag = line.strip().rsplit('/', 1)
    if tag in tag_whitelist and word not in word_blacklist:
        rules[tag].append(word)

        if tag in tag_whitelist_phrases:
            words.append(word)
            tags.append(tag)
            continue

    # stop word from being a repeat
    words.append(str(random.random())) 
    tags.append(IGNORE)

# print some single word rules
for tag, tag_words in rules.iteritems():
    if len(tag_words) >= sample_size:
        tag_words = random.sample(tag_words, sample_size)
    for word in tag_words:
        print tag, word

# print some more complicated phrases
for phrase_len in range(2, 20):
    results = tcc(words, tags, phrase_len, sample_size)
    for count, phrase, variations in results:
        for variation in variations:
            if IGNORE in variation:
                continue

            uniq = set(variation.split())
            if len(uniq) == 1 and variation != 'NN':
                print uniq.pop(),
            elif 'NNP' in variation:
                print 'NNP',
            else:
                print 'PHRASE',
            print phrase
