__author__ = 'George'
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_message(message, email, subject):
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login("george.mausshardt@gmail.com", "Jaerawildwater1920")

    msg = MIMEMultipart()

    msg['From'] = "george.mausshardt@gmail.com"
    msg['To'] = email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    s.send_message(msg)

    del msg

# send_message("Hi there!", "george.mausshardt@gmail.com", "TEST")

