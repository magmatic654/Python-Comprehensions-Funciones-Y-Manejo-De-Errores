import random
countries = ['col', 'mex', 'bol', 'per']

population_v1 = {country: random.randint(1,100) for country in countries}
print(population_v1)

result = {country: population for (country, population) in population_v1.items() if population > 20}
print(result)

text = 'Hola soy Harold'

text_vowels = { c: text.count(c)  for c in text if c in 'aeiou'}

print(text_vowels)