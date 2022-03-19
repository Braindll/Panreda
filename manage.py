from tkinter import *

window=Tk()
window.geometry("800x600")
window.title("Helllooo Beauty")
window.config(background="white")
alper=1

def arti():
    global alper
    alper+=1

buton=Button(window,command=arti,text=alper,width=10,padx=15,pady=15)
buton.pack(padx=15,pady=15)

buton1=Button(window,command=window.destroy,text="LaLa Paşa",width=10,padx=15,pady=15)
buton1.pack(padx=15,pady=15)

while True:
    window.update()
    buton.config(text=alper)
    