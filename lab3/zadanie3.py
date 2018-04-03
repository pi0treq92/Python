f=open("liczby.txt", "w")
line=2
for i in range(11,21):
    f.write(str(i))
    f.write("\n")
f.close()
thefile = open("liczby.txt", "r")
theint=[]
for val in thefile.read().split():
    theint.append(int(val))

for i in theint:
    i=i**2
    print(i)
