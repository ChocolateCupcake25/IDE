# -*- coding: utf-8 -*-
"""
Created on Sun May 29 09:00:27 2022

@author: HP
"""

from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import os

root=Tk()
root.minsize(650,650)
root.maxsize(650,650)

Open=ImageTk.PhotoImage(Image.open("open.png"))
Save=ImageTk.PhotoImage(Image.open("save.png"))
Exit=ImageTk.PhotoImage(Image.open("exit.jpg"))

label_file_name=Label(root,text="file name")
label_file_name.place(relx=0.28,rely=0.03,anchor=CENTER)

input_file_name=Entry(root)
input_file_name.place(relx=0.46,rely=0.03,anchor=CENTER)

my_text=Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.55,anchor=CENTER)

name=""
def openfile():
    global name
    my_text.delete(1.0,END)
    input_file_name.delete(0,END)
    text_file= filedialog.askopenfilename(title="Open Text file",filetypes=(("Text Files","*.text"),))
    print(text_file)  
    name=os.path.basename(text_file)
    formated_name=name.split('.')[0]
    input_file_name.insert(END,formated_name)
    root.title(formated_name)
    text_file=open(name,'r')
    paragraph=text_file.read()
    my_text.insert(END,paragraph)
    text_file.close()
    
                                              
open_button=Button(root,image=Open,command=openfile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)

root.mainloop()









