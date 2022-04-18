#!/usr/bin/env python
# coding: utf-8

# In[1]:


#pandas assignment2


# In[2]:


import pandas as pd


# In[28]:


url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user'
users=pd.read_csv(url,index_col=[0],sep='|')
users


# In[29]:


users


# In[30]:


users.head(10)


# In[31]:


users.tail(10)


# In[32]:


#What is the number of observations in the dataset?
observations = len(users.axes[0])
observations


# In[33]:


#What is the number of columns in the dataset?
columns = len(users.axes[1])
columns


# In[34]:


#Print the name of all the columns.
users.columns


# In[35]:


#How is the dataset indexed?
users.index


# In[38]:


#What is the data type of each column?
users.info()


# In[39]:


#Print only the occupation column
users['occupation']


# In[40]:


#How many different occupations are in this dataset?
users['occupation'].nunique()


# In[41]:


#What is the most frequent occupation?
users['occupation'].mode()[0]


# In[42]:


#DataFrame Info.
users.info()


# In[44]:


#Describe all the columns
users.describe(include='all')


# In[52]:


#Summarize only the occupation column
users['occupation'].value_counts()


# In[53]:


#What is the mean age of users?
users['age'].mean()


# In[55]:


#What is the age with least occurrence?
users['occupation'].value_counts().min()


# In[ ]:




