#!/usr/bin/env python
# coding: utf-8

#  # <center>Final Exam &ndash; DATA 3401 (Spring 2023)</center>
# 
# ## Start Date: 5/5
# ## Due Date: 5/8 (at 11:59pm) &ndash; this is a hard deadline so don't miss it!
# 
# ## Final Rules
# This final exam is simliar to the midterm exam. Please work the exercises below **on your own**.  When you have completed the exam, you should push your completed jupyter notebook to your GitHub repo for this class in the **Exams->Final** folder.
# 
# You may not discuss the problems with **anyone else**, including persons on an online internet forum. Consulting an outside source like this will be considered an academic integrity violation. **Any questions should be referred to me.**
# 
# You may use all class resources including previous labs and lectures, and anything posted on the course website or Teams.
# 
# You may not use any function that trivializes a problem. For example, if I ask you to write a `max` function that computes the maximum entry in a list, you are not allowed to use the pre-defined Python function `max`; you must write your own.
# 
# 

# ## Exercise 1 (25 points)
# In this exercise you will be working with the files abalone.names and abalone.data in the Final Exam folder.
# 
# 1. Open the abalone.names file in your notebook. Using the information there, in a new cell briefly describe the data set and relevant features.
# 1. Load the abalone.data file into a dataframe using pandas. Print the .head() of the dataframe
# 1. Using the .names file, **add** a header line to your dataframe describing each column of data
# 1. Take the last column and make a new dataframe called `labels`
#     1. Print out the value counts of each label.
#     1. What do you notice about the distribution of the labels?
#     1. Based on your observations, propose a way to modify the labels to consolidate some of the classes, and do this modification (you should describe in comments in your code what change you are making)
#     1. After making your modification, show the value counts of the new labels again
# 1. Make a scatterplot of each feature against the others (it should be a single plot)
#     1. Describe any trends or correlations that you see.
# 

# In[4]:


## Write your code here
f = open("abalone.names",'r')
print(f.read())


# In[ ]:


#The data set measures abalone through many features to predict the age, primarily from rings in the shell. Other features 
#include sex, length, diameter, height, whole weight, shucked weight, gut weight and shell weight.


# In[61]:


import pandas as pd

# Load data and add column names
ab_data = pd.read_csv("abalone.data", header=None)
ab_data.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole Weight', 'Shucked Weight', 'Viscera Weight', 'Shell Weight', 'Rings']


ab_data['Class Range'] = pd.cut(count, bins=[0, 5, 10, 15, 20, 25, 29])

# Count the number of examples in each range
count = ab_data['Class Range'].value_counts().sort_index()

# Display the distribution
print("Class Distribution")
print("------------------")
for i in range(len(count)):
    label = count.index[i]
    examples = count.values[i]
    print("{}: \t{}".format(label, examples))


# ## Exercise 2: (20 points)
# 
# 
# Consider that a person is standing on the real line at a given point $x_0$. The person then goes on a "random walk", meaning that they first take a step of size 1 in a random direction (so after this step they are either standing at $x_0+1$ or $x_0-1$), then they take another step of size 1 in a random direction (after the second step they are standing at one of $x_0-2,  x_0, $ or  $x_0+2$), and they continue this process for $n$ steps. At each stage, the person flips a fair coin to decide which direction to go in.
# 1. Write a function `RandomWalk(num_steps,start_position)`, that takes the number of steps `num_steps` for a random walk and the `start_position` of the random walk on the real line (so a float), and returns the location of the final step of the random walker.
# 2. Write another function `SimulateRandomWalk(num_sims,num_steps,start_position)` that simulates num_sims number of random walks, each of which contains `num_steps` steps and starts at `start_position`. Then, this function calls `RandomWalk()` repeatedly for `num_sims` times and finally returns a vector of size `num_sim` containing the final locations of all of the `num_sims` simulated random-walks.
# 3. Now write a script that plots the output of `SimulateRandomWalk(num_sims = 10000, num_steps = 100, start_position = 0)` in a histogram
# 4. Repeat step 3 for `num_steps` = 1000, 5000
# 

# In[12]:


## Write your code here
import random
import numpy as np
import matplotlib.pyplot as plt

def RandomWalk(num_steps, start_position):
    position = start_position
    for i in range(num_steps):
        direction = random.choice([-1, 1])
        position += direction
    return position

def SimulateRandomWalk(num_sims, num_steps, start_position):
    final_positions = []
    for i in range(num_sims):
        final_position = RandomWalk(num_steps, start_position)
        final_positions.append(final_position)
    return np.array(final_positions)

# Simulate random walks and plot histograms
num_sims = 10000
start_position = 0
for num_steps in [100, 1000, 5000]:
    final_positions = SimulateRandomWalk(num_sims, num_steps, start_position)
    plt.hist(final_positions, bins=20, density=True, alpha=0.5, label=f'Num Steps = {num_steps}')
plt.legend()
plt.title(f'Histogram of Final Positions After {num_sims} Random Walks')
plt.xlabel('Final Position')
plt.ylabel('Density')
plt.show()


