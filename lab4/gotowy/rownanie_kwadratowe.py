def f():
    for i in range(0,10):
        a, b, c = map(float, input().split())
        if (b**2-4*(a*c))==0:
            print(1)
        elif (b**2-4*(a*c))<0:
            print(0)
        else:
            print(2)
f()