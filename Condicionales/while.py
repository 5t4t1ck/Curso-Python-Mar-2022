"""Ejemplo con el while"""

"""contador = 1
while contador < 5:
    print(contador)
    contador = contador + 1"""
    
"""contador = 0
while contador < 5:
    print(contador)
    contador += 1
else:
    print("Dejo de Contar")"""
    
"""contador = 0
while contador < 5:
    print(contador)
    contador+=1
    if (contador==4):
        print("Se rompio")
        break
print(contador)"""

contador = 0
while contador < 5:
    print(contador)
    contador+=1
    if (contador==3):
        continue
print(contador)