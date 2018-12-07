graf = {
    '1' : ['3','5'],
    '2' : ['4'],
    '3' : ['1','6','7','8'],
    '4' : ['2', '6'],
    '5' : ['1','8'],
    '6' : ['3','4'],
    '7' : ['3'],
    '8' : ['3','5']
}
t=[]
b=[]
items=(graf.values())
t=list(items)
for i in range(8):
    print('Stopien wierzcholka ',i+1,' = ', len(t[i]))
    b.append(len(t[i]))
print('Stopien grafu wynosi = ',max(b))