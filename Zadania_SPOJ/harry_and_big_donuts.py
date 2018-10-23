def f():
    a, b, c = map(int, input().split())
    if a * c <= b:
        print('yes')
    else:
        print('no')
x=int(input())
for i in range(x):
    f()
