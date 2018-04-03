def liczba(a):
    if a==0:
        print("zero")
    elif a==1:
        print("jeden")
    elif a==2:
        print("dwa")
    elif a==3:
        print("trzy")
    elif a == 4:
        print("cztery")
    elif a==5:
        print("piec")
    elif a==6:
        print("szesc")
    elif a==7:
        print("siedem")
    elif a==8:
        print("osiem")
    elif a==9:
        print("dziewiec")
t=[]
x=0
x=int(input())
y=0
g={}
while x>0:
    t.append(x%10)
    x=int(x/10)
    y=y+1
for a in range(y-1,-1,-1):
   liczba(t[a])
