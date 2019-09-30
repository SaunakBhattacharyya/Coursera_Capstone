#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


df = pd.read_excel(r'C:\Users\U327390\OneDrive - Danfoss\Desktop\Python.xlsx') 
print (df)


# In[6]:


# Ranking of School Ratings descending order
df['School Ratings_Rank']=df['School Ratings'].rank(ascending=0)
df


# In[7]:


# Ranking of Housing Price Ratings ascending order
df['Housing Price Ratings']=df['Housing Price Ratings'].rank(ascending=1)
df


# In[8]:


col = df.loc[: , "Housing Price Ratings":"School Ratings_Rank"]
df['Ranking_avg'] = col.mean(axis=1)
df


# In[9]:


df.sort_values(by=['Ranking_avg'])


# In[ ]:




