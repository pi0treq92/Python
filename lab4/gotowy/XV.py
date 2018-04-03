y=int(input())
def f(y):
    while y!=0:
        if y%15==0:
            print('TAK')
        else:
            print('NIE')
        y = int(input())
f(y)