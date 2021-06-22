from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from PIL import ImageTk, Image
import time as t
start_time = t.time()
from datetime import *
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import cv2
import os
import pyzbar.pyzbar as pyzbar
import warnings
warnings.filterwarnings("ignore")
from db_class import *
from pydub import AudioSegment
from pydub.playback import play
from image_class import *

qrcount=0
a=True
b=True
cap=""
font=""
color="#28383c"
#color="#5f6b6d"


welcome_msg="";

from admin import *
from admin_generateids import *
from admin_impexp import *
from admin_viewattendance import *
from forgot import *

root,gtx_name="",""

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
            forgot()
        except:
            root.destroy()
            admin_start()        
        root.destroy()
        admin_start()
    
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


cap = cv2.VideoCapture(0)
vs = cv2.VideoCapture(0)
#cap2 = VideoStream(src=0).start()
cap2=cv2.VideoCapture(0)
lmain=""
gmain=""
step1_info1=""
step2_info2=""
first_capture=""
second_capture=""
g_name,g_admno,g_class,g_type="","","",""

args=[]
entry_count=0
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--face", type=str,
        default="face_detector",
        help="path to face detector model directory")
ap.add_argument("-m", "--model", type=str,
        default="mask_detector.model",
        help="path to trained face mask detector model")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
        help="minimum probability to filter weak detections")
args = vars(ap.parse_args())


prototxtPath = os.path.sep.join([args["face"], "deploy.prototxt"])
weightsPath = os.path.sep.join([args["face"],
        "res10_300x300_ssd_iter_140000.caffemodel"])
faceNet = cv2.dnn.readNet(prototxtPath, weightsPath)

maskNet = load_model(args["model"])
content_frame=""


def admin_takeat(name):
    global root,gtx_name
    global lmain,gmain,cap,cap2,step1_info1,content_frame,first_capture,second_capture
    gtx_name=name
    root = Tk()
    root.geometry("300x200")
    root.attributes("-fullscreen", True)
    welcome_msg="Hello "+name+" | Take Attendance"

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

    step1_label=tk.Label(content_frame,font=('Arial',11))
    step1_label["bg"] = "#333333"
    step1_label["fg"] = "#ffffff"
    step1_label["text"] = "Step 1 - QR Code"
    step1_label.place(x=50,y=200,width=600,height=25)
    
    lmain=tk.Label(content_frame,text=gtx_name,borderwidth=2, relief="solid")
    lmain.place(x=50,y=225,width=600)

    step1_info1=tk.Label(content_frame,font=('Courier',11,'bold'))
    step1_info1["bg"] = "#DCDCDC"
    step1_info1["fg"] = "red"
    step1_info1["text"] = ""
    step1_info1.place(x=50,y=709,width=600,height=50)


    step2_label=tk.Label(content_frame,font=('Arial',11))
    step2_label["bg"] = "#333333"
    step2_label["fg"] = "#ffffff"
    step2_label["text"] = "Step 2 - Face Detection"
    step2_label.place(x=700,y=200,width=600,height=25)

    gmain=tk.Label(content_frame,text="Wait for Step 1", borderwidth=2, relief="solid")
    gmain.place(x=700,y=225,width=600)
    
    
    _, frame = cap.read()
    font = cv2.FONT_HERSHEY_PLAIN
    im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    decodedObjects = pyzbar.decode(im)     
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)

    cont="True"
    for obj in decodedObjects:
        data=obj.data.decode('utf-8')
        cont="False"
        qr_match(data)
        
    if cont=="False":
        cap.release()
        first_capture = encodeFrame(frame)
        print(first_capture)
        #encodeImage(cv2image)
    else:
        lmain.after(1, scann_qr)

    root.mainloop() 


