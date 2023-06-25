import tkinter as tk
from tkinter import  *
from tkinter.tix import IMAGETEXT
from PIL import Image, ImageTk
window=tk.Tk()
window.title("User Authentication")
window.geometry('1366x750')
c=Canvas(window,bg="gray16",height=200,width=200)
filename = PhotoImage(file="pictures\\BG2.png")
background_label=Label(window,image = filename)
background_label.place(x=0,y=0, relwidth=1, relheight=1)

login_label= tk.Label(window, text="USER AUTHENTICATION" ,bg="#71B280"  ,fg="#05445E" ,width=100 ,height=1,font=('times', 35, 'bold')).pack(fill = 'x') 

img3 = Image.open("pictures\\face.png")
ph = ImageTk.PhotoImage(img3)
I = Label(window, image=ph,width=770 ,height=510,highlightthickness=5, highlightbackground="#21B6A8")
I.place(x=50, y=150) 
login_label= tk.Label(window, text="Are you a registered user?" ,bg="#71B280"  ,fg="#05445E"  ,width=20 ,height=1,font=('times', 20, 'bold')) 
login_label.place(x=900, y=200)

login_label= tk.Label(window, text="New user? \nClick here to register." ,bg= '#71B280' ,fg="#05445E" ,width=18,justify=LEFT ,height=2,font=('times', 20, 'bold')) 
login_label.place(x=900, y=360)


def reg1():
    window.destroy()
    import reg
def log1():
    window.destroy()
    import login

def on_enter(button):
    button.config(bg="#21B6A8", fg="#003032")

def on_leave(button):
     button.config(bg="#003032", fg="#21B6A8")


loginb = tk.Button(window, text="LOGIN", command=log1,fg="#21B6A8" ,bg="#003032"  ,width=30  ,height=3, activebackground = "#203A43" ,font=('times', 14, ' bold '))
loginb.place(x=900, y=250)

regb = tk.Button(window, text="REGISTER", command=reg1 ,fg="#21B6A8" ,bg="#003032", width=30  ,height=3 ,activebackground = "#203A43" ,font=('times', 14, ' bold '))
regb.place(x=900, y=450)

quitb = tk.Button(window, text="Exit", command=window.destroy  ,fg="#21B6A8" ,bg="#003032"  ,width=20  ,height=2, activebackground = "#203A43" ,font=('times', 15, ' bold '))
quitb.place(x=1000, y=550)
but=[loginb,regb,quitb]
for button in but:
    button.bind('<Enter>', lambda e, b=button: on_enter(b))
    button.bind('<Leave>', lambda e, b=button: on_leave(b))

window.mainloop()