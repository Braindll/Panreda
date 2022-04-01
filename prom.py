from tkinter import *
from tkinter import ttk
import threading
from os import system
from time import sleep
system("clear")
osk=0
def kapa():
    root.destroy()

def artti():
    global osk
    osk+=1

def updatew():
    bot2.config(text=osk)
    bot2.after(1,updatew)

def bekle():
    print("bekleme")
    sleep(5)
    print("bitti")
def thre():
    threading.Thread(target=bekle).start()


root=Tk()
root.geometry("500x500")
root.title("Hello Threat")

bot=Button(root,text="kapa",command=kapa)
bot.pack()

bot2=Button(root,text=osk,command=artti)
bot2.pack()

bot3=Button(root,text="Bekle",command=thre)
bot3.pack()

threading.Thread(target=updatew).start()
mainloop()

