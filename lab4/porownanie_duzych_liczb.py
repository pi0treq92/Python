for i in range(0,10):
    a,b,c=map(str, input().split())
    if b=='==':
        if int(a) == int(c):
            print(1)
        else:
            print(0)
    if b=='<=':
        if int(a) <= int(c):
            print(1)
        else:
            print(0)
    if b=='>=':
        if int(a) >= int(c):
            print(1)
        else:
            print(0)