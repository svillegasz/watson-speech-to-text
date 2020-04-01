import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('apikey', 'EYt8BL9EbEmQQt2Hg4TXBukU9f_C74DASsm66d1LUWiL')
def transcribe(data):
    #r = requests.post('https://api.us-east.speech-to-text.watson.cloud.ibm.com/instances/ab86d099-97ae-4faa-877a-98ea2cbc8f6c/v1/recognize', 
    #              data = data,
    #              headers = {'Content-Type': 'application/octet-stream'},
    #             auth = auth)
    #jsno = r.json
    json = {
    'results': [
            {
                'alternatives': [
                    {
                    'confidence': 0.94, 
                    'transcript': 'several tornadoes touched down as a line of severe thunderstorms swept through Colorado on Sunday '
                    }
                ], 
                'final': True
            }
        ], 
        'result_index': 0
    }
    print(json)
    f = open('transcript.txt', 'w')
    f.write(json.get('results')[0].get('alternatives')[0].get('transcript'))
    f.close()