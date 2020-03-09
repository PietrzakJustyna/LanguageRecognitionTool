from flask import render_template, request

from tool.app import app

import tool.predictor as p


@app.route('/')
@app.route('/result')
def index():
    word = request.args.get('word')
    if word is not None:
        result = p.predict(word)
    else:
        result = "Nothing to predict yet"
    return render_template('index.html', result=result)
