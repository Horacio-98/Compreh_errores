def message_creator(text):
   if text == 'computadora' : 
       return 'Con mi computadora puedo programar usando Python'
   elif text == 'celular' : 
       return 'En mi celular apendo usando la app de Platzi'
   elif text == 'cable' : 
       return '¡Hay un cable en mi bota' 

text = input('Ingrese una palabra clave : ').lower()
response = message_creator(text)
print(response)


'''
Otra forma con diccionarios

def message_creator(text):
   # Escribe tu solución 👇

   respuestas = {'computadora' : "Con mi computadora puedo programar usando Python", 
                    'celular' : "En mi celular puedo aprender usando la app de Platzi",
                    'cable' : "¡Hay un cable en mi bota!"}

   if text in respuestas.keys(): 
      return respuestas[text]
   else: 
      return 'Artículo no encontrado'

text = 'computadora'
response = message_creator(text)
print(response)

'''