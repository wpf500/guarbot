#!/usr/bin/python
import sys, nltk

sents = nltk.sent_tokenize(sys.stdin.read())
for sent in sents:
    for word, tag in nltk.pos_tag(nltk.word_tokenize(sent)):
        print word,
        print >> sys.stderr, tag,
