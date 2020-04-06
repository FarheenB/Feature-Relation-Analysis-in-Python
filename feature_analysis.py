#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required packages
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import VarianceThreshold  


# In[2]:


#get flights dataset
flights_data = pd.read_csv('dataset/FlightDelays.csv')


# In[25]:


#get ontime flights

ontimeflights = flights_data[(flights_data["Flight_Status"] == "ontime") & (flights_data["ORIGIN"] == "DCA") & (flights_data["DEST"] == "JFK")]
ontimeflights.head()


# In[26]:


#no. of times a flight is delayed

sns.countplot(x="Weather",data=ontimeflights)
plt.show()

#ideal weather conditions for the highest chance of an ontime flight is 0


# In[29]:


#no. of times a flight is delayed

ontimeflights["DEP_TIME"].plot.hist(bins=50,figsize=(10,5))
plt.show()

#ideal DEP_TIME for the highest chance of an ontime flight lies between 3pm to 4pm


# In[30]:


#no. of times a flight is ontime

sns.countplot(x="DAY_OF_MONTH",data=ontimeflights)
plt.show()

#ideal day of the month when the highest chance of an ontime flight is 20


# In[31]:


#no. of times a flight is ontime

sns.countplot(x="CARRIER",data=ontimeflights)
plt.show()

#ideal carrier when the highest chance of an ontime flight is MQ


# In[ ]:




