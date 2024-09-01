numbers = [1,2,3,4,5]
# filter filtra los elementos de una lista dependiendo de una condicion, si da como verdadero la expresion logica, entonces ese elemento será añadido a la lista de numeros nueva sin afectar a la original

# Filter
new_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(new_numbers)
print(numbers)

# List comprehension
new_numbers_v2 = [x for x in numbers if x % 2 == 0]
print(new_numbers_v2)
print(numbers)

