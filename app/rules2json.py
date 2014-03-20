#!/usr/bin/python
import sys, json, cfg
print json.dumps(cfg.read_rules(sys.stdin))
