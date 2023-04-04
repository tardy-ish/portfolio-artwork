from flask import Flask, render_template
import os

app = Flask(__name__)


@app.route('/')
@app.route('/en')
def index():
    art = list(os.listdir('./static/assets/artworks'))
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
    )


if __name__ == '__main__':
    app.run(debug=True)