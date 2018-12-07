from networkx import *
import matplotlib.pyplot as plt
g = nx.read_adjlist("1_macierz.txt")
print(g.degree())
d=complement(g)
k=line_graph(g)

pos = nx.spring_layout(d)
nx.draw(d)
plt.show()
pos = nx.spring_layout(k)
nx.draw(k)
plt.show()