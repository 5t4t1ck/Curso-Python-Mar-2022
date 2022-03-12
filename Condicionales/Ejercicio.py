"""Encontrar el mayor de 3 números ingresados por teclado

Caso 1: Si el primero es el mayor
Caso 2: Si el segundo es el mayor
Caso 3: Si el tercero es el mayor
"""

"""Inicio
Paso 1: ingresar los 3 numeros
Paso 2: Comprobar si el 1er número es mayor que 2
Paso 3: Comprobar si el 1er número es mayor que 3
Paso 4: Comprobar si el 2do número es mayor que 1
Paso 5: Comprobar si el 2do número es mayor que 3
Paso 6: Comprobar si el 3er número es mayor que 1
Paso 7: Comprobar si el 3er número es mayor que 2
Fin"""

x = input("Por favor ingrese el primer numero: ")
y = input("Por favor ingrese el segundo numero: ")
z = input("Por favor ingrese el tercer numero: ")

if x > y and x > z:
    print(f"El mayor es {x}, y pertenece al primer numero")
elif y > x and y > z:
    print(f"El mayor es {y}, y pertenece al segundo numero")
elif z > x and z > y:
    print(f"El mayor es {z}, y pertenece al tercer numero")
else:
    print(f"Los valores ingresados: {x}, {y} y {z} son iguales o no son valores enteros")