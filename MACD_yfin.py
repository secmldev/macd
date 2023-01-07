#!/usr/bin/env python
# coding: utf-8

# In[19]:


import pandas_datareader as web
import pandas as pd
import matplotlib.pyplot as plt


# In[20]:


pip install yfinance


# In[21]:


from pandas_datareader import data as pdr
import yfinance as yfin
yfin.pdr_override()


# In[22]:


from pandas_datareader import data as pdr
mkt = pdr.get_data_yahoo('SPY',start="2022-01-1",end="2022-12-31")


# In[14]:


mkt


# In[31]:


mkt['12dema']=mkt['Adj Close'].ewm(span=12).mean()
mkt['26dema']=mkt['Adj Close'].ewm(span=26).mean()
mkt['MACD']=mkt['12dema']-mkt['26dema']
mkt['signal']=mkt['MACD'].ewm(span=26).mean()
mkt.describe()


# In[32]:


plt.plot(mkt['MACD'])
plt.plot(mkt['signal'])
         
plt.show()


# In[33]:


mkt['buy_signal']=0
mkt['sell_signal']=0


# In[35]:


mkt.loc[mkt['MACD']>mkt['signal'], 'buy_signal']=1
mkt.loc[mkt['MACD']<mkt['signal'], 'sell_signal']=1


# In[41]:


print(mkt[['MACD','buy_signal','sell_signal']])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




