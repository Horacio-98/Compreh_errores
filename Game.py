import random

print('------- JUEGO DE PIEDRA, PAPEL O TIJERA--------\n\n')

user_option = '0'
computer_option = '0'


user_option = input(' Elige piedra, papel o tijera: ').lower()

options = ['piedra', 'papel', 'tijera']
computer_option = random.choice(options)

print(f'\nEl usuario ha elegido: {user_option}\nY la computadora selecciono: {computer_option}\n\n')
  


if user_option == computer_option :
  print('EMPATE')

elif user_option == 'piedra' : 
  if computer_option == 'papel' : 
    print('LA COMPUTADORA HA GANADO ')

  elif computer_option == 'tijera' : 
    print('EL USUARIO HA GANADO')

elif user_option == 'papel' : 
  if computer_option == 'piedra' : 
    print('EL USUARIO HA GANADO')

  elif computer_option == 'tijera' : 
    print('LA COMPUTADORA HA GANADO')

elif user_option == 'tijera' : 
  if computer_option == 'piedra' : 
    print('LA COMPUTADORA HA GANADO')

  elif computer_option == 'papel' : 
    print('EL USUARIO HA GANADO')


