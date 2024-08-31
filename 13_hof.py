# Higher order functions
# las higher order functions son funciones que reciben como parametro a otra funcion para ejecutarla dentro de la misma

def increment(x):
    return x + 1

def high_ord_func(x, func):
    return x + func(x)

result = high_ord_func(2, increment) # 2 + (2 + 1) = 5
print(result) # => 5

# Con lambda
increment_v2 = lambda x: x + 1
high_ord_func_v2 = lambda x, func: x + func(x) 

result_2 = high_ord_func_v2(2, increment_v2) # 2 + (2 + 1) = 5
print(result_2) # => 5

# no es necesario guardar las funciones lambda en variables
result_3 = high_ord_func_v2(2, lambda x: x + 2) # 2 + (2 + 2) = 6
print(result_3) # => 6

result_4 = high_ord_func_v2(2, lambda x: x * 5) # 2 + (2 * 5) = 12
print(result_4) # => 12