""" 
Crear ficheros o archivos
"""

from io import open

archivo_texto = open("C:/Users/Statick/Desktop/workspace/Curso Python Mar 2022/Archivos/archivo.txt", "w")

frase = "Esto es un texto diferente al que se escribio anteriormente"

archivo_texto.write(frase)

archivo_texto.close()