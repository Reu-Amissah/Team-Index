from django.test import TestCase

# Create your tests here.
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_sender = "teamind3x@gmail.com"
email_password = "TeamInd3xPrep7"
subject = "Alpha test for Prep"

with open('lms/testemails/testemails.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        text = "Hello "+line[2] + ", You are recieving this email because you signed up for our alpha test. This is a test transmission. Do not reply. This is an automated email"
       
        send_email_to = line[3]
        message = MIMEMultipart()
        message['From'] = email_sender
        message['To'] = send_email_to
        message['Subject'] = subject
        message.attach(MIMEText(text, "plain"))
        text  = message.as_string()

        print(line[3])
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(email_sender, email_password)
        server.sendmail(email_sender, send_email_to, text)

        server.quit()