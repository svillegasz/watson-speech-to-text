from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

# Set your classes here.

class TranscribeForm(FlaskForm):
    audio = FileField('Seleccionar un audio', validators=[FileRequired('No se seleccionó ningún audio.'), FileAllowed(['flac', 'mp3', 'wav', 'mpeg', 'ogg'], 'Formato no soportado, solo se permitén audios.')])
