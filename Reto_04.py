# Para resolver este desafío, tu reto es utilizar la función map de Python y una función lambda para transformar una lista de números. 
# Debes retornar una lista en la que cada número de la lista original sea multiplicado por dos.

# La función multiply_numbers recibirá como entrada una lista con números. 
# Finalmente, la función retornará la lista transformada.

# Ejemplo 1:
# Input: [2, 4, 5, 6, 8]
# Output: [4, 8, 10, 12, 16]

# Ejemplo 2:
# Input: [1, 1, -2, -3]
# Output: [2, 2, -4, -6]

# lambda y map
multiply_numbers = lambda numbers: list(map(lambda number: number * 2, numbers))
print(multiply_numbers([1, 1, -2, -3]))

# lambda y list comprehension
multiply_numbers_v2 = lambda numbers: [number * 2 for number in numbers]
print(multiply_numbers_v2([1, 1, -2, -3]))
