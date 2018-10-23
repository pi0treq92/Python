def v(a,b):
    p=(2*x/((x/a)+(x/b)))
    print(round(p))
x=int(input())
for i in range(x):
    a,b=map(int,input().split())
    v(a,b)