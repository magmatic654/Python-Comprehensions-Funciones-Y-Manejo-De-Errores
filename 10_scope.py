# el scope es el alcance de nuestras variables
price = 100 # global

def increment():
    price = 200 # local - no tiene nada que ver con la variable global y solo funciona en el contexto dentro de la funcion
    result = price + 10  # local
    print(price)
    return result
    
print(price)
price_2 = increment()
print(price_2)