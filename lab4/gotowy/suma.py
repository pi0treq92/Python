def f(x,y):
    y+=x
    print(y)
    return(y)
y=0
for i in range(0,10):
    x=int(input())
    y = f(int(x),y)

