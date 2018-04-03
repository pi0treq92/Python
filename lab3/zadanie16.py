import re
s='80,121,116,104,111,110'
t=[]
t=re.findall('\d+', s)
print(t)
for a in t:
    a=int(a)
    print(chr(a))
def f(s):
    print(s)
    d=[]
    for a in s:
        d.append((ord(a)))

    print(d)
g='Dolar'
f(g)

