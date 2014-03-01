#!/usr/bin/python
import json, nltk
from collections import Counter, deque
from bs4 import BeautifulSoup

data = json.loads(open('toynbee.json').read())

def tcc(words, phrase_len):
    phrases = Counter()
    window = deque(words[:phrase_len], phrase_len)
    for word in words[phrase_len:]:
        phrases[' '.join(window)] += 1
        window.append(word)

    return phrases

results = filter(lambda a: 'fields' in a, data['response']['results'])
texts = ''
for article in results:
    body = BeautifulSoup(article['fields']['body'], 'html5lib')
    texts += ' '.join(body.find_all(text=True)) + ' '

sents = nltk.sent_tokenize(texts)
words = [word for sent in sents for word in nltk.word_tokenize(sent)]

for phrase, count in tcc(words, 5).most_common(20):
    print '%d %s' % (count, phrase)
