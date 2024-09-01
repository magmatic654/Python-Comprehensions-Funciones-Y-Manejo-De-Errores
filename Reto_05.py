# Para resolver este desafío, tu reto es usar la función filter de Python y una función lambda para filtrar una lista de palabras, retornando una
# lista solo con las que cumplan con la condición de tener 4 o más letras.

# La función filter_by_length recibirá como entrada una lista con palabras. Finalmente, la función retornará la lista filtrada.

# Ejemplo 1:
# Input: ['amor', 'sol', 'piedra', 'día']
# Output: [ 'amor', 'piedra' ]

# Ejemplo 2:
# Input: ['rosa', 'gol', 'pez', 'día', 'gafas']
# Output: [ 'rosa', 'gafas' ]

# Con filter
filter_by_length = lambda words: list(filter(lambda word: len(word) >= 4, words))

# Con list comprehension
filter_by_length = lambda words: [word for word in words if len(word) >= 4]