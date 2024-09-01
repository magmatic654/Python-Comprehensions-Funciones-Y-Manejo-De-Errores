import copy

items = [
    {
        'product': 'camisa',
        'price': 120
    },
    {
        'product': 'pantalones',
        'price': 300
    },
    {
        'product': 'gorra',
        'price': 50
    }
]

# Obtener una lista con los precios de items
################################################################
# List comprehension
prices = [item['price'] for item in items]
print(prices) # => [120, 300, 50]

# Map
prices_v2 = list(map(lambda item: item['price'], items)) 
print(prices_v2) # => [120, 300, 50]
################################################################

# Obtener una lista con los precios de items y aplicar los taxes
################################################################
def add_taxes(item): 
    item = item.copy() # esto con el proposito de que no se afecta al item original y en consecuencia a la lista original, con esto creando una copia para referirnos a este item
    item['taxes'] = item['price'] * .19
    return item

# utilizar map para transformar cada elemento de la lista con una función
new_items = list(map(add_taxes, items))
# print(new_items)
# print(items)
################################################################

# Utilizar list comprehension para transformar cada elemento de la lista con una función
new_items_v2 = [add_taxes(item) for item in items]
print(new_items_v2)