import imap_tools
import smtplib
from email.mime.text import MIMEText
import imaplib
import email
# Gmail Username and Password for emails:
username = 'b.sajras21@gmail.com'
password = 'qpwgiorvmobwrgze'

# Using gmail to send emails.
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465

# Fetching gmails's emails
SERVER = 'imap.gmail.com'


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