def start_detect():
    global step2_info2,second_capture
    step2_info2=tk.Label(content_frame,font=('Courier',11,'bold'))
    step2_info2["bg"] = "#DCDCDC"
    step2_info2["fg"] = "red"
    step2_info2["text"] = "No Mask Detected"
    step2_info2.place(x=700,y=709,width=600,height=50)
    
    _, second_frame = vs.read()
    #font = cv2.FONT_HERSHEY_PLAIN
    t.sleep(2)
    cv2imagee = cv2.cvtColor(second_frame, cv2.COLOR_BGR2RGBA)
    (locs, preds) = detect_and_predict_mask(second_frame, faceNet, maskNet)
    imgg = Image.fromarray(cv2imagee)
    imgtkk = ImageTk.PhotoImage(image=imgg)
    gmain.imgtk = imgtkk
    gmain.configure(image=imgtkk)
    cont_command=True
    for (box, pred) in zip(locs, preds):
        print("Here")
        (startX, startY, endX, endY) = box
        (mask, withoutMask) = pred

        label = "Mask" if mask > withoutMask else "No Mask"
        color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
        if mask > withoutMask:
            step2_info2["fg"] = "green"
            step2_info2["text"] = "Mask Detected"
            
            vs.release()
            second_capture = encodeFrame(second_frame)
            print(second_capture)
            record()
            reverse()
            cont_command=False
        else:
            step2_info2["fg"] = "red"
            step2_info2["text"] = "No Mask Detected"
            
            #cont=True

        label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

        cv2.putText(second_frame, label, (startX, startY - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
        cv2.rectangle(second_frame, (startX, startY), (endX, endY), color, 2)

    #gmain.after(1, repeat)
    if cont_command==True:
        gmain.after(1, repeat)
    #root.mainloop()

def record():
    today=date.today().strftime("%d/%m/%Y")
    time_curr=datetime.now()
    q="select * from attendance where id='"+g_admno+"' and date='"+str(today)+"';"
    s=find(q)
    if s==0:
        query="insert into attendance values ('"+g_admno+"', '"+g_name+"', '"+str(today)+"', '"+str(time_curr)+"', '"+g_class+"', '"+g_type+"');"
        insert(query)

def reverse():
    global cap
    print("reverse function")
    cap = cv2.VideoCapture(0)
    step1_info1["text"]=""
    step2_info2["text"]=""
    """step2_info2["bg"]="white"
    step2_info2["fg"]="white"""
    scann_qr()

def repeat():
    global step2_info2,second_capture
    _, second_frame = vs.read()
    (locs, preds) = detect_and_predict_mask(second_frame, faceNet, maskNet)
    font = cv2.FONT_HERSHEY_PLAIN
    t.sleep(0)
    imgg = cv2.cvtColor(second_frame, cv2.COLOR_BGR2GRAY)
    cv2imagee = cv2.cvtColor(second_frame, cv2.COLOR_BGR2RGBA)
    imgg = Image.fromarray(cv2imagee)
    imgtkk = ImageTk.PhotoImage(image=imgg)
    gmain.imgtk = imgtkk
    gmain.configure(image=imgtkk)
    
    cont_command=True
    for (box, pred) in zip(locs, preds):
        (startX, startY, endX, endY) = box
        (mask, withoutMask) = pred
        label = "Mask" if mask > withoutMask else "No Mask"
        color = (0, 255, 0) if label == "Mask" else (0, 0, 255)
        if mask > withoutMask:
            step2_info2["fg"] = "green"
            step2_info2["text"] = "Mask Detected"
            
            vs.release()
            second_capture = encodeFrame(second_frame)
            print(second_capture)
            record()
            reverse()
            cont_command=False
        else:
            step2_info2["fg"] = "red"
            step2_info2["text"] = "No Mask Detected"
            
            #cont=True
        label = "{}: {:.2f}%".format(label, max(mask, withoutMask) * 100)

        cv2.putText(second_frame, label, (startX, startY - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 2)
        cv2.rectangle(second_frame, (startX, startY), (endX, endY), color, 2)

    if cont_command==True:
        gmain.after(1, repeat)
        
def video_stream():
    _, framee = cap2.read()
    cv2imagee = cv2.cvtColor(framee, cv2.COLOR_BGR2RGBA)
    imgg = Image.fromarray(cv2imagee)
    imgtkk = ImageTk.PhotoImage(image=imgg)
    gmain.imgtk = imgtkk
    gmain.configure(image=imgtkk)
    gmain.after(1, video_stream)

def qr_match(d):
    global g_name,g_admno,g_class,g_type,vs
    print("In QR Match")
    q="select name,id,class,type from people where id='"+d+"';"
    s=select(q)
    try:
        value="Name : "+s[0]+" | Admno : "+s[1]+" | Class : "+s[2]
        step1_info1["fg"] = "green"
        step1_info1["text"]=value        
        g_name,g_admno,g_class,g_type=s[0],s[1],s[2],s[3]
        try:
            start_detect()
        except:
            vs = cv2.VideoCapture(0)
            start_detect()
        #play(AudioSegment.from_wav("goodies/found.wav"))
        #start_facemaskdetect(d)
    except :
        play(AudioSegment.from_wav("goodies/notfound.wav"))
        scann_qr()

def detect_and_predict_mask(frame, faceNet, maskNet):
    (h, w) = frame.shape[:2]
    #print(np.asarray(frame).shape[:3])
    blob = cv2.dnn.blobFromImage(frame, 1.0, (300, 300),(104.0, 177.0, 123.0))

    faceNet.setInput(blob)
    detections = faceNet.forward()

    faces = []
    locs = []
    preds = []

    for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            if confidence > args["confidence"]:
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")

                    (startX, startY) = (max(0, startX), max(0, startY))
                    (endX, endY) = (min(w - 1, endX), min(h - 1, endY))

                    face = frame[startY:endY, startX:endX]
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
                    face = cv2.resize(face, (224, 224))
                    face = img_to_array(face)
                    face = preprocess_input(face)

                    faces.append(face)
                    locs.append((startX, startY, endX, endY))

    if len(faces) > 0:
            faces = np.array(faces, dtype="float32")
            preds = maskNet.predict(faces, batch_size=32)

    return (locs, preds)


def scann_qr():
    global first_capture,cap
    _, frame = cap.read()
    font = cv2.FONT_HERSHEY_PLAIN
    try:
        im = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    except:
        cap = cv2.VideoCapture(0)
        scann_qr()
    decodedObjects = pyzbar.decode(im)     
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)

    cont="True"
    for obj in decodedObjects:
        data=obj.data.decode('utf-8')
        cont="False"
        qr_match(data)
        
    if cont=="False":
        cap.release()
        first_capture = encodeFrame(frame)
        print(first_capture)
        #encodeImage(cv2image)
        
    else:
        lmain.after(1, scann_qr)

#admin_takeat("admin")

