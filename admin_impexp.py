from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
from ttkthemes import ThemedStyle
from functools import partial
import pandas as pd
#import mysql.connector
from db_class import *
import numpy as np
from table_class import *
from db_class import *
from datetime import date, timedelta
from tkinter import messagebox,filedialog
from PIL import Image, ImageTk
from report_print import *
from report_print2 import *


color="#28383c"
#color="#5f6b6d"
root,ssubmitcommand,submitcommand,submitcommandd="","","",""
Science, Commerce, Humanities, Sciencee, Commercee, Humanitiess,Scienceee, Commerceee, Humanitiesss="","","","","","","","",""
GLineEdit_97,GLineEdit_916,GLineEdit_977,GLineEdit_9166,GLineEdit_9777,GLineEdit_91666,att_select,att_selectt,att_selecttt="","","","","","","","",""
tab4=""
result_set=""
final=""
tt=""
root,gtx_name="",""

from admin import *
from admin_generateids import *
from admin_takeattendance import *
from admin_viewattendance import *
from forgot import *

def home():
    try:
        root.destroy()
        admin_start(gtx_name)
    except:
        try:
            root.destroy()
            admin_start(gtx_name)
        except:
            a="Hello"
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
            root.destroy()
            admin_start(gtx_name)        
        root.destroy()
        admin_start(gtx_name)
def va():
    try:
        root.destroy()
        start_viewattendance(gtx_name)
    except:
        try:
            root.destroy()
            start_viewattendance(gtx_name)
        except:
            root.destroy()
            admin_start(gtx_name)
        root.destroy()
        admin_start(gtx_name)
def idg():
    try:
        root.destroy()
        start_generateids(gtx_name)
    except:
        try:
            root.destroy()
            start_generateids(gtx_name)
        except:
            root.destroy()
            admin_start(gtx_name)
        root.destroy()
        admin_start(gtx_name)
def mu():
    a="hello"

def cp():
    try:    
        root.destroy()
        forgot()
    except:
        try:    
            root.destroy()
            forgot()            
        except:                    
            root.destroy()
            admin_start()
        root.destroy()
        forgot()

def logout():
    root.destroy()

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


def localfind(cursor_obj,q):
    cursor_obj.execute(q)
    result=cursor_obj.fetchall()
    return result
    """count=0
    for x in result:
        count+=1
    return count"""


def submitcommand(fromm,to,resulttype,classes):
    query="select name, id, type, class, phone,address from people where id is not null "
    if fromm.get!="" and to.get()!="":
        query+="and id between "+fromm.get()+" and "+to.get()
    if resulttype.get()=="Teachers":
        query+="and type='Teacher' "
    if resulttype.get()=="Students":
        query+="and type='Student' "
    query+=";"

    s=ftcall(query)
    data=pd.DataFrame(s,columns=["Name","ID No.","Type","Class","Mobile","Address"])
    file_name = filedialog.asksaveasfilename()
    if classes.get()=="EXCEL (.xls/.xlsx)":
        data.to_excel(file_name+".xlsx",index = False, header=True)
    else:
        data.to_csv(file_name,index = False, header=True)
        
    #query_execute(query,classes.get())


