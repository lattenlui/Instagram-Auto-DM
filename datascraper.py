from bs4 import BeautifulSoup
import requests
import re

link = 'https://hiftie.xyz/'



response = requests.get(link)
soup = BeautifulSoup(response.content, 'html.parser')

# Get Contact Information and remove duplticates
def getContact(html):

    def getEmail():
        email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,4}"
        emails = re.findall(email_pattern, str(html))
        emails = [*set(emails)]
        return emails


    Email = getEmail() 
    # Phone = getPhone()
    # Phone = [*set(Phone)]

    return Email #, Phone

Contact = getContact(soup)

print(Contact)