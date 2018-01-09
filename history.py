# -*- coding: utf-8 -*-
# *** Spyder Python Console History Log ***

## ---(Sat Jan  6 14:03:10 2018)---
# one input, and several output in simple data structure:
def factors(number):
    factorsList=[] # empty list that will collect output

    for i in range(1, number + 1):
        #if the remainder of 'number'/'i' equals zero...
        if number % i == 0:
            # ...add 'i' to the list of factors!
            factorsList.append(i)

    return factorsList # returning  values in a list.

factors(-1)
factors(1.3)
factors(-1)
def factors(number):
    
    for i in range(1, number + 1):
        #if the remainder of 'number'/'i' equals zero...
        if number % i == 0:
     print i

    return factors
def factors(number):

    for i in range(1, number + 1):
        #if the remainder of 'number'/'i' equals zero...
        if number % i == 0:
     print(i)

    return factors
def print_factors(x):
   # This function takes a number and prints the factors

   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
           
print_factors(30)
def print_factors(x):
   # This function takes a number and prints the fa
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
           
print_factors(30)
def factors(number):
    factorsList=[] 
    for value in number:
        if value<0:
            print("the value is lower than 0")
        
    for i in range(1, number + 1):
        if number % i == 0:
        factorsList.append(i)
    return factorsList
def factors(number):
    factorsList=[] 
    for value in number:
        if value<0:
            print("the value is lower than 0")
        if value>0:
            for i in range(1, number + 1):
                 if number % i == 0:
                    factorsList.append(i)
return factorsList
def factors(number):
    factorsList=[] 
    for value in number:
        if value<0:
            print("the value is lower than 0")
        if value>0:
            for i in range(1, number + 1):
                 if number % i == 0:
                    factorsList.append(i)
                          return factorsList
def factors(number):
    factorsList=[] 
    for value in number:
        if value<0:
            print("the value is lower than 0")
            continue
        if value>0:
            for i in range(1, number + 1):
                 if number % i == 0:
                    factorsList.append(i)
                          return factorsList
def factors(number):
    factorsList=[] 
    for value in number:
        if value<0:
            print("the value is lower than 0")
            continue
        if value>0:
            for i in range(1, number + 1):
                 if number % i == 0:
                    factorsList.append(i)
return factorsList
def factors(number):
    factorsList=[] 
    for value in number:
        if value<0:
            print("the value is lower than 0")
            continue
        if value>0:
            for i in range(1, number + 1):
                 if number % i == 0:
                    factorsList.append(i)
        return factorsList
    
factors(15)
def factors(number):
    factorsList=[] 
    for value in number:
        if value<0:
            print("the value is lower than 0")
            continue
        if value>0:
            for i in range(1, number + 1):
                 if number % i == 0:
                    factorsList.append(i)
    return factorsList

factors(15)
factors(20)
def factors(number):
    factorsList=[] 
    for value in number:
        if value<0:
            print("the value is lower than 0")
            continue
        for i in range(1, number + 1):
            if number % i == 0:
                factorsList.append(i)
        return factorsList
    
factors(20)
  def factors(number):
    factorsList=[]
    for i in range(1, number + 1):
        if number % i == 0:
            factorsList.append(i)
    return factorsList

factors(20)
factors(-20)
def factors(number):
    factorsList=[] 
    for value in number:
        if value<0:
            print("the value is lower than 0")
            
factors(-2)
def factors(numbers):
    factorsList=[] 
    for value in numbers:
        if value<0:
            print("the value is lower than 0")
            
factors(numbers)
factors(-10)

## ---(Sat Jan  6 14:38:42 2018)---
def factors(number):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
           
factors(30)
def factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
           
factors(30)
factors(0)
def factors(x):
    for x: # notice the order of 'IFs'
        if x==None: # condition1
            print ('missing values as input')
            continue
        if isinstance(x, str): #condition2
            print ('string as input')
            continue
        if x <= 0: # condition3
            print ('invalid value as input')
            continue
        if x > 0
def factors(x):
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
           
factors(15)
factors(-5)
def factors(x):
   for i in range(abs(x)-1, x + 1):
       if x % i == 0:
           print(i)
           
factos(-5)
factors(-5)
def factors(x):
   for i in range(-abs(x)-1, x + 1):
       if x % i == 0:
           print(i)
           
factors(-5)
def factors(x):
   for i in range(-abs(x)-1, abs(x) + 1):
       if x % i == 0:
           print(i)
           
factors(-20)

## ---(Sat Jan  6 14:57:02 2018)---
def factors1(x):
   for i in range(-abs(x)-1, abs(x) + 1):
       if x % i == 0:
           print(i)
           
factors1(-5)
def factors1(x):
   for i in range(-abs(x)-1,0) & (0, abs(x) + 1):
       if x % i == 0:
           print(i)
           
factors1(-5)
def factors1(x):
   for i in range(-abs(x)-1,0):
       if x % i == 0:
           print(i)
   for i in range(0, abs(x)+1):
       if x % i == 0:
           print(i)
           
factors1(-5)
def factors1(x):
   for i in range(-abs(x)-1,-1):
       if x % i == 0:
           print(i)
   for i in range(1, abs(x)+1):
       if x % i == 0:
           print(i)
           
factors1(-5)
factors1(-20)
def factors1(x):
   for i in range(-abs(x)-1,0):
       if x % i == 0:
           print(i)
   for i in range(1, abs(x)+1):
       if x % i == 0:
           print(i)
           
