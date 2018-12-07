graf = {
    '1' : ['5', '7'],
    '2' : ['4'],
    '3' : ['6','8'],
    '4' : ['2','7'],
    '5' : ['1','8'],
    '6' : ['3','4'],
    '7' : ['4', '1'],
    '8' : ['3','5']
}
t=[]
def dfs(G, W, odwiedzone):
    if W not in odwiedzone:
        odwiedzone.append(W)
        for i in G[W]:
            dfs(G,i, odwiedzone)
    return odwiedzone

odwiedzone = dfs(graf,'1', t)


print('Wynik przeszukiwania w głąb:',odwiedzone)

l=[]
for k in graf:
    l.append( len(graf[k]))
print(l)
h=0
if len(graf) == len(odwiedzone):
    for i in range(len(l)):
        if l[i]%2!=0:
            h+=1
    if h ==0:
        print("graf jest eulerowski")
    elif h<=2 and h>0:
        print("graf jest poleulerowski")
    else:
        print("graf nie jest eulerowski")
else:
    print("graf nie jest eulerowski - graf jest niespojny")