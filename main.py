#!/usr/bin/python
import json
from collections import Counter, deque
from bs4 import BeautifulSoup

data = json.loads(open('articles.json').read())

def tcc(words, phrase_len):
    phrases = Counter()
    window = deque(words[:phrase_len], phrase_len)
    for word in words[phrase_len:]:
        phrases[' '.join(window)] += 1
        window.append(word)

    return phrases

texts = ''
for article in data['response']['results']:
    body = BeautifulSoup(article['fields']['body'], 'html5lib')
    texts += ' '.join(body.find_all(text=True)) + ' '

words = texts.lower().split()
for n in xrange(20):
    phrases = tcc(words, n + 1)
    print 'Phrase length %d' % n
    for phrase, count in phrases.most_common(10):
        if count > 1:
            print '%s\t%d' % (phrase, count)
