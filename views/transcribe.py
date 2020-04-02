import app
import os

from flask import Blueprint, render_template, request, redirect, url_for, send_file, make_response
from services.watson import transcribe
from werkzeug.utils import secure_filename
from pathlib import Path

transcribe_page = Blueprint('transcribe', __name__)

@transcribe_page.route('/', methods=['GET', 'POST'])
def index():
    return render_template('transcribe.html')

@transcribe_page.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    Path(app.TEMP_FOLER).mkdir(parents=True, exist_ok=True)
    save_path = os.path.join(app.TEMP_FOLER, secure_filename(file.filename))
    with open(save_path, 'ab') as f:
        # Goto the offset, aka after the chunks we already wrote 
        f.seek(int(request.form['dzchunkbyteoffset']))
        f.write(file.stream.read())
    return make_response(('Uploaded Chunk', 200))
