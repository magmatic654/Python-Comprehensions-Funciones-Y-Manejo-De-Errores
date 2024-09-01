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

def add_taxes(item): 
    new_item = item.copy() 
    new_item['taxes'] = new_item['price'] * .19
    return item

new_items = list(map(add_taxes, items))
print(new_items)
print(items)
