import csv
from charts import generate_bar_chart, generate_pie_chart

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = list()
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for (key, value) in iterable}
            data.append(country_dict)

        return data
    
if __name__ == '__main__':
    data = read_csv('./app/data.csv')
    print(data)
