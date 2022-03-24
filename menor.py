lista = [2,-300, 4,6,-9,-100, -200]
menor = "init"

for x in lista:
    if menor == "init":
        menor = x
    else:
        menor = x
        if x < menor:
            menor = x
        else:
            menor = menor
print(menor)