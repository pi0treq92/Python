import networkx as nx
import matplotlib.pyplot as plt
from networkx import *

G=nx.Graph()

for i in range(8):
    G.add_node(i)


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


pos = nx.spring_layout(G)
nx.draw(G)
plt.show()
file = open('macierz.txt', 'w')
file.write(str(to_numpy_matrix(G)))
file.close()
fh=open('lista.txt','w')
nx.write_adjlist(G,"lista.txt")
