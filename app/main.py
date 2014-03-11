from flask import Flask, request, render_template
import cfg

app = Flask(__name__)
app.debug = True

@app.route('/cfg')
def handler():
    rules = request.args.get('rules', '')
    base = request.args.get('base', '')
    if len(rules):
        cfg_rules = cfg.read_rules(rules.split('\n'))
        results = [cfg.expand(base, cfg_rules) for i in xrange(10)]
    else:
        results = []

    return render_template(
            'cfg.html',
            rules=rules,
            base=base,
            results=results
        )
