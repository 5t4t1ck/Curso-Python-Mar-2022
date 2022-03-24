import os

if os.path.exists("C:/Users/Statick/Desktop/workspace/Curso Python Mar 2022/Archivos/micarpeta"):
    os.rmdir("C:/Users/Statick/Desktop/workspace/Curso Python Mar 2022/Archivos/micarpeta")
else:
    print("El directorio no existe")