import networkx as nx
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
for i in G.nodes():
    print('Stopień wierzcholka: ',i,' =',G.degree(i))
print('Liczba wierzcholkow: ',G.number_of_nodes())
print('Liczba krawedzi: ',G.number_of_edges())
t=[]
d=[]
for i in G.nodes():

    if G.degree(i)==1:
        t.append(i)
    if G.degree(i)==3:
        d.append(i)
print('Liczba liści grafu: ',len(t))
print('Graf ma: ',len(d), 'wierzcholkow stopnia 3')



