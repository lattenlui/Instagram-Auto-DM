import flask
from flask import Flask, request, Response
import os, json, requests

app = Flask(__name__)

port = os.getenv('PORT', 3000)

@app.route('/f4c3b00kw3bh00k', methods=['GET'])
def webhook_verify():
    verify_token = 'msg-reciever'
    if request.args.get('hub.verify_token') == verify_token:
        return request.args.get('hub.challenge')
    return "Wrong verify token"

@app.route('/f4c3b00kw3bh00k', methods=['POST'])
def webhook_action():
    print('hi')
    data = json.loads(request.data.decode('utf-8'))  
    print(data)

    # Extract id and msg
    common = data['value']
    uid = common['sender']['id']
    msg = common['message']['text']

    os.system('python3 reply.py ' + uid + ' "' + msg + '"')

    return Response(response="EVENT RECEIVED", status=200)

app.run(host='0.0.0.0', port=port)

