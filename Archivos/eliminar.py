import os

if os.path.exists("C:/Users/Statick/Desktop/workspace/Curso Python Mar 2022/Archivos/archivo.txt"):
    print("El archivo existe")
    os.remove("C:/Users/Statick/Desktop/workspace/Curso Python Mar 2022/Archivos/archivo.txt")
else:
    print("El archivo no existe")