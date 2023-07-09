from instagpy import InstaGPy
import instaloader

# Is Instagram account getting banned? Refer -> https://github.com/iSarabjitDhiman/InstaGPy/blob/master/instagpy/docs/docs.md

# Instagram credentials for extracting contact information (REQUIRED)
usrname = ''
passwd = ''

insta = InstaGPy()
insta.login(username=usrname, password=passwd)

def usrValid(userid):

    L = instaloader.Instaloader()
    username = instaloader.Profile.from_id(L.context, userid).username

    try:
        usrInfo = insta.get_user_info(username)
        followers = usrInfo['data']['user']['edge_followed_by']['count']
        if followers < 100:
            return False

    except: 
        return False

    return True


def getUsrInfo(username):
    if not usrValid(username):
        return False
        
    usr_details = insta.get_user_data(username)['user']
    print(usr_details)
        
    return usr_details


def getPosts(tag):
    post_owners = []
    for tags in tag:
        all_posts = insta.get_hashtag_posts(tag,total=10)
        for post in all_posts:
            post_owner = post['node']['owner']['id']
            if usrValid(post_owner):
                post_owners.append(post_owner)
    
    return post_owners


getPosts('fitness')

def getContact():
    tag = ['fitness', 'health', 'gym']
    contacts = []
    post_owners = getPosts(tag)
    for owner in post_owners:
        contact = getUsrInfo(owner)
        contacts.append(contact)

    return contacts
