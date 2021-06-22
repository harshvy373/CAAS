import tkinter as tk
import tkinter.font as tkFont
import tkinter.ttk as ttk 
from ttkthemes import ThemedStyle
from functools import partial
from db_class import *


def validate():
    ques,ans=sec_ques, sec_ans
    print(username,ques,ans,password,cpassword)
    if username.get()=="" or ques.get()=="" or ques.get()=="Select" or ans.get()=="" or password.get()=="" or cpassword.get()=="":
        message["text"] = "Enter all the details !"
        message["fg"] = "#d10606"
        message.place(x=0,y=320,width=150,height=30)
    elif password.get()!=cpassword.get():
        message["text"] = "Password mismatch !"
        message["fg"] = "#d10606"
        message.place(x=0,y=320,width=150,height=30)
    else:
        q="select * from users where username='"+username.get()+"' and sec_ques='"+ques.get()+"' and sec_ans='"+ans.get()+"';"
        s=find(q)
        if s==1:
            qq="update users set password='"+password.get()+"' where username='"+username.get()+"';"
            insert(qq)
            message["text"] = "Password Changed !"
            message["fg"] = "#008000"
            message.place(x=0,y=320,width=150,height=30)
            
        else:
            message["text"] = "Wrong Credentials !"
            message["fg"] = "#d10606"
            message.place(x=0,y=320,width=150,height=30)

username, sec_ques, sec_ans,password,cpassword="","","","",""
message=""
def forgot():
    global username, sec_ques, sec_ans,password,cpassword,message
    root = tk.Tk()
    root.iconbitmap(default='goodies/favicon.ico')
    #app = App(root)
    style = ThemedStyle(root)
    #style.set_theme("alt")

    #setting title
    root.title("CASS | Forgot Password")
    #setting window size
    width=396
    height=350
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    root.geometry(alignstr)
    root.resizable(width=False, height=False)

    heading=tk.Label(root)
    ft = tkFont.Font(family='Arial',size=11)
    heading["font"] = ft
    heading["fg"] = "#333333"
    heading["justify"] = "center"
    heading["text"] = "Enter your credentials to reset password"
    heading.place(x=65,y=5,width=281,height=30)


    #username
    label_username=tk.Label(root)
    ft = tkFont.Font(family='Arial',size=10)
    label_username["font"] = ft
    label_username["fg"] = "#333333"
    label_username["justify"] = "left"
    label_username["text"] = "Username"
    label_username.place(x=8,y=40,width=70,height=25)

    username = tk.StringVar()
    username_entry=tk.Entry(root,textvariable=username)
    username_entry["borderwidth"] = "1px"
    ft = tkFont.Font(family='Arial',size=10)
    username_entry["font"] = ft
    username_entry["fg"] = "#333333"
    username_entry["justify"] = "left"
    username_entry.place(x=160,y=40,width=222,height=30)


    #sec_ques
    label_sques=tk.Label(root)
    ft = tkFont.Font(family='Arial',size=10)
    label_sques["font"] = ft
    label_sques["fg"] = "#333333"
    label_sques["justify"] = "left"
    label_sques["text"] = "Security Question"
    label_sques.place(x=5,y=90,width=118,height=30)

    sec_ques = tk.StringVar()
    ques_select=ttk.Combobox(root,textvariable=sec_ques,state="readonly")
    ques_select["values"]=('Select','DOB','DOA')
    ft = tkFont.Font(family='Arial',size=10)
    ques_select["font"] = ft
    ques_select["background"] = "#ffffff"
    ques_select["justify"] = "left"
    ques_select.place(x=160,y=90,width=222,height=30)


    #sec_ans
    label_sans=tk.Label(root)
    ft = tkFont.Font(family='Arial',size=10)
    label_sans["font"] = ft
    label_sans["fg"] = "#333333"
    label_sans["justify"] = "left"
    label_sans["text"] = "Security Answer"
    label_sans.place(x=10,y=140,width=102,height=30)

    sec_ans = tk.StringVar()
    ans_entry=tk.Entry(root,textvariable=sec_ans)
    ans_entry["borderwidth"] = "1px"
    ft = tkFont.Font(family='Arial',size=10)
    ans_entry["font"] = ft
    ans_entry["fg"] = "#333333"
    ans_entry["justify"] = "left"
    ans_entry.place(x=160,y=140,width=218,height=30)


    #password
    label_password=tk.Label(root)
    ft = tkFont.Font(family='Arial',size=10)
    label_password["font"] = ft
    label_password["fg"] = "#333333"
    label_password["justify"] = "left"
    label_password["text"] = "New Password"
    label_password.place(x=7,y=190,width=102,height=30)

    password = tk.StringVar()
    password_entry=tk.Entry(root,textvariable=password,show="*")
    password_entry["borderwidth"] = "1px"
    ft = tkFont.Font(family='Arial',size=10)
    password_entry["font"] = ft
    password_entry["fg"] = "#333333"
    password_entry["justify"] = "left"
    password_entry.place(x=160,y=190,width=218,height=30)


    #cpassword
    label_cpassword=tk.Label(root)
    ft = tkFont.Font(family='Arial',size=10)
    label_cpassword["font"] = ft
    label_cpassword["fg"] = "#333333"
    label_cpassword["justify"] = "left"
    label_cpassword["text"] = "Confirm Password"
    label_cpassword.place(x=7,y=240,width=120,height=30)

    cpassword = tk.StringVar()
    cpassword_entry=tk.Entry(root,textvariable=cpassword,show="*")
    cpassword_entry["borderwidth"] = "1px"
    ft = tkFont.Font(family='Arial',size=10)
    cpassword_entry["font"] = ft
    cpassword_entry["fg"] = "#333333"
    cpassword_entry["justify"] = "left"
    cpassword_entry.place(x=160,y=240,width=218,height=30)

    #submit
    submit_button=tk.Button(root)
    submit_button["bg"] = "#525458"
    ft = tkFont.Font(family='Arial',size=10)
    submit_button["font"] = ft
    submit_button["fg"] = "#ffffff"
    submit_button["justify"] = "center"
    submit_button["text"] = "SUBMIT"
    submit_button.place(x=10,y=290,width=371,height=30)
    submit_button["command"] = validate


    #message
    message=tk.Label(root)
    ft = tkFont.Font(family='Arial',size=10)
    message["font"] = ft
    message["fg"] = "#333333"
    message["justify"] = "left"
    message.place(x=10,y=320,width=70,height=25)

    root.mainloop()


