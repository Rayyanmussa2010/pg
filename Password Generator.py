# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 16:02:22 2021

@author: DELL
"""

from tkinter import *
import random
root=Tk()

root.title("multidimensional array")

root.geometry("400x400")

array_3d=[[[1, 2, 3, 4, 5, 6],["head", "tail"],["a", "b", "c", "d" "e", "f", "g", "h"]]]
print(array_3d[0][2][3])
label=Label(root)

def generate_password():
    random_number1=random.randint(0, 5)
    random_number2=random.randint(0, 1)
    random_number3=random.randint(0, 7)
    letter1=str(array_3d[0][0][random_number1])
    letter2=str(array_3d[0][1][random_number2])
    letter3=str(array_3d[0][2][random_number3])
    label["text"]=letter1+""+letter2+""+letter3

btn=Button(root,text="New Password",command=generate_password)
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
label.place(relx=0.5, rely=0.4, anchor=CENTER)








root.mainloop()