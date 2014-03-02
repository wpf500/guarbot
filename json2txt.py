#!/usr/bin/python
import sys, json
from bs4 import BeautifulSoup

data = json.loads(sys.stdin.read())
results = filter(lambda a: 'fields' in a, data['response']['results'])
texts = ''
for article in results:
    body = BeautifulSoup(article['fields']['body'], 'html5lib')
    texts += ' '.join(body.find_all(text=True)) + ' '

print texts.encode('ascii', 'ignore')
