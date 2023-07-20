import flask
from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/f4c3b00kw3bh00k', methods=['POST'])
def return_response():
    print(request.json)
    
    data = json.load(request.json)

    # Extract id and msg
    uid = ''
    msg = ''

    os.system('python3 reply.py ' + uid + ' ' + msg)

    return Response(status=200)

app.run()

