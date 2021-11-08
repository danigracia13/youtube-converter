import smtplib

name = "Dani"
last_name = "Gracia"
email = "danigraciaquiroga@gmail.com"
message = "There's a error in the mp4 ... due to this i cant download my file"

sender = 'no_reply@youtubeconverter.com'
receivers = ['ytconverter.contact@gmail.com']

message = """From: No Reply <no_reply@youtubeconverter.com>
To: Person <ytconverter.contact@gmail.com>
Subject: New Contact Form Submission

Name -> {name}
Last Name -> {last_name}
Email -> {email}
Message:
{message}
"""

smtpObj = smtplib.SMTP('localhost')
smtpObj.sendmail(sender, receivers, message)         
print("Successfully sent email")


"""try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print("Successfully sent email")
except:
   print("Error: unable to send email")"""