from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
app.config.from_object(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')


@socketio.on('code_text')
def handle_code_text(message):
    socketio.emit('code_text', message, broadcast=True)


socketio.run(app, host="0.0.0.0", log_output=True)
