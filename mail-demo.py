import os
import smtplib
import threading
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

# If we want to send the email to multiple users then we just need to add all the emails like this
contacts = ['shubh28062000@gmail.com', 'ss4854@srmist.edu.in']

msg = EmailMessage()
msg['Subject'] = 'Invitation to my birthday party'
msg['From'] = EMAIL_ADDRESS
msg['Bcc'] = ', '.join(contacts) # all the contacts separated by a comma
msg.set_content(f'Hi, you are invited to my birthday party {contacts} which will be held on my birth date at my home. I look forward to meeting you on my birthday.')


#The code below is for sending an image attachment
# files = ['ricardo.jpg', 'ricardo_cat.jpg']

# for file in files:
#     with open(file, 'rb') as f:
#         file_data = f.read()
#         file_type = imghdr.what(f.name)
#         file_name = f.name

#     msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)


# The below code is for sending pdf files
# Files = ['DS CT3.pdf']

# for file in Files:
#     with open(file, 'rb') as f:
#         file_data = f.read()
#         file_name = f.name

#     msg.add_attachment(file_data, maintype='application', subtype='octect-stream', filename=file_name)


# def sendMail():
#     with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
#         smtp.ehlo() #this is to introduce ourselves to the server that we're going to use
#         smtp.starttls() #this is to encrypt the email
#         smtp.ehlo() #we gotta re run this after starting tls

#         smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

#         subject = 'Invitation to my birthday party'
#         body = f'Hi, you are invited to my birthday party {contacts} which will be held on my birth date at my home. I look forward to meeting you on my birthday.'

#         msg = f'Subject: {subject}\n\n{body}'

#         smtp.sendmail(EMAIL_ADDRESS, 'shubh28062000@gmail.com', msg)


# we can use SSL to get rid of the ehlo and starttls functions and this will run on port 465
def sendMailSSL():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


# sendMailSSL()

