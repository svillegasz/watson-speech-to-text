from flask import Flask, render_template, request, redirect, url_for, send_file
from services.watson import transcribe
from forms.transcribe import TranscribeForm

app = Flask(__name__)
app.config.from_object('config')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TranscribeForm()
    if form.validate_on_submit():
        transcribe(form.audio.data)
        return send_file('transcript.txt', as_attachment = True)
    return render_template('transcribe.html', form=form)
