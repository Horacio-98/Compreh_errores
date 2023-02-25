lista_1 = [1,2,3,4,5,6]
pares = lambda x:x%2 == 0
resultado = list(filter(pares,lista_1))
print(resultado)