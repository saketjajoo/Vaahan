import json
import requests

def get_vno(img):
    regions = ['fr', 'it']
    with open(img, 'rb') as fp:
        response = requests.post(
            'https://api.platerecognizer.com/v1/plate-reader/',
            files=dict(upload=fp),
            headers={'Authorization': 'Token 679d2b840e1a45d255896209ba8185389a2d7a5f'})
    json_data = response.json()
    parsed_json = (json.dumps(json_data))
    o = json.loads(parsed_json)
    #print(o["results"][0]["plate"])
    return o["results"][0]["plate"].upper()