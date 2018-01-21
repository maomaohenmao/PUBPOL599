# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 09:16:57 2018

@author: Qi Suo
"""
# link to data, which is in Stata format (dta)
dataURL = "https://github.com/EvansDataScience/data/raw/master/lapopUSA2017_13.dta" 

import pandas as pd
lapop = pd.read_stata(dataURL,convert_categoricals=False) 
#%%
lapop.shape[1]
#%%
# all the questions that begin with 'b'
# this gives you positions
positions1=[i for i, s in enumerate(list(lapop.columns)) if s.startswith('b')]
positions1
#%%
names1=lapop.columns[lapop.columns.str.contains('^b')].tolist()# notice 'tolist()
names1
#%%
# this gives you positions
positions2=[i for i, s in enumerate(list(lapop.columns)) if s.startswith('ros') or s.startswith('media')]
positions2
#%%
# this gives you names
names2=lapop.columns[lapop.columns.str.contains('^ros|^media')].tolist() # notice 'tolist()
names2
#%%
positions=positions1+positions2
names=names1+names2
#%%
lapop[names].info()
#%%
lapop[names].describe()
#%%
lapop[names].plot.box(vert=False,figsize=(12, 12))
#%%
lapop.loc[:,names]=lapop.loc[:,names].fillna(lapop.loc[:,names].median(skipna=True))
#%%
lapop[names].info()
#%%
lapop[names].describe().round(2) # just rounding
#%%
from sklearn.preprocessing import StandardScaler
# Standardizing 
x = StandardScaler().fit_transform(lapop.loc[:, names].values)
#%%
from sklearn.decomposition import PCA
lapopPC = PCA(n_components=3).fit_transform(x)
lapopPCscores = pd.DataFrame(data = lapopPC, columns = ['PC1', 'PC2','PC3'])
lapopPCscores