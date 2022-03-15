variable = 60

def funcion():
    #global variable
    variable = 30
    if variable < 100:
        print(variable)
print(variable)
funcion()
print(variable)