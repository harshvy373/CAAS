import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from ttkthemes import ThemedStyle
from functools import partial
from db_class import *
import socket
from getmac import get_mac_address as gma

#from login import *

def validate(nam):
    print(nam.get())

def validate_registration(name, username, password, cpassword, typ, clas, ques, ans):
    
    if name.get()=="" or username.get()=="" or password.get()=="" or cpassword.get()=="" or typ.get()=="" or typ.get()=="Select" or clas.get()=="" or clas.get()=="Select" or ques.get()=="" or ques.get()=="Select" or ans.get()=="":
        Message["text"] = "Enter all the details !"
        Message["fg"] = "#d10606"
        Message.place(x=0,y=510,width=140,height=30)
    elif password.get()!=cpassword.get():
        Message["text"] = "Password and Confirm Password doesn't match !"
        Message["fg"] = "#d10606"
        Message.place(x=2,y=510,width=300,height=30)
    else:
        q="select * from users where username='"+username.get()+"';"
        s=find(q)
        if s==1:
            Message["text"] = "Username already exists !"
            Message["fg"] = "#d10606"
            Message.place(x=0,y=510,width=170,height=30)
        else:
            hostname = socket.gethostname()    
            IPAddr = socket.gethostbyname(hostname)
            mac_add=gma()
            details = "Hostname => "+hostname+", IP Address => "+IPAddr+", MAC Address => "+mac_add
            q="insert into users values('"+name.get()+"','"+username.get()+"','"+password.get()+"','"+typ.get()+"','"+clas.get()+"','"+ques.get()+"','"+ans.get()+"','"+details+"');"
            insert(q)
            name_entry.delete(0,"end")
            username_entry.delete(0,"end")
            acc_select.set('')
            class_select.set('')
            ques_select.set('')
            password_entry.delete(0,"end")
            cpassword_entry.delete(0,"end")
            sans_entry.delete(0,"end")
            Message["text"] = "Registered successfully !"
            Message["fg"] = "#008000"
            Message.place(x=0,y=510,width=170,height=30)

        
    
root = tk.Tk()
root.iconbitmap(default='favicon.ico')
#app = App(root)


#setting title
root.title("CASS | Register")
#setting window size
width=400
height=550
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

Heading=tk.Label(root)
ft = tkFont.Font(family='Arial',size=11)
Heading["font"] = ft
Heading["fg"] = "#333333"
Heading["justify"] = "center"
Heading["text"] = "Enter the details for registration"
Heading.place(x=90,y=10,width=203,height=30)

#name
name_label=tk.Label(root)
ft = tkFont.Font(family='Arial',size=10)
name_label["font"] = ft
name_label["fg"] = "#333333"
name_label["justify"] = "left"
name_label["text"] = "Name"
name_label.place(x=-2,y=60,width=70,height=25)

name = tk.StringVar()
name_entry=tk.Entry(root,textvariable=name)
name_entry["borderwidth"] = "1px"
ft = tkFont.Font(family='Arial',size=10)
name_entry["font"] = ft
name_entry["fg"] = "#333333"
name_entry["justify"] = "left"
name_entry.place(x=160,y=60,width=212,height=30)


#username
username_label=tk.Label(root)
ft = tkFont.Font(family='Arial',size=10)
username_label["font"] = ft
username_label["fg"] = "#333333"
username_label["justify"] = "left"
username_label["text"] = "Username"
username_label.place(x=10,y=110,width=70,height=25)

username = tk.StringVar()
username_entry=tk.Entry(root,textvariable=username)
username_entry["borderwidth"] = "1px"
ft = tkFont.Font(family='Arial',size=10)
username_entry["font"] = ft
username_entry["fg"] = "#333333"
username_entry["justify"] = "left"
username_entry.place(x=160,y=110,width=211,height=30)


#password
password_label=tk.Label(root)
ft = tkFont.Font(family='Arial',size=10)
password_label["font"] = ft
password_label["fg"] = "#333333"
password_label["justify"] = "left"
password_label["text"] = "Password"
password_label.place(x=10,y=160,width=70,height=25)

password = tk.StringVar()
password_entry=tk.Entry(root,textvariable=password,show="*")
password_entry["borderwidth"] = "1px"
ft = tkFont.Font(family='Arial',size=10)
password_entry["font"] = ft
password_entry["fg"] = "#333333"
password_entry["justify"] = "left"
password_entry.place(x=160,y=160,width=213,height=30)


