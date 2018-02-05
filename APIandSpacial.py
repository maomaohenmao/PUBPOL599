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
