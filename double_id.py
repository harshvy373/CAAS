from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import pyqrcode 
import png 
from pyqrcode import QRCode
import qrcode
from tkinter import messagebox,filedialog

def draw(pdf,name,id_no,position,clss,phn_no,status):
    image = 'goodies/page1.png'
    schl_name="REMAL PUBLIC SR. SEC. SCHOOL"
    add="Pocket A-2, Sector-3, Rohini, New Delhi"
    pdf.drawImage(image,0,0)


    pdf.setFillColor("red")
    pdf.setFont("Helvetica-Bold", 22)
    pdf.drawCentredString(300, 770, schl_name)
    pdf.setFillColor("black")
    pdf.setFont("Helvetica", 18)
    pdf.drawCentredString(300, 745, add)
    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawCentredString(300, 300, name.upper())
    pdf.setFont("Helvetica", 22)
    pdf.drawCentredString(300, 260, status.upper())
    pdf.setFillColor("red")
    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawCentredString(300, 130, "ID No : "+id_no)



    qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=1)
    qr.add_data(id_no)
    qr.make(fit=False)
    img = qr.make_image(fill='black', back_color='white')
    img.save('myqr.png')
    pdf.drawImage("myqr.png",179,427)
    pdf.showPage()
    pdf.drawImage("goodies/page2.png",0,0)
    #drawMyRuler(pdf)


    #pdf.drawImage("logo2.png",300,200)
    pdf.setFillColor("red")
    pdf.setFont("Helvetica-Bold", 22)
    pdf.drawCentredString(300, 250, schl_name)
    pdf.setFillColor("black")
    pdf.setFont("Helvetica", 18)
    pdf.drawCentredString(300, 225, add)
    pdf.setFont("Helvetica", 16)
    pdf.drawCentredString(300, 200, "Phone : 011-47512024,29 Email : remalps@yahoo.com")

    pdf.setFont("Helvetica-Oblique", 14)
    pdf.drawString(103, 120, "T&C")
    pdf.drawString(103, 85, "1. This is school property and must be kept safely by the holder")
    pdf.drawString(103, 65, "2. In case of loss or damage, report immediately to the authority")


    pdf.line(120, 700, 470, 700)
    pdf.setFillColor("red")
    pdf.setFont("Helvetica", 18)
    pdf.drawString(120, 720, "Phone No")
    pdf.setFillColor("black")
    pdf.drawString(300, 720, phn_no)

    pdf.line(120, 640, 470, 640)
    pdf.setFillColor("red")
    pdf.setFont("Helvetica", 18)
    pdf.drawString(120, 660, "Address")
    pdf.setFillColor("black")
    pdf.drawString(300, 660, "354A POCKET D6 S")
    pdf.drawString(120, 600, "ECTOR - 6 ROHINI NEW DELHI - 110085")
    pdf.line(120, 580, 470, 580)

#pdf.save()


def doubleside_start(data):
    fileName = filedialog.asksaveasfilename(defaultextension='.pdf')

    pdf = canvas.Canvas(fileName)
    pdf.setTitle("CAAS | ID Card")
    
    for i in data:
        name=i[0]
        id_no=i[1]
        position=i[2]
        clss=i[3]
        phn_no=i[4]
        status=position+" ("+clss+")"
        
        draw(pdf,name,id_no,position,clss,phn_no,status)
        pdf.showPage()
    pdf.save()
    messagebox.showinfo("Export","PDF exported successfully")

    """
    name="Harsh Vardhan Yadav"
    id_no="5999"
    position="Student"
    clss="XII-C"
    phn_no="8384098112"
    status=position+" ("+clss+")"
    """

    
#doubleside_start([["Harsh Vardhan Yadav","5999","Student","XII-C","8384098112"]])
