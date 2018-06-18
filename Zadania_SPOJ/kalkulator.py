def f(a,b,c):
		if str(a)=='+':
			print(int(b)+int(c))
		elif str(a)=='-':
			print(int(b) - int(c))
		elif str(a) == '*':
			print(int(b) * int(c))
		elif str(a)=='/':
			#if c!=0:
				print(int(int(b) / int(c)))
		elif str(a) == '%':
			print(int(b) % int(c))
while True:
		try:
			a, b, c = map(str, input().split())
			f(a, b, c)
		except EOFError:
			break