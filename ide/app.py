from flask import Flask, render_template
from flask_codemirror import CodeMirror

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

@app.route('/', methods=['GET','POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        text = form.source_code.data
    return render_template('index.html', form=form)

if __name__ == "__main__":
  codemirror.init_app(app)
