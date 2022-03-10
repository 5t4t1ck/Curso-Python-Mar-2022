"""Ejemplos de Operaciones con listas"""

lista = ["a", "e", "i", "o", "u", "e"]
print("La cantidad de valores de lista es: ", len(lista))
print(lista[4])
lista2 = lista[0:3]
print(lista2)

lista.append("j")
print(len(lista))
print(lista)

print("j" in lista)

lista.remove("j")
print(len(lista))
print(lista)

"""lista.remove("x")
print(len(lista))
print(lista)"""

lista.insert(4, "Juan")
print(lista)

print("j" in lista)

print(lista.index("u"))

lista3 = lista + lista2
print(lista3)

print(lista3[0:9:2])

print(max(lista))
print(min(lista))