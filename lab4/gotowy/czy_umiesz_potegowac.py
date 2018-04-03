def f(t,x,y):
    z=1
    while x:
        if x&1:
            z=z*t%y
        x>>=1
        t*=t%y

    return z
x=int(input())
if x>0 and x<11:
    for i in range(x):
        a,b=map(int, input().split())
        print(f(a,b,10))
