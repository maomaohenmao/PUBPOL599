# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 15:48:44 2018

@author: Sony
"""
namesList=["Qing", "Françoise", "Raúl", "Bjork","Jim", "Peter","Maria","Rosita"]
agesList=[32,-33,28,30,21,3,21,190]
countryList=["China", "Senegal", "Spain", "Norway", "Peru", "Chile","Venezuela","Singapur"]
educationList=["Bach", "Bach", "Bach", "PhD","Master","Master","PhD","Bach"]

#%%
data={'names':namesList, 'ages':agesList, 'country':countryList, 'education':educationList}
data

import pandas as pd
students=pd.DataFrame.from_dict(data)
students

#%% algorithm thinking
#  read the data frame
#  get the age from the data
#  save the age in an object
#  define age make sense limits
#  read each value
#  and check in a loop
#  show me those bad ages

#%%
students.ages[(students.ages<10) | (students.ages>80)]

#%%
guyages=students['ages']
for value in guyages:
    if (value >= 10) and (value <=80):
        print ('good value')
    else: 
        print('bad value',value)
        
#%%
guyages=students['ages']
for value in guyages:
    if (value >= 10) and (value <=80):
        print ('good value')
    else:
        print(students[students['ages']==value])
        
#%%
# The function needs these fields as inputs:
# DF is the dataframe
# ageColumnName is the name of the column of ages
# namesColumName is the name of the column of names
# lowT and upT are the thresholds

def badAgeDetector(DF,ageColumnName,namesColumName,lowT=10,upT=80):  # Read all the data
    
    goodAges=range(lowT,upT+1) # Assume a lower and upper threshold
    
    # subset the original DF:keep the rows whose ages are NOT good
    DFdetected=DF[~DF[ageColumnName].isin(goodAges)] # this style replaces 'for' and 'if'
    
    return DFdetected[namesColumName] # return the names: you are returning a pandas "series" (like a list)

badAgeDetector(DF=students,ageColumnName='ages',namesColumName="names")
#%%
def badAgeDetector2(DF,ageColumnName,namesColumName,lowT=10,upT=80):
    goodAges=range(lowT,upT+1)
    DFdetected=DF[~DF[ageColumnName].isin(goodAges)]
    return DFdetected[[namesColumName]] # The extra [] create a dataframe

badAgeDetector2(DF=students,ageColumnName='ages',namesColumName="names")
#%%
def badAgeDetector3(DF,ageColumnName,namesColumName,lowT=10,upT=80):
    goodAges=range(lowT,upT+1)
    DFdetected=DF[~DF[ageColumnName].isin(goodAges)]
    return DFdetected[[namesColumName,ageColumnName]] # here was the change.

badAgeDetector3(DF=students,ageColumnName='ages',namesColumName="names")
#%%
def badAgeDetector4(DF,ageColumnName,namesColumName,lowT=10,upT=80):
    guyages=DF[ageColumnName]
    goodAges=list(range(lowT,upT+1))
    DFdetected=DF[~DF[ageColumnName].isin(goodAges)]
    return DFdetected

badAgeDetector4(DF=students,ageColumnName='ages',namesColumName="names")