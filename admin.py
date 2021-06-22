from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from PIL import Image, ImageTk
import time
#from admin_takeattendance import *

color="#28383c"
#color="#5f6b6d"

welcome_msg="";
root,gtx_name="",""

from admin_generateids import *
from admin_impexp import *
from admin_takeattendance import *
from admin_viewattendance import *
from forgot import *

def home():
    a="Hello"

def ta():
    try:    
        root.destroy()
        admin_takeat(gtx_name)
    except:
        try:
            root.destroy()
            admin_takeat(gtx_name)
        except:
            a="Hello"
        a="Hello"
def va():
    try:
        root.destroy()
        start_viewattendance(gtx_name)
    except:
        try:
            root.destroy()
            start_viewattendance(gtx_name)
        except:
            a="Hello"
        a="Hello"

def idg():
    try:
        root.destroy()
        start_generateids(gtx_name)
    except:
        try:
            root.destroy()
            start_generateids(gtx_name)
        except:
            a="Hello"
        a="Hello"
def mu():
    try:
        root.destroy()
        start_impexp(gtx_name)
    except:
        try:
            root.destroy()
            start_impexp(gtx_name)
        except:
            a="Hello"
        a="Hello"
def cp():
    try:
        root.destroy()
        forgot()
    except:
        try:
            root.destroy()
            forgot()
        except:
            a="Hello"
        a="Hello";

def logout():
    root.destroy()
    
def takeattendance():
    scan_qr()
    
def GButton_849_command():
    print("command")

def GButton_349_command():
    print("command")

def GButton_357_command():
    print("command")

def GButton_27_command():
    print("command")

def GButton_778_command():
    print("command")

def admin_start(name):
    global root,gtx_name
    gtx_name=name
    root = Tk()
    root.geometry("300x200")
    root.attributes("-fullscreen", True)
    welcome_msg="Hello "+name+" | Admin Dashboard"

    navbar = Frame(root, bg=color, width=200)
    navbar.pack(anchor=W, fill=Y, expand=False, side=LEFT)

    GLabel_848=tk.Label(navbar,font=('Arial',18,'bold'))
    GLabel_848["bg"] = color
    GLabel_848["fg"] = "#ffffff"
    GLabel_848["justify"] = "center"
    GLabel_848["text"] = "CAAS"
    GLabel_848.place(x=35,y=50,width=125,height=55)

    GLabel_848=tk.Label(navbar,wraplength=155,font=('Arial',11,'bold'))
    GLabel_848["bg"] = color
    GLabel_848["fg"] = "#ffffff"
    GLabel_848["justify"] = "center"
    GLabel_848["text"] = "COVID-19 Automated Attendance System"
    GLabel_848.place(x=20,y=100,width=155,height=55)

    ttk.Separator(navbar).place(x=0, y=155, relwidth=1)

    GButton_849=tk.Button(navbar)
    GButton_849["bg"] = color
    GButton_849["borderwidth"] = "0px"
    ft = tkFont.Font(family='Arial',size=12)
    GButton_849["font"] = ft
    GButton_849["fg"] = "#ffffff"
    GButton_849["justify"] = "left"
    GButton_849["text"] = "Home"
    GButton_849.place(x=35,y=230,width=125,height=50)
    GButton_849["command"] = home

    GButton_349=tk.Button(navbar)
    GButton_349["bg"] = color
    GButton_349["borderwidth"] = "0px"
    ft = tkFont.Font(family='Arial',size=12)
    GButton_349["font"] = ft
    GButton_349["fg"] = "#ffffff"
    GButton_349["justify"] = "left"
    GButton_349["text"] = "Take Attendance"
    GButton_349.place(x=35,y=290,width=125,height=50)
    GButton_349["command"] = ta

    GButton_357=tk.Button(navbar)
    GButton_357["bg"] = color
    GButton_357["borderwidth"] = "0px"
    ft = tkFont.Font(family='Arial',size=12)
    GButton_357["font"] = ft
    GButton_357["fg"] = "#ffffff"
    GButton_357["justify"] = "left"
    GButton_357["text"] = "View Attendance"
    GButton_357.place(x=35,y=350,width=125,height=50)
    GButton_357["command"] = va


    GButton_27=tk.Button(navbar)
    GButton_27["bg"] = color
    GButton_27["borderwidth"] = "0px"
    ft = tkFont.Font(family='Arial',size=12)
    GButton_27["font"] = ft
    GButton_27["fg"] = "#ffffff"
    GButton_27["justify"] = "left"
    GButton_27["text"] = "IDs Generation"
    GButton_27.place(x=35,y=410,width=125,height=50)
    GButton_27["command"] = idg

    GButton_778=tk.Button(navbar)
    GButton_778["bg"] = color
    GButton_778["borderwidth"] = "0px"
    ft = tkFont.Font(family='Arial',size=12)
    GButton_778["font"] = ft
    GButton_778["fg"] = "#ffffff"
    GButton_778["justify"] = "left"
    GButton_778["text"] = "Manage Users"
    GButton_778.place(x=35,y=470,width=125,height=50)
    GButton_778["command"] = mu

    GButton_779=tk.Button(navbar)
    GButton_779["bg"] = color
    GButton_779["borderwidth"] = "0px"
    ft = tkFont.Font(family='Arial',size=12)
    GButton_779["font"] = ft
    GButton_779["fg"] = "#ffffff"
    GButton_779["justify"] = "left"
    GButton_779["text"] = "Change Password"
    GButton_779.place(x=30,y=530,width=130,height=50)
    GButton_779["command"] = cp

    GButton_7799=tk.Button(navbar)
    GButton_7799["bg"] = color
    GButton_7799["borderwidth"] = "0px"
    ft = tkFont.Font(family='Arial',size=12)
    GButton_7799["font"] = ft
    GButton_7799["fg"] = "#ffffff"
    GButton_7799["justify"] = "left"
    GButton_7799["text"] = "Log Out"
    GButton_7799.place(x=35,y=590,width=125,height=50)
    GButton_7799["command"] = logout

    author=tk.Label(navbar,font=('Arial',11,'bold'))
    author["bg"] = color
    #ft = tkFont.Font(family='Arial',size=11)
    #author["font"] = ft
    author["fg"] = "#ffffff"
    author["justify"] = "center"
    author["text"] = "By Harsh Vardhan"
    author.place(x=35,y=650,width=125,height=195)

    content_frame = Frame(root, bg="white")
    content_frame.pack(anchor=N, fill=BOTH, expand=True, side=LEFT)

    greeting=tk.Label(content_frame,font=('Arial',14,'bold'))
    #greeting["bg"] = "#ffffff"
    greeting["fg"] = "#000000"
    greeting["text"] = welcome_msg
    greeting.place(x=0,y=106,width=1350,height=50)

    image1 = Image.open("goodies/longlogo.png")
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(content_frame,image=test,borderwidth=0)
    label1.image = test
    label1.place(x=980, y=0)

    image2 = Image.open("goodies/banner2.jpg")
    test2 = ImageTk.PhotoImage(image2)
    label2 = tk.Label(content_frame,image=test2,highlightcolor="black",borderwidth=2, relief="solid")
    label2.image = test2
    label2.place(x=100, y=190)
    
    root.mainloop()

#admin_start("Harsh")

