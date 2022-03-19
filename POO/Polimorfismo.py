class Animal:
    def hablar(self):
        pass
    
class Perro(Animal):
    def hablar(self):
        print("Guau")

class Gato(Animal):
    def hablar(self):
        print("Miauuu")

class Vaca(Animal):
    def hablar(self):
        print("Muuuuu")
        
animales = [Perro(), Gato(), Vaca()]

for animal in animales:
    animal.hablar()

