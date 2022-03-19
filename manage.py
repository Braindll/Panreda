import time
import datetime
import os
from tkinter import *
import random


window=Tk()
window.geometry("800x600")
window.title("Helllooo Beauty")
window.config(background="white")

tek=1

def saveMe():
    global tek
    if tek==1:
        ss = ["Mark", "Amber", "Todd", "Anita", "Sandy","Alper","Tektaş","Hulusi","Desa","Guldan"]
        a=random.randint(0, 9)
        btn1.config(text=ss[a])
        btn1.after(100,saveMe)
        tek=0
    elif tek==0:
        tek=1
        pass



btn1=Button(window ,text="LoLa",command=saveMe,foreground="purple")
btn1.pack(padx=10,pady=10)

window.mainloop()