import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk 
from ttkthemes import ThemedStyle
from functools import partial
from db_class import *
from admin import *

def validateLogin(username,password):
    q="select type,name from users where username='"+username.get()+"' and password='"+password.get()+"';"
    s=select(q)
    try:
        if s[0]=="Admin":
            root.destroy()
            admin_start(s[1])
            
        elif s[0]=="Teacher":
            root.destroy()
            print("Teacher")
            
        elif s[0]=="Student":
            root.destroy()
            print("Student")
            
    except:
        Message["text"]="Wrong credentials !"
       
root = tk.Tk()
root.iconbitmap(default='goodies/favicon.ico')
style = ThemedStyle(root)

#setting title
root.title("CASS | Login")
#setting window size
width=390
height=220
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

GLabel_898=tk.Label(root)
ft = tkFont.Font(family='Arial Bold',size=11)
GLabel_898["font"] = ft
GLabel_898["fg"] = "#000000"
GLabel_898["justify"] = "center"
GLabel_898["text"] = "Enter your details to login"
GLabel_898.place(x=90,y=10,width=197,height=30)

GLabel_692=tk.Label(root)
ft = tkFont.Font(family='Arial',size=11)
GLabel_692["font"] = ft
GLabel_692["fg"] = "#000000"
GLabel_692["justify"] = "left"
GLabel_692["text"] = "Username"
GLabel_692.place(x=20,y=50,width=70,height=30)

username = tk.StringVar()
GLineEdit_526=tk.Entry(root, textvariable=username)
GLineEdit_526["borderwidth"] = "1px"
ft = tkFont.Font(family='Arial',size=11)
GLineEdit_526["font"] = ft
GLineEdit_526["fg"] = "#000000"
GLineEdit_526["justify"] = "left"
GLineEdit_526.place(x=150,y=50,width=212,height=30)

GLabel_232=tk.Label(root)
ft = tkFont.Font(family='Arial',size=11)
GLabel_232["font"] = ft
GLabel_232["fg"] = "#000000"
GLabel_232["justify"] = "left"
GLabel_232["text"] = "Password"
GLabel_232.place(x=20,y=100,width=70,height=25)

password = tk.StringVar()
GLineEdit_165=tk.Entry(root, textvariable=password, show='*')
GLineEdit_165["borderwidth"] = "1px"
ft = tkFont.Font(family='Arial',size=11)
GLineEdit_165["font"] = ft
GLineEdit_165["fg"] = "#000000"
GLineEdit_165["justify"] = "left"
GLineEdit_165.place(x=150,y=100,width=212,height=30)

GButton_819=tk.Button(root)
GButton_819["bg"] = "#333333"
ft = tkFont.Font(family='Arial Bold',size=11)
GButton_819["font"] = ft
GButton_819["fg"] = "#ffffff"
GButton_819["justify"] = "center"
GButton_819["text"] = "L O G I N"
GButton_819.place(x=20,y=150,width=345,height=30)
validateLogin = partial(validateLogin, username, password)
GButton_819["command"] = validateLogin


Message=tk.Label(root)
ft = tkFont.Font(family='Arial',size=10)
Message["font"] = ft
Message["fg"] = "#d10606"
Message["text"] = ""
Message.place(x=4,y=190,width=150,height=30)

root.mainloop()
