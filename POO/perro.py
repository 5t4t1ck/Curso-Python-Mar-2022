class Perro:
    
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f"{self.nombre} de {self.edad} años"
    
    def ladrar(self):
        return f"{self.nombre} ladra fuerte"
    
perro_1 = Perro("Wolf",7)
#print(perro_1.nombre)
print(perro_1)
print(perro_1.ladrar())

perro_2 = Perro("Pequitas","2")
print(perro_2)
print(perro_2.ladrar())
