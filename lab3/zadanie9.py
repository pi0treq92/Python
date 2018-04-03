s='Jan'
e='uli'
t=[]
for a in s:
    t.append(a)
t.insert(1,e)
import string
print(dir(str(t)))
for a in t:
    print(str(a))