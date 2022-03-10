"""Ejemplos de Listas"""

compras = ["manzanas","pollo","zanahorias","papa"]
notas = [9.4 , 5.8 , 10.0]
indefinido = [4.6, "Diego", True, ["Juan", "Maria"],  5j]

print(compras)
print(type(compras))

print(compras[0])
print(compras[3])

compras.append("uvas")
print(compras)
compras.remove("manzanas")
print(compras)

print(notas)
print(type(notas))

print(indefinido)
print(type(indefinido))
