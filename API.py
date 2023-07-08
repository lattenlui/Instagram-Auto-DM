from flask import Flask, jsonify, request
import flask

app = Flask(__name__)
#Flask Port number
port = 5000


@app.route('/mails', methods = ['GET', 'POST'])
def mail():
    if(request.method == 'GET'):
  
        # sending email list logic below
        data = "hello world"

        return data


@app.route('/sms', methods = ['GET', 'POST'])
def sms():
    if(request.method == 'GET'):
  
        # sending email list logic below
        data = "hello sms"

        return data



app.run(debug = True, port=port)
