import os
import math
import random
import smtplib
from python_http_client.exceptions import HTTPError


import configparser
from tkinter import *
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content

# config = configparser.ConfigParser()
# config.read("config.ini")

# def sendMailUsingSendGrid(API,from_email,to_emails,subject,html_content):
#     if API!=None and from_email!=None and len(to_emails)>0:
#         message = Mail(from_email,to_emails,subject,html_content)
#         try:
#             # sg = SendGridAPIClient(API)
#             response = sg.send(message)
#             print(response.status_code)
#             print(response.body)
#             print(response.headers)
#         except Exception as e:
#             print(e.message)




# try:
#     settings = config["SETTINGS"]
# except:
#     settings = {}

# API = settings.get("APIKEY",None)
# from_email = settings.get("FROM",None)
# # to_emails = settings.get("TO","")

def sendMail(email):
    try:
        sg = SendGridAPIClient('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')
        from_email = Email("kungumaakshatra@gmail.com")  # Change to your verified sender
        to_email = email
        subject = "Authenication"
        digits="0123456789"
        OTP=""
        for i in range(6):
            OTP+=digits[math.floor(random.random()*10)]
        otp = OTP + " is your OTP"
        html_content = otp
        mail = Mail(from_email, to_email, subject, html_content)

# Get a JSON-ready representation of the Mail object
        mail_json = mail.get()

# Send an HTTP POST request to /mail/send


        response = sg.client.mail.send.post(request_body=mail_json)
        print(response.status_code)
        print(response.headers)
    except HTTPError as e:
        print(e.to_dict)
    #return otp

#sendMailUsingSendGrid(from_email,to_email,subject,html_content)



# address_info = address.get()

# email_body_info=email_body.get()

# server.sendmail(sender_email,address_info,email_body_info)
# print("Message Sent")
# address_entry.delete(0,END)
# email_body_entry.delete(0,END)





# app=Tk()
# app.geometry("500x500")
# app.title("Python email sending app")
# heading = Label(text="Python mail sending app", bg="yellow", fg="black",font="10",width="500")
# heading.pack()

# address_field= Label(text="Recipent Address :")
# # email_body_field= Label(text="Message")

# address_field.place(x=15,y=70)
# # email_body_field.place(x=15,y=140)

# address = StringVar()
# # email_body =StringVar()
# address_entry=Entry(textvariable=address,width="30")
# # email_body_entry=Entry(textvariable=email_body,width="20")
# address_entry.place(x=15,y=100)
# # email_body_entry.place(x=15,y=180)
# address_info = address.get()
# # email_body_info=email_body.get()

# button=Button(app,text="Send Message",bg="grey",command= sendMail,width="30",height="2")
# # if(email_body_info==otp):
# #     print("verified")
# button.place(x=15,y=220)
# mainloop()