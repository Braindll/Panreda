from tkinter import *
from tkinter import ttk

window=Tk()
window.geometry("500x500")

nonebook=ttk.Notebook(window)
nonebook.pack()



tab1=Frame(nonebook,width=500,height=500,background="pink")
tab2=Frame(nonebook,width=500,height=500,background="purple")
tab3=Frame(nonebook,width=500,height=500,background="magenta")

tab1.pack(fill="both",expand=1)
tab2.pack(fill="both",expand=1)
tab3.pack(fill="both",expand=1)

nonebook.add(tab1,text="pink")
nonebook.add(tab2,text="purple")
nonebook.add(tab3,text="magenta")




window.mainloop()