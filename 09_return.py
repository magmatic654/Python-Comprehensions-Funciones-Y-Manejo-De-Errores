# definir una funcion con valores por defecto
def find_volume(lenght = 1, width = 1, depth = 1): 

    # Se pueden retornar multiples valores y por defecto será en una tupla 
    return lenght * width * depth, width, 'hola'

volume_1 = find_volume(10, 5, 2)
print(volume_1)

# Si no ponemos ningún valor se pondrán los valores por defecto que la función tiene asignada, de lo contrario mandará un error
volume_2 = find_volume()
print(volume_2)

# Enviar un valor en especifico poniendo el nombre e igualandolo al valor que queremos mandar
volume_3 = find_volume(width=10)
print(volume_3)

# podemos obtener los distintos valores de una función si separamos con una coma el nombre de la variable en el orden que la funcion retorna
# los resultados

volume, width, text = find_volume(width=10)

# gracias a esto podemos sacar cada valor devuelto de manera independiente
print(volume) # => 10
print(width) # => 10
print(text) # => 'hola'