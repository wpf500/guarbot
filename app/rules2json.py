#!/usr/bin/env python
import sys, json, cfg
print json.dumps(cfg.read_rules(sys.stdin))