factors1(-20)
def factors1(x):
   factorsList1=[] 
   for i in range(-abs(x)-1,0):
       if x % i == 0:
           factorsList1.append(i)
   for i in range(1, abs(x)+1):
       if x % i == 0:
           factorsList.append(i)
   return factorsList1

factors1(-20)
def factors1(x):
   factorsList1=[] 
   for i in range(-abs(x)-1,0):
       if x % i == 0:
           factorsList1.append(i)
   for i in range(1, abs(x)+1):
       if x % i == 0:
           factorsList1.append(i)
   return factorsList1

factors1(-20)
factors1(0)
def factors1(x):
   factorsList1=[] 
   for x==0:
       print('All the numbers are factors of 0')
   for i in range(-abs(x)-1,0):
       if x % i == 0:
           factorsList1.append(i)
   for i in range(1, abs(x)+1):
       if x % i == 0:
           factorsList1.append(i)
   return factorsList1
def factors1(x):
   factorsList1=[] 
   for x=0:
       print('All the numbers are factors of 0')
   for i in range(-abs(x)-1,0):
       if x % i == 0:
           factorsList1.append(i)
   for i in range(1, abs(x)+1):
       if x % i == 0:
           factorsList1.append(i)
   return factorsList1

## ---(Sat Jan  6 16:02:35 2018)---
def factors1(x):
   factorsList1=[]
   if x != 0:
       for i in range(-abs(x)-1,0):
           if x % i == 0:
               factorsList1.append(i)
       
       for i in range(1, abs(x)+1):
           if x % i == 0:
               factorsList1.append(i)
       return factorsList1
   elif x = 0:
       print('All other numbers are the facters of 0')
def factors1(x):
   factorsList1=[]
   if x != 0:
       for i in range(-abs(x)-1,0):
           if x % i == 0:
               factorsList1.append(i)
       
       for i in range(1, abs(x)+1):
           if x % i == 0:
               factorsList1.append(i)
       return factorsList1
   elif x == 0:
       print('All other numbers are the facters of 0')
       
factors1(-20)
factors1(0)
factors1(20)
def factors1(x):
   factorsList1=[]
   if x < 0:
       for i in range(-abs(x)-1,0):
           if x % i == 0:
               factorsList1.append(i)
       return factorsList1
   if x == 0:
       print('All other numbers are the facters of 0')
   elif x > 0:
       print('invalid number')
       
factors1(-10)
factors1(10)
factors1(0)
def factors1(x):
   factorsList1=[]
   if x > 0
       for i in range(-abs(x)-1,0):
           if x % i == 0:
               factorsList1.append(i)
       for i in range(1, abs(x)+1):
           if x % i == 0:
               factorsList1.append(i)
       return factorsList1
   elif x <= 0:
       print('invalid number')
def factors1(x):
   factorsList1=[]
   if x > 0:
       for i in range(-abs(x)-1,0):
           if x % i == 0:
               factorsList1.append(i)
       for i in range(1, abs(x)+1):
           if x % i == 0:
               factorsList1.append(i)
       return factorsList1
   elif x <= 0:
       print('invalid number')
       
def factors1(x):
   factorsList1=[]
   if x > 0:
       for i in range(-abs(x)-1,0):
           if x % i == 0:
               factorsList1.append(i)
       for i in range(1, abs(x)+1):
           if x % i == 0:
               factorsList1.append(i)
       return factorsList1
   elif x <= 0:
       print('invalid number')def factors1(x):
   factorsList1=[]
   if x > 0:
       for i in range(1,x + 1):
           if x % i == 0:
               factorsList1.append(i)
       return factorsList1
   elif x < 0:
       print('invalid number')
def factors1(x):
   factorsList1=[]
   if x > 0:
       for i in range(1,x + 1):
           if x % i == 0:
               factorsList1.append(i)
       return factorsList1
   elif x < 0:
       print('invalid number')
       
factors1(0)
def factors1(x):
   factorsList1=[]
   if x > 0:
       for i in range(1,x + 1):
           if x % i == 0:
               factorsList1.append(i)
       return factorsList1
   elif x <= 0:
       print('invalid number')
       
factors1(0)
factors1(0)10
factors1(10)
factors1(-10)
def factors1(x):
  factorsList1=[]
  if x > 0:
      for i in range(1,x + 1):
          if x % i == 0:
              factorsList1.append(i)
      return factorsList1
  if x==None: # condition1
      print ('missing values as input')
      continue
  if isinstance(x, str): #condition2
      print ('string as input')
      continue
  if x <= 0: # condition3
      print ('negative value as input')
def factors1(x):
  factorsList1=[]
  if x > 0:
      for i in range(1,x + 1):
          if x % i == 0:
              factorsList1.append(i)
      return factorsList1
  if x==None: # condition1
      print ('missing values as input')
  if isinstance(x, str): #condition2
      print ('string as input')
  if x <= 0: # condition3
      print ('negative value as input')
      
factors1(-10)
factors1(0)
factors1()
factors1("-10")
def factors1(x):
  factorsList1=[]
  if x==None: # condition1
      print ('missing values as input')
  if isinstance(x, str): #condition2
      print ('string as input')
  if x <= 0: # condition3
      print ('negative value as input')
  if x > 0:
      for i in range(1,x + 1):
          if x % i == 0:
              factorsList1.append(i)
      return factorsList1
  
factors1()
factors1('12erer')
def factors1(x):
  factorsList1=[]
  for x:
  if x==None:
      print ('missing values as input')
  if isinstance(x, str):
      print ('string as input')
  if x <= 0:
      print ('negative value as input')
  if x > 0:
      for i in range(1,x + 1):
          if x % i == 0:
              factorsList1.append(i)
      return factorsList1
factors1(None)