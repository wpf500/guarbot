import random, collections
from flask import Flask, request, render_template
import cfg

app = Flask(__name__)
app.debug = True

subjects = {
    'quinoa': 'Quinoa',
    'selfie': 'Selfie',
    'sexism': 'Sexism',
    'psc': 'Pamela Stephenson Connelly'
}

base_rules = cfg.read_rules(open('data/base.rules'))

def get_rules(subject):
    rules = cfg.read_rules(open('data/%s.rules' % subject))
    rules['SUBJECT'] = subject
    # add base rules
    for rule_name, rule in base_rules.iteritems():
        if rule_name not in rules:
            rules[rule_name] = []
        rules[rule_name].extend(rule)
    return rules

@app.route('/')
def index_handler():
    subject = request.args.get('subject', '')
    tree = []
    if subject:
        rules = get_rules(subject)
        article = cfg.expand('START', rules, tree)
    else:
        rules = {}
        article = ''

    return render_template('index.html',
        subjects=subjects, subject=subject,
        article=article, rules=rules, tree=tree)

@app.route('/cfg')
def cfg_handler():
    rules = request.args.get('rules', '')
    base = request.args.get('base', '')
    results = []
    if len(rules):
        cfg_rules = cfg.read_rules(rules.split('\n'))
        results = [cfg.expand(base, cfg_rules) for i in xrange(10)]

    return render_template('cfg.html', rules=rules, base=base, results=results)
