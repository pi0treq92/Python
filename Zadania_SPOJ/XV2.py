def f(n):
    if n%15 == 0:
        return n
    else:
        return  f(n-1)
x=int(input())
for i in range(x):
    print(f(int(input())))