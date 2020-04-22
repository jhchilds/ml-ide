from flask import Flask, render_template, request
from flask_codemirror import CodeMirror
from flask_socketio import SocketIO

from flask_wtf import FlaskForm
from flask_codemirror.fields import CodeMirrorField
from wtforms.fields import SubmitField


class MyForm(FlaskForm):
    source_code = CodeMirrorField(language='python',
                                config={'lineNumbers' : 'true'})
    submit = SubmitField('Submit')


SECRET_KEY = 'secret!'
# mandatory
CODEMIRROR_LANGUAGES = ['python', 'html']
# optional
CODEMIRROR_THEME = '3024-day'
CODEMIRROR_ADDONS = (
     ('display','placeholder'),
)

app = Flask(__name__)
app.config.from_object(__name__)
codemirror = CodeMirror(app)
socketio = SocketIO(app, cors_allowed_origins='*')


@app.route('/', methods=['GET','POST'])
def index():
    code_form = MyForm()
    if code_form.validate_on_submit():
        text = code_form.source_code.data
    return render_template('index.html', form=code_form)


@socketio.on('code_text')
def handle_code_text(message):
    socketio.emit('code_text', message, broadcast=True)


socketio.run(app, host="0.0.0.0", log_output=True)
