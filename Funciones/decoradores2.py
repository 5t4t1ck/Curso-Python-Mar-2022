def funcion_decoradora(funcion_parametro):
    def funcion_interna():
        print("Ahora vamos a realizar algunas operaciones matemáticas")
        
        funcion_parametro()
        
        print("Se termina la ejecución del código")
        
    return funcion_interna

@funcion_decoradora
def suma():
    print(2+4)
    
@funcion_decoradora 
def resta():
    print(4-2)
    
suma()
resta()