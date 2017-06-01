import sys

from flask import Flask, request, send_file
from flask.json import jsonify
from verify import plarralx_verifiy

app = Flask(__name__)


@app.route('/', methods=['GET'])
def verify():
    return "Hello world", 200


@app.route('/verify', methods=['GET'])
def webhook():

    # Params
    try:
        image_url = request.args['image_url']
    except KeyError:
        return "Must include image_url arg", 400

    try:
        result = plarralx_verifiy(image_url=image_url)
    except ValueError:
        return "image_url invalid", 400

    return jsonify(result)


def log(message):  # simple wrapper for logging to stdout on heroku
    print(str(message))
    sys.stdout.flush()


if __name__ == '__main__':
    app.run(debug=True)