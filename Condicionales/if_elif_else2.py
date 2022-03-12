"""Saber el rango de edad de una persona

Por ejemplo:
    Si es menor o igual a 12 años, es un niño
    Si es mayor 12 años pero menor o igual a 18, es un adolecente
    Si es mayor a 18 años pero menor a 60 años, es un adulto
    Si es mayor a 60 años, es un adulto mayor"""
    
edad = int(input("Por favor ingrese su edad: "))

if edad <= 12:
    print("Es un niño")
elif edad < 18:
    print("Es un adolcente")
elif edad <= 60:
    print("Es un adulto")
else:
    print("Es un adulto mayor")

