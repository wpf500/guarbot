#!/usr/bin/python
import sys
from collections import Counter, deque

def tcc(words, phrase_len):
    phrases = Counter()
    window = deque(words[:phrase_len], phrase_len)
    for word in words[phrase_len:]:
        phrases[' '.join(window)] += 1
        window.append(word)

    return phrases

words = sys.stdin.read().split()

phrase_len = int(sys.argv[1])
top_len = int(sys.argv[2])

for phrase, count in tcc(words, phrase_len).most_common(top_len):
    print '%d %s' % (count, phrase)
