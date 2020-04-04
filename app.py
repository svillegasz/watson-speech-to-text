from flask import Flask
from views.transcribe import transcribe_page
import logging

app = Flask(__name__)
app.register_blueprint(transcribe_page)
app.config.from_object('config')
gunicorn_error_logger = logging.getLogger('gunicorn.error')
app.logger.handlers.extend(gunicorn_error_logger.handlers)
app.logger.setLevel(logging.DEBUG)
logger = app.logger
TEMP_FOLDER = 'temp'
TRANSCRIPT_FILE = '%s/transcript.txt' % TEMP_FOLDER

if __name__ == "__main__":
    app.run()
