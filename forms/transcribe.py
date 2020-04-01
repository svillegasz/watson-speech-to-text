from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

# Set your classes here.

class TranscribeForm(FlaskForm):
    audio = FileField('audio', validators=[FileRequired('Archivo requerido'), FileAllowed(['flac', 'mp3', 'wav', 'mpeg', 'ogg'], 'Solo audio vida!')])
