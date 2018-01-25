# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 08:29:17 2018

@author: Sony
"""
import pandas as pd
dataFile='https://github.com/EvansDataScience/data/raw/master/hdi2016.xlsx'
data=pd.read_excel(dataFile)
#%%
data.columns
#%%
data.dtypes
#%%
from pandas.api.types import CategoricalDtype
data['Category']=data['Category'].astype(CategoricalDtype(ordered=True))
#%%
data['Category'].cat.categories
#%%
levels=list(data['Category'].cat.categories) # turn index into a list
newLevels=levels[-1::]+levels[0:1]+levels[2:3]+levels[1:2]
newLevels
#%%
data['Category']=data['Category'].cat.reorder_categories(newLevels)
#%%
%matplotlib inline
import seaborn as sns
sns.pairplot(data.iloc[:,2:6])
#%%
len(data.Country.unique())==len(data.Country)
#%%
data.index=data.Country
#%%
from sklearn import preprocessing

data_scaled = preprocessing.scale(data.iloc[:,2:6])
#%%
# compute similarity matrix:
from scipy.spatial.distance import pdist, squareform

dataSimi_simple = pdist(data_scaled,metric='euclidean') # output is not matrix
dataSimi_matrix =squareform(dataSimi_simple) # this is a matrix
#%%
from scipy.cluster.hierarchy import linkage, cut_tree
# computing the linkage
dataSimi_link = linkage(dataSimi_simple,method='average')
#%%
import seaborn as sns

g = sns.clustermap(data.iloc[:,2:6],
                   metric='euclidean',
                   method='average',
                   col_cluster=False,
                  figsize=(10, 20))
#%%
from sklearn.metrics import silhouette_score
from numpy import ravel

for nOfClusters in range(2,5):
    # get cluster labels
    clusterLabels = ravel(cut_tree(dataSimi_link, nOfClusters)) # formatting cut_tree output with ravel
    # get silhouettes
    silhouette_avg = silhouette_score(dataSimi_matrix,clusterLabels,metric='precomputed')
    
    # print results:
    print("For n_clusters =", nOfClusters, 
          "The average silhouette_score is:", silhouette_avg)
#%%
import numpy as np
from sklearn.metrics import silhouette_samples

clusterLabels3=np.ravel(cut_tree(dataSimi_link, 3))
data['sil3']=silhouette_samples(dataSimi_matrix, clusterLabels3, metric='precomputed')

clusterLabels4=np.ravel(cut_tree(dataSimi_link, 4))
data['sil4']=silhouette_samples(dataSimi_matrix, clusterLabels4, metric='precomputed')
#%%
set(data[data.sil4<0].index)
#%%
set(data[data.sil3<0].index)
#%%
set(data[data.sil4<0].index) & set(data[data.sil3<0].index)
#%%
data['k3']=clusterLabels3
#%%
import matplotlib.pyplot as plt

myPalette = {0 : 'b',1 : 'orange',2 : 'r'}      
myColors = [myPalette[l] for l in data.loc[:,'k3']]

pd.plotting.scatter_matrix(data.iloc[:,2:6],
                           figsize=(16, 16),
                           c=myColors)
plt.show()
#%%
data['k4']=clusterLabels4
#%%
import matplotlib.pyplot as plt

myPalette = {0 : 'b',1 : 'black',2 : 'r', 3 : 'g'}      
myColors = [myPalette[l] for l in data.loc[:,'k4']]

pd.plotting.scatter_matrix(data.iloc[:,2:6],
                           figsize=(16, 16),
                           c=myColors)
plt.show()