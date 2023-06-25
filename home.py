# from home import *
import tkinter as tk
from tkinter import  *
from tkinter.tix import IMAGETEXT
from PIL import Image, ImageTk

window=tk.Tk()
window.title("home")
window.geometry('1366x768')
c=Canvas(window,bg="gray16",height=200,width=200)
filename = PhotoImage(file="pictures\\BG2.png")
background_label=Label(window,image = filename)
background_label.place(x=0,y=0, relwidth=1, relheight=1)
login_label= tk.Label(window, text="USER AUTHENTICATION" ,bg="#71B280"  ,fg="#05445E"  ,width=100 ,height=1,font=('times', 35, 'bold')).pack(fill = 'x') 

img = Image.open("pictures\\Digital-banking.jpg")
photo = ImageTk.PhotoImage(img)
# img = IMAGETEXT.PhotoImage(Image.open("pictures\\Digital-banking.jpg"))
I = Label(window, image=photo,width=770 ,height=510,highlightthickness=5, highlightbackground="#21B6A8")
I.place(x=50, y=150)

#HEADINGS
login_label= tk.Label(window, text="You have successfully \nVerified your identity!" ,bg="#003032"  ,fg="#21B6A8"  ,width=20 ,height=5,font=('times', 30, 'bold')) 
login_label.place(x=840, y=150)

login_label= tk.Label(window, text="Enjoy your session!" ,bg="#003032"  ,fg="#21B6A8"  ,width=20 ,height=3,font=('times', 30, 'bold')) 
login_label.place(x=840, y=530)
img1 = Image.open("pictures\\verify.png")
photo1 = ImageTk.PhotoImage(img1)
# img = IMAGETEXT.PhotoImage(Image.open("pictures\\Digital-banking.jpg"))
I = Label(window, image=photo1,width=482 ,height=200,bg="#003032")
I.place(x=840, y=350)



def logout():
    window.destroy()
    import welcome

logoutButton = tk.Button(window, text="Log Out", command=logout,fg="#21B6A8" ,bg="#003032"  ,width=20  ,height=1, activebackground = "#203A43" ,font=('times', 14, ' bold '))
logoutButton.place(x=1100, y=80)
def on_enter(button):
    button.config(bg="#21B6A8", fg="#003032")
def on_leave(button):
     button.config(bg="#003032", fg="#21B6A8")
but=[logoutButton]
for button in but:
    button.bind('<Enter>', lambda e, b=button: on_enter(b))
    button.bind('<Leave>', lambda e, b=button: on_leave(b))

window.mainloop()
