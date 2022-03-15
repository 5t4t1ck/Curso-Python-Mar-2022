def nombre(nombre="Nombre",apellido="Apellido"):
    return nombre #yield
    return apellido
    
"""a = next(nombre("Diego"))
print(a)
b = next(nombre("Saavedra"))
print(b)"""
z = nombre("Diego", "Saavedra")
print(z)
z = nombre("Juan", "Saavedra")
print(z)

