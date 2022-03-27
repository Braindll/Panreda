from tkinter import *
from tkinter import ttk

def closeWindow():
    window.destroy()

window=Tk()
window.geometry("500x500")


nonebook=ttk.Notebook(window)
nonebook.pack()


tab1=Frame(nonebook,width=500,height=500,background="pink")
tab2=Frame(nonebook,width=500,height=500,background="purple")
tab3=Frame(nonebook,width=500,height=500,background="magenta")
tab4=Frame(nonebook,width=500,height=500,background="aqua")
tab5=Frame(nonebook,width=500,height=500,background="#FFA17F")


tab1.pack(fill="both",expand=1)
tab2.pack(fill="both",expand=1)
tab3.pack(fill="both",expand=1)
tab4.pack(fill="both",expand=1)
tab5.pack(fill="both",expand=1)


nonebook.add(tab1,text="pink")
nonebook.add(tab2,text="purple")
nonebook.add(tab3,text="magenta")
nonebook.add(tab4,text="aqua")
nonebook.add(tab5,text="Yavruağzı")


buton=Button(tab1,text="LaLa Paşa",command=closeWindow)
buton.pack(padx=15,pady=15)

buton2=Button(tab2,text="DaDa Paşa")
buton2.pack(padx=15,pady=15)


buton3=Button(tab3,text="Tosun Paşa")
buton3.pack(padx=15,pady=15)

buton4=Button(tab4,text="Sunrise")
buton4.pack(padx=15,pady=15)

buton5=Button(tab4,text="Sunset")
buton5.pack(padx=15,pady=15)

label=Label(tab4,text="LALA PAŞA")
label.pack()


window.mainloop()