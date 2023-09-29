from tkinter import *
from tkinter import messagebox
def fun():
    messagebox.showerror("Error","Enter all information")
top = Tk()
top.geometry("800x700")
top.title("ganesh")
label1= Label(top,text="EXAMINATION FORM",fg="red",font="bold").place(x=320,y=15)
label2= Label(top,text="RASHTRASANT TUKADOJI MAHARAJ NAGPURE UNIVERSITY,NAGPUR ",font="bold").place(x=200,y=40)

label1= Label(top,text="Name of Examination: ").place(x=50,y=70)
entry1= Entry(top).place(x=200,y=70)


label2= Label(top,text="Student Name: ").place(x=50,y=100)
entry1= Entry(top).place(x=200,y=100)

label3= Label(top,text="Session: Winter/Summer ").place(x=50,y=130)
entry3= Entry(top).place(x=200,y=130)

label4= Label(top, text="First Name: ").place(x=50,y=160)
entry4= Entry(top).place(x=200,y=160)

label5= Label(top, text="Middle Name: ").place(x=50,y=190)
entry5= Entry(top).place(x=200,y=190)

label6= Label(top, text="Last Name: ").place(x=50,y=220)
entry6= Entry(top).place(x=200,y=220)

label7= Label(top, text="Mother Name: ").place(x=50,y=250)
entry7= Entry(top).place(x=200,y=250)

label8= Label(top, text="Dath of Birth: ").place(x=400,y=250)
entry8= Entry(top).place(x=500,y=250)

label9= Label(top, text="Category: ").place(x=50,y=280)
entry9= Entry(top).place(x=200,y=280)

label10= Label(top, text="Mobile No.: ").place(x=400,y=280)
entry10= Entry(top).place(x=500,y=280)

label11= Label(top, text="Email ID: ").place(x=50,y=310)
entry11= Entry(top).place(x=200,y=310)

label12= Label(top, text="Subject Applied For: ").place(x=50,y=330)
label13= Label(top, text="Sr. no.: ").place(x=80,y=360)

label4= Label(top, text="Subject Name ").place(x=400,y=360)

label5= Label(top, text="1. ").place(x=80,y=390)
entry16= Entry(top).place(x=400,y=390)

label7= Label(top, text="2. ").place(x=80,y=420)
entry18= Entry(top).place(x=400,y=420)

labe19= Label(top, text="3. ").place(x=80,y=450)
entry20= Entry(top).place(x=400,y=450)

labe21= Label(top, text="4. ").place(x=80,y=480)
entry22= Entry(top).place(x=400,y=480)

labe23= Label(top, text="5. ").place(x=80,y=510)
entry24= Entry(top).place(x=400,y=510)

label25= Label(top, text=" upload Student Signature ").place(x=500,y=540)
entry26= Entry(top).place(x=520,y=570)

button1= Button(top, text="Submit",command=fun ,fg="white",bg="blue").place(x=500,y=615)

button2= Button(top, text="Cancel",command=fun ,fg="white",bg="blue").place(x=585,y=615)


top.mainloop()