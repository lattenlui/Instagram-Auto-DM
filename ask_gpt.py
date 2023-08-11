import openai
import time

from var import *


# Don't use this, use reply function below in most cases!
def askGPT(question):
    while True:
        try:
            response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                    {"role": "system", "content": "You are a" + info},
                    {"role": "user", "content": question},
                ]
            )
            responseGPT = response.choices[0].message["content"]
            msgHistory.append(responseGPT)

            break
        except Exception as e:
            print(e)
            time.sleep(20)
            continue
    
    return responseGPT

def subjectGPT(message):
    return askGPT("write an email subject for the message below \n" + message)

#pending
def reply(msgHistory, question):
    return askGPT(str(msgHistory) + question)