def f(x):
    for i in range(x):
        z=[]
        a,b=map(str, input().split())
        if len(a)>len(b):
            y=len(b)
        else:
            y=len(a)
        for j in range(y):
            t=(((a[j])+(b[j])))
            z.append(t)

        print(''.join(z))
y=int(input())
f(y)
