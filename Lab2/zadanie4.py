li = []
x=0
for i in range(100):
    x=i
    li.insert(i, x)

l=[y for y in li if y>=40 and y<=50]
print(l)
