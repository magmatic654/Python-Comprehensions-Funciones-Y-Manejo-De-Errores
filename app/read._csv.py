import csv
from charts import generate_bar_chart, generate_pie_chart

def read_csv(path, inSearch):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = list()
        for row in reader:
            if inSearch in row:
                iterable = zip(header, row)
                country_dict = {key: value for (key, value) in iterable}
                data.append(country_dict)
        
        country_pop_years = {
            '2022' : data[0]['2022 Population'],
            '2020' : data[0]['2020 Population'],
            '2015' : data[0]['2015 Population'],
            '2010' : data[0]['2010 Population'],
            '1990' : data[0]['1990 Population'],
            '1980' : data[0]['1980 Population'],
            '1970' : data[0]['1970 Population']
        }

        return country_pop_years
    
if __name__ == '__main__':
    data = read_csv('./app/data.csv', 'Colombia')
    years = [year for year, pop in data.items()]
    pop = [int(pop) for year, pop in data.items()]
    generate_bar_chart(years,pop)