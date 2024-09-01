# Map
# La funcion map es una funcion que corresponde a las hof, esta se encarga
# de realizar transformaciones a una lista de elementos

numbers = [1, 2, 3, 4]
numbers_v2 = [i * 2 for i in numbers] # list comprehension
print(numbers_v2) # => [2, 4, 6, 8]

# Con map y lambda
numbers_v3 = list(map(lambda i: i * 2, numbers ))
print(numbers_v3)

numbers_1 = [1, 2, 3, 4, 5]
numbers_2 = [5, 6, 7]

print(numbers_1)
print(numbers_2)
# Con el map podemos transformar elementos de 2 o mas listas aunque no tengan la misma longitud.
#Ejemplo:
result = list(map(lambda x, y: x + y, numbers_1, numbers_2))
print(result)