def ssubmitcommand(fromm,to,resulttype,classes):
    a=messagebox.askyesno("Confirm", "Is the file in order of Name,ID No.,Type,Class,Mobile,Address")
    print(classes.get())
    if a=="True" or a==True:
        h=None
        if resulttype.get()=="Yes":
            h=0
        if classes.get()=="Excel (.xlsx/.xls)":
            print("Here")
            file_name = filedialog.askopenfilename(defaultextension='.xls')
            data = pd.read_excel(file_name,header=h)
            data.to_csv("Test.csv",index = False, header=h)
            #data.to_csv (,index = None, header=h)
            data=pd.read_csv("Test.csv",header=h)
        else:
            file_name = filedialog.askopenfilename(defaultextension='.csv')
            data = pd.read_csv(file_name,header=h)
        i=0
        frm=0
        too=data.shape[0]
        if fromm.get()!="":
            frm=int(fromm.get())+0
        if to.get()!="":
            too=int(to.get())+1
        data=pd.DataFrame(data)
        for row in data.itertuples():
            print(row)
            print(type(row))
            i+=1
            if i>=frm and i<=too:
                print("Found",row[2])
                q="insert into people values('"+str(row[2])+"','"+str(row[1])+"','"+str(row[4])+"','"+str(row[3])+"','"+str(row[5])+"','"+str(row[6])+"');"
                print(q)
                insert(q)
        messagebox.showinfo("Import","Imported successfully")
            
        
    
    
    """query="select name, id, type, class, phone,address from people where id is not null "
    if fromm.get!="" and to.get()!="":
        query+="and id between "+fromm.get()+" and "+to.get()
    if resulttype.get()=="Teachers":
        query+="and type='Teacher' "
    if resulttype.get()=="Students":
        query+="and type='Student' "
    query+=";"

    s=ftcall(query)
    data=pd.DataFrame(s,columns=["Name","ID No.","Type","Class","Mobile","Address"])
    file_name = filedialog.asksaveasfilename()
    if classes.get()=="EXCEL (.xls/.xlsx)":
        data.to_excel(file_name,index = False, header=True)
    else:
        data.to_csv(file_name,index = False, header=True)"""
        
    #query_execute(query,classes.get())
  

def resetcommand():
    GLineEdit_97.set_date('01/01/2021')
    GLineEdit_916.set_date('01/01/2021')
    att_select.set('')
    for items in Science, Commerce, Humanities:
        items.set(False)

def rresetcommand():
    GLineEdit_97.set_date('01/01/2021')
    GLineEdit_916.set_date('01/01/2021')
    att_select.set('')
    for items in Science, Commerce, Humanities:
        items.set(False)


def send():
    draw_Tableee(final)
    
def export():
    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    final.to_excel (export_file_path, index = False, header=True)
    messagebox.showinfo("Export","Excel exported successfully")
    
def report_send():
    if tt=="Double sided":
        doubleside_start(final)
    else:
        singleside_start(final)        


          
     
        
tabControl2=""

