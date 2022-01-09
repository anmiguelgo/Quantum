# Importamos librerías
import networkx as nx
import dwave_networkx as dnx
import matplotlib.pyplot as mpl
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

# Definimos los Samplers
sampler = EmbeddingComposite(DWaveSampler())

# Definimos el grafo, con 5 nodos, 
s5 = nx.star_graph(5)

# lo dibujo
print(dnx.min_vertex_cover(s5, sampler))

# Al ejecutarlo, como hemos pedido grafo en estrella, el del centro lo crea com [0], por lo que ese debería ser el resultado
# Resultado:
# Leap IDE /workspace/Quantum $ /usr/local/bin/python /workspace/Quantum/Pruebagrafo8.py (Esta es la cola de ejecución)
# # [0]

# si ahora lo quiero representar graficamente, le pido que lo represente con etiquetas y lo almacene en .png
nx.draw(s5, with_labels = True)
mpl.savefig("grafo5.png")