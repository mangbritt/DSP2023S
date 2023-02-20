#!/usr/bin/env python
# coding: utf-8

# 1.(A) What is the closest programming language to machine code (i.e., binary code)?
# Assembly
# 
# (B) Does it need interpretation in order to become machine-comprehensible?
# Yes
# 
# 2.(A) Name the oldest high-level programming language that is still in active daily use.
# Fortran
# 
# (B) Approximately how many decades is it old? (±15 years is acceptable answer. the decade it was created is also an acceptable answer)
# 1950's
# 
# 3.(A) Name a second-generation programming language.
# Assembly
# 
# (B) Which language-generation are Fortran, C, C++, MATLAB, Python, R?
# 3rd, 3rd, 3rd, 4th, 4th, 4th
# 
# 4.In what decades C, C++, and MATLAB/Python were created, respectively?
# 70's,80's,90s
# 
# 5.Name an ancestor programming language of C.
# Pascal
# 
# 6.Name a programming language ancestor of C++.
# C
# 
# 7.Name a programming language ancestor of MATLAB and a programming language ancestor of Python.
# Fortran, ABC
# 
# 8.What are the three common types of errors in computer programs? Provide an example for each category.
# Runtime Error-memory leak, Semantic Error-code does not do what is intended, Syntax Error - has to do with syntax
# 
# 9.Which type of bug (error) in coding is the least dangerous kind and easiest to fix? why?
# Syntax, as the code will give an error message when attempting to run.
# 
# 10.Which type of bug (error) in coding is the most dangerous and costly kind? why?
# Semantic, the code will still run but will not show errors.
# 
# 11.Suppose you write a program that has memory leak. What type of programming error you dealing with?
# Runtime Error.
# 
# 12.What is the biggest integer (in base 10) that you could store in an int32 type?
# 2,147,483,647
# 
# 13.What is the difference between int16 and the int64 types?
# int64 can store a much larger integer
# 
# 14.Write a single-line python statement that applies the relevant Python string manipulator methods to this string,
# 
# Python Is Great For String Manipulation.
# and transforms it to the following string and and prints it on screen,
# 
# .noitalupinaM gnirtS roF taerG sI nohtyP
# myString = "Python Is Great For String Manipulation."[::-1]
# 
# 15.Write a single-line python statement that takes the following string,
# 
# Python Is Great For String Manipulation.
# and transforms it to the following,
# 
# .otlpnMgit o ar Inhy
# Hint: Print every other character in reverse, but note that you need to use Python string slicing method.
# myString = "Python Is Great For String Manipulation."[::-2]
# 
# 16.How do you define an empty dictionary?
# myDict = {}
# 
# 17.When an integer overflow happens in Python, what is the expected behavior (what value would be assigned to the overflowed variable)? You may explain with an example.
# The value will go into the other end of the possible range.
# 
# 18.Handling Dictionaries.
# a. Define a Dictionary of all the courses you are taking this semester.
# Use the course numbers as the keys and the course names as the values.
# If you do not know or cannot find the course numbers, use a random number as the key.
# b. Now convert the list of all course numbers to a python list and print it on screen.
# c. Now use a proper command that deletes your least favorite course from the dictionary.
#     Class_Dict={"1000":"DATA","1426":"MATH","1400":"PSYC"}
#     Class_Dict["1000"]
#     resultList = list(Class_Dict.keys())
#     del Class_Dict["1400"]
# 
# 19.Python script full of syntax errors.
# 
# 20.What is the meaning of Value Coercion in Python? Explain with an example.
# The process when a value of one type is changed to another when required. 2.0 * 7 will return 14.0.
# 
# 21.What is the difference between aliasing and copying values in Python?
# Copying makes the value copy directly, aliasing points to the chosen data and will become it when called on.
# 
# 22.What is the difference between a == b and a is b?
#  "==" tests for equality, "is" tests for identity
# 
# Consider the following Python statement.
# a = b = c = [1,2,3]
# Explain what the following command does, what is its output, and why?
# 
# a is b is c
# Test to see if the 3 lists are all the same and since they are, it shows true
# 
# Consider the following Python statement.
# [a,b] = [c,d] = [4,5]
# Explain what the following command does, what is its output, and why?
# It compares the two arrays, it shows false because they are both aliasing from [4,5]

# In[20]:


#Question 19
a1 = 2
b = a1
x = 2
y = x + 4 # is it 6?
import math
print (math.tan(math.pi))
pi = 3.14159
print (math.tan(pi))
c = 4**3**2**3
_ = ((c-78564)/c + 32)
discount = .12
AMOUNT = 120.
amount = 120
address = 'hpl@simula.no'
And = 'duck'
Class = "INF1100, gr 2"
continue_ = x > 0
rev = fox = True
Persian = ['a human language']
true = fox is rev in Persian
#Line checks to see if fox and rev are indentical to each other


# In[ ]:





# In[ ]:




