def f(r, d):
	pi=3.141592654
	if d>=1 and d<r*2 and r*2<=2000:
		a= pi*(r**2-(d/2)**2)
		print('%.2f' %a)
a,b = map(float, input().split())
f(a,b)