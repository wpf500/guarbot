#!/usr/bin/python
import sys
from collections import defaultdict, deque

def tcc(words, phrase_len):
    phrases = defaultdict(list)
    window = deque(words[:phrase_len], phrase_len)
    for i, word in enumerate(words[phrase_len:]):
        phrases[' '.join(window)].append(i)
        window.append(word)

    return phrases

words = open('%s.words' % sys.argv[1]).read().split()
tags = open('%s.tags' % sys.argv[1]).read().split()

phrase_len = int(sys.argv[2])
top_len = int(sys.argv[3])

results = tcc(tags, phrase_len)
for phrase, pos in sorted(results.iteritems(), key=lambda (k, v): len(v))[:top_len]:
    if len(pos) > 1:
        print '%s %s' % (len(pos), phrase)
        for p in pos:
            print ' '.join(words[p:p+phrase_len])
        print
