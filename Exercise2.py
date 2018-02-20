# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 11:32:51 2018

@author: Qi Suo
"""

import requests
import pandas as pd
url = 'https://en.wikipedia.org/w/index.php?title=Democracy_Index&oldid=820776800'
html = requests.get(url).content
df_list = pd.read_html(html)
df = df_list[-3]
df.columns = df.iloc[0]
df = df[1:]
df.to_csv('my data.csv')
#%%
df.dtypes
#%%
from pandas.api.types import CategoricalDtype
df['Category'] = df['Category'].astype(CategoricalDtype(ordered=True))
#%%
df['Category'].mode()
#%%
toNum=lambda x:pd.to_numeric(x)
democracy=df.iloc[:,2:8].apply(toNum)
democracy.dtypes
#%%
democracy['country'] = df.Country
#%%
print(list(range(democracy.shape[0])))
#%%
for i in range(democracy.shape[0]):
   if democracy.iloc[i,0]<5:
       print(democracy.iloc[i,0])
       democracy.iloc[i,0]=0
#%%
democracy['new']=democracy.Score
for i in range(democracy.shape[0]):
   if democracy.iloc[i,0]<5:
       print(democracy.iloc[i,0])
       democracy.loc[i,'new']=0
   else:
       democracy.loc[i,'new']=1
        
#%%
import matplotlib.pyplot as plt 
pd.plotting.scatter_matrix(democracy,figsize=(12, 12))
plt.show()
#%%
df[['Score', 'Electoral process and pluralism', 'Functioning of government', 'Political participation', 'Political culture', 'Civil liberties']] = df[['Score', 'Electoral process and pluralism', 'Functioning of government', 'Political participation', 'Political culture', 'Civil liberties']].apply(pd.to_numeric)
#%%
plot,dataBP=democracy['Electoral process and pluralism'].plot.box(vert=False,return_type='both')
len([flier.get_xdata() for flier in dataBP["fliers"]][0])
#%%
plot,dataBP2=democracy['Functioning of government'].plot.box(vert=False,return_type='both')
len([flier.get_xdata() for flier in dataBP2["fliers"]][0])
#%%
plot,dataBP3=democracy['Political participation'].plot.box(vert=False,return_type='both')
len([flier.get_xdata() for flier in dataBP3["fliers"]][0])
#%%
plot,dataBP4=democracy['Political culture'].plot.box(vert=False,return_type='both')
len([flier.get_xdata() for flier in dataBP4["fliers"]][0])
#%%
plot,dataBP5=democracy['Civil liberties'].plot.box(vert=False,return_type='both')
len([flier.get_xdata() for flier in dataBP5["fliers"]][0])