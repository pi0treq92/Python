import functools
f = lambda x,y: x if x>y else y
lista = [1,2,3,7,5,6]
print(functools.reduce(f, lista))