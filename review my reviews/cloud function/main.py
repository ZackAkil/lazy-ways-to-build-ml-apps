import json

from flask import Response

from google.cloud import automl_v1beta1


prediction_client = automl_v1beta1.PredictionServiceClient()
project_id = YOUR PROJECT ID
model_id = YOUR MODEL ID
name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)

def predict(request):
    
    resp = Response()
    resp.headers.set('Content-Type','application/json')
    resp.headers.set('Access-Control-Allow-Origin', '*')
    resp.headers.set('Access-Control-Allow-Headers', 'Content-Type')
    
    if request.method == 'OPTIONS':
        resp.status_code = 204
        return resp
    
    print(name)
    print(prediction_client)
    request_json = request.get_json()
    payload = {'text_snippet': {'content': request_json['content'], 'mime_type': 'text/plain' }}
    params = {}
    request = prediction_client.predict(name, payload, params)
    
    print(request)
    
    output = [{'label':p.display_name, 'score':p.classification.score} for p in request.payload]
    
    print(output)
    
    resp.response = json.dumps(output)
    
    return resp