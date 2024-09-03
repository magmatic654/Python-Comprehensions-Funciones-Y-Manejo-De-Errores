# 'r' - es el permiso de lectura
# 'r+' - permite leer y escribir (agregar nuevas lineas respetando el contenido del archivo y agregar más)
# 'w' - es el permiso de escritura
# 'w+' - permite leer y escribir el archivo y se sobreescribira el archivo
with open('./text.txt', 'w+') as file:
    for line in file:
        print(line)
    file.write('Nuevas cosas en este archivo \n')
    file.write('otra linea \n')
    file.write('mas linea\n')