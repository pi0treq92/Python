g = lambda x: x*g(x-1) if x>0 else 1
print(g(200))