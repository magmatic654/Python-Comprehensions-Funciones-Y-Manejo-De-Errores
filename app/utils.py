def get_population():
    keys = ['col', 'bol']
    values = [300, 400]
    return keys, values

def population_by_countrie(data, country):
    return [item for item in data if item['country'] == country]


