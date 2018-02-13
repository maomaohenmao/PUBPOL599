# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 09:15:16 2018

@author: Sony
"""

linkAdjMx='https://github.com/EvansDataScience/data/raw/master/dataFigueroa.csv'
#%%
# Getting the matrix (edges):
import pandas

# column 1 will be used as row name: index_col=0
EdgesAsDF = pandas.read_csv(linkAdjMx, index_col=0) 
#%%
EdgesAsDF.shape
#%%
EdgesAsDF['Multinacional']
#%%
varsToDrop=['Multinacional']
adjacency=EdgesAsDF.drop(varsToDrop,axis=1) 

#result
adjacency
#%%
import networkx as net

EliteNet = net.Graph(adjacency) 
#%%
# number of edges:
EliteNet.size()
#%%
# number of  nodes:
len(EliteNet)
#%%
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

net.draw_random(EliteNet,
                node_color='yellow',
                edge_color='lightblue',
                with_labels=True,
                font_size=8)
#%%
# The adjacency matrix did not include the nodes attributes.
EdgesAsDF['Multinacional'].head()
#%%
EliteNet.nodes(data=True)
#%%
dict(zip(EdgesAsDF.index,EdgesAsDF['Multinacional']))
#%%
attributeToAdd=dict(zip(EdgesAsDF.index,EdgesAsDF['Multinacional']))
#%%
net.set_node_attributes(EliteNet, attributeToAdd,'multi')
#%%
EliteNet.nodes(data=True)
#%%
net.is_connected(EliteNet)
#%%
numComponents=net.number_connected_components(EliteNet)
numComponents
#%%
for c in net.connected_components(EliteNet):
    print (c, '\n')
#%%
import matplotlib.pyplot as plt

colorsForComponents = plt.get_cmap('Set2',numComponents).colors

nodesPositions=net.spring_layout(EliteNet,k=0.5)
ConnectedComponents = net.connected_component_subgraphs(EliteNet)

for eachComponent,eachColor in zip(ConnectedComponents,colorsForComponents):
    net.draw(eachComponent,nodesPositions,node_color=eachColor)
#%%
EliteNet_giant = max(net.connected_component_subgraphs(EliteNet), key=len)
#%%
net.draw(EliteNet_giant,with_labels=True)
#%%
# number of edges:
EliteNet_giant.size()
#%%
# number of  nodes:
len(EliteNet_giant)
#%%
net.density(EliteNet_giant) 
#%%
net.diameter(EliteNet_giant)
#%%
# count_zeros=False to make results compatible with R!
net.average_clustering(EliteNet_giant,count_zeros=False)
#%%
# Shorter path (average)
# shows the average number of steps it takes to get from one node to another.

net.average_shortest_path_length(EliteNet_giant)
#%%
net.transitivity(EliteNet_giant)
#%%
net.degree_assortativity_coefficient(EliteNet_giant)
#%%
net.attribute_assortativity_coefficient(EliteNet_giant,'multi')
#%%
# coloring the nodes by attribute:
color_map = plt.get_cmap("cool")
valuesForColors=[n[1]['multi'] for n in EliteNet_giant.nodes(data=True)]
net.draw(EliteNet_giant,node_color=valuesForColors,cmap=color_map,with_labels=True)
#%%
len([a for a in net.enumerate_all_cliques(EliteNet_giant)])
#%%
net.graph_number_of_cliques(EliteNet_giant)
#%%
for a in net.find_cliques(EliteNet_giant):
    print (a)
#%%
net.graph_clique_number(EliteNet_giant)
#%%
[c for c in net.find_cliques(EliteNet_giant) if len(c) == net.graph_clique_number(EliteNet_giant)]
#%%
import community 
parts = community.best_partition(EliteNet_giant)
parts
#%%
net.set_node_attributes(EliteNet_giant, parts,'community')
#%%
pos=net.spring_layout(EliteNet_giant, k=0.2) 
plt.figure(figsize=(8,8))
color_map = plt.get_cmap("cool")
valuesForColors=[n[1]['community'] for n in EliteNet_giant.nodes(data=True)]
net.draw(EliteNet_giant,node_color=valuesForColors,cmap=color_map,with_labels=True,edge_color='lightblue')
#%%
# Computing centrality measures:
degr=net.degree_centrality(EliteNet_giant)  # based on connections count
clos=net.closeness_centrality(EliteNet_giant) # "speed" to access the rest
betw=net.betweenness_centrality(EliteNet_giant,normalized=True) # "control flow" among the network nodes
eige=net.eigenvector_centrality(EliteNet_giant) # central nodes connected to central nodes (influential?)
#%%
# measures into a data frame:
Centrality=[ [rich, degr[rich],clos[rich],betw[rich],eige[rich]] for rich in EliteNet_giant]
headers=['person','Degree','Closeness','Betweenness','Eigenvector']
DFCentrality=pandas.DataFrame(Centrality,columns=headers)
DFCentrality
#%%
fig, ax = plt.subplots(figsize=(10,10))

ax.scatter(DFCentrality.Betweenness, DFCentrality.Closeness,s=(DFCentrality.Degree+1.3)**14,
           c=DFCentrality.Eigenvector,
           cmap=plt.get_cmap('YlOrRd'), alpha=0.6)

valsForAnnotate=zip(DFCentrality['person'],DFCentrality['Betweenness'],DFCentrality['Closeness'])
for name,coordX,coordY in valsForAnnotate:
    ax.annotate(name, (coordX,coordY),alpha=0.5)
    
plt.title("scatterplot (size for degree of node, color for eigenvalue)")
plt.xlabel("betweenness")
plt.ylabel("closeness")
plt.show()
#%%
# degr is a dictionary:
max(degr.keys(), key=(lambda k: degr[k]))

# or you can try:
#DFCentrality['person'].loc[DFCentrality['Degree'].idxmax()]
#%%
# Determine the hub name:
HubNode=max(degr.keys(), key=(lambda k: degr[k]))

# Get ego network of Hub
HubEgonet=net.ego_graph(EliteNet_giant,HubNode)

# prepare to plot:

## positions of the nodes
pos=net.spring_layout(HubEgonet)

## plot whole ego network
net.draw(HubEgonet,pos,node_color='b',node_size=800,with_labels=True, alpha=0.5,node_shape='^')

## make the hub salient
net.draw_networkx_nodes(HubEgonet,pos,nodelist=[HubNode],node_size=2000,node_color='r')

plt.show()
#%%
net.node_connectivity(EliteNet_giant)
#%%
list(net.articulation_points(EliteNet_giant))
#%%
# saving the cut point
cut=list(net.articulation_points(EliteNet_giant))

# positions for all the nodes
pos=net.spring_layout(EliteNet_giant,k=0.5)

# sizes for nodes
SALIENT, NORMAL=(2000,800)

# plot all nodes
net.draw(EliteNet_giant,pos,node_color='b',node_size=NORMAL,with_labels=True, alpha=0.5,node_shape='^')

# make the cut salient:
net.draw_networkx_nodes(EliteNet_giant,pos,nodelist=cut,node_size=SALIENT,node_color='r')
plt.show()
#%%
net.write_graphml(EliteNet, "EliteNetP.graphml",encoding='utf-8')
net.write_gexf(EliteNet, "EliteNetP.gexf",encoding='utf-8')