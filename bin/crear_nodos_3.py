#!/usr/bin/env python2
# basado en ideas de
# http://josechristian.com/2013/03/23/random-d3js-network-graph-python-d3js/ 
# dependencias: python2-networkx

from sys import argv
if len(argv) < 4:
  print "Uso: %s cantidad_de_nodos enlaces_minimos enlaces_maximos" % argv[0]
  exit()

import json
import networkx as nx
from networkx.readwrite import json_graph
from random import choice

nodes = int(argv[1])
min_links = int(argv[2])
max_links = int(argv[3])

G= nx.Graph()
G.add_nodes_from(range(1, nodes))

# recorremos todos los nodos
for n in G.nodes():
# elegimos al azar la cantidad de enlaces que va a tener
  e = choice(range(min_links,max_links))

  print "%d con %d enlaces" % (n, e)

# mientras la cantidad de enlaces sea menor a lo planeado
  while e > len(G.neighbors(n)):
# elegir otro nodo al azar
    i = choice(range(1,nodes))

    print "%d enlaza a %d" % (n, i)

# y agregar el enlace
    G.add_edge(n, i)

d = json_graph.node_link_data(G)
json.dump(d, open('assets/data/nodes.json','w'))
