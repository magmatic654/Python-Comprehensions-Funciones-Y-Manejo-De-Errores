import utils # importamos nuestro modulo y con ello tenemos acceso a las funciones, clases, etc dentro de el.
import read_csv
import charts

def run():
    data = read_csv.read_csv('./app/data.csv')
    country = input('Type country => ')

    result = utils.population_by_countrie(data, country)
    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country) # llamando a una funcion de nuestro modulo
        charts.generate_bar_chart(labels, values)


# Si se ejecuta directamente, se va a ejecutar la funcion run, pero si 
# es ejecutado desde otro archivo por importacion no va a pasar nada
if __name__ == '__main__':
    run()