x=int(input())
def v():
    t = []
    a,b,c=map(int, input().split())
    for j in range(a):
        if (j)%b==0 and (j)%c!=0:
            t.append(j)
        else:
            j=j+1
    print(' '.join(map(str,t)))

for d in range(x):
    v()