# Reduce
# Reduce recuce a un solo resultado una lista de elementos
from functools import reduce

numbers = [1,2,3,4,5]

# El counter es el contador acumulado, siempre inicia en 0
# y mientras se vaya iterando la funcion irá en incremento
def accum(counter, item):
    print('counter =>', counter)
    print('item =>', item)
    return counter + item

result = reduce(accum, numbers)
print(result)


result = sum(numbers)
print(result)