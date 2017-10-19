__author__ = 'George'
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_message(message):
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("george.mausshardt@gmail.com", PASSWORD)

    msg = MIMEMultipart()

    msg['From'] = "george.mausshardt@gmail.com"
    msg['To'] = "george.mausshardt@gmail.com"
    msg['Subject'] = "TEST MESSAGE"

    msg.attach(MIMEText(message, 'plain'))

    s.send_message(msg)

    del msg

send_message("Hi there!")

