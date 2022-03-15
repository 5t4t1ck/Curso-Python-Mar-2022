"""def gen_basico():
    yield "uno"
    yield "dos"
    yield "tres"

for valor in gen_basico():
    print(valor) #uno, dos, tres
    
""""""
def funcion():
    return 5

funcion()
"""
def generador():
    #yield 5
    #yield 7
    pass
   
#funcion()

"""print(funcion())
print(generador())
# Salida: 5
# Salida: <generator object generador at 0x103e7f0a0>"""

a = generador()
#print(next(a))
#print(next(a))
# Salida: 5

def generador():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n


print(  )
print(next(g))
print(next(g))
#print(next(g))