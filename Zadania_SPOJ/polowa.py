def f(x):
    if len(x)%2==0:
        print(x[0:int(len(x)/2)])
    else:
        print(x[0:(int(len(x)/2+1))])
x=int(input())
for i in range(x):
    a=str(input())
    f(a)