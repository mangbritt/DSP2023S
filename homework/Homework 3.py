#!/usr/bin/env python
# coding: utf-8

# Problem 1

# In[3]:


print(input("Enter your first and last name along with your city, all separated as columns \n").lower().replace(" ",""))


# In[ ]:





# Problem 2

# In[2]:


def dummy(i):
    if i <= 2:
        j = i
    else: j = 'j is not [0,1,2]'
    return j


# Problem 3

# In[27]:


Cdegrees = [-20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40]
print ('    C     F')
#for C in Cdegrees:
#    F = (9.0/5)*C + 32
#    print ('%5d %5.1f' % (C, F))
C=-20
while C <= 40:
    F = (9.0/5)*C + 32
    print ('%5d %5.1f' % (C, F))
    C = C+5


# Problem 4

# In[29]:


numbers = list(range(10))
print(numbers)
for n in numbers:
    i = len(numbers)//2
    del numbers[i]
    print ('n={}, del {}'.format(n,i), numbers)
#i is the length of the numbers list divided by 2 and rounding down, it then removes the number that corresponds to the position in the list.
#


# Problem 5

# In[31]:


eps = 1.0
while 1.0 != 1.0 + eps:
    print (eps)
    eps /= 2.0
print ('final eps:', eps)
# the while loop will continue to run until 1.0 + eps is 1.0
# each instance of the while loop will half the eps until the value is so small that python treats the final addition to be 1.0


# Problem 6

# In[32]:


from math import sqrt
for n in range(1, 60):
    r_org = 2.0
    r = r_org
    for i in range(n):
        r = sqrt(r)
    for i in range(n):
        r = r ** 2
    print ('With {} times sqrt and then {} times **2, the number {} becomes: {:.16f}'.format(n,n,r_org,r))
#The code will take the square root of 2 and then square it, due to rounding errors, it will go into decimals


# Problem 7

# In[13]:


#original code would not run
n = input('Please enter a non-negative integer or type stop: ')
def fib():
    def getFib(n_int):
        if n_int > 1:
            fib = getFib(n_int-1) + getFib(n_int-2);
        elif n_int == 1:
            fib = 1
        else:
            fib = 0
        return fib
    if n=="stop":
        return None
    else:
        StartT = process_time()
        n == int(n);
        print( "fib({}) = {}".format(n,getFib(n)) );
        EndT = process_time
        print("Average runtime: ", EndT, StartT)


# Problem 8

# In[36]:


q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]
resultlist = []
for m in range(len(q)):
    for n in range (len(q[m])):
        resultlist.append(q[m][n])
print(''.join(resultlist))


# In[ ]:





# In[ ]:




