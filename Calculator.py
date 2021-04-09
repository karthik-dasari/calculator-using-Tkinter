from tkinter import *
import cmath

root=Tk()
root.iconbitmap('cal.ico')
root.title('Calculator')

def button_clicked(number):
    current_number=text_box.get()
    text_box.delete(0,END)
    text_box.insert(0,str(current_number)+str(number))

def Root():
    current_number=text_box.get()
    text_box.delete(0,END)
    r=cmath.sqrt(int(current_number))
    text_box.insert(0,r)

def square():
    current_number=text_box.get()
    text_box.delete(0,END)
    s=int(current_number) ** 2
    text_box.insert(0,s)

def clear():
    text_box.delete(0,END)

def equal():
    current_number=text_box.get()
    text_box.delete(0,END)
    text_box.insert(0,eval(current_number))

text_box = Entry(root,width=40,borderwidth=5)
text_box.grid(row=0,column=0,columnspan=3,ipady=18)

button_1=Button(root,text="1",padx=40,pady=20,command=lambda : button_clicked(1))
button_2=Button(root,text="2",padx=40,pady=20,command=lambda : button_clicked(2))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda : button_clicked(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda : button_clicked(4))
button_5=Button(root,text="5",padx=40,pady=20,command=lambda : button_clicked(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda : button_clicked(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda : button_clicked(7))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda : button_clicked(8))
button_9=Button(root,text="9",padx=40,pady=20,command=lambda : button_clicked(9))
button_0=Button(root,text="0",padx=40,pady=20,command=lambda : button_clicked(0))
button_add=Button(root,text="+",padx=40,pady=20,command=lambda : button_clicked("+"))
button_sub=Button(root,text="-",padx=40,pady=20,command=lambda : button_clicked("-"))
button_mul=Button(root,text="*",padx=40,pady=20,command=lambda : button_clicked("*"))
button_div=Button(root,text="/",padx=40,pady=20,command=lambda : button_clicked("/"))
button_clr=Button(root,text="Clear",padx=29.5,pady=20,command=clear)
button_eql=Button(root,text="=",padx=38,pady=20,command=equal)
button_root=Button(root,text="Root",padx=30,pady=20,command=Root)
button_square=Button(root,text="Sq",padx=40,pady=20,command=square)

button_1.grid(row=1,column=0)
button_2.grid(row=1,column=1)
button_3.grid(row=1,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=3,column=0)
button_8.grid(row=3,column=1)
button_9.grid(row=3,column=2)

button_0.grid(row=4,column=0)
button_add.grid(row=4,column=1)
button_sub.grid(row=4,column=2)

button_mul.grid(row=5,column=0)
button_div.grid(row=5,column=1)
button_clr.grid(row=5,column=2)

button_eql.grid(row=6,column=2)
button_root.grid(row=6,column=0)
button_square.grid(row=6,column=1)

root.mainloop()