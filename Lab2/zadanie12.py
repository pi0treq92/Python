import functools
f = lambda x,y: x+y
lista = [1,2,3,4,5,6]
print(functools.reduce(f, lista))


