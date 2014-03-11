#!/usr/bin/env python
import sys, nltk
from collections import defaultdict

sents = nltk.sent_tokenize(sys.stdin.read())
counts = defaultdict(int)
for sent in sents:
    counts[len(nltk.word_tokenize(sent))] += 1

print 'set nokey'
print 'plot \'-\' with boxes'
print
for length, count in counts.iteritems():
    print length, count
