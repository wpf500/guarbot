#!/usr/bin/python
import sys, random
from itertools import izip
from collections import defaultdict, deque

def tcc(base_list, lookup_list, phrase_len, top_len):
    phrases = defaultdict(list)
    window = deque(base_list[:phrase_len], phrase_len)
    for i, word in enumerate(base_list[phrase_len:]):
        phrases[' '.join(window)].append(i)
        window.append(word)

    top_list = sorted(phrases.iteritems(), key=lambda (k, v): len(v))[-top_len:]
    results = []
    for phrase, pos in top_list:
        variations = set(' '.join(lookup_list[p:p+phrase_len]) for p in pos)
        results.append((len(pos), phrase, variations))
    return results


if __name__ == '__main__':
    tag_whitelist = ('JJ', 'NNP', 'VB')
    word_blacklist = ('@', '(', ')', 'GMT')

    words = open('%s.words' % sys.argv[2]).read().split()
    tags = open('%s.tags' % sys.argv[2]).read().split()

    phrase_len = int(sys.argv[3])
    top_len = int(sys.argv[4])

    if sys.argv[1] == '-t':
        base_list = tags
        lookup_list = words
    else:
        base_list = []
        lookup_list = []
        for word, tag in izip(words, tags):
            if tag in tag_whitelist and word not in word_blacklist:
                base_list.append(word)
                lookup_list.append(tag)
            else:
                # just stop it from matching
                base_list.append(str(random.random()))
                lookup_list.append('--IGNORE--')

    results = tcc(base_list, lookup_list, phrase_len, top_len)
    for count, phrase, variations in results:
        print '%d %s' % (count, phrase)
        for variation in variations:
            print variation
        print
