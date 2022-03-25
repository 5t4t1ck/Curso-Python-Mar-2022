"""11. Crear una función para multiplicar los valores recibidos de tipo numérico, 
utilizando argumentos variables *args como parámetro de la función y regresar 
como resultado la multiplicación de todos los valores pasados como argumentos."""

def multiplicarValores(*args):
    multiplicar = 1
    for i in args:
        multiplicar = multiplicar * i
        print(multiplicar)

print(multiplicarValores(1,2,3,4, 5, 9))
print(multiplicarValores(1,5,3,9))
print(multiplicarValores(1,3,3,100))
print(multiplicarValores(1,2,4,4))
print(multiplicarValores(1,0))