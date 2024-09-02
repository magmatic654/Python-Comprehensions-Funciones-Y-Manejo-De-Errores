# importar funciones desde una carpeta hermana
# from pkg.mod_1 import func_1, func_2
# import pkg.mod_1
# from pkg.mod_2 import func_3, func_4


# print(func_1())
# print(func_2())
# print(func_3())
# print(func_4())


# Podemos llamar variables o funciones del init directamente

import pkg
print(pkg.URL)

# utilizando name space
print(pkg.mod_1.func_1())