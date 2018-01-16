# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%% # one input, and several output in simple data structure:
def factors(number):
    factorsList=[] # empty list that will collect output
    
    for i in range(1, number + 1):
        #if the remainder of 'number'/'i' equals zero...
        if number % i == 0:
            # ...add 'i' to the list of factors!
            factorsList.append(i)

    return factorsList # returning  values in a list.

#%% def print_factors(x):
   # This function takes a number and prints the factors
def factors1(x):
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
           
#%%
def factors2(x):
   factorsList2=[]
   if x < 0:
       for i in range(-abs(x)-1,0):
           if x % i == 0:
               factorsList2.append(i)
       return factorsList2
   if x == 0:
       print('All other numbers are the facters of 0')
   elif x > 0:
       print('invalid number')
       
#%% 
def factors2s(x):
   factorsList2s=[]
   if x != 0:
       for i in range(-abs(x)-1,0):
           if x % i == 0:
               factorsList2s.append(i)
       for i in range(1, abs(x)+1):
           if x % i == 0:
               factorsList2s.append(i)
       return factorsList2s
   elif x == 0:
       print('All other numbers are the facters of 0')
    
#%%
def factors3(x):
   factorsList3=[]
   if x > 0:
       for i in range(1,x + 1):
           if x % i == 0:
               factorsList3.append(i)
       return factorsList3
   elif x <= 0:
       print('invalid number')

    
 #%%
def factors4(x):
   factorsList4=[]
   if x==None:
       print ('missing values as input')
   if isinstance(x, str):
       print ('string as input')
   if x <= 0:
       print ('negative value as input')
   if x > 0:
       for i in range(1,x + 1):
           if x % i == 0:
               factorsList4.append(i)
       return factorsList4