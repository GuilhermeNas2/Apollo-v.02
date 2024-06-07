from tkinter import * 
from tkinter import ttk 


root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Bem vindo ao Apollo").grid(column=0,row=0)
ttk.Label(frm, text="Cliente").grid(column=0, row=1)
ttk.Entry(frm).grid(column=1, row=1)
root.mainloop()
