# -*- coding: utf-8 -*-
"""
Created on Sun May 29 09:53:01 2022

@author: HP
"""

from tkinter import*
from PIL import ImageTk, Image

root=Tk()
root.minsize(650,650)
root.maxsize(650,650)

Run_img=ImageTk.PhotoImage(Image.open("run.jpg"))
Open_img=ImageTk.PhotoImage(Image.open("open.png"))
Save_img=ImageTk.PhotoImage(Image.open("save.png"))

label_image_file=Label(root,text="image file")
label_image_file.place(relx=0.28,rely=0.03,anchor=CENTER)

input_image_file=Entry(root)
input_image_file.place(relx=0.46,rely=0.03,anchor=CENTER)

my_text=Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)

open_button=Button(root,image=Open_img,command=open_file)
open_button.place(relx=0.05,rely=0.03)

root.mainloop()






