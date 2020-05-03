from flask import Flask, render_template, request, url_for
from flask_socketio import SocketIO

app = Flask(__name__)
app.config.from_object(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/test/', methods=['GET','POST'])
def test():
    if request.method == "POST":
        print(request.form["code"])
    return 'return'

socketio.run(app, host="0.0.0.0", log_output=True)
