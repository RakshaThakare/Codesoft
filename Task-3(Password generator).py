import random
from tkinter import *
import tkinter

meta = Tk()

meta.title("Password Generator")

meta.geometry("600x600")

Label(meta, font=('bold', 8), text='Generate Password').pack()


length1 = tkinter.IntVar()
length2 = tkinter.IntVar()
length3 = tkinter.IntVar()
length4 = tkinter.IntVar()
length5 = tkinter.IntVar()


def passwordGeneration(n):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_+-*/!#$%^&()'

    password = ''.join(random.sample(characters, n))

    l = Label(meta, text=password, font=('bold', 15)) 
    l.place(x=225, y=65)

def getLength():
    if length1.get() == 6:
        passwordGeneration(6)
    elif length2.get() == 8:
        passwordGeneration(8)
    elif length3.get() == 10:
        passwordGeneration(10)
    elif length4.get() == 12:
        passwordGeneration(12)
    else:
        passwordGeneration(14)

Button(meta, text='Generate Password', font=('bold', 10),bg='green', command=getLength).place(x=230, y=100)

Checkbutton(text='6 character', onvalue=6, offvalue=0,variable=length1).place(x=250, y=150)
Checkbutton(text='8 character', onvalue=8, offvalue=0,variable=length2).place(x=250, y=170)
Checkbutton(text='10 character', onvalue=10, offvalue=0,variable=length3).place(x=250, y=190)
Checkbutton(text='12 character', onvalue=12, offvalue=0,variable=length4).place(x=250, y=210)
Checkbutton(text='14 character', onvalue=14, offvalue=0,variable=length4).place(x=250, y=230)

meta.mainloop()