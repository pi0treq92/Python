import LF
import networkx as nx
import itertools


a=int(input())
if a ==1:
    fh=open("1_adjlist.txt", 'rb')
if a ==2:
    fh=open("2_adjlist.txt", 'rb')
if a ==3:
    fh=open("3_adjlist.txt", 'rb')
if a ==4:
    fh=open("4_adjlist.txt", 'rb')
if a ==5:
    fh=open("5_adjlist.txt", 'rb')
if a ==6:
    fh=open("6_adjlist.txt", 'rb')
if a ==7:
    fh=open("7_adjlist.txt", 'rb')
if a ==8:
    fh=open("8_adjlist.txt", 'rb')
if a ==9:
    fh=open("9_adjlist.txt", 'rb')
if a ==10:
    fh=open("10_adjlist.txt", 'rb')
if a ==11:
    fh=open("11_adjlist.txt", 'rb')
if a ==12:
    fh=open("12_adjlist.txt", 'rb')
if a ==13:
    fh=open("13_adjlist.txt", 'rb')
if a ==14:
    fh=open("14_adjlist.txt", 'rb')
if a ==15:
    fh=open("15_adjlist.txt", 'rb')
if a ==16:
    fh=open("16_adjlist.txt", 'rb')
if a ==17:
    fh=open("17_adjlist.txt", 'rb')
if a ==18:
    fh=open("18_adjlist.txt", 'rb')
if a ==19:
    fh=open("19_adjlist.txt", 'rb')
if a ==20:
    fh=open("20_adjlist.txt", 'rb')

G=nx.read_adjlist(fh)

def bubbleSort(array):
	length=len(array)
	result = True
	count=0
	while result:
		result = False
		i=0
		while (i < length-1):
			if (array[i] > array[i+1]):
				tempVar = array[i]
				array[i] = array[i+1]
				array[i+1] = tempVar
				result = True
			i=i+1
			count+=1
			print ("Sorting: " + str(array))
	return array
d = nx.coloring.greedy_color(G, LF.bubblesort)
def greedy_color(G, bubbleSort, interchange=False):

    if len(G) == 0:
        return {}

    colors = {}
    wierzcholek = bubbleSort(G, colors)

    for u in wierzcholek:

        kolor_sasiada = {colors[v] for v in G[u] if v in colors}

        for color in itertools.count():
            if color not in kolor_sasiada:
                break
        # Przypisanie koloru do wierzcholka
        colors[u] = color
    return colors

a=[]


for v in d.values():
    a.append(v)

t=set(list(a))
b=str(input())


if b=='k':
    for i in d:
        print('Stopien wierzcholka V', i, ' = ', G.degree(i))

    print('Kolorowanie metodą LF: ',a)

if b=='l':
    for i in d:
        print('Stopien wierzcholka v', i, ' = ', G.degree(i))

    print('liczba chromatyczna = ',len(t))

