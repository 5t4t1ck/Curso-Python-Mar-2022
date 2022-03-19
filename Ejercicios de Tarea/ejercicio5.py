
"""Ejercicio 5

Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el 
valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el máximo 
y el mínimo, utilizando la función anterior."""

lista_num = [2, 3, 4, 5, 6]
"""num_max = int(input("Ingrese un valor maximo: "))
num_min = int(input("Ingrese un valor minimo: "))"""

def calcularMaxMin(lista_num):
    
    num_max = 0
    num_min = 1000
    
    for i, dato in enumerate(lista_num):
        num_max = max(num_max, dato)
        num_min = min(num_min, dato)
    print(f"La lista es> {lista_num}")
    print(f"El valor maximo es: {num_max}")
    print(f"El valor minimo es: {num_min}")
    
calcularMaxMin([1,2,3,4,5])
    