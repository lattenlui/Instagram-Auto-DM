#
#   TTTTTTTT  OOOOO    DDDDD     OOOOO 
#      T     O     O   D    D   O     O
#      T     O     O   D    D   O     O
#      T     O     O   D    D   O     O
#      T      OOOOO    DDDDD     OOOOO
# 
# Maybe*


import json
from instagramScraper import bot
from ask_gpt import askGPT
import sys

args = sys.argv
print(args)

def send_reply(uid, msg):
    reply = askGPT(msg)
    bot.send_message(reply, uid)

userid = args[1]
message = args[2]

print(userid)
print(message)


send_reply(userid, message)
