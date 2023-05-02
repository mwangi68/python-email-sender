import os
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.message import EmailMessage
import ssl
import smtplib

email_sender="insert email you are sending from"
email_password= "insert password"
email_receiver="the one receiving the email"

subject="Learning to semd email with attachments"
content="Check this out"

em=MIMEMultipart()
em["From"]= email_sender
em["To"]= email_receiver
em["Subject"]= subject
body=MIMEText(content,"plain")
em.attach(body)
filename="test.txt" \insert name of preffered attachment

with open (filename,"r") as f:
    attachment=MIMEApplication(f.read(),Name=basename(filename))
    attachment['content-Disposition']='attachment;filename="{}"'.format(basename(filename))
em.attach(attachment)

context= ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smptp:
    smptp.login(email_sender,email_password)
    smptp.sendmail(email_sender, email_receiver, em.as_string())
