from flask import render_template, request

from tool.app import app

import tool.predictor as p


@app.route('/')
@app.route('/result')
def index():
    word = request.args.get('word')
    if word is not None and word.isalpha():
        result = p.predict(word)
    else:
        word = ""
        result = "Nothing to predict yet. Please enter valid word to check"
    return render_template('index.html', result=result, word=word)
