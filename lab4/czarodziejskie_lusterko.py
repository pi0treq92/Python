while True:
    x = int(input())
    y=bin(x)
    print(y)
    y=str(y)
    z=('0b'+y[-1:-len(y)+1:-1])
    print(z)
    z=int(z,2)
    print(z)