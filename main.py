import tkinter as tkr
from tkinter import simpledialog
import FUNCIONESS as fun 
from FUNCIONESS import mayoria_de_edad2, mayoria_de_edad

base = tkr.Tk()
base.title("djfngdher")

nombre= simpledialog.askstring("nombre", "digite su nombre:")
edad= simpledialog.askstring("edad", "digite su edad:")
RR=fun.mayoria_de_edad(nom,ed)
usar_label = tkr.Label.base,text=mayoria_de_edad(nom,ed),font=
usar_label.pack(pady=30)

base.mainloop()

