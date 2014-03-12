from flask import Flask, request, render_template
import cfg

app = Flask(__name__)
app.debug = True

subjects = ['quinoa', 'fracking']

def open_rules(name):
    rules = {}
    try:
        with open('rules/%s.rules' % name) as f:
            rules = cfg.read_rules(f)
    except IOError:
        pass
    return rules

base_rules = open_rules('base')

@app.route('/')
def index_handler():
    subject = request.args.get('subject', '')
    article = ''
    if subject:
        subject_rules = open_rules(subject)
        subject_rules.update(base_rules)
        subject_rules['SUBJECT'] = [subject]
        article = cfg.expand('START', subject_rules)

    return render_template('index.html', subjects=subjects, subject=subject, article=article)

@app.route('/cfg')
def cfg_handler():
    rules = request.args.get('rules', '')
    base = request.args.get('base', '')
    results = []
    if len(rules):
        cfg_rules = cfg.read_rules(rules.split('\n'))
        results = [cfg.expand(base, cfg_rules) for i in xrange(10)]

    return render_template('cfg.html', rules=rules, base=base, results=results)
