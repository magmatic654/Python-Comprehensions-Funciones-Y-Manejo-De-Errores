# Comprension de listas

# forma "normal"
numbers = []
for element in range(1, 11):
    numbers.append(element*2)
print(numbers) # => [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# list comprenhension
numbers_v2 = [element*2 for element in range(1, 11)]
print(numbers_v2) # => [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

###############################################################
# condiciones

# forma "normal"
numbers_v3 = list()

for i in range(1, 11):
    if i % 2 == 0:
        numbers_v3.append(i * 2)

print(numbers_v3) # =>[4, 8, 12, 16, 20]

# List comprehension
numbers_v4 = [i*2 for i in range(1,11) if i % 2 == 0]
print(numbers_v4) # =>[4, 8, 12, 16, 20]


days = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
newlist = [day for day in days if "d" in day] # => ['sabado', 'domingo']
print(newlist)