import openai
import time

# TODO fetch from mail/sms/database
msgHistory = []

calendy_link = ''

# Change this :) 
openai.api_key = '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'

info = "employee from agency which helps fitness trainers get more clients by performing advertisements for them.This Agency Is an online Marketing Agency, we provide Facebook and instagram ads. We work with Fitness Coaches and Online trainers and gyms, and we Get them More Clients and revenue through ads! Our Outreach methods outreach through Instagram, Facebook, Email, Linkedin and cold calling. The agency you work in has helped alot of trainers by getting them thousands of clients. You can book a meeting with us using the calendy app at this link: {calendy_link}. "
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

def reply(msgHistory, question):
    return askGPT(str(msgHistory) + question)
