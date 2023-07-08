from instagpy import InstaGPy

# Is Instagram account getting banned? Refer -> https://github.com/iSarabjitDhiman/InstaGPy/blob/master/instagpy/docs/docs.md

# Instagram credentials for extracting contact information (REQUIRED)
usrname = 'sarbjeetkoursidhusarb@gmail.com'
passwd = 'BLACKS21@SAJRAS21'


insta = InstaGPy()
insta.login(username=usrname, password=passwd)

def usrDetails(username):
    def usrValid():
        usrInfo = insta.get_user_info(username)
        followers = usrInfo['data']['user']['edge_followed_by']['count']

        if followers < 5:
            return False
        return True

    def getUsrInfo():
        if not usrValid():
            return "This user account is too small to message."
        
        usr_details = insta.get_user_data(username)['user']
        print(usr_details)
            
    getUsrInfo()        

usrDetails('arq1es')

