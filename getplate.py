import json
import requests

def get_vno(img):
    regions = ['fr', 'it']
    with open(img, 'rb') as fp:
        response = requests.post(
            'https://api.platerecognizer.com/v1/plate-reader/',
            files=dict(upload=fp),
            headers={'Authorization': 'Token YOUR_API_TOKEN'})
    json_data = response.json()
    parsed_json = (json.dumps(json_data))
    o = json.loads(parsed_json)
    #print(o["results"][0]["plate"])
    return o["results"][0]["plate"].upper()
