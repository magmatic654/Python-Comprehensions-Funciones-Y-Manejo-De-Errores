# Para resolver este desafío, tu reto completar la función message_creator para que retorne un mensaje
# distinto dependiendo del artículo de tecnología que reciba como entrada.

# La función message_creator recibirá como entrada un string que indica el artículo de tecnología. Luego,
# deberás evaluar el valor de este string y retornar un mensaje distinto dependiendo del valor que reciba.

# La implementacion debe responder al siguiente comportamiento:

# Si recibes una computadora, debes retornar el mensaje: "Con mi computadora puedo programar usando Python".

# Si recibes un celular, debes retornar el mensaje: "En mi celular puedo aprender usando la app de Platzi".

# Si recibes un cable, debes retornar el mensaje: "¡Hay un cable en mi bota!".

# Y si no recibes ninguno de estos valores, debes retornar el mensaje: "Artículo no encontrado".

# Ejemplo 1:
# Input: 'computadora'
# Output: Con mi computadora puedo programar usando Python

# Ejemplo 2:
# Input: 'celular'
# Output: En mi celular puedo aprender usando la app de Platzi

# Ejemplo 3:

# Input: 'cable'
# Output: ¡Hay un cable en mi bota!

# Ejemplo 4:

# Input: 'ornitorrinco'
# Output: Artículo no encontrado

def message_creator(text):
    text = text.lower()
    phrases = {
        'computadora': 'Con mi computadora puedo programar usando Python',
        'celular': 'En mi celular puedo aprender usando la app de Platzi',
        'cable': '¡Hay un cable en mi bota!'
    }
    return phrases[text] if text in phrases.keys() else 'Artículo no encontrado'

print('computadora =>',message_creator('computadora'))
print('celular =>',message_creator('celular'))
print('cable =>',message_creator('cable'))
print('sulivan =>',message_creator('sulivan'))