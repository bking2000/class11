#!/usr/bin/env python
# coding: utf-8

# ## Script to calculate Basic Statistics

# ### Equation for the mean:   $\mu_x = \sum_{i=1}^{N}\frac{x_i}{N}$
# 
# ### Equation for the standard deviation:  $\sigma_x = \sqrt{\sum_{i=1}^{N}\left(x_i - \mu \right)^2}\frac{1}{N-1}$
# 
# 
# **Instructions:**
# 
# **(1) Before you write code, write an algorithm that describes the sequence of steps you will take to compute the mean and standard deviation for your samples.  The algorithm can be written in pseudocode or as an itemized list.***
# 
# **(2) Use 'for' loops to help yourself compute the average and standard deviation.**
# 
# **(3) Use for loops and conditional operators to count the number of samples within $1\sigma$ of the mean.**
# 
# **Note:** It is not acceptable to use the pre-programmed routines for mean and st. dev., e.g. numpy.mean()

# ### Edit this box to write an algorithm for computing the mean and std. deviation.
# 2.a) Mean:
# - Initialize a sum and count variable
# - For each element in the input list
#     - Increment count by 1
#     - Add that element's value to the sum
# - Divide sum by count
# - Return result
# 
# 2.b) Std Dev:
# - Compute average of the list as above
# - Initialize a sum and count variable
# - For each element in the input list
#     - Increment count by 1
#     - Compute (that element's value minus average) squared
#     - Add that result to the sum
# - Take square root of sum
# - Divide this by (count - 1)
# - Return result
# 
# 
# 
# 
# 
# 
# 

# ### Write your code using instructions in the cells below.

# In[1]:


# Put your Header information here.  Name, creation date, version, etc.

# Brendan King, 9/19/23, v1.0


# In[2]:


# Import the matplotlib module here.  No other modules should be used.
import matplotlib.pyplot as plt


# In[3]:


# Create a list variable that contains at least 25 elements.  You can create this list any number of ways.  
# This will be your sample.
x = [1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]


# In[4]:


# Pretend you do not know how long x is; compute it's length, N, without using functions or modules.
N = 0
for i in x:
    N+=1
print(N)


# In[5]:


# Compute the mean of the elements in list x.
sum1 = 0
count = 0
for i in x:
    count+=1
    sum1+=i
mu = sum1/count
print(mu)


# In[6]:


# Compute the std deviation, using the mean and the elements in list x.
sum2 = 0
count2 = 0
for i in x:
    count2+=1
    diff = (i-mu)**2
    sum2 += diff
sigma = (sum2**0.5)/(count2-1)
print(sigma)




# In[7]:


# Use the 'print' command to report the values of average (mu) and std. dev. (sigma).
print(mu)
print(sigma)



# In[8]:


# Count the number of values that are within +/- 1 std. deviation of the mean.  
# A normal distribution will have approx. 68% of the values within this range.  
# Based on this criteria is the list normally distributed?
upper = mu + sigma
lower = mu - sigma
count3 = 0
for i in x:
    if i < upper:
        if i > lower:
            count3 += 1
print(count3)



# In[9]:


# Use print() and if statements to report a message about whether the data is normally distributed.
if count3/N > 0.67:
    if count3/N < 0.69:
        print('Normally distributed')
else:
    print('Not normally distributed')
                
        



# In[10]:


### Use Matplotlb.pyplot to make a histogram of x.
plt.hist(x)



# ### OCG 593 students, look up an equation for Skewness and write code to compute the skewness. 
# #### Compute the skewness and report whether the sample is normally distributed.

# In[11]:


count4 = 0
diff2 = 0
sum4 = 0
for i in x:
    diff2 = (i-mu)**3
    sum4 += diff2
    count4 +=1
skew = sum4/((count4 - 1)*mu**3)
print(skew)

