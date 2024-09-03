def get_population(country_dict):
    years = ['2022', '2020', '2015', '2010', '2000', '1990', '1980', '1970']
    population_dict = {year: int(country_dict[f'{year} Population']) for year in years}

    labels = population_dict.keys()
    values = population_dict.values() 
    print(labels)
    print(values)
    return labels, values

def population_by_countrie(data, country):
    return [item for item in data if item['Country/Territory'] == country]


