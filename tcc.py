#!/usr/bin/python
import sys
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
    words = []
    tags = []
    for line in sys.stdin:
        word, tag = line.strip().rsplit('/', 1)
        words.append(word)
        tags.append(tag)

    if sys.argv[1] == '-t':
        base_list, lookup_list = tags, words
    else:
        base_list, lookup_list = words, tags

    phrase_len = int(sys.argv[2])
    top_len = int(sys.argv[3])

    results = tcc(base_list, lookup_list, phrase_len, top_len)
    for count, phrase, variations in results:
        print '%d %s' % (count, phrase)
        for variation in variations:
            print variation
        print
