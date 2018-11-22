import json
from flask import Response
import base64

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

def check(request):
    '''
    Takes a JSON body of {"image": base64 encoded image data}
    '''
    
    resp = Response()
    resp.headers.set('Content-Type','application/json')
    resp.headers.set('Access-Control-Allow-Origin', '*')
    resp.headers.set('Access-Control-Allow-Headers', 'Content-Type')
    
    if request.method == 'OPTIONS':
        resp.status_code = 204
        return resp

    request_json = request.get_json()
    image_data = request_json['image']
    image = types.Image(content=base64.b64decode(image_data))
    
    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = [label.description for label in response.label_annotations]
    
    has_teapot = bool('teapot' in labels)

    resp.response = json.dumps({"labels":labels,
                               	"is_good":has_teapot})
    
    return resp