for i in range(1, 10):
    print(i)

# iter es un tipo de objeto, controlamos de forma manual la manera en la que se ejecuta
my_iter = iter(range(1, 4))
print(my_iter)
print(next(my_iter)) # siguiente valor de forma manual
print(next(my_iter)) 
print(next(my_iter)) 
print(next(my_iter)) 
