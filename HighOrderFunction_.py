def increment(x) : 
    return x+1

def high_function(x) :
    return x + increment(x)

resultado = high_function(2)
print(resultado)


# Otro metodo

multiplicar = lambda x: x*5
orden_superior = lambda x,funcion: x + funcion(x)
orden_superior_2 = lambda x,multiplicar : x + multiplicar(x)
print(orden_superior_2(3,multiplicar))
print(orden_superior(2,lambda x:x+2))





