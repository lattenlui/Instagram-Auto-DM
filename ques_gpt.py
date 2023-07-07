import openai

openai.api_key = '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'

info = 'developer who programs in python, can do meetings between 9am - 5pm ist'

question = "which time can we have a meeting?"


def askGPT(question, info):
    
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a" + info},
            {"role": "user", "content": question},

        ]
    )

    return response.choices[0].message["content"]



replyGPT = askGPT(question, info)

print(replyGPT)