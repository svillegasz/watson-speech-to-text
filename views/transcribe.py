import app
import os
import shutil
import threading

from flask import Blueprint, render_template, request, make_response, jsonify
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
    if (int(request.form['dzchunkindex']) == 0):
        shutil.rmtree(app.TEMP_FOLDER, ignore_errors=True)
        Path(app.TEMP_FOLDER).mkdir(parents=True, exist_ok=True)
    save_path = os.path.join(app.TEMP_FOLDER, secure_filename(file.filename))
    with open(save_path, 'ab') as f:
        # Goto the offset, aka after the chunks we already wrote 
        f.seek(int(request.form['dzchunkbyteoffset']))
        f.write(file.stream.read())
    if ((int(request.form['dzchunkindex']) + 1) == int(request.form['dztotalchunkcount'])):
        transcribe_thread = threading.Thread(target=transcribe, args=(save_path,))
        transcribe_thread.start()
    return make_response(('Uploaded Chunk', 200))

@transcribe_page.route('/transcription', methods=['GET'])
def get_transcription():
    if Path(app.TRANSCRIPT_FILE).is_file():
        with open(app.TRANSCRIPT_FILE, 'r') as file: 
            return jsonify({
                'file': file.read(),
                'status': 'COMPLETED'
            })
    return jsonify({
                'status': 'IN_PROGRESS'
            })
