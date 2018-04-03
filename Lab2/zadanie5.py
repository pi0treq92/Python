def euclides(x, y):
	    r = x % y
	    if r == 0:
		    print (y)
	    else:
		    euclides(y, r)

a, b = map(int, input().split())

euclides(a, b)