set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# union
# retortna todos los elementos de ambos conjuntos 
# sin duplicidad

# Por método 
# union
set_c = set_a.union(set_b)
print(set_c) # => {'mex', 'bol', 'col', 'pe'}

# Por operador 
# |
set_c = set_a | set_b
print(set_c) # => {'mex', 'bol', 'col', 'pe'}

##########################################################

# intersección
# retorna unicamente los elementos que comparten ambos 
# conjuntos

# Por método 
# intersection 
set_c = set_a.intersection(set_b)
print(set_c) # => {'bol'}

# Por operador
# &
set_c = set_a & set_b
print(set_c) # => {'bol'}

##########################################################

# diferencia
# retorna los elementos del primer conjunto exceptuando
# a los que están en la diferencia

# Por metodo
# difference
set_c = set_a.difference(set_b) 
# todos los elementos del conjunto a exceptuando a los que comparte con el b
print(set_c) # => {'col', 'mex'}

# Por operador
# -
set_c = set_a - set_b
print(set_c) # => {'mex', 'col}

##########################################################

# Diferencia simetrica
# retorna unicamente los elementos que ambos conjuntos
# comparten

# Por metodo
# symmetric_difference
set_c = set_a.symmetric_difference(set_b)
print(set_c)

# Por operador
# ^
set_c = set_a ^ set_b
print(set_c)