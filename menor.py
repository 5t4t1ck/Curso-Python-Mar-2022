lista = [2,-800, 4,6,-9,-1000, -200]
menor = "init"
for x in lista:
    if menor == "init" or menor > x:
        menor = x
    elif menor < x:
        menor = menor       
print(menor)