#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[8]:


data = pd.read_csv('C://Users//aruni//Documents//Data//AAPL.csv')


# In[9]:


data.head()


# In[10]:


data.describe()


# In[11]:


data['12d_ema']= data["Adj. Close"].ewm(span=12).mean()


# In[12]:


data['26d_ema']= data["Adj. Close"].ewm(span=26).mean()


# In[13]:


data.describe()


# In[14]:


data['buy_signal']=0
data['sell_signal']=0


# In[15]:


data['MACD']=data['12d_ema']-data['26d_ema']


# In[16]:


data.describe()


# In[17]:


data['singal_line']= data['MACD'].ewm(span=9).mean()


# In[18]:


data.describe()


# In[24]:


data.loc[data['MACD']>data['singal_line'], 'buy_signal']=1


# In[21]:


data.loc[data['MACD']<data['singal_line'], 'sell_signal']=1


# In[22]:


print(data[['MACD','singal_line','buy_signal','sell_signal']])


# In[ ]:





# In[ ]:




