from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
from ttkthemes import ThemedStyle
from functools import partial
import pandas as pd
import mysql.connector
import numpy as np
from table_class import *
#from db_class import *
from datetime import date, timedelta
from tkinter import messagebox,filedialog
from PIL import Image, ImageTk
from report_print import *
from report_print2 import *


color="#28383c"
#color="#5f6b6d"
root,submitcommand,submitcommandd="","",""
Science, Commerce, Humanities, Sciencee, Commercee, Humanitiess,Scienceee, Commerceee, Humanitiesss="","","","","","","","",""
GLineEdit_97,GLineEdit_916,GLineEdit_977,GLineEdit_9166,GLineEdit_9777,GLineEdit_91666,att_select,att_selectt,att_selecttt="","","","","","","","",""
tab4=""
result_set=""
final=""

from admin import *
from admin_generateids import *
from admin_impexp import *
from admin_takeattendance import *
from forgot import *

root,gtx_name="",""

def home():
    try:
        root.destroy()
        admin_start(gtx_name)
    except:
        try:
            root.destroy()
            admin_start()
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
            root.destroy()
            admin_start(gtx_name)
        root.destroy()
        admin_start(gtx_name)
        
def mu():
    try:
        root.destroy()
        start_impexp(gtx_name)
    except:
        try:
            root.destroy()
            start_impexp(gtx_name)
        except:
            root.destroy()
            admin_start(gtx_name)
        root.destroy()
        admin_start(gtx_name)
def cp():
    try:
        root.destroy()
        forgot()
    except:
        try:
            root.destroy()
            start_impexp(gtx_name)
        except:
            root.destroy()
            admin_start(gtx_name)
        root.destroy()
        admin_start(gtx_name)
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
    Classes=[]
    if Science.get()==True:
        Classes.append("XII-A")
    if Commerce.get()==True:
        Classes.append("XII-B")
    if Humanities.get()==True:
        Classes.append("XII-C")
    if resulttype=="":
        messagebox.showerror("Error 101", "Fill Properly")
    elif len(Classes)==0:
        messagebox.showerror("Error 102", "Fill Properly")
    else:
        query_execute(fromm.get(),to.get(),resulttype.get(),Classes)
    

def resetcommand():
    GLineEdit_97.set_date('01/01/2021')
    GLineEdit_916.set_date('01/01/2021')
    att_select.set('')
    for items in Science, Commerce, Humanities:
        items.set(False)

def submitcommandd(fromm,to,resulttype,classes):
    Classes=[]
    if Sciencee.get()==True:
        Classes.append("XII-A")
    if Commercee.get()==True:
        Classes.append("XII-B")
    if Humanitiess.get()==True:
        Classes.append("XII-C")
    if resulttype=="":
        messagebox.showerror("Error 101", "Fill Properly")
    elif len(Classes)==0:
        messagebox.showerror("Error 102", "Fill Properly")
    else:
        query_executee(fromm.get(),to.get(),resulttype.get(),Classes)

def resetcommandd():
    GLineEdit_977.set_date('01/01/2021')
    GLineEdit_9166.set_date('01/01/2021')
    att_selectt.set('')
    for items in Sciencee, Commercee, Humanitiess:
        items.set(False)


def submitcommanddd(fromm,to,resulttype,classes):
    Classes=[]
    if Scienceee.get()==True:
        Classes.append("XII-A")
    if Commerceee.get()==True:
        Classes.append("XII-B")
    if Humanitiesss.get()==True:
        Classes.append("XII-C")
    if resulttype=="":
        messagebox.showerror("Error 101", "Fill Properly")
    elif len(Classes)==0:
        messagebox.showerror("Error 102", "Fill Properly")
    else:
        query_executeee(fromm.get(),to.get(),resulttype.get(),Classes)

def resetcommanddd():
    GLineEdit_9777.set_date('01/01/2021')
    GLineEdit_91666.set_date('01/01/2021')
    att_selectt.set('')
    for items in Sciencee, Commercee, Humanitiess:
        items.set(False)

def send():
    draw_Tableee(final)
    
def export():
    export_file_path = filedialog.asksaveasfilename(defaultextension='.xlsx')
    final.to_excel (export_file_path, index = False, header=True)
    messagebox.showinfo("Export","Excel exported successfully")
    
def report_send():
    a=messagebox.askquestion("Border", "Do you want borders alongside?")
    if a=="yes":
        receive_Data(final.values.tolist())
    else:
        receive_Data2(final.values.tolist())


def query_execute(fromm,to,resulttype,classes):
    global tab4,result_set,final
    combined_list=[]
    present_list=[]
    absent_list=[]
    
    my_connect = mysql.connector.connect(
        host="185.210.145.52",
        user="u649387556_iproject",
        password="Remal@123",
        database="u649387556_ipproject"
    )

    my_conn = my_connect.cursor()
    my_conn2 = my_connect.cursor()
    
    query="select id,name,class,type from people;"
    my_conn.execute(query)
    rows = my_conn.fetchall()
    d=""
    for j in classes:
        d="'"+j+"',"
    d=d[:-1]
    
    
    start_date=date(2021,1,1)
    end_date = date(2021,3,1)

    delta = timedelta(days=1)

    for i in rows:
        i_id_no=i[0]
        i_name=i[1]
        i_class=i[2]
        i_type=i[3]
        start_date=date(2021,1,1)
        print("...Crawling...")
        while start_date <= end_date:
            count=0
            dd=start_date.strftime("%d/%m/%Y")
            start_date+= delta
        
            query="select id as ID,name as NAME,type as TYPE,class as CLASS,date as DATE,time as 'TIME STAMP (IST)' from attendance\
 where STR_TO_DATE(date,'%d/%m/%Y') between (STR_TO_DATE('"+fromm+"','%d/%m/%Y')) and (STR_TO_DATE('"+to+"','%d/%m/%Y')) and class in ("+d+") and id='"+i_id_no+"' and date='"+dd+"'"
            s=localfind(my_conn2,query)
            count=0
            for x in s:
                count+=1
            if count==0:
                l=[i_id_no,i_name,i_type,i_class,dd,"ABSENT","N/A"]
                absent_list.append(l)
            else:
                l=[i_id_no,i_name,i_type,i_class,dd,"PRESENT",x[5]]
                present_list.append(l)
            combined_list.append(l)
        
            
            
    keys=['ID NO.','NAME','TYPE','CLASS','DATE','STATUS','TIMESTAMP (IST)']
    combined=pd.DataFrame(combined_list,columns=keys)
    present=pd.DataFrame(present_list,columns=keys)
    absent=pd.DataFrame(absent_list,columns=keys)

    if resulttype=="Both":
        p=combined
        selected=combined_list
    elif resulttype=="Present":
        p=present
        selected=present_list
    else:
        p=absent
        selected=absent_list
    """names = [ x[0] for x in my_conn.description]
    rows = my_conn.fetchall()"""

    
    #p=p.sort_values(by=['DATE', 'ID NO.'])
    p=p.assign(x=pd.to_datetime(p['DATE'])).sort_values('x').drop('x',1)

    p['DATE'] = pd.to_datetime(p['DATE'], dayfirst=True)
    p = p.sort_values(['DATE','ID NO.'], ascending=[True,True])
    #p['DATE']=p['DATE'].dt.date
    p['DATE']=p['DATE'].dt.strftime('%d/%m/%Y')
    final=p
    
    selected=p.values.tolist()
    

    
    i=0
    top=75
    side=15
    ft = tkFont.Font(family='Arial Bold',size=10)
    ft1 = tkFont.Font(family='Arial',size=10)

    h_txt=StringVar()
    h_txt.set("ID NO")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=side,y=50,width=50,height=25)

    h_txt=StringVar()
    h_txt.set("NAME")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=65,y=50,width=175,height=25)

    h_txt=StringVar()
    h_txt.set("TYPE")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=240,y=50,width=90,height=25)

    h_txt=StringVar()
    h_txt.set("CLASS")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=330,y=50,width=50,height=25)

    h_txt=StringVar()
    h_txt.set("DATE")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=380,y=50,width=90,height=25)

    h_txt=StringVar()
    h_txt.set("STATUS")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=470,y=50,width=90,height=25)

    
    h_txt=StringVar()
    h_txt.set("TIMESTAMP (IST)")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=560,y=50,width=175,height=25)
    """
    l=tk.Button(tab4, text="Showing only 7 entries. Click for more")
    l.place(x=600, y=450,width=300,height=50)
    
    """
    
    #GButton_849["command"] = GButton_849_command
    
    
    row_count=0
    for student in selected:
        row_count+=1
        
        GButton_8490=tk.Button(tab4, borderwidth=1)
        GButton_8490["borderwidth"] = "0px"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_8490["font"] = ft
        GButton_8490["bg"] = "#333333"
        GButton_8490["fg"] = "#ffffff"
        GButton_8490["justify"] = "left"
        GButton_8490["text"] = "SHOW FULL TABLE"
        GButton_8490.place(x=15,y=225,width=150,height=35)
        GButton_8490["command"]=send

        GButton_84900=tk.Button(tab4, borderwidth=1)
        GButton_84900["borderwidth"] = "0px"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_84900["font"] = ft
        GButton_84900["bg"] = "#333333"
        GButton_84900["fg"] = "#ffffff"
        GButton_84900["justify"] = "left"
        GButton_84900["text"] = "EXPORT TO EXCEL"
        GButton_84900.place(x=550,y=225,width=150,height=35)
        GButton_84900["command"]=export

        GButton_849000=tk.Button(tab4, borderwidth=1)
        GButton_849000["borderwidth"] = "0px"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_849000["font"] = ft
        GButton_849000["bg"] = "#333333"
        GButton_849000["fg"] = "#ffffff"
        GButton_849000["justify"] = "left"
        GButton_849000["text"] = "GENERATE PDF REPORT"
        GButton_849000.place(x=1050,y=225,width=175,height=35)
        GButton_849000["command"]=report_send
        
        if row_count==7:
            ft2 = tkFont.Font(family='Arial',size=10)
            ttk.Label(tab4, text ="Showing only 7 rows",font=ft2, background='white', foreground="red").grid(column = 4, row = 0, padx = 350,pady = 10)
            
            break
        else:
            for j in range(len(student)):
                mystr = StringVar()
                mystr.set(student[j])
                #print(j,mystr.get())
                
                e = Entry(tab4, width=100,textvariable=mystr,state='disabled',font=ft1,disabledforeground='black',disabledbackground='white')
                ii=i+20
                if j==6 or j==1:
                    e.place(x=side,y=top,width=175,height=25)
                    side+=175
                elif j==4 or j==2 or j==5 or j==7:
                    e.place(x=side,y=top,width=90,height=25)
                    side+=90
                else:
                    e.place(x=side,y=top,width=50,height=25)
                    side+=50
                e.insert(END, student[j])
                e.configure(state='readonly')
                #e.grid(column=1,row=0)
                
            i=i+1
            top+=21
            side=15
    
        
def query_executee(fromm,to,resulttype,classes):
    global tab4,result_set,final
    combined_list=[]
    present_list=[]
    absent_list=[]
    
    my_connect = mysql.connector.connect(
        host="185.210.145.52",
        user="u649387556_iproject",
        password="Remal@123",
        database="u649387556_ipproject"
    )

    my_conn = my_connect.cursor()
    my_conn2 = my_connect.cursor()
    
    query="select id,name,class,type from people where type='Student'"
    my_conn.execute(query)
    rows = my_conn.fetchall()
    d=""
    for j in classes:
        d="'"+j+"',"
    d=d[:-1]
    
    
    
    start_date = date(2021, 1, 1)
    end_date = date(2021, 3, 1)
    delta = timedelta(days=1)

    for i in rows:
        i_id_no=i[0]
        i_name=i[1]
        i_class=i[2]
        i_type=i[3]
        start_date=date(2021,1,1)
        while start_date <= end_date:
            count=0
            dd=start_date.strftime("%d/%m/%Y")
            start_date+= delta
        
            query="select id as ID,name as NAME,type as TYPE,class as CLASS,date as DATE,time as 'TIME STAMP (IST)' from attendance\
 where STR_TO_DATE(date,'%d/%m/%Y') between (STR_TO_DATE('"+fromm+"','%d/%m/%Y')) and (STR_TO_DATE('"+to+"','%d/%m/%Y')) and class in ("+d+") and id='"+i_id_no+"' and date='"+dd+"'"
            
            s=localfind(my_conn2,query)
            count=0
            for x in s:
                count+=1
            if count==0:
                l=[i_id_no,i_name,i_type,i_class,dd,"ABSENT","N/A"]
                absent_list.append(l)
            else:
                l=[i_id_no,i_name,i_type,i_class,dd,"PRESENT",x[5]]
                present_list.append(l)
            combined_list.append(l)
    keys=['ID NO.','NAME','TYPE','CLASS','DATE','STATUS','TIMESTAMP (IST)']
    combined=pd.DataFrame(combined_list,columns=keys)
    present=pd.DataFrame(present_list,columns=keys)
    absent=pd.DataFrame(absent_list,columns=keys)

    if resulttype=="Both":
        p=combined
        selected=combined_list
    elif resulttype=="Present":
        p=present
        selected=present_list
    else:
        p=absent
        selected=absent_list
    """names = [ x[0] for x in my_conn.description]
    rows = my_conn.fetchall()"""

    
    #p=p.sort_values(by=['DATE', 'ID NO.'])
    p=p.assign(x=pd.to_datetime(p['DATE'])).sort_values('x').drop('x',1)

    p['DATE'] = pd.to_datetime(p['DATE'], dayfirst=True)
    p = p.sort_values('DATE', ascending=True)
    #p['DATE']=p['DATE'].dt.date
    p['DATE']=p['DATE'].dt.strftime('%d/%m/%Y')
    final=p

    
    selected=p.values.tolist()
    

    
    i=0
    top=75
    side=15
    ft = tkFont.Font(family='Arial Bold',size=10)
    ft1 = tkFont.Font(family='Arial',size=10)

    h_txt=StringVar()
    h_txt.set("ID NO")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=side,y=50,width=50,height=25)

    h_txt=StringVar()
    h_txt.set("NAME")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=65,y=50,width=175,height=25)

    h_txt=StringVar()
    h_txt.set("TYPE")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=240,y=50,width=90,height=25)

    h_txt=StringVar()
    h_txt.set("CLASS")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=330,y=50,width=50,height=25)

    h_txt=StringVar()
    h_txt.set("DATE")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=380,y=50,width=90,height=25)

    h_txt=StringVar()
    h_txt.set("STATUS")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=470,y=50,width=90,height=25)

    
    h_txt=StringVar()
    h_txt.set("TIMESTAMP (IST)")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=560,y=50,width=175,height=25)
    """
    l=tk.Button(tab4, text="Showing only 7 entries. Click for more")
    l.place(x=600, y=450,width=300,height=50)
    
    """
    
    #GButton_849["command"] = GButton_849_command
    
    
    row_count=0
    for student in selected:
        row_count+=1
        if row_count==7:
            GButton_8490=tk.Button(tab4, borderwidth=1)
            GButton_8490["borderwidth"] = "0px"
            ft = tkFont.Font(family='Arial',size=10)
            GButton_8490["font"] = ft
            GButton_8490["bg"] = "#333333"
            GButton_8490["fg"] = "#ffffff"
            GButton_8490["justify"] = "left"
            GButton_8490["text"] = "SHOW FULL TABLE"
            GButton_8490.place(x=15,y=225,width=150,height=35)
            GButton_8490["command"]=send

            GButton_84900=tk.Button(tab4, borderwidth=1)
            GButton_84900["borderwidth"] = "0px"
            ft = tkFont.Font(family='Arial',size=10)
            GButton_84900["font"] = ft
            GButton_84900["bg"] = "#333333"
            GButton_84900["fg"] = "#ffffff"
            GButton_84900["justify"] = "left"
            GButton_84900["text"] = "EXPORT TO EXCEL"
            GButton_84900.place(x=550,y=225,width=150,height=35)
            GButton_84900["command"]=export

            GButton_849000=tk.Button(tab4, borderwidth=1)
            GButton_849000["borderwidth"] = "0px"
            ft = tkFont.Font(family='Arial',size=10)
            GButton_849000["font"] = ft
            GButton_849000["bg"] = "#333333"
            GButton_849000["fg"] = "#ffffff"
            GButton_849000["justify"] = "left"
            GButton_849000["text"] = "GENERATE PDF REPORT"
            GButton_849000.place(x=1050,y=225,width=175,height=35)
            GButton_849000["command"]=report
            

            ft2 = tkFont.Font(family='Arial',size=10)
            ttk.Label(tab4, text ="Showing only 7 rows",font=ft2, background='white', foreground="red").grid(column = 4, row = 0, padx = 350,pady = 10)
            
            break
        else:
            for j in range(len(student)):
                mystr = StringVar()
                mystr.set(student[j])
                #print(j,mystr.get())
                
                e = Entry(tab4, width=100,textvariable=mystr,state='disabled',font=ft1,disabledforeground='black',disabledbackground='white')
                ii=i+20
                if j==6 or j==1:
                    e.place(x=side,y=top,width=175,height=25)
                    side+=175
                elif j==4 or j==2 or j==5 or j==7:
                    e.place(x=side,y=top,width=90,height=25)
                    side+=90
                else:
                    e.place(x=side,y=top,width=50,height=25)
                    side+=50
                e.insert(END, student[j])
                e.configure(state='readonly')
                #e.grid(column=1,row=0)
                
            i=i+1
            top+=21
            
            side=15

def query_executeee(fromm,to,resulttype,classes):
    global tab4,result_set,final
    combined_list=[]
    present_list=[]
    absent_list=[]
    
    my_connect = mysql.connector.connect(
        host="185.210.145.52",
        user="u649387556_iproject",
        password="Remal@123",
        database="u649387556_ipproject"
    )

    my_conn = my_connect.cursor()
    my_conn2 = my_connect.cursor()
    
    query="select id,name,class,type from people where type='Teacher'"
    my_conn.execute(query)
    rows = my_conn.fetchall()
    d=""
    for j in classes:
        d="'"+j+"',"
    d=d[:-1]
    start_date = date(2021, 1, 1)
    end_date = date(2021, 3, 1)
    delta = timedelta(days=1)
    start_date=date(2021,1,1)
    for i in rows:
        i_id_no=i[0]
        i_name=i[1]
        i_class=i[2]
        i_type=i[3]
        
        while start_date <= end_date:
            count=0
            dd=start_date.strftime("%d/%m/%Y")
            start_date+= delta
        
            query="select id as ID,name as NAME,type as TYPE,class as CLASS,date as DATE,time as 'TIME STAMP (IST)' from attendance\
 where STR_TO_DATE(date,'%d/%m/%Y') between (STR_TO_DATE('"+fromm+"','%d/%m/%Y')) and (STR_TO_DATE('"+to+"','%d/%m/%Y')) and class in ("+d+") and id='"+i_id_no+"' and date='"+dd+"'"
            
            s=localfind(my_conn2,query)
            count=0
            for x in s:
                count+=1
            if count==0:
                l=[i_id_no,i_name,i_type,i_class,dd,"ABSENT","N/A"]
                absent_list.append(l)
            else:
                l=[i_id_no,i_name,i_type,i_class,dd,"PRESENT",x[5]]
                present_list.append(l)
            combined_list.append(l)
    keys=['ID NO.','NAME','TYPE','CLASS','DATE','STATUS','TIMESTAMP (IST)']
    combined=pd.DataFrame(combined_list,columns=keys)
    present=pd.DataFrame(present_list,columns=keys)
    absent=pd.DataFrame(absent_list,columns=keys)

    if resulttype=="Both":
        p=combined
        selected=combined_list
    elif resulttype=="Present":
        p=present
        selected=present_list
    else:
        p=absent
        selected=absent_list
    """names = [ x[0] for x in my_conn.description]
    rows = my_conn.fetchall()"""

    
    #p=p.sort_values(by=['DATE', 'ID NO.'])
    p=p.assign(x=pd.to_datetime(p['DATE'])).sort_values('x').drop('x',1)

    p['DATE'] = pd.to_datetime(p['DATE'], dayfirst=True)
    p = p.sort_values('DATE', ascending=True)
    #p['DATE']=p['DATE'].dt.date
    p['DATE']=p['DATE'].dt.strftime('%d/%m/%Y')
    final=p

    
    selected=p.values.tolist()
    

    
    i=0
    top=75
    side=15
    ft = tkFont.Font(family='Arial Bold',size=10)
    ft1 = tkFont.Font(family='Arial',size=10)

    h_txt=StringVar()
    h_txt.set("ID NO")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=side,y=50,width=50,height=25)

    h_txt=StringVar()
    h_txt.set("NAME")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=65,y=50,width=175,height=25)

    h_txt=StringVar()
    h_txt.set("TYPE")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=240,y=50,width=90,height=25)

    h_txt=StringVar()
    h_txt.set("CLASS")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=330,y=50,width=50,height=25)

    h_txt=StringVar()
    h_txt.set("DATE")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=380,y=50,width=90,height=25)

    h_txt=StringVar()
    h_txt.set("STATUS")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=470,y=50,width=90,height=25)

    
    h_txt=StringVar()
    h_txt.set("TIMESTAMP (IST)")
    h = Entry(tab4, textvariable=h_txt,state="readonly",font=ft,disabledforeground='black',disabledbackground='white')
    h.place(x=560,y=50,width=175,height=25)
    """
    l=tk.Button(tab4, text="Showing only 7 entries. Click for more")
    l.place(x=600, y=450,width=300,height=50)
    
    """
    
    #GButton_849["command"] = GButton_849_command
    
    
    row_count=0
    for student in selected:
        row_count+=1
        if row_count==7:
            GButton_8490=tk.Button(tab4, borderwidth=1)
            GButton_8490["borderwidth"] = "0px"
            ft = tkFont.Font(family='Arial',size=10)
            GButton_8490["font"] = ft
            GButton_8490["bg"] = "#333333"
            GButton_8490["fg"] = "#ffffff"
            GButton_8490["justify"] = "left"
            GButton_8490["text"] = "SHOW FULL TABLE"
            GButton_8490.place(x=15,y=225,width=150,height=35)
            GButton_8490["command"]=send

            GButton_84900=tk.Button(tab4, borderwidth=1)
            GButton_84900["borderwidth"] = "0px"
            ft = tkFont.Font(family='Arial',size=10)
            GButton_84900["font"] = ft
            GButton_84900["bg"] = "#333333"
            GButton_84900["fg"] = "#ffffff"
            GButton_84900["justify"] = "left"
            GButton_84900["text"] = "EXPORT TO EXCEL"
            GButton_84900.place(x=550,y=225,width=150,height=35)
            GButton_84900["command"]=export

            GButton_849000=tk.Button(tab4, borderwidth=1)
            GButton_849000["borderwidth"] = "0px"
            ft = tkFont.Font(family='Arial',size=10)
            GButton_849000["font"] = ft
            GButton_849000["bg"] = "#333333"
            GButton_849000["fg"] = "#ffffff"
            GButton_849000["justify"] = "left"
            GButton_849000["text"] = "GENERATE PDF REPORT"
            GButton_849000.place(x=1050,y=225,width=175,height=35)
            GButton_849000["command"]=report
            

            ft2 = tkFont.Font(family='Arial',size=10)
            ttk.Label(tab4, text ="Showing only 7 rows",font=ft2, background='white', foreground="red").grid(column = 4, row = 0, padx = 350,pady = 10)
            
            break
        else:
            for j in range(len(student)):
                mystr = StringVar()
                mystr.set(student[j])
                #print(j,mystr.get())
                
                e = Entry(tab4, width=100,textvariable=mystr,state='disabled',font=ft1,disabledforeground='black',disabledbackground='white')
                ii=i+20
                if j==6 or j==1:
                    e.place(x=side,y=top,width=175,height=25)
                    side+=175
                elif j==4 or j==2 or j==5 or j==7:
                    e.place(x=side,y=top,width=90,height=25)
                    side+=90
                else:
                    e.place(x=side,y=top,width=50,height=25)
                    side+=50
                e.insert(END, student[j])
                e.configure(state='readonly')
                #e.grid(column=1,row=0)
                
            i=i+1
            top+=21
            
            side=15
        
        
tabControl2=""

def start_viewattendance(name):
    global root,gtx_name,tab4,scrollbar,tabControl2,submitcommand,submitcommandd,submitcommanddd,Science, Commerce, Humanities, Sciencee, Commercee, Humanitiess,Scienceee, Commerceee, Humanitiesss
    global GLineEdit_97,GLineEdit_916,GLineEdit_977,GLineEdit_9166,GLineEdit_9777,GLineEdit_91666,att_select,att_selectt,att_selecttt
    gtx_name=name
    root = Tk()
    root.geometry("300x200")
    root.attributes("-fullscreen", True)
    root.title("CASS | View Attendance")
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
    greeting["text"] = "Hello "+name+" | View Attendance"
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
    tab2 = ttk.Frame(tabControl,style='Frame1.TFrame')
    tab3 = ttk.Frame(tabControl,style='Frame1.TFrame')


    tabControl.add(tab1, text ='Combined')
    tabControl.add(tab2, text ='Student')
    tabControl.add(tab3, text ='Teacher')
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
    GLabel_516["text"] = "From Date"
    GLabel_516.place(x=10,y=50,width=70,height=25)

    GLabel_901=tk.Label(tab1, anchor = 'w', background='white')
    ft = tkFont.Font(family='Arial Bold',size=10)
    GLabel_901["font"] = ft
    GLabel_901["fg"] = "#000000"
    GLabel_901["justify"] = "left"
    GLabel_901["text"] = "To Date"
    GLabel_901.place(x=550,y=50,width=70,height=25)

    GLabel_984=tk.Label(tab1, anchor = 'w', background='white')
    ft = tkFont.Font(family='Arial Bold',size=10)
    GLabel_984["font"] = ft
    GLabel_984["fg"] = "#000000"
    GLabel_984["justify"] = "left"
    GLabel_984["text"] = "Result Type"
    GLabel_984.place(x=10,y=110,width=78,height=25)

    GLabel_32=tk.Label(tab1, anchor = 'w', background='white')
    ft = tkFont.Font(family='Arial Bold',size=10)
    GLabel_32["font"] = ft
    GLabel_32["fg"] = "#000000"
    GLabel_32["justify"] = "left"
    GLabel_32["text"] = "Class "
    GLabel_32.place(x=550,y=110,width=70,height=25)

    fromdate = tk.StringVar()
    GLineEdit_97=DateEntry(tab1,locale="en_US", date_pattern="dd/MM/yyyy", textvariable = fromdate, highlightthickness=1, relief="flat")
    GLineEdit_97.config(state='readonly')
    GLineEdit_97.set_date('01/01/2021')
    GLineEdit_97["borderwidth"] = "1"
    ft = tkFont.Font(family='Arial',size=10)
    GLineEdit_97["font"] = ft
    GLineEdit_97["foreground"] = "#000000"
    GLineEdit_97["justify"] = "left"
    GLineEdit_97.place(x=96,y=50,width=250,height=30)

    todate = tk.StringVar()
    GLineEdit_916=DateEntry(tab1,locale="en_US", date_pattern="dd/MM/yyyy", textvariable = todate, highlightthickness=1, relief="flat")
    GLineEdit_916.config(state='readonly')
    GLineEdit_916.set_date('01/01/2021')
    GLineEdit_916["borderwidth"] = "1"
    ft = tkFont.Font(family='Arial',size=10)
    GLineEdit_916["font"] = ft
    GLineEdit_916["foreground"] = "#000000"
    GLineEdit_916["justify"] = "left"
    GLineEdit_916.place(x=650,y=50,width=250,height=30)

    att_type = tk.StringVar()
    att_select=ttk.Combobox(tab1,textvariable=att_type,state="readonly")
    att_select["values"]=('Select','Present','Absent','Both')
    ft = tkFont.Font(family='Arial',size=10)
    att_select["font"] = ft
    att_select["background"] = "#ffffff"
    att_select["justify"] = "left"
    att_select.place(x=96,y=110,width=250,height=30)

    Science=tk.BooleanVar()
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
            menu.add_checkbutton(label=choice, variable=Humanities, onvalue=1, offvalue=0)
        

    GButton_559=tk.Button(tab1, borderwidth=1)
    ft = tkFont.Font(family='Arial',size=10)
    GButton_559["font"] = ft
    GButton_559["fg"] = "#ffffff"
    GButton_559["bg"] = "#333333"
    GButton_559["justify"] = "center"
    GButton_559["text"] = "S U B M I T"
    GButton_559.place(x=340,y=180,width=120,height=35)
    submitcommand = partial(submitcommand, fromdate, todate, att_type, choices)
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


    ########################################################################
    ########################################################################

    GLabel_5166=tk.Label(tab2, anchor = 'w', background='white')
    ft = tkFont.Font(family='Arial Bold',size=10)
    GLabel_5166["font"] = ft
    GLabel_5166["fg"] = "#000000"
    GLabel_5166["text"] = "From Date"
    GLabel_5166.place(x=10,y=50,width=70,height=25)

    GLabel_9011=tk.Label(tab2, anchor = 'w', background='white')
    ft = tkFont.Font(family='Arial Bold',size=10)
    GLabel_9011["font"] = ft
    GLabel_9011["fg"] = "#000000"
    GLabel_9011["justify"] = "left"
    GLabel_9011["text"] = "To Date"
    GLabel_9011.place(x=550,y=50,width=70,height=25)

    GLabel_9844=tk.Label(tab2, anchor = 'w', background='white')
    ft = tkFont.Font(family='Arial Bold',size=10)
    GLabel_9844["font"] = ft
    GLabel_9844["fg"] = "#000000"
    GLabel_9844["justify"] = "left"
    GLabel_9844["text"] = "Result Type"
    GLabel_9844.place(x=10,y=110,width=78,height=25)

    GLabel_322=tk.Label(tab2, anchor = 'w', background='white')
    ft = tkFont.Font(family='Arial Bold',size=10)
    GLabel_322["font"] = ft
    GLabel_322["fg"] = "#000000"
    GLabel_322["justify"] = "left"
    GLabel_322["text"] = "Class "
    GLabel_322.place(x=550,y=110,width=70,height=25)

    fromdatee = tk.StringVar()
    GLineEdit_977=DateEntry(tab2,locale="en_US", date_pattern="dd/MM/yyyy", textvariable = fromdatee, highlightthickness=1, relief="flat")
    GLineEdit_977.config(state='readonly')
    GLineEdit_977.set_date('01/01/2021')
    GLineEdit_977["borderwidth"] = "1"
    ft = tkFont.Font(family='Arial',size=10)
    GLineEdit_977["font"] = ft
    GLineEdit_977["foreground"] = "#000000"
    GLineEdit_977["justify"] = "left"
    GLineEdit_977.place(x=96,y=50,width=250,height=30)

    todatee = tk.StringVar()
    GLineEdit_9166=DateEntry(tab2,locale="en_US", date_pattern="dd/MM/yyyy", textvariable = todatee, highlightthickness=1, relief="flat")
    GLineEdit_9166.config(state='readonly')
    GLineEdit_9166.set_date('01/01/2021')
    GLineEdit_9166["borderwidth"] = "1"
    ft = tkFont.Font(family='Arial',size=10)
    GLineEdit_9166["font"] = ft
    GLineEdit_9166["foreground"] = "#000000"
    GLineEdit_9166["justify"] = "left"
    GLineEdit_9166.place(x=650,y=50,width=250,height=30)

    att_typee = tk.StringVar()
    att_selectt=ttk.Combobox(tab2,textvariable=att_typee,state="readonly")
    att_selectt["values"]=('Select','Present','Absent','Both')
    ft = tkFont.Font(family='Arial',size=10)
    att_selectt["font"] = ft
    att_selectt["background"] = "#ffffff"
    att_selectt["justify"] = "left"
    att_selectt.place(x=96,y=110,width=250,height=30)

    Sciencee=tk.BooleanVar()
    Commercee=tk.BooleanVar()
    Humanitiess=tk.BooleanVar()


    #class selection
    menuubuttonn = tk.Menubutton(tab2, width=250,text="Select",background="white",activebackground="white",justify="left",anchor='w', indicatoron=True, borderwidth=1, highlightthickness=2, relief="flat")
    menuubuttonn.config(highlightbackground="#333333", highlightcolor= "#333333")
    menuu = tk.Menu(menuubuttonn, tearoff=False)
    menuubuttonn.configure(menu=menuu)
    #menuubuttonn.grid(column=0,row=1,padx=10, pady=10)
    menuubuttonn.place(x=650,y=110,width=250,height=30)
    choicess = {}
    for choice in ("XII-A","XII-B","XII-C"):
        choicess[choice] = tk.IntVar(value=0)
        if choice=="XII-A":
            menuu.add_checkbutton(label=choice, variable=Sciencee, onvalue=1, offvalue=0)
        if choice=="XII-B":
            menuu.add_checkbutton(label=choice, variable=Commercee, onvalue=1, offvalue=0)
        if choice=="XII-C":
            menuu.add_checkbutton(label=choice, variable=Humanitiess, onvalue=1, offvalue=0)
        

    GButton_5599=tk.Button(tab2, borderwidth=1)
    GButton_5599["bg"] = "#efefef"
    ft = tkFont.Font(family='Arial',size=10)
    GButton_5599["font"] = ft
    GButton_5599["fg"] = "#ffffff"
    GButton_5599["bg"] = "#333333"
    GButton_5599["justify"] = "center"
    GButton_5599["text"] = "S U B M I T"
    GButton_5599.place(x=340,y=180,width=120,height=35)
    submitcommandd = partial(submitcommandd, fromdatee, todatee, att_typee, choicess)
    GButton_5599["command"] = submitcommandd

    GButton_7899=tk.Button(tab2, borderwidth=1, relief="ridge")
    GButton_7899["bg"] = "#efefef"
    ft = tkFont.Font(family='Arial',size=10)
    GButton_7899["font"] = ft
    GButton_7899["fg"] = "#ffffff"
    GButton_7899["bg"] = "#333333"
    GButton_7899["justify"] = "center"
    GButton_7899["text"] = "R E S E T"
    GButton_7899.place(x=510,y=180,width=120,height=35)
    GButton_7899["command"] = resetcommandd
    ########################################################################
    ########################################################################


    #HERE COMES THE THIRD TAB DATA

    ########################################################################
    ########################################################################

    GLabel_51666=tk.Label(tab3, anchor = 'w', background='white')
    ft = tkFont.Font(family='Arial Bold',size=10)
    GLabel_51666["font"] = ft
    GLabel_51666["fg"] = "#000000"
    GLabel_51666["text"] = "From Date"
    GLabel_51666.place(x=10,y=50,width=70,height=25)

    GLabel_90111=tk.Label(tab3, anchor = 'w', background='white')
    ft = tkFont.Font(family='Arial Bold',size=10)
    GLabel_90111["font"] = ft
    GLabel_90111["fg"] = "#000000"
    GLabel_90111["justify"] = "left"
    GLabel_90111["text"] = "To Date"
    GLabel_90111.place(x=550,y=50,width=70,height=25)

    GLabel_98444=tk.Label(tab3, anchor = 'w', background='white')
    ft = tkFont.Font(family='Arial Bold',size=10)
    GLabel_98444["font"] = ft
    GLabel_98444["fg"] = "#000000"
    GLabel_98444["justify"] = "left"
    GLabel_98444["text"] = "Result Type"
    GLabel_98444.place(x=10,y=110,width=78,height=25)

    GLabel_3222=tk.Label(tab3, anchor = 'w', background='white')
    ft = tkFont.Font(family='Arial Bold',size=10)
    GLabel_3222["font"] = ft
    GLabel_3222["fg"] = "#000000"
    GLabel_3222["justify"] = "left"
    GLabel_3222["text"] = "Class "
    GLabel_3222.place(x=550,y=110,width=70,height=25)

    fromdateee = tk.StringVar()
    GLineEdit_9777=DateEntry(tab3,locale="en_US", date_pattern="dd/MM/yyyy", textvariable = fromdateee, highlightthickness=1, relief="flat")
    GLineEdit_9777.config(state='readonly')
    GLineEdit_9777.set_date('01/01/2021')
    GLineEdit_9777["borderwidth"] = "1"
    ft = tkFont.Font(family='Arial',size=10)
    GLineEdit_9777["font"] = ft
    GLineEdit_9777["foreground"] = "#000000"
    GLineEdit_9777["justify"] = "left"
    GLineEdit_9777.place(x=96,y=50,width=250,height=30)

    todateee = tk.StringVar()
    GLineEdit_91666=DateEntry(tab3,locale="en_US", date_pattern="dd/MM/yyyy", textvariable = todateee, highlightthickness=1, relief="flat")
    GLineEdit_91666.config(state='readonly')
    GLineEdit_91666.set_date('01/01/2021')
    GLineEdit_91666["borderwidth"] = "1"
    ft = tkFont.Font(family='Arial',size=10)
    GLineEdit_91666["font"] = ft
    GLineEdit_91666["foreground"] = "#000000"
    GLineEdit_91666["justify"] = "left"
    GLineEdit_91666.place(x=650,y=50,width=250,height=30)

    att_typeee = tk.StringVar()
    att_selecttt=ttk.Combobox(tab3,textvariable=att_typeee,state="readonly")
    att_selecttt["values"]=('Select','Present','Absent','Both')
    ft = tkFont.Font(family='Arial',size=10)
    att_selecttt["font"] = ft
    att_selecttt["background"] = "#ffffff"
    att_selecttt["justify"] = "left"
    att_selecttt.place(x=96,y=110,width=250,height=30)

    Scienceee=tk.BooleanVar()
    Commerceee=tk.BooleanVar()
    Humanitiesss=tk.BooleanVar()


    #class selection
    menuuubuttonnn = tk.Menubutton(tab3, width=250,text="Select",background="white",activebackground="white",justify="left",anchor='w', indicatoron=True, borderwidth=1, highlightthickness=2, relief="flat")
    menuuubuttonnn.config(highlightbackground="#333333", highlightcolor= "#333333")
    menuuu = tk.Menu(menuuubuttonnn, tearoff=False)
    menuuubuttonnn.configure(menu=menuuu)
    #menuuubuttonnn.grid(column=0,row=1,padx=10, pady=10)
    menuuubuttonnn.place(x=650,y=110,width=250,height=30)
    choicess = {}
    for choice in ("XII-A","XII-B","XII-C"):
        choicess[choice] = tk.IntVar(value=0)
        if choice=="XII-A":
            menuuu.add_checkbutton(label=choice, variable=Scienceee, onvalue=1, offvalue=0)
        if choice=="XII-B":
            menuuu.add_checkbutton(label=choice, variable=Commerceee, onvalue=1, offvalue=0)
        if choice=="XII-C":
            menuuu.add_checkbutton(label=choice, variable=Humanitiesss, onvalue=1, offvalue=0)
        

    GButton_55999=tk.Button(tab3, borderwidth=1)
    GButton_55999["bg"] = "#efefef"
    ft = tkFont.Font(family='Arial',size=10)
    GButton_55999["font"] = ft
    GButton_55999["fg"] = "#ffffff"
    GButton_55999["bg"] = "#333333"
    GButton_55999["justify"] = "center"
    GButton_55999["text"] = "S U B M I T"
    GButton_55999.place(x=340,y=180,width=120,height=35)
    submitcommanddd = partial(submitcommanddd, fromdateee, todateee, att_typeee, choicess)
    GButton_55999["command"] = submitcommanddd

    GButton_78999=tk.Button(tab3, borderwidth=1, relief="ridge")
    GButton_78999["bg"] = "#efefef"
    ft = tkFont.Font(family='Arial',size=10)
    GButton_78999["font"] = ft
    GButton_78999["fg"] = "#ffffff"
    GButton_78999["bg"] = "#333333"
    GButton_78999["justify"] = "center"
    GButton_78999["text"] = "R E S E T"
    GButton_78999.place(x=510,y=180,width=120,height=35)
    GButton_78999["command"] = resetcommanddd
    ########################################################################
    ########################################################################


    ############################## RESULT TAB ##############################
    tabControl2 = ttk.Notebook(content_frame)
    s2 = ttk.Style()
    s2.configure('Frame2.TFrame', background='white')
    

    tab4 = ttk.Frame(tabControl2,style='Frame2.TFrame')    
    tabControl2.add(tab4,text="RESULTS")
    tabControl2.place(x=30,y=500,width=1270,height=300)
 
    ft2 = tkFont.Font(family='Arial Bold',size=11)
    ttk.Label(tab4, text ="The result based on your query set",font=ft2, background='white', foreground="black").grid(column = 0, row = 0, padx = 10,pady = 10)
    ttk.Label(tab1, text ="Combined Query",font=ft2, background='white', foreground="black").grid(column = 0, row = 0, padx = 10,pady = 10)
    ttk.Label(tab2, text ="Student Query",font=ft2, background='white', foreground="black").grid(column = 0, row = 0, padx = 10,pady = 10)
    ttk.Label(tab3, text ="Teacher Query",font=ft2, background='white', foreground="black").grid(column = 0, row = 0, padx = 10,pady = 10)

    
    
    

    root.mainloop()

#start_viewattendance("Harsh")
