set_countries = {'col', 'mex', 'bol'}

# len
# retorna el número de elementos dentro del conjunto
size = len(set_countries)
print(size)

# in 
# retorna en booleano si está un elemento especifico 
# dentro del conjunto
print('col' in  set_countries) # => True
print('ar' in  set_countries) # False

# add
# agrega un elemento al conjunto
set_countries.add('ar')
print(set_countries) # => {'ar', 'col', 'bol', 'mex'}

# no se pueden duplicar elementos en un conjunto
set_countries.add('ar')
print(set_countries) # => {'ar', 'col', 'bol', 'mex'}

# update
# Actualizar conjuntos (pueden ser varios a la vez)
set_countries.update({'pe', 'ar', 'ecu'})
print(set_countries) # => {'ar', 'pe', 'ecu', 'col', 'bol', 'mex'}

# remove
# elimina un elemento en especifico del conjunto
# si no existe el elemento dará un error en el programa
set_countries.remove('col')
print(set_countries) # => {'ar', 'ecu', 'mex', 'pe', 'bol'}
set_countries.remove('ar')
print(set_countries) # => {'mex', 'bol', 'pe', 'ecu'}

# discard
# elimina un elemento en especidico del conjunto y
# si no existe no habrán errores
set_countries.discard('arg') # no existe pero no hay errores

# clear
# vacía todo el conjunto
set_countries.clear()
print(set_countries) # => set()
