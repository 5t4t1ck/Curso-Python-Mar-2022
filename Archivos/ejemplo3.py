""" 
Leer ficheros o archivos
"""

from io import open

archivo_texto = open("C:/Users/Statick/Desktop/workspace/Curso Python Mar 2022/Archivos/archivo.txt", "r")

texto = archivo_texto.readlines()

archivo_texto.close()

print(texto)