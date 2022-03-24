""" 
Abrir ficheros o archivos
"""

from io import open

archivo_texto = open("C:/Users/Statick/Desktop/workspace/Curso Python Mar 2022/Archivos/archivo.txt", "a")

texto = archivo_texto.write("\nSiempre es una buena ocasión para aprender Python")

archivo_texto.close()

