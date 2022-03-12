""" 
Ebercicio1: Imprimir en pantalla los números pares del 1 al 500
Ebercicio2: Imprimir en pantalla los números primos del 1 al 100
"""
"""for num in range(1,500):
    if num % 2 == 0:
        print(num)"""

contador = 1
limite = 100
for a in range(1, limite+1):
    c = 0
    for b in range(1, contador+1):
        a = contador % b
        if a == 0:
            c = c + 1
    if c == 2:
        print(contador)
    else:
        a = a - 1
    contador += 1
            
