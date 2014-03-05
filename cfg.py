#!/usr/bin/python
import sys, random, re
from collections import defaultdict

# read rules from stdin
group = False
rules = defaultdict(list)
for line in sys.stdin:
    line = line.strip()
    if len(line) == 0 or line[0] == '#':
        continue

    toks = line.split()
    # group rule
    if toks[-1] == '{':
        group = True
        rule_name = toks[0]
        rule_toks = []
    elif toks[0] == '}':
        group = False
    elif group:
        rule_toks.extend(toks)
    # single line rule
    else:
        rule_name = toks[0]
        rule_toks = toks[1:]

    if not group:
        weight = 1
        if '+' in rule_name:
            rule_name, weight = rule_name.split('+')

        for i in xrange(int(weight)):
            rules[rule_name].append(' '.join(rule_toks))

# stop allowing unknown rule names
rules.default_factory = None

# non-terminals are all uppercase with underscores, at least 2 chars
nt_re = re.compile('[A-Z_]{2,}')
def expand(m):
    return nt_re.sub(expand, random.choice(rules[m.group(0)]))

# list possible expansions
if sys.argv[1] == '-l':
    print '\n'.join(rules[sys.argv[2]])
else:
    print nt_re.sub(expand, sys.argv[1])
