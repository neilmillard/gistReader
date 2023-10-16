from flask import Flask, send_file
from src.reader import Reader

app = Flask(__name__)


@app.route('/')
def hello_world():
    return ('Equal Experts Gist API User explorer.'
            'try <a href="octocat>octocat</a>')


@app.route('/favicon.ico/')
def favicon():
    return send_file('src/favicon.ico', mimetype='image/gif')


@app.route('/<name>/')
def get_public_gists(name):
    reader = Reader(name)
    gists = reader.getGists()

    return gists


if __name__ == '__main__':
    app.run(host='0.0.0.0')
