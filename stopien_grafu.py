x= int(input('Podaj liczbe wierzcholkow: '))
b=[]
t=0
c=[]
for i in range(x):
    a = [int(x) for x in input('Podaj wartosci dla wierzcholka: ').split()]
    b.append(a)
print('Macierz sasiedztwa grafu G: ')
for i in range(x):
    print(b[i])
print('\n')
for i in range(x):
    t=0
    for j in range(0,x):
        t=t+int(b[i][j])
    c.append(t)
    print("stopien wierzcholka: ", i+1, 'wynosi:', c[i])
print('Stopien grafu G wynosi: ',max(c))