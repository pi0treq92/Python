x,y = map(int,input().split())
a=[]
t=0

a= [[int(input()) for i in range(x)] for i in range(y)]
for i in range(x):
    print(a[i])
for i in range(x):
    t=0
    for j in range(0,y):
        t=t+int(a[i][j])
    print("stopien wierzcholka: ", i, 'wynosi:', t)
print(t)