import tkinter
#from tkinter import *

ventana = tkinter.Tk()
ventana.geometry("800x600")

boton1 = tkinter.Button(ventana, text="Boton1", height=2, width=2)
boton2 = tkinter.Button(ventana, text="Boton2")
boton3 = tkinter.Button(ventana, text="Boton3")

boton1.grid(row=0, column=0)
boton2.grid(row=0, column=1)
boton3.grid(row=3, column=3)

ventana.mainloop()