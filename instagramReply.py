import flask
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/f4c3b00kw3bh00k', methods=['POST'])
def return_response():
    print(request.json)
    
    data = json.load(request.json)

    # Extract id and msg || REMOVE [0] if doesn't work
    common = data['entry'][0]['messaging'][0]
    uid = common['sender']['id']
    msg = common['message']['text']

    os.system('python3 reply.py ' + uid + ' "' + msg + '"')

    return Response(status=200)

app.run()