# ## Exercise 4: (15 Points)
# 
# Consider the problem of projectile motion that we solved in class and we calculated the **height** of the motion (or in the Y-direction). Here is the class we defined for the projectile, (**Note** I renamed the **getHieght** method (function) to **getLocY**, which is a *method* (a function) to calculate the Y-component of the location):

# In[13]:


class ProjLocY():  
    def __init__(self, velInitY, g = 9.8):  
        self.velInitY = velInitY # initial velocity along the y direction.  
        self.gravityConstant = g # gravityConstant, 9.81 on earth.  
    def getLocY(self, time):  
        """  
        Return the location of the projectile at the specific given `time` and initial velocity.  
        Input  
            time    :   An input real (float) representing the time  
                        past since the start of the projectile motion.  
        """  
        return self.velInitY * time - 0.5 * self.gravityConstant * time**2  
    
    def evaluate(self, time): 
        return self.getLocY(time)  


# 1. Now, define a similar class for projectile motion in the x direction.
# (Note: Recall the projectile motion along the x direction does not involve acceleration.)
# 
# 1. Define a subclass that inherits the properties of the projectiles in x and y directions from the corresponding super (parent) classes (```ProjLocX``` and ```ProjLocY```).
# 
# 1. In addition to the inherited methods (functions), this new subclass must contain a ```evaluate(self, time)``` method which computes and returns the location (x,y) of the projectile by calling and aggregating information from the corresponding methods of the parent classes ```getLocX(time)``` and ```getLocY(time)```.
# 
# 1. Compute and return the location of the projectile in X-Y plane for initial velocities (10, 10) meters / sec at time 1 sec since the start of the projectile.
# 

# In[15]:


# Write your code here
class ProjLocX:
    def __init__(self, init_vel_x, init_pos_x):
        self.init_vel_x = init_vel_x
        self.init_pos_x = init_pos_x
    
    def getLocX(self, time):
        return self.init_pos_x + self.init_vel_x * time
    
class ProjLocXY(ProjLocX, ProjLocY):
    def __init__(self, init_vel_x, init_pos_x, init_vel_y, init_pos_y):
        ProjLocX.__init__(self, init_vel_x, init_pos_x)
        ProjLocY.__init__(self, init_vel_y, init_pos_y)
        
    def evaluate(self, time):
        x = self.getLocX(time)
        y = self.getLocY(time)
        return (x, y)

proj = ProjLocXY(10, 0, 10, 0)
location = proj.evaluate(1)
print(location)


# ## Bonus Exercise: (30 points)
# If you invest a principal value of $P$ at time 0, and interest is continuously compounded at a rate $r$ (between 0 and 1), then the amount of money you would have after $t$ years is
# $$M(t) = Pe^{rt}.$$
# Fry has \\$0.01 in his bank account, but is accidentally transported 1,000 years into the future. He returns to his bank (which luckily still exists) to see how much money he now has. Assume Fry's account earns continuously compounded interest at a rate of 5\% (or $r=0.05$).
# 1. Create a numpy array of time from 0 to 1,000 years increasing by 1 year
# 1. Create a new numpy array that calculates how much money Fry's account has at each year
# 1. Plot Fry's money over the given timeframe
# 
# 
# Now if Fry only earned simple interest, the amount of money he would have after $t$ years would be
# $$ S(t) = P(1+rt).$$
# 
# 1. Perform the same procedure as steps 1-3 above assuming Fry earns 5\% simple interest.
# 1. To illustrate the difference, also plot $M(t)-S(t)$ over the timeframe.
# 1. What do you conclude?
# 
# *Aside:* This problem, while silly, should teach you an important lesson: invest your money as early as you possibly can!

# In[62]:


## Write your code here
import numpy as np
import matplotlib.pyplot as plt

# Set initial values
initial_balance = 0.01
interest_rate = 0.05

# Create array of time from 0 to 1000 years in increments of 1 year
time = np.arange(0, 1001, 1)

# Calculate the balance at each year using the formula for continuous compounding
balance = initial_balance * np.exp(interest_rate * time)

# Plot the results
plt.plot(time, balance)
plt.xlabel("Time (years)")
plt.ylabel("Balance ($)")
plt.title("Fry's Bank Account Balance over Time")
plt.show()


# In[65]:


import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create array of time from 0 to 1000 years
t = np.arange(0, 1001)

# Step 2: Calculate Fry's money at each year with simple interest
P = 0.01
r = 0.05
M = P * (1 + r * t)

# Step 3: Plot Fry's money over time
plt.plot(t, M)
plt.title("Fry's Money with Simple Interest")
plt.xlabel("Time (years)")
plt.ylabel("Amount ($)")
plt.show()

# Step 4: Plot difference between Fry's money with continuous vs. simple interest
plt.plot(t, balance - M)
plt.title("Difference between Fry's Money with Continuous vs. Simple Interest")
plt.xlabel("Time (years)")
plt.ylabel("Amount ($)")
plt.show()


# In[ ]:




