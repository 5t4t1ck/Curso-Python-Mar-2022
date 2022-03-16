"""def generadorPares(Limite):
    
    num = 1
    
    lista = []
    
    while num<Limite:
        lista.append(num*2)
        num += 1
    return lista

print(generadorPares(10))"""

def generadorPares(Limite):
    
    num = 1
    
    while num<Limite:
        yield num*2
        num += 1
        
devuelvePares=generadorPares(10)

"""for i in devuelvePares:
    print(i)"""
    
print(next(devuelvePares))
print("Aquí va un poco más de código")
print(next(devuelvePares))
print("Aquí va mucho más código del que necesitamos hacer")
print(next(devuelvePares))