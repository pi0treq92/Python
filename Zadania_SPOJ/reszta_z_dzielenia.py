x=int(input())
def f(c):
    for a in range(c):
        a,b=map(int,input().split())
        if (a and b)<10**6 and b!=0:
            print(a%abs(b))
f(x)