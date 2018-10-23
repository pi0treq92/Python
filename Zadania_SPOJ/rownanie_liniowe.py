def f(a,b,c):
    if a==0:
        if b==c:
            print('NWR')
        else:
            print('BR')
    else:
        print('%.2f' %((c-b)/a))
a,b,c=map(float,input().split())
f(a,b,c)