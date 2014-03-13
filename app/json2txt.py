#!/usr/bin/env python
import sys, json
from bs4 import BeautifulSoup, Comment

hidden = ['style', 'script', '[document]', 'head', 'title']
def get_text(body):
    def visible(ele):
        return not (ele.parent.name in hidden or isinstance(ele, Comment))
    texts = BeautifulSoup(body, 'html5lib').find_all(text=True)
    return ' '.join(filter(visible, texts))

data = json.loads(sys.stdin.read())
results = filter(lambda a: 'fields' in a, data['response']['results'])
texts = ''
for article in results:
    texts += get_text(article['fields'].get('body', '')) + ' '

print texts.encode('ascii', 'ignore')
