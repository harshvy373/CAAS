from tkinter import *
from pandastable import Table, TableModel
from tkinter import messagebox

df,final="",""
def copy():
        a=messagebox.askquestion("Copy","Do you want to copy in excel format?")
        if a=="yes":
                final.to_clipboard(excel = True)
        else:
                final.to_clipboard(excel = False) 
        messagebox.showinfo("Copy","Copied to clipboard")
                

def draw_Tableee(dataframe):
        global final
        df=final=dataframe
        root=Tk()
        root.title("Table View")
        root.geometry('600x400+200+100')
        frame = Frame(root) 
        frame.pack(fill=BOTH,expand=1)
        #df = TableModel.getSampleData()
        table = pt = Table(frame, dataframe=df,showtoolbar=False, showstatusbar=False,editable=False, enable_menus=False)
        pt.show()
        button2=Button(frame,text="Copy to Clipboard",command=copy)
        button2["bg"] = "#333333"
        button2["fg"] = "#ffffff"
        button2.grid(row=4,column=1)
        frame.pack()
        root.mainloop()

#draw_Table("d")

