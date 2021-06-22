import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import os
import warnings
warnings.filterwarnings("ignore")
from db_class import *
from pydub import AudioSegment
from pydub.playback import play
from detect_mask_video import *

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
qrcount=0
a=True

#print(conn)

def scan_qr():
    global a,qrcount
    cv2.startWindowThread()
    while a==True:    
        _, frame = cap.read()
        decodedObjects = pyzbar.decode(frame)
        #print(len(decodedObjects))
        cv2.imshow("QR Code", frame)
        if len(decodedObjects)==1 and qrcount==0:
            for o in range (1,2):
                qrcount=1
                data=decodedObjects[o-1].data
                data=data.decode('utf-8')
                #print(data)
                #cv2.putText(frame, str(data), (50, 50), font, 2,(255, 0, 0), 3)
                qr_match(data)
                a=False
                cv2.destroyWindow("QR Code")
                cap.release()
        
        key = cv2.waitKey(1)
        
        if key == 27:
            a=False
            cv2.destroyWindow("QR Code")
            cap.release()

def qr_match(d):
    global a, qrcount
    print(d)
    q="select * from students where admno='"+d+"';"
    s=find(q)
    if s==1:
        a=False
        cv2.destroyWindow("QR Code")
        cap.release()
        play(AudioSegment.from_wav("found.wav"))
        #scan_qr()
        start_detect(d)
    else:
        play(AudioSegment.from_wav("notfound.wav"))
        a=True
        qrcount=0
        scan_qr()
#scan_qr()

