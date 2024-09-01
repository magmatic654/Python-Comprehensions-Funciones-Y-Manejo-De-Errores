# Importar sistema
import sys
print(sys.path)

# Importar expresiones regulares
import re
text = 'Mi numero de telefono es 545 556 123, el codigo del pais es 57, mi numero de la suerte 3'

result = re.findall('[0-9]+', text)
print(result) # => ['545', '556', '123', '57', '3']

# Importar tiempo
import time
timestamp = time.time()
print(timestamp)

local = time.localtime()
result = time.asctime(local)
print(result)

# Importar colecciones
import collections
numbers = [1, 2, 3, 4, 1, 1, 2, 3, 1, 5, 2, 5, 2, 4, 3, 7, 8]
counter = collections.Counter(numbers)
print(counter) # => Counter({1: 4, 2: 4, 3: 3, 4: 2, 5: 2, 7: 1, 8: 1})
