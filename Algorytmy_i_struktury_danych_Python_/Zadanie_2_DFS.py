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
def dfs(G, W, odwiedzone):
    if W not in odwiedzone:
        odwiedzone.append(W)
        for i in G[W]:
            dfs(G,i, odwiedzone)
    return odwiedzone

odwiedzone = dfs(graf,'1', t)
print('Wynik przeszukiwania w głąb:',odwiedzone)