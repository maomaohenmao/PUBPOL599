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
%matplotlib inline

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
