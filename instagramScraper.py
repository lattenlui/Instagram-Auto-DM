from instagpy import InstaGPy
from instabot import Bot
from mailHandler import sendMail
from ask_gpt import askGPT
from ask_gpt import subjectGPT
import time
import shutil

shutil.rmtree('config/')

# Is Instagram account getting banned? Refer -> https://github.com/iSarabjitDhiman/InstaGPy/blob/master/instagpy/docs/docs.md

# Instagram credentials for extracting contact information (REQUIRED)
usrname = 'karwisausetsh'
passwd = 'hjklasdf'
sentList = []
insta = InstaGPy()
insta.login(username=usrname, password=passwd)
bot = Bot()
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
        notGym = askGPT('give yes/no answer on if this could be bio of a trainer, gym, coach or someone related, say yes if unsure. ' + userTh['biography'])
        print(userTh['biography'])
        print(notGym)
        if notGym.lower() == 'yes' and userTh['follower_count'] > 100:
            return True
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
        all_posts = insta.get_hashtag_posts(tags, total=5)
        for post in all_posts:
            try:
                post_owner = post['node']['owner']['id']
                post_owners.append(post_owner)
            except:
                continue
    
    return post_owners



print(posts)

def validatedOwners(poste):
    owners = []
    for post in poste:
        print('\n \n' + post + '\n \n')
        if usrValid(post):
            print("Valid Whatever the username above this message is")
            owners.append(post)

    return owners

            

def runOwner(owner):
    # send first message here :)

    return    



def forValidOwners():
    tag = ['fitness', 'health', 'gym']
    posts = getPosts(tag)
    vOwners = validatedOwners(posts)

    for owner in validatedOwners():
        runOwner(owner)





# -------- DIVIDER ( Not using anything from here currently, sms/email stuff ) -------
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