def start_impexp(name):
    global root,gtx_name,tab4,scrollbar,tabControl2,submitcommand,ssubmitcommand,submitcommanddd,Science, Commerce, Humanities, Sciencee, Commercee, Humanitiess,Scienceee, Commerceee, Humanitiesss
    global GLineEdit_97,GLineEdit_916,GLineEdit_977,GLineEdit_9166,GLineEdit_9777,GLineEdit_91666,att_select,att_selectt,att_selecttt
    gtx_name=name
    root = Tk()
    root.geometry("300x200")
    root.attributes("-fullscreen", True)
    root.title("CAAS | Generate IDs")
    root.iconbitmap(default='goodies/favicon.ico')
    style = ThemedStyle(root)
    #print(style.theme_names())
    style.set_theme("black")
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
    greeting["text"] = "Hello "+name+" | Manage Users"
    greeting.place(x=0,y=106,width=1350,height=50)

    image1 = Image.open("goodies/longlogo.png")
    test = ImageTk.PhotoImage(image1)
    label1 = tk.Label(content_frame,image=test,borderwidth=0)
    label1.image = test
    label1.place(x=980, y=0)


    """df = pd.DataFrame({'A': [1,2,3,4,5,6,],
        'B': [1,1,2,2,3,3,],
        'C': [1,2,3,1,2,3,],
        'D': [1,1,1,2,2,2,],
    })"""

    data = [['Harsh',10],['Vardhan',12],['Yadav',13]]
    df = pd.DataFrame(data,columns=['Name','Age'])

    """
    frame_table = tk.Frame(content_frame)
    frame_table.place(x=200,y=170,width=1200,height=100)
    #frame_table.pack(fill='x', expand=False)

    pt = Table(content_frame, dataframe=df)
    #pt.place(x=0,y=170,width=1350,height=50)
    pt.show()
    """
    
    tabControl = ttk.Notebook(content_frame)

    s = ttk.Style()
    s.configure('Frame1.TFrame', background='white')
    tab1 = ttk.Frame(tabControl,style='Frame1.TFrame')

    tabControl.add(tab1, text ='Export Tab')
    #tabControl.add(tab2, text ='Student')
    #tabControl.add(tab3, text ='Teacher')
    
    #tabControl.pack(expand = 1)
    tabControl.place(x=30,y=200,width=1270,height=250)
    #ttk.Label(tab1, text ="Welcome to CAAS", background='white').grid(column = 0, row = 0, padx = 30,pady = 30) 
    #ttk.Label(tab2, text ="Developed by Harsh Vardhan Yadav", background='white').grid(column = 0, row = 0, padx = 30,pady = 30)
    #ttk.Label(tab3, text ="Project XII", background='white').grid(column = 0, row = 0, padx = 30,pady = 30)


    ####### end of connection ####

    GLabel_516=tk.Label(tab1, anchor = 'w', background='white')
    ft = tkFont.Font(family='Arial Bold',size=10)
    GLabel_516["font"] = ft
    GLabel_516["fg"] = "#000000"
    GLabel_516["text"] = "From ID"
    GLabel_516.place(x=10,y=50,width=70,height=25)

    GLabel_901=tk.Label(tab1, anchor = 'w', background='white')
    ft = tkFont.Font(family='Arial Bold',size=10)
    GLabel_901["font"] = ft
    GLabel_901["fg"] = "#000000"
    GLabel_901["justify"] = "left"
    GLabel_901["text"] = "To ID"
    GLabel_901.place(x=550,y=50,width=70,height=25)

    GLabel_984=tk.Label(tab1, anchor = 'w', background='white')
    ft = tkFont.Font(family='Arial Bold',size=10)
    GLabel_984["font"] = ft
    GLabel_984["fg"] = "#000000"
    GLabel_984["justify"] = "left"
    GLabel_984["text"] = "User Type"
    GLabel_984.place(x=10,y=110,width=78,height=25)

    GLabel_32=tk.Label(tab1, anchor = 'w', background='white')
    ft = tkFont.Font(family='Arial Bold',size=10)
    GLabel_32["font"] = ft
    GLabel_32["fg"] = "#000000"
    GLabel_32["justify"] = "left"
    GLabel_32["text"] = "Format "
    GLabel_32.place(x=550,y=110,width=70,height=25)

    fromdate = tk.StringVar()
    GLineEdit_97=Entry(tab1,textvariable = fromdate, highlightthickness=2, highlightbackground="#333333", relief="flat")
    #GLineEdit_97=DateEntry(tab1,locale="en_US", date_pattern="dd/MM/yyyy", textvariable = fromdate, highlightthickness=1, relief="flat")
    #GLineEdit_97.config(state='readonly')
    #GLineEdit_97.set_date('01/01/2021')
    GLineEdit_97["borderwidth"] = "2"
    ft = tkFont.Font(family='Arial',size=10)
    GLineEdit_97["font"] = ft
    GLineEdit_97["foreground"] = "#000000"
    GLineEdit_97["justify"] = "left"
    GLineEdit_97.place(x=96,y=50,width=250,height=30)

    todate = tk.StringVar()
    GLineEdit_916=Entry(tab1,textvariable = todate, highlightthickness=2, highlightbackground="#333333", relief="flat")
    #GLineEdit_916=DateEntry(tab1,locale="en_US", date_pattern="dd/MM/yyyy", textvariable = todate, highlightthickness=1, relief="flat")
    #GLineEdit_916.config(state='readonly')
    #GLineEdit_916.set_date('01/01/2021')
    GLineEdit_916["borderwidth"] = "2"
    ft = tkFont.Font(family='Arial',size=10)
    GLineEdit_916["font"] = ft
    GLineEdit_916["foreground"] = "#000000"
    GLineEdit_916["justify"] = "left"
    GLineEdit_916.place(x=650,y=50,width=250,height=30)

    att_type = tk.StringVar()
    att_select=ttk.Combobox(tab1,textvariable=att_type,state="readonly")
    att_select["values"]=('Select','Combined','Teachers','Students')
    ft = tkFont.Font(family='Arial',size=10)
    att_select["font"] = ft
    att_select["background"] = "#ffffff"
    att_select["justify"] = "left"
    att_select.place(x=96,y=110,width=250,height=30)

    card_type = tk.StringVar()
    card_select=ttk.Combobox(tab1,textvariable=card_type,state="readonly")
    card_select["values"]=('Select','EXCEL (.xls/.xlsx)','CSV (.csv)')
    ft = tkFont.Font(family='Arial',size=10)
    card_select["font"] = ft
    card_select["background"] = "#ffffff"
    card_select["justify"] = "left"
    card_select.place(x=650,y=110,width=250,height=30)


    """Science=tk.BooleanVar()
    Commerce=tk.BooleanVar()
    Humanities=tk.BooleanVar()


    #class selection
    menubutton = tk.Menubutton(tab1, width=250,text="Select",background="white",activebackground="white",justify="left",anchor='w', indicatoron=True, borderwidth=1, highlightthickness=2, relief="flat")
    menubutton.config(highlightbackground="#333333", highlightcolor= "#333333")
    menu = tk.Menu(menubutton, tearoff=False)
    menubutton.configure(menu=menu)
    #menubutton.grid(column=0,row=1,padx=10, pady=10)
    menubutton.place(x=650,y=110,width=250,height=30)
    choices = {}
    for choice in ("XII-A","XII-B","XII-C"):
        choices[choice] = tk.IntVar(value=0)
        if choice=="XII-A":
            menu.add_checkbutton(label=choice, variable=Science, onvalue=1, offvalue=0)
        if choice=="XII-B":
            menu.add_checkbutton(label=choice, variable=Commerce, onvalue=1, offvalue=0)
        if choice=="XII-C":
            menu.add_checkbutton(label=choice, variable=Humanities, onvalue=1, offvalue=0)"""
        

    GButton_559=tk.Button(tab1, borderwidth=1)
    ft = tkFont.Font(family='Arial',size=10)
    GButton_559["font"] = ft
    GButton_559["fg"] = "#ffffff"
    GButton_559["bg"] = "#333333"
    GButton_559["justify"] = "center"
    GButton_559["text"] = "S U B M I T"
    GButton_559.place(x=340,y=180,width=120,height=35)
    submitcommand = partial(submitcommand, fromdate, todate, att_type, card_type)
    GButton_559["command"] = submitcommand


    GButton_789=tk.Button(tab1, borderwidth=1, relief="ridge")
    ft = tkFont.Font(family='Arial',size=10)
    GButton_789["font"] = ft
    GButton_789["fg"] = "#ffffff"
    GButton_789["bg"] = "#333333"
    GButton_789["justify"] = "center"
    GButton_789["text"] = "R E S E T"
    GButton_789.place(x=510,y=180,width=120,height=35)
    GButton_789["command"] = resetcommand



    ############################## RESULT TAB ##############################
    tabControl2 = ttk.Notebook(content_frame)
    s2 = ttk.Style()
    s2.configure('Frame2.TFrame', background='white')
    

    tab4 = ttk.Frame(tabControl2,style='Frame2.TFrame')    
    tabControl2.add(tab4,text="Import Tab")
    tabControl2.place(x=30,y=500,width=1270,height=270)
 
    ft2 = tkFont.Font(family='Arial Bold',size=11)
    ttk.Label(tab4, text ="Import the users' credentials",font=ft2, background='white', foreground="black").grid(column = 0, row = 0, padx = 10,pady = 10)
    ttk.Label(tab1, text ="Export the users' credentials",font=ft2, background='white', foreground="black").grid(column = 0, row = 0, padx = 10,pady = 10)
    ttk.Label(tab1, text ="Leave from & to blank in case of all ID No.",font=ft, background='white', foreground="red").grid(column = 1, row = 0, padx = 700,pady = 10)
    ttk.Label(tab4, text ="Leave from & to blank in case of all ID No.",font=ft, background='white', foreground="red").grid(column = 1, row = 0, padx = 700,pady = 10)
    
    GLabel_516=tk.Label(tab4, anchor = 'w', background='white')
    ft = tkFont.Font(family='Arial Bold',size=10)
    GLabel_516["font"] = ft
    GLabel_516["fg"] = "#000000"
    GLabel_516["text"] = "From Row"
    GLabel_516.place(x=10,y=50,width=70,height=25)

    GLabel_901=tk.Label(tab4, anchor = 'w', background='white')
    ft = tkFont.Font(family='Arial Bold',size=10)
    GLabel_901["font"] = ft
    GLabel_901["fg"] = "#000000"
    GLabel_901["justify"] = "left"
    GLabel_901["text"] = "To Row"
    GLabel_901.place(x=550,y=50,width=70,height=25)

    GLabel_984=tk.Label(tab4, anchor = 'w', background='white')
    ft = tkFont.Font(family='Arial Bold',size=10)
    GLabel_984["font"] = ft
    GLabel_984["fg"] = "#000000"
    GLabel_984["justify"] = "left"
    GLabel_984["text"] = "Header"
    GLabel_984.place(x=10,y=110,width=78,height=25)

    GLabel_32=tk.Label(tab4, anchor = 'w', background='white')
    ft = tkFont.Font(family='Arial Bold',size=10)
    GLabel_32["font"] = ft
    GLabel_32["fg"] = "#000000"
    GLabel_32["justify"] = "left"
    GLabel_32["text"] = "Format "
    GLabel_32.place(x=550,y=110,width=70,height=25)

    fromdate = tk.StringVar()
    GLineEdit_97=Entry(tab4,textvariable = fromdate, highlightthickness=2, highlightbackground="#333333", relief="flat")
    #GLineEdit_97=DateEntry(tab4,locale="en_US", date_pattern="dd/MM/yyyy", textvariable = fromdate, highlightthickness=1, relief="flat")
    #GLineEdit_97.config(state='readonly')
    #GLineEdit_97.set_date('01/01/2021')
    GLineEdit_97["borderwidth"] = "2"
    ft = tkFont.Font(family='Arial',size=10)
    GLineEdit_97["font"] = ft
    GLineEdit_97["foreground"] = "#000000"
    GLineEdit_97["justify"] = "left"
    GLineEdit_97.place(x=96,y=50,width=250,height=30)

    todate = tk.StringVar()
    GLineEdit_916=Entry(tab4,textvariable = todate, highlightthickness=2, highlightbackground="#333333", relief="flat")
    #GLineEdit_916=DateEntry(tab4,locale="en_US", date_pattern="dd/MM/yyyy", textvariable = todate, highlightthickness=1, relief="flat")
    #GLineEdit_916.config(state='readonly')
    #GLineEdit_916.set_date('01/01/2021')
    GLineEdit_916["borderwidth"] = "2"
    ft = tkFont.Font(family='Arial',size=10)
    GLineEdit_916["font"] = ft
    GLineEdit_916["foreground"] = "#000000"
    GLineEdit_916["justify"] = "left"
    GLineEdit_916.place(x=650,y=50,width=250,height=30)

    att_type = tk.StringVar()
    att_select=ttk.Combobox(tab4,textvariable=att_type,state="readonly")
    att_select["values"]=('Select','Yes','No')
    ft = tkFont.Font(family='Arial',size=10)
    att_select["font"] = ft
    att_select["background"] = "#ffffff"
    att_select["justify"] = "left"
    att_select.place(x=96,y=110,width=250,height=30)

    card_type = tk.StringVar()
    card_select=ttk.Combobox(tab4,textvariable=card_type,state="readonly")
    card_select["values"]=('Select','CSV (.csv)')
    ft = tkFont.Font(family='Arial',size=10)
    card_select["font"] = ft
    card_select["background"] = "#ffffff"
    card_select["justify"] = "left"
    card_select.place(x=650,y=110,width=250,height=30)

    GButton_559=tk.Button(tab4, borderwidth=1)
    ft = tkFont.Font(family='Arial',size=10)
    GButton_559["font"] = ft
    GButton_559["fg"] = "#ffffff"
    GButton_559["bg"] = "#333333"
    GButton_559["justify"] = "center"
    GButton_559["text"] = "S U B M I T"
    GButton_559.place(x=340,y=200,width=120,height=35)
    ssubmitcommand = partial(ssubmitcommand, fromdate, todate, att_type, card_type)
    GButton_559["command"] = ssubmitcommand

    GButton_789=tk.Button(tab4, borderwidth=1, relief="ridge")
    ft = tkFont.Font(family='Arial',size=10)
    GButton_789["font"] = ft
    GButton_789["fg"] = "#ffffff"
    GButton_789["bg"] = "#333333"
    GButton_789["justify"] = "center"
    GButton_789["text"] = "R E S E T"
    GButton_789.place(x=510,y=200,width=120,height=35)
    GButton_789["command"] = rresetcommand

    root.mainloop()
#start_impexp("Harsh")    

