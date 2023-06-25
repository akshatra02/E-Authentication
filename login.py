# from home import *
import tkinter as tk
from tkinter import  *
import cv2,os
import tkinter.ttk as ttk
import tkinter.font as font
import numpy as np
# from PIL import Image, ImageTk
import PIL.Image
import csv
import json
import pandas as pd
# from mail import *
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

#import shutil
#import pandas as pd
#import datetime
#import time


window=tk.Tk()
window.title("Login/Logout Website")
window.geometry('1366x750')
c=Canvas(window,bg="gray16",height=200,width=200)
filename = PhotoImage(file="pictures\\BG2.png")
background_label=Label(window,image = filename)
background_label.place(x=0,y=0, relwidth=1, relheight=1)
login_label= tk.Label(window, text="USER AUTHENTICATION" ,bg="#71B280"  ,fg="#05445E"  ,width=100 ,height=1,font=('times', 35, 'bold')).pack(fill = 'x')
# Button(window,text="click",width=20,command=lambda : change(window)).grid()

def change():
    window.destroy()
    import home


####Login Credentials


#####Loading Data from txt file
def loading_data():
    file=open('data.txt','r',encoding='utf-8')
    data=json.load(file)
    file.close()
    return data
##Saving Data to .txt file
def saving_data(data):
    file=open('data.txt','w',encoding='utf-8')
    json.dump(data,file,ensure_ascii=False)
    file.close()

##saving data in a variable
#data=dict()
data=loading_data()
print(data)

style = ttk.Style()
style.configure('GradientButton', background='linear-gradient(90deg, #134E5E, #71B280)')






#HEADINGS
login_label= tk.Label(window, text="Login Here" ,bg="#05445E"  ,fg="#71B280"  ,width=20 ,height=1,font=('times', 30, 'bold')) 
login_label.place(x=450, y=150)
msg_label=tk.Label(window,text="Notification: ",bg='#05445E' ,fg='#71B280',width=10,height=1,font=('times',20,'bold'))
msg_label.place(x=300,y=500)
message = tk.Label(window,text="",bg="#71B280" ,fg="#0F2027", width=30, height=1, font=('times',20,'bold'))
message.place(x=500,y=500)



#Login FIEDLS 
lbl = tk.Label(window, text="Enter ID :",width=10,height=1  ,fg="#05445E" ,bg="#71B280" ,font=('times', 15, ' bold ') ) 
lbl.place(x=430, y=210)

txt = tk.Entry(window,width=25  ,fg="#0F2027" ,bg="#71B280",font=('times', 15, ' bold '))
txt.place(x=690, y=210)

lbl2= tk.Label(window, text="Enter Password :",width=15  ,height=1  ,fg="#05445E" ,bg="#71B280" ,font=('times', 15, ' bold ') ) 
lbl2.place(x=430, y=250)

txt2 = tk.Entry(window,width=25  ,bg="#71B280" ,show='*',fg="#0F2027",font=('times', 15, ' bold '))
txt2.place(x=690, y=250)

address_field1= tk.Label(window, text="E-mail Address :",width=20,height=1  ,fg="#05445E" ,bg="#71B280" ,font=('times', 15, ' bold ') )
address_field1.place(x=430,y=290)
address = StringVar()
address_entry1=tk.Entry(window,textvariable=address,width=25  ,bg="#71B280" ,fg="#0F2027",font=('times', 15, ' bold '))
address_entry1.place(x=690,y=290)
mail=address_entry1.get()

OTP= tk.Label(window, text="OTP :",width=20,height=1  ,fg="#05445E" ,bg="#71B280" ,font=('times', 15, ' bold ') )
OTP.place(x=430,y=385)
otp_entry=tk.Entry(window,width=25  ,bg="#71B280" ,fg="#0F2027",font=('times', 15, ' bold '))
otp_entry.place(x=690,y=385)
o=otp_entry.get()
print(o)

#Main

def login_clear():
    txt.delete(0,'end')
    txt2.delete(0,'end')
    address_entry1.delete(0,'end')
    #res = ""
    #txt.configure(text= res)
    #txt2.configure(text=res)

################## Login_Functions   ######################

#When Submit button is clicked We have to Track the Person from our data through web cam
    
def TrackImages(UserId):
    recognizer = cv2.face.LBPHFaceRecognizer_create()#cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainingImageLabel\Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df=pd.read_csv("Details\Details.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX          
    run_count=0;run=True
    while run:
        
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
            print(Id, conf)
            if(conf < 50):
                aa=df.loc[df['Id'] == Id]['Name'].values
                tt=str(Id)+"-"+aa
                if (str(Id)==UserId):
                    message.configure(text="Face Recognized Successfully")
                    run=False
                    cam.release()
                    change()
            else:
                Id='Unknown'                
                tt=str(Id)            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(255,255,255),2)        
        run_count += 1    
        cv2.imshow('im',im) 
        if (cv2.waitKey(1)==ord('q') or run_count==150):
            message.configure(text="Unable to Recognise Face")
            break
    
    cam.release()
    cv2.destroyAllWindows()

    


def login_submit():
    a=txt.get()
    b=txt2.get()
    o=otp_entry.get()
    t=OTP
    if (a in data):
        if(data[a] [0] == b):
        
            if(t!=o):
                TrackImages(a)
            else:
                message.configure(text="Incorrect OTP")
        else:
            message.configure(text="Id and Password does not Match")
    else:
        message.configure(text="Entered Id does not Exists")

    login_clear()


#Email verification
def sendMail():
    try:
        sg = SendGridAPIClient('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')
        from_email = Email("r00kiec0ders22@gmail.com")  # Change to your verified sender
        to_email = address_entry1.get()
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
    print(OTP)
    return OTP    


def back():
    window.destroy()
    import welcome     


def on_enter(button):
    button.config(bg="#21B6A8", fg="#05445E")

def on_leave(button):
     button.config(bg="#05445E", fg="#21B6A8")
    


#Login Actions
otpsubmit = tk.Button(window, text="Send OTP",fg="#21B6A8",command= sendMail, bg="#05445E"  ,width=20  ,height=1 ,activebackground = "#203A43" ,font=('times', 14, ' bold '))
otpsubmit.place(x=715, y=330)

submit = tk.Button(window, text="Submit",fg="#21B6A8",command= login_submit, bg="#05445E"  ,width=20  ,height=1 ,activebackground = "#203A43" ,font=('times', 14, ' bold '))
submit.place(x=430, y=425)

clearButton = tk.Button(window, text="Clear", command=login_clear,fg="#21B6A8" ,bg="#05445E"  ,width=20  ,height=1, activebackground = "#203A43" ,font=('times', 14, ' bold '))
clearButton.place(x=715, y=425)
quitWindow = tk.Button(window, text="Back", command=back  ,fg="#21B6A8" ,bg="#05445E"  ,width=20  ,height=2, activebackground = "#203A43" ,font=('times', 15, ' bold '))
quitWindow.place(x=1000, y=550)


but=[clearButton,submit,quitWindow,otpsubmit]
for button in but:
    button.bind('<Enter>', lambda e, b=button: on_enter(b))
    button.bind('<Leave>', lambda e, b=button: on_leave(b))



#final Actions

window.mainloop()
