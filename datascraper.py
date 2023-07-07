from bs4 import BeautifulSoup
import requests
import re


r = requests.get('https://arqies.com')
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,4}"

# Get emails and remove duplticates
emails = re.findall(email_pattern, str(soup))
emails = [*set(emails)]

print(emails)
