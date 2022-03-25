"""4. El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:

El usuario proporcionará un valor entre 0 y 10.

Si está entre 9 y 10: imprimir una A
Si está entre 8 y menor a 9: imprimir una B
Si está entre 7 y menor a 8: imprimir una C
Si está entre 6 y menor a 7: imprimir una D
Si está entre 0 y menor a 6: imprimir una F

Cualquier otro valor debe imprimir: Valor desconocido

Por ejemplo:

    Proporciona un valor entre 0 y 10:
    A"""

num = int(input("Por favor ingrese un valor de calificación de 0 a 10: "))

if num >= 9 and num <= 10:
    print(f" Su nota es: {num} que equivale a A")
elif num >= 8 and num < 9:
    print(f" Su nota es: {num} que equivale a B")
elif num >= 7 and num < 8:
    print(f" Su nota es: {num} que equivale a C")
elif num >= 6 and num < 7:
    print(f" Su nota es: {num} que equivale a D")
elif num >= 0 and num < 6:
    print(f" Su nota es: {num} que equivale a F")
else:
    print("Valor Desconocido")