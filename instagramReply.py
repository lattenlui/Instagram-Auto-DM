import flask
from flask import Flask, request, Response
import os

app = Flask(__name__)

port = os.getenv('PORT', 3000)


@app.route('/f4c3b00kw3bh00k', methods=['POST'])
def return_response():
    print(request.json)
    
    data = json.load(request.json)  

    if data == None:
        return Response(status=200)

    # Extract id and msg || REMOVE [0] if doesn't work
    common = data['entry'][0]['messaging'][0]
    uid = common['sender']['id']
    msg = common['message']['text']

    os.system('python3 reply.py ' + uid + ' "' + msg + '"')

    return Response(status=200)

@app.route('/f4c3b00kw3bh00k', methods=['GET'])
def webhook_verify():
    verify_token = 'msg-reciever'
    if request.args.get('hub.verify_token') == verify_token:
        return request.args.get('hub.challenge')
    return "Wrong verify token"


app.run(host='0.0.0.0', port=port)

