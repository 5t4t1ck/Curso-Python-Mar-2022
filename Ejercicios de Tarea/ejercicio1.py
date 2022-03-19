"""
1) Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
Mostrar una suma de los dos números
Mostrar una resta de los dos números (el primero menos el segundo)
Mostrar una multiplicación de los dos números
En caso de no introducir una opción inválida, el programa informará de que no es correcta.
"""

print("Operaciones con 2 numeros \n")

num1 = int(input("Introduzca el primer numero: "))
num2 = int(input("Introduzca el segundo numero: "))

while True:
    
    print("\n Que operacione desea realizar \n")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicacion")
    print("4) Division")
    print("5) Salir")
    
    operacion = int(input("Elige un numero del 1 al 5: "))
    
    if operacion == 1:
        print("La suma de ", num1, "+", num2, "=", num1+num2)
        
    elif operacion == 2:
        print("La resta de", num1, "-", num2, "=", num1+num2)
    
    else:
        break