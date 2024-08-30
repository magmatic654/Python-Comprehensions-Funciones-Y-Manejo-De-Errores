# return es el valor que retorna la función
def sum_with_range(min, max):
    print('min=>', min, 'max =>', max)
    sum = 0
    for x in range(min, max):
        sum += x
    return sum # valor retornado

# Llamar a la funcion y guardar el valor de retorno en una variable
sum_1 = sum_with_range(1, 10)
print(sum_1)
sum_2 = sum_with_range(sum_1, sum_1 + 10)
print(sum_2)
