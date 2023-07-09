from flask import Flask, jsonify, request
import flask
from mailHandler import getMail
from mailHandler import sendMail

app = Flask(__name__)
#Flask Port number
port = 5005



@app.route('/mails', methods = ['GET', 'POST'])
def mail():
    if(request.method == 'GET'):
        data = []
        # sending email list logic below
        for mail in getMail():
            data.append(mail)

        return data


@app.route('/sendmails', methods = ['POST'])
def sendManualMail():
    jsdata = request.form['javascript_data']
    sendMail(jsdata)
    return jsdata


@app.route('/sms', methods = ['GET', 'POST'])
def sms():
    if(request.method == 'GET'):
  
        # sending email list logic below
        data = "hello sms"
        return data



app.run(debug = True, port=port)
