file = open('./text.txt')
# leer todo el archivo (requiere de muchos recursos pues lee todo al momento)
'''
print(file.read())
'''
# leer linea a linea el archivo (requiere de menos recursos pues va de linea en linea)
'''
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
'''
# Podemos utilizar un ciclo para leer todo el archivo linea por linea
'''
for line in file:
    print(line)
'''

# debemos cerrar el archivo para liberar espacio en memoria
file.close()


# Podemos automatizar abrir y cerrar el archivo para no hacerlo manualmente
with open('./text.txt') as file:
    for line in file:
        print(line)