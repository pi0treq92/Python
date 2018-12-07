import sys
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
    return G


def stopien(G):

    t = []
    for wierzcholek in G:
        deg = len(G[wierzcholek])
        t.append(deg)
    return t

def sortowanie():
    d= list(reversed(sorted(stopien(G))))
    return d
tworzenie_grafu()
c = [int(i) for i in G]
colors=sorted(c)
d = [i for i in G]
wierzcholki=sorted(d)
kolor_wierzcholka = {}

print(G)
def f(i, color):
    for sasiad in G.get(i):
        kolor_sasiada = kolor_wierzcholka.get(sasiad)
        if kolor_sasiada == color:
            return False
    return True

def kolorowanie_wierzcholkow(i):
    for color in colors:
        if f(i, color):
            return color
#def liczba_chromatyczna():
def main():
    for i in wierzcholki:
        kolor_wierzcholka[i] = kolorowanie_wierzcholkow(i)
    print('Liczba_chromatyczna: ',len(list(set(kolor_wierzcholka.values()))))
    for key in G.keys():
        a = list(G)

    for j in range(len(a)):
            print('wierzcholek: ',a[j], 'kolor: ', kolor_wierzcholka[a[j]])

main()
print(stopien(G))
"""
#funkcja main()

def g():
    if sys.argv[1] == '-k':
        kolorowanie_wierzcholkow()
    else sys.argv[0] =='-l':
        liczba_chromatyczna
    else
        kolorowanie_wierzcholkow()
        liczba chromatyczna
if name == '__main__':
    main()
def color(tab_sortowane, graf):
    kolory = {}
    tab_sortowane[0]
    kolory_V=[v] = 0
    for v in tab_sortowane

def color_graph(method, opt):
    l = [len(graph)]
"""