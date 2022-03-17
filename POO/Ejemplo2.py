class Vehiculo:
    
    def __init__(self, tipo, motor):
        self.tipo = tipo
        self.motor = motor
        
    def acelerar(self):
        print("Estoy acelerando")
        
    def frenar(self):
        print("Estoy frenando")
        
    def girar_a_la_derecha(self):
        print("Estoy girando a la derecha")
        
    def girar_a_la_izquierda(self):
        print("Estoy girando a la izquierda")
        
    def cambiar_marcha(self):
        print("Estoy cambiando de marcha")
        
moto = Vehiculo("moto","125 cc")
print(moto.tipo)
print(moto.motor)
moto.acelerar()
moto.frenar()
moto.girar_a_la_derecha()
moto.girar_a_la_izquierda()

carro = Vehiculo("carro","1800 cc")
print(carro.tipo)
print(carro.motor)
carro.acelerar()
carro.girar_a_la_izquierda()
carro.frenar()