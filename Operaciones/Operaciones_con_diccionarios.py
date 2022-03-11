"""Operaciones con Diccionarios"""

lista1 = [["Juan", "Pedro"],
          ["persona1", "persona2"]]
lista2= dict(lista1)
print(lista2)

lista3 = [('persona1','Juan'), 
          ('persona2','Pedro'), 
          ('persona3','Maria')]
print(dict(lista3))
print(type(dict(lista3)))

diccionario = {"nombre":"Juan", "apellido":"Perez", "cedula":1104528271, "f_nacimiento":"12/01/2022"}

print(diccionario.get("nombre"))

print(diccionario.pop("f_nacimiento"))
print(diccionario)

diccionario.update({"f_nacimiento":"16/03/2021"})
print(diccionario)
print(diccionario.get("f_nacimiento"))

print("cedula" in diccionario)
print("edad" in diccionario)

print(1104528271 in diccionario.values())
print(1104528275 in diccionario.values())

print("---------------------------------------------------------")

#Diccionarios dict
dic =  dict(nombre='nestor', 
            apellido='Plasencia', 
            edad=22)
print(dic)

#Diccionarios zip
dic = dict(zip('abcd',[1,2,3,4]))
print(dic)

#Diccionarios items
dic =   {"a" : 1, "b" : 2, "c" : 3 , "d" : 4}
items = dic.items()
print(items)

#Dicciconarios keys
dic =  {"a" : 1, "b" : 2, "c" : 3 , "d" : 4}
keys= dic.keys()
print(keys)

#Diccionarios values
dic =  {"a" : 1, "b" : 2, "c" : 3 , "d" : 4}
values= dic.values()
print(values)