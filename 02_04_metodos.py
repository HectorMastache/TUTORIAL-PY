def message_creator(text):
   # Escribe tu solución 👇
   return {'computadora' : 'Con mi computadora puedo programar usando Python',
   'celular': 'En mi celular puedo aprender usando la app de Platzi',
   'cable': '¡Hay un cable en mi bota!'}.get(text, 'Artículo no encontrado')

text = 'cable'
response = message_creator(text)
print(response)