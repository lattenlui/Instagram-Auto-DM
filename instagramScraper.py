from instagpy import InstaGPy
from instabot import Bot
from ask_gpt import askGPT
from ask_gpt import subjectGPT
import time
import shutil

from var import *

try:
    shutil.rmtree('config/')
except: 
    print('no dir config')

# Instagram credentials for extracting contact information (REQUIRED)

insta = InstaGPy()
bot = Bot()
insta.login(username=usrname, password=passwd, save_session=False)

time.sleep(3)

instaBot = bot.login(username=usrname, password=passwd)

def getEmail(text):
    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,4}"
    emails = re.findall(email_pattern, str(text))
    emails = [*set(emails)]
    return emails


def usrValid(userid):
    userInfo = bot.get_user_info(userid)

    try:
        userTh = userInfo
        print(userTh['biography'])
        if userTh['follower_count'] > 100:
            notGym = askGPT( isValidVar + userTh['biography'])
            if notGym.lower() == 'yes':
                return True
            else:
                return False
        else:
            return False

    except: 
        return False



def getUsrInfo(username):
    if not usrValid(username):
        return False
        
    usr_details = insta.get_user_data(username)['user']
        
    return usr_details


def getPosts(tag):
    post_owners = []

    for tags in tag:
        all_posts = insta.get_hashtag_posts(tags, total=1)
        for post in all_posts:
            try:
                post_owner = post['node']['owner']['id']
                post_owners.append(post_owner)
            except:
                continue
        time.sleep(delay)
    return post_owners


def validatedOwners(poste):
    owners = []
    for post in poste:
        print(post)
        if usrValid(post):
            print("Valid Whatever the username above this message is")
            owners.append(post)

    return owners

            

def runOwner(owner):
    # send first message here :)
    ownerUsername = bot.get_username_from_user_id(owner)
    userInfo = bot.get_user_info(owner)['biography']
    message = 'Hi ' + ownerUsername+ '. ---'
    # TODO message = askGPT('write a message telling about this agency to a person with username ' + str(ownerUsername) + ' and bio as follows ' + str(userInfo) ) 
    print(ownerUsername + '\n \n' + message)
    bot.send_message(message, ownerUsername)

    return    



def forValidOwners():
    
    posts = getPosts(tag)
    vOwners = validatedOwners(posts)

    for owner in vOwners:
        runOwner(owner)

def start():
    print('started \n \n \n \n \n \n \n \n \n \n \n')
    while True:
        forValidOwners()
        time.sleep(delay)


# -------- DIVIDER ( Not using anything from here currently, sms/email stuff ) -------
'''
def getContact():
    tag = ['fitness', 'health', 'gym']
    contacts = []
    post_owners = getPosts(tag)
    for owner in post_owners:
        contact = getUsrInfo(owner)
        contacts.append(contact)

    return contacts


def emails():
    contacts = getContact()
    for contact in contacts:
        mail = getEmail(str(contact))

        if mail:
            if mail not in sentList:
                sendMail(to_addrs=mail, 
                subject='Get more clients.', 
                mail_message='Hi, I am Jermy. I am from a agency named NIR which helps fitness trainers and gyms find more clients. Are you interested?'
        )
            sentList.append(sentList)

'''