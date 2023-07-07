import imap_tools
import smtplib
from email.mime.text import MIMEText

# Gmail Username and Password for emails:
username = 'origin@gmail.com'
password = 'password'

# Using gmail to send emails.
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465

def send_mail(mail_message, subject, to_address):
    from_address = username
    if not isinstance(to_address, list):
        list(to_address)

    message = MIMEText(mail_message)
    message['subject'] = subject
    message['from'] = from_addr
    message['to'] = ', '.join(to_addrs)

    server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)

    server.login(username, password)
    server.sendmail(from_addr, to_addrs, message.as_string())
    server.quit()