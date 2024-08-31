# las lambda functions son funciones que permiten retornar valores dada una funcion anonima que se escribe en una sola linea, para crear una lambda function se utiliza la siguiente estructura:

# name = lambda arguments: expression

# name - nombre de la funcion que deberemos llamar
# lambda - declaracion de la función anonima
# arguments - los argumentos de la funcion
# expresion - la expresion de la funcion

# función normal
def increment(x):
    return x + 1

result = increment(10)
print(result)

# funcion anonima lambda
increment_v2 = lambda x: x + 1
print(increment_v2(120))

# Varios argumentos en una funcion anonima
full_name = lambda name, last_name: f'Full name is: {name.title()} {last_name.title()}' 
print(full_name('harold edward', 'rodriguez navarro'))
