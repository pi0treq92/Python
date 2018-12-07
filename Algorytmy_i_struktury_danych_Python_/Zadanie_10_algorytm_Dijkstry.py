from networkx import *
import networkx as nx
import matplotlib.pyplot as plt

G1=nx.Graph()
G2=nx.Graph()
G3=nx.Graph()
G4=nx.Graph()
G5 = nx.Graph()

G1.add_weighted_edges_from([
        (0,1,2),
        (0,5,4),
        (0,7,5.3),
        (0,4,4.1),
        (1,4,2.1),
        (1,7,3.9),
        (1,2,2.1),
        (1,3,6.4),
        (2,6,3.3),
        (2,3,1.8),
        (3,4,2.7),
        (5,4,2.5),
        (7,4,3.5),
        (7,5,5),])
G1.add_node(8)
G1.add_node(9)

G2.add_weighted_edges_from([
        (0,1,2),
        (1,5,4),
        (2,7,5.3),
        (0,4,4.1),
        (1,4,2.1),
        (3,7,3.9),
        (1,2,2.1),
        (4,3,6.4),
        (8,6,3.3),
        (2,3,1.8),
        (9,4,2.7),
        (5,4,2.5),
        (3,4,3.5),
        (4,5,5),
        (10,1, 3.3),
        (12,3, 1.8),
        (9, 5, 2.7),
        (10, 9, 2.5),
        (8, 10, 3.5),
        (11, 9, 5),
        (11, 4, 3.3),
        (11, 7, 1.8),
        (11, 6, 2.7),
        (12, 10, 2.5),
        (10, 4, 3.5),
        (8, 2, 5),])

G3.add_weighted_edges_from([
        (0, 1, 3.0),
        (1, 2, 7.5),
        (2, 3, 4.5),
        (1, 4, 2.0),
        (2, 4, 5.5),
        (2, 5, 1.5),])

G4.add_weighted_edges_from([
        (0, 1, 3.0),
        (1, 2, 7.5),
        (1, 8, 2.0),
        (2, 4, 5.5),
        (2, 5, 1.5),
        (0, 9, 2),
        (6, 8, 4),
        (0, 7, 5.3),
        (9, 4, 4.1),
        (1, 4, 2.1),
        (6, 7, 3.9),
        (1, 3, 6.4),
        (4, 6, 3.3),
        (9, 3, 1.8),
        (8, 4, 2.7),
        (5, 4, 2.5),
        (7, 4, 3.5),
        (7, 5, 5),])

G5.add_weighted_edges_from([
        (2,1,2),
        (3,5,4),
        (1,7,5.3),
        (1,4,4.1),
        (3,4,2.1),
        (6,7,3.9),
        (4,2,2.1),
        (6,3,6.4),
        (7,6,3.3),
        (2,3,1.8),
        (3,4,2.7),
        (5,4,2.5),
        (2,4,3.5),
        (7,5,5),])

a=int(input('Wybierz graf: '))
if a==1:
    G=G1
    print('Graf ma: ', number_of_nodes(G), 'wierzchołków.')
    b = int(input('Podaj wierzcholek: '))
elif a==2:
    G = G2
    print('Graf ma: ',number_of_nodes(G),'wierzchołków.')
    b = int(input('Podaj wierzcholek: '))
elif a==3:
    G = G3
    print('Graf ma: ', number_of_nodes(G), 'wierzchołków.')
    b = int(input('Podaj wierzcholek: '))

elif a==4:
    G = G4
    print('Graf ma: ', number_of_nodes(G), 'wierzchołków.')
    b = int(input('Podaj wierzcholek: '))

elif a==5:
    G = G5
    print('Graf ma: ', number_of_nodes(G), 'wierzchołków.')
    b = int(input('Podaj wierzcholek: '))

if is_connected(G)==1:
    for i in G:
        if nx.dijkstra_path_length(G,a,i)!=0:
            print('najkrotsza sciezka z wierzcholka',a,'do wierzcholka ',i,'= ',nx.dijkstra_path_length(G,a,i))

A=str(nx.to_numpy_matrix(G))
A=A.replace('0','∞')
print('Macierz odległości: ')
print(A)
file = open('macierz.txt', 'w')
file.write(str(to_numpy_matrix(G)))
file.close()
fh=open('lista.txt','w')
nx.write_adjlist(G,"lista.txt")

pos = nx.spring_layout(G)  # positions for all nodes
nx.draw_networkx_nodes(G, pos, node_size=300)
nx.draw_networkx_edges(G, pos,width=6)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
nx.draw_networkx_labels(G, pos, font_size=15, font_family='arial')
plt.axis('equal')
plt.show()
if a==1:
    plt.savefig("Graph1.png", format="PNG")
elif a==2:
    plt.savefig("Graph2.png", format="PNG")
elif a==3:
    plt.savefig("Graph3.png", format="PNG")
elif a==4:
    plt.savefig("Graph4.png", format="PNG")
elif a==5:
    plt.savefig("Graph5.png", format="PNG")