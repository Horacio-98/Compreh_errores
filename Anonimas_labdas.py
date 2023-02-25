
increment = lambda x,y : x+y
print(increment(10,100))

saludo = lambda : 'Hola mundo'
print(saludo())

full_name = lambda x, y : f'{x} {y}'
print(full_name('Horacio','Granados'))

sqr = lambda i: i ** 2
lst = [sqr(i) for i in range(1, 10)]
print(lst)

