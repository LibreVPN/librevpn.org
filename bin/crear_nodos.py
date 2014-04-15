#!/usr/bin/env python2
# http://josechristian.com/2013/03/23/random-d3js-network-graph-python-d3js/ 


from random import choice

# start with the number of edges and nodes
int_edges = 150
int_nodes = 100

# location of output file
str_output_file = 'assets/data/nodes.json'

range_edges = range(0,int_edges)
range_nodes = range(0,int_nodes)

# a function to build and print the links
def createLink(int_from,int_to):
	str_from = '\t\t{"source":%d' % int_from
	str_to = '"target":%d}' % int_to
	str_output = ','.join([str_from,str_to])
	return str_output

# a function to make sure we have no loops
def nodesToString(int_from_node,int_to_node):
	if int_from_node != int_to_node:
		str_output_link = createLink(int_from_node,int_to_node)
		return str_output_link
	else:
		if int_from_node==(int_nodes-1):
			str_output_link = createLink(int_from_node-1,int_to_node)
			return str_output_link
		else:
			str_output_link = createLink(int_from_node+1,int_to_node)
			return str_output_link

# open file for writing
file_w_output=open(str_output_file,'w')

# start the node section
file_w_output.write('{\n\t"nodes":[\n')

# print nodes
for n in range_nodes:
	str_node_line = '\t\t{"name":%d}' % n
	if n==int_nodes-1:
		file_w_output.write(str_node_line+'\n\t],\n')
	else:
		file_w_output.write(str_node_line+',\n')

# start the links section
file_w_output.write('\t"links":[\n')

# print links
for i in range_edges:
	int_from_node = choice(range_nodes)
	int_to_node = choice(range_nodes)

	str_link = nodesToString(int_from_node,int_to_node)

	if i == int_edges-1:
		file_w_output.write(str_link+'\n\t]\n}')
	else:
		file_w_output.write(str_link+',\n')

# close files
file_w_output.close()
