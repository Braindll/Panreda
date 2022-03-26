from tkinter import *
from tkinter import ttk


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



window.mainloop()