# Cuando existe un error el programa ya no continua y se detiene por completo

# print(0 / 0)) # => SyntaxError
# print(0 / 0) # => ZeroDivisionError
# print(result) # => NameError

suma = lambda x, y: x + y
assert suma(2, 2) == 4
# assert suma(2, 2) == 2 # AssertionError

# si queremos provocar un error en determinadas circunstancias utilizamos raise Exception
age = 10
if age < 18:
    raise Exception('No se permiten menores de edad')

print('Hola') # Este codigo ya no se va a ejecutar por el error provocado