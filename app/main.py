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

def merge(a, b):
    for k, v in b.iteritems():
        if k in a:
            a[k].extend(v)
        else:
            a[k] = v

tag_whitelist = [
    'RB', 'CD', 'VB', 'VBD', 'VBG', 'VBZ', 'JJ', 'JJR', 'JJS',
    'NN', 'NNS', 'NNP', 'NNPS'
]
word_blacklist = ['be', 'is', '\'s', '(', ')', 'was', 'n\'t', 'so', 'have', 'here']

def generate_rules(subject):
    rules = {}
    words = collections.defaultdict(list)
    for line in open('data/%s.tags' % subject):
        word, tag = line.strip().rsplit('/', 1)
        if word not in word_blacklist:
            words[tag].append(word)
    for t in tag_whitelist:
        if len(words[t]) < 15:
            rules[t] = words[t]
        else:
            rules[t] = random.sample(words[t], 15)
    return rules

base_rules = cfg.read_rules(open('data/base.rules'))

@app.route('/')
def index_handler():
    subject = request.args.get('subject', '')
    rules = {}
    article = ''
    tree = []
    if subject:
        rules = generate_rules(subject)
        rules['SUBJECT'] = [subject]
        merge(rules, base_rules)
        merge(rules, cfg.read_rules(open('data/%s.rules' % subject)))

        article = cfg.expand('START', rules, tree)

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
