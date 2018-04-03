def euclides(x, y):
	    r = x % y
	    if r == 0:
		    print(y)
	    else:
		    euclides(y, r)
x=int(input())
for c in range(x):
	a,b = map(int, input().split())
	(euclides(a,b))