#cpassword
cpassword_label=tk.Label(root)
ft = tkFont.Font(family='Arial',size=10)
cpassword_label["font"] = ft
cpassword_label["fg"] = "#333333"
cpassword_label["justify"] = "left"
cpassword_label["text"] = "Confirm Password"
cpassword_label.place(x=8,y=210,width=122,height=30)

cpassword = tk.StringVar()
cpassword_entry=tk.Entry(root,textvariable=cpassword,show="*")
cpassword_entry["borderwidth"] = "1px"
ft = tkFont.Font(family='Arial',size=10)
cpassword_entry["font"] = ft
cpassword_entry["fg"] = "#333333"
cpassword_entry["justify"] = "left"
cpassword_entry.place(x=160,y=210,width=213,height=30)

#acc_type
type_label=tk.Label(root)
ft = tkFont.Font(family='Arial',size=10)
type_label["font"] = ft
type_label["fg"] = "#333333"
type_label["justify"] = "left"
type_label["text"] = "Type"
type_label.place(x=-3,y=260,width=70,height=25)

acc_type = tk.StringVar()
acc_select=ttk.Combobox(root,textvariable=acc_type,state="readonly")
acc_select["values"]=('Select','Admin','Teacher','Student')
ft = tkFont.Font(family='Arial',size=10)
acc_select["font"] = ft
acc_select["background"] = "#ffffff"
acc_select["justify"] = "left"
acc_select.place(x=160,y=260,width=213,height=30)


#class
class_label=tk.Label(root)
ft = tkFont.Font(family='Arial',size=10)
class_label["font"] = ft
class_label["fg"] = "#333333"
class_label["justify"] = "left"
class_label["text"] = "Class"
class_label.place(x=0,y=310,width=70,height=25)

class_type = tk.StringVar()
class_select=ttk.Combobox(root,textvariable=class_type,state="readonly")
class_select["values"]=('Select','XII-A','XII-B','XII-C')
ft = tkFont.Font(family='Arial',size=10)
class_select["font"] = ft
class_select["background"] = "#ffffff"
class_select["justify"] = "left"
class_select.place(x=160,y=310,width=213,height=30)


#sques
sques_label=tk.Label(root)
ft = tkFont.Font(family='Arial',size=10)
sques_label["font"] = ft
sques_label["fg"] = "#333333"
sques_label["justify"] = "left"
sques_label["text"] = "Security Question"
sques_label.place(x=10,y=360,width=122,height=30)

sec_ques = tk.StringVar()
ques_select=ttk.Combobox(root,textvariable=sec_ques,state="readonly")
ques_select["values"]=('Select','DOB','DOA')
ft = tkFont.Font(family='Arial',size=10)
ques_select["font"] = ft
ques_select["background"] = "#ffffff"
ques_select["justify"] = "left"
ques_select.place(x=160,y=360,width=213,height=30)

#s_ans
sans_label=tk.Label(root)
ft = tkFont.Font(family='Arial',size=10)
sans_label["font"] = ft
sans_label["fg"] = "#333333"
sans_label["justify"] = "left"
sans_label["text"] = "Security Answer"
sans_label.place(x=10,y=410,width=112,height=30)

sec_ans = tk.StringVar()
sans_entry=tk.Entry(root,textvariable=sec_ans)
sans_entry["borderwidth"] = "1px"
ft = tkFont.Font(family='Arial',size=10)
sans_entry["font"] = ft
sans_entry["fg"] = "#333333"
sans_entry["justify"] = "left"
sans_entry.place(x=160,y=410,width=212,height=30)
     

#register_button
register_button=tk.Button(root)
register_button["bg"] = "#525458"
ft = tkFont.Font(family='Arial',size=10)
register_button["font"] = ft
register_button["fg"] = "#ffffff"
register_button["justify"] = "center"
register_button["text"] = "REGISTER"
register_button.place(x=10,y=470,width=364,height=30)
validate_registration = partial(validate_registration, name, username, password, cpassword, acc_type, class_type, sec_ques, sec_ans)
register_button["command"] = validate_registration

#message
Message=tk.Label(root)
ft = tkFont.Font(family='Arial',size=10)
Message["font"] = ft
Message["fg"] = "#008000"
Message["justify"] = "left"
Message.place(x=0,y=510,width=170,height=30)

root.mainloop()
    
