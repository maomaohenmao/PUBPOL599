# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 09:12:17 2018

@author: Qi Suo
"""

#this is my token, get yours:
token='&$$app_token=4womkelHXIsox0I8jMpUyNRRF'

#this is the endpoint:
endpoint="https://data.wa.gov/resource/74eq-kst5.json?"

#subsetting at API:
filters='&jurisdiction_type=Statewide'
sqlQueries='&$where=election_year >= 2012'
limit='$limit=4000000'

#building url:
urlLink = endpoint+limit+filters+token
#%%
import requests

#get the data:
response = requests.get(urlLink)
if response.status_code == 200:
    dataContri = response.json() # data will come as JSON format.
#%%
type(dataContri)
#%%
dataContri[0] # first row
#%%
import pandas as pd

contributions = pd.DataFrame(dataContri)
#%%
contributions.columns
#%%
contributions=contributions[['contributor_state','contributor_zip','amount','election_year','party']]
#%%
contributions.dtypes
#%%
# coerce will put a missing value where a conversion to numeric is not possible:
contributions.amount=pd.to_numeric(contributions.amount, errors='coerce')
#%%
contributions.contributor_state.value_counts()
#%%
WASzip=contributions[contributions.contributor_state=='WA']
#%%
WASzip.reset_index(inplace=True,drop=True) # good practice
#%%
'985'>'9800'
#%%
WASzip.contributor_zip[0] #the first value
#%%
valueAsInt=[]
for value in WASzip.contributor_zip:
    try:
        valueAsInt.append(int(value))
    except:
        valueAsInt.append(None)
#%%
#valueAsInt will be transformed to a pandas series
replacingSeries=pd.Series(valueAsInt,dtype='object') # other than 'object' I get decimals

# I used the same name to replace 'contributor_zip' , thus replacing that old column:
WASzip = WASzip.assign(contributor_zip=replacingSeries)
#%%
WASzip=WASzip[(WASzip.contributor_zip <=99403) & (WASzip.contributor_zip>=98001)]
#%%
WASzip.contributor_zip.describe()
#%%
# I do this to make sure index 0 is in the data (it may have dropped during sub setting above)
WASzip.reset_index(inplace=True,drop=True)

WASzip.contributor_zip[0]
#%%
WASzip.dropna(axis=0,inplace=True) # axis=0 is for delete by row.
#%%
WASzip.head()
#%%
WASzip.reset_index(inplace=True,drop=True)
#%%
numericColumns =["amount"]
aggregateBY=['contributor_zip']

#'as_index = False' avoids that the column of zip codes becomes a row name: 
WA_zip_contri=WASzip.groupby (aggregateBY, as_index = False)[numericColumns].sum()

#see result:
WA_zip_contri.head()
#%%
compressedMap= 'https://github.com/EvansDataScience/data/raw/master/WAzips.zip'
#%%
import geopandas as gpd
#%%
wazipMap = gpd.GeoDataFrame.from_file(compressedMap)
#%%
wazipMap.head()
#%%
wazipMap.ZCTA5CE10.dtype
#%%
WA_zip_contri.contributor_zip.dtype
#%%
wazipMap.ZCTA5CE10=wazipMap.ZCTA5CE10.astype(int)
#%%
contribWAmap=wazipMap.merge(WA_zip_contri, left_on='ZCTA5CE10', right_on='contributor_zip')
#%%
contribWAmap.shape[0]
#%%
wazipMap.shape[0]
#%%
#install matplotlib
#pip install descartes
%matplotlib inline
base = wazipMap.plot(color='black',figsize=(20,13))

contribWAmap.plot(ax=base, color='pink')
#%%
#NOW that you are in maps, make sure column names are not longer than 10 characters
contribWAmap['contribDen']=contribWAmap.amount/contribWAmap.POP2017
#%%
contribWAmap['contribDen'].describe()
#%%
#finding the issue:
import numpy as np

contribWAmap[contribWAmap['contribDen']==np.inf][['contribDen']]
#%%
contribWAmap=contribWAmap[contribWAmap['contribDen']!=np.inf]
#%%
contribWAmap['contribDen'].describe()
#%%
base = wazipMap.plot(color='red',figsize=(20,13))

contribWAmap.plot(ax=base,column='contribDen',cmap='YlGnBu',scheme='Quantiles',k=5,legend=True)
#%%
import matplotlib.pyplot as plt

base = wazipMap.plot(color='red',figsize=(20,13))

topLayer=contribWAmap.plot(ax=base,column='contribDen',cmap='YlGnBu',scheme='Quantiles',k=5,legend=True,
                  legend_kwds={'loc': 3,'title':'Contribution rate: \n (red missing)'})
topLayer.set_title('Contribution towards candidates in WA since 2012 per zip code', 
                   color='black',fontdict={'fontsize':30})
leg = topLayer.get_legend()
plt.setp(leg.get_title(), multialignment='center')
plt.show()
#%%
cd
#%%
contribWAmap.to_file(driver = 'ESRI Shapefile', filename= "contribWAmap.shp")
#%%
# LINK

wikiLink = "https://en.wikipedia.org/wiki/Democracy_Index" # Location

# SCRAPING VIA PANDAS

import pandas as pd

wikiTables=pd.read_html(wikiLink,header=0,attrs={'class': 'wikitable sortable',})

# index 0 is the first element!
demodex=wikiTables[0]
#%%
list(demodex.Category.value_counts().index)
#%%
from pandas.api.types import CategoricalDtype

goodOrderCat=['Authoritarian','Hybrid regime','Flawed democracy', 'Full democracy']
demodex.Category=demodex.Category.astype(CategoricalDtype(categories=goodOrderCat, 
                                         ordered=True))
#%%
demodex.dropna(inplace=True)
#%%
compressedMap2='https://github.com/EvansDataScience/data/raw/master/worldMap.zip'
worldMap = gpd.GeoDataFrame.from_file(compressedMap2)
#%%
worldMap.head()
#%%
worldMap.dtypes
#%%
worldMapDem=worldMap.merge(demodex,left_on='NAME', right_on='Country')
#%%
# where is the missing countries:

base = worldMap.plot(color='black',figsize=(20,13),edgecolor='black')

worldMapDem.plot(ax=base, color='pink')
#%%
base = worldMap.plot(color='black',figsize=(20,13),edgecolor='black')

worldMapDem.plot(ax=base,column='Category',cmap='Set2',categorical=True,legend=True)
#%%
list(zip(worldMapDem.Category.cat.codes,worldMapDem.Category))
#%%
# I need str(x) because 'x' is a number, and numbers and text can not be concatenated with '+':
# zip is used to make parallel pairs:
[str(x)+'.'+y for (x,y) in zip(worldMapDem.Category.cat.codes+1,worldMapDem.Category)]
#%%
worldMapDem['Category2']=[str(x)+'.'+y for (x,y) in zip(worldMapDem.Category.cat.codes+1,worldMapDem.Category)]
#%%
base = worldMap.plot(color='black',figsize=(20,13),edgecolor='black')
worldMapDem.plot(ax=base,column='Category2',cmap='Set2',categorical=True,legend=True)
#%%
base = worldMap.plot(color='black',figsize=(20,13),edgecolor='black')
topLayer=worldMapDem.plot(ax=base,column='Category2',cmap='Set2',categorical=True,legend=True,
                  legend_kwds={'loc': 6,'title':'Democracy Level: \n (black missing)'})
topLayer.set_title('How democracy is spread around the world (2016)', 
                   color='black',fontdict={'fontsize':30})
leg = topLayer.get_legend()
plt.setp(leg.get_title(), multialignment='center')
plt.show()