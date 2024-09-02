import utils # importamos nuestro modulo y con ello tenemos acceso a las funciones, clases, etc dentro de el.

data = [
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
    ]


def run():
    keys, values = utils.get_population() # llamando a una funcion de nuestro modulo
    print(keys, values)

    # print(utils.A) # llamando a una variable de nuestro modulo

    country = input('Type Country => ').capitalize()

    result = utils.population_by_countrie(data, country)
    print(result)

# Si se ejecuta directamente, se va a ejecutar la funcion run, pero si 
# es ejecutado desde otro archivo por importacion no va a pasar nada
if __name__ == '__main__':
    run()