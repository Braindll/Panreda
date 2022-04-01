import datetime
from tkinter import *
from time import *

now = datetime.datetime.now()
target = datetime.datetime(2022, 6,17)
tar=target-now
ayla=Tk()
ayla.geometry("800x600")
ayla.title("Şafak Emeklilik")
ayla.config(background="pink")

def kalan():
    now = datetime.datetime.today().replace(microsecond=0)
    target = datetime.datetime(2022, 6,17)
    sonuc=str(target-now)
    sonuc = sonuc.replace("days", "Gün")
    ex.config(text=sonuc)
    ex.after(100,kalan)

def kalan2():
    suan=int(time())
    hedef=1655413253
    kalanson=str(round(((hedef-suan)/60)))+" Dakika Kaldı"
    saat.config(text=kalanson)
    saat.after(100,kalan2)
    
ex=Label(ayla,text=tar,font="calibri 100",foreground="purple",background="pink")
ex.pack(pady=100)
saat=Label(ayla,text="saat",font="calibri 50",foreground="purple",background="pink")
saat.pack()
kalan()
kalan2()
ayla.mainloop()