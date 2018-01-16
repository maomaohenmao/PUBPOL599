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
print(df)
df.columns = df.iloc[0]
df = df[1:]
df.to_csv('my data.csv')
#%%
df.dtypes
df['Category'].mode()
#%%
toNum=lambda x:pd.to_numeric(x)
democracy=df.iloc[:,3:8].apply(toNum)
democracy.dtypes
#%%
pd.plotting.scatter_matrix(democracy,figsize=(12, 12))
plt.show()
#%%
plot,dataBP=democracy['Electoral process and pluralism'].plot.box(vert=False,return_type='both')
[value.get_xdata() for value in dataBP["boxes"]]
#%%
[value.get_xdata() for value in dataBP["caps"]] 
df['Electoral process and pluralism'].max()