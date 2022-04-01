from tkinter import *
from os import system

arttir=0

def arti():
    global arttir
    arttir+=1
    buton.config(text=arttir)
    if arttir==20:
        window.destroy()

def closeWindow():
    window.destroy()

system("clear")
window=Tk()
window.geometry("800x600")
window.title("Helllooo Beauty")
window.config(background="white")

buton=Button(window,command=arti,width=140,height=70,bitmap='button2.png',borderwidth=0,text=arttir)
buton.pack(padx=15,pady=15)

buton1=Button(window,command=closeWindow,text="LaLa Paşa",width=10,padx=15,pady=15,borderwidth=0)
buton1.pack(padx=15,pady=15)

window.mainloop()
