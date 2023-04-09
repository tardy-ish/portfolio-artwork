from flask import Flask, render_template, url_for
import os
import json

app = Flask(__name__)


@app.route('/')
@app.route('/<lang>',methods=["POST","GET"])
def index(lang='en'):
    art = list(os.listdir('static/assets/artworks'))
    translations = json.load(open('static/translations.json',encoding='utf-8'))
    paintingNames = []
    paintingSizes = []
    for f in art:
        s = f[:-4].split('_')
        paintingNames.append(s[1])
        paintingSizes.append(s[2])

    return render_template(
        'artworks.html',
        files=art,
        sizes=paintingSizes,
        names=paintingNames,
        lang=lang,
        langP=translations[lang],
    )


if __name__ == '__main__':
    app.run(debug=True)