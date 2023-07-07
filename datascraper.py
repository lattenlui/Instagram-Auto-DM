from bs4 import BeautifulSoup
import requests
import re
import pandas as pd 
from selenium import webdriver 
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

link = 'https://hiftie.xyz/'

options = ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)
response = requests.get(link)
soup = BeautifulSoup(response.content, 'lxml')
driver.get(link)
html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
print(html)

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