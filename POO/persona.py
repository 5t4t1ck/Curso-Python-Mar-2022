class Abuelo:
    def __init__(self,nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    def __str__(self):
        return f"Yo soy la clase Abuelo, mi nombre es {self.nombre}"
    
    def contarHistorias(self, epoca):
        self.epoca = epoca
        return f"Esta historia paso en la {self.epoca}"

class Padre(Abuelo):
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, edad)
        
    def __str__(self):
        return f"Yo soy la clase Padre, mi nombre es {self.nombre}"
    
    def empleo(self, profesion):
        self.profesion = profesion
        return f"Yo tengo la profesion de {self.profesion}"

class Hijo(Padre):
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, edad)
        
    def __str__(self):
        return f"Yo soy la clase Hijo, mi nombre es {self.nombre}"

    def jugar(self, deporte):
        self.deporte = deporte
        return f"Yo suelo jugar {self.deporte}"
    
class Hija(Padre):
    def __init__(self, nombre, apellido, edad):
        super().__init__(nombre, apellido, edad)
        
    def __str__(self):
        return f"Yo soy la clase hija, mi nombre es {self.nombre}"

    
Juan = Padre("Juan","Martinez",35)
print(Juan.empleo("Carpintero"))
print(Juan)

Luisa = Hija("Luisa","Martinez",10)
print(Luisa.contarHistorias("1980"))
print(Luisa)