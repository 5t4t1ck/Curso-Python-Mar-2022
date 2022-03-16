"""Aquí va el código de excepciones"""

"""while True:
    try: #intenta ejecutar el código
        x = int(input("Por favor ingrese un número: "))
        break
    except ValueError: #Maneja el error
        print("Opps! No era válido. Por favor intenta de nuevo")"""
        
def division():
    try: #El codigo a ejecutarse es el siguiente
        a = int(input("Por favor ingrese un valor: "))
        b = int(input("Por favor ingrese un segundo valor: "))
        div = a / b
        return div
    except SyntaxError:
        print("Ingrese un valor válido")
    except ValueError:
        print("Ingrese un valor válido")
    except ZeroDivisionError:
        print("No se ha podido realizar la división")
    finally:
        print("Nos vemos en una próxima ocasión")
print(division())