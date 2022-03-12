"""Ejemplos con if, elif y else"""

"""Una persona necesita ingresar por teclado 1 valor numerico, este valor necesita comprobar lo siguiente:
    
    Caso 1: Si este valor es positivo.
    Caso 2: Si este valor es negativo.
    Caso 3: Si este valor es 0"""
    
numero = int(input("Por favor ingrese un valor numerico: "))
#print(f"Me alegro de conocerle, {nombre}")

# -2, -1, 0, 1, 2, 3, 4, 5, ...
#print(type(numero))
if numero > 0:
    print("Es un valor positivo")
elif numero < 0:
    print("Es un valor negativo")
else:
    print("El valor es 0")