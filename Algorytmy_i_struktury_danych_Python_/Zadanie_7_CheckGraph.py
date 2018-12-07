import networkx as nx
from networkx.algorithms import is_bipartite
from networkx.algorithms import is_tree
from networkx.algorithms import coloring

G=nx.Graph()
G1=nx.Graph()
G2=nx.Graph()
G3=nx.Graph()
G4=nx.Graph()

for i in range(8):
    G.add_node(i)
for i in range(5):
    G1.add_node(i)
for i in range(8):
    G2.add_node(i)
for i in range(8):
    G3.add_node(i)
for i in range(4):
    G4.add_node(i)

G.add_edge(0,1)
G.add_edge(0,5)
G.add_edge(0,7)
G.add_edge(0,4)
G.add_edge(1,4)
G.add_edge(1,7)
G.add_edge(1,2)
G.add_edge(1,3)
G.add_edge(2,6)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(5,4)
G.add_edge(7,4)
G.add_edge(7,5)

G1.add_edge(0,1)
G1.add_edge(1,2)
G1.add_edge(2,3)
G1.add_edge(3,4)
G1.add_edge(0,4)

G2.add_edge(0,1)
G2.add_edge(0,5)
G2.add_edge(0,7)
G2.add_edge(0,4)
G2.add_edge(1,2)
G2.add_edge(2,3)
G2.add_edge(2,6)


G3.add_edge(0,5)
G3.add_edge(1,7)
G3.add_edge(3,4)
G3.add_edge(5,4)
G3.add_edge(1,2)
G3.add_edge(2,3)
G3.add_edge(2,6)

G4.add_edge(0,1)
G4.add_edge(0,2)
G4.add_edge(0,3)
G4.add_edge(0,4)
G4.add_edge(1,2)
G4.add_edge(1,3)
G4.add_edge(1,4)
G4.add_edge(2,3)
G4.add_edge(2,4)
G4.add_edge(3,4)

def czy_jest_drzewem(G):
    if is_tree(G)==1:
        print('graf jest drzewem')
    else:
        print('graf nie jest drzewem')

def czy_jest_cyklem(G):
    try:
        nx.find_cycle(G)
        print('Graf jest cyklem')
    except:
        print('graf nie jest cyklem')

def czy_jest_dwudzielny(G):
    if is_bipartite(G)==1:
        print('graf jest dwudzielny')
    else:
        print('graf nie jest dwudzielny')

def czy_jest_pelny(G):
    a=[]
    for i in G4:
        a.append(G.degree(i))
    if (G.number_of_nodes()-1)==min(a) and (G.number_of_nodes()-1)==max(a):
        print('Graf jest pełny')
    else:
        print('Graf nie jest pełny')



czy_jest_drzewem(G)
czy_jest_cyklem(G4)
czy_jest_pelny(G)
czy_jest_dwudzielny(G)
czy_jest_cyklem(G1)
czy_jest_drzewem(G2)
czy_jest_dwudzielny(G3)
czy_jest_pelny(G4)


