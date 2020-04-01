from flask import Blueprint, render_template, request, redirect, url_for, send_file
from services.watson import transcribe
from forms.transcribe import TranscribeForm
import app

transcribe_page = Blueprint('transcribe', __name__)

@transcribe_page.route('/', methods=['GET', 'POST'])
def index():
    print('transcribe process start')
    app.logger.info('asdfasdfasfdasdf')
    form = TranscribeForm()
    if form.validate_on_submit():
        transcribe(form.audio.data)
        return send_file('transcript.txt', as_attachment = True)
    return render_template('transcribe.html', form=form)
