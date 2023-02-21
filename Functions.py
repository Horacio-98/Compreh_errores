# Multiples returns
def sumar(numero1,numero2) :
    return numero1 + numero2, numero1, numero2

def restar(numero1,numero2) :
    return numero1 - numero2, numero1, numero2

def multiplicar(numero1,numero2) :
    return numero1 * numero2, numero1, numero2

def dividir(numero1,numero2) :
    return numero1 / numero2, numero1, numero2 


print('\n------------Calculadora----------\n')
print('1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir')
opcion = int(input('Digite una opcion: '))

if opcion == 1 : 
    resultado,num1,num2 = sumar(5,5)
    print(f'{num1} + {num2} = {resultado}')
    
if opcion == 2 : 
    resultado,num1,num2 = restar(5,5)
    print(f'{num1} - {num2} = {resultado}')
    
if opcion == 3 : 
    resultado,num1,num2 = multiplicar(5,5)
    print(f'{num1} * {num2} = {resultado}')
    
if opcion == 4 : 
    resultado,num1,num2 = dividir(5,5)
    print(f'{num1} / {num2} = {resultado}')

