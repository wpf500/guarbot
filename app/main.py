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

@app.route('/')
def index_handler():
    return render_template('index.html', subjects=subjects)

@app.route('/cfg')
def cfg_handler():
    return render_template('cfg.html')
