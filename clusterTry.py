# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 08:48:05 2018

@author: Qi Suo
"""
wikiLink = "https://en.wikipedia.org/wiki/Democracy_Index"
#%%
import pandas as pd

wikiTables=pd.read_html(wikiLink,header=0,attrs={'class': 'wikitable sortable',})
#%%
len(wikiTables)
#%%
demodex=wikiTables[0]
demodex.columns
#%%
demodex.dtypes
#%%
try:
    demodex['Category'].cat.categories
except:
    print ('not a category')
#%%    
from pandas.api.types import CategoricalDtype
demodex['Category']=demodex['Category'].astype(CategoricalDtype(ordered=True))
#%%
demodex['Category'].cat.categories
#%%
levels=list(demodex['Category'].cat.categories) # turn index into a list
newLevels=levels[0:1]+levels[-1::]+levels[1:3]
newLevels
#%%
demodex['Category']=demodex['Category'].cat.reorder_categories(newLevels)
#%%
%matplotlib inline
import seaborn as sns
sns.pairplot(demodex.loc[:,'Electoral process and pluralism':'Civil liberties'])
#%%
en(demodex.Country.unique())==len(demodex.Country)
len(demodex.Country.unique())==len(demodex.Country)
#%%
demodex.index=demodex.Country
#%%
demodex.iloc[:,3:8].dtypes
#%%
from sklearn import preprocessing
demodex_scaled = preprocessing.scale(demodex.loc[:,'Electoral process and pluralism':'Civil liberties'])
#%%
from scipy.spatial.distance import pdist, squareform
demoSimi_simple = pdist(demodex_scaled,metric='euclidean') 
demoSimi_matrix =squareform(demoSimi_simple)
#%%
from scipy.cluster.hierarchy import linkage, cut_tree
# computing the linkage
demoSimi_link = linkage(demoSimi_simple,method='average') 
#%%
import seaborn as sns

g = sns.clustermap(demodex.loc[:,'Electoral process and pluralism':'Civil liberties'],
                   metric='euclidean',
                   method='average',
                   col_cluster=False,
                  figsize=(10, 20))
#%%
from sklearn.metrics import silhouette_score
from numpy import ravel

for nOfClusters in range(2,5):
    # get cluster labels
    clusterLabels = ravel(cut_tree(demoSimi_link, nOfClusters)) # formatting cut_tree output with ravel
    # get silhouettes
    silhouette_avg = silhouette_score(demoSimi_matrix,clusterLabels,metric='precomputed')
    
    # print results:
    print("For n_clusters =", nOfClusters, 
          "The average silhouette_score is:", silhouette_avg)
#%%
import numpy as np
from sklearn.metrics import silhouette_samples

clusterLabels3=np.ravel(cut_tree(demoSimi_link, 3))
demodex['sil3']=silhouette_samples(demoSimi_matrix, clusterLabels3, metric='precomputed')
#%%
clusterLabels4=np.ravel(cut_tree(demoSimi_link, 4))
demodex['sil4']=silhouette_samples(demoSimi_matrix, clusterLabels4, metric='precomputed')
#%%
set(demodex[demodex.sil4<0].index)
#%%
set(demodex[demodex.sil3<0].index)
#%%
set(demodex[demodex.sil4<0].index)&set(demodex[demodex.sil3<0].index)
#%%
demodex['k3']=clusterLabels3
#%%
import matplotlib.pyplot as plt

myPalette = {0 : 'b',1 : 'orange',2 : 'r'}      
myColors = [myPalette[l] for l in demodex.loc[:,'k3']]

pd.plotting.scatter_matrix(demodex.loc[:,'Electoral process and pluralism':'Civil liberties'],
                           figsize=(16, 16),
                           c=myColors)
plt.show()