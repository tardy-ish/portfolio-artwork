from flask import Flask, render_template, url_for
import os
import json

app = Flask(__name__)


@app.route('/')
@app.route('/<lang>',methods=["POST","GET"])
def index(lang='en'):
    translations = json.load(open('./static/translations.json',encoding='utf-8'))
    paintings = json.load(open('./static/paintings.json',encoding='utf-8'))

    return render_template(
        'artworks.html',
        lang=lang,
        paintings=paintings[lang],
        langP=translations[lang],
    )


if __name__ == '__main__':
    app.run(debug=True)