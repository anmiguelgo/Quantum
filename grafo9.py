# Importamos librerías modulos python para trabajar con grafos

import networkx as nx 
import dwave_networkx as dnx 
import matplotlib.pyplot as plt 

# Importamos librerías OCEAN para ejecutar contra QPU
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

# Ahora creamos un grafo de 6 nodos
G=nx.Graph()
G.add_nodes_from(["1","2","3","4","5","6","7","8","9"])
G.add_edge("1","2")
G.add_edge("1","3")
G.add_edge("2","3")
G.add_edge("2","4")
G.add_edge("3","4")
G.add_edge("3","5")
G.add_edge("4","5")
G.add_edge("2","6")
G.add_edge("4","6")
G.add_edge("4","7")
G.add_edge("2","8")
G.add_edge("4","9")
G.add_edge("7","8")
G.add_edge("7","9")

# Dibujamos el grafo y lo almacenamos
nx.draw(G, with_labels = True)
plt.savefig("grafo9.png")

# ejecutams contra la QPU
sampler = EmbeddingComposite(DWaveSampler())
print(dnx.min_vertex_cover(G, sampler))