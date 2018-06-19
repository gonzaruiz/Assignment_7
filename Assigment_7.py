
# coding: utf-8

# In[1]:


import numpy as np


# In[5]:


x = [3,5,7,2,8,10,11,65,72,81,99,100,150]
x


# In[6]:


n = len(x)
k = 3
r = n - k + 1 
r


# In[7]:


for z in range(r):
    promedio = np.average(x[z:z+k])
    print(promedio)

