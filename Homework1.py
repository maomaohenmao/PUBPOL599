<<<<<<< HEAD
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
def badAgeDetector(adataframe):
    import pandas as pd
    wronglist=[]
    for val in adataframe.ages:
        if val < 16 | val > 80:
            wronglist.append(adataframe.names)
    answerAsDicts={'age':adataframe.ages,'name'adataframe.names:wronglist}
    return pd.DataFrame(answerAsDicts)
=======
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

#%%
students.ages
#  test whether the student age is resonable between 16 to 80
#  get the result as students.ages[(students.ages<16) | (students.ages>80)]

#%%
students.ages[(students.ages<16) | (students.ages>80)]

#%%
def badAgeDetector(adataframe):
    import pandas as pd
    wronglist=[]
    for val in adataframe.ages:
        if val < 16 | val > 80:
            wronglist.append(adataframe.names)
    answerAsDicts={'age':adataframe.ages,'name'adataframe.names:wronglist}
    return pd.DataFrame(answerAsDicts)
        
        
>>>>>>> dc9b432e7c4c06ab3e96efe2fa2cb45104a85c9f
