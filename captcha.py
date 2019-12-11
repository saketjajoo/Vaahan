import json
import requests

def get_text_from_captcha(img_path):
    payload = {'isOverlayRequired': False,
                   'apikey': "edfedcdc0788957",
                   'language': "eng",
               'OCREngine' : 2
                   }

    with open(img_path, 'rb') as fp:
        response = requests.post(
            "https://api.ocr.space/parse/image",
            files={img_path: fp},
                              data=payload)

    x = json.loads(response.content.decode())

    y = x["ParsedResults"][0]["ParsedText"]
    return str(y)