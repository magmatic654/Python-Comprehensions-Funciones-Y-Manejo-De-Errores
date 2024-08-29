# Comprension de diccionarios

# Forma "normal"
dict_v1 = dict()
for i in range(1,5):
    dict_v1[i] = i*2

print(dict_v1) # => {1: 2, 2: 4, 3: 6, 4: 8}

# Dict comprehensions
dict_v2 = { i: i*2 for i in range(1,5)}
print(dict_v2)

#########################################################
# crear un diccionario apartir de una lista existente
import random
countries = ['col', 'mex', 'bol', 'per']

# Forma "normal"
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
print(population)

# Dict comprehension
population_v2 = {country: random.randint(1,100) for country in countries}
print(population_v2)

#########################################################
# crear un diccionario apartir de dos listas existentes
names = ['harold', 'nico', 'pablo']
ages = [24, 32, 55]

# Forma "normal"
users = dict()
for i in range(len(names)):
    users[names[i]] = ages[i]
print(users)

# Dict comprehensions
users_v2 = {names[i]: ages[i] for i in range(len(names))}
print(users_v2)

#########################################################
# Utilizando método zip
zip_list = zip(names, ages)
print(zip_list) # => <zip object at 0x0000015282C43680>
print(list(zip_list)) # => [('harold', 24), ('nico', 32), ('pablo', 55)]
# Forma "normal"
users_v3 = dict()

for (name, age) in zip(names, ages):
    users_v3[name] = age
print(users_v3)

# Dict comprehensions
users_v4 = {name: age for (name, age) in zip(names, ages)}
print(users_v4)

# Direct form
users_v5 = dict(zip(names, ages))
print(users_v5)