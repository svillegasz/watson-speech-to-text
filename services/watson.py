import requests
import os
import app
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('apikey', os.environ.get('WATSON_API_KEY'))
model = 'es-CO_BroadbandModel'

def transcribe(file_path):
    app.logger.info("Transcription process started: calling watson speech to text API")
    with open(file_path, 'rb') as data:
        response = requests.post('https://api.us-east.speech-to-text.watson.cloud.ibm.com/instances/%s/v1/recognize' % os.environ.get('WATSON_INSTANCE'), 
                data = data.read(),
                headers = {'Content-Type': 'application/octet-stream'},
                params = {'model': model},
                auth = auth)

    app.logger.info('Transcription process finished with status code %s and content:')
    json = response.json()
    app.logger.info(json)
    app.logger.info('Writing file transcript.txt with transcripted audio (first result/alternative)')
    f = open(app.TRANSCRIPT_FILE, 'w')
    alternative = json.get('results')[0].get('alternatives')[0]
    f.write(alternative.get('transcript'))
    f.close()
    app.logger.info('Confidence on alternative: %s' % alternative.get('confidence'))
