"""Multiplicar 2 numeros sin usar el simbolo de la multiplicacion"""

a = int(input("Por favor ingrese un valor numérico: "))
b = int(input("Por favor ingrese un segundo valor numérico: "))
resultado = 0

for x in range(a):
    resultado = resultado + b
    #resultado += b
print(resultado)