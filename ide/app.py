from flask import Flask, render_template, request, url_for
from flask_socketio import SocketIO
import json
from predict import predict
from run import run

app = Flask(__name__)
app.config.from_object(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/classify', methods=['POST'])
def classify():
    text = request.form["code"]
    return json.dumps({'lang': predict(text)})


@app.route('/run', methods=['POST'])
def run_code():
    code = request.form["code"]
    lang = request.form["lang"]
    return json.dumps(run(code, lang))


socketio.run(app, host="0.0.0.0", log_output=True, debug=True)
