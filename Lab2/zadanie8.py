d={"orange": 5,"cheese": 10, "apple": 4, "ham": 8}
l=['ham', 'cheese','apple']
def f(x,y):
	lst = []
	for a in x:
		if a in y:
			c=y.get(a, y)
			print(a, c)
		if a in y:
			lst.append(c)
	print("cena za zakupy: ", sum(lst), "zl")

f(l,d)


