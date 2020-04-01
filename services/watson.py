import requests
import os
import app
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('apikey', os.environ.get('WATSON_API_KEY'))
model = 'es-CO_BroadbandModel'

def transcribe(data):
    app.logger.info("acaaaaaaaaaaaaaaaaaaaaaAAåå")
    print('https://api.us-east.speech-to-text.watson.cloud.ibm.com/instances/%s/v1/recognize' % os.environ.get('WATSON_INSTANCE'))
    response = requests.post('https://api.us-east.speech-to-text.watson.cloud.ibm.com/instances/%s/v1/recognize' % os.environ.get('WATSON_INSTANCE'), 
            data = data,
            headers = {'Content-Type': 'application/octet-stream'},
            params = {'model': model},
            auth = auth)
    print(response)
    json = response.json()
    print('Watson trascription success: %s' % json)
    f = open('transcript.txt', 'w')
    f.write(json.get('results')[0].get('alternatives')[0].get('transcript'))
    f.close()
