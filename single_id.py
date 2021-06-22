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

    

#pdf.save()


def singleside_start(data):
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

    
#singleside_start([["Harsh Vardhan Yadav","5999","Student","XII-C","8384098112"]])
