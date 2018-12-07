G = {}




""" Utworzenie grafu z pliku wejscia .txt"""
def tworzenie_grafu():

    while 1:
        try:
            wejscie = input().split()
            if len(wejscie) >= 2:
                if wejscie[0] not in G:
                    G[wejscie[0]] = []
                G[wejscie[0]].append(wejscie[1])

                if wejscie[1] not in G:
                    G[wejscie[1]] = []
                G[wejscie[1]].append(wejscie[0])

            else:
                G[wejscie[0]] = []

        except EOFError:
            break
    print(G)

""" sprawdzenie spojnosci grafu """
def spojnosc(G):
    t=[]
    visited = dfs(G, '1')
    for k in G.keys():
        t.append(k)
    return (len(visited) == len(t))

""" sprawdzenie parzystosci wierzcholkow grafu """
def parzystosc(G):
    l = stopien(G)
    par = []
    npar = []
    for i in l:
        if i % 2 == 0:
            par.append(i)
        else:
            npar.append(i)
    a = len(l) - len(par)
    if a==0:
        return 1
    elif len(npar) == 2:
        return 2

def stopien(G):

    t = []
    for wierzcholek in G:
        deg = len(G[wierzcholek])
        t.append(deg)
    return t

def sortowanie():
    d= list(reversed(sorted(stopien(G))))
    return d

def greedy(s, f):

    assert(len(s) == len(f))
    n = len(s)
    a = []
    k = 0
    for m in range(1, n):
        if s[m] >= f[k]:
            a.append(m)
            k = m
    return a

def dfs(G, V):

    stack = []
    stack.append(V)
    visited = []
    visited.append(V)

    while stack:
        V = stack.pop()
        for i in G[V]:
            if not i in visited:
                stack.append(V)
                stack.append(i)
                visited.append(i)
    return visited

def spojny(G):
    return spojnosc(G)

def poleulerowski(G):
    return spojnosc(G) and parzystosc(G) == 2

def eulerowski(G):
    return spojnosc(G) and parzystosc(G) == 1

def f(G):
    if eulerowski(G):
        print("Graf G jest eulerowski")
    elif poleulerowski(G):
        print("Graf G jest poleulerowski")
    elif spojny(G):
        print("Graf G jest spojny")
    else:
        print("Graf G jest niespojny")

tworzenie_grafu()

""" Sprawdzenie dla pliku 13"""
def sprawdzenie_1(G):
    l = []
    for i in G.keys():
        l.append(int(i))
    t = sorted(l)

    return (t[0] == 1)
if sprawdzenie_1(G):
    f(G)
else:
   print("graf nie ma wierzcholka 1")

f=stopien(G)

print(greedy(sortowanie(), f))
