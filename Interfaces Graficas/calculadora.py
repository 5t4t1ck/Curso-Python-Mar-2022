"""Crear una calculadora sencilla con tkinter"""
#from tkinter import *
import tkinter
ventana = tkinter.Tk()
ventana.geometry("800x600")

# Caja de texto
cajaDeTexto = tkinter.Entry(ventana)
cajaDeTexto.grid(row=0,column=0, columnspan=4, padx=5, pady=5)

# Botones
boton1 = tkinter.Button(ventana, text="1", width=10, height=5)
boton2 = tkinter.Button(ventana, text="2", width=10, height=5)
boton3 = tkinter.Button(ventana, text="3", width=10, height=5)
boton4 = tkinter.Button(ventana, text="4", width=10, height=5)
boton5 = tkinter.Button(ventana, text="5", width=10, height=5)
boton6 = tkinter.Button(ventana, text="6", width=10, height=5)
boton7 = tkinter.Button(ventana, text="7", width=10, height=5)
boton8 = tkinter.Button(ventana, text="8", width=10, height=5)
boton9 = tkinter.Button(ventana, text="9", width=10, height=5)
boton0 = tkinter.Button(ventana, text="0", width=10, height=5)

boton_suma = tkinter.Button(ventana, text="+", width=10, height=5)
boton_resta = tkinter.Button(ventana, text="-", width=10, height=5)
boton_division = tkinter.Button(ventana, text="/", width=10, height=5)
boton_multiplicacion = tkinter.Button(ventana, text="*", width=10, height=5)

boton_borrar = tkinter.Button(ventana, text="AC", width=10, height=5)
boton_igual = tkinter.Button(ventana, text="=", width=10, height=5)
boton_punto = tkinter.Button(ventana, text=".", width=10, height=5)

boton_parentesis_1 = tkinter.Button(ventana, text="(", width=10, height=5)
boton_parentesis_2 = tkinter.Button(ventana, text=")", width=10, height=5)
#Posicion de cada boton

boton1.grid(row=4, column=1)
boton2.grid(row=4, column=2)
boton3.grid(row=4, column=3)
boton4.grid(row=3, column=1)
boton5.grid(row=3, column=2)
boton6.grid(row=3, column=3)
boton7.grid(row=2, column=1)
boton8.grid(row=2, column=2)
boton9.grid(row=2, column=3)
boton0.grid(row=5, column=2)

boton_suma.grid(row=4, column=4)
boton_resta.grid(row=3, column=4)
boton_multiplicacion.grid(row=2, column=4)
boton_division.grid(row=1, column=4)

boton_punto.grid(row=5, column=3)
boton_igual.grid(row=5, column=4)
boton_borrar.grid(row=1, column=3)

boton_parentesis_1.grid(row=1, column=1)
boton_parentesis_2.grid(row=1, column=2)

ventana.mainloop()