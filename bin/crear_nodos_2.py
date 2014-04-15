#!/usr/bin/env python2
# http://josechristian.com/2013/03/23/random-d3js-network-graph-python-d3js/ 

import json
import networkx as nx
from networkx.readwrite import json_graph

G= nx.random_regular_graph(2,10)
for n in G:
  G.node[n]['name'] = n

d = json_graph.node_link_data(G)
json.dump(d, open('assets/data/nodes.json','w'))
