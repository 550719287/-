#coding: utf-8  
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

sender = 'kong.ly@neusoft.com'
receiver = 'kong.ly@neusoft.com'
subject = 'python email test'
smtpserver = 'mail.neusoft.com'
username = 'kong.ly'
password = 'kly1234<><>'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = 'test message'

#构造附件  
att = MIMEText(open('D:/1.jpg', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="1.jpg"'
msgRoot.attach(att)
          
smtp = smtplib.SMTP()
smtp.connect('mail.neusoft.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()