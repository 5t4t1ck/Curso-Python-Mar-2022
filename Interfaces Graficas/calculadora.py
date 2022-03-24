"""Crear una calculadora sencilla con tkinter"""
from tkinter import *
import tkinter

ventana = tkinter.Tk()
ventana.title("Calculadora")
#ventana.configure(background="SkyBlue4")
#ventana.geometry("800x600")

# Caja de texto
cajaDeTexto = tkinter.Entry(ventana, font="Calibri 20", justify=RIGHT)
cajaDeTexto.grid(row=0,column=0, columnspan=4, padx=5, pady=5)

#Funciones

i = 0
def click_boton(valor):
    """Poner números"""
    global i
    cajaDeTexto.insert(i, valor)
    i += 1

def borrar():
    """botón borrar"""
    cajaDeTexto.delete(0, END)
    i=0

def igual():
    """botón igual"""
    ecuacion = cajaDeTexto.get()
    resultado = eval(ecuacion)
    cajaDeTexto.delete(0, END)
    cajaDeTexto.insert(0, resultado)
    i=0

def backspace():
    """delete char"""
    input_len = len(cajaDeTexto.get())
    cajaDeTexto.delete(input_len - 1)

# Botones
boton1 = tkinter.Button(ventana, text="1", width=5, height=2, command=lambda: click_boton(1))
boton2 = tkinter.Button(ventana, text="2", width=5, height=2, command=lambda: click_boton(2))
boton3 = tkinter.Button(ventana, text="3", width=5, height=2, command=lambda: click_boton(3))
boton4 = tkinter.Button(ventana, text="4", width=5, height=2, command=lambda: click_boton(4))
boton5 = tkinter.Button(ventana, text="5", width=5, height=2, command=lambda: click_boton(5))
boton6 = tkinter.Button(ventana, text="6", width=5, height=2, command=lambda: click_boton(6))
boton7 = tkinter.Button(ventana, text="7", width=5, height=2, command=lambda: click_boton(7))
boton8 = tkinter.Button(ventana, text="8", width=5, height=2, command=lambda: click_boton(8))
boton9 = tkinter.Button(ventana, text="9", width=5, height=2, command=lambda: click_boton(9))
boton0 = tkinter.Button(ventana, text="0", width=5, height=2, command=lambda: click_boton(0))

boton_suma = tkinter.Button(ventana, text="+", width=5, height=2, command=lambda: click_boton("+"))
boton_resta = tkinter.Button(ventana, text="-", width=5, height=2, command=lambda: click_boton("-"))
boton_multiplicacion = tkinter.Button(ventana, text="*", width=5, height=2, command=lambda: click_boton("*"))
boton_division = tkinter.Button(ventana, text="/", width=5, height=2, command=lambda: click_boton("/"))

boton_borrar = tkinter.Button(ventana, text="AC", width=5, height=2, command=lambda: borrar())
boton_igual = tkinter.Button(ventana, text="=", width=5, height=2, command=lambda: igual())
boton_punto = tkinter.Button(ventana, text=".", width=5, height=2, command=lambda: click_boton("."))
boton_retroceso = tkinter.Button(ventana, text="<-", width=5, height=2, command=lambda: backspace())

boton_parentesis_1 = tkinter.Button(ventana, text="(", width=5, height=2, command=lambda: click_boton("("))
boton_parentesis_2 = tkinter.Button(ventana, text=")", width=5, height=2, command=lambda: click_boton(")"))

#Posicion de cada boton
boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)

boton0.grid(row=5, column=0, padx=5, pady=5)

boton_suma.grid(row=4, column=4, padx=5, pady=5)
boton_resta.grid(row=3, column=4, padx=5, pady=5)
boton_multiplicacion.grid(row=2, column=4, padx=5, pady=5)
boton_division.grid(row=1, column=4, padx=5, pady=5)

boton_punto.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=4, padx=5, pady=5)
boton_retroceso.grid(row=5, column=1, padx=5, pady=5)
boton_borrar.grid(row=1, column=2, padx=5, pady=5)

boton_parentesis_1.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis_2.grid(row=1, column=1, padx=5, pady=5)

ventana.mainloop()