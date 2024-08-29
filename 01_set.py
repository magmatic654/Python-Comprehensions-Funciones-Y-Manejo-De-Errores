# set
# Los conjuntos agrupa elementos con algo en común

# Propiedades.
# - Se pueden modificar
# - No tienen un orden
# - No permite duplicados

# Los conjuntos se definen con llaves de la siguiente manera:
set_countries = {'col', 'mex', 'bol'}
print(set_countries) # => {'col', 'mex', 'bol'}
print(type(set_countries)) # => <class 'set'>

# Aunque los valores se repiten, solo guardará a uno de ellos
set_numbers = {1, 2, 3, 3, 444, 20}
print(set_numbers)

set_types = {1, 'hola', True, 12.5}
print(set_types)

# Crear un conjunto a partir de un string
set_from_string = set('hoola')
print(set_from_string) # => {'l', 'o', 'a', 'h'}

# Crear un conjunto a traves de una tupla
set_from_tuple = set(('abc', 'cde', 'cdf', 'abc' ))
print(set_from_tuple) # => {'cdf', 'cde', 'abc'}

# Crear un conjunto a traves de una lista
numbers = [1,2,3,4,1,2,3,4]
set_numbers = set(numbers)
print(set_numbers) # => {1, 2, 3, 4}

# Volver a lista el conjunto con los numeros 
# unicos de la lista inicial
unique_numbers = list(set_numbers)
print(unique_numbers) # => [1, 2, 3, 4]