#!/usr/bin/python
import sys, collections, json

rules = collections.defaultdict(list)
for line in sys.stdin:
    rule_name, rule = line.strip().split(' ', 1)
    rules[rule_name].append(rule)

print json.dumps(rules)
