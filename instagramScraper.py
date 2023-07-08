from instagpy import InstaGPy

insta = InstaGPy()

def usrValid(username):
    usrInfo = insta.get_user_info(username)
    followers = usrInfo['data']['user']['edge_followed_by']['count']
    print(followers)
    

usrValid('arq1es')

