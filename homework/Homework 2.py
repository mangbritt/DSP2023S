#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np
#1\2 wrong operator
1/2 #Divides 1 by 2 and sets as float
print(np.uint8(1/2)) #sets output range to 8-bit integer
print(np.uint8(1/3)) #sets output range to 8-bit integer
print(-5^2) #Uses xor operator and makes negative
print(-5**2) #Squares 5 and makes negative
print((-5) ^2) #Uses xor operator and makes negative
print((-5)**2) # Squares negative 5
print(10-6/2) # divides 6 by 2, then subtracts from 10
print(5*4/2*3) # Multiplies 5 by 4, then divide by 2 then multiplies by 3


# Overflow. What would happen if you went beyond the range for a particular type? For example, the largest integer that can be stored in int8 is 127, and the smallest integer is -128, so what would happen if we type cast a larger integer to the type int8? Smaller integer? Use the MATLAB built-in functions intmin and intmax or Python’s numpy package command iinfo to find the largest and smallest integers that can be stored in int16 and int32.

# In[29]:


import numpy as np
np.int8(-130) #Going over 127 overflows into negative, going below -128 overflows to positive
ii16 = np.iinfo(np.int16)
print(ii16.min)
print(ii16.max)#Going over 32,767 overflows into negative, going below -32,768 overflows to positive
ii32 = np.iinfo(np.int32) 
print(ii32.min)
print(ii32.max)#Going over 2,147,483,647 overflows into negative, going below -2,147,483,648 overflows to positive


# In[43]:


import numpy as np
a = 1 #sets a as 1
b = 'x' #sets b as "x" string
c = True #makes c true
whos a b c #Finds type of a b c
a == c #makes a equal to c
a + c #adds a and c
d = [1, 2, 3, 4] #Makes list
e = ['a' 'b' 'c' 'd'] #makes one line list
f = ['a', 'b', 'c', 'd'] #makes multiline list
g = ['abcd'] #Makes into one part list
h = {'a' 'b' 'c' 'd'} #Makes into dictionary object
i = {a b c d}#Makes into dictionary object
whos d e f g h i #Finds type of d e f g h i
class(a) #Creates class named a
type(a) #Finds what the class of a is
True #Makes a variable true
true #bad syntax
False #Makes variable false
false #Bad syntax


# In[56]:


#part a
a = 5
b = a
print(id(a), id(b))

c = b
b = 3
print(a,b,c)
print(id(a), id(b), id(c))

b = a
b = 5
print(id(a), id(b))
#id() returns unique integer for every unique value

#part b
a = [5]
b = a
print(id(a),id(b))

b.append(1)
print(a,b)
print(id(a), id(b))
#append adds an element to the list made by []

#part c
a = [5]
b = list(a)
print(a,b)
print(id(a),id(b))
#list(a) creates a copy and are not the same list

#part d
a = (5,)
b = tuple(a)
print (id(a),id(b))

b = a[:]
print (id(a),id(b))
#the lists are the same so the id is the same


# In[75]:


#Question 4
a1 = 2 #1a is not variable
b = a1 #b was not yet defined
x = 2
y = x + 4 # is it 6? #x needs to match case with x above
import math #need to import math
c = math.pi
print (math.tan(c)) #importing math has pi listed
c = 4**3**2**3
_ = ((c-78564)/c + 32)
discount = .12 #% is modulus operator
AMOUNT = 120 # - is subtracting
amount = 120 # $ is illegal operator
address = "hpl@simula.no"
And = "duck"
Class = "INF1100, gr 2" #Must be strings
continue_ = x > 0
rev = fox = True
Persian = ['a human language']
true = fox is rev in Persian


# In[121]:


#Question 5
get_ipython().system("# \\usr\\bin\\env 'python'")

print("The life expectancy for the millennials is projected to be {life_expectancy} years! (But don't believe it...)".format(life_expectancy = 120))

print("A recent study published in the journal of Nature, discovered that over the past century,"
    "although the life expectancy has significantly increased due to technological advances,"
    "the maximum life span of the oldest people in the world has not changed much.")

from cmath import sqrt # cmath function always return complex numbers
from math import sqrt # math function always work with and return real numbers
print ("""
Cardano was the first to introduce complex numbers of the form a + sqrt(-b) into algebra, but he had misgivings about it. \

In his solution to an algebra equation he encountered the solution 5 + sqrt(-15) for the unknown, which is now mathematically represented by \n \n \
      {first} \n\nin Python, which can also be obtained as an addition of real and imaginary numbers in Python like this \n\n\
      
      5 + sqrt(-15) = {second}, \n\n
      which can also be manually stated as 
      
      
      {third} \n

\
""".format( second=complex(5,-15) , first=5+ cmath.sqrt(-15) , third=5+3.872983346207417j ) )

print('''

One final note: \n
\tIn python the sqrt function from math and cmath modules are different.
\tThe sqrt function that returns "float" results is sqrt from math module.
\tTherefore, if using math module, then,

\t\tsqrt(25) = {:.4f}, 

\twhich is obviously a float (real number).

''' .format(sqrt(25)) 
)

print('''

Also note that by convention, 0**0 = {first:d} in Python.
And division by 0, will give you a runtime exception: 1/0 = {second:}

''' .format(first=0**0,second=1/0) 
)


# In[ ]:





# In[ ]:




