#!/usr/bin/python
import nltk
from collections import Counter, deque

def tcc(words, phrase_len):
    phrases = Counter()
    window = deque(words[:phrase_len], phrase_len)
    for word in words[phrase_len:]:
        phrases[' '.join(window)] += 1
        window.append(word)

    return phrases

texts = open('monbiot.txt').read()

sents = nltk.sent_tokenize(texts)
words = [word for sent in sents for word in nltk.word_tokenize(sent)]

for phrase, count in tcc(words, 5).most_common(20):
    print '%d %s' % (count, phrase)
