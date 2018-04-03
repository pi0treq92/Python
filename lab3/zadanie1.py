x=int(input())
if x<1 or x>10:
    x = int(input())
t=[]
if x<1 or x>10:
    x = int(input())
for c in range(x):
    a,b = map(int, input().split())
    if (a<1 or a>1000000) or (b<1 or b>1000000):
        a, b = map(int, input().split())
    else:
        t.append((a,b))
for a in range(x):
    d= str(int(t[a][0]**t[a][1]))
    print(d[len(d)-1])
