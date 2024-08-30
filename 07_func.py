# Las funciones permite reutilizar codigo multiples veces sin la necesidad de escribirlo varias veces

# Ventajas
# + Reutilizacion de codigo
# + Mayor mantenibilidad del programa

print('Hello')

# Definimos la funcion con la palabra reservada def
def my_print(text):
    print(text * 2)

my_print('Este es mi texto')
my_print('Hi')

a = 10
b = 90

c = a + b

def sum(a, b):
    # Utilizar una funcion dentro de otra
    my_print(a + b)

sum(1, 5) # => 6
sum(10, 4) # => 14