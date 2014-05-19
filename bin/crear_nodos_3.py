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

hosts = [ 'nexus', 'pvnoidentificado', 'marcopolo', 'parabola',
'BlackWood', 'tardis', 'gauss', 'brendanvps', 'robotica', 'clementina',
'almendro', 'susa', 'hilarious', 'lancelot', 'PuntoRojo1', 'i2x',
'karlitoxz', 'rasputin', 'bender', 'scarlet', 'rapanui', 'dvm',
'edoras', 'atlantis', 'pauloat', 'uchi', 'ealing', 'carioca', 'orion',
'britta', 'andromeda', 'smeagol', 'maxpower', 'dzup', 'threepwood',
'c3p0', 'jara', 'hexodica', 'ExodicaWorld', 'saboteur', 'ponape',
'dojonet', 'cooperativa_libertad', 'nbtrimwork', 'x0r', 'feston',
'medieval', 'perceval', 'barney2', 'kagada', 'amaretto', 'sh4r3m4n',
'hat', 'diablo', 'kelvin', 'haiti', 'retro', 'atom', 'anastasia',
'noanoa', 'libertatia', 'apolo', 'conan', 'victoria', 'jarvis', 'ciego',
'morgana', 'WTF', 'jack', 'arpon', 'fibonacci', 'berreta', 'kaus',
'd0h', 'galleguindio', 'zorak', 'caipiroska', 'tesla', 'rigel', 'pixie',
'relogi' ]

nodes = int(argv[1])
min_links = int(argv[2])
max_links = int(argv[3])

# TODO expandir hosts a cantidad de nodos
if len(hosts) <= nodes:
  print "La cantidad de nodos es mayor a la cantidad de hosts actual"
  exit()

G= nx.Graph()
G.add_nodes_from(range(1, nodes))

# recorremos todos los nodos
for n in G.nodes():
# elegimos al azar la cantidad de enlaces que va a tener
  e = choice(range(min_links,max_links))
  G.node[n]['name'] = hosts[n]

# mientras la cantidad de enlaces sea menor a lo planeado
  while e > len(G.neighbors(n)):
# elegir otro nodo al azar
    i = choice(range(1,nodes))

# y agregar el enlace
    G.add_edge(n, i)

d = json_graph.node_link_data(G)
json.dump(d, open('assets/data/nodes.json','w'))
