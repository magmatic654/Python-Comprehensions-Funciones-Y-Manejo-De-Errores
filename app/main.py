import utils # importamos nuestro modulo y con ello tenemos acceso a las funciones, clases, etc dentro de el.

keys, values = utils.get_population() # llamando a una funcion de nuestro modulo
print(keys, values)

# print(utils.A) # llamando a una variable de nuestro modulo

country = input('Type Country => ').capitalize()

print(utils.population_by_countrie([
    {
        'country': 'Mexico',
        'population': '1200'
    },
    {
        'country': 'Colombia',
        'population': '300'
    },
    {
        'country': 'Bolivia',
        'population': '50'
    }
], country))