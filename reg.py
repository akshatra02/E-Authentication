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


#HEADINGS
reg_label= tk.Label(window, text="Registeration" ,bg="#05445E"  ,fg="#71B280"  ,width=20 ,height=1,font=('times', 30, 'bold')) 
reg_label.place(x=450, y=150)

msg_label=tk.Label(window,text="Notification: ",bg='#05445E' ,fg='#71B280',width=10,height=1,font=('times',20,'bold'))
msg_label.place(x=300,y=450)
message = tk.Label(window,text="",bg="#71B280" ,fg="#0F2027", width=30, height=1, font=('times',20,'bold'))
message.place(x=500,y=450)

#Register Fields

lbl3 = tk.Label(window, text="Enter ID :",width=10  ,height=1  ,fg="#05445E"  ,bg="#71B280" ,font=('times', 15, ' bold ') ) 
lbl3.place(x=450, y=213)

txt3 = tk.Entry(window,width=25  ,bg="#71B280" ,fg="#0F2027",font=('times', 15, ' bold '))
txt3.place(x=690, y=213)

lbl4= tk.Label(window, text="Enter Password",width=15  ,height=1  ,fg="#05445E"  ,bg="#71B280" ,font=('times', 15, ' bold ') ) 
lbl4.place(x=450, y=250)

txt4 = tk.Entry(window,width=25  ,bg="#71B280" ,show='*',fg="#0F2027",font=('times', 15, ' bold '))
txt4.place(x=690, y=250)

address_field2= tk.Label(window, text="Enter E-mail :",width=15,height=1  ,fg="#05445E" ,bg="#71B280" ,font=('times', 15, ' bold ') )
address_field2.place(x=450,y=287)
address = StringVar()
address_entry2=tk.Entry(window,textvariable=address,width=25  ,bg="#71B280" ,fg="#0F2027",font=('times', 15, ' bold '))
address_entry2.place(x=690,y=287)


#Main
def reg_clear():
    txt3.delete(0,'end')
    txt4.delete(0,'end')
    address_field2(0,'end')
    address_entry2(0,'end')
    #res = ""
    #txt3.configure(text= res)
    #txt4.configure(text=res)







################## Register_Functions   ######################





def TakeImages():        
    Id=(txt3.get())
    name=(txt4.get())
    ret=0
    if (Id not in data):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                #incrementing sample number 
                sampleNum=sampleNum+1
                #saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage\ "+name +'.'+Id+'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                #display the frame
                cv2.imshow('frame',img)
            #wait for 100 miliseconds 
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum>100:
                break
        cam.release()
        cv2.destroyAllWindows() 
        res = "Images Saved for ID : " + Id +" Name : "+ name
        row = [Id , name]
        with open('Details\Details.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message.configure(text= res)
        ret=1
    else:
        res = "User name Already Exists...Try another one!!!"
        message.configure(text= res)
    return ret

# Training Images

def TrainImages():
    recognizer = cv2.face_LBPHFaceRecognizer.create()#recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("TrainingImageLabel\Trainner.yml")
    #print(faces,np.array(Id))
    #res = "Image Trained"#+",".join(str(f) for f in Id)
    res="Registration Successful"
    message.configure(text= res)
    return True
    

def getImagesAndLabels(path):
    #get the path of all the files in the folder
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    #print(imagePaths)
    
    #create empth face list
    faces=[]
    #create empty ID list
    Ids=[]
    #now looping through all the image path  s and loading the Ids and the images
    for imagePath in imagePaths:
        #loading the image and converting it to gray scale
        pilImage=PIL.Image.open(imagePath).convert('L')
        #Now we are converting the PIL image into numpy array
        imageNp=np.array(pilImage,'uint8')
        #getting the Id from the image
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        # extract the face from the training image sample
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids

def back():
    window.destroy()
    import welcome   



def reg_submit():
    Userid=txt3.get()
    if Userid.isdigit():
        if TakeImages()==1:
            if TrainImages():
                data[txt3.get()] = [txt4.get()] + [address_entry2.get()]
                saving_data(data)

            else:
                pass
    
    else:
        message.configure(text="User Id Should contain number only!!!")
    reg_clear()

    print(data)


def on_enter(button):
    button.config(bg="#21B6A8", fg="#05445E")

def on_leave(button):
     button.config(bg="#05445E", fg="#21B6A8")
    

#Register Actions
submit2 = tk.Button(window, text="Submit", command=reg_submit ,fg="#21B6A8" ,bg="#05445E", width=20  ,height=1 ,activebackground = "#203A43" ,font=('times', 14, ' bold '))
submit2.place(x=450, y=340)


clearButton2 = tk.Button(window, text="Clear",command=reg_clear ,fg="#21B6A8" ,bg="#05445E" ,width=20  ,height=1, activebackground = "#203A43" ,font=('times', 14, ' bold '))
clearButton2.place(x=690, y=340)

quitWindow = tk.Button(window, text="Back", command=back  ,fg="#21B6A8" ,bg="#05445E"  ,width=20  ,height=2, activebackground = "#203A43" ,font=('times', 15, ' bold '))
quitWindow.place(x=1000, y=550)


but=[clearButton2,submit2,quitWindow]
for button in but:
    button.bind('<Enter>', lambda e, b=button: on_enter(b))
    button.bind('<Leave>', lambda e, b=button: on_leave(b))



#final Actions

window.mainloop()
