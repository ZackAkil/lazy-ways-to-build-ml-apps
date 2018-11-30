import json

def model(x):
    return int(x[6] < 3.5)


def pred(request):

    request_json = request.get_json()
    
    input_data = request_json['input']
    
    return json.dumps({'prediction': model(input_data)})