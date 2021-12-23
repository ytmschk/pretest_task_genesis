#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), 'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]}) 
df


# In[3]:


grouped_df = df.groupby("grps")


# In[4]:


maximum = grouped_df.max()


# In[5]:


maximum


# In[7]:


maximum

