import imap_tools
import smtplib
from email.mime.text import MIMEText
import imaplib
import email
import re
import email_listener
from ask_gpt import reply


# Gmail Username and Password for emails:
username = 'b.sajras21@gmail.com'
password = 'gglmehzwxjonsjsg'
mail_folder = 'inbox'
# Using gmail to send emails.
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465

# Fetching gmails's emails
SERVER = 'imap.gmail.com'
def getEmail(text):
    email_pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,4}"
    emails = re.findall(email_pattern, str(text))
    emails = [*set(emails)]
    return emails

def sendMail(mail_message, subject, to_addrs):
    from_addr = username
    if not isinstance(to_addrs, list):
        list(to_addrs)

    message = MIMEText(mail_message)
    message['subject'] = subject
    message['from'] = from_addr
    message['to'] = ', '.join(to_addrs)

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)

    server.login(username, password)
    server.sendmail(from_addr, to_addrs, message.as_string())
    server.quit()



def getMail():
    mail = imaplib.IMAP4_SSL(SERVER)
    mail.login(username, password)
    mail.select('inbox')
    status, data = mail.search(None, 'ALL')

    mail_ids = []

    all_emails = []


    for block in data:
        mail_ids += block.split()

    # now for every id we'll fetch the email
    # to extract its content
    for i in mail_ids:

        status, data = mail.fetch(i, '(RFC822)')
        for response_part in data:
            # so if its a tuple...
            if isinstance(response_part, tuple):
                message = email.message_from_bytes(response_part[1])

                mail_from = message['from']
                mail_subject = message['subject']

                if message.is_multipart():
                    mail_content = ''


                    for part in message.get_payload():

                        if part.get_content_type() == 'text/plain':
                            mail_content += part.get_payload()
                else:
                    mail_content = message.get_payload()

                this = [mail_from, mail_subject, mail_content]
                all_emails.append(this)
    return all_emails
# send_mail('hello', 'subject', 'blackyshhi@gmail.com')

def cleanMail():
    get_mail = getMail()
    cleaned_mail = []
    for mail in get_mail:
        mail[0] = getEmail(mail[0])
        for email in mail[0]:
            if email == username:
                mail[0].remove(email)

        print(str(mail[2]))
    
        
        cleaned_mail.append(mail[2])
    
    # print(cleaned_mail)
    return cleaned_mail


def mailReply(smth_idk, mail):
    print(smth_idk)
    print(mail)


# Always run, replies only doesn't send first.
def mailListener():
    el = email_listener.EmailListener(username, password, mail_folder, attachment_dir='./attachments')
    el.login()
    el.listen(60, mailReply)

