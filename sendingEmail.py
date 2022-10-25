from email.message import EmailMessage
from logging import NOTSET
import mimetypes
message = EmailMessage()
# print(message)

sender = "827johndoe@gmail.com"
recipient = "uxair.abs@gmail.com"

# NOTES
# From, To, and Subject are examples of email header fields.
# They’re key-value pairs of labels and instructions used by
# email clients and servers to route and display the email.
# They’re separate from the email's message body, which is
# the main content of the message.

message['From'] = sender
message["To"] = recipient
message["Subject"] = "Greetings from {} to {}".format(sender, recipient)

body = """Hi there!
I'm Uxair Abbas and email library"""
message.set_content(body)

# to check what sort of file you are sending 
import os.path
attachment_path = "assets/starwar4.jpg"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
# print(mime_type)

# seperate the mimetype and subtype 
mime_type, mime_subtype = mime_type.split('/', 1)
# print(mime_type)
# print(mime_subtype)

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=os.path.basename(attachment_path))

# print(message)

import smtplib
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')

# setting password and username
import getpass
mail_pass = getpass.getpass('Enter your Password?')
print(mail_pass)

mail_server.login(sender, mail_pass)
mail_server.send_message(message)
mail_server.quit()