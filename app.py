from flask import Flask
from views.transcribe import transcribe_page

app = Flask(__name__)
app.register_blueprint(transcribe_page)
app.config.from_object('config')
logger = app.logger

if __name__ == "__main__":
    app.run()
