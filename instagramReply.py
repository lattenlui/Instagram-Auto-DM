import flask
import json
from instagramScraper import bot
from flask import Flask, request, Response
from ask_gpt import askGPT
app = Flask(__name__)

def send_reply(uid, msg):
    reply = askGPT(msg)
    bot.send_message(reply, uid)

def send_message(data):
    print(data)

    # Extract both
    userid = '' 
    message = ''

    send_reply(userid, message)

    return


@app.route('/f4c3b00kw3bh00k', methods=['POST'])
def return_response():
    print(request.json)
    
    data = json.load(request.json)
    send_message(data)

    return Response(status=200)

app.run()

# reply to message recieved on webhook accordingly


